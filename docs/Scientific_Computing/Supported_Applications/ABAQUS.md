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
|                                   |     #SBA                          |
| -------------------------------   | TCH --job-name      ABAQUS-Shared |
|                                   |     #SBATCH --time                |
| For when only [one CPU is         |         00:05:00       # Walltime |
| required]{.dfn                    |     #SBATC                        |
| .dictionary-of-numbers},          | H --cpus-per-task 1               |
| generally as part of an [job      |     #SBATCH --mem                 |
| array](https://support.nesi.      |         1500          # total mem |
| org.nz/hc/en-gb/articles/36000069 |                                   |
| 0275-Parallel-Execution#t_array). |     module load ABAQUS/2019       |
|                                   |                                   |
|                                   |     abaqus job="propeller_s       |
|                                   | 4rs_c3d8r" verbose=2 interactive  |
+-----------------------------------+-----------------------------------+
| Shared Memory                     |     #!/bin/bash -e                |
| -------------                     |                                   |
|                                   |     #SBA                          |
| -------------------------------   | TCH --job-name      ABAQUS-Shared |
|                                   |     #SBATCH --time                |
| `mp_mode=threads`                 |         00:05:00       # Walltime |
|                                   |     #SBATC                        |
| Uses a nodes shared memory for    | H --cpus-per-task 4               |
| communication.                    |     #SBATCH --me                  |
|                                   | m           2G        # total mem |
| May have a small speedup compared |                                   |
| to MPI when using a low number of |     module load ABAQUS/2019       |
| CPUs, scales poorly. Needs        |                                   |
| significantly less memory than    |     abaqus job="propeller_s4      |
| MPI.                              | rs_c3d8r" verbose=2 interactive \ |
|                                   |         cpus=${SLU                |
| *Hyperthreading may be enabled if | RM_CPUS_PER_TASK} mp_mode=threads |
| using shared memory but it is not |                                   |
| recommended.*                     |                                   |
+-----------------------------------+-----------------------------------+
| UDF                               |     #!/bin/bash -e                |
| ---                               |                                   |
|                                   |     #SBATCH                       |
| -------------------------------   |  --job-name      ABAQUS-SharedUDF |
|                                   |     #SBATCH --time                |
| Shared memory run with user       |         00:05:00       # Walltime |
| defined function (fortran or C).  |     #SBATC                        |
|                                   | H --cpus-per-task 4               |
| `user=<name_of_function>`         |     #SBATCH --mem                 |
|                                   |            2G         # total mem |
| Function will be compiled at      |                                   |
| start of run.                     |     module load gimkl             |
|                                   |     module load ABAQUS/2019       |
| *You may need to chance the       |                                   |
| function suffix if you usually    |     abaqus                        |
| compile on windows.*              | job="propeller_s4rs_c3d8r" user=m |
|                                   | y_udf.f90 verbose=2 interactive \ |
|                                   |         cpus=${SLU                |
|                                   | RM_CPUS_PER_TASK} mp_mode=threads |
+-----------------------------------+-----------------------------------+
| Distributed Memory                |     #!/bin/bash -e                |
| ------------------                |                                   |
|                                   |     #SBATCH --                    |
| -------------------------------   | job-name      ABAQUS-Distributed  |
|                                   |     #SBATCH --time                |
| `mp_mode=mpi`                     |         00:05:00       # Walltime |
|                                   |     #SBATC                        |
| Multiple *processes* each with a  | H --ntasks        8               |
| single *thread*.                  |                                   |
|                                   |   #SBATCH --mem-per-cpu   1500    |
| Not limited to [one node]{.dfn    |        # Each CPU needs it's own. |
| .dictionary-of-numbers}.\         |     #SBATCH --nodes         1     |
| Model will be segmented into      |                                   |
| `-np` pieces which should be      |     module load ABAQUS/2019       |
| equal to `--ntasks`.              |                                   |
|                                   |     abaqus job="propeller_s4      |
| Each task could be running on a   | rs_c3d8r" verbose=2 interactive \ |
| different node leading to         |                                   |
| increased communication overhead\ |  cpus=${SLURM_NTASKS} mp_mode=mpi |
| .Jobs can be limited to a single  |                                   |
| node by                           |                                   |
| adding  `--nodes=1`{              |                                   |
| style="font-size: 14px;"} however |                                   |
| this will increase your time in   |                                   |
| the queue as contiguous cpu\'s    |                                   |
| are harder to schedule.           |                                   |
|                                   |                                   |
| This is the default method if     |                                   |
| `mp_mode` is left unspecified.    |                                   |
+-----------------------------------+-----------------------------------+
| GPUs                              |     #!/bin/bash -e                |
| ----                              |                                   |
|                                   |     #                             |
| -------------------------------   | SBATCH --job-name      ABAQUS-gpu |
|                                   |     #SBATCH --time                |
| The GPU nodes are limited to [16  |         00:05:00       # Walltime |
| CPUs]{.dfn                        |     #SBATC                        |
| .dictionary-of-numbers}           | H --cpus-per-task 4               |
|                                   |     #SBATCH --mem                 |
| In order for the GPUs to be       |            4G         # total mem |
| worthwhile, you should see a      |     #SBATCH --gpus-per-node 1     |
| speedup equivalent to [56         |                                   |
| CPU]{.dfn                         |     module load ABAQUS/2019       |
| .dictionary-of-numbers}\'s per    |     module load CUDA              |
| GPU used. GPU modes will          |                                   |
| generally have less memory/cpus   |     abaqus job="propeller_s4      |
|                                   | rs_c3d8r" verbose=2 interactive \ |
|                                   |         cpus=                     |
|                                   | ${SLURM_CPUS_PER_TASK} gpus=${SLU |
|                                   | RM_GPUS_PER_NODE} mp_mode=threads |
+-----------------------------------+-----------------------------------+

User Defined Functions 
=======================

User defined functions (UDFs) can be included on the command line with
the argument `user=<filename>` where `<filename>` is the C or fortran
source code.

Extra compiler options can be set in your local `abaqus_v6.env` file.

The default compile commands are for `gimkl`, other compilers can be
loaded with `module load`, you may have to change the [compile
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

 

> ### Useful Links {#prerequisites}
>
> -   [Command line options for standard
>     submission.](https://www.sharcnet.ca/Software/Abaqus610/Documentation/docs/v6.10/books/usb/default.htm?startat=pt01ch03s02abx02.html)

 

![ABAQUS\_speedup\_SharedVMPI.png](https://support.nesi.org.nz/hc/article_attachments/360002123695/ABAQUS_speedup_SharedVMPI.png)

 

*Note: Hyperthreading off, testing d[one on small mechanical ]{.dfn
.dictionary-of-numbers}FEA model. Results highly model dependant. Do
your own tests.*
