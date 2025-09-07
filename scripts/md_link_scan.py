import os
import re
import json

DOCS_DIR = "docs"
LINK_REGEX = re.compile(r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)')
MD_EXT = ".md"
IGNORE_PATTERNS = [
    "FORMAT.md",
    "MACROS.md",
    "CONTRIBUTING.md",
    "NEWPAGE.md",
    "Storage/Long_Term_Storage/Release_Notes_freezer-nesi-org-nz/"
]

def is_internal(link):
    return link.endswith(MD_EXT) or link.startswith("./") or link.startswith("../")

def is_ignored(path):
    basename = os.path.basename(path.split("#")[0])
    for pattern in IGNORE_PATTERNS:
        if basename == pattern or path.startswith(pattern):
            return True
    return False

def scan_md_links(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    links = LINK_REGEX.findall(content)
    return links

docs_data = {}

for root, _, files in os.walk(DOCS_DIR):
    for file in files:
        if file.endswith(MD_EXT):
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, DOCS_DIR)
            if is_ignored(rel_path):
                continue
            links = scan_md_links(abs_path)
            internal_links = []
            external_links = []
            for _, link in links:
                link_rel_path = os.path.normpath(os.path.join(os.path.dirname(rel_path), link))
                if is_internal(link):
                    if not is_ignored(link_rel_path):
                        internal_links.append(link_rel_path)
                else:
                    external_links.append(link)
            docs_data[rel_path] = {
                "internal_links": internal_links,
                "external_links": external_links
            }

with open("docs_links.json", "w", encoding="utf-8") as f:
    json.dump(docs_data, f, indent=2)
