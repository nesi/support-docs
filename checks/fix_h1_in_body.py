#!/usr/bin/env python3

"""
Auto-fixes the 'h1_in_body' warning from run_meta_check.py: H1 is reserved
for the page title (see FORMAT.md/styleguide.md) - a literal '# ...' in the
body silently overrides the nav title too, so it's removed.

If the page has no explicit 'title:' in front matter and the H1 text differs
from what mkdocs would derive from the filename, the H1 text is preserved by
promoting it to an explicit 'title:' field first - otherwise deleting the H1
would silently change the page's nav title back to the filename-derived one.
"""

import re
from pathlib import Path

import yaml

DOC_ROOT = Path("docs")
EXCLUDED_FROM_CHECKS = [
    r"docs/assets/.*",
    r".*/index\.md",
]
H1_RE = re.compile(r"^#\s+(.*)$")
FENCE_RE = re.compile(r"^\s*```.*$")


def mkdocs_title(stem):
    """Matches mkdocs' own Page.title fallback - see run_meta_check.py's _title_from_filename."""
    name = stem.replace("-", " ").replace("_", " ")
    if name.lower() == name:
        name = name.capitalize()
    return name


def find_body_h1s(lines):
    in_code_block = False
    found = []
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        m = H1_RE.match(line)
        if m:
            found.append((i, m.group(1)))
    return found


def insert_title(frontmatter, title_text):
    title_line = yaml.safe_dump({"title": title_text}, default_flow_style=False, allow_unicode=True)
    return title_line + frontmatter


def collapse_blank_runs(text):
    return re.sub(r"\n{3,}", "\n\n", text)


def fix_file(path):
    content = path.read_text()
    match = re.match(r"---\n([\s\S]*?)---\n", content, re.MULTILINE)
    if not match:
        return None
    frontmatter = match.group(1)
    body_start = match.end()

    body_lines = content[body_start:].split("\n")
    h1s = find_body_h1s(body_lines)
    if not h1s:
        return None

    meta = yaml.safe_load(frontmatter) or {}
    added_title = None
    if "title" not in meta:
        h1_text = h1s[0][1]
        if h1_text != mkdocs_title(path.stem):
            frontmatter = insert_title(frontmatter, h1_text)
            added_title = h1_text

    h1_linenos = {i for i, _ in h1s}
    new_body = "\n".join(l for i, l in enumerate(body_lines) if i not in h1_linenos)

    new_content = collapse_blank_runs(
        content[:match.start(1)] + frontmatter + "---\n" + new_body
    )
    path.write_text(new_content)
    return len(h1s), added_title


def main():
    fixed = []
    for path in sorted(DOC_ROOT.rglob("*.md")):
        rel = str(path)
        if any(re.match(pattern, rel) for pattern in EXCLUDED_FROM_CHECKS):
            continue
        result = fix_file(path)
        if result:
            fixed.append((path, *result))

    for path, count, added_title in fixed:
        note = f", set title: '{added_title}'" if added_title else ""
        print(f"{path}: removed {count} H1 line(s){note}")
    print(f"\nFixed {len(fixed)} file(s).")


if __name__ == "__main__":
    main()
