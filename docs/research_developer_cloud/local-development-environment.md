### Setting up a local development environment

Note for windows users, this process will be much easier if you set up [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install), then the commands below will work within the WSL environment.

### MkDocs Installation

Install mkdocs
```sh
python3 -m pip install mkdocs
```

Install theme and addons
```sh
pip install mkdocs-material mkdocs-glightbox mkdocs-literate-nav neoteroi-mkdocs mkdocs-git-revision-date-localized-plugin
```

Once the above items are installed you can then serve the files locally with the below command ensuring you are in the root of the repo

```sh
mkdocs serve
```

Then browse to http://localhost:8000/