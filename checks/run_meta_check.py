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
from titlecase import titlecase
from pathlib import Path

# Ignore files if they match this regex
EXCLUDED_FROM_CHECKS = [
    r"docs/assets/.*",
    r".*/index\.html",
    r".*/index\.md",
    r".*\.pages\.yml",
    r".*\.yml"
]

msg_count = {"debug": 0, "notice": 0, "warning": 0, "error": 0}

# Constants for use in checks.

MAX_TITLE_LENGTH = 28  # As font isn't monospace, this is only approx
MAX_HEADER_LENGTH = 32  # minus 2 per extra header level
MIN_TAGS = 1
RANGE_SIBLING = [4, 8]
ALLOWED_BE_BIG = ["Available_Applications"] # Categories not to trigger too many children warnings.
# Site-infrastructure pages (tag index, updates feed, glossary) have no topic of their
# own to tag - forcing a tag on them would just be generic filler, which tags.yml's
# vocabulary explicitly discourages (see its "RETIRED TAGS" section).
NO_TAGS_REQUIRED = ["docs/tags.md", "docs/updates.md", "docs/GLOSSARY.md"]
DOC_ROOT = "docs"

# Warning level for missing parameters.
EXPECTED_PARAMETERS = {
    "title": "",
    "template": ["main.html", "supported_apps.html", "updates.html"],
    "description": "",
    "icon": "",
    "status": ["new", "deprecated"],
    "prereq": "",
    "postreq": "",
    "suggested": "",  # Add info here when implimented.
    "created_at": "",
    "tags": "",  # Add info here when implimented.
    "search": "",
    "hide": ["toc", "nav", "tags"],
    "no_module": [True, False],
}


def main():
    # Per file variables
    global \
        input_path, \
        title_from_h1, \
        title_from_filename, \
        title, \
        meta, \
        contents, \
        input_path

    # Walk variables
    global \
        lineno, \
        line, \
        in_code_block, \
        last_header_level, \
        last_header_lineno, \
        sibling_headers

    global toc, toc_parents, header, nav_tree_failed

    inputs = sys.argv[1:]

    for input_string in inputs:
        input_path = Path(input_string)
        if any(re.match(pattern, input_string) for pattern in EXCLUDED_FROM_CHECKS):
            continue
        _nav_check()
        with open(input_path, "r") as f:
            _emit(
                "",
                {
                    "level": "debug",
                    "file": input_path,
                    "message": f"Checking meta for {f.name}",
                },
            )
            try:
                contents = f.read()
                match = re.match(r"---\n([\s\S]*?)---", contents, re.MULTILINE)
                if not match:
                    _emit(
                        "meta.parse",
                        {
                            "file": input_path,
                            "col": 0,
                            "endColumn": 99,
                            "line": 1,
                            "message": "Meta block missing or malformed.",
                        },
                    )
                    meta = {}
                else:
                    meta = yaml.safe_load(match.group(1))

                title_from_filename = _title_from_filename()
                title_from_h1 = _title_from_h1()
                title = (
                    meta["title"]
                    if "title" in meta
                    else "" or title_from_h1 or title_from_filename
                )
                # global lineno, line, in_code_block, last_header_level, last_header_lineno, sibling_headers

                header = ""
                lineno = 0
                in_code_block = False
                toc_parents = [title]
                toc = {title: {"level": 1, "lineno": 0, "children": {}}}
                nav_tree_failed = False

                for line in contents.split("\n"):
                    lineno += 1
                    in_code_block = (
                            not in_code_block
                            if re.match(r"^\s*```.*$", line)
                            else in_code_block
                        )
                    for check in WALKCHECKS:

                        _get_nav_tree()
                        _run_check(check)
                for check in ENDCHECKS:
                    _run_check(check)
            except Exception as e:
                _emit("misc", {"level": "error", "file": input_path, "message": e})


def _run_check(f):
    for r in f():
        _emit(f.__name__, r)


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


def _title_from_h1():
    m = re.search(r"^ #(\S*)$", contents, flags=re.MULTILINE)
    return m.group(1) if m else ""


def _get_lineno(pattern):
    i = 1
    for line in contents.split("\n"):
        m = re.match(pattern, line)
        if m:
            return i
        i += 1
    return i


def _get_nav_tree():
    """Makes a nice dictionary of header tree"""
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
            toc_parents = [header_name]
            return

        while header_level < len(toc_parents) + 1:
            toc_parents.pop(-1)

        _unpack(toc, toc_parents)["children"][header_name] = {
            "level": header_level,
            "lineno": lineno,
            "children": {},
        }
        toc_parents += [header_name]
    except Exception:
        if not nav_tree_failed:
            nav_tree_failed = True
            _emit(
                "misc.nav",
                {
                    "level": "error",
                    "file": input_path,
                    "message": "Failed to parse Nav tree. Something is very wrong.",
                },
            )


