#!/usr/bin/env python3
"""
One-off script: replace all tags in markdown frontmatter with their canonical forms.

Usage:
    python3 normalize_tags.py           # apply changes in-place
    python3 normalize_tags.py --dry-run # preview only, no writes
"""

import os
import re
import sys
import yaml
from pathlib import Path

TAGS_VOCAB_PATH = os.getenv("TAGS_VOCAB_PATH", "docs/assets/tags.yml")
DOC_ROOT = os.getenv("DOC_ROOT", "docs")
DRY_RUN = "--dry-run" in sys.argv


def load_vocabulary(path):
    vocab = yaml.safe_load(open(path))
    alias_map = {}
    for canonical, entry in vocab.items():
        alias_map[canonical.lower()] = canonical
        for alias in (entry.get("aliases") or []):
            alias_map[alias.lower()] = canonical
    return vocab, alias_map


def replace_tags_in_frontmatter(text, new_tags, old_tags):
    """Replace the tags block in raw frontmatter text, preserving all other content."""
    # Build replacement block with the same indentation as the first existing tag line.
    indent_match = re.search(r"^( *)-", text, re.MULTILINE)
    indent = indent_match.group(1) if indent_match else "- "
    new_block = "tags:\n" + "".join(f"{indent}- {t}\n" for t in new_tags)

    # Replace tags block: `tags:\n` followed by lines starting with optional spaces + `-`
    updated = re.sub(
        r"tags:\s*\n(?:[ \t]*-[ \t]+[^\n]*\n?)*",
        new_block,
        text,
    )
    return updated


vocab, alias_map = load_vocabulary(TAGS_VOCAB_PATH)

files_changed = 0
files_skipped = 0

for md_file in sorted(Path(DOC_ROOT).rglob("*.md")):
    original = md_file.read_text()

    # Extract frontmatter block
    fm_match = re.match(r"(---\n)([\s\S]*?)(---)", original)
    if not fm_match:
        continue

    fm_open, fm_body, fm_close = fm_match.group(1), fm_match.group(2), fm_match.group(3)

    meta = yaml.safe_load(fm_body) or {}
    raw_tags = meta.get("tags") or []
    if not raw_tags:
        continue

    canonical_tags = []
    unknown = []
    for tag in raw_tags:
        canonical = alias_map.get(str(tag).lower())
        if canonical is None:
            unknown.append(str(tag))
        elif canonical not in canonical_tags:
            canonical_tags.append(canonical)

    # Skip if already canonical and nothing was deduped
    if canonical_tags == [str(t) for t in raw_tags] and not unknown:
        continue

    new_fm_body = replace_tags_in_frontmatter(fm_body, canonical_tags, raw_tags)
    new_content = fm_open + new_fm_body + fm_close + original[fm_match.end():]

    rel = md_file.relative_to(DOC_ROOT)
    if raw_tags != canonical_tags or unknown:
        print(f"{rel}")
        raw_display = [str(t) for t in raw_tags]
        if raw_display != canonical_tags:
            print(f"  before: {raw_display}")
            print(f"  after : {canonical_tags}")
        if unknown:
            print(f"  SKIPPED unknown tags: {unknown}")

    if new_content == original:
        files_skipped += 1
        continue

    files_changed += 1
    if not DRY_RUN:
        md_file.write_text(new_content)

print()
if DRY_RUN:
    print(f"DRY RUN — {files_changed} file(s) would be updated.")
else:
    print(f"Updated {files_changed} file(s).")
if files_skipped:
    print(f"Skipped {files_skipped} file(s) (no text change after canonicalization).")
