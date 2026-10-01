#!/usr/bin/env python3

"""
Auto-fixes the 'title_redundant' warning from run_meta_check.py for the
"Title set in meta is redundant as it is already set in filename" case:
when front-matter 'title' is identical to the title mkdocs would derive from
the filename anyway, the explicit 'title:' line is just removed.

Cases where the redundancy is against the H1 instead are left alone - they're
rare (the check's H1 detection barely ever fires) and worth a human glance.

Available_Applications/ pages are also left alone: their title doubles as the
lookup key into applications[] (see app_header.html), and a page rename would
silently break that lookup with no explicit title left to notice or restore.
"""

import re
from pathlib import Path

import yaml

DOC_ROOT = "docs"
EXCLUDED_FROM_CHECKS = [
    r"docs/assets/.*",
    r".*/index\.md",
    r"docs/Software/Available_Applications/.*",
]

TITLE_LINE_RE = re.compile(r"^title:.*\n", re.MULTILINE)


def title_from_filename(path):
    """Matches mkdocs' own Page.title fallback - see run_meta_check.py's _title_from_filename."""
    name = path.stem.replace("-", " ").replace("_", " ")
    if name.lower() == name:
        name = name.capitalize()
    return name


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

    if meta["title"] != title_from_filename(path):
        return None

    new_frontmatter, n = TITLE_LINE_RE.subn("", frontmatter, count=1)
    if n != 1:
        return None

    path.write_text(content.replace(frontmatter, new_frontmatter, 1))
    return meta["title"]


def main():
    fixed = []
    for path in iter_md_files():
        result = fix_file(path)
        if result:
            fixed.append((path, result))

    for path, title in fixed:
        print(f"{path}: removed redundant title '{title}'")
    print(f"\nFixed {len(fixed)} file(s).")


if __name__ == "__main__":
    main()
