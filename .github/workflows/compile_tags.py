#!/usr/bin/env python3

"""
Validates page tags, links app pages to the module list, and writes compiled indexes.

Run during CI lint checks to surface tag warnings.
Run on deploy to ensure tag-index.json and module-list.json are up to date before building.

Replaces: link_apps_pages.py
"""

import os
import re
import json
import yaml
import sys
from pathlib import Path


TAGS_VOCAB_PATH = os.getenv("TAGS_VOCAB_PATH", "docs/assets/tags.yml")
TAG_INDEX_PATH = os.getenv("TAG_INDEX_PATH", "docs/assets/tag-index.json")
MODULE_LIST_PATH = os.getenv("MODULE_LIST_PATH", "docs/assets/module-list.json")
DOC_ROOT = os.getenv("DOC_ROOT", "docs")
APPS_PAGES_PATH = os.getenv("APPS_PAGES_PATH", "Software/Available_Applications")
BASE_URL = os.getenv("BASE_URL", "https://www.docs.nesi.org.nz")


def load_vocabulary(path):
    vocab = yaml.safe_load(open(path))
    alias_map = {}
    for canonical, entry in vocab.items():
        alias_map[canonical.lower()] = canonical
        for alias in (entry.get("aliases") or []):
            alias_map[alias.lower()] = canonical
    return vocab, alias_map


def parse_frontmatter(path):
    content = path.read_text()
    match = re.match(r"---\n([\s\S]*?)---", content)
    if not match:
        return None
    return yaml.safe_load(match.group(1)) or {}


def title_from_path(md_file):
    return md_file.stem.replace("_", " ")


vocab, alias_map = load_vocabulary(TAGS_VOCAB_PATH)
module_list = json.load(open(MODULE_LIST_PATH))

tag_index = {canonical: [] for canonical in vocab}
warnings = 0

for md_file in sorted(Path(DOC_ROOT).rglob("*/*.md")):
    rel = str(md_file.relative_to(DOC_ROOT))
    if rel.startswith("assets/"):
        continue
    meta = parse_frontmatter(md_file)

    if meta is None:
        print(f"::warning file= {md_file},title=meta.parse::Meta block missing or malformed.")
        warnings += 1
        continue

    raw_tags = meta.get("tags") or []
    title = meta.get("title") or title_from_path(md_file)
    canonical_tags = []

    for tag in raw_tags:
        canonical = alias_map.get(str(tag).lower())
        if canonical is None:
            print(f"::warning file= {md_file},title=tag.unknown::Unknown tag '{tag}' on '{title}'. Add to {TAGS_VOCAB_PATH} or use an existing alias.")
            warnings += 1
        else:
            entry = {"title": title, "path": rel}
            if entry not in tag_index[canonical]:
                tag_index[canonical].append(entry)
            canonical_tags.append(canonical)

    # For app pages: update support URL and merge canonical tags into module domains.
    is_app_page = str(md_file.relative_to(DOC_ROOT)).startswith(APPS_PAGES_PATH)
    if is_app_page and md_file.name != "index.md":
        app = meta.get("title") or title_from_path(md_file)
        if app in module_list:
            page_link = f"{BASE_URL}/{APPS_PAGES_PATH}/{app}"
            existing = module_list[app].get("support", "")
            if existing and existing != page_link:
                print(f"::warning file={md_file},title=docpath.change::Support URL for '{app}' changed from '{existing}' to '{page_link}'.")
            module_list[app]["support"] = page_link
            for canonical in canonical_tags:
                if canonical not in module_list[app]["domains"]:
                    module_list[app]["domains"].append(canonical)
        elif not meta.get("no_module"):
            print(f"::warning file= {md_file},title=missing.module::'{md_file.name}' has no corresponding module in {MODULE_LIST_PATH}.")
            warnings += 1

tag_index = {k: v for k, v in tag_index.items() if v}

with open(TAG_INDEX_PATH, "w") as f:
    f.write(json.dumps(tag_index, indent=4))

with open(MODULE_LIST_PATH, "w") as f:
    f.write(json.dumps(module_list, indent=4))

print(f"tag-index.json: {len(tag_index)} tags, {sum(len(v) for v in tag_index.values())} entries.")
print(f"module-list.json: updated support URLs and domains for app pages.")
