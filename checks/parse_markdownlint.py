#!/usr/bin/env python3

"""
Parse piped in markdownlint --json output to github-recognised warning
annotations.
"""

import json
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

for m in findings:
    error_range = ""
    if m.get("errorRange"):
        error_range = f"col={m['errorRange'][0]},endcol={m['errorRange'][1]},"
    print(
        f"::warning file={m['fileName']},line={m['lineNumber']},"
        f"{error_range}title={m['ruleDescription']}::{m['errorDetail']}",
        flush=True,
    )
