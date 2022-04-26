#!/usr/bin/python3.9

import re
import sys
import json
import pandocfilters as pf


def struncateify(value):
    """Stringify and truncate value for print to stderr"""
    stringified = pf.stringify(value)
    return (stringified[:20] + "...") if len(stringified) > 75 else stringified


def remove_span_spam(key, value, format, meta):
    """Exlplodes spam span elements"""
    spam_span_classes = ["dfn", "dictionary-of-numbers"]
    if key == "Span":
        [[_, classes, _], content] = value
        for cs in spam_span_classes:
            if cs in classes:
                sys.stderr.write(
                    f"Stripping spam class '{cs}' from '{struncateify(content)}'\n"
                )
                return content


def remove_old_toc(key, value, format, meta):
    """Deletes old non-dynamic table of conents"""
    if key == "Div":
        [[_, classes, _], _] = value
        if "toc" in classes:
            sys.stderr.write("Deleting hard TOC\n")
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
                sys.stderr.write(f"Replacing '{value}' with '{newval}'\n")
                return pf.Str(newval)
            else:
                sys.stderr.write(f"NOT replacing '{value}'\n")


def clean_codeclass(key, value, format, meta):
    """Removed unwanted formatting from code and make conform to 'SPECIFICATION.md"""

    allowed_classes = {"bash": "bash"}

    def fix_keypairs():
        if keypairs:
            sys.stderr.write(f"Removing unknown keypair {str(keypairs)}\n")
        return []

    def fix_classes():
        # Return first valid lang identifr
        output_classes = []
        for cs in classes:
            if cs in allowed_classes.keys():
                output_classes.append([allowed_classes[cs]])
            else:
                sys.stderr.write(
                    f"Removing class '{cs}' from '{struncateify(text)}'.\n"
                )
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


if __name__ == "__main__":
    pf.toJSONFilters([clean_codeclass, macronify, remove_old_toc, remove_span_spam])
