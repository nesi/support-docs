#!/usr/bin/env python3

#  gh pr list --json headRefName
# for pr in ; do gh pr checks $pr && git --work-tree=docs/ checkout origin/$pr -- docs/ && mv docs/docs docs/$pr;done


# $(gh pr list --json headRefName | jq -r '.[].headRefName')

&& gh pr comment $pr -b  "Test deployment available at "
