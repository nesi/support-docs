#!/usr/bin/env python3

"""
Modify proselint outputs into a format recognised by github actions.
Fenced code blocks are blanked first (keeping line numbers), as their contents aren't prose.
Proselint's own checks also don't see inline code, so `ls *t?ne.*` isn't read as words.

Also runs this repo's own rules, BANNED_PATTERNS in prose_rules.py, as proselint checks named 'reannz.<name>'.
"""

import os
import re
import sys
from pathlib import Path
import time
from typing import NamedTuple

from proselint import config, tools
from proselint.checks import __register__
from proselint.registry import CheckRegistry
from proselint.registry.checks import Check, CheckFlags, CheckResult

from prose_rules import BANNED_PATTERNS, FETCHED_FILES, mask_inline_code, mask_non_prose

FENCE_RE = re.compile(r"^\s*```")


def blank_code_blocks(content):
    lines = content.split("\n")
    in_code_block = False
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_code_block = not in_code_block
            lines[i] = ""
        elif in_code_block:
            lines[i] = ""
    return "\n".join(lines)


class LinePattern(NamedTuple):
    """A BANNED_PATTERNS entry as a proselint check type, matched one line at a time."""

    pattern: re.Pattern

    def check(self, text, check):
        offset = 0
        for line in text.split("\n"):
            for m in self.pattern.finditer(line):
                found = m.group(m.lastindex) if m.lastindex else m.group(0)
                yield CheckResult(
                    check_path=check.path,
                    message=check.message.replace("{0}", found.strip()),
                    span=(offset + m.start(), offset + m.end()),
                    replacements=None,
                )
            offset += len(line) + 1


RULES = {f"reannz.{rule['name']}": rule for rule in BANNED_PATTERNS}


def rule_checks():
    # allow_quotes: proselint skips matches inside quotation marks by default, the rules decide that themselves.
    return tuple(
        Check(
            check_type=LinePattern(re.compile(rule["pattern"], rule.get("flags", 0))),
            path=path,
            message=rule["message"],
            flags=CheckFlags(allow_quotes=True),
        )
        for path, rule in RULES.items()
    )


def rule_enabled(path, file, checks_config):
    rule = RULES[path]
    if re.search(FETCHED_FILES, file) or any(re.search(skip, file) for skip in rule.get("skip", [])):
        return False
    # .proselint.json can turn a rule off, eg. "reannz.hpc3": false. Its keys are sorted most specific first.
    return next((on for key, on in checks_config.items() if path == key or path.startswith(f"{key}.")), True)


def lint(file, raw, config_custom):
    """Proselint's own checks on the page without code, then each scope of rules on its own version of the page."""
    no_code = blank_code_blocks(raw)
    # '~' rather than spaces, so the words either side of the code don't read as a repeated phrase ('and `x` and').
    no_inline_code = "\n".join(mask_inline_code(line, "~") for line in no_code.split("\n"))
    texts = {
        "text": "\n".join(mask_non_prose(line) for line in no_code.split("\n")),
        "markup": no_code,
        "all": raw,
    }
    builtin = {k: v for k, v in config_custom["checks"].items() if not k.startswith("reannz")}
    passes = [(no_inline_code, {"reannz": False} | builtin)]
    for scope, text in texts.items():
        paths = [p for p, r in RULES.items() if r.get("scope", "text") == scope and rule_enabled(p, file, config_custom["checks"])]
        if paths:
            passes.append((text, {p: True for p in paths}))
    results = []
    for text, checks in passes:
        if text.strip():
            results += tools.LintFile(file, content=text).lint({"max_errors": config_custom["max_errors"], "checks": checks})
    return sorted(results, key=lambda r: r.pos)


if __name__ == "__main__":

    files = sys.argv[1:]

    count_warnings = 0

    # Load defaults from config.

    config_custom = config.load_from(Path(".proselint.json"))
    CheckRegistry().register_many(__register__ + rule_checks())
    for file in files:
        print(f"::DEBUG file={file},line=0,col=0,endColumn=0,title=file:: Running proselint on '{file}'")
        for notice in lint(file, Path(file).read_text(encoding="utf8"), config_custom):
            path = notice.check_result.check_path
            level = RULES[path].get("level", "warning") if path in RULES else "warning"
            line, col = notice.pos
            print(
                f"::{level} file={file},line={line},col={col},endColumn={col + notice.extent - 1},"
                f"title={path}::'{notice.check_result.message}'",
                flush=True
            )
            count_warnings += level == "warning"
            time.sleep(0.01)

    # CHECKS_STRICT=1: exit non-zero if any warning or error was reported (notices don't count).
    if os.getenv("CHECKS_STRICT") and count_warnings:
        sys.exit(1)
