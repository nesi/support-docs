#!/usr/bin/env python3


from mkdocs.commands import build, serve
from mkdocs.config.base import Config, load_config
import logging
import sys
import re

""" 
This doesnt work and I have no idea why.
"""

def parse_macro(record):

    # These are not useful messages
    if record.name == "mkdocs.commands.build":
        return False
    # Macro log messages are wrapped in a INFO message (priciple of least astonishment).
    # Need to be parsed to be useful
    if record.name == "mkdocs.plugins.mkdocs_macros.util":
        m = re.search(r"\[macros\] - (?P<level>\S*) # _(?P<title>.*)_\n\n_File_: `(?P<file>.*)`\n\n(?P<message>.*)",
                      record.msg, re.MULTILINE)
        if not m:
            return False

        g = m.groupdict()
        record.levelname = g["level"]
        record.name = g["title"]
        record.filename = g["file"]
        record.msg = g["message"]
    return True


if __name__ == '__main__':
    log = logging.getLogger('root')
    log.setLevel(logging.INFO)
    sh = logging.StreamHandler(sys.stdout)
    sh.addFilter(parse_macro)
    sh.setFormatter(logging.Formatter(
        '::%(levelname)s file=%(filename)s,title=%(name)s,col=0,endColumn=0,line=%(lineno)s::%(message)s'))
    log.addHandler(sh)
    config = load_config(config_file_path="./mkdocs.yml")
    build.build(config, dirty=True)
