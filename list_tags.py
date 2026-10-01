#!/usr/bin/env python3
"""
List all raw tags found in markdown frontmatter, their frequencies,
and the canonical form each maps to.
"""

import os
import re
import yaml
from collections import Counter
from pathlib import Path

TAGS_VOCAB_PATH = os.getenv("TAGS_VOCAB_PATH", "docs/assets/tags.yml")
DOC_ROOT = os.getenv("DOC_ROOT", "docs")


def load_vocabulary(path):
    vocab = yaml.safe_load(open(path))
    alias_map = {}
    for canonical, entry in vocab.items():
        alias_map[canonical.lower()] = canonical
        for alias in (entry.get("aliases") or []):
            alias_map[alias.lower()] = canonical
    return vocab, alias_map


def parse_frontmatter(path):
    content = path.read_text()
    match = re.match(r"---\n([\s\S]*?)---", content)
    if not match:
        return None
    return yaml.safe_load(match.group(1)) or {}


vocab, alias_map = load_vocabulary(TAGS_VOCAB_PATH)

raw_counter = Counter()
unknown_tags = Counter()
# canonical -> set of raw forms seen
raw_forms = {c: set() for c in vocab}

for md_file in sorted(Path(DOC_ROOT).rglob("*.md")):
    meta = parse_frontmatter(md_file)
    if meta is None:
        continue
    for tag in meta.get("tags") or []:
        tag_str = str(tag)
        raw_counter[tag_str] += 1
        canonical = alias_map.get(tag_str.lower())
        if canonical is None:
            unknown_tags[tag_str] += 1
        else:
            raw_forms[canonical].add(tag_str)

# Group raw tags by canonical form
print("=" * 70)
print(f"{'RAW TAG':<35} {'CANONICAL':<25} {'COUNT':>5}")
print("=" * 70)
for tag, count in sorted(raw_counter.items(), key=lambda x: (-x[1], x[0])):
    canonical = alias_map.get(tag.lower(), "UNKNOWN")
    already_canonical = (tag == canonical)
    marker = "" if already_canonical else "  <-- needs rename"
    print(f"{tag:<35} {canonical:<25} {count:>5}{marker}")

if unknown_tags:
    print()
    print("UNKNOWN TAGS (not in vocabulary):")
    for tag, count in unknown_tags.most_common():
        print(f"  {tag!r:<35} count={count}")

print()
print(f"Total distinct raw tags : {len(raw_counter)}")
print(f"Total tag occurrences   : {sum(raw_counter.values())}")
print(f"Tags needing rename     : {sum(1 for t in raw_counter if alias_map.get(t.lower(), 'UNKNOWN') != t)}")
print(f"Unknown tags            : {len(unknown_tags)}")

# Show canonical forms that have multiple raw aliases in use
print()
print("CANONICAL FORMS WITH MULTIPLE RAW ALIASES IN USE:")
any_found = False
for canonical, forms in sorted(raw_forms.items()):
    if len(forms) > 1:
        print(f"  {canonical}: {sorted(forms)}")
        any_found = True
if not any_found:
    print("  (none)")
