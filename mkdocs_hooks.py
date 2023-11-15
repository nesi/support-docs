import linkcheckmd as lc
import proselint as pl
import glob
from pathlib import Path
import json
import mkdocs.plugins
import os

module_list_path = os.getenv("MODULE_LIST_PATH", "docs/assets/module-list.json")

def on_env(env, config, files, **kwargs):
    # add entire module list to keyword 'applications
    env.globals["applications"] = json.load(open(module_list_path))

    # env.globals["domains"]=json.load(open('../tags/domains.json')).keys() # Needs list of cannon domains to make into

    # For image paths.
    # cant remember what this line does, if anything.
    # env.globals["includes"] = os.path.abspath("")
   
    # Debugging
    # for symbol, value in locals().items():
    #     print(symbol, value)

def check_links(*args, **kwargs):
    print("running link checker")
    # lc.check_links("docs", ext=".md", recurse=True, use_async=True)


def lint(*args, **kwargs):
    output = {}
    print("running linter")
    for file in glob.iglob("docs/**/*.md", recursive=True):
        with open(file, "r") as f:
            output[Path(file).stem] = pl.tools.lint(f.read())
    with open("lint_report.json", "w+") as f:
        f.write(json.dumps(output))
    print(output)
