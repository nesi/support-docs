#!/usr/bin/env python3


from mkdocs.commands import build, serve
from mkdocs.config.base import Config, load_config
import logging
import sys
import re

""" 
This doesnt work and I have no idea why.
"""

def ignore_macro(record):

    if record.name == "mkdocs.commands.build":
        return False
    if record.name == "mkdocs.plugins.mkdocs_macros.util":
        m = re.search(r"\[macros\] - (?P<level>\S*) # _(?P<title>.*)_\n\n_File_: `(?P<file>.*)`\n\n(?P<message>.*)",
                      record.msg, re.MULTILINE)
        if m:
            g = m.groupdict()
            record.levelname = g["level"]
            record.name = g["title"]
            record.filename = g["file"]
            record.msg = g["message"]
        else:
            return False
    return True
    
if __name__ == '__main__':
    try:
        log = logging.getLogger('root')
        log.setLevel(logging.INFO)
        sh = logging.StreamHandler(sys.stdout)
        sh.addFilter(ignore_macro)
        sh.setFormatter(logging.Formatter(
            '::%(levelname)s file=%(filename)s,title=%(name)s,col=0,endColumn=0,line=%(lineno)s::%(message)s'))
        log.addHandler(sh)
        config = load_config(config_file_path="./mkdocs.yml")
        build.build(config, None, True)
    except Exception as e:
        print(e)
