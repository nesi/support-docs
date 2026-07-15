#!/usr/bin/env python3

"""
Auto-fixes the 'title_capitalisation' warning from run_meta_check.py.

Phase 1 touches pages that have an explicit 'title:' key in their front
matter - a simple field edit.

Phase 2 covers pages whose title is derived from the filename instead: it
renames the file itself, updates every internal link/.pages.yml nav entry
that pointed at the old name, and records the move in redirect_map.yml so
external/bookmarked links still resolve.

Skipped, on purpose:
- Anything under Software/Available_Applications/ - software names often
  have legitimate non-standard casing (fastStructure, ollama, VASP) that
  titlecase() would mangle.
- Filenames that are entirely uppercase once separators are stripped (eg.
  GLOSSARY, MACROS, MATLAB) - a strong signal it's an intentional acronym or
  product name, not an undercased phrase.
- Filenames containing 'nesi-org-nz' - that's the my.nesi.org.nz brand
  rendered lowercase-hyphenated by convention (see the sibling directory of
  the same name), not a phrase to titlecase.
"""

import re
import subprocess
from pathlib import Path

import yaml
from titlecase import titlecase

DOC_ROOT = "docs"
EXCLUDED_FROM_CHECKS = [
    r"docs/assets/.*",
    r".*/index\.md",
]
EXCLUDED_FROM_RENAME = EXCLUDED_FROM_CHECKS + [
    r"docs/Software/Available_Applications/.*",
]
REDIRECT_MAP_PATH = Path(DOC_ROOT) / "redirect_map.yml"

TITLE_LINE_RE = re.compile(r"^(title:\s*)(.*)$", re.MULTILINE)


def iter_md_files():
    for path in sorted(Path(DOC_ROOT).rglob("*.md")):
        rel = str(path)
        if any(re.match(pattern, rel) for pattern in EXCLUDED_FROM_CHECKS):
            continue
        yield path


def fix_file(path):
    content = path.read_text()
    match = re.match(r"---\n([\s\S]*?)---", content, re.MULTILINE)
    if not match:
        return None

    frontmatter = match.group(1)
    meta = yaml.safe_load(frontmatter) or {}
    if "title" not in meta or not isinstance(meta["title"], str):
        return None

    orig_title = meta["title"]
    new_title = titlecase(orig_title)
    if new_title == orig_title:
        return None

    def repl(m):
        prefix, raw_val = m.group(1), m.group(2).strip()
        if raw_val[:1] == raw_val[-1:] and raw_val[:1] in ("'", '"'):
            quote = raw_val[0]
            return f"{prefix}{quote}{new_title}{quote}"
        return f"{prefix}{new_title}"

    new_frontmatter, n = TITLE_LINE_RE.subn(repl, frontmatter, count=1)
    if n != 1:
        return None

    path.write_text(content.replace(frontmatter, new_frontmatter, 1))
    return orig_title, new_title


def mkdocs_title(stem):
    """Matches mkdocs' own Page.title fallback - see run_meta_check.py's _title_from_filename."""
    name = stem.replace("-", " ").replace("_", " ")
    if name.lower() == name:
        name = name.capitalize()
    return name


def is_acronym_or_brand(stem):
    bare = stem.replace("_", "").replace("-", "")
    if bare.isupper():
        return True
    if "nesi-org-nz" in stem.lower() or "nesi_org_nz" in stem.lower():
        return True
    return False


def word_level_rename(stem):
    """Re-cases each underscore/hyphen-separated word via titlecase(), keeping
    the original separators and word boundaries untouched. Returns None if
    titlecase() changed the word count (unsafe to remap 1:1)."""
    tokens = re.split(r"([_-])", stem)
    words = tokens[0::2]
    seps = tokens[1::2]

    new_words = titlecase(" ".join(words)).split(" ")
    if len(new_words) != len(words):
        return None

    out = []
    for i, word in enumerate(new_words):
        out.append(word)
        if i < len(seps):
            out.append(seps[i])
    return "".join(out)


def update_references(old_name, new_name):
    """Rewrites internal links/nav entries across docs/ from old filename to new."""
    pattern = re.compile(r"(?<=[/(\s-])" + re.escape(old_name) + r"(?=[)#\s\"']|$)", re.MULTILINE)
    changed_files = []
    for path in Path(DOC_ROOT).rglob("*.md"):
        content = path.read_text()
        new_content, n = pattern.subn(new_name, content)
        if n:
            path.write_text(new_content)
            changed_files.append(path)
    for path in Path(DOC_ROOT).rglob(".pages.yml"):
        content = path.read_text()
        new_content, n = pattern.subn(new_name, content)
        if n:
            path.write_text(new_content)
            changed_files.append(path)
    return changed_files


def update_redirect_map(old_rel, new_rel):
    if not REDIRECT_MAP_PATH.exists():
        return
    lines = REDIRECT_MAP_PATH.read_text().split("\n")
    updated = []
    for line in lines:
        if ":" not in line or line.strip().startswith("#"):
            updated.append(line)
            continue
        key, _, value = line.partition(":")
        if value.strip() == old_rel:
            updated.append(f"{key}: {new_rel}")
        else:
            updated.append(line)
    updated.append(f"{old_rel}: {new_rel}")
    REDIRECT_MAP_PATH.write_text("\n".join(updated))


def rename_files():
    renamed = []
    skipped_acronym = []
    unchanged = []

    for path in sorted(Path(DOC_ROOT).rglob("*.md")):
        rel = str(path)
        if any(re.match(pattern, rel) for pattern in EXCLUDED_FROM_RENAME):
            continue

        content = path.read_text()
        match = re.match(r"---\n([\s\S]*?)---", content, re.MULTILINE)
        meta = yaml.safe_load(match.group(1)) if match else {}
        if meta and "title" in meta:
            continue  # handled by fix_file()/Phase 1

        title = mkdocs_title(path.stem)
        if titlecase(title) == title:
            continue  # not actually miscapitalised

        if is_acronym_or_brand(path.stem):
            skipped_acronym.append(path)
            continue

        new_stem = word_level_rename(path.stem)
        if new_stem is None or new_stem == path.stem:
            unchanged.append(path)
            continue

        new_path = path.with_name(new_stem + ".md")
        if new_path.exists():
            print(f"CONFLICT: {new_path} already exists, skipping rename of {path}")
            continue

        subprocess.run(["git", "mv", str(path), str(new_path)], check=True)
        changed_refs = update_references(path.name, new_path.name)
        old_rel = str(path.relative_to(DOC_ROOT))
        new_rel = str(new_path.relative_to(DOC_ROOT))
        update_redirect_map(old_rel, new_rel)
        renamed.append((path, new_path, changed_refs))

    return renamed, skipped_acronym, unchanged


def main():
    fixed = []
    for path in iter_md_files():
        result = fix_file(path)
        if result:
            fixed.append((path, *result))

    for path, orig, new in fixed:
        print(f"{path}: '{orig}' -> '{new}'")
    print(f"\nPhase 1 (meta title edits): fixed {len(fixed)} file(s).")

    renamed, skipped_acronym, unchanged = rename_files()
    print()
    for old, new, refs in renamed:
        print(f"renamed: {old} -> {new} ({len(refs)} referencing file(s) updated)")
    print(f"\nPhase 2 (file renames): renamed {len(renamed)} file(s).")

    if skipped_acronym:
        print(f"\nSkipped (looks like an acronym/brand name), {len(skipped_acronym)}:")
        for path in skipped_acronym:
            print(f"  {path}")


if __name__ == "__main__":
    main()
