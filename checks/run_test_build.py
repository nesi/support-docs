#!/usr/bin/env python3


from mkdocs.commands import build, serve
from mkdocs.config.base import Config, load_config
import logging
import sys
import re
import time


""" 
This works but is a bit messy
"""

msg_count = {"DEBUG": 0, "INFO": 0, "WARNING": 0, "ERROR": 0}


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
        record.levelname = g["level"].strip().upper().split("\x1b")[0]
        record.name = g["title"]
        record.filename = g["file"]
        record.msg = g["message"]

    # Does not give correct path to file in question in 'title'.
    # Infer from message.
    m = re.search(r"'(.*?\.md)'",  record.msg)
    if m:
        record.filename = m.group(1)

    return True


def count_msg(record):
    msg_count[record.levelname] += 1

    return True


if __name__ == '__main__':
    log = logging.getLogger('root')
    log.setLevel(logging.INFO)
    sh = logging.StreamHandler(sys.stdout)
    sh.addFilter(parse_macro)
    sh.addFilter(count_msg)
    sh.setFormatter(logging.Formatter(
        '::%(levelname)s file=%(filename)s,title=%(name)s,col=0,endColumn=0,line=%(lineno)s::%(message)s'))
    log.addHandler(sh)
    config = load_config(config_file_path="./mkdocs.yml")
    config.plugins.on_startup(command='build', dirty=True)
    try:
        build.build(config, dirty=True)
    finally:
        config.plugins.on_shutdown()

    time.sleep(5)
    exit(100 < msg_count["INFO"] + (30 * msg_count["WARNING"] + (100 * msg_count["ERROR"])))
