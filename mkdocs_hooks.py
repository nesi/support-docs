"""
mkdocs_hooks allows injection of variables into templating stage of rendering.
This allows for arbitrary use of variables in TEMPLATE FILES, (e.g. `overrides/*.html`).
As opposed to `macro_hooks.py` which injects variables into macro rendering (e.g. `docs/*.md`).
If this is confusing, ask Cal to explain.
"""

import fnmatch
import glob
from pathlib import Path
import json
import os
import re

import yaml

module_list_path = os.getenv("MODULE_LIST_PATH", "docs/assets/module-list.json")

_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _page_description(path):
    """Return a page's front matter `description` as one line, or None."""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None
    match = _FRONT_MATTER.match(text)
    if not match:
        return None
    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        # checks/run_meta_check.py is what reports a malformed meta block; the build
        # itself should skip the page rather than fall over.
        return None
    if not isinstance(meta, dict):
        return None
    description = meta.get("description")
    if not isinstance(description, str):
        return None
    # Folded YAML descriptions span several lines; llms.txt entries are one line each.
    return " ".join(description.split()) or None


def on_config(config, **kwargs):
    """Rewrite the llmstxt section globs into explicit per-page entries.

    mkdocs-llmstxt takes link descriptions only from its own config - it never reads page
    front matter, and a glob entry hands every page it matches the same description.
    Expanding the globs here instead lets each llms.txt link carry its own description,
    which is what lets a reader pick a page without fetching several.

    Hooks are appended last in the plugin collection, so this runs after the plugin's own
    on_config. The plugin expands `sections` in on_files, so the rewrite still lands.
    """
    plugin = config.plugins.get("llmstxt")
    if plugin is None:
        return config

    docs_dir = Path(config.docs_dir)
    uris = sorted(p.relative_to(docs_dir).as_posix() for p in docs_dir.rglob("*.md"))

    sections = {}
    for section, patterns in plugin.config.sections.items():
        entries = []
        seen = set()
        for pattern in patterns:
            matches = sorted(fnmatch.filter(uris, pattern)) if "*" in pattern else [pattern]
            for uri in matches:
                if uri in seen:
                    continue
                seen.add(uri)
                description = _page_description(docs_dir / uri)
                entries.append({uri: description} if description else uri)
        sections[section] = entries

    plugin.config.sections = sections
    return config


def on_env(env, config, files, **kwargs):
    # add entire module list to keyword 'applications
    env.globals["applications"] = json.load(open(module_list_path))
    # env.globals["domains"]=json.load(open('../tags/domains.json')).keys() # Needs list of cannon domains to make into


def lint(*args, **kwargs):
    # Imported lazily: proselint pulls in google-re2 and a large rule set,
    # and this function is not part of the mkdocs build path.
    import proselint as pl

    output = {}
    print("running linter")
    for file in glob.iglob("docs/**/*.md", recursive=True):
        with open(file, "r") as f:
            output[Path(file).stem] = pl.tools.lint(f.read())
    with open("lint_report.json", "w+") as f:
        f.write(json.dumps(output))
    print(output)
