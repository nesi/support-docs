#!/usr/bin/env python3

"""
Runs checks on article meta block and outputs in github action readable format
"""

__author__ = "cal w"

import re
import sys
import yaml
import os
import time
from pathlib import Path

# Ignore files if they match this regex
EXCLUDED_FROM_CHECKS = [r"docs/assets/.*", r".*/index\.html",  r".*/index\.md", r".*\.pages\.yml"]

msg_count = {"debug": 0, "notice": 0, "warning": 0, "error": 0}

# Constants for use in checks.

MAX_TITLE_LENGTH = 28   # As font isn't monospace, this is only approx
MAX_HEADER_LENGTH = 32  # minus 2 per extra header level
MIN_TAGS = 2
RANGE_SIBLING = [4, 8]
DOC_ROOT = "docs"

# Warning level for missing parameters.
EXPECTED_PARAMETERS = {
    "title": "",
    "template": ["main.html", "supported_apps.html", "updates.html"],
    "description": "",
    "icon": "",
    "status": ["new", "deprecated"],
    "prereq": "",
    "postreq": "",
    "suggested": "",    # Add info here when implimented.
    "created_at": "",
    "tags": "",         # Add info here when implimented.
    "search": "",
    "hide": ["toc", "nav", "tags"],
}


def main():
    # Per file variables
    global input_path, title_from_h1, title_from_filename, title, meta, contents, input_path

    # Walk variables
    global lineno, line, in_code_block, last_header_level, last_header_lineno, sibling_headers

    global toc, toc_parents, header

    inputs = sys.argv[1:]

    for input_string in inputs:

        input_path = Path(input_string)
        if any(re.match(pattern, input_string) for pattern in EXCLUDED_FROM_CHECKS):
            continue
        _nav_check()
        with open(input_path, "r") as f:
            _emit("", {"level": "debug", "file":  input_path, "message": f"Checking meta for {f.name}"})
            try:
                contents = f.read()
                match = re.match(r"---\n([\s\S]*?)---", contents, re.MULTILINE)
                if not match:
                    _emit("meta.parse", {"file": input_path, "col": 0, "endColumn": 99, "line": 1,
                          "message": "Meta block missing or malformed."})
                    meta = {}
                else:
                    meta = yaml.safe_load(match.group(1))

                title_from_filename = _title_from_filename()
                title_from_h1 = _title_from_h1()
                title = meta["title"] if "title" in meta else "" or title_from_h1 or title_from_filename
                # global lineno, line, in_code_block, last_header_level, last_header_lineno, sibling_headers

                header = ""
                lineno = 0
                in_code_block = False
                toc_parents = [title]
                toc = {title: {"level": 1, "lineno": 0, "children": {}}}

                for line in contents.split("\n"):
                    lineno += 1
                    for check in WALKCHECKS:
                        in_code_block = not in_code_block if re.match(r"^\s*```\s?\w*$", line) else in_code_block
                        _get_nav_tree()
                        _run_check(check)
                for check in ENDCHECKS:
                    _run_check(check)
            except Exception as e:
                _emit("misc", {"level": "error", "file": input_path, "message": e})


def _run_check(f):
    for r in f():
        _emit(f.__name__, r)


def _emit(f, r):
    msg_count[r.get('level', 'warning')] += 1
    print(f"::{r.get('level', 'warning')} file={input_path},title={f},col={r.get('col', 0)},endColumn={r.get('endColumn', 99)},line={r.get('line', 1)}::{r.get('message', 'something wrong')}")
    sys.stdout.flush()
    time.sleep(0.01)


def _title_from_filename():
    """
    I think this is the same as what mkdocs does.
    """
    name = " ".join(input_path.name[0:-3].split("_"))
    return name[0].upper() + name[1:]


def _title_from_h1():
    m = re.search(r"^ #(\S*)$", contents, flags=re.MULTILINE)
    return m.group(1) if m else ""


def _get_lineno(pattern):
    i = 1
    for line in contents.split("\n"):
        m = re.match(pattern, line)
        if m:
            return i
        i += 1
    return 0


def _get_nav_tree():
    """Makes a nice dictionary of header tree"""
    global toc, toc_parents

    def _unpack(toc, a):
        if len(a) < 1:
            return toc
        if len(a) < 2:
            return toc[a[0]]
        return _unpack(toc[a[0]]["children"], a[1:])

    try:
        if in_code_block:
            return

        header_match = re.match(r"^(#+)\s*(.*)$", line)

        if not header_match:
            return

        header_level = len(header_match.group(1))
        header_name = header_match.group(2)

        if header_level == 1:
            toc = {header_name: {"lineno": lineno, "children": {}}}
            toc_parents = [header_name]

        while header_level < len(toc_parents)+1:
            toc_parents.pop(-1)

        _unpack(toc, toc_parents)["children"][header_name] = {"level": header_level, "lineno": lineno, "children": {}}
        toc_parents += [header_name]
    except Exception:
        _emit("misc.nav", {"level": "error", "file": input_path,
              "message": "Failed to parse Nav tree. Something is very wrong."})


