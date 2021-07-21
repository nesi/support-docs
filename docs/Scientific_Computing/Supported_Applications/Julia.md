Julia is a flexible dynamic language, appropriate for scientific and
numerical computing, with performance comparable to traditional
statically-typed languages. The Julia home page is
at <https://julialang.org/>.

Licensing requirements {#licensing}
======================

The Julia language is (mostly) licensed under the MIT licence. For more
details, including the full text of the licence and a list of
exceptions,
see <https://github.com/JuliaLang/julia/blob/master/LICENSE.md>.

Julia packages
==============

Besides the core Julia language and interpreter, a great deal of
functionality is provided by Julia packages contributed by the Julia
developers and by third parties, or you can write your own packages.
These packages are licensed separately from the main Julia software, so
different terms and conditions may apply.

Installing Julia packages
-------------------------

Julia extensions, i.e. pieces of code that add functionality, are called
*modules*, and for installation and management purposes modules are
grouped into *packages*. Each package thus consists of one or more
modules.

NeSI provides a range of packages with our centrally managed Julia
installations, however you may wish to install additional packages,
either in your home directory or, more likely, in a project directory so
your research team members can be sure of using the same version of
relevant software.

Julia provides its own package management system, which is itself a
module, the Pkg module, that is included with the base Julia
installation. You can use the Pkg module within a Julia script, or on
the Julia command line. In this documentation, we will assume you are
using the command line, but the commands are the same within a script.

1.  Load the environment module (not the same as a Julia module)
    corresponding to the version of Julia you want to use, e.g. Julia
    1.1.0:

        $ module load Julia/1.1.0

2.  Launch the Julia executable:

        # Use Julia interactively
        $ julia
        # Alternatively, use a Julia script
        $ julia script.jl

3.  If you have opened Julia interactively, you should now see a Julia
    welcome message and prompt, like the following.

                       _
           _       _ _(_)_     |  Documentation: https://docs.julialang.org
          (_)     | (_) (_)    |
           _ _   _| |_  __ _   |  Type "?" for help, "]?" for Pkg help.
          | | | | | | |/ _` |  |
          | | |_| | | | (_| |  |  Version 1.1.0 (2019-01-21)
         _/ |\__'_|_|_|\__'_|  |  Official https://julialang.org/ release
        |__/                   |

        julia>

4.  Load the Julia package manager:

        julia> using Pkg

5.  The most important variable for installing packages is called
    `DEPOT_PATH`. The depot path is a series of directories that will be
    searched, in order, for the package that you wish to install and its
    dependencies. Clear the depot path.

    > ### Warning
    >
    > It is possible for a package to be installed somewhere on
    > `DEPOT_PATH`, but not compiled. If this happens, and the package
    > is a dependency of what you\'re trying to install, Julia will try
    > to compile it in situ. This is a bad thing most of the time,
    > because you\'re unlikely to have write access to the install
    > location, so the compilation will fail. Hence why clearing the
    > depot path is important.

        julia> empty!(DEPOT_PATH)

6.  Add your preferred Julia package directory to the newly empty depot
    path.

        julia> push!(DEPOT_PATH, "/nesi/project/nesi12345/julia")

    > ### Tip
    >
    > While a conventional personal Julia package directory is
    > `/home/joe.bloggs/.julia` or similar, there is no reason for the
    > directory to be within any particular user\'s home directory, or
    > for it to be a hidden directory with a name starting with a dot.
    > For shared Julia package directories, a visible directory within a
    > project directory will probably be more useful to you and your
    > colleagues.
    >
    > In any case, for obvious reasons, you should choose a directory to
    > which you have write access.

7.  Install the desired Julia package. In this case, we are showing the
    machine-learning package Flux as an example.

        julia> Pkg.add("Flux")

    Julia should chug away for a while, downloading and compiling
    various packages into the chosen directory.

Making Julia packages available at runtime {#loading-julia-packages}
------------------------------------------

For some reason, Julia uses the `DEPOT_PATH` variable only to control
where newly obtained packages are to be installed. The directories where
existing packages are searched for are stored in a different variable,
`LOAD_PATH`.

On NeSI, the default contents of `LOAD_PATH` are as follows:

    julia> LOAD_PATH
    5-element Array{String,1}:
     "@"
     "@v#.#"
     "@stdlib"
     "/opt/nesi/mahuika/Julia/1.1.0/local/share/julia/environment/v1.1"
     "."

The first three elements are special entries, while the fourth element
is the set of centrally managed Julia packages, and the fifth is the
current working directory. As you can see, custom depot directories are
not present in `LOAD_PATH` by default.

There are several ways to add a directory to `LOAD_PATH`, but almost
certainly the easiest is to do the following in your environment:

    $ export JULIA_LOAD_PATH="/nesi/project/nesi12345/julia:${JULIA_LOAD_PATH}"

> ### Tip
>
> By prepending the directory to `JULIA_LOAD_PATH` instead of appending
> it, you ensure that your project\'s versions of Julia packages are
> used by default, in preference to whatever might be managed centrally.
> This is probably what you want to do. If you want to use the centrally
> managed versions of Julia packages first and only use your project\'s
> package if there isn\'t a centrally managed instance, you can append
> it instead:
>
>     $ export JULIA_LOAD_PATH=${JULIA_LOAD_PATH}:/nesi/project/nesi12345/julia"

> ### Tip
>
> To revert to the default load path, just unset `JULIA_LOAD_PATH`:
>
>     $ unset JULIA_LOAD_PATH
>     $ export JULIA_LOAD_PATH

Profiling Julia code
====================

In addition to the Julia Profile module (see the [official
documentation](https://docs.julialang.org/en/v1/manual/profile/)), it is
also possible to profile Julia code with [external
profilers](https://docs.julialang.org/en/v1/manual/profile/#External-Profiling-1).
On Mahuika we have installed \"-VTune\" variants of Julia, which are
built from source with support for profiling using Intel VTune. VTune is
a nice tool for profiling parallel code (e.g. code making use of
threading or MPI.jl).

In order to collect profiling data with VTune you should:

-   load a \"-VTune\" variant of Julia, for example:

        module load Julia/1.2.0-gimkl-2018b-VTune

-   load a VTune module:

        module load VTune

-   enable Julia VTune profiling by setting an environment variable:

        export ENABLE_JITPROFILING=1

-   prepend the usual command that you use to run your Julia program
    with the desired VTune command, for example to run a hotspots
    analysis:

        srun amplxe-cl -collect hotspots -- julia your_program.jl

VTune will create a result directory which contains the profiling
information. This result can be loaded using the VTune GUI, assuming you
have X11 forwarding enabled:

    amplxe-gui --path-to-open <vtune-result-directory>

 Additional information about VTune can be found in the [User
Guide](https://software.intel.com/en-us/vtune-amplifier-help).
