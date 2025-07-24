# NeSI support documentation

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/nesi/support-docs?quickstart=1)

[![Deploy to gh-pages](https://github.com/nesi/support-docs/actions/workflows/deploy.yml/badge.svg?branch=main&event=deployment_status)](https://github.com/nesi/support-docs/actions/workflows/deploy.yml)

This repository contains the sources files for the NeSI support documentation.

Rendered pages are visible at [https://docs.nesi.org.nz](http://docs.nesi.org.nz).

## Contents

The repository is organised using the following folders:

- `checks` : scripts intended to be run by CI,
- `docs`: markdown files, structure determines categories and sections[^1],
- `docs/assets`: non-template related files, e.g. images,
- `overrides`: theme overides or extensions for page templates.
- `overrides/partials`: Overrides and extensions for sub components.

[^1]: A section or category can be replaced by an `index.md` file, this will replace the default nav with a page.

## Developer Documentation

Following pages contain information to help maintain the documentation:

- See [contributing](https://nesi.github.io/support-docs/CONTRIBUTING) ([local version](docs/CONTRIBUTING.md)), to learn how to you can contribute.
- See [formatting](https://nesi.github.io/support-docs/FORMAT), for examples of markdown syntax.
- See [create a new page](https://nesi.github.io/support-docs/NEWPAGE), for general principles to consider when writing pages.
- See [macros](https://nesi.github.io/support-docs/MACROS), for `mkdocs-macros-plugin` environment.
- See [checks](checks/README.md), for information on quality assurance tests.
- See [workflows](.github/workflows/README.md), for information on CI workflows.

## Viewing PR Branches

![Demo Site](https://github.com/CallumWalley/support-docs-dev/actions/workflows/deploy.yml/badge.svg)

Deployments of open pull requests can be viewed at [https://callumwalley.github.io/support-docs-dev/NAME-OF-BRANCH](https://callumwalley.github.io/support-docs-dev/)

## Theme

We are using the [mkdocs material theme](https://squidfunk.github.io/mkdocs-material/).

## Analytics

The site uses [Google analytics](https://analytics.google.com/analytics/web/#/p424742084). You will need to ask a google workspace admin to add you to the project.

## Updating Dependencies

Occasionally you may want to update the dependencies used by mkdocs to build and lint this site.

Make a new branch and

```sh
pip-compile --allow-unsafe > requirements.txt
pip install -r requirements.txt
```

Make sure to test it on a GitHub runner (not just locally), as this is the actual build environment.

## Migration

Migration of the Zendesk documentation is done using our [migration pipeline (NeSI internal GitLab](https://git.hpcf.nesi.org.nz/cwal219/migratedocs).

Any one off filters (e.g. don't need to be checked every time, just when converting from ZD) should go there.
