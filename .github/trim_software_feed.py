#!/usr/bin/env python3
"""Clean up the software updates RSS feed fetched from modules-list.

The upstream feed is never trimmed and contains exact duplicate items, so it
grows to several MB. This keeps the last KEEP_DAYS days, drops duplicates
(same title, date and categories), sorts newest first and sets the channel's
lastBuildDate from the newest item.

It also gives each item a <link>: the package's application page if it has one
(matched on title, as compile_tags.py does), otherwise a search for it on the
Supported Applications page.

Usage: trim_software_feed.py FEED_FILE  (rewritten in place, run from the repository root)
"""

import os
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime, parsedate_to_datetime
from pathlib import Path
from urllib.parse import quote

KEEP_DAYS = 365
SITE_URL = os.getenv("SITE_URL", "https://docs.nesi.org.nz/")
APPS_PAGES_PATH = "Software/Available_Applications"

# Read without PyYAML: the daily fetch workflow doesn't install requirements.txt.
_FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_TITLE = re.compile(r"^title:\s*[\"']?(.*?)[\"']?\s*$", re.MULTILINE)

ET.register_namespace("atom", "http://www.w3.org/2005/Atom")


def item_date(item):
    try:
        date = parsedate_to_datetime(item.findtext("pubDate", ""))
    except (TypeError, ValueError):
        return None
    return date if date.tzinfo else date.replace(tzinfo=timezone.utc)


def app_pages():
    """{module name: page URL} for the application pages, matched as in compile_tags.py."""
    pages = {}
    for md_file in Path("docs", APPS_PAGES_PATH).glob("*.md"):
        if md_file.name == "index.md":
            continue
        front_matter = _FRONT_MATTER.match(md_file.read_text(encoding="utf-8", errors="ignore"))
        match = front_matter and _TITLE.search(front_matter.group(1))
        title = match.group(1) if match else md_file.stem.replace("_", " ")
        pages[title] = f"{SITE_URL}{APPS_PAGES_PATH}/{md_file.stem}/"
    return pages


def item_link(item, pages):
    software = next((c.text for c in item.findall("category") if c.get("domain") == "software"), None)
    if not software:
        return None
    return pages.get(software) or f"{SITE_URL}{APPS_PAGES_PATH}/?search={quote(software)}"


def main(path):
    tree = ET.parse(path)
    channel = tree.getroot().find("channel")
    items = channel.findall("item")
    cutoff = datetime.now(timezone.utc) - timedelta(days=KEEP_DAYS)
    pages = app_pages()

    seen = set()
    kept = []
    for item in items:
        channel.remove(item)
        date = item_date(item)
        if date is None or date < cutoff:
            continue
        key = (
            item.findtext("title"),
            date,
            tuple(c.text for c in item.findall("category")),
        )
        if key in seen:
            continue
        seen.add(key)
        link = item_link(item, pages)
        if link and item.find("link") is None:
            ET.SubElement(item, "link").text = link
        kept.append((date, item))

    kept.sort(key=lambda pair: pair[0], reverse=True)
    channel.extend(item for _, item in kept)

    # Upstream writes a stray lastBuildDate attribute and a stale element.
    channel.attrib.pop("lastBuildDate", None)
    if kept:
        build_date = channel.find("lastBuildDate")
        if build_date is None:
            build_date = ET.SubElement(channel, "lastBuildDate")
        build_date.text = format_datetime(kept[0][0])

    ET.indent(tree, space="  ")
    tree.write(path, encoding="utf-8", xml_declaration=True)
    print(f"{path}: kept {len(kept)} of {len(items)} items")


if __name__ == "__main__":
    main(sys.argv[1])
