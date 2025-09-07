import os
import re
import json

DOCS_DIR = "docs"
LINK_REGEX = re.compile(r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)')  # Ignore images: ![]()
MD_EXT = ".md"
IGNORE_PATTERNS = [
    "FORMAT.md",
    "MACROS.md",
    "CONTRIBUTING.md",
    "NEWPAGE.md",
    "Storage/Long_Term_Storage/Release_Notes_freezer-nesi-org-nz/"
]

with open("docs_links.json", "r", encoding="utf-8") as f:
    docs_data = json.load(f)

nodes = set()
edges = []

for src, links in docs_data.items():
    nodes.add(src)
    for dst in links["internal_links"]:
        nodes.add(dst)
        edges.append((src, dst))
    for dst in links["external_links"]:
        edges.append((src, dst))

# Generate Graphviz DOT
print("digraph docs_links {")
print('  rankdir=LR;')
for node in nodes:
    if node.startswith("http"):
        print(f'  "{node}" [shape=box, style=dashed, color=blue];')
    else:
        print(f'  "{node}" [shape=ellipse, style=filled, fillcolor=lightgrey];')
for src, dst in edges:
    print(f'  "{src}" -> "{dst}";')
print("}")
