#!/usr/bin/env python3

"""
Auto-fixes the 'title_capitalisation' warning from run_meta_check.py for
pages with an explicit 'title:' in front matter: re-cases it with titlecase().

Pages with no front-matter title (title comes from the filename instead) are
left alone - see fix_filename_capitalisation.py for those.
"""

import re
from pathlib import Path

import yaml
from titlecase import titlecase

DOC_ROOT = Path("docs")
EXCLUDED_FROM_CHECKS = [
    r"docs/assets/.*",
    r".*/index\.md",
    # Software names are often acronyms/proper nouns (BLAST, VASP, ont-guppy-gpu) that
    # titlecase() mangles, and the mangled title breaks the applications[app_name]
    # macro lookup on Available_Applications pages (a KeyError, not just a cosmetic typo).
    r"docs/Software/Available_Applications/.*",
]

TITLE_LINE_RE = re.compile(r"^(title:\s*)(.*)$", re.MULTILINE)


def fix_file(path):
    content = path.read_text()
    match = re.match(r"---\n([\s\S]*?)---", content, re.MULTILINE)
    if not match:
        return None

    frontmatter = match.group(1)
    meta = yaml.safe_load(frontmatter) or {}
    if not isinstance(meta.get("title"), str):
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


def main():
    fixed = []
    for path in sorted(DOC_ROOT.rglob("*.md")):
        if any(re.match(p, str(path)) for p in EXCLUDED_FROM_CHECKS):
            continue
        result = fix_file(path)
        if result:
            fixed.append((path, *result))

    for path, orig, new in fixed:
        print(f"{path}: '{orig}' -> '{new}'")
    print(f"\nFixed {len(fixed)} file(s).")


if __name__ == "__main__":
    main()
