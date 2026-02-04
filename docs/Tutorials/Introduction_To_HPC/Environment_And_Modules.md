---
created_at: 2026-01-13
title: "Environment & Modules"
description: How do we load and unload software packages?
tags: 
    - software
status: tutorial
---


!!! time "Time: 20 Minutes"

!!! prerequisite
    - Page Link

!!! objectives
    - Load and use a software package.
    - Explain how the shell environment changes when the module mechanism loads or unloads packages.

On a high-performance computing system, it is seldom the case that the software
we want to use is available when we log in. It is installed, but we will need
to "load" it before it can run.

Before we start using individual software packages, however, we should
understand the reasoning behind this approach. The three biggest factors are:

- software incompatibilities
- versioning
- dependencies

Software incompatibility is a major headache for programmers. Sometimes the
presence (or absence) of a software package will break others that depend on
it. Two of the most famous examples are Python 2 and 3 and C compiler versions.
Python 3 famously provides a `python` command that conflicts with that provided
by Python 2. Software compiled against a newer version of the C libraries and
then used when they are not present will result in a nasty `'GLIBCXX_3.4.20'
not found` error, for instance.

<!-- I think python is a bad example here as "python 2 and python 3 conflict" sounds like a versioning issue. -->

Software versioning is another common issue. A team might depend on a certain
package version for their research project - if the software version was to
change (for instance, if a package was updated), it might affect their results.
Having access to multiple software versions allows a set of researchers to
prevent software versioning issues from affecting their results.

Dependencies are where a particular software package (or even a particular
version) depends on having access to another software package (or even a
particular version of another software package). For example, the VASP
materials science software may depend on having a particular version of the
FFTW (Fastest Fourier Transform in the West) software library available for it
to work.

## Environment

Before understanding environment modules we first need to understand what is meant by _environment_.

The environment is defined by it's _environment variables_.

_Environment Variables_ are writable named-variables.

We can assign a variable named "FOO" with the value "bar" using the syntax.

```sh
FOO="bar"
```

Convention is to name fixed variables in all caps.

Our new variable can be referenced using `$FOO`, you could also use  `${FOO}`,
enclosing a variable in curly brackets is good practice as it avoids possible ambiguity.

```sh
$FOO
```

```out
-bash: bar: command not found
```

We got an error here because the variable is evaluated _in the terminal_ then executed.
If we just want to print the variable we can use the command,

```sh
echo $FOO
```

```out
bar
```

We can get a full list of environment variables using the command,

```sh
env
```

```out
[removed some lines for clarity]
EBROOTTCL=/opt/nesi/CS400_centos7_bdw/Tcl/8.6.10-GCCcore-9.2.0
CPUARCH_STRING=bdw
TERM=xterm-256color
SHELL=/bin/bash
EBROOTGCCCORE=/opt/nesi/CS400_centos7_bdw/GCCcore/9.2.0
EBDEVELFREETYPE=/opt/nesi/CS400_centos7_bdw/freetype/2.10.1-GCCcore-9.2.0/easybuild/freetype-2.10.1-GCCcore-9.2.0-easybuild-devel
HISTSIZE=10000
XALT_EXECUTABLE_TRACKING=yes
MODULEPATH_ROOT=/usr/share/modulefiles
LMOD_SYSTEM_DEFAULT_MODULES=NeSI
SSH_CLIENT=192.168.94.65 45946 22
EBDEVELMETIS=/opt/nesi/CS400_centos7_bdw/METIS/5.1.0-GCCcore-9.2.0/easybuild/METIS-5.1.0-GCCcore-9.2.0-easybuild-devel
LMOD_PACKAGE_PATH=/opt/nesi/share/etc/lmod
```

These variables control many aspects of how your terminal, and any software launched from your terminal works.

## Environment Modules

Environment modules are the solution to these problems. A _module_ is a
self-contained description of a software package -- it contains the
settings required to run a software package and, usually, encodes required
dependencies on other software packages.

There are a number of environment module implementations commonly
used on HPC systems: the two most common are _TCL modules_ and _Lmod_. Both of
these use similar syntax and the concepts are the same so learning to use one
will allow you to use whichever is installed on the system you are using. In
both implementations the `module` command is used to interact with environment
modules. An additional sub-command is usually added to the command to specify
what you want to do. For a list of sub-commands you can use `module -h` or
`module help`. As for all commands, you can access the full help on the _man_
pages with `man module`.

