#!/usr/bin/env python3

# FIXME direct use of aspell might be simpler than postprocessing pyspelling

import sys
import re
from pyspelling import spellcheck

if __name__ == "__main__":

    for source in sys.argv[1:]:
        with open(source) as f:
            print(f"Running Pyspelling on {f}")
            source_md = f.readlines()

        results = spellcheck(
            ".spellcheck.yml",
            names=["Markdown"],
            sources=[source],
            verbose=0,
            debug=True,
        )

        for r in results:
            if not r.words:
                continue

            for word in r.words:
                line_no = 0
                for line in source_md:
                    line_no += 1
                    for word in r.words:
                        matches = re.finditer(
                            r"[^a-zA-Z`._/[\\-]+(" + word + r")[^a-zA-Z`_/\\-]+", line
                        )
                        for m in matches:
                            print(
                                f"::warning file={source},line={line_no},"
                                f"col={m.start()+3},endColumn={m.end()},"
                                f"title=spelling::Word '{word}' is misspelled.",
                                flush=True,
                            )

        sys.exit(0)
