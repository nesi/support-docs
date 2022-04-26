import requests
import os
from json2html import json2html
import json
import re
import importlib
import subprocess
import yaml


def main():
    """main"""
    global cache_root_dir

    doc_root_dir = "docs"
    cache_root_dir = "from_zendesk/cache"
    # module_list_location = os.environ["ZENDESK_MODULE_LIST"]

    with open(f"{cache_root_dir}/root.json") as f:
        rootload = json.load(f)
    site_nav = [
        writeCategories(category, doc_root_dir) for category in rootload["categories"]
    ]

    print(yaml.dump(site_nav))


def writeArticles(article, filepath):
    """"""
    article_sanitized = sanitise_name(article["name"])
    with open(
        f"{filepath}/{article_sanitized}.md",
        "w+",
    ) as article_file:
        article_file.write((create_article(article)))
    return article_sanitized


def writeSections(section, filepath):
    section_sanitized = sanitise_name(section["name"])
    try:
        os.mkdir(f"{filepath}/{section_sanitized}")
    except FileExistsError:
        pass

    # with open(f"{doc_root_dir}/{category_sanitized}/{section_sanitized}/index.md", 'w') as index_file:
    #     index_file.write(create_category_index(category))

    with open(f"{cache_root_dir}/sections/{section['id']}.json") as f:
        sectionRoot = json.load(f)

    return {
        section_sanitized: [
            writeArticles(
                section,
                f"{filepath}/{section_sanitized}",
            )
            for section in sectionRoot["articles"]
        ]
    }


def writeCategories(category, filepath):
    category_sanitized = sanitise_name(category["name"])

    try:
        os.mkdir(f"{filepath}/{category_sanitized}")
    except FileExistsError:
        pass

    # with open(f"{doc_root_dir}/{category_sanitized}/index.md", 'w') as index_file:
    #     index_file.write(create_category_index(category))
    with open(f"{cache_root_dir}/categories/{category['id']}.json") as f:
        categoryroot = json.load(f)

    return {
        category_sanitized: [
            writeSections(section, f"{filepath}/{category_sanitized}")
            for section in categoryroot["sections"]
        ]
    }


# def writeThing(thingName, thingId, filepath, thingType, callback):
#     mkdir(f"{filepath}/{thingName}")

#     with open(f"{cache_root_dir}/{thingType}/{thingId}.json") as f:
#         thingroot = json.load(f)

#     return {
#         thingName: [
#             callback(
#                 sanitise_name(nextThing["name"]),
#                 nextThing["id"],
#                 f"{filepath}/{thingName}",
#             )
#             for nextThing in thingroot[thingType]
#         ]
#     }


# "-L", "pandoc/filters/spellcheck.lua",
def to_markdown(html):
    """Use pandoc to convert HTML pages to Markdown"""

    output_format = [
        "markdown",  # duh
        "simple_tables"  # other tables include 'grid_tables','multiline_tables'
        # Commented out because only works when *reading* markdown.
        # "fenced_code_attributes",  # classes for fenced code
        # "backtick_code_blocks",  # use fenced rather than tab code blocks
        # "inline_code_attributes",  # allow attributes for inline code
    ]

    markdown = subprocess.run(
        [
            "pandoc",
            "-t",
            "+".join(output_format),
            "-f",
            "html",
            "--css",
            "style.css",
            "--filter",
            "pandoc/filters/custom_filters.py",
        ],
        input=html,
        stdout=subprocess.PIPE,
        check=True,
        encoding="utf-8",
    ).stdout
    return markdown


def create_category_index(category):
    return f"""\
        {{% extends "category.md" -%}}
        {category['description']}
        {{% block content -%}}
        {{% endblock %}}
    """


def create_article(article):
    return to_markdown(article["body"])


def sanitise_name(string):
    return string.replace(" ", "_").replace("/", "-")


def mkdir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


main()
