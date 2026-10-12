#!/usr/bin/env python3

"""
Runs checks on article meta block and outputs in github action readable format
"""

__author__ = "cal w"

import re
import sys
import yaml
import os
import time
import traceback
from titlecase import titlecase
from pathlib import Path
from difflib import get_close_matches

# Ignore files if they match this regex
EXCLUDED_FROM_CHECKS = [
    r"docs/assets/.*",
    r".*/index\.md",
    r".*\.yml"
]

msg_count = {"debug": 0, "notice": 0, "warning": 0, "error": 0}

# Constants for use in checks.

MAX_TITLE_LENGTH = 28  # As font isn't monospace, this is only approx
MAX_HEADER_LENGTH = 32  # minus 2 per header level, so h2: 28, h3: 26
MAX_CODE_LINE_LENGTH = 80  # Approx monospace chars visible in a top level code block at 1280-1920px wide
CODE_ADMONITION_EXTRA = 5  # Admonitions use a smaller font, so fit more (85-94 chars)
CODE_LIST_LESS = 3  # Each level of list indent costs ~3 chars
RANGE_SECTION_CHARS = [ 400, 3200 ] # Mirrors nesi-docs-rag's scripts/chunker.mjs MIN_CHARS/MAX_CHARS
RANGE_TAGS = [1, 5]
# Below this, descriptions stop distinguishing pages ("Release notes", "Freezer Quick
# Start", eleven Freezer pages all sharing "Freezer upgrade release notes"). Descriptions
# in the low 30s are still doing real work, so don't raise this without checking.
MIN_DESCRIPTION_LENGTH = 30
RANGE_SIBLING = [4, 8]
ALLOWED_BE_BIG = ["Available_Applications"] # Categories not to trigger too many children warnings.
# Site-infrastructure pages (tag index, updates feed, glossary) have no topic of their
# own to tag - forcing a tag on them would just be generic filler, which tags.yml's
# vocabulary explicitly discourages (see its "RETIRED TAGS" section).
NO_TAGS_REQUIRED = ["docs/tags.md", "docs/updates.md", "docs/GLOSSARY.md"]
DOC_ROOT = "docs"
TAGS_VOCAB_PATH = "docs/assets/tags.yml"


def _load_tag_aliases(vocab):
    """Lower-cased alias (or mis-cased canonical tag) -> canonical tag, matched the same way as compile_tags.py."""
    aliases = {}
    for canonical, entry in vocab.items():
        aliases[canonical.lower()] = canonical
        for alias in (entry.get("aliases") or []):
            aliases[str(alias).lower()] = canonical
    return aliases


# Material's admonition types and their aliases, plus the custom ones styled in our stylesheets.
MATERIAL_ADMONITION_TYPES = {
    "note", "abstract", "summary", "tldr", "info", "todo", "tip", "hint", "important", "success", "check",
    "done", "question", "help", "faq", "warning", "caution", "attention", "failure", "fail", "missing",
    "danger", "error", "bug", "example", "quote", "cite",
}
ADMONITION_TYPES = MATERIAL_ADMONITION_TYPES | {
    m.lower()
    for css in Path(DOC_ROOT, "assets", "stylesheets").glob("*.css")
    for m in re.findall(r"\.admonition\.([\w-]+)", css.read_text())
}
# Used title-only by design (eg. '!!! time "45 Minutes"' in tutorials), so no body is expected.
TITLE_ONLY_ADMONITION_TYPES = {"time"}
# Opener syntax from python-markdown's admonition.py and pymdownx's details.py and tabbed.py, applied to a stripped line.
BLOCK_OPENERS = {
    "!!!": re.compile(r'^!!! ?[\w\-]+(?: +[\w\-]+)*(?: +".*?")? *$'),
    "???": re.compile(r'^\?{3}\+? ?(?:(?:[\w\-]+(?: +[\w\-]+)*?)?(?: +".*?")|[\w\-]+(?: +[\w\-]+)*?) *$'),
    "===": re.compile(r'^={3}(?:\+|\+!|!\+|!)? +".*?" *$'),
}

