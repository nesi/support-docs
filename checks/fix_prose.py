#!/usr/bin/env python3

"""
Auto-fixes the 'reannz.<name>' prose warnings from run_proselint.py whose rule in prose_rules.py has a 'fix':
preferred terms that need no judgement, such as 'file system' -> 'filesystem', 'logged into' -> 'logged in to',
'20GB' -> '20 GB'. The check prints the same fix at the end of its message ("Fix: '...'").

Prints a diff of the changes by default. With --apply, writes them.

It runs the same lint() as run_proselint.py, so it only changes text the check flagged: never code blocks, inline code,
link targets, or pages a rule skips. Left alone, so rerun run_proselint.py afterwards and fix these by hand:
- rules without a 'fix', which need a judgement call (eg. 'the HPC', 'an array job' -> 'a job array', 'sign in'),
- proselint's own checks.

Usage: fix_prose.py [--apply] [--rule NAME ...] FILE ...
"""

import argparse
import difflib
import re
import sys
from pathlib import Path

from prose_rules import fix_for
from run_proselint import RULES, lint, setup


def find_fixes(file, raw, config_custom, rules):
    """Returns the (start, end, replacement, rule) fixes for a page, and the hits that couldn't be placed."""
    lines = raw.split("\n")
    line_starts = [0]
    for line in lines:
        line_starts.append(line_starts[-1] + len(line) + 1)
    fixes, unplaced = [], []
    for result in lint(file, raw, config_custom):
        path, replacement = result.check_result.check_path, result.check_result.replacements
        if path not in RULES or not replacement or (rules and path.removeprefix("reannz.") not in rules):
            continue
        # pos is (line, column), both from 1. Match the rule again on the raw line to be sure it's the same text.
        line, col = result.pos
        rule = RULES[path]
        m = re.compile(rule["pattern"], rule.get("flags", 0)).match(lines[line - 1], col - 1)
        if not m or m.end() - m.start() != result.extent or fix_for(rule, m) != replacement:
            unplaced.append((line, col, path, replacement))
            continue
        start = line_starts[line - 1] + m.start()
        fixes.append((start, start + result.extent, replacement, path))
    return fixes, unplaced


def apply_fixes(raw, fixes):
    """Applies fixes from the end of the page backwards, so earlier offsets stay valid. Overlaps keep the first fix."""
    kept, last_end = [], -1
    for fix in sorted(fixes):
        if fix[0] >= last_end:
            kept.append(fix)
            last_end = fix[1]
    for start, end, replacement, _ in reversed(kept):
        raw = raw[:start] + replacement + raw[end:]
    return raw, len(kept)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0].strip(),
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("files", nargs="+", metavar="FILE")
    parser.add_argument("--apply", action="store_true", help="write the fixes (default: print a diff)")
    parser.add_argument("--rule", action="append", default=[], metavar="NAME",
                        help="only fix this rule, eg. 'filesystem' (repeatable)")
    args = parser.parse_args()

    unknown = [r for r in args.rule if f"reannz.{r}" not in RULES]
    if unknown:
        sys.exit(f"Unknown rule(s): {', '.join(unknown)}")
    without_fix = [r for r in args.rule if "fix" not in RULES[f"reannz.{r}"]]
    if without_fix:
        print(f"No 'fix' in prose_rules.py for: {', '.join(without_fix)}", file=sys.stderr)

    config_custom = setup()
    total, unplaced_all = 0, []
    for file in args.files:
        raw = Path(file).read_text(encoding="utf8")
        fixes, unplaced = find_fixes(file, raw, config_custom, args.rule)
        unplaced_all += [(file, *u) for u in unplaced]
        if not fixes:
            continue
        fixed, count = apply_fixes(raw, fixes)
        total += count
        if args.apply:
            Path(file).write_text(fixed, encoding="utf8")
            print(f"fixed: {file} ({count})")
        else:
            sys.stdout.writelines(difflib.unified_diff(raw.splitlines(keepends=True), fixed.splitlines(keepends=True),
                                                       f"a/{file}", f"b/{file}"))

    print(f"\n{'Fixed' if args.apply else 'Would fix'} {total} hit(s). "
          "Rerun run_proselint.py for the ones that need a judgement call.")
    if unplaced_all:
        print(f"\nSkipped, couldn't match the hit again in the page ({len(unplaced_all)}):")
        for file, line, col, path, replacement in unplaced_all:
            print(f"  {file}:{line}:{col}: {path} -> '{replacement}'")


if __name__ == "__main__":
    main()
