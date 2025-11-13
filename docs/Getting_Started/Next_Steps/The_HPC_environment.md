---
created_at: '2019-08-16T01:22:03Z'
tags:
- software
description: Information about the modules available
---

## Environment Modules

Modules are a convenient way to provide access to applications on the cluster.
They prepare the environment you need to run an application.

For a full list of module commands run `man module` or visit the [`lmod` documentation](https://lmod.readthedocs.io/en/latest/010_user.html).

|  Command                      | Description                                                   |
|-------------------------------|---------------------------------------------------------------|
| `module spider`               | Lists all available modules. (only Mahuika)                   |
| `module spider [module name]` | Searches available modules for \[module name\] (only Mahuika) |
| `module show [module name]`   | Shows information about \[module name\]                       |
| `module load [module name]`   | Loads \[module name\]                                         |
| `module list [module name]`   | Lists currently loaded modules.                               |