TAGS_VOCAB = yaml.safe_load(Path(TAGS_VOCAB_PATH).read_text())
CANONICAL_TAGS = set(TAGS_VOCAB)
TAG_ALIASES = _load_tag_aliases(TAGS_VOCAB)


# Warning level for missing parameters.
EXPECTED_PARAMETERS = {
    "title": "",
    "template": ["main.html", "supported_apps.html", "updates.html"],
    "description": "",
    "icon": "",
    "status": ["new", "deprecated", "tutorial"],
    "prereq": "",
    "postreq": "",
    "suggested": "",  # Add info here when implimented.
    "created_at": "",
    "tags": "",  # Values are checked by approved_tags().
    "search": "",
    "hide": ["toc", "nav", "tags"],
    "no_module": [True, False],
}


def main():
    # Per file variables
    global input_path, title_from_filename, title, meta, contents, crashed_checks

    # Walk variables
    global lineno, line, in_code_block, toc, toc_parents, nav_tree_failed

    # code_line_length variables
    global code_fence_indent, code_containers, code_line_limit, code_line_where

    for input_string in sys.argv[1:]:
        input_path = Path(input_string)
        lineno = 1
        if any(re.match(pattern, input_string) for pattern in EXCLUDED_FROM_CHECKS):
            continue
        if not input_path.is_file():
            _emit("misc", {"message": "File not found, skipping. (Deleted in this change?)"})
            continue
        _nav_check()
        _emit("", {"level": "debug", "message": f"Checking meta for {input_path}"})
        contents = input_path.read_text()

        match = re.match(r"---\n([\s\S]*?)---", contents, re.MULTILINE)
        if not match:
            _emit("meta.parse", {"line": 1, "message": "Meta block missing or malformed."})
            meta = {}
        else:
            try:
                meta = yaml.safe_load(match.group(1)) or {}
            except yaml.YAMLError as e:
                # Only blocking error, mkdocs silently ignores front matter it can't parse.
                _emit("meta.parse", {"level": "error", "line": 1, "message": "Front matter is not valid YAML. " + " ".join(str(e).split())})
                continue

        title_from_filename = _title_from_filename()
        title = meta.get("title") or title_from_filename
        crashed_checks = set()

        lineno = 0
        in_code_block = False
        toc_parents = [(title, 1)]
        toc = {title: {"level": 1, "lineno": 0, "children": {}}}
        nav_tree_failed = False

        code_fence_indent = 0
        code_containers = []
        code_line_limit = MAX_CODE_LINE_LENGTH
        code_line_where = ""

        for line in contents.split("\n"):
            lineno += 1
            if re.match(r"^\s*```", line):
                in_code_block = not in_code_block
            _get_nav_tree()
            for check in WALKCHECKS:
                _run_check(check)
        for check in ENDCHECKS:
            _run_check(check)


def _run_check(f):
    """Runs a check, a check that crashes is reported once per file and skipped, the others still run."""
    if f.__name__ in crashed_checks:
        return
    try:
        for r in f():
            _emit(f.__name__, r)
    except Exception as e:
        crashed_checks.add(f.__name__)
        traceback.print_exc(file=sys.stderr)
        _emit(f.__name__, {"line": lineno, "message": f"Check '{f.__name__}' crashed ({type(e).__name__}: {e}), \
it was skipped for the rest of this file."})


def _emit(f, r):
    msg_count[r.get("level", "warning")] += 1
    # Trailing "path:line:col" is redundant with the file=/line=/col= fields above, but
    # terminals (eg. VS Code's integrated terminal) auto-link that exact shape, letting you
    # click straight to the location without going through the task's Problems panel.
    location = f"{input_path}:{r.get('line', 1)}:{r.get('col', 0)}"
    print(
        f"::{r.get('level', 'warning')} file= {input_path},title={f},col={r.get('col', 0)},\
endColumn={r.get('endColumn', 99)},line={r.get('line', 1)}::{r.get('message', 'something wrong')} ({location})"
    )
    sys.stdout.flush()
    time.sleep(0.01)


