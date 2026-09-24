# CI

Description of current CI workflow.

## [fetch_includes.yml](fetch_includes.yml)

Retrieves dynamically generated content from external sources.

Currently retrieves:

- Software module list from [modules-list](https://github.com/nesi/modules-list).
- Glossary, spellcheck dictionary and snippets from [nesi-wordlist](https://github.com/nesi/nesi-wordlist)

- The training calendar and the software updates feed.

Runs daily at 00:00 UTC, and can be started manually.
If anything changed (ignoring changes that are only to the calendar), the files are committed directly to `main`
as `nesi-mkdocs-bot` ("Automatic asset update"), using the `NESI_PAT` secret. There is no intermediate branch.

The same script also runs at the start of every deploy, so the deployed site always uses the latest files.

## [compile_tags.py](compile_tags.py)

Replaces the old `link_apps_pages.py`.

Validates page tags against the canonical vocabulary in [`docs/assets/tags.yml`](../../docs/assets/tags.yml), writes two compiled indexes, and links app pages to the module list:

- **`docs/assets/tag-index.json`** — maps each canonical tag to the list of pages that carry it. Used by the `pages_with_tag()` macro at render time.
- **`docs/assets/module-list.json`** — updated with support-page URLs and canonical domain tags for each application.

Any tag not present in `tags.yml` (as a key or alias) produces a CI warning. Unknown tags are silently dropped from the index.
An alias listed under more than one tag also produces a warning.

Runs in the `Compile tags` job of [checks.yml](#checksyml) and before every build in [deploy.yml](#deployyml).

### Tag vocabulary

Tags are defined in [`docs/assets/tags.yml`](../../docs/assets/tags.yml). Each entry has a canonical key (snake\_case), a display label, and optional aliases. Pages should always use canonical keys; aliases are accepted for backwards compatibility but are normalised at compile time.

## [checks.yml](checks.yml)

A series of QA checks run on the documentation.

The checks can be started manually from the ![workflow page](https://github.com/nesi/support-docs/actions/workflows/checks.yml/badge.svg),
select the target branch, give the pattern of files to include, and select which checks you want done.

Checks will also be run on any _non main_ branch pushes. All checks will be run, but only on _changed_ files
(deleted files are left out).

Jobs: spelling, prose, markdownlint, page meta (plus an ARIA reference check), Slurm scripts, accessibility (WCAG),
compile tags, and a full test build. Findings are reported as annotations; the jobs do not fail on warnings.

More info on what these checks do in [README.md](../../checks/README.md)

## [deploy.yml](deploy.yml)

Runs on push to _main_ branch, daily at 12:00 UTC, and manually. Fetches remote assets, compiles tags, builds the site and deploys it to GitHub Pages.

The `rag-ingest` job, which triggers a refresh of the docs search assistant index, is currently disabled (`if: false`).

## [demo_deploy.yml](demo_deploy.yml)

Runs on every pull request (except from `assets-update`). Triggers a build of the branch in
[CallumWalley/mkdocs-demo-deploy](https://github.com/CallumWalley/mkdocs-demo-deploy), waits up to 10 minutes for it,
then comments on the pull request with a link to the preview and to each changed page.

## [auto_merge.yml](auto_merge.yml)

Runs daily at 12:30 UTC, and manually. Squash-merges **every** open pull request with the `auto_merge` label, with no review.
Only add the label to pull requests that should merge without review.
