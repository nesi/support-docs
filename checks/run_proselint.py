#!/usr/bin/env python

"""
Modify proselint outputs into a format recognised by github actions.
"""

import sys
import proselint
from proselint import config, tools


files = sys.argv[1:]

ret_code = 0

# Load defaults from config.
config_custom = tools.load_options(config_file_path=".proselint.json", conf_default=config.default)

for file in files:
    with open(file, "r", encoding="utf8") as f:
        for notice in proselint.tools.lint(f.read(), config=config_custom):
            if (notice[7] == "error"):
                ret_code = 1
            print(f"::{notice[7]} file={file},line={notice[2]},col={notice[3]},endLine={notice[2]+notice[6]},title={notice[0]}::'{notice[1]}'")

sys.exit(ret_code)