def _title_from_filename():
    """
    Matches mkdocs' own Page.title fallback (mkdocs/structure/pages.py):
    replace '-'/'_' with spaces, then capitalize only if the whole
    filename was already lowercase - mixed-case names are left as-is.
    """
    name = input_path.name[0:-3].replace("-", " ").replace("_", " ")
    if name.lower() == name:
        name = name.capitalize()
    return name


def _get_lineno(pattern):
    """Line number of the first line matching pattern, or 1 if none do."""
    for i, l in enumerate(contents.split("\n"), start=1):
        if re.match(pattern, l):
            return i
    return 1


def _did_you_mean(word, options):
    """Closest option to word, or None if nothing is close enough to be worth suggesting."""
    match = get_close_matches(str(word), sorted(options), n=1, cutoff=0.6)
    return match[0] if match else None


def _get_nav_tree():
    """
    Makes a nice dictionary of header tree.
    toc_parents is the stack of (name, level) headers enclosing the current line, so a skipped level
    (### straight after ##, or no ## at all) still nests under the nearest header above it.
    """
    global toc, toc_parents, nav_tree_failed

    def _unpack(toc, a):
        if len(a) < 1:
            return toc
        if len(a) < 2:
            return toc[a[0]]
        return _unpack(toc[a[0]]["children"], a[1:])
    try:
        if in_code_block:
            return

        header_match = re.match(r"^(#+)\s*(.*)$", line)

        if not header_match:
            return

        header_level = len(header_match.group(1))
        header_name = header_match.group(2)

        if header_level == 1:
            toc = {header_name: {"lineno": lineno, "children": {}}}
            toc_parents = [(header_name, 1)]
            return

        while toc_parents[-1][1] >= header_level:
            toc_parents.pop(-1)

        _unpack(toc, [name for name, _ in toc_parents])["children"][header_name] = {
            "level": header_level,
            "lineno": lineno,
            "children": {},
        }
        toc_parents.append((header_name, header_level))
    except Exception:
        if not nav_tree_failed:
            nav_tree_failed = True
            _emit("misc.nav", {"line": lineno, "message": "Failed to parse Nav tree. Something is very wrong."})


def _nav_check():
    try:
        doc_root = Path(DOC_ROOT).resolve()
        rel_path = input_path.resolve().relative_to(doc_root)
        for i in range(1, len(rel_path.parts)):
            category = rel_path.parts[i - 1]
            num_siblings = 0
            for file_name in os.listdir(doc_root.joinpath(Path(*rel_path.parts[:i]))):
                if not any(
                    re.match(pattern, file_name) for pattern in EXCLUDED_FROM_CHECKS
                ):
                    num_siblings += 1
            if num_siblings < RANGE_SIBLING[0]:
                _emit(
                    "meta.siblings",
                    {
                        "level": "notice",
                        "message": f"Parent category '{category}' has too few children ({num_siblings}). \
Try to nest '{RANGE_SIBLING[0]}' or more items here to justify its existence.",
                    },
                )
            elif num_siblings > RANGE_SIBLING[1] and category not in ALLOWED_BE_BIG:
                _emit(
                    "meta.siblings",
                    {
                        "level": "notice",
                        "message": f"Parent category '{category}' has too many children ({num_siblings}). \
Try to keep number of items in a category under '{RANGE_SIBLING[1]}', maybe add some new categories?",
                    },
                )
    except ValueError as e:
        _emit("meta.nav", {"message": f"{e}. Nav checks will be skipped"})


