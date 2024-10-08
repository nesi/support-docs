---
created_at: '2019-01-10T02:22:09Z'
tags: 
 - Slurm
 - cheat sheet
title: 'Slurm: Reference Sheet'
description: Quick list of the most commonly used Slurm commands, flags, and environment variables.
vote_count: 10
vote_sum: 10
zendesk_article_id: 360000691716
zendesk_section_id: 360000278975
---

If you are unsure about using our job scheduler Slurm, more details can
be found on [Submitting_your_first_job](../Submitting_A_Job/index.md).

## Slurm Commands

A complete list of Slurm commands can be found [in the full documentation](https://slurm.schedmd.com/man_index.html), or by entering `man slurm` into a terminal

|           |                       |                                                                          |
| --------- | --------------------- | ------------------------------------------------------------------------ |
| `sbatch`  | `sbatch submit.sl`    | Submits the Slurm script `submit.sl`                                      |
| `squeue`  | `squeue`              | Displays entire queue.                                                   |
|           | `squeue --me`         | Displays your queued jobs.                                               |
|           | `squeue -p long`      | Displays queued jobs on the *long* partition.                             |
| `sacct`   | `sacct`               | Displays all the jobs run by you that day.                               |
|           | `sacct -S 2019-01-01` | Displays all the jobs run by you since the *1st Jan 2019*                 |
|           | `sacct -j 123456789`  | Displays job *123456789*                                                  |
| `scancel` | `scancel 123456789`   | Cancels job *123456789*                                                   |
|           | `scancel --me`        | Cancels all your jobs.                                                   |
| `sshare`  | `sshare -U`           | Shows the Fair Share scores for all projects of which *you* are a member. |
| `sinfo`   | `sinfo`               | Shows the current state of our Slurm partitions.                         |

## `sbatch` options

A complete list of `sbatch` options can be found
[in the full Slurm documentation](https://slurm.schedmd.com/sbatch.html), or by running `man sbatch`

Options can be provided on the command line or in the batch file as an
`#SBATCH` directive.  The option name and value can be separated using
an '=' sign e.g. `#SBATCH --account=nesi99999` or a space e.g.
`#SBATCH --account nesi99999`. *But not both!*

### General options

| | | |
| -- | -- | -- |
| `--job-name`   | `#SBATCH --job-name=MyJob`              | The name that will appear when using squeue or sacct.                                                           |
| `--account`    | `#SBATCH --account=nesi99999`           | The account your core hours will be 'charged' to.                                                               |
| `--time`       | `#SBATCH --time=DD-HH:MM:SS`            | Job max walltime.                                                                                               |
| `--mem`        | `#SBATCH --mem=512MB`                   | Memory required per node.                                                                                       |
| `--partition`  | `#SBATCH --partition=milan`              | Specified job[partition](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Mahuika_Slurm_Partitions.md). |
| `--output`     | `#SBATCH --output=%j_output.out`        | Path and name of standard output file.                                                                          |
| `--mail-user`  | `#SBATCH --mail-user=user123@gmail.com` | Address to send mail notifications.                                                                             |
| `--mail-type`  | `#SBATCH --mail-type=ALL`               | Will send a mail notification at `BEGIN END FAIL`.                                                            |
|                  | `#SBATCH --mail-type=TIME_LIMIT_80`     | Will send message at *80%* walltime.                                                                           |
| `--no-requeue` | `#SBATCH --no-requeue`                  | Will stop job being requeued in the case of node failure.                                                       |

### Parallel options

|                       |                                  |                                                                                                                         |
| --------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `--nodes`           | ``#SBATCH --nodes=2``            | Will request tasks be run across 2 nodes.                                                                               |
| `--ntasks`          | ``#SBATCH --ntasks=2 ``          | Will start 2 [MPI](../Submitting_A_Job/Parallel_Execution.md) tasks.                                           |
| `--ntasks-per-node` | `#SBATCH --ntasks-per-node=1` | Will start 1 task per requested node.                                                                                   |
| `--cpus-per-task`   | `#SBATCH --cpus-per-task=10`  | Will request 10 [*logical* CPUs](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Hyperthreading.md) per task. |
| `--mem-per-cpu`     | `#SBATCH --mem-per-cpu=512MB` | Memory Per *logical* CPU. `--mem`  Should be used if shared memory job. See [How do I request memory?](../../General/FAQs/How_do_I_request_memory.md) |
| --array | `#SBATCH --array=1-5` | Will submit job 5 times each with a different `$SLURM_ARRAY_TASK_ID` (1,2,3,4,5). |
| | `#SBATCH --array=0-20:5` | Will submit job 5 times each with a different `$SLURM_ARRAY_TASK_ID` (0,5,10,15,20). |
| | `#SBATCH --array=1-100%10` | Will submit 1 though to 100 jobs but no more than 10 at once. |

### Other

|    |    |    |
| -- | -- | -- |
| `--qos` | `#SBATCH --qos=debug` | Adding this line gives your job a high priority. *Limited to one job at a time, max 15 minutes*. |
| `--profile` | `#SBATCH --profile=ALL` | Allows generation of a .h5 file containing job profile information. See [Slurm Native Profiling](../../Scientific_Computing/Profiling_and_Debugging/Slurm_Native_Profiling.md) |
| `--dependency` | `#SBATCH --dependency=afterok:123456789` | Will only start after the job 123456789 has completed. |
| `--hint` | `#SBATCH --hint=nomultithread` | Disables [hyperthreading](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Hyperthreading.md), be aware that this will significantly change how your job is defined. |

!!! tip
     Many options have a short (`-`) and long (`--`) form e.g.  
     `#SBATCH --job-name=MyJob`  
     or  
     `#SBATCH -J=MyJob`.

## Tokens

These are predefined variables that can be used in sbatch directives
such as the log file name.

## Environment variables

Common examples.

|                          |                                                  |
| ------------------------ | ------------------------------------------------ |
| `$SLURM_JOB_ID`        | Useful for naming output files that won't clash. |
| `$SLURM_JOB_NAME`      | Name of the job.                                 |
| `$SLURM_ARRAY_TASK_ID` | The current index of your array job.             |
| `$SLURM_CPUS_PER_TASK` | Useful as an input for multi-threaded functions. |
| `$SLURM_NTASKS`        | Useful as an input for MPI functions.            |
| `$SLURM_SUBMIT_DIR`    | Directory where `sbatch` was called.           |

!!! tip
     In order to decrease the chance of a variable being misinterpreted you
     should use the syntax `${NAME_OF_VARIABLE}` and define in strings if
     possible. e.g.

    ```sh
    echo "Completed task ${SLURM_ARRAY_TASK_ID} / ${SLURM_ARRAY_TASK_COUNT} successfully"
    ```
