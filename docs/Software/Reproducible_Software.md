---
Title: Reproducible Software
tags:
    - software
    - reproducible
    - reproducibility
    - environments
    - containers
---

## Research Software

According to [this article in Nature](https://www.nature.com/articles/s41597-022-01710-x):

> Research software is a fundamental and vital part of research, yet significant challenges 
> to discoverability, productivity, quality, reproducibility, and sustainability exist.

So what can we as researchers and technologists do to make our software easier to reproduce and use?
Below are some tips, tricks and best practice to help get you started.

## Established Software Environment Tools

### Conda/Mamba Environments

Conda environments are supported via the [Miniforge3](../Software/Available_Applications/Miniforge3.md) module.

### Python Virtual Environments

TODO: find and point to venv

## New Tools for Reproducible Environments

### uv

The [uv](../Software/Available_Applications/uv.md) package manager is available as module.

### pixi

TODO: new page

### anything else work mentioning?


## Containerisation

Containers are supported on Mahuika via [Apptainer](Available_Applications/Apptainer.md).

## Compiled Software

In addition to the ability to search available modules using `module spider <search-term>`, all installed modules and available versions can be found in [this table](Available_Applications/index.md).
