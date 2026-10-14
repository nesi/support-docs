#!/usr/bin/env python3

"""
Modify proselint outputs into a format recognised by github actions.
Fenced code blocks are blanked first (keeping line numbers), as their contents aren't prose.

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

from prose_rules import BANNED_PATTERNS, FETCHED_FILES, fix_for, mask_non_prose

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
    """A BANNED_PATTERNS entry as a proselint check type, matched one line at a time.

    With 'first_mention', only the page's first match is reported, and only if it comes before the full form.
    The rule's 'fix', if it has one for the match, is added to the message and given as the result's replacement.
    """

    pattern: re.Pattern
    first_mention: re.Pattern | None = None
    rule: dict | None = None

    def check(self, text, check):
        full_form = self.first_mention and self.first_mention.search(text)
        offset = 0
        for line in text.split("\n"):
            for m in self.pattern.finditer(line):
                if self.first_mention and full_form and full_form.start() <= offset + m.start():
                    return
                found = m.group(m.lastindex) if m.lastindex else m.group(0)
                fix = fix_for(self.rule, m) if self.rule else None
                yield CheckResult(
                    check_path=check.path,
                    message=check.message.replace("{0}", found.strip()) + (f" Fix: '{fix}'." if fix else ""),
                    span=(offset + m.start(), offset + m.end()),
                    replacements=fix,
                )
                if self.first_mention:
                    return
            offset += len(line) + 1


RULES = {f"reannz.{rule['name']}": rule for rule in BANNED_PATTERNS}


def rule_checks():
    # allow_quotes: proselint skips matches inside quotation marks by default, the rules decide that themselves.
    return tuple(
        Check(
            check_type=LinePattern(re.compile(rule["pattern"], rule.get("flags", 0)),
                                   re.compile(rule["first_mention"]) if "first_mention" in rule else None, rule),
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


def setup():
    """Registers proselint's checks and ours, and returns the config from .proselint.json to pass to lint()."""
    config_custom = config.load_from(Path(".proselint.json"))
    CheckRegistry().register_many(__register__ + rule_checks())
    return config_custom


def lint(file, raw, config_custom):
    """Proselint's own checks on the page without code blocks, then each scope of rules on its own version of the page."""
    no_code = blank_code_blocks(raw)
    texts = {
        "text": "\n".join(mask_non_prose(line) for line in no_code.split("\n")),
        "markup": no_code,
        "all": raw,
    }
    builtin = {k: v for k, v in config_custom["checks"].items() if not k.startswith("reannz")}
    passes = [(no_code, {"reannz": False} | builtin)]
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

    config_custom = setup()
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
