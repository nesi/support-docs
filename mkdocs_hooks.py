"""
mkdocs_hooks allows injection of variables into templating stage of rendering.
This allows for arbitrary use of variables in TEMPLATE FILES, (e.g. `overrides/*.html`).
As opposed to `macro_hooks.py` which injects variables into macro rendering (e.g. `docs/*.md`).
If this is confusing, ask Cal to explain.
"""

import glob
from pathlib import Path
import json
import os

module_list_path = os.getenv("MODULE_LIST_PATH", "docs/assets/module-list.json")


def on_env(env, config, files, **kwargs):
    # add entire module list to keyword 'applications
    applications = json.load(open(module_list_path))
    env.globals["applications"] = applications
    # Domains actually in use, for the supported-apps filter UI - derived from
    # the data so it can't drift out of sync the way a hardcoded list would.
    env.globals["domain_whitelist"] = sorted({
        domain
        for app in applications.values()
        for domain in app.get("domains", [])
    })


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
