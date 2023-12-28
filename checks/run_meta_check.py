#!/usr/bin/python3
###!/usr/bin/env python3

"""
Runs checks on article meta block and outputs in github action readable format
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
    "tags": "",  # Add info here when implimented.
    "weight": "",
    "vote_count": "",
    "vote_sum": "",
    "zendesk_article_id": "",
    "zendesk_section_id": "",
}


def main():
    """Main entry point of the app"""

    ret_code = 0

    input_files = sys.argv[1:]
    global line_of_title, input_file, meta, contents, startline, endline

    for input_file in input_files:
        if any(re.match(pattern, input_file) for pattern in EXCLUDED_FROM_CHECKS):
            continue
        with open(input_file, "r") as f:
            contents = f.read()
            match = re.match(r"---\n([\s\S]*?)---", contents, re.MULTILINE)
            if not match:
                ret_code +=1
                print(
                    f"::warning file={input_file},title=meta.parse::Meta block missing or malformed."
                )
                continue
            meta = yaml.safe_load(match.group(1))
            endline = match.end()+1
            startline = match.start()+1
            line_of_title = (list(meta).index('title') if 'title' in meta else 1) + startline + 1
            for check in all_checks:
                ret_code += check()
    sys.exit(0)         
    # sys.exit(ret_code)


def get_page_title():
    """
    This is silly codegolf.
    Delete this before anyone sees.
    """

    def _title_from_filename(filename):
        """
        I think this is the same as what mkdocs does.
        """
        name = " ".join(filename[0:-3].split("_"))
        return name[0].upper() + name[1:]

    def _title_from_h1(contents):
        m = re.match(r"^ #(\S*)$", contents)
        return m.group(1) if m else ""

    def _compare(type1, title1, type2, title2):

        if title1 and title2:
            if title1 == title2:
                print(
                    f"::notice file={input_file},line={line_of_title},title=title.redundant::Title set in {type1} is redundant, already set in {type2}."
                )
            else:
                print(
                    f"::notice file={input_file},line={line_of_title},title=title.redundant::Title set in {type1} ({title1}) does not match title set in {type2} ({title2})."
                )

    if input_file == "index.md":
        return

    t = [
        ["meta", meta["title"] if "title" in meta else ""],
        ["header", _title_from_h1(contents)],
        ["filename", _title_from_filename(input_file.split("/")[-1])]
    ]

    _compare(*t[0], *t[1])
    _compare(*t[0], *t[2])
    _compare(*t[1], *t[2])

    return t[0][1] or t[1][1] or t[2][1]

    # path, file = os.path.split()
    # This would be where you check title correctness.


def check_expected_parameters():
    """
    Check for unexpected keys, and confirm existance of required.
    """
    ret_code = 0

    # Check if any unexpected keys.
    line_of_key = startline
    for key in meta.keys():
        line_of_key += 1
        if key not in EXPECTED_PARAMETERS.keys():
            ret_code += 1
            print(
                f"::warning file={input_file},line={line_of_key},title=meta.unexpected::Unexpected parameter in front-matter '{key}'"
            )

    # Yes this is 2 x O().

    # Check that all required keys are present.
    for key, value in EXPECTED_PARAMETERS.items():
        if value:
            if key not in meta.keys():
                ret_code += 1
                print(
                    f"::{value} file={input_file},line={startline},title=meta.unexpected::Missing parameter from front-matter '{key}'"
                )
    return ret_code


def check_article_titles():
    resolved_title = get_page_title()

    if len(resolved_title) > MAX_TITLE_LENGTH:
        f"::warning file={input_file},line={line_of_title},title=title.long::Title '{resolved_title}' is too long"
        return 1
    return 0


all_checks = [check_expected_parameters, check_article_titles]


if __name__ == "__main__":
    main()
