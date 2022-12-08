<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->

# Description

The Intel Cluster Toolkit Compiler Edition provides Intel C/C++ and
Fortran compilers, Intel MPI & Intel MKL.

The Intel Cluster Toolkit Compiler Edition home page is at
<http://software.intel.com/en-us/intel-cluster-toolkit-compiler>.

# Available modules

## Packages with modules

  Module             NeSI Cluster
  ------------------ --------------
  intel/2017a        pan
  intel/2015a        pan
  intel/2015.02      pan
  intel/ics-2013     pan
  intel/2011-64bit   pan

# Licensing requirements

The Intel Cluster Toolkit has been made available to all NeSI users
under the terms of a commercial, closed-source licence agreement. Any
authorised user of the Pan cluster may use the Intel Cluster Toolkit at
no cost, subject to the terms of the licence. For more information,
please get in touch with [our support desk](mailto:support@nesi.org.nz).

# Usage

The Intel Cluster Toolkit contains some executables, but is not a
conventional software package. Instead, it contains compilers and
libraries. Accordingly, it is most useful when either you wish to use it
to compile a program or a library from source code, or you intend to run
a program or library that has been compiled with it. In the latter case,
the main purpose of loading the Intel Cluster Toolkit is to set up your
runtime environment appropriately.

You can use a batch submission script to compile code, in which case you
might use the compiler command (`icc`, `icpc`, `ifort`, etc.) directly,
or more likely you will use a dedicated building workflow package such
as `make` or `cmake`. Either way, the compilation will then run on a
compute node as if it were a normal job. Alternatively, you are welcome
to build and test your code on one of the build nodes, bearing in mind
that if your package is very large or has time-consuming tests, it may
not finish within the time limits set on the build nodes.

If you are not compiling a program or library, but are instead running
previously compiled code, it is normally sufficient for you to load the
Intel Cluster Toolkit\'s module. If the program or library you are
running has its own module, it is likely that the Intel module will be
loaded automatically as a required dependency, and that no further
action will be required on your part.

If you load another module, you can always check whether it has loaded
the Intel Compiler module by running

    module list

and having a look for loaded modules with names such as \"intel\" and
\"icc\".

# Example scripts

## Example script to compile code on the Pan cluster

    #!/bin/bash -e

    #SBATCH --job-name      Compilation_job
    #SBATCH --account       nesi99999
    #SBATCH --time          01:00:00
    #SBATCH --mem-per-cpu   4G
    #SBATCH --output        Compilation_job.%j.out # Include the job ID in the names
    #SBATCH --error         Compilation_job.%j.err # of the output and error files

    module load intel/2015a

    # This is a basic compiler command and does not represent the full range of
    # compilation options available.
    srun icc -o myprog.exe myprog.c

    # Perhaps you are building using a Makefile.
    srun make

## Example script to run Intel-compiled code on the Pan cluster

    #!/bin/bash -e

    #SBATCH --job-name      Execution_job
    #SBATCH --account       nesi99999
    #SBATCH --time          01:00:00
    #SBATCH --mem-per-cpu   4G
    #SBATCH --output        Execution_job.%j.out # Include the job ID in the names
    #SBATCH --error         Execution_job.%j.err # of the output and error files

    module load intel/2015a

    # This command is given for example purposes only and does not suggest that all
    # programs compiled with the Intel compilers should be invoked in this manner.
    srun myprog.exe inputfile.dat
