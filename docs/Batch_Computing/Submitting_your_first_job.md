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

## Writing your first batch script

## Submitting your first batch script

## Checking the queue

All users have the ability to view the entire queue for the cluster by running the command `squeue`.
This will list all jobs running or waiting to run on Mahuika, which can be quite a large number.

![Example of `squeue`](../../assets/images/squeue.png)

It is often far more useful to look at the status of running or queued jobs that you submitted, and there is a shortcut to help with this: `squeue --me`.
This will return information on only the jobs that you have in the queue.

By default, `squeue` will return X columns of information, but you can request additional fields.

## Checking on previous jobs

## Useful Slurm commands

There are two good sources for quick references on using Slurm:

- our [Slurm Reference Sheet](../Getting_Started/Cheat_Sheets/Slurm-Reference_Sheet.md)
- the official [Slurm documentation](https://slurm.schedmd.com/) and [cheatsheet](https://slurm.schedmd.com/pdfs/summary.pdf)

Below is a summary of the commands you are likely to use on a regular basis while using Mahuika.

### `sbatch`

### `srun`

### `salloc`

### `squeue`

### `sacct`

### `scancel`

## Next steps

[Slurm Best Practices](SLURM-Best_Practice.md)

[Checking resource usage](Checking_resource_usage.md)
