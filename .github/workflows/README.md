# CI

Description of current CI workflow.

## [fetch_includes.yml](fetch_includes.yml)

Retrieves dynamically generated content from external sources.

Currently retrieves:
- Software module list from [modules-list](https://github.com/nesi/modules-list).
- Glossary, spellcheck dictionary and snippets from [nesi-wordlist](https://github.com/nesi/nesi-wordlist)

It then runs [link_apps_pages.py](#link_apps_pagespy).

All modified files are added to a new branch called `new-assets` and merged into main.

In theory, all this could be done at deployment, but I wanted to make sure that changes to these remote files didn't break anything.

## [link_apps_pages.py](link_apps_pages.py)

A Python script used to add a link to the appropriate documentation to [modules-list.json](../../docs/assets/module-list.json).

The script checks all titles of input files, and sets the `support` key to be equal to the pages url.
It also adds whatever tags are on that page to the `domains` key.

_One day I would like to simplify this whole thing._

## [checks.yml](checks.yml)

A series of QA checks run on the documentation.

The checks can be started manually from the ![workflow page](https://github.com/nesi/support-docs/actions/workflows/checks.yml/badge.svg),
select the target branch, give the pattern of files to include, and select which checks you want done.

Checks will also be run on any _non main_ branch pushes. All checks will be run, but only on _changed_ files.

More info on what these checks do in [README.md](../../checks/README.md)

## [deploy.yml](deploy.yml)

Runs on push to _main_ branch. Builds and deploys pages.
