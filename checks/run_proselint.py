#!/usr/bin/env python3

"""
Modify proselint outputs into a format recognised by github actions.
"""

import sys
from pathlib import Path

import proselint
from proselint import config, tools

if __name__ == "__main__":

    files = sys.argv[1:]

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
                flush=True,
            )