### Purging Modules

Depending on how you are accessing the HPC the modules you have loaded by default will be different. So before we start listing our modules we will first use the `module purge` command to clear all but the minimum default modules so that we are all starting with the same modules.

```sh
module purge
```

```out
The following modules were not unloaded:
  (Use "module --force purge" to unload all):

  1) NeSI/zen3
```

Note that `module purge` is informative. It lets us know that all but a minimal default
set of packages have been unloaded (and how to actually unload these if we
truly so desired).

We are able to unload individual modules, unfortunately within the NeSI system it does not always unload it's dependencies, therefore we recommend `module purge` to bring you back to a state where only those modules needed to perform your normal work on the cluster.

`module purge` is a useful tool for ensuring repeatable research by guaranteeing that the environment that you build your software stack from is always the same. This is important since some modules have the potential to silently effect your results if they are loaded (or not loaded).

### Listing Available Modules

To see available software modules, use `module avail`:

```sh
module avail
```

```out
-------------------------------------------------------------------------- /opt/nesi/lmod/zen3 --------------------------------------------------------------------------
   Amber/24.0-foss-2023a-AmberTools-25.0-CUDA-12.5.0                  HTSlib/1.22-GCC-12.3.0                                   (D)    pixi/0.61.0
   AUGUSTUS/3.5.0-gimkl-2022a-patch1                                  IGV/2.19.4                                                      PLUMED/2.10.0-foss-2023a                   (D)
   AUGUSTUS/3.5.0-gimkl-2022a                                  (D)    IGV/2.19.7                                               (D)    pod5/0.3.28-foss-2023a                     (D)
   Basilisk/20250612-gompi-2023a                               (D)    json-fortran/9.0.2-GCC-12.3.0                                   prokka/1.14.5-GCC-11.3.0
   BayPass/3.0-GCC-12.3.0                                      (D)    JupyterLab/2025.5.0-foss-2023a-4.4.2                     (D)    prokka/1.14.6-apptainer                    (D)
   BCFtools/1.22-GCC-12.3.0                                    (D)    Kraken2/2.1.6-GCC-12.3.0                                 (D)    pstoedit/4.02-GCCcore-12.3.0               (D)
   BCL-Convert/4.2.4                                                  LAMMPS/22Jul2025-foss-2023a-kokkos-CUDA-12.2.2                  pybind11/2.9.2-GCCcore-12.3.0
   BiG-SCAPE/1.1.9-gimkl-2022a-Python-3.11.3                          LAMMPS/22Jul2025-foss-2023a-kokkos                              Python-Geo/3.11.6-foss-2023a               (D)

[removed most of the output here for clarity]

Use "module spider" to find all possible modules and extensions.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".
```

### Listing Currently Loaded Modules

You can use the `module list` command to see which modules you currently have
loaded in your environment. On Mahuika you will have a few default modules loaded when you login.  

```sh
module list
```

```out
Currently Loaded Modules:

  1) NeSI/zen3

```

## Loading and Unloading Software

You can load software using the `module load` command. In this example we will be using the programming language _R_.

Initially, R is not loaded. We can test this by using the `which`
command. `which` looks for programs the same way that Bash does, so we can use
it to tell us where a particular piece of software is stored.

```sh
which R
```

```out
/usr/bin/which: no R in (/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/cwal219/bin:/home/cwal219/.local/bin:/opt/nesi/bin)
```

The important bit here being:

```out
/usr/bin/which: no R in (...)
```

Now lets try loading the R environment module, and try again.

```sh
module load R
which R
```

```out
/opt/nesi/zen3/R/4.3.2-foss-2023a/bin/R
```

!!! note "Tab Completion"

    The module command also supports tab completion. You may find this the easiest way to find the right software.

So, what just happened?

To understand the output, first we need to understand the nature of the `$PATH`
environment variable. `$PATH` is a special environment variable that controls
where a UNIX system looks for software. Specifically `$PATH` is a list of
directories (separated by `:`) that the OS searches through for a command
before giving up and telling us it can't find it. As with all environment
variables we can print it out using `echo`.

```sh
echo $PATH 
```

