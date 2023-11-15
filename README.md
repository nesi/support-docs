Pages hosted [here](https://cwal219.pages.hpcf.nesi.org.nz/mkdocs).

## Local Development Environment

Note. A local development environment is not required to make doc edits. See [CONTRIBUTING.md](./CONTRIBUTING.md)

### First time setup

```bash
git clone https://github.com/nesi/support-docs-concept.git
cd support-docs-concept
python -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

You may have to source your `.venv/bin/activate` again before being able to deploy.

### Build and deploy

```bash
source .venv/bin/activate
mkdocs serve -c
```

Take note of any warnings or errors.

A link to the deployment will be printed.

### IDE

[Reccomended VSCode Plugins](./code_extensions.json)

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
