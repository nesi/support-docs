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

## Theme
https://squidfunk.github.io/mkdocs-material/reference/code-blocks/
