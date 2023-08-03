Pages hosted [here](https://cwal219.pages.hpcf.nesi.org.nz/mkdocs).

## Migrate

Migration pipeline hosted [here](https://git.hpcf.nesi.org.nz/cwal219/migratedocs)

Any one off filters (e.g. don't need to be checked every time, just when converting from ZD) should go there.

## Build

`mkdocs build --strict -t material`

### Build filters

These are filters that should be run whenever a page is edited.

Currently triggered in CI
    - proselint
    - mdspellcheck

Currently Being run through mkdocs:
    - Spellcheck
    - Dead link checker

Would be better to run these independently so they can be run by gitlab CI.

## Build


## Serve Local

`mkdocs serve`

## Files

### docs/

Location of markdown docs.
File structure determines categories and sections.
A section or category can be replaced by an `index.md` file, this will replace the default nav with a page.

### includes/

For non-template related files, e.g. images.

### overrides/

Theme overides or extensions.

### custom_hooks.py

Custom hooks.
    - on_env : Injects application info from 'module-list' into jinja build env.
    - lint -> moved to CI
    - link_checker -> moved to CI

domains

## Theme

https://squidfunk.github.io/mkdocs-material/reference/code-blocks/

## mkdocs Installation

Basic installation of mkdocs and modules
    - Install mkdocs, 
        - python3 -m pip install mkdocs
        - on OSX can also do
            - `brew install mkdocs`
    - Install python modules
        - `python3 -m pip install linkcheckmd proselint pymdown-extensions 
        - `python3 -m pip install mkdocs-material mkdocs-macros-plugin`