def title_redundant():
    # A page's title doubles as the applications[] lookup key (see app_header.html);
    # keep it explicit so a future filename change can't silently break that lookup.
    if "Available_Applications" in input_path.parts:
        return
    if meta.get("title") == title_from_filename:
        yield {
            "level": "notice",
            "line": _get_lineno(r"^title:.*$"),
            "message": "Title set in meta is redundant as it is already set in filename.",
        }


def meta_unexpected_key():
    """
    Check for unexpected keys.
    """

    def _test(v):
        if v not in EXPECTED_PARAMETERS[key]:
            yield {
                "level": "warning",
                "line": _get_lineno(f"^{re.escape(key)}:.*$"),
                "message": f"'{v}' is not valid for {key}. [{','.join(str(x) for x in EXPECTED_PARAMETERS[key])}]",
            }

    for key, value in meta.items():
        if key not in EXPECTED_PARAMETERS:
            similar = _did_you_mean(key, EXPECTED_PARAMETERS)
            yield {
                "line": _get_lineno(f"^{re.escape(str(key))}:.*$"),
                "message": f"Unexpected parameter in front-matter '{key}'" + (f", did you mean '{similar}'?" if similar else "."),
            }
        elif EXPECTED_PARAMETERS[key]:
            if isinstance(value, list):
                for v in value:
                    yield from _test(v)
            else:
                yield from _test(value)


def meta_missing_description():
    if not meta.get("description"):
        yield {"message": "Missing 'description' from front matter."}


def meta_thin_description():
    """
    A description that just restates the title carries no information. These descriptions
    are what each llms.txt link is annotated with (see mkdocs_hooks.on_config), so a reader
    picking between pages has only this line to go on - 'Guide to batch computing' on
    Batch_Computing_Guide.md tells them nothing the title didn't.
    """
    description = meta.get("description")
    if not isinstance(description, str):
        return
    description = " ".join(description.split())
    if not description:
        return
    lineno = _get_lineno(r"^description:.*$")
    if len(description) < MIN_DESCRIPTION_LENGTH:
        yield {
            "level": "notice",
            "line": lineno,
            "message": f"Description '{description}' is too short to tell pages apart. \
Aim for at least {MIN_DESCRIPTION_LENGTH} characters saying what the page answers.",
        }
    elif title and _squash(description) == _squash(title):
        yield {
            "level": "notice",
            "line": lineno,
            "message": f"Description '{description}' just restates the title. \
Say what the page answers instead.",
        }


def _squash(text):
    """Lowercase and strip everything but letters and digits, for comparing phrasings."""
    return re.sub(r"[^a-z0-9]", "", text.lower())


def title_length():
    if len(title) > MAX_TITLE_LENGTH:
        yield {
            "level": "notice",
            "line": _get_lineno(r"^title:.*$"),
            "message": f"Title '{title}' is too long. \
Try to keep it under {MAX_TITLE_LENGTH} characters to avoid word wrapping in the nav.",
        }

def title_capitalisation():
    # Software names are often acronyms/proper nouns (BLAST, VASP, ont-guppy-gpu) that
    # titlecase() mangles, and the mangled title breaks the applications[app_name]
    # macro lookup on Available_Applications pages (a KeyError, not just a cosmetic typo).
    if "Available_Applications" in input_path.parts:
        return
    correct_title = titlecase(title)
    if title != correct_title:
        yield {
            "level": "notice",
            "line": _get_lineno(r"^title:.*$"),
            "message": f"Title '{title}' uses incorrect capitalisation. \
'{correct_title}' is preferred",
        }

def number_tags():
    if str(input_path) in NO_TAGS_REQUIRED or (meta.get("search") or {}).get("exclude"):
        return
    if "tags" not in meta or not isinstance(meta["tags"], list):
        yield {"message": "'tags' property in meta is missing or malformed."}
    elif len(meta["tags"]) < RANGE_TAGS[0]:
        yield {
            "line": _get_lineno(r"^tags:.*$"),
            "message": f"Try to include at least {RANGE_TAGS[0]} 'tags' (helps with search optimisation).",
        }
    elif len(meta["tags"]) > RANGE_TAGS[1]:
        yield {
            "line": _get_lineno(r"^tags:.*$"),
            "message": f"{len(meta['tags'])} is a lot of 'tags', are you sure they are all useful?",
        }

