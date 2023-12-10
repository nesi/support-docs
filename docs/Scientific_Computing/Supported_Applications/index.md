---
title: Supported Applications
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/appHeader.md" %}
[//]: <> (APPS PAGE BOILERPLATE END)
=== "Mahuika"

    On Mahuika, and Ancillary nodes (both Mahuika and Māui) software packages are provided using 'lmod' an implementation of Environment Modules with [additional features](https://lmod.readthedocs.io/en/latest/010_user.html).
    
    A list of available software can be obtained with the `module spider` command.

=== "Maui"

    On Māui (XC50), software packages are provided using traditional Environment Modules. No modules are loaded by default.
    
    A list of available software can be obtained with the `module avail` command.
