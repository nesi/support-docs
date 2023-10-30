---
created_at: '2018-07-31T10:13:22Z'
hidden: false
label_names: []
position: 15
title: Finding Software
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000360576
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

## Environment Modules

NeSI uses environment modules to manage [installed
software](https://support.nesi.org.nz/hc/articles/360000170355).

Using the `module` command you can:

-   View loaded modules:
    ``` highlight
    module list
    ```
-   List all available modules
    ``` highlight
    module avail
    ```
-   Load a module:
    ``` highlight
    module load Python/2.7.14-gimkl-2017a
    ```
-   Switch out a loaded module for a different version:
    ``` highlight
    module switch Python/2.7.14-gimkl-2017a Python/3.6.3-gimkl-2017a
    ```

## Lmod on Mahuika

As on Pan, Mahuika uses an enhanced version of modules called
[Lmod](https://lmod.readthedocs.io/en/latest/010_user.html) .

Lmod extends the basic environment modules by adding simple shortcuts
and a more powerful search capability. The `ml` shortcut can be used in
place of `module`. With Lmod you can:

-   View loaded modules:
    ``` highlight
    ml
    ```
-   List all available modules:
    ``` highlight
    ml spider
    ```
-   Use “spider” to search for modules, e.g. “Python” modules:
    ``` highlight
    ml spider Python
    ```
-   Load a module:
    ``` highlight
    ml Python/2.7.14-gimkl-2017a
    ```
-   Prefix a module with “-“ to unload it, e.g. switch from Python 2 to
    Python 3:
    ``` highlight
    ml -Python/2.7.14-gimkl-2017a Python/3.6.3-gimkl-2017a
    ```
-   To get a fresh environment, we recommend that you log out and log in
    again. By logging out and logging in again you will revert to not
    only the default set of modules, but also the default set of
    environment variables.

Further information can be found in the online [User Guide for
Lmod](https://lmod.readthedocs.io/en/latest/010_user.html).

## Modules on Māui

On Māui and Māui\_Ancil we use top level modules to provide the
different software stacks. Per default the "NeSI" module is loaded,
which provides access to the different NeSI software stacks.

On Māui XC nodes an improved version of the modules framework is
provided. Therewith you can also search for modules using a sub-string
using the "-S" option, e.g.

``` highlight
module avail -S netcdf
```

as a result you will also find modules having the substring "netcdf" in
name, e.g. cray-netcdf.

NOTE: The substring search will be soon implemented by default, then you
do not need to specify the -S anymore. Furthermore, this improvement
should be also ported to the Māui\_Ancil part.

 

NOTE: you can create your own modules. This is described
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000474535-Installing-Third-Party-applications).
