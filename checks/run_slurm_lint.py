#!/usr/bin/env python3

"""
Runs checks on slurm scrips found in code and outputs in github action readable format
"""

__author__ = "cal w"

import re
import sys
import time
from pathlib import Path

msg_count = {"debug": 0, "notice": 0, "warning": 0, "error": 0}

LINES_AFTER_SHEBANG = 1
LINES_AFTER_HEADER = 1
SHEBANG = r"^#!\/bin\/bash -e\s*$"
SBATCH_HEADER = r"^(.*)#SBATCH\s*(-[^=\s]*)([\s=]*)(\S*.*?)(#.*)?$"
SBATCH_DELIM = r"=|\s+"

REQUIRED_SBATCH_HEADER = [
    {"long": "--job-name", "short": "-j"},
    {"long": "--account", "short": "-A"},
    {"long": "--time", "short": "-t"},
]

# Not used yet
ALLOWED_SBATCH_HEADER = [
    {"long": "--cpus-per-task", "short": "-c"},
    {"long": "--array", "short": "-a"},
    {"long": "--dependency", "short": "-d"},
    {"long": "--gpus-per-node", "short": ""},
    {"long": "--hint", "short": ""},
    {"long": "--mem=", "short": ""}
]


def main():
    # Per file variables
    global input_path, title_from_h1, title_from_filename, title, meta, contents, input_path

    # Walk variables
    global lineno, line, in_code_block, last_header_level, last_header_lineno, sibling_headers

    global toc, toc_parents, header

    inputs = sys.argv[1:]

    for input_string in inputs:

        input_path = Path(input_string)
        with open(input_path, "r") as f:
            contents = f.read()
            for lineno, indent, slurm in finditer2(r"\n( *)```\s*sl.*\n([\s\S\n]*?)\n\s*```", contents, re.MULTILINE):
                #try:
                parse_script(lineno+3, indent, slurm)
                #except Exception as e:
                #    print(f"::ERROR file={input_path},title=failed_to_parse, col=0, endColumn=99, line={lineno}::Failed to parse slurm script {e}")


def parse_script(start_linno, indent, slurm):
    global step, n_lines_after_shebang, n_lines_after_header, line, uses_equals_delim, uses_whitespace_delim
    global match_header_line, start_of_header, slurm_headers

    uses_equals_delim = False
    uses_whitespace_delim = False

    def _run_check(f):
        for r in f():
            msg_count[r.get('level', 'warning')] += 1
            print(f"::{r.get('level', 'warning')} file={input_path},title={f.__name__}," +
                  f"col={r.get('col', 0) + indent},endColumn={r.get('endColumn', 99) + indent}," +
                  f"line={start_linno + r.get('line', lineno)}::{r.get('message', 'something wrong')}")
            sys.stdout.flush()
            time.sleep(0.01)

    n_lines_after_shebang = 0
    n_lines_after_header = 0
    slurm_headers = []

    start_of_header = 0
    end_of_header = 0
    step = 0    # 0 : shebang
                # 1 : slurm header
                # 2 : bash
    for lineno, line in enumerate(slurm.split("\n")):
        line = line.removeprefix(' '*indent)
        if lineno == 0:
            _run_check(slurm_shebang)
            continue
        if step == 0:
            if re.match(r"^\s*$", line):
                n_lines_after_shebang += 1
            elif re.match(SBATCH_HEADER, line):
                _run_check(lines_after_shebang)
                step = 1
                start_of_header = lineno
            else:
                _run_check(content_before_slurm_header)
        if step == 1:
            if re.match(r"^\s*$", line):
                n_lines_after_header += 1
                continue
            match_header_line = re.match(SBATCH_HEADER, line)
            slurm_headers.append(match_header_line)
            if match_header_line:
                for check in SBATCH_HEADER_WALK:
                    _run_check(check)
            else:
                step = 2
                end_of_header = line
                for check in SBATCH_HEADER_ALL:
                    _run_check(check)

        # elif :


def finditer2(pattern, string, flags):
    """
    A version of ``re.finditer`` that returns ``(match, line_number)`` pairs.
    """
    matches = list(re.finditer(pattern, string, flags))
    if matches:
        end = matches[-1].start()
        # -1 so a failed `rfind` maps to the first line.
        newline_table = {-1: 0}
        for i, m in enumerate(re.finditer("\\n", string), 1):
            # Don't find ncewlines past our last match.
            offset = m.start()
            if offset > end:
                break
            newline_table[offset] = i

        # Failing to find the newline is OK, -1 maps to 0.
        for m in matches:
            newline_offset = string.rfind("\n", 0, m.start())
            line_number = newline_table[newline_offset]
            yield (line_number, len(m.group(1)), m.group(2))


def slurm_shebang():
    if not re.match(SHEBANG, line):
        yield {"message": f"Your shebang was '{line}', should use '{SHEBANG}'"}


def lines_after_shebang():
    if n_lines_after_shebang != LINES_AFTER_SHEBANG:
        yield {"level": "notice", "message": f"There are {n_lines_after_shebang} blank lines after the shebang, should be {LINES_AFTER_SHEBANG}."}


def content_before_slurm_header():
    yield {"level": "error", "message": f"There is text ('{line}') between the shebang and slurm header. This is not a valid SLURM script."}


def malformed_delimiter():
    global uses_equals_delim, uses_whitespace_delim
    delim = match_header_line.group(3)
    if delim == "=":
        uses_equals_delim = True
        yield {"level": "notice", "message": "Whitespace is preffered SLURM header delimiter."}
    elif delim.isspace():
        uses_whitespace_delim = True
    else:
        yield {"level": "error", "message": f"'{delim}' is not a valid SLURM header delimiter."}


def inconsistant_delimiter():
    if uses_equals_delim and uses_whitespace_delim:
        yield {"message": "Header uses both whitespace and '=' delimiters.", "line": start_of_header}


def short_option():
    if not match_header_line.group(2)[:2] == "--":
        yield {"level": "notice", "col": 8, "endColumn": 8 + len(match_header_line.group(2)), 
               "message": f"Using short form flag '{match_header_line.group(2)}'. Long form is prefered."}


def minimum_options():
    for header in REQUIRED_SBATCH_HEADER:
        for h in slurm_headers:
            if not h:
                continue
            a = h.group(2)
            if a == header["long"] or a == header["short"]:
                break
        else:
            yield {"message": f"Script header must contain \'{header['long']}\'.",
                   "line": start_of_header}


SBATCH_HEADER_WALK = [malformed_delimiter, short_option]
SBATCH_HEADER_ALL = [inconsistant_delimiter, minimum_options]

if __name__ == "__main__":
    main()

    # FIXME terrible hack to make VSCode in codespace capture the error messages
    # see https://github.com/microsoft/vscode/issues/92868 as a tentative explanation
    time.sleep(5)

    # Arbitrary weighting whether to fail check or not
    exit(100*(len(sys.argv)-1) < msg_count["notice"] + (30 * msg_count["warning"] + (100 * msg_count["error"])))
