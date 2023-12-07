# Contributing

Any changes made should be merged via a pull request.

## Minor edits through github

Press `.`, will open up VSCode in browser.

## Local Development Environment

A local development environment is not required to make doc edits, but if you are making lots of changes, the realtime rendering can be quite helpful.

### First time setup

You will need to have Python 3 installed on your computer.

Clone this repository and create a Python virtual environment using:

```bash
git clone https://github.com/nesi/support-docs-concept.git
cd support-docs-concept
python -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Make Development Branch

```bash
git checkout -b my_development_branch
```

### Build and deploy

```bash
source .venv/bin/activate
mkdocs serve -c
```

Take note of any warnings or errors.

A link to the deployment will be printed once served.

### IDE

You can use any IDE you want, if you are using VSCode there are [Reccomended VSCode Plugins](./code_extensions.json).

## Merge Request

The `main` branch is protected, changes can be made via a pull request.

Make a pull request for your development branch into `main`.

If you are using a local development environment,

```
git checkout -b <branchname>
```
When you are done with your changes
```
git push origin <branchname>
```
CI checks will run on your branch, you can check them under 'Actions'
Might be worth having a quick look at these before making a pull request.

Make a pull [request](https://github.com/nesi/support-docs-concept/pulls)

Pull will merge automatically if all checks passed. (add timer too maybe?)


## Adding Words to Dictionary

If the CI is failing the spellcheck phase, and you beleive the identified words are not typos, (double check your capitalisation and apostrophes first) you can update the dictionary being used.

1. Visit the [NeSI Wordlist](https://github.com/nesi/nesi-wordlist), follow the instructions there on adding words.
2. Once changes to the wordlist have been merged, you can fetch the new assets by running the [![Fetch Remote Assets](https://github.com/nesi/support-docs-concept/actions/workflows/fetch_includes.yml/badge.svg?branch=main&event=workflow_run)](https://github.com/nesi/support-docs-concept/actions/workflows/fetch_includes.yml) workflow in this repo.
3. A branch `new-assets` will be created, which can be merged into main (you should see your new words are added).


## Raise an issue

*Not documented at the moment (TODO)*
