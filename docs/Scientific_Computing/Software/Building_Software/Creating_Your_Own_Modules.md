---
created_at: 2025-02-21
tags:
 - lmod
 - modules
---

You can create personalised module environments, which can load modules
and set up environment variables. For example, you could define a
modules in a project directory
`/nesi/project/<projectID>/modulefiles/ProdXY` as the following:

In the first lines, we can set conflicts with other modules (here named
ProdABC). Then we load some dependency modules and provide some
description. The additional lines depend on your requirements for the
module. With *set* you can define internal variables (within this module
file). The command *setenv* defines a environment variable. And
*prepend-path* and *append-path* extend an environment variable at the
front or end.

There are common environment variables like:

- *PATH* for providing executabl,
- *LD\_LIBRARY\_PATH* for self created libraries,
- *PYTHONPATH* for providing Python modules,
- *CONDA\_ENVS\_PATH* for providing Conda environments,
- etc.

And others which are very application specific.

To use the module (or all in that directory and sub-directories) we need
to register that directory to the module environment. This can be done
by setting the following environment variable:

by adding that line to your `$HOME/.bashrc` you will have the modules
always available.

The module then can be loaded by:

These modules can easily be shared with collaborators. They just need to
specify the last two steps.
