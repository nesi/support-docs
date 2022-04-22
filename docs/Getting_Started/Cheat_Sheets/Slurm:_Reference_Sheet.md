If you are unsure about using our job scheduler Slurm, more details can
be found
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000684396).

Slurm Commands
--------------

A complete list of Slurm commands can be found
[here](https://slurm.schedmd.com/man_index.html), or by entering [man
slurm]{.kbd} into a terminal

sbatch

`sbatch submit.sl`

Submits the SLURM script *submit.sl*

squeue

`squeue`

Displays entire queue.

`squeue -u usr9999`

Displays queued jobs submitted by *usr9999*.

`squeue -p long`

Displays queued jobs on the *long* partition.

sacct

`sacct`

Displays all the jobs run by you that day.

`sacct -S 2019-01-01`

Displays all the jobs run by you since the *1st Jan 2019*

`sacct -j 123456789`

Displays job *123456789*

scancel

`scancel 123456789`

Cancels job *123456789*

`scancel -u usr9999`

Cancels all your jobs (assuming you are *usr9999*). If you are not
*usr9999*, you will get an error message.

sshare

`sshare -U usr9999`

Shows the Fair Share scores for all projects of which *usr9999* is a
member.

sinfo

`sinfo`

Shows the current state of our SLURM partitions.

 

 

 

 

------------------------------------------------------------------------

 

