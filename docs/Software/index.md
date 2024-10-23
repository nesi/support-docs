---
created_at: '2018-07-31T10:13:22Z'
tags: []
title: Software
vote_count: 1
vote_sum: 1
---

## Environment Modules

NeSI uses environment modules to manage [installed software](../Supported_Applications/index.md).

Using the `module` command you can:

- View loaded modules:
- List all available modules
- Load a module:
- Switch out a loaded module for a different version:

## Lmod on Mahuika

As on Pan, Mahuika uses an enhanced version of modules called
[Lmod](https://lmod.readthedocs.io/en/latest/010_user.html) .

Lmod extends the basic environment modules by adding simple shortcuts
and a more powerful search capability. The `ml` shortcut can be used in
place of `module`. With Lmod you can:

- View loaded modules:
- List all available modules:
- Use “spider” to search for modules, e.g. “Python” modules:
- Load a module:
- Prefix a module with “-“ to unload it, e.g. switch from Python 2 to
  Python 3:
- To get a fresh environment, we recommend that you log out and log in
    again. By logging out and logging in again you will revert to not
    only the default set of modules, but also the default set of
    environment variables.

Further information can be found in the online [User Guide for
Lmod](https://lmod.readthedocs.io/en/latest/010_user.html).

!!! prerequisite "What Next"
    You can create your own modules. This is described
    [here](../../Scientific_Computing/HPC_Software_Environment/Installing_Third_Party_applications.md).
