#!/usr/bin/env python3

"""
Runs checks on article meta block and outputs in github action readable format
"""

__author__ = "cal w"

import re
import sys
import yaml

# Ignore files if they match this regex
EXCLUDED_FROM_CHECKS = [r"docs/assets/.*", r"index.html"]

# Constants for use in checks.
MAX_TITLE_LENGTH = 24
MIN_TAGS = 2

# Warning level for missing parameters.
EXPECTED_PARAMETERS = {
    "title": "",
    "template": ["main.html", "supported_apps.html"],
    "description": "",
    "icon": "",
    "status": ["new", "deprecated"],
    "prereq": "",
    "postreq": "",
    "suggested": "",    # Add info here when implimented.
    "created_at": "",
    "hidden": [True, False],
    "tags": "",         # Add info here when implimented.
    "weight": "",
    "vote_count": "",
    "vote_sum": "",
    "zendesk_article_id": "",
    "zendesk_section_id": "",
}


def main():
    input_files = sys.argv[1:]
    global title, title_from_h1, title_from_filename, input_file, meta, contents, title

    for input_file in input_files:
        if any(re.match(pattern, input_file) for pattern in EXCLUDED_FROM_CHECKS):
            continue
        with open(input_file, "r") as f:
            contents = f.read()
            match = re.match(r"---\n([\s\S]*?)---", contents, re.MULTILINE)
            if not match:
                print(
                    f"::warning file={input_file},title=meta.parse::Meta block missing or malformed."
                )
                meta = {}
            else:
                meta = yaml.safe_load(match.group(1))

            title_from_filename = _title_from_filename()
            title_from_h1 = _title_from_h1()
            title = meta["title"] if "title" in meta else "" or title_from_h1 or title_from_filename

            for check in CHECKS:
                _run_check(check)


def _run_check(f):
    for r in f():
        message = r.pop('message', 'something wrong')
        level = r.pop('level', 'warning')  # Defult is warning.

        print(f"::{level} file={input_file},title={f.__name__},{','.join(f'{k}={v}' for k,v in r.items())}::{message}")


def _title_from_filename():
    """
    I think this is the same as what mkdocs does.
    """
    name = " ".join(input_file.split("/")[-1][0:-3].split("_"))
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
        yield {"line": 0, "message": "Missing 'description' from front matter."}


def title_length():
    if len(title) > MAX_TITLE_LENGTH:
        yield {"line": _get_lineno(r"^title:.*$"),
               "message": f"Title '{title}' is too long. \
Try to keep it under {MAX_TITLE_LENGTH} characters to avoid word wrapping in the nav."}


def minimum_tags():
    if "tags" not in meta or not isinstance(meta["tags"], list):
        yield {"line": 0, "message": "'tags' property in meta is missing or malformed."}
    elif len(meta["tags"]) < MIN_TAGS:
        yield {"line": _get_lineno(r"^tags:.*$"), "message": "Try to include at least 2 'tags'\
(helps with search optimisation)."}


def click_here():
    """
    not currenlty identified by vscode for some reaon.
    """
    i = 0
    for line in contents.split("\n"):
        i += 1
        m = re.search(r"\[here\]\(.*\)", line)
        if m:
            yield {"line": i, "col": m.start()+1, "endColumn": m.end()-1, "message":
                   "Don't use 'here' for link text, impedes accessability."}


CHECKS = [title_redundant, title_length, meta_missing_description, meta_unexpected_key, minimum_tags, click_here]


if __name__ == "__main__":
    main()
