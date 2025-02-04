#!/usr/bin/env python3

"""
Modify proselint outputs into a format recognised by github actions.
"""

import sys
from pathlib import Path
import time

import proselint
from proselint import config, tools

ALLOWABLE_NOTICES = 5

if __name__ == "__main__":

    files = sys.argv[1:]

    count_notices = 0

    # Load defaults from config.
    config_custom = tools.load_options(
        config_file_path=".proselint.json", conf_default=config.default
    )

    for file in files:
        print(f"Running proselint on {file}")
        content = Path(file).read_text(encoding="utf8")
        for notice in proselint.tools.lint(content, config=config_custom):
            print(
                f"::{notice[7]} file={file},line={notice[2]+1},"
                f"col={notice[3]+2},endColumn={notice[2]+notice[6]+1},"
                f"title={notice[0]}::'{notice[1]}'",
                flush=True
            )
            count_notices += 1
            time.sleep(0.01)

    exit(count_notices >= ALLOWABLE_NOTICES*(len(sys.argv)-1))
