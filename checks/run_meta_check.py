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

#### Mkdocs Parameters

- `template` : which [template](#templates) to use.
- `title`    : [title](#title).

#### Material Parameters

- `description` : used for site meta.
- `icon`        : page icon.
- `status`      : `new`, `deprecated`.

#### Custom Parameters

- `prereq`      : List of prerequisites. Formatted in markdown. Will be rendered inside a admonation.
- `postreq`     : List of what next. Formatted in markdown. Will be rendered inside a admonation.

#### Zendesk Imported

Not used for anything currently. Info imported from Zendesk Page.

- `created_at`:
- `hidden`:
- `label_names`: []
- `position`:
- `vote_count`:
- `vote_sum`:
- `zendesk_article_id`:
- `zendesk_section_id`:

def main():
    """ Main entry point of the app """
    input_files = sys.argv[1:]

    for input_file in input_files:
        try:
            with open(input_file, 'r') as f:
                try:
                    contents = f.read()
                    match = re.match(r"---\n([\s\S]*)---", contents, re.MULTILINE)
                    meta = yaml.safe_load(match.group(1))
                except Exception as e:
                    print(f"::error file={input_file},line=0,title=meta.parse::Could not parse meta block. {e}")
                    continue
                for check in all_checks:
                    check(input_file, meta, contents)
        except FileNotFoundError as e:
            print(f"::info title=meta.parse::{e}")


def expected(path, meta, contents):
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
            if not key in meta.keys:
                print(f"::{value} file={path},line=0,title=meta.unexpected::Missing parameter '{key}'")

def title(path, meta, contents):
    path, file = os.path.split(input_file)

    # This would be where you check title correctness.


all_checks = [expected]

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
