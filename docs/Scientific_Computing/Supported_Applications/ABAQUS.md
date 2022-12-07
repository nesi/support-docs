::: {#append_ver}
A list of commands can be found with:

    abaqus help
:::

[Hyperthreading](https://support.nesi.org.nz/hc/en-gb/articles/360000568236)
can provide significant speedup to your computations, however
hyperthreaded CPUs will use twice the number of licence tokens. It may
be worth adding  `#SBATCH --hint nomultithread` to your slurm script if
licence tokens are your main limiting factor.

<div>

</div>

<div>

> ### Tips {#prerequisites}
>
> Required ABAQUS licences can be determined by this simple and
> intuitive formula `⌊ 5 x N0.422 ⌋` where `N` is number of CPUs.

</div>

You can force ABAQUS to use a specific licence type by setting the
parameter `academic=TEACHING` or `academic=RESEARCH` in a relevant
[environment file](#env_file).

Solver Compatibility {#solvers}
====================

Not all solvers are compatible with all types of parallelisation.

  ------------------- -------------------- ------------------ --------------- ----------------
                      Element operations   Iterative solver   Direct solver   Lanczos solver
  `mp_mode=threads`   ✖                    ✔                  ✔               ✔
  `mp_mode=mpi`       ✔                    ✔                  ✖               ✖
  ------------------- -------------------- ------------------ --------------- ----------------

> ### Note {#prerequisites}
>
> If your input files were created using an older version of ABAQUS you
> will need to update them using the command,
>
>     abaqus -upgrade -job new_job_name -odb old.odb
>
> or
>
>     abaqus -upgrade -job new_job_name -inp old.inp

+-----------------------------------+-----------------------------------+
| Serial                            |     #!/bin/bash -e                |
| ------                            |                                   |
|                                   |     #SBATCH --job-name      ABAQU |
| -------------------------------   | S-Shared                          |
|                                   |     #SBATCH --time          00:05 |
| For when only one CPU is          | :00       # Walltime              |
| required, generally as part of an |     #SBATCH --cpus-per-task 1     |
| [job                              |                                   |
| array](https://support.nesi.org.n |     #SBATCH --mem           1500  |
| z/hc/en-gb/articles/360000690275- |          # total mem              |
| Parallel-Execution#t_array).      |                                   |
|                                   |     module load ABAQUS/2019       |
|                                   |                                   |
|                                   |     abaqus job="propeller_s4rs_c3 |
|                                   | d8r" verbose=2 interactive        |
+-----------------------------------+-----------------------------------+
| Shared Memory                     |     #!/bin/bash -e                |
| -------------                     |                                   |
|                                   |     #SBATCH --job-name      ABAQU |
| -------------------------------   | S-Shared                          |
|                                   |     #SBATCH --time          00:05 |
| `mp_mode=threads`                 | :00       # Walltime              |
|                                   |     #SBATCH --cpus-per-task 4     |
| Uses a nodes shared memory for    |                                   |
| communication.                    |     #SBATCH --mem           2G    |
|                                   |      # total mem                  |
| May have a small speedup compared |                                   |
| to MPI when using a low number of |     module load ABAQUS/2019       |
| CPUs, scales poorly. Needs        |                                   |
| significantly less memory than    |     abaqus job="propeller_s4rs_c3 |
| MPI.                              | d8r" verbose=2 interactive \      |
|                                   |         cpus=${SLURM_CPUS_PER_TAS |
| *Hyperthreading may be enabled if | K} mp_mode=threads                |
| using shared memory but it is not |                                   |
| recommended.*                     |                                   |
+-----------------------------------+-----------------------------------+
| UDF                               |     #!/bin/bash -e                |
| ---                               |                                   |
|                                   |     #SBATCH --job-name      ABAQU |
| -------------------------------   | S-SharedUDF                       |
|                                   |     #SBATCH --time          00:05 |
| Shared memory run with user       | :00       # Walltime              |
| defined function (fortran or C).  |     #SBATCH --cpus-per-task 4     |
|                                   |                                   |
| `user=<name_of_function>`         |     #SBATCH --mem           2G    |
|                                   |       # total mem                 |
| Function will be compiled at      |                                   |
| start of run.                     |     module load imkl              |
|                                   |     module load ABAQUS/2019       |
| *You may need to chance the       |                                   |
| function suffix if you usually    |     abaqus job="propeller_s4rs_c3 |
| compile on windows.*              | d8r" user=my_udf.f90 verbose=2 in |
|                                   | teractive \                       |
|                                   |         cpus=${SLURM_CPUS_PER_TAS |
|                                   | K} mp_mode=threads                |
+-----------------------------------+-----------------------------------+
| Distributed Memory                |     #!/bin/bash -e                |
| ------------------                |                                   |
|                                   |     #SBATCH --job-name      ABAQU |
| -------------------------------   | S-Distributed                     |
|                                   |     #SBATCH --time          00:05 |
| `mp_mode=mpi`                     | :00       # Walltime              |
|                                   |     #SBATCH --ntasks        8     |
| Multiple *processes* each with a  |                                   |
| single *thread*.                  |     #SBATCH --mem-per-cpu   1500  |
|                                   |          # Each CPU needs it's ow |
| Not limited to one node.\         | n.                                |
| Model will be segmented into      |     #SBATCH --nodes         1     |
| `-np` pieces which should be      |                                   |
| equal to `--ntasks`.              |     module load ABAQUS/2019       |
|                                   |                                   |
| Each task could be running on a   |     abaqus job="propeller_s4rs_c3 |
| different node leading to         | d8r" verbose=2 interactive \      |
| increased communication overhead\ |         cpus=${SLURM_NTASKS} mp_m |
| .Jobs can be limited to a single  | ode=mpi                           |
| node by                           |                                   |
| adding  `--nodes=1` however this  |                                   |
| will increase your time in the    |                                   |
| queue as contiguous cpu\'s are    |                                   |
| harder to schedule.               |                                   |
|                                   |                                   |
| This is the default method if     |                                   |
| `mp_mode` is left unspecified.    |                                   |
+-----------------------------------+-----------------------------------+
| GPUs                              |     #!/bin/bash -e                |
| ----                              |                                   |
|                                   |     #SBATCH --job-name      ABAQU |
| -------------------------------   | S-gpu                             |
|                                   |     #SBATCH --time          00:05 |
| The GPU nodes are limited to 16   | :00       # Walltime              |
| CPUs                              |     #SBATCH --cpus-per-task 4     |
|                                   |                                   |
| In order for the GPUs to be       |     #SBATCH --mem           4G    |
| worthwhile, you should see a      |       # total mem                 |
| speedup equivalent to 56 CPU\'s   |     #SBATCH --gpus-per-node 1     |
| per GPU used. GPU modes will      |                                   |
| generally have less memory/cpus   |     module load ABAQUS/2019       |
|                                   |     module load CUDA              |
|                                   |                                   |
|                                   |     abaqus job="propeller_s4rs_c3 |
|                                   | d8r" verbose=2 interactive \      |
|                                   |         cpus=${SLURM_CPUS_PER_TAS |
|                                   | K} gpus=${SLURM_GPUS_PER_NODE} mp |
|                                   | _mode=threads                     |
+-----------------------------------+-----------------------------------+

User Defined Functions 
=======================

User defined functions (UDFs) can be included on the command line with
the argument `user=<filename>` where `<filename>` is the C or fortran
source code.

Extra compiler options can be set in your local `abaqus_v6.env` file.

The default compile commands are for `imkl`, other compilers can be
loaded with `module load`, you may have to change the[compile
commands](https://support.nesi.org.nz/hc/en-gb/articles/360000329015) in
your local `.env` file.

Environment file {#env_file}
================

The [ABAQUS environment
file](http://media.3ds.com/support/simulia/public/v613/installation-and-licensing-guides/books/sgb/default.htm?startat=ch04s01.html) contains
a number of parameters that define how the your job will run, some of
these you may with to change.

These parameters are read, 

`../ABAQUS/SMA/site/abaqus_v6.env` Set by NeSI and cannot be changed.

`~/abaqus_v6.env` (your home directory) If exists, will be used in all
jobs submitted by you.

`<working directory>/abaqus_v6.env` If exists, will used in this job
only.

You may want to include this short snippet when making changes specific
to a job.

    # Before starting abaqus
    echo "parameter=value
    parameter=value
    parameter=value" > "abaqus_v6.env"

    # After job is finished.
    rm "abaqus_v6.env"

 

> ### Useful Links {#prerequisites}
>
> -   [Command line options for standard
>     submission.](https://www.sharcnet.ca/Software/Abaqus610/Documentation/docs/v6.10/books/usb/default.htm?startat=pt01ch03s02abx02.html)

 

![ABAQUS\_speedup\_SharedVMPI.png](https://support.nesi.org.nz/hc/article_attachments/360002123695/ABAQUS_speedup_SharedVMPI.png)

 

*Note: Hyperthreading off, testing done on small mechanical FEA model.
Results highly model dependant. Do your own tests.*
