#!/usr/bin/env bash
# Create or update a pull request comment, found by a hidden marker, so each
# workflow keeps a single comment up to date rather than posting new ones.
# If BODY_FILE is left out, the comment is deleted instead (if there is one).
set -euo pipefail

pr=$1
marker="<!-- $2 -->"
comments="repos/${GITHUB_REPOSITORY}/issues/${pr}/comments"

id="$(gh api "${comments}" --paginate --jq ".[] | select(.body | startswith(\"${marker}\")) | .id" | head -n 1)"

if [ $# -lt 3 ]; then
  if [ -n "${id}" ]; then
    gh api -X DELETE "repos/${GITHUB_REPOSITORY}/issues/comments/${id}"
  fi
  exit 0
fi

body="${marker}"$'\n'"$(cat "$3")"
if [ -n "${id}" ]; then
  gh api -X PATCH "repos/${GITHUB_REPOSITORY}/issues/comments/${id}" -f body="${body}" > /dev/null
else
  gh api "${comments}" -f body="${body}" > /dev/null
fi
