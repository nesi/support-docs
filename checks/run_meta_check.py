#!/usr/bin/env python3

"""
Runs checks on article meta block and outputs in github action readable format. 
"""

__author__ = "cal w"

import re
import sys
import yaml

# Ignore files if they match this regex
EXCLUDED_FROM_CHECKS = [r"docs/assets/.*"]
MAX_TITLE_LENGTH = 28

# Warning level for missing parameters.
EXPECTED_PARAMETERS = {
    "title": "",
    "template": "",
    "description": "warning",
    "icon": "notice",
    "status": "",
    "prereq": "",
    "postreq": "",
    "suggested": "",  # Add info here when implimented.
    "created_at": "",
    "hidden": "",
    "label_names": "",  # Add info here when implimented.
    "position": "",
    "vote_count": "",
    "vote_sum": "",
    "zendesk_article_id": "",
    "zendesk_section_id": "",
}


def main():
    """Main entry point of the app"""
    input_files = sys.argv[1:]

    for input_file in input_files:
        if any(re.match(pattern, input_file) for pattern in EXCLUDED_FROM_CHECKS):
            continue
        with open(input_file, "r") as f:
            contents = f.read()
            match = re.match(r"---\n([\s\S]*?)---", contents, re.MULTILINE)
            if not match:
                print(
                    f"::warning file={input_file},line=0,title=meta.parse::Meta block missing or malformed."
                )
                continue
            meta = yaml.safe_load(match.group(1))
            for check in all_checks:
                check(input_file, meta, contents)


def page_title(input_file, meta, contents):
    """
    This is silly codegolf.
    Delete this before anyone sees.
    """

    if input_file == "index.md":
        return

    def _compare(c1, c2):
        if (c1[0] == c2[0]) or not (c1[1] and c2[1]):
            return c1[1]
        if c1[1] == c2[1]:
            print(
                f"::notice file={input_file},line=0,title=title.redundant::Title set in {c1[0]} is redundant."
            )
        else:
            print(f"::notice file={input_file},line=0,title=title.mismatch::Title in {c1[0]}('{c1[1]}') \
doesn't match that set in {c2[0]} ('{c2[1]}')")
        return c2[1]

    t = {
        "filename": title_from_filename(input_file.split("/")[-1]),
        "header": title_from_h1(contents),
        "meta": meta["title"] if "title" in meta else ""
    }
    return [x for x in reversed([_compare(i, j) for i in t.items() for j in t.items()]) if x][-1]


def title_from_filename(filename):
    """
    I think this is the same as what mkdocs does.
    """
    name_parts = filename[0:-3].split("_")
    name_parts[0] = name_parts[0].capitalize()
    return " ".join(name_parts)


def title_from_h1(contents):
    m = re.match(r"^ #(\S*)$", contents)
    return m.group(1) if m else ""


def check_title(path):
    if (path) > 28:
        f"::warning file={path},line=0,title=title.long::Title '{path}' is too long"

    # path, file = os.path.split()
    # This would be where you check title correctness.

def check_expected_parameters(path, meta, contents):
    """
    Check for unexpected keys, and confirm existance of required.
    """
    return
    # Check if any unexpected keys.
    for key in meta.keys():
        if key not in EXPECTED_PARAMETERS.keys():
            print(
                f"::notice file={path},line=0,title=meta.unexpected::Unexpected parameter '{key}'"
            )

    # Yes this is 2 x O().

    # Check that all required keys are present.
    for key, value in EXPECTED_PARAMETERS.items():
        if value:
            if key not in meta.keys():
                print(
                    f"::{value} file={path},line=0,title=meta.unexpected::Missing parameter '{key}'"
                )


def check_article_titles(path, meta, contents):
    check_title(page_title(path, meta, contents))


all_checks = [check_expected_parameters, check_article_titles]


if __name__ == "__main__":
    main()
