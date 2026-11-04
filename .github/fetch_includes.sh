#!/bin/bash -e

MODULES_LIST_URL="https://raw.githubusercontent.com/nesi/modules-list/main/module-list.json"
MODULES_UPDATE_URL="https://raw.githubusercontent.com/nesi/modules-list/main/software_updates.xml"
SLURM_LIMITS_URL="https://raw.githubusercontent.com/nesi/modules-list/main/slurm-limits.json"
GLOSSARY_URL="https://raw.githubusercontent.com/nesi/nesi-wordlist/main/outputs/glossary.md"
DICTIONARY_URL="https://raw.githubusercontent.com/nesi/nesi-wordlist/main/outputs/dictionary.txt"
SNIPPETS_URL="https://raw.githubusercontent.com/nesi/nesi-wordlist/main/outputs/snippets.md"
ICAL_URL="https://outlook.office365.com/owa/calendar/3d4e3c7b28ca4549803470b109cba86a@reannz.co.nz/0830583db389420aaa843dc231af48d810099982634588501079/calendar.ics"

mkdir -p docs/assets/glossary overrides/partials

# Download to a temporary file and only replace the destination if the download
# succeeded and is not empty, so a failed fetch keeps the last good copy
# instead of overwriting it with an empty file.
fetch() {
    local dest="$1" url="$2"
    if wget -q -O "${dest}.tmp" "${url}" && [ -s "${dest}.tmp" ]; then
        mv "${dest}.tmp" "${dest}"
    else
        rm -f "${dest}.tmp"
        echo "::error title=Remote asset fetch failed::${url} -> ${dest} (kept previous copy)"
        return 1
    fi
}

# Everything runs in parallel. A bare 'wait' always returns 0, so wait on each
# job to collect failures.
pids=()
fetch docs/assets/training_calendar.ics "${ICAL_URL}" & pids+=($!)
fetch docs/assets/module-list.json     "${MODULES_LIST_URL}" & pids+=($!)
fetch docs/software_updates.xml        "${MODULES_UPDATE_URL}" & pids+=($!)
fetch docs/assets/slurm-limits.json    "${SLURM_LIMITS_URL}" & pids+=($!)
fetch overrides/partials/glossary.html "${GLOSSARY_URL}" & pids+=($!)
fetch docs/assets/glossary/dictionary.txt "${DICTIONARY_URL}" & pids+=($!)
fetch docs/assets/glossary/snippets.md "${SNIPPETS_URL}" & pids+=($!)

failed=0
for pid in "${pids[@]}"; do
    wait "${pid}" || failed=1
done

# The upstream feed is never trimmed and contains duplicates.
if [ -s docs/software_updates.xml ]; then
    python3 .github/trim_software_feed.py docs/software_updates.xml || failed=1
fi

exit "${failed}"
