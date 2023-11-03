#!/usr/bin/env python

import sys
import proselint
from proselint import config

files = sys.argv[1:]

for file in files:
    with open(file, "r", encoding="utf8") as f:
        for notice in proselint.tools.lint(f.read(), config=config.default):
            print(f"::{notice[7]} file={file},line={notice[2]},col={notice[3]},endLine={notice[2]+notice[6]},title={notice[0]}::'{notice[1]}'")
