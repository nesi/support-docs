#!/bin/bash 

source .venv/bin/activate

export MODULE_LIST_PATH="docs/assets/module-list.json"
mkdocs serve &
sleep 5
xdg-open http://127.0.0.1:8000/nesi/support-docs-concept/