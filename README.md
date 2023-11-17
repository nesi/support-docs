[![Deploy to gh-pages](https://github.com/nesi/support-docs-concept/actions/workflows/deploy.yml/badge.svg?branch=main&event=deployment_status)](https://github.com/nesi/support-docs-concept/actions/workflows/deploy.yml)

Pages hosted [here](https://cwal219.pages.hpcf.nesi.org.nz/mkdocs).

## Migrate

[Migration pipeline](https://git.hpcf.nesi.org.nz/cwal219/migratedocs)

Any one off filters (e.g. don't need to be checked every time, just when converting from ZD) should go there.

## Theme

We are using the [mkdocs material theme](https://squidfunk.github.io/mkdocs-material/)

## Subdirectories

### checks/

Scripts intended to be run by CI.

### docs/

Location of markdown docs.
File structure determines categories and sections.
A section or category can be replaced by an `index.md` file, this will replace the default nav with a page.

### docs/assets/

For non-template related files, e.g. images.

### overrides/

Theme overides or extensions.

