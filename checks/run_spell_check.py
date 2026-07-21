#!/usr/bin/env python3

# FIXME direct use of aspell might be simpler than postprocessing pyspelling

import sys
import time
from collections import Counter
from pathlib import Path

import yaml
from pyspelling import spellcheck
from pyspelling.filters import context as context_filter
from pyspelling.filters import url as url_filter
from flashtext import KeywordProcessor

ALLOWABLE_TYPOS = 20

CONFIG_FILE = ".spellcheck.yml"


def build_context_filter():
    """Build a pyspelling ContextFilter using the same delimiters as .spellcheck.yml.

    This lets us recompute, on the raw source text, which regions pyspelling
    considers 'ignored' (fenced code, front matter, inline back ticks, link
    targets, macros, includes) so those regions can be excluded again below.
    """

    with open(CONFIG_FILE) as f:
        config = yaml.safe_load(f)

    for step in config["matrix"][0]["pipeline"]:
        if "pyspelling.filters.context" in step:
            cf = context_filter.ContextFilter(step["pyspelling.filters.context"])
            cf.setup()
            return cf

    return None


def ignored_spans(text, cf):
    """Return a sorted list of (start, end) character spans in `text` that
    pyspelling's context/url filters would strip out before spell checking.

    Words that are only found inside these spans should not be reported,
    even if the same word text is genuinely misspelled elsewhere in the
    visible prose of the file.
    """

    spans = []

    if cf is not None:
        norm_text = cf.norm_nl(text) if cf.line_endings else text
        index = 0
        end = len(norm_text)
        while index < end:
            m = cf.escapes.match(norm_text, pos=index) if cf.escapes else None
            if m:
                index = m.end(0)
                continue
            handled = False
            for delimiter in cf.delimiters:
                m = delimiter[0].match(norm_text, pos=index)
                if m:
                    spans.append((m.start(0), m.end(0)))
                    index = m.end(0)
                    handled = True
                    break
            if handled:
                continue
            index += 1

    # Bare URLs/emails (not wrapped in markdown link syntax) are stripped by
    # pyspelling.filters.url wherever they occur in the text.
    for pattern in (url_filter.RE_LINK, url_filter.RE_MAIL):
        for m in pattern.finditer(text):
            spans.append(m.span())

    spans.sort()
    return spans


def in_ignored_span(offset, spans):
    # Linear scan is fine here: spans per file are few relative to file size.
    return any(start <= offset < end for start, end in spans)


if __name__ == "__main__":

    count_typos = 0
    word_frequency = Counter()
    context_filter_instance = build_context_filter()

    for file in sys.argv[1:]:
        print(f"::DEBUG file={file},line=0,col=0,endColumn=0,title=file:: Running pyspelling on '{file}'")

        results = spellcheck(
            CONFIG_FILE,
            names=["Markdown"],
            sources=[file],
            verbose=0,
            debug=True,
        )

        keyword_processor = KeywordProcessor(case_sensitive=True)
        for r in results:
            if not r.words:
                continue
            keyword_processor.add_keywords_from_list(r.words)

        source_text = Path(file).read_text()
        spans = ignored_spans(source_text, context_filter_instance)
        source_md = source_text.split("\n")

        offset = 0
        for i, line in enumerate(source_md, start=1):
            for match in keyword_processor.extract_keywords(line, span_info=True):
                word, col_start, col_end = match
                if in_ignored_span(offset + col_start, spans):
                    continue
                print(
                    f"::warning file={file},line={i},"
                    f"col={col_start + 1},endColumn={col_end + 1},"
                    f"title=spelling::Word '{word}' is misspelled.",
                    flush=True,
                )
                count_typos += 1
                word_frequency[word] += 1
            offset += len(line) + 1

    with open("spellcheck.results", "w") as f:
        for word, count in word_frequency.most_common():
            f.write(f"{count}\t{word}\n")

    # FIXME terrible hack to make VSCode in codespace capture the error messages
    # see https://github.com/microsoft/vscode/issues/92868 as a tentative explanation
    time.sleep(5)
    # exit(count_typos >= ALLOWABLE_TYPOS*(len(sys.argv)-1))
