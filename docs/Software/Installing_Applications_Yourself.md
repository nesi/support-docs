---
created_at: '2018-09-24T01:51:32Z'
description: How to configure, compile and install software on the cluster. 
tags: 
  - software
---

Before installing your own applications, first check;

- The software you want is not already installed. `module spider <appname>` can be used to search software,
or see [Supported Applications](index.md).
- If you are looking for a new version of existing software,
{% include "partials/support_request.html" %} and we will install the new version.
- If you would like us to install something for you or help you install something yourself {% include "partials/support_request.html" %}. If the software is popular, We may decide to install it centrally, in which case there will be no additional steps for you. Otherwise the software will be installed in your project directory, in which case it is your responsibility to maintain.

In any case, if you have issues, do not hesitate to
{% include "partials/support_request.html" %}.

See [Software Installation Request](Software_Installation_Request.md) for guidelines on what information you should include.

## Packages for Existing Module

How to add package to an existing module will vary based on the language in question.

- [Python](Available_Applications/Python.md#python-packages)
- [R](Available_Applications/R.md#dealing-with-packages)
- [Julia](Available_Applications/Julia.md#installing-julia-packages)
- [MATLAB](Available_Applications/MATLAB.md#adding-support-packages)

For other languages check if we have additional documentation for it
in our [application documentation](../Scientific_Computing/Supported_Applications/index.md).

## Other Applications

Installation instructions vary from application to application, we suggest you read the provided installing instructions. Nevertheless, the following should give you an impression which steps
you usually need to consider.

### Install Directory

You will need to decide on where you want to install your application.
We recommend using your `project` directory i.e `/nesi/project/<projectID>`,
that way the install can be easily shared with any collaborators.
Move to the desired location and create a directory to work from `mkdir <appname>`.

### Download

Downloading the code can be done in various ways.

- Checkout a git repo `git clone <URL>`
- Downloading a tarball (`wget <URL>.tgz`). Unpack the tarball using the command `tar -xf <downloaded file>.tgz`.

### Load Dependencies

You will probably want to build your application against some of the existing NeSI software stack.
Almost certainly, this will include a toolchain.

```sh
module load foss/{{ applications["foss"].versions | last }}
```

You can read more about the toolchains used in the
[EasyBuild Documentation](https://docs.easybuild.io/common-toolchains/).

Make sure to take a note of the modules used when installing,
as there is a high chance you will need those same modules to be loaded at runtime.

### Configuring

If the source contains a `.configure` file, you may have to run this first.

e.g.

```sh
./configure
```

Often configure options can be listed with `./configure --help`

The documentation of the software you are installing will be the best place to look for instructions.

### Building

- If there is a `Makefile` in the source directory, you can call the command `make`, or `make all`.
- If there is a `CmakeLists.txt` file you will need to;
  
    ```sh
    module load CMake
    mkdir build && cd build
    cmake ../
    make
    ```

### Linking

Your application may depend on one or more external software packages,
normally libraries, and if so it will need to link against them when you
compile the program. In general, to link against an external package,
one must specify:

- The location of the header files, using the option
    `-I/path/to/include`
- The location of the compiled library or libraries, using
    `-L/path/to/lib/`
- The name of each library, typically without prefixes and suffixes.
    For example, if the full library file name is `libfoo.so.1.2.3`
    (with aliases `libfoo.so.1` and `libfoo.so`), the expected entry on
    the link line is `-lfoo`.

Thus the linker expects to find the include headers in the
`/path/to/headers` and the library at `/path/to/lib/lib.so`
(we assume dynamic linking).

The order in which you list libraries matters, as the linker will go through the list
in order of appearance. If library "A" depends on library "B", you will need to specify `-lA -lB` first.

Often you will want to link against libraries included in an easybuild module.
The path to loaded easybuilt libraries are defined in the environment variable
`$EBROOT<library name in upper case>`.

You would include these when linking
e.g. `-L$EBROOT<library name in upper case>/lib`
and `-I$EBROOT<header name in upper case>/include`

### Add to Path

To run your newly installed application, the process may look something like,

```sh
module load foss/{{ applications["foss"].versions | last }} FFTW
/nesi/project/nesi99991/myApplication/bin/launchApplication
```

You may want to make the command accessible on it's own by modifying your `PATH` in your `.bash_profile`.

e.g.

```sh
echo "\$PATH=\$PATH:/nesi/project/nesi99991/myApplication/bin/" >> ~/.bash_profile
source ~/.bash_profile
```

(This only needs to be done once).

You will then be able to launch your application with

```sh
module load foss/{{ applications["foss"].versions | last }} FFTW
/nesi/project/nesi99991/myApplication/bin/launchApplication
```

## Common Issues

### Missing Symbols

This occurs when the linker could not find a function used
in your program or in one of the libraries that you linked against. To
resolve this problem, have a closer look at the function names that the
linker reported:

- Are you missing some object code files (these are compiled source
    files and have suffix `.o`) that should appear on the linker line?
    This can happen if the build system was not configured correctly or
    has a bug. Try running the linking step manually with all source
    files and debug the build system (which can be a lengthy and
    cumbersome process, unfortunately).
- Do the missing functions have names that contain "mp" or "omp"? This
    could mean that some of your source files or external libraries were
    built with OpenMP support, which requires you to set an OpenMP flag
    (`-fopenmp` for GNU compilers, `-qopenmp` for Intel) in your linker
    command.
- Do you see a very long list of complex-looking function names, and
    does your source code or external library dependency include C++
    code? You may need to explicitly link against the C++ standard
    library (`-lstdc++` for GNU compilers, `-cxxlib` for Intel
    compilers); this is a particularly common problem for statically
    linked code.
- Do the function names end with an underscore ("\_")? You might be
    missing some Fortran code, either from your own sources or from a
    library that was written in Fortran, or parts of your Fortran code
    were built with flags such as `-assume nounderscore` (Intel) or
    `-fno-underscoring` (GNU), while others were using different flags.
- Do the function names end with double underscores ("\_\_")? Fortran
    compilers offer an option to add double underscores to Fortran
    subroutine names for compatibility reasons
    (`-h [no]second_underscore`, `-assume [no]2underscores`,
    `-f[no-]second-underscore`) which you may have to add or remove.
- Compiler not necessarily enable preprocessing, which could result in
    `#ifndef VAR; Warning: Illegal preprocessor directive`. For example,
    using preprocessor directives in `.f` files with gfortran requires
    the `-cpp` option.