```out
/opt/nesi/zen3/R/4.3.2-foss-2023a/bin:/opt/nesi/CS400_centos7_bdw/LibTIFF/4.4.0-GCCcore-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/nodejs/18.18.2-GCCcore-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/libgit2/1.6.4-GCC-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/Java/20.0.2:/opt/nesi/CS400_centos7_bdw/Java/20.0.2/bin:/opt/nesi/CS400_centos7_bdw/cURL/8.3.0-GCCcore-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/OpenSSL/1.1/bin:/opt/nesi/CS400_centos7_bdw/SQLite/3.42.0-GCCcore-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/libxml2/2.11.4-GCCcore-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/ncurses/6.4-GCCcore-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/PCRE2/10.42-GCCcore-12.3.0/bin:/opt/nesi/zen3/XZ/5.4.2-GCCcore-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/bzip2/1.0.8-GCCcore-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/FFTW/3.3.10-GCC-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/FlexiBLAS/3.3.1-GCC-12.3.0/bin:/opt/nesi/zen3/OpenMPI/4.1.5-GCC-12.3.0/bin:/opt/nesi/zen3/UCC/1.3.0-GCCcore-12.3.0/bin:/opt/nesi/zen3/UCX/1.18.1-GCCcore-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/numactl/2.0.16-GCCcore-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/binutils/2.40-GCCcore-12.3.0/bin:/opt/nesi/CS400_centos7_bdw/GCCcore/12.3.0/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/cwal219/bin:/opt/nesi/vdt:/home/cwal219/.local/bin:/opt/nesi/bin
```

We can improve the readability of this command slightly by replacing the colon delimiters (`:`) with newline (`\n`) characters.

```sh
echo $PATH | tr ":" "\n"
```

??? info "Wait, what did I just run??"
    mention pipe and stuff. point to intro bash.

```out
/opt/nesi/zen3/R/4.3.2-foss-2023a/bin
/opt/nesi/CS400_centos7_bdw/LibTIFF/4.4.0-GCCcore-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/nodejs/18.18.2-GCCcore-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/libgit2/1.6.4-GCC-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/Java/20.0.2
/opt/nesi/CS400_centos7_bdw/Java/20.0.2/bin
/opt/nesi/CS400_centos7_bdw/cURL/8.3.0-GCCcore-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/OpenSSL/1.1/bin
/opt/nesi/CS400_centos7_bdw/SQLite/3.42.0-GCCcore-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/libxml2/2.11.4-GCCcore-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/ncurses/6.4-GCCcore-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/PCRE2/10.42-GCCcore-12.3.0/bin
/opt/nesi/zen3/XZ/5.4.2-GCCcore-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/bzip2/1.0.8-GCCcore-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/FFTW/3.3.10-GCC-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/FlexiBLAS/3.3.1-GCC-12.3.0/bin
/opt/nesi/zen3/OpenMPI/4.1.5-GCC-12.3.0/bin
/opt/nesi/zen3/UCC/1.3.0-GCCcore-12.3.0/bin
/opt/nesi/zen3/UCX/1.18.1-GCCcore-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/numactl/2.0.16-GCCcore-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/binutils/2.40-GCCcore-12.3.0/bin
/opt/nesi/CS400_centos7_bdw/GCCcore/12.3.0/bin
/usr/local/bin
/usr/bin
/usr/local/sbin
/usr/sbin
/home/cwal219/bin
/home/cwal219/.local/bin
```

You'll notice a similarity to the output of the `which` command. However, in this case,
there are a lot more directories at the beginning. When we
ran the `module load` command, it added many directories to the beginning of our
`$PATH`.

Looking at the first line: `/opt/nesi/CS400_centos7_bdw/R/4.2.1-gimkl-2022a/bin` 

Let's examine what's there:

```sh
ls /opt/nesi/zen3/R/4.3.2-foss-2023a/bin
```

```out
R  Rscript 
```

`module load` "loads" not only the specified software, but it also loads software dependencies. That is, the software that the application you load requires to run.

To demonstrate, let's use `module list`.

```sh
module list
```

