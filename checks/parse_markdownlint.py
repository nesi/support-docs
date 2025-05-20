#!/usr/bin/env python3

"""
Parse piped in mardownlint output to a format recognised by github actions.
"""

import json
import sys

if sys.stdin.isatty():
    print(f"Parsing markdown for {sys.std}")
    j = json.load(sys.stdin)
    for m in j:
        error_range = ""
        if "errorRange" in m and m["errorRange"]:
            error_range = f"col={m['errorRange'][0]},endcol={m['errorRange'][1]},"
        print(f"::warning file={m['fileName']},line={m['lineNumber']},\
            {error_range}title={m['ruleDescription']}::{m['errorDetail']}", flush=True)
        sys.stdout.flush()
