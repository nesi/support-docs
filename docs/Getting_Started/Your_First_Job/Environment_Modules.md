---
created_at: 2024-10-11
description: How to access software on the NeSI cluster with the use of environment modules.
tags: []
---



## Environment Modules

For most users _Environment modules_ are the most convenient way to provide access to applications on the cluster.

NeSI staff centrally install and maintain a wide range of applications. Each of these software packages require a specific set of environment variables in order to work. It would not be possible to have all the software accessible, as many of these environment variables would interfere with each other (especially in the case of multiple versions of the same software).

An _Environment Module_ encapsulates all these variables and other dependencies allowing for straight forward loading and unloading as required using the `module` command.

!!! warn  "Other Types of Module"
    These modules are different from 'perl' or 'python' modules and should not be confused with that.

They prepare the environment you need to run an application.

For a full list of module commands run `man module`.

| Command | Description |
| - | - |
| `module spider [ <string> ]` | List all modules whose names, including version strings, contain `<string>`. If the `<string>` argument is not supplied, list all available modules. (only on Mahuika)                                                |
| `module show <string>`       | Show the contents of the module given by `<string>`. If only the module name (e.g. `Python`) is given, show the default module of that name. If both name and version are given, show that particular version module. |
| `module load <string>`       | Load the module (name and version) given by `<string>`. If no version is given, load the default version.|
| `module unload <string>`     | Load the module |
| `module list [ <string> ]`   | List all currently loaded modules whose names, including version strings, contain `<string>`. If the `<string>` argument is not supplied, list all currently loaded modules. |
| `module purge`               | List all currently loaded modules whose names, including version strings, contain `<string>`. If the `<string>` argument is not supplied, list all currently loaded modules.                                          |
