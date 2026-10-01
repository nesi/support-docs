#!/usr/bin/env python3

"""
Auto-fixes the 'absolute_site_link' warning from run_meta_check.py: rewrites
markdown links that point at this site by absolute URL (docs.nesi.org.nz/...)
into a link relative to the linking page, when the target can be resolved to
an actual file under docs/.

docs/redirect_map.yml is consulted as a fallback for links to a page that's
since moved/been renamed. Anything still unresolved after that - genuinely
deleted pages - is left untouched and printed under "Unresolved" for a human
to find the right target.
"""

import os
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

DOC_ROOT = Path("docs")
REDIRECT_MAP_PATH = DOC_ROOT / "redirect_map.yml"
EXCLUDED = r"docs/assets/.*"

LINK_RE = re.compile(
    r"\[([^\]]*)\]\(((?:https?:\/\/)?(?:www\.)?docs\.nesi\.org\.nz(\/[^)\s]*)?)\)",
    re.IGNORECASE,
)
FENCE_RE = re.compile(r"^\s*```.*$")


def site_path_of(path):
    """The site path a doc file is served at (eg. 'Data_Transfer/Data_Transfer_Overview')."""
    rel = path.relative_to(DOC_ROOT)
    rel = rel.parent if rel.stem == "index" else rel.with_suffix("")
    return str(rel).replace("\\", "/").strip("/")


def build_url_map():
    return {
        site_path_of(path): path
        for path in DOC_ROOT.rglob("*.md")
        if not re.match(EXCLUDED, str(path))
    }


def build_redirect_map():
    if not REDIRECT_MAP_PATH.exists():
        return {}
    raw = yaml.safe_load(REDIRECT_MAP_PATH.read_text()) or {}
    return {
        str(old).strip().removesuffix(".md").strip("/"): str(new).strip().removesuffix(".md").strip("/")
        for old, new in raw.items()
    }


def strip_index(site_path):
    if site_path == "index":
        return ""
    return site_path.removesuffix("/index")


def resolve(url, url_map, redirect_map):
    parts = urlsplit(url if "://" in url else f"https://{url}")
    site_path = unquote(parts.path).strip("/")
    fragment = f"#{parts.fragment}" if parts.fragment else ""

    seen = set()
    while site_path not in url_map and site_path not in seen:
        seen.add(site_path)
        if site_path in redirect_map:
            site_path = strip_index(redirect_map[site_path])
        elif f"{site_path}/index" in redirect_map:
            site_path = strip_index(redirect_map[f"{site_path}/index"])
        else:
            break

    target = url_map.get(site_path)
    return (target, fragment) if target else (None, None)


def relative_link(src_file, target_file):
    rel = Path(os.path.relpath(target_file, start=src_file.parent)).as_posix()
    return rel if rel.startswith(".") else f"./{rel}"


def fix_file(path, url_map, redirect_map, unresolved):
    original = path.read_text()
    lines = original.split("\n")
    in_code_block = False

    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        def repl(m):
            text, url = m.group(1), m.group(2)
            target, fragment = resolve(url, url_map, redirect_map)
            if target is None:
                unresolved.append((path, i + 1, url))
                return m.group(0)
            return f"[{text}]({relative_link(path, target)}{fragment})"

        lines[i] = LINK_RE.sub(repl, line)

    new_content = "\n".join(lines)
    if new_content == original:
        return False
    path.write_text(new_content)
    return True


def main():
    url_map = build_url_map()
    redirect_map = build_redirect_map()
    fixed_files = []
    unresolved = []

    for path in sorted(DOC_ROOT.rglob("*.md")):
        if re.match(EXCLUDED, str(path)):
            continue
        if fix_file(path, url_map, redirect_map, unresolved):
            fixed_files.append(path)

    for path in fixed_files:
        print(f"fixed: {path}")
    print(f"\nFixed links in {len(fixed_files)} file(s).")

    if unresolved:
        print(f"\nUnresolved (needs a human to find the right target), {len(unresolved)}:")
        for path, lineno, url in unresolved:
            print(f"  {path}:{lineno}: {url}")


if __name__ == "__main__":
    main()