```out
Currently Loaded Modules:
  1) NeSI/zen3                     (S)   8) UCC/1.3.0-GCCcore-12.3.0     15) ScaLAPACK/2.2.0-gompi-2023a-fb  22) libxml2/2.11.4-GCCcore-12.3.0  29) libgit2/1.6.4-GCC-12.3.0
  2) GCCcore/12.3.0                      9) OpenMPI/4.1.5-GCC-12.3.0     16) foss/2023a                      23) SQLite/3.42.0-GCCcore-12.3.0   30) nodejs/18.18.2-GCCcore-12.3.0
  3) zlib/1.2.13-GCCcore-12.3.0         10) OpenBLAS/0.3.23-GCC-12.3.0   17) bzip2/1.0.8-GCCcore-12.3.0      24) OpenSSL/1.1                    31) LibTIFF/4.4.0-GCCcore-12.3.0
  4) binutils/2.40-GCCcore-12.3.0       11) FlexiBLAS/3.3.1-GCC-12.3.0   18) XZ/5.4.2-GCCcore-12.3.0         25) cURL/8.3.0-GCCcore-12.3.0      32) R/4.3.2-foss-2023a
  5) GCC/12.3.0                         12) FFTW/3.3.10-GCC-12.3.0       19) PCRE2/10.42-GCCcore-12.3.0      26) NLopt/2.7.1-GCC-12.3.0
  6) numactl/2.0.16-GCCcore-12.3.0      13) gompi/2023a                  20) ncurses/6.4-GCCcore-12.3.0      27) GMP/6.2.1-GCCcore-12.3.0
  7) UCX/1.18.1-GCCcore-12.3.0          14) FFTW.MPI/3.3.10-gompi-2023a  21) libreadline/8.2-GCCcore-12.3.0  28) Java/20.0.2
```

Notice that our initial list of modules has increased by 30.  When we loaded R, it also loaded all of it's dependencies along with all the dependencies of those modules.

Before moving onto the next session lets use `module purge` again to return to the minimal environment.

```sh
module purge
```

```out
The following modules were not unloaded:
  (Use "module --force purge" to unload all):

  1) NeSI/zen3
```

!!! warning "Thinking"
    Just because you see a command, you don't have to run it.
    Removing `NeSI/zen3` will break your environment. You _do not_ want to run `module --force purge`

## Software Versioning

So far, we've learned how to load and unload software packages. However, we have not yet addressed the issue of software versioning. At
some point or other, you will run into issues where only one particular version
of some software will be suitable. Perhaps a key bugfix only happened in a
certain version, or version _X_ broke compatibility with a file format you use.
In either of these example cases, it helps to be very specific about what
software is loaded.

Let's examine the output of `module avail` more closely.

```sh
module avail
```

```out
-----------------/opt/nesi/CS400_centos7_bdw/modules/all ------------------
  Flye/2.9-gimkl-2020a-Python-3.8.2      (D)    PyQt/5.10.1-gimkl-2018b-Python-3.7.3
  fmlrc/1.0.0-GCC-9.2.0                         PyQt/5.12.1-gimkl-2018b-Python-2.7.16
  fmt/7.1.3-GCCcore-9.2.0                       PyQt/5.12.1-gimkl-2020a-Python-3.8.2   (D) 
  fmt/8.0.1                              (D)    pyspoa/0.0.8-gimkl-2018b-Python-3.8.1
  fontconfig/2.12.1-gimkl-2017a                 Python-Geo/2.7.14-gimkl-2017a
  fontconfig/2.13.1-GCCcore-7.4.0               Python-Geo/2.7.16-gimkl-2018b
  fontconfig/2.13.1-GCCcore-9.2.0        (D)    Python-Geo/3.6.3-gimkl-2017a
  forge/19.0                                    Python-Geo/3.7.3-gimkl-2018b
  forge/20.0.2                           (D)    Python-Geo/3.8.2-gimkl-2020a
  FoX/4.1.2-intel-2018b                         Python-Geo/3.9.5-gimkl-2020a           (D)
  FragGeneScan/1.31-gimkl-2018b                 Python-GPU/3.6.3-gimkl-2017a
  FreeBayes/1.1.0-gimkl-2017a                   Python/2.7.14-gimkl-2017a
  FreeBayes/1.3.1-GCC-7.4.0                     Python/2.7.16-gimkl-2018b
  FreeBayes/1.3.2-GCC-9.2.0              (D)    Python/2.7.16-intel-2018b
  freetype/2.7.1-gimkl-2017a                    Python/2.7.18-gimkl-2020a
  freetype/2.9.1-GCCcore-7.4.0                  Python/3.6.3-gimkl-2017a
  freetype/2.10.1-GCCcore-9.2.0          (D)    Python/3.7.3-gimkl-2018b
  FreeXL/1.0.2-gimkl-2017a                      Python/3.8.1-gimkl-2018b
  FreeXL/1.0.5-GCCcore-7.4.0             (D)    Python/3.8.2-gimkl-2020a                 (D) 
  FreeXL/1.0.5-GCCcore-9.2.0                    Python/3.9.5-gimkl-2020a
  FriBidi/1.0.10-GCCcore-9.2.0                  qcat/1.1.0-gimkl-2020a-Python-3.8.2

[removed most of the output here for clarity]

----------------------------------- /cm/local/modulefiles -----------------------------------
   cluster-tools/8.0    freeipmi/1.5.5     module-git     openmpi/mlnx/gcc/64/2.1.2a1
   cmd                  gcc/6.3.0          module-info    shared
   cuda-dcgm/1.3.3.1    ipmitool/1.8.18    null
   dot                  lua/5.3.4          openldap

  Where:
   D:  Default Module

Use "module spider" to find all possible modules.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the
"keys".
```