def _nav_check():
    try:
        doc_root = Path(DOC_ROOT).resolve()
        rel_path = input_path.resolve().relative_to(doc_root)
        for i in range(1, len(rel_path.parts)):
            num_siblings = 0
            for file_name in os.listdir(doc_root.joinpath(Path(*rel_path.parts[:i]))):
                if not any(re.match(pattern, file_name) for pattern in EXCLUDED_FROM_CHECKS):
                    num_siblings += 1
            if num_siblings < RANGE_SIBLING[0]:
                _emit("meta.siblings", {"file": input_path, "message": f"Parent category \
    '{rel_path.parts[i-1]}' has too few children ({num_siblings}). Try to nest '{RANGE_SIBLING[0]}' or more \
    items here to justify it's existence."})
            elif num_siblings > RANGE_SIBLING[1]:
                _emit("meta.siblings", {"file": input_path, "message": f"Parent category \
    '{rel_path.parts[i-1]}' has too many children ({num_siblings}). Try to keep number of items in a category \
    under '{RANGE_SIBLING[1]}', maybe add some new categories?"})
    except ValueError as e:
        _emit("meta.nav", {"file": input_path, "level": "error", "message": f"{e}. Nav checks will be skipped"})


def title_redundant():
    lineno = _get_lineno(r"^title:.*$")
    if "title" in meta.keys() and title_from_filename == meta["title"]:
        yield {"level": "notice", "line": lineno, "message": "Title set in meta is redundant as it is already set in filename."}
    if "title" in meta.keys() and title_from_h1 == meta["title"]:
        yield {"level": "notice", "line": lineno, "message": "Title set in h1 is redundant as it is already set in filename."}
    if title_from_filename == title_from_h1:
        yield {"level": "notice", "line": lineno, "message": "Title set in meta is redundant as it is already set in h1."}


def meta_unexpected_key():
    """
    Check for unexpected keys.
    """
    for key, value in meta.items():
        if key not in EXPECTED_PARAMETERS.keys():
            yield {"line": _get_lineno(r"^" + key + r":.*$"),
                   "message": f"Unexpected parameter in front-matter '{key}'"}
        elif EXPECTED_PARAMETERS[key] and value not in EXPECTED_PARAMETERS[key]:
            yield {"level": "error", "line": _get_lineno(r"^status:.*$"),
                   "message": f"'{value}' is not valid for {key}. [{','.join(EXPECTED_PARAMETERS[key])}]"}


def meta_missing_description():
    if "description" not in meta.keys() or len(meta["description"]) < 1:
        yield {"message": "Missing 'description' from front matter."}


def title_length():
    if len(title) > MAX_TITLE_LENGTH:
        yield {"line": _get_lineno(r"^title:.*$"),
               "message": f"Title '{title}' is too long. \
Try to keep it under {MAX_TITLE_LENGTH} characters to avoid word wrapping in the nav."}


def minimum_tags():
    if "tags" not in meta or not isinstance(meta["tags"], list):
        yield {"message": "'tags' property in meta is missing or malformed."}
    elif len(meta["tags"]) < MIN_TAGS:
        yield {"line": _get_lineno(r"^tags:.*$"), "message": "Try to include at least 2 'tags'\
(helps with search optimisation)."}


def click_here():
    """
    Click [here](for more details)
    """
    if in_code_block:
        return

    m1 = re.search(r"\[.*\s?here\s?.*\]\(.*\)", line, re.IGNORECASE)
    if m1:
        yield {"line": lineno, "col": m1.start()+1, "endColumn": m1.end()-1, "message": "Don't use 'here' for link text, impedes accessability."}

    # Impliment check for html links when I can be fd.
    # m2 = re.search(r"\[here\]\(.*\)", line)


def walk_toc():
    def _count_children(d):
        only_child = (len(d["children"]) == 1)
        for title, c in d["children"].items():
            if only_child:
                yield {"line": c['lineno'], "message": f"Header '{title}' is a useless only-child. Give it siblings or remove it."}
            # As header gets deeper nested, it will have less horizontal room in toc.
            if len(title) > (MAX_HEADER_LENGTH - (2*c["level"])):
                yield {"line": c['lineno'], "message": f"Header '{title}' is too long. \
 Try to keep it under {MAX_HEADER_LENGTH} characters to avoid word wrapping in the toc."}
            for y in _count_children(c):
                yield y
    for d in toc.values():
        for y in _count_children(d):
            yield y


# For checks to run on page as a whole
ENDCHECKS = [title_redundant, title_length, meta_missing_description, meta_unexpected_key, minimum_tags,
             walk_toc]

# Checks to be run on each line
WALKCHECKS = [click_here]


if __name__ == "__main__":
    main()

    # FIXME terrible hack to make VSCode in codespace capture the error messages
    # see https://github.com/microsoft/vscode/issues/92868 as a tentative explanation
    time.sleep(5)

    # Arbitrary weighting whether to fail check or not
    exit((100 * (len(sys.argv)-1)) < msg_count["notice"] + (30 * msg_count["warning"] + (100 * msg_count["error"])))
