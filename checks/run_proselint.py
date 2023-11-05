#!/usr/bin/env python

import sys
import proselint
from proselint import config

"""
Modify proselint outputs into a format recognised by github actions.
"""

files = sys.argv[1:]

ret_code = 0
proselint.config.default["checks"]["hyperbole.misc"] = False

for file in files:
    with open(file, "r", encoding="utf8") as f:
        for notice in proselint.tools.lint(f.read(), config=config.default):
            if (notice[7] == "error"):
                ret_code = 1
            print(f"::{notice[7]} file={file},line={notice[2]},col={notice[3]},endLine={notice[2]+notice[6]},title={notice[0]}::'{notice[1]}'")

sys.exit(ret_code)
