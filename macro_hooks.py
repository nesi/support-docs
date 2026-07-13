"""
Allows injection of variables into macro stage of rendering.
This allows for arbitrary use of variables in ARTICLES, (e.g. `docs/.md`).
As opposed to `mkdocs_hooks.py` which works only in template step, (e.g. `overrides/*.html`).
If this is confusing, ask Cal to explain.
"""

import os
import json

module_list_path = os.getenv("MODULE_LIST_PATH", "docs/assets/module-list.json")
tag_index_path = os.getenv("TAG_INDEX_PATH", "docs/assets/tag-index.json")


def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    env.variables.applications = json.load(open(module_list_path))
    tag_index = json.load(open(tag_index_path))

    @env.macro
    def pages_with_tag(tag):
        entries = tag_index.get(tag.lower(), [])
        try:
            current_dir = os.path.dirname(env.page.file.src_path)
        except AttributeError:
            return entries
        return [
            {"title": e["title"], "path": os.path.relpath(e["path"], current_dir)}
            for e in entries
        ]
