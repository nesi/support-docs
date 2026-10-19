---
created_at: 2026-01-13
title: "Environment & Modules"
description: How environment variables and modules control which software you can use on Mahuika, and how to load a specific version
tags:
- tutorial
- software
status: tutorial
---

!!! time "20 Minutes"

!!! objectives
    - Load and use a software package.
    - Explain how the shell environment changes when the module mechanism loads packages.

On a high-performance computing system, it is seldom the case that the software we want to use is available when we log in. It is installed, but we will need to "load" it before it can run.

Before we start using individual software packages, however, we should understand the reasoning behind this approach.
The three biggest factors are:

- software incompatibilities
- versioning
- dependencies

**Software incompatibility** is when the presence (or absence) of a software package will break others that depend on it.
Two of the most famous examples are Python 2 and Python 3, and C++ library versions.
Python 3 famously provides a `python` command that conflicts with that provided by Python 2.
Software compiled against a newer version of the C++ standard library and then used when they are not present will result in a nasty `'GLIBCXX_3.4.20' not found` error, for instance.

<!-- I think python is a bad example here as "python 2 and python 3 conflict" sounds like a versioning issue. -->

**Software versioning** is an issue if a team depends on a certain package version for their research project - if the software version was to change (for instance, if a package was updated), it might affect their results.
Having access to multiple software versions allows a set of researchers to prevent software versioning issues from affecting their results.

**Dependencies** are where a particular software package (or even a particular version) depends on having access to another software package (or even a particular version of another software package).
For example, the VASP materials science software may depend on having a particular version of the FFTW (Fastest Fourier Transform in the West) software library available for it to work.

## Environment

Before understanding environment modules we first need to understand what is meant by _environment_.

The environment is defined by its _environment variables_.

_Environment variables_ are named variables that programs started from your shell can read.

We can create an environment variable named "FOO" with the value "bar" using the syntax:

```sh
export FOO="bar"
```

Without `export`, `FOO` would only be a variable in your current shell, and programs you start would not see it.
By convention, environment variable names are written in capitals.

Our new variable can be referenced using `$FOO`, you could also use `${FOO}`, enclosing a variable in curly brackets is good practice as it avoids possible ambiguity.

```sh
$FOO
```

```out
-bash: bar: command not found
```

We got an error here because the variable is evaluated _in the terminal_ then executed.
If we just want to print the variable we can use the command `echo`:

```sh
echo $FOO
```

```out
bar
```

We can get a full list of environment variables using the command `env`:

```sh
env
```

```out
[removed some lines for clarity]
SHELL=/bin/bash
HISTSIZE=10000
HOME=/home/username
USER=username
FOO=bar
```

These variables control many aspects of how your terminal, and any software launched from your terminal works.

