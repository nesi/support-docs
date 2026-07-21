#!/usr/bin/env python3

"""
Auto-fixes the 'meta_unexpected_key' warning from run_meta_check.py, for the
Zendesk Help Center export leftovers only (zendesk_article_id,
zendesk_section_id, vote_sum, vote_count, position, hidden) - these have no
purpose in this mkdocs site.

zendesk_article_id/zendesk_section_id are pure migration IDs and are always
removed. vote_sum/vote_count/position/hidden carry actual data from the old
system, so they're only removed when they hold the boilerplate "nothing
happened" default (0 / 0 / 0 / False) - a page with a non-default value (eg.
actual votes, or 'hidden: true') keeps the key and keeps showing up as a
meta_unexpected_key warning, since that value might matter and deserves a
human look rather than being silently deleted.

Any OTHER unexpected key (typos like 'Title'/'created', etc.) is left alone -
this script only ever touches the six keys named above.
"""

import re
from pathlib import Path

import yaml

DOC_ROOT = Path("docs")
EXCLUDED_FROM_CHECKS = [
    r"docs/assets/.*",
]

ANY_VALUE = object()  # sentinel: strip regardless of value
STRIP_KEYS = {
    "zendesk_article_id": ANY_VALUE,
    "zendesk_section_id": ANY_VALUE,
    "vote_sum": 0,
    "vote_count": 0,
    "position": 0,
    "hidden": False,
}


def fix_file(path):
    content = path.read_text()
    match = re.match(r"---\n([\s\S]*?)---", content, re.MULTILINE)
    if not match:
        return None
    frontmatter = match.group(1)
    meta = yaml.safe_load(frontmatter) or {}

    removed = []
    kept_unique = []
    new_frontmatter = frontmatter

    for key, default in STRIP_KEYS.items():
        if key not in meta:
            continue
        if default is not ANY_VALUE and meta[key] != default:
            kept_unique.append((key, meta[key]))
            continue
        new_frontmatter, n = re.subn(rf"^{key}:.*\n", "", new_frontmatter, count=1, flags=re.MULTILINE)
        if n:
            removed.append(key)

    if not removed:
        return None

    path.write_text(content.replace(frontmatter, new_frontmatter, 1))
    return removed, kept_unique


def main():
    fixed = []
    for path in sorted(DOC_ROOT.rglob("*.md")):
        rel = str(path)
        if any(re.match(pattern, rel) for pattern in EXCLUDED_FROM_CHECKS):
            continue
        result = fix_file(path)
        if result:
            fixed.append((path, *result))

    total_kept = 0
    for path, removed, kept_unique in fixed:
        note = ""
        if kept_unique:
            note = " (kept non-default: " + ", ".join(f"{k}={v!r}" for k, v in kept_unique) + ")"
            total_kept += len(kept_unique)
        print(f"{path}: removed {', '.join(removed)}{note}")
    print(f"\nFixed {len(fixed)} file(s), kept {total_kept} non-default value(s) for manual review.")


if __name__ == "__main__":
    main()
