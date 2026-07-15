#!/usr/bin/env python3

"""
Auto-fixes the 'support_mailto_link' warning from run_meta_check.py: replaces
raw markdown/HTML links to mailto:support@nesi.org.nz with the
'partials/support_request.html' include, per FORMAT.md's convention. The
include always renders as "Contact our Support Team", so the original link
text is discarded - surrounding sentences read fine with the standard
phrasing (this is already the pattern used elsewhere in the docs, eg. VASP.md).

Links with a mailto query string (eg. '?subject=...') are left alone and
reported separately: the plain include has no way to carry a pre-filled
subject line, so collapsing those would silently drop functionality - a human
should decide whether to keep the custom subject or standardise it away.
"""

import re
from pathlib import Path

DOC_ROOT = Path("docs")
EXCLUDED_FROM_CHECKS = [
    r"docs/assets/.*",
    r"docs/FORMAT\.md",  # documents the mailto -> include convention using a literal example
]
INCLUDE_TAG = '{% include "partials/support_request.html" %}'

# Order matters: markdown links and full <a>...</a> tags must be matched
# (and thus replaced) before the bare-autolink case, since a markdown link's
# URL segment would otherwise also satisfy the bare-autolink pattern.
LINK_RES = [
    re.compile(r'\[[^\]]*\]\(\s*(?:mailto:)?support@nesi\.org\.nz[^)]*\)', re.IGNORECASE),
    re.compile(
        r'<a\s[^>]*href=["\'](?:mailto:)?support@nesi\.org\.nz[^"\']*["\'][^>]*>.*?</a>',
        re.IGNORECASE,
    ),
    re.compile(r'<(?:mailto:)?support@nesi\.org\.nz>', re.IGNORECASE),
]
FENCE_RE = re.compile(r"^\s*```.*$")
HAS_QUERY_RE = re.compile(r'support@nesi\.org\.nz\?', re.IGNORECASE)


def fix_file(path, needs_review):
    content = path.read_text()
    lines = content.split("\n")
    in_code_block = False
    changed = False

    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        new_line = line
        for pattern in LINK_RES:
            def repl(m):
                nonlocal changed
                if HAS_QUERY_RE.search(m.group(0)):
                    needs_review.append((path, i + 1, m.group(0)))
                    return m.group(0)
                changed = True
                return INCLUDE_TAG

            new_line = pattern.sub(repl, new_line)
        lines[i] = new_line

    if changed:
        path.write_text("\n".join(lines))
    return changed


def main():
    fixed_files = []
    needs_review = []

    for path in sorted(DOC_ROOT.rglob("*.md")):
        rel = str(path)
        if any(re.match(pattern, rel) for pattern in EXCLUDED_FROM_CHECKS):
            continue
        if fix_file(path, needs_review):
            fixed_files.append(path)

    for path in fixed_files:
        print(f"fixed: {path}")
    print(f"\nFixed links in {len(fixed_files)} file(s).")

    if needs_review:
        print(f"\nSkipped, has a mailto query string (subject/etc.) - needs a human call, {len(needs_review)}:")
        for path, lineno, snippet in needs_review:
            print(f"  {path}:{lineno}: {snippet}")


if __name__ == "__main__":
    main()
