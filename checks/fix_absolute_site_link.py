#!/usr/bin/env python3

"""
Auto-fixes the 'absolute_site_link' warning from run_meta_check.py: rewrites
markdown links that point at this site by absolute URL (docs.nesi.org.nz/...)
into a link relative to the linking page, when the target can be resolved to
an actual file under docs/.

Many of these absolute URLs are stale, pointing at a pre-restructure site
layout (eg. 'General/Announcements/...' instead of 'Announcements/...').
docs/redirect_map.yml (used by the mkdocs-redirects-style plugin to 301 old
URLs to their new home) is consulted as a fallback for those. Anything still
unresolved after that - genuinely deleted pages - is left untouched and
printed under "Unresolved" for a human to find the right target.
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

DOC_ROOT = Path("docs")
REDIRECT_MAP_PATH = DOC_ROOT / "redirect_map.yml"
EXCLUDED_FROM_CHECKS = [
    r"docs/assets/.*",
]

LINK_RE = re.compile(
    r"\[([^\]]*)\]\(((?:https?:\/\/)?(?:www\.)?docs\.nesi\.org\.nz(\/[^)\s]*)?)\)",
    re.IGNORECASE,
)
FENCE_RE = re.compile(r"^\s*```.*$")


def build_url_map():
    """Maps a site path (eg. 'Data_Transfer/Data_Transfer_Overview') to its source file."""
    url_map = {}
    for path in DOC_ROOT.rglob("*.md"):
        rel = str(path)
        if any(re.match(pattern, rel) for pattern in EXCLUDED_FROM_CHECKS):
            continue
        site_rel = path.relative_to(DOC_ROOT)
        if site_rel.stem == "index":
            site_path = str(site_rel.parent).replace("\\", "/")
            if site_path == ".":
                site_path = ""
        else:
            site_path = str(site_rel.with_suffix("")).replace("\\", "/")
        url_map[site_path.strip("/")] = path
    return url_map


def build_redirect_map():
    """Maps an old site path (eg. 'General/FAQs/Foo') to its new site path."""
    if not REDIRECT_MAP_PATH.exists():
        return {}
    raw = yaml.safe_load(REDIRECT_MAP_PATH.read_text()) or {}
    redirect_map = {}
    for old, new in raw.items():
        old_path = str(old).strip().removesuffix(".md").strip("/")
        new_path = str(new).strip().removesuffix(".md").strip("/")
        redirect_map[old_path] = new_path
    return redirect_map


def resolve(url, url_map, redirect_map):
    parts = urlsplit(url if "://" in url else f"https://{url}")
    site_path = unquote(parts.path).strip("/")
    fragment = f"#{parts.fragment}" if parts.fragment else ""

    def strip_index(p):
        return p[: -len("/index")] if p.endswith("/index") else ("" if p == "index" else p)

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
    if target is None:
        return None, None
    return target, fragment


def relative_link(src_file, target_file):
    rel = Path(
        __import__("os").path.relpath(target_file, start=src_file.parent)
    ).as_posix()
    if not rel.startswith("."):
        rel = f"./{rel}"
    return rel


def fix_file(path, url_map, redirect_map, unresolved):
    content = path.read_text()
    lines = content.split("\n")
    in_code_block = False
    changed = False

    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        def repl(m):
            nonlocal changed
            text, url = m.group(1), m.group(2)
            target, fragment = resolve(url, url_map, redirect_map)
            if target is None:
                unresolved.append((path, i + 1, url))
                return m.group(0)
            new_url = relative_link(path, target) + fragment
            changed = True
            return f"[{text}]({new_url})"

        lines[i] = LINK_RE.sub(repl, line)

    if changed:
        path.write_text("\n".join(lines))
    return changed


def main():
    url_map = build_url_map()
    redirect_map = build_redirect_map()
    fixed_files = []
    unresolved = []

    for path in sorted(DOC_ROOT.rglob("*.md")):
        rel = str(path)
        if any(re.match(pattern, rel) for pattern in EXCLUDED_FROM_CHECKS):
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
