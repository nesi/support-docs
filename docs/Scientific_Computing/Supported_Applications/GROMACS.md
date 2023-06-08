---
created_at: '2019-02-21T02:46:25Z'
hidden: false
label_names: []
position: 30
title: GROMACS
vote_count: 2
vote_sum: 2
zendesk_article_id: 360000792856
zendesk_section_id: 360000040076
---

GROMACS (the GROningen MAchine for Chemical Simulations) is a versatile
package to perform molecular dynamics, i.e. simulate the Newtonian
equations of motion for systems with hundreds to millions of particles.

It is primarily designed for biochemical molecules like proteins, lipids
and nucleic acids that have a lot of complicated bonded interactions,
but since GROMACS is extremely fast at calculating the nonbonded
interactions (that usually dominate simulations) many groups are also
using it for research on non-biological systems, e.g. polymers.

GROMACS is available to anyone at no cost under the terms of [the GNU
Lesser General Public
Licence](http://www.gnu.org/licenses/lgpl-2.1.html). Gromacs is a joint
effort, with contributions from developers around the world: users agree
to acknowledge use of GROMACS in any reports or publications of results
obtained with the Software (see

# Job submission

GROMACS performance depends on several factors, such as usage (or lack
thereof) of GPUs, the number of MPI tasks and OpenMP threads, the load
balancing algorithm, the ratio between the number of Particle-Particle
(PP) ranks and Particle-Mesh-Ewald (PME) ranks, the type of simulation
being performed, force field used and of course the simulated system.
For a complete set of GROMACS options, please refer to GROMACS
documentation.

The following job script is just an example and asks for five MPI tasks,
each of which consists of three OpenMP threads, for a total of 15
threads. Please try other `mdrun` flags in order to see if they make
your simulation run faster. Examples of such flags are `-npme`, `-dlb`,
`-ntomp`. If you use more MPI tasks per node you will have less memory
per MPI task. If you use multiple MPI tasks per node, you need to set
CRAY\_CUDA\_MPS=1 to enable the tasks to access the GPU device on each
node at the same time.

    #!/bin/bash -e

    #SBATCH --job-name      GROMACS_test # Name to appear in squeue
    #SBATCH --time          00:10:00     # Max walltime
    #SBATCH --mem-per-cpu   512MB        # Max memory per logical core
    #SBATCH --ntasks        5            # 5 MPI tasks
    #SBATCH --cpus-per-task 3            # 3 OpenMP threads per task

    module load GROMACS/5.1.4-intel-2017a

    # Prepare the binary input from precursor files 
    srun -n 1 gmx grompp -v -f minim.mdp -c protein.gro -p protein.top -o protein-EM-vacuum.tpr

    # Run the simulation
    # Note that the -deffnm option is an alternative to specifying several input files individually
    # Note also that the -ntomp option should be used when using hybrid parallelisation
    srun gmx_mpi mdrun -ntomp ${SLURM_CPUS_PER_TASK} -v -deffnm protein-EM-vacuum -c input/protein.gr -cpt 30

**Note:** To prevent performance issues we moved the serial "gmx" to
"gmx\_serial". The present "gmx" prints a note and calls "gmx\_mpi
mdrun" (if called as "gmx mdrun") and "gmx\_serial" in all other cases.

**Note:** The hybrid version with CUDA can also run on pure CPU
architectures. Thus you can use gmx\_mpi from the
GROMACS/???-cuda-???-hybrid module on Mahuika compute nodes as well as
Mahuika GPU nodes.

## Checkpointing and restarting

In the examples given above, the `-cpt 30` option instructs Gromacs to
write a full checkpoint file every 30 minutes. You can restart from a
checkpoint file using the `-cpi` flag, thus: `-cpi state.cpt`.

## Warnings regarding CPU affinity

If you run GROMACS on a node that is simultaneously running other jobs
(even other GROMACS jobs), you may see warnings like this in your
output:

> WARNING: In MPI process \#0: Affinity setting failed. This can cause
> performance degradation! If you think your setting are correct,
> contact the GROMACS developers.

One way to prevent these warnings, which is also useful for reducing the
risk of inefficient CPU usage, is to request entire nodes. On the
Mahuika cluster, this can be done using the following lines in your
input, altered as appropriate:

-   Using MPI parallelisation and hyperthreading, but no OpenMP
    parallelisation:

<!-- -->

    #SBATCH --nodes           4    # May vary
    #SBATCH --ntasks-per-node 72   # Must be 72
                                   # (the number of logical cores per node)
    #SBATCH --cpus-per-task   1    # Must be 1

-   Using MPI parallelisation with neither hyperthreading nor OpenMP
    parallelisation:

<!-- -->

    #SBATCH --nodes           4    # May vary
    #SBATCH --ntasks-per-node 36   # Must be 36
                                   # (the number of physical cores per node)
    #SBATCH --cpus-per-task   1    # Must be 1
    #SBATCH --hint=nomultithread   # Don't use hyperthreading

-   Using hybrid (OpenMP + MPI) parallelisation and hyperthreading:

<!-- -->

    #SBATCH --nodes           4    # May vary
    #SBATCH --ntasks-per-node 1    # Must be 1
    #SBATCH --cpus-per-task   72   # Must be 72
                                   # (the number of logical cores per node)

-   Using hybrid (OpenMP + MPI) parallelisation but not hyperthreading:

<!-- -->

    #SBATCH --nodes           4    # May vary
    #SBATCH --ntasks-per-node 1    # Must be 1
    #SBATCH --cpus-per-task   36   # Must be 36
                                   # (the number of physical cores per node)
    #SBATCH --hint=nomultithread   # Don't use hyperthreading

If you opt to use hybrid parallelisation, it is also important to run
`mdrun_mpi` with the `-ntomp <number>` option, where `<number>` should
be the number of CPUs per task. You can make sure the value is correct
by using `-ntomp ${SLURM_CPUS_PER_TASK}`. Hybrid parallelisation can be
more efficient than MPI-only parallelisation, as within the same node
there is no need for inter-task communication.

 

**NOTE** on using GROMACS on Māui:

On the Māui cluster, normally there is no reason to specifically request
a whole node, as all jobs are scheduled to run on one or more entire
nodes.  However, we have seen issues with slow performance and will
recommend using the \`--exclusive\` flag when running GROMACS. It may
also be advisable to request tasks or CPUs in multiples of 80, since
that is the number of vCPUs per node.

# NVIDIA GPU Container

NVIDIA has a GPU accelerated version of GROMACS in its NGC container
registry (more details about NGC
[here](https://support.nesi.org.nz/hc/en-gb/articles/360001500156-NVIDIA-GPU-Containers)).
We have pulled a version of their container and stored it at this
location (you can also pull your own version if you wish):
*/opt/nesi/containers/nvidia/gromacs-2020\_2.sif*. We have also provided
an example submission script that calls the Singularity image here:
*/opt/nesi/containers/nvidia/gromacs-example.sl*.

# Further Documentation

[GROMACS Homepage](http://www.gromacs.org/)

[GROMACS Manual](http://www.gromacs.org/Documentation/Manual)
