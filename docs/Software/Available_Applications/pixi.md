---
created_at: 2026-11-03
description: Using pixi on Mahuika to install conda and PyPI packages into a project environment, run it in a batch job, and share it with a lock file
title: pixi
tags:
    - python
    - software
---

[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

pixi gives each project its own environment, with packages from conda-forge and PyPI.
The packages you ask for are listed in `pixi.toml`, and the exact version of every package is pinned in `pixi.lock`.
To compare pixi with Conda, uv and containers, see [Reproducible Software](../Reproducible_Software.md).

## Set the cache directory

By default, pixi keeps its package cache in your home directory. Move it to your project's nobackup directory:

```sh
export PIXI_CACHE_DIR=/nesi/nobackup/nesi99991/pixi_cache
```

Replace `nesi99991` with your project code. Add this line to your `~/.bashrc` to keep the setting.

## Create a project

Make the project in your project directory: its environment, in the `.pixi` directory, can contain many files.

```sh
module purge
module load pixi/{{ app.default }}
cd /nesi/project/nesi99991/my_project
pixi init
pixi add python numpy
pixi run python my_script.py
```

Replace `nesi99991` with your project code. Add PyPI packages with `pixi add --pypi PACKAGE_NAME`.

To run the project in a batch job:

```sl
#!/bin/bash -e

#SBATCH --job-name    pixi-job
#SBATCH --account     nesi99991
#SBATCH --time        01:00:00

module purge
module load pixi/{{ app.default }}

cd /nesi/project/nesi99991/my_project
pixi run python my_script.py
```

## Share an environment

Keep `pixi.toml` and `pixi.lock` with your code, for example in Git. Anyone with both files can recreate the environment with `pixi install`.

A project made on Mahuika only lists the `linux-64` platform. To use it on another computer, such as a Mac, add that platform:

```sh
pixi workspace platform add osx-arm64
```

The [pixi documentation](https://pixi.sh/latest/) has more on projects, tasks and multiple environments.