Let's take a closer look at the `Python` modules. There are many applications
that are run using python and may fail to run if the wrong version is loaded.
In this case, there are many different versions: `Python/3.6.3-gimkl-2017a`,
`Python/3.7.3-gimkl-2018b` through to the newest versions.

How do we load each copy and which copy is the default?

In this case, `Python/3.8.2-gimkl-2020a` has a `(D)` next to it. This indicates that it is the
default &mdash; if we type `module load Python`, as we did above, this is the copy that will be
loaded.

```sh
module load Python
python3 --version
```

```out
Python 3.11.6
```

So how do we load the non-default copy of a software package? In this case, the
only change we need to make is be more specific about the module we are
loading. There are many other Python versions.  To load a
non-default module, the only change we need to make to our `module load`
command is to add the version number after the `/`.

```sh
module load Python/3.9.5-gimkl-2020a
```

```out
The following have been reloaded with a version change:
  1) Python 3.11.6-foss-2023a => Python/3.9.5-gimkl-2020a
```

Notice how the module command has swapped out versions of the Python module.
And now we test which version we are using:

```sh
python3 --version
```

```out
Python 3.9.5
```

We are now left with only those module required to do our work for this project.

```sh
module list
```

```out
Currently Loaded Modules:
  1) NeSI/zen3                   (S)  10) gimkl/2020a                        19) libreadline/8.0-GCCcore-9.2.0      28) tbb/2019_U9-GCCcore-9.2.0
  2) GCCcore/9.2.0                    11) bzip2/1.0.8-GCCcore-9.2.0          20) libxml2/2.9.10-GCCcore-9.2.0       29) SuiteSparse/5.6.0-gimkl-2020a-METIS-5.1.0
  3) zlib/1.2.11-GCCcore-9.2.0        12) XZ/5.2.4-GCCcore-9.2.0             21) libxslt/1.1.34-GCCcore-9.2.0       30) Tcl/8.6.10-GCCcore-9.2.0
  4) binutils/2.32-GCCcore-9.2.0      13) libpng/1.6.37-GCCcore-9.2.0        22) LegacySystemLibs/.crypto7     (H)  31) Tk/8.6.10-GCCcore-9.2.0
  5) GCC/9.2.0                        14) freetype/2.10.1-GCCcore-9.2.0      23) cURL/7.64.0-GCCcore-9.2.0          32) LLVM/10.0.1-GCCcore-9.2.0
  6) libpmi/1                         15) Szip/2.1.1-GCCcore-9.2.0           24) PCRE/8.43-GCCcore-9.2.0            33) OpenSSL/1.1.1k-GCCcore-9.2.0
  7) impi/2019.6.166-GCC-9.2.0        16) HDF5/1.10.5-gimpi-2020a            25) netCDF/4.7.3-gimpi-2020a           34) Python/3.9.5-gimkl-2020a
  8) gimpi/2020a                      17) libjpeg-turbo/2.0.2-GCCcore-9.2.0  26) SQLite/3.31.1-GCCcore-9.2.0
  9) imkl/2020.0.166-gimpi-2020a      18) ncurses/6.1-GCCcore-9.2.0          27) METIS/5.1.0-GCCcore-9.2.0
```

!!! keypoints
    - "Load software with `module load softwareName`."
    - "Unload software with `module unload`"
    - "The module system handles software versioning and package conflicts for you
    automatically."

!!! postrequisite
    - Link to next page
