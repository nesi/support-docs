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

### Build and deploy

```bash
source .venv/bin/activate
mkdocs serve -c
```

Take note of any warnings or errors.

A link to the deployment will be printed once served.

### IDE

[Reccomended VSCode Plugins](./code_extensions.json)

## Raise an issue

If you find an issues that needs to be resolved, please have a look through the list of existing issues to see whether your issues hasn't already been reported. If it has, or a closely related issues exists, please add your comments to the existing issue.

If your issue isn't already listed, then create a New Issue. Provide details of your suggestion and include the user guide and url to which your suggestion applies. One of our team members will review your suggestion and resolve it if they can. They may contact you if they need some more clarification.
