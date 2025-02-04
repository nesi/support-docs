#!/bin/bash -e

MODULES_LIST_URL="https://raw.githubusercontent.com/nesi/modules-list/main/module-list.json"
MODULES_UPDATE_URL="https://raw.githubusercontent.com/nesi/modules-list/main/rss.xml"
GLOSSARY_URL="https://raw.githubusercontent.com/nesi/nesi-wordlist/main/outputs/glossary.md"
DICTIONARY_URL="https://raw.githubusercontent.com/nesi/nesi-wordlist/main/outputs/dictionary.txt"
SNIPPETS_URL="https://raw.githubusercontent.com/nesi/nesi-wordlist/main/outputs/snippets.md"

wget -O docs/assets/module-list.json ${MODULES_LIST_URL}
wget -O docs/software_updates.xml ${MODULES_UPDATE_URL}
python3 .github/workflows/link_apps_pages.py
git add docs/assets/module-list.json docs/software_updates.xml
git commit -m "Updated Module List" || (echo "No Changes";exit 0)

echo "Fetch Wordlist"

wget -O overrides/partials/glossary.html ${GLOSSARY_URL}
wget -O docs/assets/glossary/dictionary.txt ${DICTIONARY_URL}
wget -O docs/assets/glossary/snippets.md ${SNIPPETS_URL}
git add overrides/partials/glossary.html docs/assets/glossary/dictionary.txt docs/assets/glossary/snippets.md
git commit -m "Updated Glossary" || (echo "No Changes";exit 0)

sleep 1