`USER` is the variable we used to name your directory in [Bash Shell](Bash_Shell.md#creating-directories). It holds your username:

```sh
echo $USER
```

```out
username
```

## Environment modules

The three problems from the start of this lesson, software incompatibility, versioning and dependencies, are what modules solve.
A _module_ is a self-contained description of a software package -- it contains the settings required to run a software package and, usually, encodes required dependencies on other software packages.

There are a number of environment module implementations commonly used on HPC systems: the two most common are _TCL modules_ and _Lmod_, Mahuika uses Lmod
Both of these use similar syntax and the concepts are the same so learning to use one will allow you to use whichever is installed on the system you are using.
In both implementations the `module` command is used to interact with environment modules.
An additional sub-command is usually added to the command to specify what you want to do.
For a list of sub-commands you can use `module -h` or `module help`.
As for all commands, you can access the full help on the _man_ pages with `man module`.
On Mahuika, we use Lmod.

### Purging modules

Depending on how you are accessing the cluster, the modules you have loaded by default will be different.
So before we start listing our modules we will first use the `module purge` command to clear all but the minimum default modules so that we are all starting with the same modules.

```sh
module purge
```

```out
The following modules were not unloaded:
  (Use "module --force purge" to unload all):

  1) NeSI/zen3
```

Note that `module purge` is informative.
It lets us know that all but a minimal default set of packages have been unloaded (and how to actually unload these if we truly so desired).
The module it keeps, `NeSI/zen3`, sets up Mahuika's research software stack: it makes the other modules available,
and adds the directory holding Mahuika's own commands, such as `storage_quota`, to your `PATH`.

`module purge` is a useful tool for ensuring repeatable research by guaranteeing that the environment that you build your software stack from is always the same.
This is important since some modules have the potential to silently affect your results if they are loaded (or not loaded).

!!! warning "Think before you copy/paste code"
    Just because you see a command, you don't have to run it.
    Removing `NeSI/zen3` will break your environment: you won't be able to load any other modules, and commands such as `storage_quota` stop working.
    You _do not_ want to run `module --force purge`.
    If you do, log out and log back in to get `NeSI/zen3` back.

### Listing available modules

To see available software modules, use `module avail`:

```sh
module avail
```

```out
--------------------------- /opt/nesi/lmod/generic ----------------------------
   BLASTDB/2025-08        EESSI/2025.06            NeSI/zen4       (S)
   BLASTDB/2026-01        gufi                     nesi_eb/mahuika
   BLASTDB/2026-04        NeSI/mahuika  (S)        nesi_eb/zen3    (D)
   BLASTDB/2026-08 (D)    NeSI/zen3     (S,L,D)

----------------------------- /opt/nesi/lmod/zen3 -----------------------------
   Abseil/20260107.1-GCC-15.2.0                                (D)
   Amber/24.0-foss-2023a-AmberTools-25.0-CUDA-12.5.0
   AMRFinderPlus/4.2.7-foss-2023a                              (D)
   ANIcalculator/1.0-GCC-15.2.0                                (D)
   any2fasta/0.8.1-GCC-12.3.0                                  (D)
   AOCL-BLAS/5.2.2-GCC-15.2.0

[removed most of the output here for clarity]

Use "module spider" to find all possible modules and extensions.
Use "module keyword key1 key2 ..." to search for all possible modules matching
any of the "keys".
```

!!! tip "module spider"
    `module avail` is picky about capitalisation and spelling.
    If you are struggling to find a module, you can try `module spider` followed by the package name (for example `module spider python`), which will search the available modules without case sensitivity and return descriptions of the available modules.

### Listing currently loaded modules

You can use the `module list` command to see which modules you currently have loaded in your environment.
On Mahuika you will have a few default modules loaded when you log in.

```sh
module list
```

```out
Currently Loaded Modules:
  1) NeSI/zen3 (S)

  Where:
   S:  Module is Sticky, requires --force to unload or purge
```

## Loading software

You can load software using the `module load` command.
In this example we will be using the programming language _R_.

Initially, R is not loaded.
We can test this by using the `which` command.
`which` looks for programs the same way that Bash does, so we can use it to tell us where a particular piece of software is stored.

```sh
which R
```

```out
/usr/bin/which: no R in (/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/username/bin:/home/username/.local/bin:/opt/nesi/bin:/opt/nesi/sbin)
```

The important bit here being:

```out
/usr/bin/which: no R in (...)
```

Now let's try loading the R environment module, and try again.

```sh
module load R
which R
```

```out
/opt/nesi/zen3/R/{{ applications.R.default }}/bin/R
```

!!! note "Tab Completion"
    The module command also supports tab completion. You may find this the easiest way to find the right software.

### The `PATH` variable

So, what just happened?

To understand the output, first we need to understand the nature of the `$PATH` environment variable.
`$PATH` is a special environment variable that controls where a UNIX system looks for software.
Specifically `$PATH` is a list of directories (separated by `:`) that the OS searches through for a command before giving up and telling us it can't find it.
As with all environment variables we can print it out using `echo`.

```sh
echo $PATH
```

```out
/opt/nesi/zen3/R/{{ applications.R.default }}/bin:/opt/nesi/CS400_centos7_bdw/pandoc/2.8.0.1/bin:/opt/nesi/zen3/libgit2/1.9.3-GCC-15.2.0/bin:/opt/nesi/zen3/FFTW/3.3.10-GCC-15.2.0/bin:/opt/nesi/zen3/FlexiBLAS/3.5.0-GCC-15.2.0/bin:/opt/nesi/zen3/OpenMPI/5.0.10-GCC-15.2.0/bin:/opt/nesi/zen3/UCC/1.7.0-GCCcore-15.2.0/bin:/opt/nesi/zen3/UCX/1.20.0-GCCcore-15.2.0/bin:/opt/nesi/zen3/binutils/2.45-GCCcore-15.2.0/bin:/opt/nesi/zen3/GCCcore/15.2.0/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/username/bin:/opt/nesi/vdt:/home/username/.local/bin:/opt/nesi/bin:/opt/nesi/sbin
```

We can improve the readability of this command slightly by replacing the colon delimiters (`:`) with newline (`\n`) characters.

```sh
echo $PATH | tr ":" "\n"
```

??? info "Wait, what did I just run??"
    The `|` is called a pipe and sends the output of one command as the input to a subsequent command.
    So here we passed the output of `echo $PATH` to the command `tr` (translate) and told it to replace any `:` with a new line (`\n`).
    For more information about pipes and command line operations, check out the [Unix Shell workshop materials](https://swcarpentry.github.io/shell-novice/index.html).

```out
/opt/nesi/zen3/R/{{ applications.R.default }}/bin
/opt/nesi/CS400_centos7_bdw/pandoc/2.8.0.1/bin
/opt/nesi/zen3/libgit2/1.9.3-GCC-15.2.0/bin
/opt/nesi/zen3/FFTW/3.3.10-GCC-15.2.0/bin
/opt/nesi/zen3/FlexiBLAS/3.5.0-GCC-15.2.0/bin
/opt/nesi/zen3/OpenMPI/5.0.10-GCC-15.2.0/bin
/opt/nesi/zen3/UCC/1.7.0-GCCcore-15.2.0/bin
/opt/nesi/zen3/UCX/1.20.0-GCCcore-15.2.0/bin
/opt/nesi/zen3/binutils/2.45-GCCcore-15.2.0/bin
/opt/nesi/zen3/GCCcore/15.2.0/bin
/usr/local/bin
/usr/bin
/usr/local/sbin
/usr/sbin
/home/username/bin
/opt/nesi/vdt
/home/username/.local/bin
/opt/nesi/bin
/opt/nesi/sbin
```

You'll notice a similarity to the output of the `which` command.
However, in this case, there are a lot more directories at the beginning.
When we ran the `module load` command, it added many directories to the beginning of our `$PATH`.

Looking at the first line: `/opt/nesi/zen3/R/{{ applications.R.default }}/bin`

Let's examine what's there:

```sh
ls /opt/nesi/zen3/R/{{ applications.R.default }}/bin
```

```out
R  Rscript
```

### Dependencies

`module load` "loads" not only the specified software, but it also loads software dependencies.
That is, the software that the application you load requires to run.

To demonstrate, let's use `module list`.

```sh
module list
```

```out
Currently Loaded Modules:
  1) NeSI/zen3                    (S)  11) gompi/2026
  2) GCCcore/15.2.0                    12) FFTW.MPI/3.3.10-gompi-2026
  3) binutils/2.45-GCCcore-15.2.0      13) ScaLAPACK/2.2.2-gompi-2026-fb
  4) GCC/15.2.0                        14) foss/2026
  5) UCX/1.20.0-GCCcore-15.2.0         15) NLopt/2.10.1-GCC-15.2.0
  6) UCC/1.7.0-GCCcore-15.2.0          16) libgit2/1.9.3-GCC-15.2.0
  7) OpenMPI/5.0.10-GCC-15.2.0         17) GMP/6.3.0-GCCcore-15.2.0
  8) OpenBLAS/0.3.32-GCC-15.2.0        18) Arrow/24.0.0-GCC-15.2.0
  9) FlexiBLAS/3.5.0-GCC-15.2.0        19) pandoc/2.8.0.1
 10) FFTW/3.3.10-GCC-15.2.0            20) R/4.6.0-foss-2026

  Where:
   S:  Module is Sticky, requires --force to unload or purge
```

Notice that our initial list of modules has increased by 19.
When we loaded R, it also loaded all of its dependencies along with all the dependencies of those modules.

Before moving onto the next session let's use `module purge` again to return to the minimal environment.

```sh
module purge
```

```out
The following modules were not unloaded:
  (Use "module --force purge" to unload all):

  1) NeSI/zen3
```

## Software versioning

So far, we've learned how to load software packages.
However, we have not yet addressed the issue of software versioning.
At some point or other, you will run into issues where only one particular version of some software will be suitable.
Perhaps a key bug fix only happened in a certain version, or version _X_ broke compatibility with a file format you use.
In either of these example cases, it helps to be specific about what software is loaded.

Let's examine the output of `module avail Python`, which lists only the modules with 'Python' in their name.

```sh
module avail Python
```

```out
----------------------------- /opt/nesi/lmod/zen3 -----------------------------
[removed some lines for clarity]
   Python-Geo/3.11.6-foss-2023a
   Python-Geo/3.14.4-foss-2026                                 (D)
   python-igraph/1.0.0-foss-2023a
   Python/3.14.4-foss-2026                                     (D)
[removed some lines for clarity]

--------------------------- /opt/nesi/lmod/mahuika ----------------------------
[removed some lines for clarity]
   Python/2.7.16-gimkl-2018b
   Python/2.7.18-gimkl-2020a
   Python/3.7.3-gimkl-2018b
   Python/3.8.1-gimkl-2018b
   Python/3.8.2-gimkl-2020a
   Python/3.9.5-gimkl-2020a
   Python/3.9.9-gimkl-2020a
   Python/3.10.5-gimkl-2022a
   Python/3.11.3-gimkl-2022a
   Python/3.11.6-foss-2023a
[removed most of the output here for clarity]

  Where:
   D:  Default Module
```

Let's take a closer look at the `Python` modules.
There are many applications that are run using Python and may fail to run if the wrong version is loaded.
In this case, there are many different versions: `Python/2.7.16-gimkl-2018b`, `Python/3.7.3-gimkl-2018b` through to the newest versions.

How do we load a specific version and which version is the default?

In this case, `Python/{{ applications.Python.default }}` has a `(D)` next to it.
This indicates that it is the default &mdash; if we type `module load Python`, this is the version that will be loaded.

```sh
module load Python
python3 --version
```

```out
Python {{ applications.Python.default.split('-')[0] }}
```

## Non-default versions

So how do we load the non-default version of a software package?
In this case, the only change we need to make is be more specific about the module we are loading.
There are many other Python versions.
To load a non-default module, the only change we need to make to our `module load` command is to add the version number after the `/`.

```sh
module load Python/3.9.5-gimkl-2020a
```

```out
The following have been reloaded with a version change:
  1) GCC/15.2.0 => GCC/9.2.0
  2) GCCcore/15.2.0 => GCCcore/9.2.0
  3) HDF5/1.14.6-gompi-2026 => HDF5/1.10.5-gimpi-2020a
  4) METIS/5.1.0-GCC-15.2.0 => METIS/5.1.0-GCCcore-9.2.0
  5) Python/3.14.4-foss-2026 => Python/3.9.5-gimkl-2020a
  6) SuiteSparse/7.12.2-gfbf-2026 => SuiteSparse/5.6.0-gimkl-2020a-METIS-5.1.0
  7) binutils/2.45-GCCcore-15.2.0 => binutils/2.32-GCCcore-9.2.0
  8) netCDF/4.9.3-gompi-2026 => netCDF/4.7.3-gimpi-2020a
```

Notice how the module command has swapped out versions of the Python module, and of the modules it depends on.
And now we can test which version of Python we are using:

```sh
python3 --version
```

```out
Python 3.9.5
```

Let's take a look at what is now loaded:

```sh
module list
```

```out
Currently Loaded Modules:
  1) NeSI/zen3                                 (S)
  2) GCCcore/9.2.0
  3) zlib/1.2.11-GCCcore-9.2.0
  4) binutils/2.32-GCCcore-9.2.0
  5) GCC/9.2.0
  6) libpmi/1
  7) impi/2019.6.166-GCC-9.2.0
  8) gimpi/2020a
  9) imkl/2020.0.166-gimpi-2020a
 10) gimkl/2020a
 11) bzip2/1.0.8-GCCcore-9.2.0
 12) XZ/5.2.4-GCCcore-9.2.0
 13) libpng/1.6.37-GCCcore-9.2.0
 14) freetype/2.10.1-GCCcore-9.2.0
 15) Szip/2.1.1-GCCcore-9.2.0
 16) HDF5/1.10.5-gimpi-2020a
 17) libjpeg-turbo/2.0.2-GCCcore-9.2.0
 18) ncurses/6.1-GCCcore-9.2.0
 19) libreadline/8.0-GCCcore-9.2.0
 20) libxml2/2.9.10-GCCcore-9.2.0
 21) libxslt/1.1.34-GCCcore-9.2.0
 22) LegacySystemLibs/.crypto7                 (H)
 23) cURL/7.64.0-GCCcore-9.2.0
 24) PCRE/8.43-GCCcore-9.2.0
 25) netCDF/4.7.3-gimpi-2020a
 26) SQLite/3.31.1-GCCcore-9.2.0
 27) METIS/5.1.0-GCCcore-9.2.0
 28) tbb/2019_U9-GCCcore-9.2.0
 29) SuiteSparse/5.6.0-gimkl-2020a-METIS-5.1.0
 30) Tcl/8.6.10-GCCcore-9.2.0
 31) Tk/8.6.10-GCCcore-9.2.0
 32) LLVM/10.0.1-GCCcore-9.2.0
 33) OpenSSL/1.1.1k-GCCcore-9.2.0
 34) Python/3.9.5-gimkl-2020a

  Where:
   H:  Hidden Module
   S:  Module is Sticky, requires --force to unload or purge
```

!!! keypoints
    - Load software with `module load softwareName`.
    - Load a specific version with `module load softwareName/version`, as the default version can change.

!!! postrequisite "What Next"
    - [Submitting Your First Job](Submitting_Your_First_Job.md)
