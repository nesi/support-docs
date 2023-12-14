#!/usr/bin/env python3


from mkdocs.commands import build
from mkdocs.config.base import Config, load_config
import logging

log = logging.getLogger('mkdocs')
log.setLevel(logging.INFO)
sh = logging.StreamHandler()
sh.setFormatter(logging.Formatter('::%(levelname)s title=%(name)s::%(message)s'))
log.addHandler(sh)
# logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
# log.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
config = load_config(config_file_path="./mkdocs.yml")
try:
    build.build(config, None, False)
except Exception as e:
    # print(e)
    pass
