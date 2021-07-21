[[Hyperthreading](https://en.wikipedia.org/wiki/Hyper-threading) is
enabled on the NeSI machines, so for each physical CPU core, there are
two logical CPUs. This increases the efficiency of some multithreaded
jobs, but the fact that Slurm is counting in logical CPUs makes aspects
of running non-hyperthreaded jobs confusing, even when hyperthreading is
turned off in the job with
]{style="font-weight: 400;"}**\--hint=nomultithread.**

-   [Non-hyperthreaded jobs which use
     ]{style="font-weight: 400;"}**\--mem-per-cpu**[ requests should
    halve their memory requests as those are based on memory per logical
    CPU, not per the number of threads or tasks.  For non-MPI jobs, or
    for MPI jobs that request the same number of tasks on every node, we
    recommend to specify **\--mem** (i.e. memory per node) instead. See
    [How to request memory
    (RAM)](https://support.nesi.org.nz/hc/en-gb/articles/360001108756)
    for more information.]{style="font-weight: 400;"}
-   [Non-MPI jobs which specify
    ]{style="font-weight: 400;"}**\--cpus-per-task**[ and use
    ]{style="font-weight: 400;"}**srun** [should also set
    ]{style="font-weight: 400;"}**\--ntasks=1**[, otherwise the program
    will be run twice in parallel, halving the efficiency of the
    job.]{style="font-weight: 400;"}

[The precise rules about when hyperthreading applies are as
follows:]{style="font-weight: 400;"}

 

Mahuika

Māui

Jobs

Never share physical cores

MPI tasks within the same job

Never share physical cores

Share physical cores by default. You can override this behaviour by
using `--hint=nomultithread` in your job submission script.

Threads within the same task

Share physical cores by default. You can override this behaviour by
using\
`--hint=nomultithread` in your job submission script.

How many logical CPUs will my job use or be charged for?
--------------------------------------------------------

The possible job configurations and their results are shown in the
following table. We have also included some recommendations to help you
make the best choices, depending on the needs of your workflow.

Job configuration

Mahuika

Māui

-   Only one task
-   `--cpus-per-task` is not used

The job gets, and is charged for, two logical
CPUs. `--hint=nomultithread` is irrelevant.

The job gets one logical CPU, but is charged for 80.\
`--hint=nomultithread` is irrelevant.

[**This configuration is extremely uneconomical on Māui. Consider using
Mahuika or the Māui ancillary nodes instead.**]{.wysiwyg-color-red}

-   Only one task
-   `--cpus-per-task=`*N*
-   `--hint=nomultithread` is not used

The job gets, and is charged for, *N* logical CPUs, rounded up to the
nearest even number.

**Set *N* to an even number if possible.**

The job gets *N* logical CPUs, but is charged for 80.

**Set *N* to 80 if possible.**

-   Only one task
-   `--cpus-per-task=`*N*
-   `--hint=nomultithread` is used

The job gets, and is charged for, 2*N* logical CPUs.

The job gets 2*N* logical CPUs, but is charged for 80.

**Set *N* to 40 if possible.**

-   More than one task on one or more nodes
-   `--cpus-per-task` is not used
-   `--hint=nomultithread` is not used

Each task gets two logical CPUs. The job is charged for two logical CPUs
per task. `--hint=nomultithread` is irrelevant.

 

Each task gets one logical CPU. The job is charged for 80 logical CPUs
per allocated node.

**If possible, set the number of tasks per node to 80.**

-   More than one task on one or more nodes
-   `--cpus-per-task` is not used
-   `--hint=nomultithread` is used

Each task gets two logical CPUs. The job is charged for 80 logical CPUs
per allocated node.

**If possible, set the number of tasks per node to 40.** 

-   More than one task on one or more nodes
-   `--cpus-per-task=`*N*
-   `--hint=nomultithread` is not used

Each task gets *N* logical CPUs, rounded up to the nearest even number.
The job is charged for that number of logical CPUs per task.

**Set *N* to an even number if possible.**

Each task gets *N* logical CPUs. The job is charged for 80 logical CPUs
per allocated node.

**If possible, set *N* and the number of tasks per node such that *N* ×
(tasks per node) = 80.**

-   More than one task on one or more nodes
-   `--cpus-per-task=`*N*
-   `--hint=nomultithread` is used

Each task gets 2*N* logical CPUs. The job is charged for 2*N* logical
CPUs per task.

Each task gets 2*N* logical CPUs. The job is charged for 80 logical CPUs
per allocated node.

**If possible, set *N* and the number of tasks per node such that *N* ×
(tasks per node) = 40.**

 
