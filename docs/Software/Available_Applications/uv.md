---
created_at: 2025-12-22
description: Documentation for uv on Mahuika
title: uv
tags:
    - python
    - software
---

[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

uv will manage Python packages including determining dependencies to create virtual environments.
There are two primary approaches to using uv: [for individual scripts](#using-uv-for-scripts) and [for projects or groups of scripts](#using-uv-for-projects).

## Using uv for scripts

[uv can initialize and run a script using a virtual environment based on the `import` statements in a Python file.](https://docs.astral.sh/uv/guides/scripts/#running-a-script-with-dependencies)
Given the following Python script (`cities.py`):

```python
import pandas

# Data provided as a dictionary
data = {
    "City": ["Tokyo", "Delhi", "Shanghai", "Sao Paulo"],
    "Country": ["Japan", "India", "China", "Brazil"],
    "Population_Millions": [37.3, 32.0, 28.5, 22.4]
}

# Load the data into a DataFrame object
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
```

uv can add requirements directly to the Python file using `uv add --script cities.py 'pandas'`.
This will add a `script` section to the top of the `cities.py` containing TOML.

```python
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "pandas>=2.3.3",
# ]
# ///
```

Now when you use `uv run cities.py` the environment setup will be handled for you and the script will be run in an environment matching the specifications.
You can manually edit this TOML section as needed to update the script dependencies.

## Using uv for projects

This is a brief overview, the uv docs have a [detailed guide for projects](https://docs.astral.sh/uv/guides/projects/).
There are two key files for uv projects:

- The dependency file: `pyproject.toml` or `uv.toml`
    - This file is editable and provides the specifications and details of the packages needed.
- The lock file: `uv.lock`
    - This file should not be edited manually. It contains the details about the exact version for every dependency to build the virtual environment.

To set up a uv-managed Python project run `uv init` in the desired location.
This will create a set of files to help manage your project:

``` sh
├── .gitignore
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

You can then add needed packages with `uv add <package>`.
You can also specify packages by editing the `pyproject.toml` file that is created by `uv init`.
Versions can be specified in both the command line and `pyproject.toml`.

Any script can then be run in the virtual environment by running `uv run script.py`.
uv will confirm that the virtual environment, dependency file and lockfile are up-to-date prior to running the script.

You can also sync the virtual environment, dependency file and lockfile and then activate the virtual environment and run Python commands as usual with:

``` sh
uv sync
source .venv/bin/activate
python script.py
```

## Package sources

The default index used by uv is the [Python Package Index (PyPI)](https://pypi.org/).
Additional indexes can be defined in the `pyproject.toml` by adding an index to the `[[tool.uv.index]]` entry.

You can also specify the source for a package either in the `[tool.uv.sources]` entry or when adding a package via the command line using `uv add "my-package @ git+https://github.com/my/package"`.

```toml
[tool.uv.sources]
my-package = { git = "https://github.com/my/package" }

[[tool.uv.index]]
name = "my-index"
url = "https://link.to.my-index"
```

For more detailed information on package indices and specifying sources, see the [uv documentation page](https://docs.astral.sh/uv/concepts/indexes/).

## Caching

uv will always use a cache, using a temporary cache directory when the `--no-cache` flag is used.
To avoid filling your `/home/` directory space, you can add `export UV_CACHE_DIR=/nesi/nobackup/<projectid>/uv_cache` to your `~/.bashrc` to set a cache directory.

## Sharing, importing, and exporting uv environments

Sharing just the `pyproject.toml` will simply share the specifications of the environment.
Sharing the `uv.lock` file will share the exact set of packages and dependencies used to create the project.
This will allow uv to create an identical virtual environment.

To create a virtual environment using an existing `uv.lock`, you simply need to run `uv sync` in the directory containing the dependency and lock files.

In addition to importing and exporting uv environments to be shared with other uv users, you can also import and export dependency specifications from other package managers.
After initializing the uv project, you can [import from a `requirements.txt`](https://docs.astral.sh/uv/guides/migration/pip-to-project/) using `uv add -r requirements.txt`.
uv also supports [exporting to multiple formats](https://docs.astral.sh/uv/concepts/projects/export/) using `uv export --format <format> --output-file <filename>` where `<format>` can be one of: `requirements.txt`, `pylock.toml`, or `cyclonedx1.5`.

## External resources

The [uv documentation](https://docs.astral.sh/uv/) is the best source for additional information about using uv.
