#!/usr/bin/env python3

# FIXME direct use of aspell might be simpler than postprocessing pyspelling

import sys
import time
from pathlib import Path

from pyspelling import spellcheck
from flashtext import KeywordProcessor

ALLOWABLE_TYPOS = 20

if __name__ == "__main__":

    count_typos = 0

    for source in sys.argv[1:]:
        print(f"Running Pyspelling on {source}")

        results = spellcheck(
            ".spellcheck.yml",
            names=["Markdown"],
            sources=[source],
            verbose=0,
            debug=True,
        )

        keyword_processor = KeywordProcessor(case_sensitive=True)
        for r in results:
            if not r.words:
                continue
            keyword_processor.add_keywords_from_list(r.words)

        source_md = Path(source).read_text().split("\n")

        for i, line in enumerate(source_md, start=1):
            for match in keyword_processor.extract_keywords(line, span_info=True):
                word, col_start, col_end = match
                print(
                    f"::warning file={source},line={i},"
                    f"col={col_start + 1},endColumn={col_end + 1},"
                    f"title=spelling::Word '{word}' is misspelled.",
                    flush=True,
                )
                count_typos += 1

    # FIXME terrible hack to make VSCode in codespace capture the error messages
    # see https://github.com/microsoft/vscode/issues/92868 as a tentative explanation
    time.sleep(5)
    exit(count_typos >= ALLOWABLE_TYPOS*(len(sys.argv)-1))
