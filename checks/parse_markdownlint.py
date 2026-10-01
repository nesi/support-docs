#!/usr/bin/env python3

"""
Parse piped in markdownlint --json output to github-recognised warning
annotations.
"""

import json
import os
import sys

if sys.stdin.isatty():
    sys.exit(0)  # No piped input (e.g. run directly) - nothing to parse.

raw = sys.stdin.read()

if not raw.strip():
    sys.exit(0)  # markdownlint prints nothing at all when there are no findings.

try:
    findings = json.loads(raw)
except json.JSONDecodeError:
    print(f"::error::markdownlint produced unparseable output:\n{raw}")
    sys.exit(1)

# Rules that don't change the rendered page (checked against this site's markdown extensions),
# reported as notices instead of warnings.
NOTICE_RULES = {
    "MD004",  # Unordered list style
    "MD010",  # Hard tabs
    "MD012",  # Multiple consecutive blank lines
    "MD022",  # Headings should be surrounded by blank lines
    "MD027",  # Multiple spaces after blockquote symbol
    "MD029",  # Ordered list item prefix
    "MD030",  # Spaces after list markers
    "MD034",  # Bare URL used (pymdownx.magiclink links them anyway)
    "MD047",  # Files should end with a single newline character
    "MD049",  # Emphasis style
    "MD050",  # Strong style
    "MD060",  # Table column style
}

warnings = 0
for m in findings:
    rule = m["ruleNames"][0]
    detail = m.get("errorDetail") or m.get("errorContext") or m["ruleDescription"]
    level = "notice" if rule in NOTICE_RULES else "warning"
    # A single trailing space is invisible, but two or more render as a line break.
    if rule == "MD009" and detail.endswith("Actual: 1"):
        level = "notice"
    warnings += level == "warning"
    error_range = ""
    if m.get("errorRange"):
        error_range = f"col={m['errorRange'][0]},endcol={m['errorRange'][1]},"
    print(
        f"::{level} file={m['fileName']},line={m['lineNumber']},"
        f"{error_range}title={m['ruleDescription']}::{detail}",
        flush=True,
    )

# CHECKS_STRICT=1: exit non-zero if any warning was reported.
if os.getenv("CHECKS_STRICT") and warnings:
    sys.exit(1)