def approved_tags():
    if "tags" not in meta or not isinstance(meta["tags"], list):
        return
    for tag in meta["tags"]:
        if tag in CANONICAL_TAGS:
            continue
        tag_lineno = _get_lineno(rf"^\s*-\s*['\"]?{re.escape(str(tag))}['\"]?\s*$")
        if str(tag).lower() in TAG_ALIASES:
            canonical = TAG_ALIASES[str(tag).lower()]
            yield {
                "line": tag_lineno,
                "message": f"Tag '{tag}' is an alias, use the canonical tag '{canonical}' instead. \
('python3 normalize_tags.py' can fix this.)",
            }
        else:
            similar = _did_you_mean(tag, CANONICAL_TAGS)
            yield {
                "line": tag_lineno,
                "message": f"Tag '{tag}' is not an approved tag, "
                + (f"did you mean '{similar}'?" if similar else f"see '{TAGS_VOCAB_PATH}'."),
            }

def h1_in_body():
    """
    H1 is reserved for the page title (see FORMAT.md/styleguide.md): it's set
    via front matter or the filename, and a literal '# ...' in the body
    silently overrides the nav title too.
    """
    if in_code_block:
        return

    m = re.match(r"^#\s+(.*)$", line)
    if m:
        yield {
            "line": lineno,
            "message": f"Don't use H1 ('# {m.group(1)}') in the body, it's reserved for the \
page title and overrides the nav title. Remove it (or set 'title' in front matter instead).",
        }


def click_here():
    """
    Click [here](for more details)
    """
    if in_code_block:
        return

    m1 = re.search(r"\[[^\]]*\bhere\b[^\]]*\]\([^)]*\)", line, re.IGNORECASE)
    if m1:
        yield {
            "line": lineno,
            "col": m1.start() + 1,
            "endColumn": m1.end() - 1,
            "message": "Don't use 'here' for link text, impedes accessibility.",
        }

    # Impliment check for html links when I can be fd.
    # m2 = re.search(r"\[here\]\(.*\)", line)


def absolute_site_link():
    """
    Checks for markdown links that point to this site by absolute URL
    instead of using a relative link.
    """
    if in_code_block:
        return

    for m in re.finditer(
        r"\[[^\]]*\]\((https?:\/\/)?docs\.nesi\.org\.nz(/[^)\s]*)?\)",
        line,
        re.IGNORECASE,
    ):
        yield {
            "line": lineno,
            "col": m.start() + 1,
            "endColumn": m.end() - 1,
            "message": "Don't use an absolute URL to link to a page on this site. Use a link relative to \
this page's own location instead (e.g. './Page.md' or '../Other_Section/Page.md'), not a path relative to the \
site root or to the linked page.",
        }


def support_mailto_link():
    """
    Checks for any mention of support@nesi.org.nz - as a markdown/HTML link,
    an autolink, or just raw text - these should use the
    'partials/support_request.html' include instead.
    """
    if in_code_block:
        return

    for m in re.finditer(
        r"(\[[^\]]*\]\((mailto:)?support@nesi\.org\.nz[^)]*\)"
        r"|<a\s[^>]*href=[\"'](mailto:)?support@nesi\.org\.nz[^>]*>"
        r"|<(mailto:)?support@nesi\.org\.nz>"
        r"|(mailto:)?support@nesi\.org\.nz)",
        line,
        re.IGNORECASE,
    ):
        yield {
            "line": lineno,
            "col": m.start() + 1,
            "endColumn": m.end() - 1,
            "message": 'Don\'t reference support@nesi.org.nz directly, use the \
{% include "partials/support_request.html" %} macro instead.',
        }


