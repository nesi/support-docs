---
created_at: '2025-10-12T08:00:00Z'
tags: 
  -  molecular dynamics
  -  chemistry
description: How to run LAMMPS on the Mahuika cluster
---


[//]:LAMMPS.md> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]:LAMMPS.md> (APPS PAGE BOILERPLATE END)

LAMMPS is a classical molecular dynamics code with a focus on materials modeling. It's an acronym for Large-scale Atomic/Molecular Massively Parallel Simulator.

LAMMPS has potentials for solid-state materials (metals, semiconductors) and soft matter (biomolecules, polymers) and coarse-grained or mesoscopic systems. It can be used to model atoms or, more generically, as a parallel particle simulator at the atomic, meso, or continuum scale.

LAMMPS runs on single processors or in parallel using message-passing techniques and a spatial-decomposition of the simulation domain. Many of its models have versions that provide accelerated performance on CPUs and GPUs. The code is designed to be easy to modify or extend with new functionality.

LAMMPS is distributed as an open source code under the terms of the GPLv2. The main authors of LAMMPS can be contacted via email to [developers@lammps.org](mailto:developers@lammps.org).


## Examples

=== "Serial"
    For when only one CPU is required, generally as part of
    a [job array](../../Getting_Started/Next_Steps/Parallel_Execution.md#job-arrays)

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      LAMMPS-serial
    #SBATCH --time          00:05:00     # Walltime
    #SBATCH --account       nesi99991    # Your project ID
    #SBATCH --mem           1500         # How much memory.
    
    module load LAMMPS/{{app.default}}
    
    srun lmp -in lj.in -sf omp
    ```

=== "Parallel"
    When using multiple cores on one node or across multiple nodes
    
    ```sl
    #!/bin/bash -e

    #SBATCH --job-name        LAMMPS-parallel
    #SBATCH --time            00:05:00     # Walltime
    #SBATCH --account         nesi99991    # Your project ID
    #SBATCH --ntasks-per-node 12           # The number of MPI tasks
    #SBATCH --cpus-per-task   2            # The number of OpenMP threads
    #SBATCH --mem             1500         # How much memory.
    
    module load LAMMPS/{{app.default}}

    # Also need to export the number of OpenMP threads so the application knows about it
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    
    # srun handles the MPI placement based on the choices in the job script file
    srun lmp -in lj.in -sf omp -pk omp $OMP_NUM_THREADS

    ```

=== "GPU"
    For more information on using GPUs see [GPU use on NeSI](../Batch_Jobs/Using_GPUs.md)
    ```sl
    #!/bin/bash -e

    #SBATCH --job-name        LAMMPS-parallel
    #SBATCH --time            00:05:00     # Walltime
    #SBATCH --account         nesi99991    # Your project ID
    #SBATCH --ntasks-per-node 12           # The number of MPI tasks
    #SBATCH --cpus-per-task   2            # The number of OpenMP threads
    #SBATCH --gpus-per-node   1            # The number of GPUs being used
    #SBATCH --mem             1500         # How much memory.
    
    module load LAMMPS/{{app.default}}

    # Also need to export the number of OpenMP threads so the application knows about it
    export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
    
    # srun handles the MPI placement based on the choices in the job script file
    srun lmp -in lj.in -sf gpu -pk gpu 1
    ```

## Parallelisation Using OpenMP and MPI

Parallisation is used to increase the speed of a LAMMPS simulations. 
LAMMPS does this by breaking up a simulation cell into multiple tasks. 
LAMMPS has two strategies for breaking a cell of particles into multiple
tasks. 

* Domain Decomposition: In this approach, the global domain is divided 
  into many sub-domains and then each sub-domain is assigned to a processor.
* Particle Decomposition: In this approach, each atom/particle is assigned 
  a processor to calculate everything that is needed for that atom/particle. 

Both domain and particle decomposition strategies can be used together. 
Domain decomposition is accomplished by MPI, while particle decomposition
is performed by OpenMP. These methods and their consequences to the 
performance of your LAMMPS simulations can vary, so testing is key
to optimising your LAMMPS simulation. However, in general terms:

* For dense, homogeneous, well behaved system with a sufficient 
  number of atoms, so that the MPI parallelization can be at its 
  most efficient.
* In inhomogeneous systems where there could be lots of empty spaces 
  in the simulation cell, a sensible mix of MPI and OpenMP could be
  used. 

See here for more of a discussion on how MPI and OpenMP are used by 
LAMMPS and under what simulation conditions each strategy is best used
for: [MPI vs OpenMP](https://www.hpc-carpentry.org/tuning_lammps/04-lammps-bottlenecks/index.html)

## GPUs

LAMMPS is built with CUDA support, but that is optional to use - it will run without a GPU.

## Further Documentation

[LAMMPS Homepage](http://www.LAMMPS.org/)

[LAMMPS Manual](https://docs.lammps.org/Manual.html)
