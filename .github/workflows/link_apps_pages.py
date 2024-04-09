#!/usr/bin/env python3


import os
import re
import json
import yaml

"""
Quick and dirty script to associate support pages with apps in module list.
"""


MODULE_LIST_PATH = os.getenv("MODULE_LIST_PATH", "docs/assets/module-list.json")

# Relative to doc directory.
DOC_ROOT = os.getenv("DOC_ROOT", "docs")
APPS_PAGES_PATH = os.getenv("APPS_PAGES_PATH", "Scientific_Computing/Supported_Applications")
BASE_URL = os.getenv("BASE_URL", "https://nesi.github.io/support-docs/")

module_list = json.load(open(MODULE_LIST_PATH))

for input_file in os.listdir(os.path.join(DOC_ROOT, APPS_PAGES_PATH)):
    if input_file == "index.md":
        continue
    with open(os.path.join(DOC_ROOT, APPS_PAGES_PATH, input_file), "r") as f:
        contents = f.read()

        # Read yaml block
        match = re.match(r"---\n([\s\S]*?)---", contents, re.MULTILINE)
        if not match:
            print(
                f"::warning file={input_file},title=meta.parse::Meta block missing or malformed."
            )
            meta = {}
        else:
            meta = yaml.safe_load(match.group(1))

        name = " ".join(input_file.split("/")[-1][0:-3].split("_"))
        title_from_filename = name[0].upper() + name[1:]
        app = meta["title"] if "title" in meta else "" or title_from_filename

        if app in module_list:
            page_link = os.path.join(BASE_URL, APPS_PAGES_PATH, app)
            if module_list[app]["support"] and module_list[app]["support"] != page_link:
                print(f"::warning file={os.path.join(DOC_ROOT, APPS_PAGES_PATH, input_file)},\
title=docpath.change:: Support doc reference for {app} changed from '{module_list[app]['support']}' to '{page_link}'")
            module_list[app]["support"] = page_link
            for tag in meta["tags"]:
                if tag not in module_list[app]["domains"]:
                    module_list[app]["domains"] += [tag]
        else:
            print(
                f"::warning file={os.path.join(DOC_ROOT, APPS_PAGES_PATH, input_file)},\
title=missing.module::'{input_file} has no corresponding module in {MODULE_LIST_PATH}.'"
            )

with open(MODULE_LIST_PATH, "w") as f:
    f.write(json.dumps(module_list, indent=4))
