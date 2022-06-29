::: {.wrapper}
::: {.trigger}
 
:::
:::

::: {.wrapper}
Building code on Māui - the Cray XC Programming Environment {#building-code-on-māui---the-cray-xc-programming-environment .post-title}
===========================================================

 

::: {.post-content}
-   [The Cray programming environment on the XC50
    platform](#the-cray-programming-environment-on-the-xc50-platform)
    -   [Overview](#overview)
    -   [The build node](#the-build-node)
    -   [Choosing a programming
        environment](#choosing-a-programming-environment)
    -   [Targetting a CPU](#targetting-a-cpu)
    -   [Using the compiler drivers](#using-the-compiler-drivers)
    -   [Common compiler options](#common-compiler-options)
-   [Building code that depends on external
    libraries](#building-code-that-depends-on-external-libraries)
    -   [Using libraries provided by
        Cray](#using-libraries-provided-by-cray)
    -   [Using libraries provided by
        NeSI/NIWA](#using-libraries-provided-by-nesiniwa)
    -   [Using your own libraries](#using-your-own-libraries)
    -   [Static and dynamic linking](#static-and-dynamic-linking)
    -   [Common linker problems](#common-linker-problems)
-   [Building code on the CS500
    platform](#building-code-on-the-cs500-platform)

 

The Cray programming environment on the XC50 platform
-----------------------------------------------------

### Overview

Building Fortran, C, or C++ code on the XC50 platform requires using the
Cray programming environment. From a user perspective, the programming
environment consists of a set of environment modules that select a
compiler, essential libraries such as the MPI library, a CPU target, and
more. The build process on the XC50 thus differs slightly from a
standard Linux system. Non-compiled code, such as Python or R programs,
do not use the programming environment. Note, however, that loading a
module provided by NeSI/NIWA to get access to, e.g., the "RegCM" code,
may change the Cray programming environment in that Cray environment
modules may be swapped.

**Important:**

-   It is essential to use a Programming Environment (PrgEnv-cray,
    PrgEnv-intel or PrgEnv-gnu) when you build code, otherwise it is
    very likely that problems at build time or run time appear
-   **Never** use `module purge` on the XC50 platform, this will render
    the programming environment unusable, and you will have to log out
    and log back in
-   Code that was built on the XC50 platform is unlikely to run on
    Māui's CS500 platform or on Mahuika's CS400 platform; please rebuild
    your code when you change platform

### The build node

Māui has a dedicated build node, `login.maui.nesi.org.nz`, which should
be used for building code. Please do not build code on the compute nodes
by submitting a build job through SLURM:

-   The compute nodes only run a thin operating system with very few
    command line utilities, it is thus likely that your build will fail
-   The file system on XC50 compute nodes is optimised for handling
    large block IO, small block IO that is typical for a build job is
    inefficient
-   Submitting a job will allocate entire nodes. This is a waste of
    compute resources, especially if only one core or a few cores are
    used

Furthermore, please keep in mind that the build node is a shared
resource. Instead of using as many parallel build processes as possible
(with `make -j`), please limit the amount of processes (`make -j 5` for
example).

### Choosing a programming environment

The following Programming Environments are provided on Māui, named after
the underlying compiler suite:

1.  `PrgEnv-cray`
2.  `PrgEnv-intel`
3.  `PrgEnv-gnu`

The `PrgEnv-cray` environment is the default. If you want to change
programming environment to use the Intel or GNU compilers, run

::: {.highlighter-rouge}
::: {.highlight}
    module swap PrgEnv-cray PrgEnv-intel
:::
:::

or

::: {.highlighter-rouge}
::: {.highlight}
    module swap PrgEnv-cray PrgEnv-gnu
:::
:::

Note that several compiler versions are currently installed, in case of
GNU for example:

::: {.highlighter-rouge}
::: {.highlight}
    > module avail gcc
    -------------------------------------- /opt/modulefiles --------------------------------------
    gcc/4.9.3          gcc/5.3.0          gcc/6.1.0          gcc/7.1.0          gcc/7.3.0(default)
:::
:::

To change GCC version, run for example

::: {.highlighter-rouge}
::: {.highlight}
    module swap gcc gcc/7.1.0
:::
:::

GCC v6.1.0 or later is required to build code that can make use of the
Intel Skylake microarchitecture and its advanced capabilities, such as
AVX-512, on the XC50 platform.

Note: There is not **the** best compiler. Depending on your
application/algorithms, different compilers can optimise the code
better. Keep in mind trying different compilers.

### Targeting a CPU {#targetting-a-cpu}

Compiling a program translates source code into machine instructions. It
is important to let the compiler know for which CPU ("target") the
executable shall be build, to make best use of that CPU's capabilities.
Māui uses Intel Skylake microprocessors on all XC50 build and compute
nodes, which come with AVX-512 vector instructions, enabling better
performance for some codes.

CPU targets can be set by loading a module. By default, module
`craype-x86-skylake` is loaded. In the rare case that you encounter
problems with the Skylake target at build time or run time, try target
for "Broadwell" processors instead:

::: {.highlighter-rouge}
::: {.highlight}
    module swap craype-x86-skylake craype-broadwell
:::
:::

Choosing the "Broadwell" target is also necessary if you want to build
code using the older GCC compilers prior to GCC 6.1.0, which were
released before Skylake became available. If you see the error message

::: {.highlighter-rouge}
::: {.highlight}
    craype-x86-skylake requires cce/8.6 or later, intel/15.1 or later, or gcc/6.1 or later
:::
:::

when trying to swap to the `PrgEnv-gnu` environment, or an error message
of the kind

::: {.highlighter-rouge}
::: {.highlight}
    f951: error: bad value (skylake-avx512) for -march= switch
:::
:::

when you compile a program with a GNU compiler, run

::: {.highlighter-rouge}
::: {.highlight}
    module swap craype-x86-skylake craype-broadwell
:::
:::

and try again.

Make sure that a target is always set. If you do not set a target, the
compilers will produce generic code that runs on many processors of the
"x86-64" family, and the program will thus not be able to benefit from
capabilities such as AVX-512. You will see the following warning message
when you run a compiler:

::: {.highlighter-rouge}
::: {.highlight}
    No supported cpu target is set, CRAY_CPU_TARGET=x86-64 will be used.
    Load a valid targeting module or set CRAY_CPU_TARGET
:::
:::

### Using the compiler drivers

The programming environment provides compiler drivers for compiling
Fortran, C, and C++ code. This means that you will need to use the
following commands instead of the actual compilers:

::: {.highlighter-rouge}
::: {.highlight}
    ftn -o simpleMpi simpleMpi.f90 # compile Fortran code
    cc  -o simpleMpi simpleMpi.c    # compile C code
    CC  -o simpleMpi simpleMpi.cxx  # compile C++ code
:::
:::

The drivers will ensure correct linking of your code with compiler
runtime libraries, and with Cray-supported libraries (such as Cray's
"libsci" scientific library, or Cray's version of netCDF). It is
therefore not recommended to use the compilers directly, there is a good
chance that the executable will fail to build or run correctly.

The compiler drivers automatically add necessary compile and link flags
to the compile/link line for the selected hardware and Cray-supported
libraries. If you are interested in seeing what the compiler driver
does, add the `-craype-verbose` flag:

::: {.highlighter-rouge}
::: {.highlight}
    ftn -craype-verbose -o simpleMpi simpleMpi.f90
:::
:::

Further compiler driver options can be found on their man pages:

::: {.highlighter-rouge}
::: {.highlight}
    man ftn
    man cc
    man CC
:::
:::

The compiler drivers will also automatically build MPI codes correctly,
there is no need to use special compilers or add additional compiler or
linker flags.

Note that running an MPI code on the build node
(`login.maui.nesi.org.nz`) using

::: {.highlighter-rouge}
::: {.highlight}
    ./simpleMPI
:::
:::

will fail with an error message, as there is no MPI runtime environment:

::: {.highlighter-rouge}
::: {.highlight}
    [Wed Oct 18 02:00:14 2017] [c0-0c0s3n1] Fatal error in MPI_Init: Other MPI error, error stack:
    MPIR_Init_thread(537):
    MPID_Init(247).......: channel initialization failed
    MPID_Init(636).......:  PMI2 init failed: 1
:::
:::

If you want to run a short test of your build, use SLURM's srun command
that submits your program to a compute node on the fly, e.g.,

::: {.highlighter-rouge}
::: {.highlight}
    SLURM_PARTITION=nesi_research srun -n 6 simpleMPI
:::
:::

### Common compiler options

Although the compiler drivers `ftn`, `cc` and `CC` have a few options of
their own, such as the `-craype-verbose` flag, they will pass through
any additional compiler options to the underlying compiler. This means
that you will still need to choose compiler flags that are specific to
the Cray, Intel, or GNU compilers, and you will need to change them if
you decide to switch compilers.

For example, if you wanted to use the gfortran compiler, activate
compiler warnings (`-Wall`), and require aggressive compiler
optimisation (`-O3`), you would use the following commands:

::: {.highlighter-rouge}
::: {.highlight}
    module swap PrgEnv-cray PrgEnv-gnu
    ftn -Wall -O3 -o simpleMpi simpleMpi.f90
:::
:::

The following table provides a list of commonly used compiler options:

  Group                              Cray                       Intel                        GNU                                       Notes
  ---------------------------------- -------------------------- ---------------------------- ----------------------------------------- --------------------------------------------------------------------------------------------
  Debugging                          `-g` or `-G{0,1,2,fast}`   `-g` or `-debug [keyword]`   `-g or -g{0,1,2,3}`                       Set level of debugging information, some levels may disable certain compiler optimisations
  Light compiler optimisation        `-O2`                      `-O2`                        `-O2`                                      
  Aggressive compiler optimisation   `-O3 -hfp3`                `-O3 -ipo`                   `-O3 -ffast-math -funroll-loops`          This may affect numerical accuracy
  Vectorisation reports              `-hlist=m`                 `-qopt-report`               `-fopt-info-vec` or `-fopt-info-missed`    
  OpenMP                             `-homp` (default)          `-openmp`                    `-fopenmp`                                 

Additional compiler options are documented on the compiler man pages,
which are accessible *after* loading the corresponding programming
environment:

  language   cray          intel       gnu
  ---------- ------------- ----------- --------------
  Fortran    man crayftn   man ifort   man gfortran
  C          man craycc    man icc     man gcc
  C++        man crayCC    man icpc    man g++

The man pages are often largely incomplete, further documentation can be
found online:

-   Cray Compiler Environment: [Cray Fortran
    v8.7](https://pubs.cray.com/content/S-3901/8.7/cray-fortran-reference-manual/fortran-compiler-introduction),
    [Cray C and C++
    v8.7](https://pubs.cray.com/content/S-2179/8.7/cray-c-and-c++-reference-manual/invoke-the-c-and-c++-compilers)
-   Intel compilers: [Intel Fortran Compiler
    v17.0](https://software.intel.com/sites/default/files/managed/93/88/PDF%20Fortran%20Compiler%20UG%2017.0%3D1%3DSSG%202.0%20PDF%3Den-US.pdf),
    [Intel C and C++ Compiler
    v17.0](https://software.intel.com/sites/default/files/managed/08/ac/PDF%20C%2B%2B%20Compiler%20UG%2017.0%3D1%3DSSG%202.0%20PDF%3Den-US.pdf)
-   GNU compilers: [GCC C and C++
    v4.9.4](https://gcc.gnu.org/onlinedocs/gcc-4.9.4/gcc.pdf), [GCC C
    and C++ v7.1.0](https://gcc.gnu.org/onlinedocs/gcc-7.1.0/gcc.pdf),
    [GNU Fortran
    v4.9.4](https://gcc.gnu.org/onlinedocs/gcc-4.9.4/gfortran.pdf), [GNU
    Fortran v7.1](https://gcc.gnu.org/onlinedocs/gcc-7.1.0/gfortran.pdf)

Building code that depends on external libraries
------------------------------------------------

While linking external libraries, one need to pay attention to the
correct compiler and linker setup. This, depends on the correct library
version (working properly with the compiler and the link type) and the
used link options. These depend on whether the libraries have been
provided by Cray, by NeSI/NIWA, or if you built them yourself.

Many libraries are provided in modules. You can search them using

::: {.highlighter-rouge}
::: {.highlight}
    module avail
:::
:::

and look in the module description using:

::: {.highlighter-rouge}
::: {.highlight}
    module help <module-name>
:::
:::

Sometimes modules provide multiple libraries, e.g. *cray-libsci*.

### Using libraries provided by Cray

If a library has been provided by Cray, the compiler drivers will
automatically take care of adding search paths for include files and
libraries, and they will add the library names to the linker line. For
example, to build a program that uses the netCDF library provided by the
`cray-netcdf` module, run the commands

::: {.highlighter-rouge}
::: {.highlight}
    module load cray-netcdf
    ftn -o simple_xy_wr simple_xy_wr.f90
:::
:::

Keep in mind that such automatic treatment of dependencies will **only**
work if the libraries have been provided by Cray - you can recognise
those by their module name, which always starts with `cray-`, e.g.,
`cray-netcdf`, or `cray-libsci`.

Note also that correct versions of the libraries (Cray CCE, Intel, or
GNU builds) will automatically be used after swapping programming
environment. This is particularly important for libraries that provide
Fortran 90 modules, due to their compiler-specific format.

### Using libraries provided by NeSI/NIWA

The situation is different when you use a library that is provided by
NeSI/NIWA. They can be recognised by the `CrayCCE`, `CrayIntel`, or
`CrayGNU` suffix attached to their version number. In this case, you
will have to provide search paths using the `-I` flag for include files,
and `-L` for library files, and the library names have to be explicitly
added to the linker line. Libraries are not always provided for all
compiler suites and versions.

Note that library names are specified in a specifically formatted form,
`-l<library name>`. The linker then expects to find a library file named
`lib<library name>.a` (for a static library) or `lib<library name>.so`
(for a shared library), e.g., `libnetcdf.a`. Note that you may need to
list several libraries to link successfully, e.g., `-lA -lB` for linking
against libraries "A" and "B". The order in which you list libraries
matters, as the linker will go through the list in order of appearance.
If library "A" depends on library "B", specifying `-lA -lB` will work.
If library "B" depends on "A", use `-lB -lA`. If they depend on each
other, use `-lA -lB -lA` (although such cases are quite rare).

Consider the following example where the `grib_api` library is used:

::: {.highlighter-rouge}
::: {.highlight}
    module load grib_api/1.23.1-CrayGNU-18.08
    cc -I$EBROOTGRIB_API/include -o mygribprogram mygribprogram.c -L$EBROOTGRIB_API/lib -lgrib_api
:::
:::

The EasyBuild software management system that NeSI/NIWA use to provide
modules automatically defines environment variables
`$EBROOT<library name in upper case>` when a module is loaded, which
help pointing the compiler and linker to include files and libraries as
in the example above. If you are unsure which `$EBROOT<...>` variables
are available, use

::: {.highlighter-rouge}
::: {.highlight}
    module show grib_api/1.23.1-CrayGNU-18.08
:::
:::

to find out.

Note that specifying search paths with `-I` and `-L` is not strictly
necessary in case of the GNU and Intel compilers, which will use the
contents of `CPATH`, `LIRARY_PATH`, and `LD_LIBRARY_PATH` provided by
the NeSI/NIWA module. This will not work with the Cray compiler.

**Important note:** Make sure that you load the correct variant of a
library, depending on your choice of compiler. Switching compiler
environment will *not* switch NeSI/NIWA modules automatically.
Furthermore, loading a NeSI/NIWA module may switch programming
environment if it was built with a different compiler.

As mentioned earlier, EasyBuild uses the following module naming
conventions ("toolchain names") to identify the programming environment
that was used to build the software:

-   `CrayCCE` for libraries and tools built with the Cray compilers
    (`PrgEnv-cray`)
-   `CrayIntel` for libraries and tools built with the Intel compilers
    (`PrgEnv-intel`)
-   `CrayGNU` for libraries and tools built with the GNU compilers
    (`PrgEnv-gnu`)

### Using your own libraries

Linking against libraries that you built yourself is the same as linking
against libraries provided by NeSI/NIWA - you will just need to point
the compiler to the location where the include and library files are
using the `-I` and `-L` flags.

### Static and dynamic linking

The XC50 compilers drivers default to static linking where possible for
maximum efficiency, avoiding the need to load shared libraries for
hundreds or thousands of MPI ranks at runtime. If all dependencies are
available as static libraries, the resulting executables will be
completely self-contained (although they may still need the Cray MPI
environment at runtime).

Here is an example that shows how to find out how your code was linked:

::: {.highlighter-rouge}
::: {.highlight}
    module load GSL/2.4-CrayGNU-2017.06
    cc -I$EBROOTGRIB_API/include -o mygribprogram mygribprogram.c -L$EBROOTGRIB_API/lib -lgrib_api
    ldd mygribprogram
:::
:::

If you see the message `not a dynamic executable`, your program was
statically linked. Otherwise you will see a list of shared library
dependencies that are needed at runtime.

If you have to link your code dynamically, either set

::: {.highlighter-rouge}
::: {.highlight}
    export CRAYPE_LINK_TYPE=dynamic
:::
:::

in your build environment (useful when using complex build systems), or
add the `-dynamic` flag to the compiler driver commands, e.g.,

::: {.highlighter-rouge}
::: {.highlight}
    cc -I$EBROOTGRIB_API/include -o mygribprogram mygribprogram.c -L$EBROOTGRIB_API/lib -lgrib_api -dynamic
:::
:::

Using the `ldd` tool, you should now see a number of libraries that are
dynamically linked.

You may occassionally see a warning message of the kind:

::: {.highlighter-rouge}
::: {.highlight}
    /opt/cray/pe/hdf5/1.10.1.1/INTEL/16.0/lib/libhdf5.a(H5PL.o): In function `H5PL_load':
    H5PL.c:(.text+0x612): warning: Using 'dlopen' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking
:::
:::

This simply means that the library must be accessible at runtime despite
fully static linking and the program is thus not entirely
self-contained, which is usually not an issue.

### Common linker problems

Linking can easily go wrong. Most often, you will see linker errors
about "missing symbols" when the linker could not find a function used
in your program or in one of the libraries that you linked against. To
resolve this problem, have a closer look at the function names that the
linker reported:

-   Are you missing some object code files (these are compiled source
    files and have suffix `.o`) that should appear on the linker line?
    This can happen if the build system was not configured correctly or
    has a bug. Try running the linking step manually with all source
    files and debug the build system (which can be a lengthy and
    cumbersome process, unfortunately).
-   Do the missing functions have names that contain "mp" or "omp"? This
    could mean that some of your source files or external libraries were
    built with OpenMP support, which requires you to set an OpenMP flag
    (`-fopenmp` for GNU compilers, `-qopenmp` for Intel) in your linker
    command. For the Cray compilers, OpenMP is enabled by default and
    can be controlled using `-h[no]omp`.
-   Do you see a very long list of complex-looking function names, and
    does your source code or external library dependency include C++
    code? You may need to explicitly link against the C++ standard
    library (`-lstdc++` for GNU and Cray compilers, `-cxxlib` for Intel
    compilers); this is a particularly common problem for statically
    linked code.
-   Do the function names end with an underscore ("\_")? You might be
    missing some Fortran code, either from your own sources or from a
    library that was written in Fortran, or parts of your Fortran code
    were built with flags such as `-assume nounderscore` (Intel) or
    `-fno-underscoring` (GNU), while others were using different flags
    (note that the Cray compiler always uses underscores).
-   Do the function names end with double underscores ("\_\_")? Fortran
    compilers offer an option to add double underscores to Fortran
    subroutine names for compatibility reasons
    (`-h [no]second_underscore`, `-assume [no]2underscores`,
    `-f[no-]second-underscore`) which you may have to add or remove.

Note that the linker requires that function names match exactly, so any
variation in function name in your code will lead to a "missing symbols"
error (with the exception of character case in Fortran source code).

Building code on the CS500 platform
-----------------------------------

Building code on the CS500 platform is different from the XC50 platform:

-   The CS500 platform does not currently use compiler drivers (these
    will be made available by Cray in the near future)
-   The CS500 module environment can be reset using `module purge`
    without problems - you will need to run `module load NeSI`
    afterwards to make the NeSI software stack available again.

Building code on the CS500 platform follows the same process as building
code on Mahuika. The only difference is that CS500 nodes use Intel
Skylake CPUs, while Mahuika's CS400 nodes use the older Intel Broadwell
CPUs. This means that programs that were compiled on the CS500 platform
may fail to run on Mahuika, producing either an error message (if built
with the Intel compiler), or an "illegal instruction" error (if built
with the Cray or GNU compilers).

Please refer to section [Building code on
Mahuika](https://support.nesi.org.nz/hc/en-gb/articles/360000329015) for
further instructions.
:::
:::
