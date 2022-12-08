<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->

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

# Solver Compatibility {#solvers}

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
| ## Serial                         |     #!/bin/bash -e                |
|                                   |                                   |
| -------------------------------   |     #SBATCH --job-name      ABAQU |
|                                   | S-Shared                          |
| For when only                     |     #SBATCH --time          00:05 |
| <dfn class="dictionary-of-numbers | :00       # Walltime              |
| ">one                             |     #SBATCH --cpus-per-task 1     |
| CPU is required</dfn>, generally  |                                   |
| as part of an [job                |     #SBATCH --mem           1500  |
| array](https://support.nesi.org.n |          # total mem              |
| z/hc/en-gb/articles/360000690275- |                                   |
| Parallel-Execution#t_array).      |     module load ABAQUS/2019       |
|                                   |                                   |
|                                   |     abaqus job="propeller_s4rs_c3 |
|                                   | d8r" verbose=2 interactive        |
+-----------------------------------+-----------------------------------+
| ## Shared Memory                  |     #!/bin/bash -e                |
|                                   |                                   |
| -------------------------------   |     #SBATCH --job-name      ABAQU |
|                                   | S-Shared                          |
| `mp_mode=threads`                 |     #SBATCH --time          00:05 |
|                                   | :00       # Walltime              |
| Uses a nodes shared memory for    |     #SBATCH --cpus-per-task 4     |
| communication.                    |                                   |
|                                   |     #SBATCH --mem           2G    |
| May have a small speedup compared |      # total mem                  |
| to MPI when using a low number of |                                   |
| CPUs, scales poorly. Needs        |     module load ABAQUS/2019       |
| significantly less memory than    |                                   |
| MPI.                              |     abaqus job="propeller_s4rs_c3 |
|                                   | d8r" verbose=2 interactive \      |
| *Hyperthreading may be enabled if |         cpus=${SLURM_CPUS_PER_TAS |
| using shared memory but it is not | K} mp_mode=threads                |
| recommended.*                     |                                   |
+-----------------------------------+-----------------------------------+
| ## UDF                            |     #!/bin/bash -e                |
|                                   |                                   |
| -------------------------------   |     #SBATCH --job-name      ABAQU |
|                                   | S-SharedUDF                       |
| Shared memory run with user       |     #SBATCH --time          00:05 |
| defined function (fortran or C).  | :00       # Walltime              |
|                                   |     #SBATCH --cpus-per-task 4     |
| `user=<name_of_function>`         |                                   |
|                                   |     #SBATCH --mem           2G    |
| Function will be compiled at      |       # total mem                 |
| start of run.                     |                                   |
|                                   |     module load imkl              |
| *You may need to chance the       |     module load ABAQUS/2019       |
| function suffix if you usually    |                                   |
| compile on windows.*              |     abaqus job="propeller_s4rs_c3 |
|                                   | d8r" user=my_udf.f90 verbose=2 in |
|                                   | teractive \                       |
|                                   |         cpus=${SLURM_CPUS_PER_TAS |
|                                   | K} mp_mode=threads                |
+-----------------------------------+-----------------------------------+
| ## Distributed Memory             |     #!/bin/bash -e                |
|                                   |                                   |
| -------------------------------   |     #SBATCH --job-name      ABAQU |
|                                   | S-Distributed                     |
| `mp_mode=mpi`                     |     #SBATCH --time          00:05 |
|                                   | :00       # Walltime              |
| Multiple *processes* each with a  |     #SBATCH --ntasks        8     |
| single *thread*.                  |                                   |
|                                   |     #SBATCH --mem-per-cpu   1500  |
| Not limited to                    |          # Each CPU needs it's ow |
| <dfn class="dictionary-of-numbers | n.                                |
| ">one                             |     #SBATCH --nodes         1     |
| node</dfn>.\                      |                                   |
| Model will be segmented into      |     module load ABAQUS/2019       |
| `-np` pieces which should be      |                                   |
| equal to `--ntasks`.              |     abaqus job="propeller_s4rs_c3 |
|                                   | d8r" verbose=2 interactive \      |
| Each task could be running on a   |         cpus=${SLURM_NTASKS} mp_m |
| different node leading to         | ode=mpi                           |
| increased communication overhead\ |                                   |
| .Jobs can be limited to a single  |                                   |
| node by                           |                                   |
| adding  `--nodes=1` however this  |                                   |
| will increase your time in the    |                                   |
| queue as contiguous cpu\'s are    |                                   |
| harder to schedule.               |                                   |
|                                   |                                   |
| This is the default method if     |                                   |
| `mp_mode` is left unspecified.    |                                   |
+-----------------------------------+-----------------------------------+
| ## GPUs                           |     #!/bin/bash -e                |
|                                   |                                   |
| -------------------------------   |     #SBATCH --job-name      ABAQU |
|                                   | S-gpu                             |
| The GPU nodes are limited to      |     #SBATCH --time          00:05 |
| <dfn class="dictionary-of-numbers | :00       # Walltime              |
| ">16                              |     #SBATCH --cpus-per-task 4     |
| CPUs</dfn>                        |                                   |
|                                   |     #SBATCH --mem           4G    |
| In order for the GPUs to be       |       # total mem                 |
| worthwhile, you should see a      |     #SBATCH --gpus-per-node 1     |
| speedup equivalent to             |                                   |
| <dfn class="dictionary-of-numbers |     module load ABAQUS/2019       |
| ">56                              |     module load CUDA              |
| CPU</dfn>\'s per GPU used. GPU    |                                   |
| modes will generally have less    |     abaqus job="propeller_s4rs_c3 |
| memory/cpus                       | d8r" verbose=2 interactive \      |
|                                   |         cpus=${SLURM_CPUS_PER_TAS |
|                                   | K} gpus=${SLURM_GPUS_PER_NODE} mp |
|                                   | _mode=threads                     |
+-----------------------------------+-----------------------------------+

# User Defined Functions 

User defined functions (UDFs) can be included on the command line with
the argument `user=<filename>` where `<filename>` is the C or fortran
source code.

Extra compiler options can be set in your local `abaqus_v6.env` file.

The default compile commands are for `imkl`, other compilers can be
loaded with `module load`, you may have to change the[compile
commands](https://support.nesi.org.nz/hc/en-gb/articles/360000329015) in
your local `.env` file.

# Environment file {#env_file}

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

 

*Note: Hyperthreading off, testing
d<dfn class="dictionary-of-numbers">one on small mechanical </dfn>FEA
model. Results highly model dependant. Do your own tests.*
