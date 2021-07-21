::: {#append_ver}
    comsol --help

Will display a list of COMSOL batch commands.
:::

> ### Useful Links {#prerequisites}
>
> -   [Running COMSOL in parallel on
>     clusters.](https://www.comsol.com/support/knowledgebase/1001/)
> -   [Running parametric sweeps, batch sweeps, and cluster sweeps from
>     the command
>     line.](https://www.comsol.com/support/knowledgebase/1250/)
> -   [COMSOL and
>     Multithreading.](https://www.comsol.com/support/knowledgebase/1096/)

<div>

Batch Submission
================

When using COMSOL batch the following flags can be used to control
distribution. 

  ------------------------- ----------------------------------------------------------------------------------------------------------------------------------
  `-mpibootstrap slurm`      Instructs COMSOL to get it\'s settings from SLURM
  `-np <cpus>`              Number of CPUs to use in each task. Equivalent to slurm input `--cpus-per-task` or environment variable `${SLURM_CPUS_PER_TASK}`
  `-nn <tasks>`             Number of tasks total. `--ntasks` or `${SLURM_NTASKS}`
  `-nnhost <tasks>`         Number of tasks per node. `--ntasks-per-node` `${SLURM_NTASKS_PER_NODE}`
  `-f <path to hostlist>`   Host file. You wont\'t need to set this in most circumstances.
  ------------------------- ----------------------------------------------------------------------------------------------------------------------------------

 
=

Example Scripts {#example-script}
===============

</div>

------------------------------------------------------------------------

+-----------------------------------+-----------------------------------+
| Serial Example                    |     #!/bin/bash -e                |
| --------------                    |                                   |
|                                   |     #SBATCH --job-name      COMSO |
| -------------------------------   | L-serial                          |
|                                   |     #SBATCH --licenses      comso |
| Single *process* with a single    | l@uoa_foe                         |
| *thread*                          |     #SBATCH --time          00:05 |
|                                   | :00          # Walltime           |
| Usually submitted as part of an   |     #SBATCH --mem           1512  |
| array, as in the case of          |               # total mem         |
| parameter sweeps.                 |                                   |
|                                   |     module load COMSOL/5.5        |
|                                   |                                   |
|                                   |     comsol batch -inputfile my_in |
|                                   | put.mph                           |
+-----------------------------------+-----------------------------------+
| Shared Memory Example             |     #!/bin/bash -e                |
| ---------------------             |                                   |
|                                   |     #SBATCH --job-name      COMSO |
| -------------------------------   | L-shared                          |
|                                   |     #SBATCH --licenses      comso |
|                                   | l@uoa_foe                         |
|                                   |     #SBATCH --time          00:05 |
|                                   | :00        # Walltime             |
|                                   |     #SBATCH --cpus-per-task 8     |
|                                   |     #SBATCH --mem           4G    |
|                                   |            # total mem            |
|                                   |                                   |
|                                   |     module load COMSOL/5.5        |
|                                   |                                   |
|                                   |     comsol batch -mpibootstrap sl |
|                                   | urm -inputfile my_input.mph       |
+-----------------------------------+-----------------------------------+
| Distributed Memory Example        |     #!/bin/bash -e                |
| --------------------------        |                                   |
|                                   |     #SBATCH --job-name      COMSO |
| -------------------------------   | L-distributed                     |
|                                   |     #SBATCH --licenses      comso |
|                                   | l@uoa_foe                         |
|                                   |     #SBATCH --time          00:05 |
|                                   | :00            # Walltime         |
|                                   |     #SBATCH --ntasks        8     |
|                                   |                                   |
|                                   |     #SBATCH --mem-per-cpu   1500  |
|                                   |                # mem per cpu      |
|                                   |                                   |
|                                   |     module load COMSOL/5.5        |
|                                   |                                   |
|                                   |     comsolbatch -mpibootstrap slu |
|                                   | rm -inputfile my_input.mph        |
+-----------------------------------+-----------------------------------+
| Hybrid Example                    |     #!/bin/bash -e                |
| --------------                    |                                   |
|                                   |     #SBATCH --job-name         CO |
| -------------------------------   | MSOL-hybrid                       |
|                                   |     #SBATCH --licenses         co |
|                                   | msol@uoa_foe                      |
|                                   |     #SBATCH --time             00 |
|                                   | :05:00          # Walltime        |
|                                   |     #SBATCH --ntasks           4  |
|                                   |                 # total mem       |
|                                   |     #SBATCH --cpus-per-task    16 |
|                                   |     #SBATCH --mem-per-cpu      15 |
|                                   | 00B             # total mem       |
|                                   |                                   |
|                                   |     module load COMSOL/5.5        |
|                                   |                                   |
|                                   |     comsol batch -mpibootstrap sl |
|                                   | urm -inputfile my_input.mph       |
+-----------------------------------+-----------------------------------+

> ### Important
>
> If no output file is set, using `--output` the input file will be
> updated instead.

Interactive Use
===============

Providing you have [set up
X11](https://support.nesi.org.nz/hc/en-gb/articles/360001075975), you
can open the COMSOL GUI by running the command `comsol`.

Large jobs should not be run on the login node.

Recommendations
===============

COMSOL is relatively smart with it\'s use of resources, if possible it
is preferable to use `--cpus-per-task` over `--ntasks`
