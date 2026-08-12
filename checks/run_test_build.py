#!/usr/bin/env python3


from mkdocs.commands import build, serve
from mkdocs.config.base import Config, load_config
import logging
import os
import sys
import re
import tempfile
import time

import requests


"""
This works but is a bit messy
"""

msg_count = {"DEBUG": 0, "NOTICE": 0, "WARNING": 0, "ERROR": 0}

MODULES_LIST_URL = "https://raw.githubusercontent.com/nesi/modules-list/main/module-list.json"


def fetch_module_list():
    """Fetch the latest module-list.json contents, or None if unavailable."""
    try:
        response = requests.get(MODULES_LIST_URL, timeout=10)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"::WARNING file={__file__},title=module_list_fetch_failed,col=0,endColumn=0,line=0::"
              f"Could not fetch latest module-list.json ({e}); using committed copy instead.")
        return None


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

    # Swap to use notice for github parsing.
    if record.levelname == "INFO":
        record.levelname = "NOTICE"

    return True

if __name__ == '__main__':
    # Github uses 'NOTICE' rather than 'INFO'
    # This should overwrite existing INFO level.
    logging.addLevelName(logging.INFO, "NOTICE")
    log = logging.getLogger('root')
    log.setLevel(logging.INFO)
    sh = logging.StreamHandler(sys.stdout)
    sh.addFilter(parse_macro)
    sh.setFormatter(logging.Formatter(
        '::%(levelname)s file=%(filename)s,title=%(name)s,col=0,endColumn=0,line=%(lineno)s::%(message)s'))
    log.addHandler(sh)

    module_list = fetch_module_list()
    tmp_module_list_path = None
    if module_list is not None:
        # mkdocs_hooks.py / macro_hooks.py read MODULE_LIST_PATH at import time,
        # so it must be set before load_config() pulls those in.
        fd, tmp_module_list_path = tempfile.mkstemp(suffix=".json", prefix="module-list-")
        with os.fdopen(fd, "wb") as f:
            f.write(module_list)
        os.environ["MODULE_LIST_PATH"] = tmp_module_list_path

    config = load_config(config_file_path="./mkdocs.yml")
    config.plugins.on_startup(command='build', dirty=True)
    try:
        build.build(config, dirty=True)
    except Exception as e:
        print(f"::ERROR file={__file__},title=build_failed,col=0,endColumn=0,line=0::{e}")
        sys.exit(1)
    finally:
        config.plugins.on_shutdown()
        if tmp_module_list_path:
            os.remove(tmp_module_list_path)

    if module_list is not None:
        # Overwrite the stale copy mkdocs just copied from docs/assets/module-list.json,
        # so the client-side app filter (supportedApplications.js) also sees fresh data.
        site_module_list_path = os.path.join(config.site_dir, "assets", "module-list.json")
        os.makedirs(os.path.dirname(site_module_list_path), exist_ok=True)
        with open(site_module_list_path, "wb") as f:
            f.write(module_list)

    time.sleep(5)
    # exit(100 < msg_count["NOTICE"] + (30 * msg_count["WARNING"] + (100 * msg_count["ERROR"])))
