---
created_at: '2020-02-24T20:26:39Z'
hidden: false
label_names: []
position: 8
title: Configuring Dask-MPI jobs
vote_count: 2
vote_sum: 2
zendesk_article_id: 360001392636
zendesk_section_id: 360000040056
---

[Dask](https://dask.org/) is a popular Python package for parallelising
workflows. It can use a variety of parallelisation backends, including
Python multiprocessing and multithreading. A separate
[Dask-MPI](https://mpi.dask.org) package is provided for distributed
high-performance computation using the
[MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) (Message
Passing Interface) backend, which can achieve scalability across many
nodes and integrates well into an HPC environment.

Installing the Dask-MPI package and configuring jobs requires careful
consideration to work reliably and efficiently. Internally it relies on
the [mpi4py](https://github.com/mpi4py/mpi4py) package that provides an
interface to the MPI library. MPI itself is implemented by different
freely available distributions, including MPICH and OpenMPI, as well as
a variety of vendor-specific distributions, such as Intel MPI and Cray
MPI.

While some of the MPI distributions should be compatible with each
other, it is advisable to use the same MPI distribution as the host HPC
system for reliability. The Mahuika and Māui Ancil clusters use Intel
MPI.

# Using Dask-MPI on Mahuika

Dask-MPI can be readily used with the more recent Python modules
available on Mahuika that come with the mpi4py package, e.g.

    module load Python/3.9.9-gimkl-2020a

# Installing Dask-MPI with Conda on Mahuika and Māui Ancil

Load an Anaconda3 or Miniconda3 module and use the following commands to
install mpi4py with the Intel MPI distribution *before* installing the
Dask-MPI package:

    conda install -c intel mpi4py
    conda install -c conda-forge dask-mpi

If you use an environment file, add the "intel" channel at the end of
the list (so that it will not take priority over other channels) and
request mpi4py with the Intel MPI distribution as follows:

    name: myenvironment
    channels:
      - myfavouritechannel
      - intel
    dependencies:
      - mypackage
      - anotherpackage
      - intel::mpi4py
      - dask-mpi

> ### See also
>
> See the
> [Miniconda3](https://support.nesi.org.nz/hc/en-gb/articles/360001580415)
> page for more information on how to create and manage Miniconda
> environments on NeSI.

# Configuring Slurm

At runtime, Slurm will launch a number of Python processes as requested
in the [Slurm configuration
script](https://support.nesi.org.nz/hc/en-gb/articles/360000691716).
Each process is given an ID (or "rank") starting at rank 0. Dask-MPI
then assigns different roles to the different ranks:

-   Rank 0 becomes the scheduler that coordinates work and communication
-   Rank 1 becomes the worker that executes the main Python program and
    hands out workloads
-   Ranks 2 and above become additional workers that run workloads

This implies that **Dask-MPI jobs must be launched on at least 3 MPI
ranks!** Ranks 0 and 1 often perform much less work than the other
ranks, it can therefore be beneficial to use
[Hyperthreading](https://support.nesi.org.nz/hc/en-gb/articles/360000568236)
to place these two ranks onto a single physical core. Ensure that
activating hyperthreading does not slow down the worker ranks by running
a short test workload with and without hyperthreading.

In the following, two cases will be discussed:

1.  The worker ranks use little memory and they do not use
    parallelisation themselves
2.  The worker ranks use a lot of memory and/or parallelisation

Note that Slurm will place different MPI ranks on different nodes on the
HPC by default - this has the advantage of much reduced queuing times as
Slurm can use gaps in node utilisation, and this should not affect
performance, unless individual work items are very small (e.g., if a
given work item only takes a few seconds or less to run).

## Dask workers have low memory usage and no parallelisation

This case is straightforward to set up. Use the following example to run
a workload with 1 scheduler rank and 4 worker ranks. Each rank will be
given 1 GB of memory and a single (logical) core.

    #SBATCH --time=01:00:00
    #SBATCH --hint=multithread
    #SBATCH --ntasks=5
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1G

    srun python mydaskprogram.py

## Dask workers have high memory usage and/or parallelisation

This case is more complex to set up and uses Slurm "job packs" to handle
the heterogeneous configuration. In the following example, the scheduler
and first worker rank will be given 1 GB of memory and a single
(logical) core each, while the remaining worker ranks will be given 4\*3
GB = 12 GB of memory and 4 (logical) cores per rank.

    #SBATCH --time=01:00:00
    #SBATCH --hint=multithread
    #SBATCH --ntasks=2 --mem-per-cpu=1G --cpus-per-task=1 --partition=<Slurm partition>
    #SBATCH packjob
    #SBATCH --ntasks=3 --mem-per-cpu=3G --cpus-per-task=4 --partition=<Slurm partition>

    srun --pack-group=0-1 python mydaskprogram.py

The "--pack-group" flag asks "srun" to launch both job packs together.

# Example

The following example illustrates how to run Dask-MPI on the HPC. It is
based on the Dask Futures tutorial on the [Dask
examples](https://examples.dask.org) webpage.

## Python program

    import os
    import dask_mpi as dm
    import dask.distributed as dd

    # Initialise Dask cluster and store worker files in current work directory
    dm.initialize(local_directory=os.getcwd())

    # Define two simple test functions
    def inc(x):
     return x + 1

    def add(x, y):
     return x + y

    client = dd.Client()

    # Submit chain of computations using futures
    a = client.submit(inc, 1)
    b = client.submit(inc, 2)
    c = client.submit(add, a, b)

    # Expect the same answer
    print("Dask result:", c.result())
    print("Local result:", add(inc(1), inc(2)))

## Slurm script

Replace "&lt;project ID&gt;" with your project ID number and use the
"sbatch" command to submit this Slurm script and run the test code on 3
MPI ranks:

    #!/bin/bash
    #SBATCH --time=00:01:00
    #SBATCH --hint=multithread
    #SBATCH --ntasks=3
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=512M

    module purge
    module load Python/3.9.9-gimkl-2020a

    srun python dask_example.py

The Slurm output file should contain some status information from
Dask-MPI, along with program output

    Dask result: 5
    Local result: 5

# Running Dask-MPI inside a Singularity container

It is straightforward to run a Dask-MPI workload inside a Singularity
container on the HPC. For reliable and efficient execution it is best to
use the same MPI distribution inside and outside the container. This
restricts choices to Intel MPI on the Mahuika and Māui Ancil clusters;
see section [Installing Dask-MPI with
Conda](#h_3e6b313b-a712-4e88-8246-5550cac1d77c) above for instructions.
It will also reduce container portability between platforms that use
different MPI distributions.

## Container configuration

While it is impossible to cover every possible scenario, the following
guidelines should help with configuring the container correctly.

1.  Make sure that the Intel MPI version of the "mpi4py" package is
    installed with Dask-MPI
2.  The correct version of Python and the Intel MPI distribution need to
    be loaded at runtime. This can be achieved by, e.g., adding the
    following command to the "%runscript" section in the Singularity
    build recipe if a Conda environment is used:

<!-- -->

    %runscript
     exec /bin/bash -c \
      ". /opt/conda/etc/profile.d/conda.sh; conda activate myenv; python $@"

## Slurm configuration

Slurm configuration is identical to the case without Singularity, see
section [Configuring Slurm](#h_75b008cc-7843-40b2-bdb4-8252ca807fab)
above. The run script needs to be slightly modified to setup and launch
the container runtime environment. In the first case with low worker
memory consumption and no parallelisation, use, e.g.,

    module load Singularity
    srun singularity run mycontainer.sif "<arguments>"

In the second case with high worker memory consumption and/or
parallelisation, use, e.g.,

    module load Singularity
    srun --pack-group=0-1 singularity run mycontainer.sif "<arguments>"
