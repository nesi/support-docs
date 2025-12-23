---
created_at: '2019-07-04T20:48:57Z'
tags:
    - software
    - versions
    - toolchain
    - module
title: Software Version Management
---

## Software Versions

Much of the software installed on the NeSI cluster have multiple
versions available as shown on the
[supported applications page](Available_Applications/index.md)
or by using the `module avail` or `module spider` commands.

If only the application name is given a default version will be chosen,
generally the most recent one. However it is good practice to load
modules using the specific version so you can ensure consistent
execution of your job even after the default version has been changed.

If you need a specific version of software, feel free to ask support and
we may install it.

#### Example

``` bash
module load ANSYS
```

Will load the default version of ANSYS, in this case {{applications.ANSYS.default}}, however
this may change.

``` bash
module load ANSYS/18.1
```

Will always load that version specifically.

## Toolchains and Environment Management

### Compiler Toolchains

Many of the software modules on the cluster are built with a specific compiler toolchain (often referred to as simply a _toolchain_).  A toolchain 
is the compiler and development libraries that are used to build software on the cluster.

You can see this in the module version, such as the following:

``` bash
Python/3.11.6-foss-2023a
PnetCDF/1.9.0-intel-2020a
```

The software version and toolchain are separated by the first hyphen, for instance the 
version of Python is `3.11.6` and the toolchain it was built with is `foss-2023a`.  Whareas 
PnetCDF was built with `intel-2020a`  These are incompatible toolchains since they use different 
compilers and have conflicting dependencies.  Therefore loading these modules in the 
same environment with either conflict and fail, or will swap module dependencies which will 
cause some of your software to crash or fail with a library error.  For example if I try to 
load the software above I receive the following notification:

```out
The following have been reloaded with a version change:
  1) GCCcore/12.3.0 => GCCcore/9.2.0
  2) binutils/2.40-GCCcore-12.3.0 => binutils/2.32-GCCcore-9.2.0
  3) zlib/1.2.13-GCCcore-12.3.0 => zlib/1.2.11-GCCcore-9.2.0
```

Python and other applications may initially run without error, but at some point a 
compatibility or conflict error will arise. So if you ever see a notification of reloading 
module versions, check the module toolchain versions.  

If you need help with this or require a software built with a specific toolchain reach out to 
<support@nesi.org.nz>

### System Toolchain

If a module has no toolchain in it's name, then it is built with the `System` toolchain and 
should be compatible with all other toolchains.  Examples of this are utilities such as `zlib`, 
`binutils` and others, for example:

```out
binutils/2.32
CUDA/12.5.0
```
