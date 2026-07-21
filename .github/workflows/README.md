# CI

Description of current CI workflow.

## [fetch_includes.yml](fetch_includes.yml)

Retrieves dynamically generated content from external sources.

Currently retrieves:

- Software module list from [modules-list](https://github.com/nesi/modules-list).
- Glossary, spellcheck dictionary and snippets from [nesi-wordlist](https://github.com/nesi/nesi-wordlist)

It then runs [compile_tags.py](#compile_tagspy).

All modified files are added to a new branch called `new-assets` and merged into main.

In theory, all this could be done at deployment, but I wanted to make sure that changes to these remote files didn't break anything.

## [compile_tags.py](compile_tags.py)

Replaces the old `link_apps_pages.py`.

Validates page tags against the canonical vocabulary in [`docs/assets/tags.yml`](../../docs/assets/tags.yml), writes two compiled indexes, and links app pages to the module list:

- **`docs/assets/tag-index.json`** — maps each canonical tag to the list of pages that carry it. Used by the `pages_with_tag()` macro at render time.
- **`docs/assets/module-list.json`** — updated with support-page URLs and canonical domain tags for each application.

Any tag not present in `tags.yml` (as a key or alias) produces a CI warning. Unknown tags are silently dropped from the index.

### Tag vocabulary

Tags are defined in [`docs/assets/tags.yml`](../../docs/assets/tags.yml). Each entry has a canonical key (snake\_case), a display label, and optional aliases. Pages should always use canonical keys; aliases are accepted for backwards compatibility but are normalised at compile time.

## [checks.yml](checks.yml)

A series of QA checks run on the documentation.

The checks can be started manually from the ![workflow page](https://github.com/nesi/support-docs/actions/workflows/checks.yml/badge.svg),
select the target branch, give the pattern of files to include, and select which checks you want done.

Checks will also be run on any _non main_ branch pushes. All checks will be run, but only on _changed_ files.

More info on what these checks do in [README.md](../../checks/README.md)

## [deploy.yml](deploy.yml)

Runs on push to _main_ branch. Builds and deploys pages.
