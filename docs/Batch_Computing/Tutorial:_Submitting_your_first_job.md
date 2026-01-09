---
created_at: '2019-01-07T01:10:28Z'
tags:
- slurm
- scheduler
- tutorial
description: Tutorial on how to submit your first Slurm job
---

!!! prerequisite ""
    This tutorial assumes basic familiarity with bash and the terminal.
    The first three lessons of the [Software Carpentry Unix Shell lessons](https://swcarpentry.github.io/shell-novice/) covers the information needed.

# Overview

The exercises in this tutorial should take approximately 10 minutes to complete.

## Questions

- What is a scheduler and why does a cluster need one?
- How do I launch a program to run on a compute node in the cluster?
- How do I capture the output of a program that is run on a node in the cluster?

## Objectives

- Run a simple script through the scheduler
- Use the batch system command line tools to monitor the execution of your job
- Inspect the output and error files of your jobs

# What is a job scheduler?

An HPC system might have thousands of nodes and thousands of users.
How do we decide who gets what and when?
How do we ensure that a task is run with the resources it needs?
This job is handled by a special piece of software called the scheduler.
On an HPC system, the scheduler manages which jobs run where and when.

The following illustration compares these tasks of a job scheduler to a waiter in a restaurant.
If you can relate to an instance where you had to wait for a while in a queue to get in to a popular restaurant, then you may now understand why sometimes your job do not start instantly as in your laptop.

![]()

The scheduler used in this lesson is [Slurm](https://slurm.schedmd.com/).
Although Slurm is not used everywhere, running jobs is quite similar regardless of what software is being used.
The exact syntax might change, but the concepts remain the same.

# What is a batch job?

Typically, when we enter a command into our terminal, we receive a response immediately in the same terminal.
This is what we call an *interactive session*.

This is all well for doing small tasks, but what if we want to do several things one after another without without waiting in-between?
Or what if we want to repeat a series of command again later?

This is where *batch* processing becomes useful, this is where instead of entering commands directly to the terminal we write them down in a text file or script.
Then, the script can be executed by calling it with bash.

## Writing your first batch script

Let's try this now, create and open a new file in your current directory called `example_job.sh`.
(If you prefer another text editor than `nano`, feel free to use that)

```sh
10:00:00 login01 $ nano example_job.sh
```

<!-- TODO: change this script to not require another file -->
```sh
#!/bin/bash -e

module purge
module load R
Rscript sum_matrix.r
echo "Done!"
```

!!! info "shebang"
    *shebang* or *shabang*, also referred to as *hashbang* is the character sequence consisting of the number sign (aka: hash) and exclamation mark (aka: bang): `#!` at the beginning of a script.
    It is used to describe the interpreter that will be used to run the script.
    In this case we will be using the Bash Shell, which can be found at the path `/bin/bash`.
    The job scheduler will give you an error if your script does not start with a shebang.

    We recommend using `#!/bin/bash -e` instead of plain `#!/bin/bash`, so that the failure of any command within the script will cause your job to stop immediately rather than attempting to continue on with an unexpected environment or erroneous intermediate data.

We can now run this script using

```sh
10:00:00 login01 $ bash example_job.sh
```
<!-- TODO: correct output based on update to the script -->
```sh
The following modules were not unloaded:
  (Use "module --force purge" to unload all):

  1) NeSI/zen3
Running non-MPI task
Shared Memory Running on 'login01.hpc.nesi.org.nz' with 1 CPU(s)
Summing [ 6.000000e+04 x 4.000000e+04 ] matrix, seed = '0'
 1% done...
 2% done...
...
 98% done...
 99% done...
 100% done...
(Non-MPI) Sums to -29910.135471
Done!
```

You will get the output printed to your terminal as if you had just run those commands one after another.

!!! info "Cancelling commands"
    You can kill a currently running task by pressing the keys `ctrl + c`.
    If you just want your terminal back, but want the task to continue running you can ‘background’ it by pressing `ctrl + v`.
    Note, a backgrounded task is still attached to your terminal session, and will be killed when you close the terminal (if you need to keep running a task after you log out, have a look at [tmux](https://github.com/tmux/tmux/wiki)).

## Scheduling your batch job

Up until now the scheduler has not been involved, our scripts were run directly on the login node.

First let's rename our batch script to clarify that we intend to run it though the scheduler.

```sh
mv example_job.sh example_job.sl
```

!!! info "File extensions"
    A file's extension in this case does not in any way affect how a script is read, it is just another part of the name used to remind users what type of file it is.
    Some common conventions:

    - `.sh`: **Sh**ell script
    - `.sl`: **Sl**urm script
    - `.out`: Commonly used to indicate the file contains the std**out** of some process
    - `.err`: Same as `.out` but for std**err**

In order for the job scheduler to do its job we need to provide a bit more information about our script.
This is done by specifying Slurm parameters in our batch script.
Each of these parameters must be preceded by the special token `#SBATCH` and placed after the shebang, but before the content of the rest of your script.

![]()

These parameters tell Slurm things around how the script should be run, like memory, cores and time required.

All the parameters available can be found by checking `man sbatch` or on the online [Slurm documentation](https://slurm.schedmd.com/).

| Parameter | Example | Description |
|-------------- | -------------- | -------------- |
| Job name | `#SBATCH --job-name=MyJob` | The name that will appear when using `squeue` or `sacct` |
| Account | `#SBATCH --account=nesi12345` | The account your core hours will be 'charged' to |
| Time | `#SBATCH --time=DD-HH:MM:SS` | Job max walltime |
| Memory | `#SBATCH --mem=1500M` | Memory required per node |
| Output | `#SBATCH --output=%j_output.out` | Path and name of the standard output file |
| Number of tasks | `#SBATCH --ntasks=2` | Will start 2 [MPI tasks](https://docs.nesi.org.nz/Software/Parallel_Computing/Parallel_Computing/#shared-memory-parallelisation) |
| CPUs per task | `#SBATCH --cpus-per-task` | Will request 10 CPUs per task |

!!! question "Comments"
    Comments in UNIX shell scripts (denoted by `#`) are ignored by the bash interpreter.
    Why is it that we start our Slurm parameters with `#` if it is going to be ignored?

    Solution:

    Commented lines are ignored by the bash interpreter, but they are *not* ignored by Slurm.
    The `#SBATCH` parameters are read by Slurm when we *submit* the job.
    When the job starts, the bash interpreter will ignore all lines starting with `#`.

    This is similar to the *shebang* mentioned earlier, when you run your script, the system looks at the `#!`, then uses the program at the subsequent path to interpret the script, in our case `/bin/bash` (the program `bash` found in the `bin` directory).

Note that just *requesting* these resources does not make your job run faster, nor does it necessarily mean that you will consume all of these resources.
It only means that these are made available to you.
Your job may end up using less memory, or less time, or fewer tasks or nodes, than you have requested, and it will still run.

It’s best if your requests accurately reflect your job’s requirements.
We’ll talk more about how to make sure that you’re using resources effectively in a later episode of this lesson.

Now, rather than running our script with `bash` we submit it to the scheduler using the command `sbatch` (**s**lurm **batch**).

```sh
10:00:00 login01 $ sbatch example_job.sl
```

```sh
Submitted batch job 360064
```

And that’s all we need to do to submit a job.
Our work is done – now the scheduler takes over and tries to run the job for us.

## Checking your running/pending jobs

All users have the ability to view the entire queue for the cluster by running the command `squeue`.
This will list all jobs running or waiting to run on Mahuika, which can be quite a large number.

It is often far more useful to look at the status of running or queued jobs that you submitted, and there is a shortcut to help with this: `squeue --me`.
This will return information on only the jobs that you have in the queue.

By default, `squeue` will return X columns of information, but you can request additional fields.

## Interacting with running jobs

`scancel`

## Checking on finished jobs

`sacct`

## References for Slurm commands

There are two good sources for quick references on using Slurm:

- our [Slurm Reference Sheet](../Getting_Started/Cheat_Sheets/Slurm-Reference_Sheet.md)
- the official [Slurm documentation](https://slurm.schedmd.com/) and [cheatsheet](https://slurm.schedmd.com/pdfs/summary.pdf)

# Key points

- The scheduler handles how compute resources are shared between users
- A job is just a shell script
- Request *slightly* more resources than you need