def code_line_length():
    """
    Checks for code block lines too long to fit in the block, which force the reader to scroll sideways.
    Length is counted from the fence's indent. The limit depends on what the block is nested in,
    tracked as a stack of (kind, body indent) for the admonitions, tabs and list items enclosing the line.
    """
    global code_fence_indent, code_containers, code_line_limit, code_line_where

    expanded = line.expandtabs(4)
    indent = len(expanded) - len(expanded.lstrip())
    m = re.match(r"^\s*```", line)

    if not in_code_block or m:
        if expanded.strip():
            # A line indented less than a container's body closes that container.
            code_containers = [c for c in code_containers if c[1] <= indent]
        opener = re.match(r"^\s*(?:(?:!!!|\?\?\?\+?)\s|===\s)", expanded)
        item = re.match(r"^\s*([-*+]|\d+[.)])\s+", expanded)
        if opener:
            kind = "tab" if opener.group(0).strip() == "===" else "admonition"
            code_containers.append((kind, indent + 4))
        elif item and not m:
            code_containers.append(("list", item.end()))
        if m and in_code_block:
            # Opening fence, work out the limit for this block.
            code_fence_indent = indent
            kinds = [c[0] for c in code_containers]
            code_line_limit = (
                MAX_CODE_LINE_LENGTH
                + (CODE_ADMONITION_EXTRA if "admonition" in kinds else 0)
                - CODE_LIST_LESS * kinds.count("list")
            )
            names = {"admonition": "an admonition", "list": "a list"}
            code_line_where = " and ".join(names[k] for k in dict.fromkeys(kinds) if k in names)
        return

    length = len(expanded[code_fence_indent:].rstrip())
    if length > code_line_limit:
        where = f" in {code_line_where}" if code_line_where else ""
        yield {
            "line": lineno,
            "col": code_fence_indent + code_line_limit + 1,
            "endColumn": code_fence_indent + length,
            "message": f"Code line is {length} characters long, so it will scroll sideways. Code blocks{where} \
fit about {code_line_limit} characters.",
        }


def walk_toc():
    """
    Checks if toc is sensible.
    """

    def _count_children(d):
        only_child = len(d["children"]) == 1
        for title, c in d["children"].items():
            if only_child:
                yield {
                    "level": "notice",
                    "line": c["lineno"],
                    "message": f"Header '{title}' is a useless only-child. Give it siblings or remove it.",
                }
            # As header gets deeper nested, it will have less horizontal room in toc.
            limit = MAX_HEADER_LENGTH - (2 * c["level"])
            if len(title) > limit:
                yield {
                    "level": "notice",
                    "line": c["lineno"],
                    "message": f"Header '{title}' is too long. \
Try to keep h{c['level']} headers under {limit} characters to avoid word wrapping in the toc.",
                }
            yield from _count_children(c)

    for d in toc.values():
        yield from _count_children(d)


def section_length():
    """
    Flags h2/h3 sections outside the band the RAG chunker merges/splits at.
    """
    lines = contents.split("\n")
    headers = []  # (lineno, name)
    in_code = False
    for i, l in enumerate(lines, start=1):
        if re.match(r"^\s*```", l):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^#{2,3}\s+(.*)$", l)
        if m:
            headers.append((i, m.group(1)))

    for idx, (start, name) in enumerate(headers):
        end = headers[idx + 1][0] - 1 if idx + 1 < len(headers) else len(lines)
        length = len("\n".join(lines[start:end]))
        if length < RANGE_SECTION_CHARS[0]:
            yield {
                "level": "notice",
                "line": start,
                "message": f"Section '{name}' is only ~{length} chars. \
Sections under {RANGE_SECTION_CHARS[0]} will be lumped into the next section when parsed by the RAG.",
            }
        elif length > RANGE_SECTION_CHARS[1]:
            yield {
                "line": start,
                "message": f"Section '{name}' is ~{length} chars. \
Sections over {RANGE_SECTION_CHARS[1]} are too long to be meaningfully parsed by the RAG. \
Consider breaking this into sub-headers.",
            }


