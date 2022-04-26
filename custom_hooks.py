import linkcheckmd as lc
import proselint as pl
import glob
from pathlib import Path
import json


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
