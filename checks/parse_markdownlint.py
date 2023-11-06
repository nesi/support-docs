#!/usr/bin/env python3

import json
import sys

j = json.load(sys.stdin)
for m in j:
    if "errorRange" in m and m["errorRange"]:
        error_range = f"col={m['errorRange'][0]},endcol={m['errorRange'][1]},"
    print(f"::warning file={m['fileName']},line={m['lineNumber']},{error_range}title={m['ruleDescription']}::{m['errorDetail']}")