---
created_at: '2019-08-16T01:22:03Z'
tags:
  - lmod
  - modules
  - containers
  - environment
description: Details the different methods available to access software on the NeSI cluster.
---

{{description}}

## Environment Modules

Environment Modules are a convenient way to access already installed applications on the cluster,
a list of which can be found in the [Software Catalouge](Software_Catalouge/index.md).

'loading' a module prepares the environment you need to run an application.

### Module Command

This is all done using the `module` command.

|  Command                      | Description                                                   |
|-------------------------------|---------------------------------------------------------------|
| `module spider`               | Lists all available modules.                                  |
| `module spider [module name]` | Searches available modules for [module name]                  |
| `module load [module name]`   | Loads [module name], and its dependencies                     |
| `module unload [module name]` | Unloads [module name], and its dependencies                   |
| `module purge`                | Unloads all modules.                                          |
| `module list [module name]`   | Lists currently loaded modules.                               |
| `module show [module name]`   | Shows information about [module name]                         |
|-------------------------------|---------------------------------------------------------------|

For a full list of module commands run `man module` or visit the
[lmod documentation](https://lmod.readthedocs.io/en/latest/010_user.html).

!!! tip
    You can create your own modules. See
    [Installing Third Party applications](Installing_Third_Party_applications.md).

### Version Management

Much of the software installed on the NeSI cluster have multiple
versions available as shown in the
[Software Catalouge](Software_Catalouge/index.md)
or by using the `module spider` command.

If only the application name is given a default version will be chosen,
generally the most recent one. However it is good practice to load
modules using the specific version so you can ensure consistent
execution of your job even after the default version has been changed.

If you need a specific version of software, feel free to ask support and
we may install it, for example.

``` sh
module load ANSYS
```

Will load the default version of ANSYS, in this case {{applications.ANSYS.default}}, however
this may change.

``` sh
module load ANSYS/18.1
```

Will always load that version specifically.

## Self Install

You are welcome to install software yourself, either in your `home` or `project` directories.
See [Building Software](Building_Software/index.md) for more info.

If you require assistance, don't hesitate to {% include "partials/support_request.html" %}.

## Installion Request

To request that we install a scientific application (either a new
application, or a new version of an already installed application),
please {% include "partials/support_request.html" %}.

??? Information to Include in Request
    - What is the name and version number of the software you would like
      to be installed? If you wish to use a copy from a version control
      repository, what tag or release do you need? Please be aware that we
      usually require a stable release version of a piece of software
      before we will install it for all users.
    - Why would you like us to install this software package?
    - What is the web site or home web page of the package? If you don't
      know this information or the package doesn't have a web site, who is
      the author or lead developer? In some cases, there exist two or more
      packages with the same or very similar names. If we know the web
      site we can be sure that we are installing the same package that you
      are requesting.
    - How is the package installed? For example, compiled from source,
      precompiled binary, or installed as a Python, Perl, R, etc. library?
    - What dependencies, if any, does the package require? Please be aware
      that the exact dependency list may depend on the particular use
      cases you have in mind (like the ability to read and write a
      specific file format).
    - Have you (or another member of your project team) tried to install
      it yourself on a NeSI system? If so, were you successful?
    - If you or your institution doesn't own the copyright in the
      software, under what licence are you permitted to use it? Does that
      licence allow you to install and run it on a NeSI system? (Hint:
      Most free, open-source software licences will allow you to do this.)
    - Who else do you know of who wants to use that software on a NeSI
      system? Please provide their names, institutional affiliations, and
      NeSI project codes (if you know them).
    - What tests do you have that will allow us to verify that the
      software is performing correctly and at an acceptable speed?

Our team will review your request and will make a decision as to whether
we will install the application and make it generally available.
