---
created_at: '2019-02-21T02:46:25Z'
tags: 
  -  molecular dynamics
  -  chemistry
description: How to run GROMACS on the NeSI cluster
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

GROMACS (the GROningen MAchine for Chemical Simulations) is a versatile
package to perform molecular dynamics, i.e. simulate the Newtonian
equations of motion for systems with hundreds to millions of particles.

It is primarily designed for biochemical molecules like proteins, lipids
and nucleic acids that have a lot of complicated bonded interactions,
but since GROMACS is extremely fast at calculating the nonbonded
interactions (that usually dominate simulations) many groups are also
using it for research on non-biological systems, e.g. polymers.

GROMACS is available to anyone at no cost under the terms of 
[the GNU Lesser General Public Licence](http://www.gnu.org/licenses/lgpl-2.1.html). 
Gromacs is a joint effort, with contributions from developers around the world: users agree
to acknowledge use of GROMACS in any reports or publications of results
obtained with the Software.


## Examples

=== "Serial"
    For when only one CPU is required, generally as part of
    a [job array](../../Getting_Started/Next_Steps/Parallel_Execution.md#job-arrays)

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      GROMACS-serial
    #SBATCH --time          00:05:00     # Walltime
    #SBATCH --account       nesi99991    # Your project ID
    #SBATCH --mem           1500         # How much memory.
    
    module load GROMACS/{{app.default}}
    
    # Note: In version 2021.5 and older use `gmx-serial` instead of `gmx` 
    srun gmx mdrun -s input.tpr -o trajectory.trr -c struct.gro -e energies.edr
    ```

=== "Shared Memory"
    Uses a nodes shared memory for communication.
    
    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      GROMACS-shared-mem
    #SBATCH --time          00:05:00     # Walltime
    #SBATCH --account       nesi99991    # Your project ID
    #SBATCH --cpus-per-task 8            # Will use 8 CPUs
    #SBATCH --mem           1500         # How much memory.
    
    module load GROMACS/{{app.default}}
    
    # Note: In version 2021.5 and older use `gmx-serial` instead of `gmx` 
    srun gmx mdrun -ntomp ${SLURM_CPUS_PER_TASK} -s input.tpr -o trajectory.trr -c struct.gro -e energies.edr
    ```

<!--
COMMENTING OUT BECAUSE UNTESTED
=== "GPU"
    For more information on using GPUs see [GPU use on NeSI](../Batch_Jobs/GPU_use_on_NeSI.md)
    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      GROMACS-multi-node
    #SBATCH --time          00:05:00     # Walltime
    #SBATCH --account       nesi99991    # Your project ID
    #SBATCH --gpus-per-node 1
    #SBATCH --cpus-per-task 8            # Should CPUs be given in gpu job? IDK
    #SBATCH --mem           1500         # How much memory.
    
    module load GROMACS/{{app.default}}
    # Note: In version 2021.5 and older use `gmx-serial` instead of `gmx` 
    srun gmx mdrun -ntomp ${SLURM_CPUS_PER_TASK} -s input.tpr -o trajectory.trr -c struct.gro -e energies.edr
    ```
    `

=== "Multi Node"
    Should only be used in the case you need more CPUs than available on a single node.
    
    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      GROMACS-multi-node
    #SBATCH --time          00:05:00     # Walltime
    #SBATCH --account       nesi99991    # Your project ID
    #SBATCH --nodes 2            # Will use 8 CPUs
    #SBATCH --mem           1500         # How much memory.
    
    module load GROMACS/{{app.default}}
    
    srun gmx-mpi mdrun-mpi -ntomp ${SLURM_CPUS_PER_TASK} -nomp ${SLURM_NNODES) -s input.tpr -o trajectory.trr -c struct.gro -e energies.edr
-->    ``


    
## Performance

GROMACS performance depends on several factors, such as usage (or lack
thereof) of GPUs, the number of MPI tasks and OpenMP threads, the load
balancing algorithm, the ratio between the number of Particle-Particle
(PP) ranks and Particle-Mesh-Ewald (PME) ranks, the type of simulation
being performed, force field used and of course the simulated system.
For a complete set of GROMACS options, please refer to GROMACS
documentation.

Within each GROMACS environment module we have two versions of GROMACS, 
one built with with "thread-MPI", which is really just 
multithreading, and one with real MPI which can run across multiple nodes in
a distributed job, ie: with `--ntasks` > 1. 
In `GROMACS/2025.2-foss-2023a-cuda-12.5.0-hybrid` and more
recent environment modules the two programs are named `gmx` and `gmx-mpi`.  
In our older GROMACS environment modules `gmx` was renamed to `gmx-serial`. 

Unless your problem is so large 
that it does not fit on one whole compute node you are probably best 
off not using `gmx-mpi`. The GROMACS documentation says on this:
    
> The thread-MPI library implements a subset of the MPI 1.1 specification, 
>  based on the system threading support. … Acting as a drop-in replacement 
>   for MPI, thread-MPI enables compiling and running mdrun on a single machine 
>   (i.e. not across a network) without MPI. Additionally, it not only provides 
>   a convenient way to use computers with multicore CPU(s), but thread-MPI 
>   does in some cases make mdrun run slightly faster than with MPI.

>   Thread-MPI is compatible with most mdrun features and parallelization schemes,
>   including OpenMP, GPUs; it is not compatible with MPI and multi-simulation runs.

## CUDA

GROMACS is built with CUDA support, but that is optional to use - it will run without a GPU.

### MPI

If you do elect to use `gmx-mpi`, note that hybrid parallelisation (i.e. with `--cpus-per-task` > `1`) can be
more efficient than MPI-only parallelisation.  With hybrid parallelisation, it is important to run
`mdrun_mpi` with the `-ntomp <number>` option, where `<number>` should
be the number of CPUs per task. You can make sure the value is correct
by using `-ntomp ${SLURM_CPUS_PER_TASK}`. 

## Checkpointing

The `-cpt 30` option instructs Gromacs to
write a full checkpoint file every 30 minutes.

We reccomend including this flag for long running jobs.

You can restart from a
checkpoint file using the `-cpi` flag, thus: `-cpi state.cpt`.

## Further Documentation

[GROMACS Homepage](http://www.gromacs.org/)

[GROMACS Manual](http://www.gromacs.org/Documentation/Manual)
