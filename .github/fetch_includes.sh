#!/bin/bash -e

MODULES_LIST_URL="https://raw.githubusercontent.com/nesi/modules-list/main/module-list.json"
MODULES_UPDATE_URL="https://raw.githubusercontent.com/nesi/modules-list/main/rss.xml"
GLOSSARY_URL="https://raw.githubusercontent.com/nesi/nesi-wordlist/main/outputs/glossary.md"
DICTIONARY_URL="https://raw.githubusercontent.com/nesi/nesi-wordlist/main/outputs/dictionary.txt"
SNIPPETS_URL="https://raw.githubusercontent.com/nesi/nesi-wordlist/main/outputs/snippets.md"
ICAL_URL="https://calendar.google.com/calendar/ical/c_hen6rr02et39kat2hmuamidots@group.calendar.google.com/public/basic.ics"

mkdir -p docs/assets/glossary

wget -q -O docs/assets/training_calendar.ics "${ICAL_URL}"
wget -q -O docs/assets/module-list.json "${MODULES_LIST_URL}"
wget -q -O docs/software_updates.xml "${MODULES_UPDATE_URL}"

python3 .github/workflows/link_apps_pages.py

wget -q -O overrides/partials/glossary.html "${GLOSSARY_URL}"
wget -q -O docs/assets/glossary/dictionary.txt "${DICTIONARY_URL}"
wget -q -O docs/assets/glossary/snippets.md "${SNIPPETS_URL}"
