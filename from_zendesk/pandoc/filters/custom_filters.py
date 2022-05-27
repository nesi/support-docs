#!/usr/bin/python3.9

import re
import sys
import json
import pandocfilters as pf
import string
import requests
import unicodedata
import logging as log
from os.path import exists
import tempfile

log.basicConfig(stream=sys.stderr, level=log.INFO, format="[%(levelname)s] %(message)s")


def struncateify(value):
    """Stringify and truncate value for print to stderr"""
    stringified = pf.stringify(value)
    return (stringified[:20] + "...") if len(stringified) > 75 else stringified


def title_clean(title):
    if len(title) > 50:
        log.warning(f"Asset '{title}' very long. Consider shortening")
    return "".join(
        c
        for c in unicodedata.normalize("NFKD", title).encode("ASCII", "ignore").decode()
        if c in f"-_.{string.ascii_letters}{string.digits})"
    )


def remove_span_spam(key, value, format, meta):
    """Exlplodes spam span elements"""
    spam_span_classes = ["dfn", "dictionary-of-numbers"]
    if key == "Span":
        [[_, classes, _], content] = value
        for cs in spam_span_classes:
            if cs in classes:
                log.info(f"Stripping spam class '{cs}' from '{struncateify(content)}'")
                return content


def remove_old_toc(key, value, format, meta):
    """Deletes old non-dynamic table of conents"""
    if key == "Div":
        [[_, classes, _], _] = value
        if "toc" in classes:
            log.info("Deleting hard TOC")
            return []


def macronify(key, value, format, meta):
    """
    Currently replaces about ~50 mispellings of 'Māui'
    """
    maui_match = re.compile(r"(?<![._-])maui(?:\.\s*$)?(?![0._-])", re.IGNORECASE)
    # For the purposes of debugging. Matches all instances of maui to report when NOT replaced.
    all_maui_match = re.compile(r"maui", re.IGNORECASE)

    if key == "Str":
        # if key != "Code" or key != "CodeBlock":
        if all_maui_match.match(value):
            if maui_match.match(value):
                newval = maui_match.sub("Māui", value)
                # Be good to include some more context here. (page line etc)
                # sys.stderr.write(str(os.environ))
                log.info(f"Replacing '{value}' with '{newval}'")
                return pf.Str(newval)
            else:
                log.info(f"NOT replacing '{value}'")


def clean_codeclass(key, value, format, meta):
    """Removed unwanted formatting from code and make conform to 'SPECIFICATION.md"""

    allowed_classes = {"bash": "bash"}

    def fix_keypairs():
        if keypairs:
            log.info(f"Removing unknown keypair {str(keypairs)}")
        return []

    def fix_classes():
        # Return first valid lang identifr
        output_classes = []
        for cs in classes:
            if cs in allowed_classes.keys():
                output_classes.append([allowed_classes[cs]])
            else:
                log.info(f"Removing class '{cs}' from '{struncateify(text)}'.")
        return output_classes

    if key == "Code":
        [[identifier, classes, keypairs], text] = value
        fixed = fix_classes()
        return pf.Code(
            ["", [], fix_keypairs()], ("#!" + str(fixed[0]) if fixed else "") + text
        )
    if key == "CodeBlock":
        [[identifier, classes, keypairs], text] = value
        return pf.CodeBlock(["", fix_classes(), fix_keypairs()], text)
        # return pf.RawBlock(format, f"{fix_classes()}\n{text}")


def localise_asset(key, value, format, meta):
    """Copies image assets into 'includes/images'"""
    tmp_img_dir = "includes/.images"
    img_dir = "includes/images"
    if key == "Image":
        [attr, inline, target] = value
        [url, alt] = target

        asset_all = url.split("/")[-1]
        try:
            [asset_name, asset_ext] = asset_all.split(".")
        except ValueError:
            log.error(f"{asset_all} is not a nice asset name.")
            [asset_name, asset_ext] = [asset_all, ""]
        # title = ""
        # for elem in inline:
        #     if elem["t"] == "Str":
        #         title = elem["c"]
        #     else:
        #         log.error(f"'{json.dumps(elem)}' too complicated. Leaving for now.")
        #         return []
        # if not title == "":
        #     log.error(f"'{url}' has no title. Do better.")

        # title = title_clean(title)

        img_data = requests.get(url).content
        while exists(f"{tmp_img_dir}/{asset_all}"):
            log.warning(
                f"'{asset_all}' is a duplicate asset name, renaming to {asset_all}.copy"
            )
            asset_name += "_copy"
        with open(f"{tmp_img_dir}/{asset_all}", "wb") as handler:
            handler.write(img_data)
        return pf.Image(attr, inline, [f"{img_dir}/{asset_name}.{asset_ext}", f"{alt}"])
        # pf.Code(
        #    ["", [], fix_keypairs()], ("#!" + str(fixed[0]) if fixed else "") + text
        # )


if __name__ == "__main__":
    pf.toJSONFilters(
        [clean_codeclass, macronify, remove_old_toc, remove_span_spam, localise_asset]
    )
