#!/usr/bin/env python3
"""Check built HTML for broken ARIA id references."""

from html.parser import HTMLParser
from pathlib import Path
import sys


class AriaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.add(d["id"])
        for key in ["aria-labelledby", "aria-describedby", "aria-controls"]:
            if key in d:
                for ref in d[key].split():
                    self.refs.append((key, ref, tag))


def main():
    base = Path("public")
    if not base.exists():
        print("::error file=checks/run_aria_check.py,title=missing_public_dir::public folder not found. Run mkdocs build first.")
        return 1

    broken = []
    for path in sorted(base.rglob("*.html")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        parser = AriaParser()
        parser.feed(text)
        for key, ref, tag in parser.refs:
            if ref not in parser.ids:
                broken.append((path, key, ref, tag))

    if broken:
        for path, key, ref, tag in broken:
            print(f"::error file={path},title=broken_aria_reference,col=0,endColumn=0,line=0::{key} reference '{ref}' missing id in tag <{tag}>")
        print(f"Found {len(broken)} broken aria references.")
        return 1

    print("ARIA reference check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
