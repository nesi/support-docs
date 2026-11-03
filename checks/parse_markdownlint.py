#!/usr/bin/env python3

"""
Parse piped in markdownlint --json output to github-recognised warning
annotations.
"""

import json
import os
import re
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

# Rules that quiz syntax (mkdocs-quiz) breaks by design: each answer is followed directly by its '> feedback'.
QUIZ_SKIP_RULES = {"MD032"}  # Lists should be surrounded by blank lines

_quiz_ranges = {}


def in_quiz(file_name, line_number):
    """True if the line is between <quiz> and </quiz>."""
    if file_name not in _quiz_ranges:
        ranges, start = [], None
        try:
            with open(file_name, encoding="utf8") as f:
                for i, line in enumerate(f, start=1):
                    if re.match(r"^\s*<quiz>", line):
                        start = i
                    elif re.match(r"^\s*</quiz>", line) and start:
                        ranges.append((start, i))
                        start = None
        except OSError:
            pass
        _quiz_ranges[file_name] = ranges
    return any(a <= line_number <= b for a, b in _quiz_ranges[file_name])


warnings = 0
for m in findings:
    rule = m["ruleNames"][0]
    if rule in QUIZ_SKIP_RULES and in_quiz(m["fileName"], m["lineNumber"]):
        continue
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
