#!/usr/bin/env bash
# Create or update a pull request comment, found by a hidden marker, so each
# workflow keeps a single comment up to date rather than posting new ones.
#
# Usage: pr_comment.sh PR_NUMBER MARKER BODY_FILE
# Needs GH_TOKEN and GITHUB_REPOSITORY set (both are in GitHub Actions).
set -euo pipefail

pr=$1
marker="<!-- $2 -->"
body="${marker}"$'\n'"$(cat "$3")"
comments="repos/${GITHUB_REPOSITORY}/issues/${pr}/comments"

id="$(gh api "${comments}" --paginate --jq ".[] | select(.body | startswith(\"${marker}\")) | .id" | head -n 1)"

if [ -n "${id}" ]; then
  gh api -X PATCH "repos/${GITHUB_REPOSITORY}/issues/comments/${id}" -f body="${body}" > /dev/null
else
  gh api "${comments}" -f body="${body}" > /dev/null
fi
