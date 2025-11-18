#!/usr/bin/env python3

"""
Modify proselint outputs into a format recognised by github actions.
"""

import sys
from pathlib import Path
import time

import proselint
from proselint import config, tools
from proselint.checks import __register__
from proselint.registry import CheckRegistry

ALLOWABLE_NOTICES = 5

if __name__ == "__main__":

    files = sys.argv[1:]

    count_notices = 0

    # Load defaults from config.

    config_custom = config.load_from(Path(".proselint.json"))
    CheckRegistry().register_many(__register__)
    for file in files:
        print(f"::DEBUG file={file},line=0,col=0,endColumn=0,title=file:: Running proselint on '{file}'")
        content = Path(file).read_text(encoding="utf8")
        for notice in tools.LintFile(file, content=content).lint(config_custom):
            print(
                f"::warning file={file},line={notice.pos[0]},"
                f"col={notice.check_result.span[0]},endColumn={notice.check_result.span[1]},"
                f"title={notice.check_result.check_path}::'{notice.check_result.message}'",
                flush=True
            )
            count_notices += 1
            time.sleep(0.01)

    # exit(count_notices >= ALLOWABLE_NOTICES*(len(sys.argv)-1))
