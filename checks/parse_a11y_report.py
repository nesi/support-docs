#!/usr/bin/env python3

"""
Parse an AccessLint audit JSON report (checks/run_a11y_check.sh) into
github-recognised warning annotations. Reads from a file path argument, or
from stdin (e.g. `run_a11y_check.sh ... | parse_a11y_report.py`) if omitted.

AccessLint's own inline `::warning::` annotations only fire when a violation
has a JS/React source map back into the workspace - for a server-rendered
mkdocs site that never happens, so we annotate against the built HTML instead.
"""

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

SITE_DIR = Path("public")


def url_to_file(url):
    path = urlparse(url).path
    if not path or path.endswith("/"):
        path += "index.html"
    return SITE_DIR / path.lstrip("/")


def main(argv):
    if len(argv) > 2:
        print("Usage: parse_a11y_report.py [accesslint-report.json]", file=sys.stderr)
        return 1

    source = argv[1] if len(argv) == 2 else "<stdin>"
    try:
        raw = Path(argv[1]).read_text() if len(argv) == 2 else sys.stdin.read()
        report = json.loads(raw)
    except (OSError, json.JSONDecodeError) as e:
        print(f"::error file=checks/parse_a11y_report.py,title=bad_report::"
              f"Could not read {source} (run checks/run_a11y_check.sh first): {e}")
        return 1

    violations = report.get("violations", [])
    for v in violations:
        file = url_to_file(v["url"])
        print(
            f"::warning file={file},title={v['ruleId']},col=0,endColumn=0,line=0::"
            f"{v['message']} (impact={v['impact']}, selector={v['selector']})",
            flush=True,
        )

    pages = len(report.get("urls", []))
    print(f"Found {len(violations)} accessibility violations across {pages} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
