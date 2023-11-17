# Contributing

Any changes made should be merged via a pull request.

## Minor edits through github

Press `.`, will open up VSCode in browser.

## Local Development Environment

A local development environment is not required to make doc edits, but if you are making lots of changes, the realtime rendering can be quite helpful. 

### First time setup

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

## Raise an issue


