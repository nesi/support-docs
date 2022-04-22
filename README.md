Pages hosted [here](https://cwal219.pages.hpcf.nesi.org.nz/mkdocs).
## Migrate

Set env `ZENDESK_USERNAME` and `ZENDESK_PASSWORD`

Run `python from_zendesk/refresh_cache.py` to scrape docs.
Run `python from_zendesk/convert_docs.py` to convert scraped docs to MD.

### Migration filters

These are filters that should only need to be run once on migration.

Currently being run:
    Identify duplicate headers.
    Macronify

Filters can be added in "from_zendesk/convert_docs.py" "to_markdown()" function by adding to the pandoc command line.

## build

`mkdocs build --strict -t material`

### Build filters

These are filters that should be run whenever a page is edited.

Currently Being run:
    - Spellcheck
    - Dead link checker

Currently these filters are run through mkdocs, but should probably be made independent so they can be run by gitlab CI.
## Serve

`mkdocs serve`