def _nav_check():
    try:
        doc_root = Path(DOC_ROOT).resolve()
        rel_path = input_path.resolve().relative_to(doc_root)
        for i in range(1, len(rel_path.parts)):
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
                        "file": input_path,
                        "message": f"Parent category \
    '{rel_path.parts[i - 1]}' has too few children ({num_siblings}). Try to nest '{RANGE_SIBLING[0]}' or more \
    items here to justify it's existence.",
                    },
                )
            elif num_siblings > RANGE_SIBLING[1] and file_name not in ALLOWED_BE_BIG:
                _emit(
                    "meta.siblings",
                    {
                        "file": input_path,
                        "message": f"Parent category \
    '{rel_path.parts[i - 1]}' has too many children ({num_siblings}). Try to keep number of items in a category \
    under '{RANGE_SIBLING[1]}', maybe add some new categories?",
                    },
                )
    except ValueError as e:
        _emit(
            "meta.nav",
            {
                "file": input_path,
                "level": "error",
                "message": f"{e}. Nav checks will be skipped",
            },
        )


def title_redundant():
    # A page's title doubles as the applications[] lookup key (see app_header.html);
    # keep it explicit so a future filename change can't silently break that lookup.
    if "Available_Applications" in input_path.parts:
        return
    lineno = _get_lineno(r"^title:.*$")
    if "title" in meta.keys() and title_from_filename == meta["title"]:
        yield {
            "level": "notice",
            "line": lineno,
            "message": "Title set in meta is redundant as it is already set in filename.",
        }
    if "title" in meta.keys() and title_from_h1 == meta["title"]:
        yield {
            "level": "notice",
            "line": lineno,
            "message": "Title set in h1 is redundant as it is already set in filename.",
        }
    if title_from_filename == title_from_h1:
        yield {
            "level": "notice",
            "line": lineno,
            "message": "Title set in meta is redundant as it is already set in h1.",
        }


def meta_unexpected_key():
    """
    Check for unexpected keys.
    """

    def _test(v):
        if v not in EXPECTED_PARAMETERS[key]:
            yield {
                "level": "error",
                "line": _get_lineno(f"^{key}:.*$"),
                "message": f"'{value}' is not valid for {key}. [{','.join(EXPECTED_PARAMETERS[key])}]",
            }

    for key, value in meta.items():
        if key not in EXPECTED_PARAMETERS.keys():
            yield {
                "line": _get_lineno(r"^" + key + r":.*$"),
                "message": f"Unexpected parameter in front-matter '{key}'",
            }
        elif EXPECTED_PARAMETERS[key]:
            if isinstance(value, list):
                for v in value:
                    _test(v)
            else:
                _test(value)


def meta_missing_description():
    if not meta.get("description"):
        yield {"message": "Missing 'description' from front matter."}


def title_length():
    if len(title) > MAX_TITLE_LENGTH:
        yield {
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
            "line": _get_lineno(r"^title:.*$"),
            "message": f"Title '{title}' uses incorrect capitalisation. \
'{correct_title}' is preferred",
        }

def minimum_tags():
    if str(input_path) in NO_TAGS_REQUIRED or (meta.get("search") or {}).get("exclude"):
        return
    if "tags" not in meta or not isinstance(meta["tags"], list):
        yield {"message": "'tags' property in meta is missing or malformed."}
    elif len(meta["tags"]) < MIN_TAGS:
        yield {
            "line": _get_lineno(r"^tags:.*$"),
            "message": "Try to include at least 2 'tags'\
(helps with search optimisation).",
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


def walk_toc():
    """
    Checks if toc is sensible.
    """

    def _count_children(d):
        only_child = len(d["children"]) == 1
        for title, c in d["children"].items():
            if only_child:
                yield {
                    "line": c["lineno"],
                    "message": f"Header '{title}' is a useless only-child. Give it siblings or remove it.",
                }
            # As header gets deeper nested, it will have less horizontal room in toc.
            if len(title) > (MAX_HEADER_LENGTH - (2 * c["level"])):
                yield {
                    "line": c["lineno"],
                    "message": f"Header '{title}' is too long. \
 Try to keep it under {MAX_HEADER_LENGTH} characters to avoid word wrapping in the toc.",
                }
            for y in _count_children(c):
                yield y

    for d in toc.values():
        for y in _count_children(d):
            yield y


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
    meta_unexpected_key,
    minimum_tags,
    walk_toc,
]

# Checks to be run on each line
WALKCHECKS = [click_here, dynamic_slurm_link, absolute_site_link, support_mailto_link, h1_in_body]

if __name__ == "__main__":
    main()

    # FIXME terrible hack to make VSCode in codespace capture the error messages
    # see https://github.com/microsoft/vscode/issues/92868 as a tentative explanation
    time.sleep(5)

    # Arbitrary weighting whether to fail check or not

    # exit((100 * (len(sys.argv)-1)) < msg_count["notice"] + (30 * msg_count["warning"] + (100 * msg_count["error"])))
