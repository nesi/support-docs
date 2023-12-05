#!/bin/bash


shopt -s globstar

total="$(echo docs/**/*.md | wc -w)"
unver="$(./checks/get_unverified.py docs/**/*.md | wc -l)"

printf "%s%%\n" "$(echo "(100-(100*$unver/$total))" | bc)"
