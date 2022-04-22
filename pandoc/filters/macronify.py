#!/usr/bin/python3.9
"""
Currently replaces about ~50 mispellings of 'Māui'"""

from pandocfilters import toJSONFilter, attributes, Span, Str
import re


def macronify(key, value, format, meta):
    if key == "Str":
        if "Maui" in value:
            return Str(value.replace("Maui", "Māui"))


if __name__ == "__main__":
    toJSONFilter(macronify)
