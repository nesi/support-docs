#!/usr/bin/env python3

"""
Runs checks on article meta block and outputs in github action readable format. 
"""

__author__ = "cal w"

import re
import sys
import yaml
import os

# Warning level for missing parameters.
expected_parameters = {
    "title":                "",
    "template":             "",
    "description":          "warning",
    "icon":                 "info",
    "status":               "",
    "prereq":               "",
    "postreq":              "",
    "suggested":            "", # Add info here when implimented.
    "created_at":           "",
    "hidden":               "",
    "label_names":          "", # Add info here when implimented.
    "position":             "",
    "vote_count":           "",
    "vote_sum":             "",
    "zendesk_article_id":   "",
    "zendesk_section_id":   ""
}


def main():
    """ Main entry point of the app """
    input_files = sys.argv[1:]

    for input_file in input_files:
        with open(input_file, 'r') as f:
            contents = f.read()
            match = re.match(r"---\n([\s\S]*)---", contents, re.MULTILINE)
            if not match:
                print(f"::error file={input_file},line=0,title=meta.parse::Meta block missing or malformed.")
                continue
            meta = yaml.safe_load(match.group(1))
            for check in all_checks:
                check(input_file, meta, contents)


def check_expected_parameters(path, meta, contents):
    """
    Check for unexpected keys, and confirm existance of required.
    """
    # Check if any unexpected keys.
    for key in meta.keys():
        if key not in expected_parameters.keys():
            print(f"::info file={path},line=0,title=meta.unexpected::Unexpected parameter '{key}'")

    # Yes this is 2 x O().   

    # Check that all required keys are present. 
    for key, value in expected_parameters.items():
        if value:
            if key not in meta.keys():
                print(f"::{value} file={path},line=0,title=meta.unexpected::Missing parameter '{key}'")


def check_title(path, meta, contents):
    return
    # path, file = os.path.split()
    # This would be where you check title correctness.


all_checks = [check_expected_parameters, check_title]


if __name__ == "__main__":
    main()
