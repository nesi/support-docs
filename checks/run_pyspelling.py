#!/usr/bin/env python3

"""
I should just use base aspell. Spyspelling is trasssssh
"""

import sys
import re
from pyspelling import util, spellcheck

ret_code = 0
for source in sys.argv[1:]:
    with open(source) as f:
        source_md = f.readlines()
    results = spellcheck(".spellcheck.yml", names=["Markdown"], sources=[source], verbose=0, debug=True)
    for r in results:
        if not r.words:
            continue
        line_no = 0
        for line in source_md:
            line_no += 1
            for word in r.words:
                matches = re.finditer(r"[^a-zA-Z`._/[\\-]+(" + word + r")[^a-zA-Z`_/\\-]+", line)
                for m in matches:
                    print(r)
                    print(f"::warning file={source},line={line_no},col={m.span()[0]+2},endColumn={m.span()[1]-1},title=spelling::Word '{word}' is mispeled.")
# util.read_config(".spellcheck.yml")

# util.call(input_file=None, input_text=None, encoding=None)

# call_spellchecker(cmd, input_text=None, encoding=None)


# # Load defaults from config.
# config_custom = tools.load_options(config_file_path=".proselint.json", conf_default=config.default)

# print(config_custom)

# for file in files:
#     with open(file, "r", encoding="utf8") as f:
#         for notice in proselint.tools.lint(f.read(), config=config_custom):
#             if (notice[7] == "error"):
#                 ret_code = 1
#             print(f"::{notice[7]} file={file},line={notice[2]},col={notice[3]},endLine={notice[2]+notice[6]},title={notice[0]}::'{notice[1]}'")

# sys.exit(ret_code)
