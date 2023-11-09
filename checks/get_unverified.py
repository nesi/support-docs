#!/usr/bin/env python3

"""
Checks which articles still need checking and produces printout
"""
import re
import sys

for input_file in sys.argv[1:]:
    with open(input_file, "r") as f:
        if re.findall(r"^\[\/\/\]: <> \(REMOVE ME IF PAGE VALIDATED\)$", f.read(), re.MULTILINE):
            print(input_file)