def admonition_structure():
    """
    Checks admonitions (!!!), collapsible blocks (???) and content tabs (===) are well-formed.
    These aren't CommonMark, so markdownlint can't see them, and a broken one renders without any build warning.
    """
    opener = line.expandtabs(4).strip()
    # '===' alone is a setext header underline, not a tab.
    if in_code_block or opener[:3] not in BLOCK_OPENERS or not opener.strip("="):
        return
    name = "Content tab" if opener[:3] == "===" else "Admonition"
    if not BLOCK_OPENERS[opener[:3]].match(opener):
        yield {"line": lineno, "message": f"{name} opener '{opener}' is malformed, so it renders as plain text."}
        return

    m = re.match(r"^(?:!!!|\?{3}\+?) ?([\w-]+)", opener)
    kind = m.group(1).lower() if m else ""  # No type for tabs, or '??? "Title"'.
    if kind and kind not in ADMONITION_TYPES:
        suggestion = _did_you_mean(kind, ADMONITION_TYPES)
        yield {
            "line": lineno,
            "message": f"Admonition type '{kind}' has no style, so it renders as a plain grey box."
            + (f" Did you mean '{suggestion}'?" if suggestion else "")
            + " Types are listed in FORMAT.md.",
        }

    # The body is the next non-blank line, and must be indented 4 more than the opener.
    indent = len(line.expandtabs(4)) - len(line.expandtabs(4).lstrip())
    rest = contents.split("\n")[lineno:]
    body_lineno, body = next(((i, l.expandtabs(4)) for i, l in enumerate(rest, lineno + 1) if l.strip()), (lineno, ""))
    body_indent = len(body) - len(body.lstrip())
    if body_indent >= indent + 4:
        return
    if body_indent > indent:
        yield {
            "line": body_lineno,
            "message": f"{name} body is indented {body_indent - indent} spaces, it needs 4 more than the opener \
(line {lineno}). As it is, the {name.lower()} renders empty and this text falls out below it.",
        }
    elif name == "Content tab":
        yield {"line": lineno, "message": "Content tab is empty. Indent its contents 4 spaces."}
    elif kind not in TITLE_ONLY_ADMONITION_TYPES:
        yield {
            "level": "notice",
            "line": lineno,
            "message": "Admonition has a title but no body. If it should have contents, indent them 4 spaces.",
        }


def dynamic_slurm_link():
    """
    Checks if slurm links point to right version of docs.
    """
    m1 = re.search(
        r".*\(https?:\/\/slurm.schedmd.com(?!\/archive\/{{\s*config\.extra\.slurm\s*}})(.*)\/(.*)\)",
        line,
        re.IGNORECASE,
    )
    if m1:
        yield {
            "line": lineno,
            "message": f"Link '{m1.group(0)}', does not use dynamic slurm version. Use 'https://slurm.schedmd.com/archive/{{{{ config.extra.slurm }}}}/{m1.group(2)}",
        }


# Define checks here
# For checks to run on page as a whole
ENDCHECKS = [
    title_redundant,
    title_length,
    title_capitalisation,
    meta_missing_description,
    meta_thin_description,
    meta_unexpected_key,
    number_tags,
    approved_tags,
    walk_toc,
    section_length,
]

# Checks to be run on each line
WALKCHECKS = [click_here, dynamic_slurm_link, absolute_site_link, support_mailto_link, h1_in_body, code_line_length,
              admonition_structure]

if __name__ == "__main__":
    main()

    # FIXME terrible hack to make VSCode in codespace capture the error messages
    # see https://github.com/microsoft/vscode/issues/92868 as a tentative explanation
    time.sleep(1)

    # Only unparseable front matter is an error.
    if msg_count["error"]:
        sys.exit(1)
    # CHECKS_STRICT=1: also exit non-zero on warnings.
    if os.getenv("CHECKS_STRICT") and msg_count["warning"]:
        sys.exit(1)
