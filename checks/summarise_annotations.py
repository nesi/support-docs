#!/usr/bin/env python3

"""
Summarise check output as markdown, for a pull request comment.

ANNOTATIONS_DIR holds one file per check (e.g. `spelling.txt`).

Only findings on lines changed since BASE_REF are shown, so contributors aren't
shown problems they didn't introduce. Errors are always shown, as they block merging.

Set NEEDS to the JSON of the workflow's `needs` context to also report failed jobs.
"""

import html
import json
import os
import re
import subprocess
import sys
from pathlib import Path

MAX_ROWS_PER_FILE = 30
MAX_MESSAGE_LENGTH = 300
MAX_LENGTH = 60000  # GitHub comments are capped at 65536 characters.
ANNOTATION = re.compile(r"^::(error|warning|notice)(?: (.*?))?::(.*)$", re.IGNORECASE)


def changed_lines(base):
    """{file: set of added/modified line numbers} for every file changed since base."""
    diff = subprocess.run(["git", "diff", "-U0", "--no-color", f"{base}...HEAD"],
                          capture_output=True, text=True, check=True).stdout
    changed, file = {}, None
    for line in diff.splitlines():
        if line.startswith("+++ "):
            file = line[6:] if line.startswith("+++ b/") else None
            if file:
                changed[file] = set()
        elif line.startswith("@@") and file:
            m = re.match(r"@@ -\S+ \+(\d+)(?:,(\d+))?", line)
            start, count = int(m.group(1)), int(m.group(2) or 1)
            changed[file].update(range(start, start + count))
    return changed


def source_file(path):
    """Map a built html page (e.g. from the a11y check) back to its markdown source."""
    path = path.strip()
    if not path.startswith("public/"):
        return path
    page = path.removeprefix("public/").removesuffix("index.html").rstrip("/")
    for candidate in (f"docs/{page}.md", f"docs/{page}/index.md"):
        if os.path.exists(candidate):
            return candidate
    return path


def parse(annotations_dir):
    seen = set()
    for path in sorted(Path(annotations_dir).glob("*.txt")):
        for line in path.read_text().splitlines():
            m = ANNOTATION.match(line)
            if not m or line in seen:
                continue
            seen.add(line)
            props = dict(p.split("=", 1) for p in (m.group(2) or "").split(",") if "=" in p)
            rule = props.get("title", "").strip()
            # Some checks end messages with a redundant '(path:line:col)'.
            message = re.sub(r"\s*\([^()]*:\d+:\d+\)$", "", " ".join(m.group(3).split()))
            if len(message) > MAX_MESSAGE_LENGTH:
                message = message[:MAX_MESSAGE_LENGTH] + "…"
            yield {
                "level": m.group(1).lower(),
                "check": path.stem if rule in ("", path.stem) else f"{path.stem}: {rule}",
                "file": source_file(props.get("file", "")),
                "line": int(props.get("line", 0) or 0),
                "message": message,
            }


def cell(text):
    return html.escape(text, quote=False).replace("|", "\\|")


def table(by_file, expanded=False):
    """Collapsible table of findings for each file."""
    out = []
    for file, findings in by_file.items():
        out += [f"<details{' open' if expanded else ''}><summary><code>{file}</code> ({len(findings)})</summary>", "",
                "| Line | Check | Message |", "| --- | --- | --- |"]
        for f in sorted(findings, key=lambda f: f["line"])[:MAX_ROWS_PER_FILE]:
            out += [f"| {f['line'] or 'page'} | {cell(f['check'])} | {cell(f['message'])} |"]
        if len(findings) > MAX_ROWS_PER_FILE:
            out += [f"| | | …and {len(findings) - MAX_ROWS_PER_FILE} more, see the 'Checks' tab |"]
        out += ["", "</details>", ""]
    return out


def main(base, annotations_dir):
    changed = changed_lines(base)
    errors, warnings, notices = {}, {}, {}
    for f in parse(annotations_dir):
        # Errors block merging, so are shown wherever they are.
        if f["level"] == "error":
            errors.setdefault(f["file"], []).append(f)
        # Line 0 is a whole-page finding.
        elif f["file"] in changed and (f["line"] == 0 or f["line"] in changed[f["file"]]):
            by_file = warnings if f["level"] == "warning" else notices
            by_file.setdefault(f["file"], []).append(f)

    failed_jobs = [job for job, v in json.loads(os.getenv("NEEDS") or "{}").items() if v["result"] == "failure"]

    status = ""

    if errors:
        status += f"🛑 {sum(len(v) for v in errors.values())} errors "
    if warnings:
        status += f"⚠️ {sum(len(v) for v in warnings.values())} warnings "
    if notices:
        status += f"ℹ️ {sum(len(v) for v in notices.values())} "

    if not any([errors, warnings, notices]):
        status += "✅ Wow! Great job!"

    out = [status]


    # Errors already explain why a job failed, this catches failures that printed nothing (e.g. install errors).
    if failed_jobs and not errors:
        out += [f"Failed jobs: {', '.join(f'`{j}`' for j in failed_jobs)}.", ""]

    if errors:
        out = out + ["#### Errors Merging blocked" ] + table(errors, expanded=True)
    if warnings:
        out = out + ["#### Warnings"] + table(warnings)
    if notices:
        out = out + ["#### Notices"] +  table(notices)

    text = "\n".join(out)
    if len(text) > MAX_LENGTH:
        text = text[:MAX_LENGTH] + "\n\n…truncated, "
    text += "\n\n See the 'Checks' tab for the full output."
    print(text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