*sbatch* options {#sVariables}
----------------

A complete list of *sbatch* options can be found
[here](https://slurm.schedmd.com/sbatch.html), or by running [man
sbatch]{.kbd}

Options can be provided on the command line or in the batch file as an
`#SBATCH` directive.  The option name and value can be separated using
an \'=\' sign e.g. `#SBATCH --account=nesi99999` or a space e.g.
`#SBATCH --account nesi99999`. *But not both!*

### General options

\--job-name

`#SBATCH --job-name=MyJob`

[The name that will appear when using squeue or sacct]{.c}

\--account

`#SBATCH --account=nesi99999`

[The account your core hours will be \'charged\' to.]{.c}

\--time

`#SBATCH --time=DD-HH:MM:SS`

[Job max walltime\
]{.c}

\--mem

`#SBATCH --mem=512MB`

Memory required per node.

\--partition

`#SBATCH --partition=long`

Specified job
[partition](https://support.nesi.org.nz/hc/en-gb/articles/360000204076-Mahuika-Slurm-Partitions).

\--output

`#SBATCH --output=%j_output.out`

Path and name of standard output file.

\--mail-user

`#SBATCH --mail-user=bob123@gmail.com`{.nohighlight}

Address to send mail notifications.

\--mail-type

`#SBATCH --mail-type=ALL`

Will send a mail notification at `BEGIN  END  FAIL`

`#SBATCH --mail-type=TIME_LIMIT_80`

Will send message at *80%* walltime

### Parallel options

+-----------------------+-----------------------+-----------------------+
| \--nodes              | `#SBATCH --nodes=2`   | Will request tasks be |
|                       |                       | run across 2 nodes.   |
+-----------------------+-----------------------+-----------------------+
| \--ntasks             | `#SBATCH --ntasks=2`  | Will start 2          |
|                       |                       | [MPI                  |
|                       |                       | ](https://support.nes |
|                       |                       | i.org.nz/knowledge/ar |
|                       |                       | ticles/360000690275/) |
|                       |                       | tasks.                |
+-----------------------+-----------------------+-----------------------+
| \--ntasks-per-node    | `#SBATCH              | Will start 1 task per |
|                       |  --ntasks-per-node=1` | requested node        |
+-----------------------+-----------------------+-----------------------+
| \--cpus-per-task      | `#SBATC               | Will request 10       |
|                       | H --cpus-per-task=10` | *logical* CPUs per    |
|                       |                       | task.                 |
|                       |                       |                       |
|                       |                       | See                   |
|                       |                       | [Hyperth              |
|                       |                       | reading](https://supp |
|                       |                       | ort.nesi.org.nz/hc/en |
|                       |                       | -gb/articles/36000056 |
|                       |                       | 8236-Hyperthreading). |
+-----------------------+-----------------------+-----------------------+
| \--mem-per-cpu        | `#SBATCH              | Memory Per *logical*  |
|                       |  --mem-per-cpu=512MB` | CPU.                  |
|                       |                       |                       |
|                       |                       | `--mem` Should be     |
|                       |                       | used if shared memory |
|                       |                       | job.                  |
|                       |                       |                       |
|                       |                       | See [How do I request |
|                       |                       | memory                |
|                       |                       | ?](https://support.ne |
|                       |                       | si.org.nz/hc/en-gb/ar |
|                       |                       | ticles/360001108756). |
+-----------------------+-----------------------+-----------------------+
| \--array              | `#SBATCH --array=1-5` | Will submit job 5     |
|                       |                       | times each with a     |
|                       |                       | different             |
|                       |                       | `                     |
|                       |                       | $SLURM_ARRAY_TASK_ID` |
|                       |                       | (1,2,3,4,5)           |
+-----------------------+-----------------------+-----------------------+
|                       | `#S                   | Will submit job 5     |
|                       | BATCH --array=0-20:5` | times each with a     |
|                       |                       | different             |
|                       |                       | `                     |
|                       |                       | $SLURM_ARRAY_TASK_ID` |
|                       |                       | (0,5,10,15,20)        |
+-----------------------+-----------------------+-----------------------+
|                       | `#SBA                 | Will submit 1 though  |
|                       | TCH --array=1-100%10` | to 100 jobs but no    |
|                       |                       | more than 10 at once. |
+-----------------------+-----------------------+-----------------------+

### Other

+-----------------------+-----------------------+-----------------------+
| \--qos                | `#SBATCH --qos=debug` | Adding this line      |
|                       |                       | gives your job a very |
|                       |                       | high priority.        |
|                       |                       | *Limited to one job   |
|                       |                       | at a time, max 15     |
|                       |                       | minutes*.             |
+-----------------------+-----------------------+-----------------------+
| \--profile            | `#                    | Allows generation of  |
|                       | SBATCH --profile=ALL` | a .h5 file containing |
|                       |                       | job profile           |
|                       |                       | information.          |
|                       |                       |                       |
|                       |                       | See [Slurm Native     |
|                       |                       | Profiling](https:/    |
|                       |                       | /support.nesi.org.nz/ |
|                       |                       | hc/en-gb/articles/360 |
|                       |                       | 000810616-How-can-I-p |
|                       |                       | rofile-a-SLURM-job-). |
+-----------------------+-----------------------+-----------------------+
| \--dependency         | `#SBATCH --dependen   | Will only start after |
|                       | cy=afterok:123456789` | the job 123456789 has |
|                       |                       | completed.            |
+-----------------------+-----------------------+-----------------------+
| \--hint               | `#SBATCH              | Disables              |
|                       | --hint=nomultithread` | [hyperth              |
|                       |                       | reading](https://supp |
|                       |                       | ort.nesi.org.nz/hc/en |
|                       |                       | -gb/articles/36000056 |
|                       |                       | 8236-Hyperthreading), |
|                       |                       | be aware that this    |
|                       |                       | will significantly    |
|                       |                       | change how your job   |
|                       |                       | is defined.           |
+-----------------------+-----------------------+-----------------------+

> ### Tip {#prerequisites}
>
> Many options have a short and long form e.g.
> `#SBATCH --job-name=MyJob` & `#SBATCH -J=MyJob`.
>
>     echo "Completed task ${SLURM_ARRAY_TASK_ID} / ${SLURM_ARRAY_TASK_COUNT} successfully"

Tokens {#tokens .highlight}
------

These are predefined variables that can be used in sbatch directives
such as the log file name.

::: {.highlight}
  -------------------- -----------------
  `%x`{.nohighlight}   Job name
  `%u`{.nohighlight}   User name.
  `%j`{.nohighlight}   Job ID 
  `%a`{.nohighlight}   Job array Index
  -------------------- -----------------
:::

Environment variables {#where-to-build}
---------------------

Common examples.

  -------------------------------------------- ----------------------------------------------------
  `$SLURM_JOB_ID`{.highlighter-rouge}          Useful for naming output files that won\'t clash.
  `$SLURM_JOB_NAME`{.highlighter-rouge}        Name of the job.
  `$SLURM_ARRAY_TASK_ID`{.highlighter-rouge}   The current index of your array job. 
  `$SLURM_CPUS_PER_TASK`{.highlighter-rouge}   Useful as an input for multi-threaded functions.
  `$SLURM_NTASKS`{.highlighter-rouge}          Useful as an input for MPI functions.
  `$SLURM_SUBMIT_DIR`{.highlighter-rouge}      Directory where `sbatch`{.nohighlight} was called.
  -------------------------------------------- ----------------------------------------------------

> ### Tip {#prerequisites}
>
> In order to decrease the chance of a variable being misinterpreted you
> should use the syntax `${NAME_OF_VARIABLE}` and define in strings if
> possible. e.g.
>
>     echo "Completed task ${SLURM_ARRAY_TASK_ID} / ${SLURM_ARRAY_TASK_COUNT} successfully"
