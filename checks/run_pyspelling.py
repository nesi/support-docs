#!/usr/bin/env python3

"""
I should just use base aspell. Pyspelling is trasssssh
"""

import sys
import re
from pyspelling import spellcheck

if __name__ == "__main__":

    ret_code = 0

    for source in sys.argv[1:]:
        with open(source) as f:
            source_md = f.readlines()
        results = spellcheck(".spellcheck.yml", names=["Markdown"], sources=[source], verbose=0, debug=True)
        for r in results:
            if not r.words:
                continue
            for word in r.words:
                print(word)
#             line_no = 0
#             for line in source_md:
#                 line_no += 1
#                 for word in r.words:
#                     matches = re.finditer(r"[^a-zA-Z`._/[\\-]+(" + word + r")[^a-zA-Z`_/\\-]+", line)
#                     for m in matches:
#                         print(f"::warning file={source},line={line_no},col={m.start()+3},endColumn={m.end()},\
# title=spelling::Word '{word}' is mispeled.")
#     sys.exit(0)
