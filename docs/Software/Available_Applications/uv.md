---
created_at: 2025-12-22
description: Documentation for uv on Mahuika
tags:
    - python
    - software
---

[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

## General usage notes

uv will manage Python packages including determining dependencies to create virtual environments.
To set up a uv-managed Python project run `uv init` in the desired location.
You can then add needed packages with `uv add <package>`.
You can also specify packages by editing the `pyproject.toml` file that is created by `uv init`.
Versions can be specified in both the command line and `pyproject.toml`.

## Caching

uv will always use a cache, using a temporary cache directory when the `--no-cache` flag is used.
To avoid filling your `/home/` directory space, you can add `export UV_CACHE_DIR=/nesi/nobackup/<projectid>/uv_cache` to your `~/.bashrc` to set a cache directory.
