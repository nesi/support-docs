"""
Allows injection of variables into macro stage of rendering.
This allows for arbitrary use of variables in ARTICLES, (e.g. `docs/.md`).
As opposed to `mkdocs_hooks.py` which works only in template step, (e.g. `overrides/*.html`).
If this is confusing, ask Cal to explain.
"""

import os
import json

from jinja2 import pass_context

module_list_path = os.getenv("MODULE_LIST_PATH", "docs/assets/module-list.json")
tag_index_path = os.getenv("TAG_INDEX_PATH", "docs/assets/tag-index.json")


# Copied from mkdocs_hooks.py, not imported: mkdocs and mkdocs-macros load their
# hook module through different mechanisms, and a cross-file import can't
# reliably resolve `mkdocs_hooks` under both.
@pass_context
def safe_include(context, name, **kwargs):
    """Like `{% include %}`, but renders as "" instead of raising."""
    try:
        template = context.environment.get_template(name)
        return template.render({**context.get_all(), **kwargs})
    except Exception as e:
        print(f"::WARNING file={name},title=safe_include_failed,col=0,endColumn=0,line=0::{e}")
        return ""


class CaseInsensitiveDict(dict):
    """Dict wrapper allowing `applications[app_name]` lookups regardless of case."""

    def __init__(self, data):
        super().__init__(data)
        self._lower_keys = {k.lower(): k for k in data}

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return super().__getitem__(self._lower_keys[key.lower()])

    def __contains__(self, key):
        return super().__contains__(key) or key.lower() in self._lower_keys

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default


def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    env.variables.applications = CaseInsensitiveDict(json.load(open(module_list_path)))
    tag_index = json.load(open(tag_index_path))
    env.macro(safe_include, "safe_include")

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
