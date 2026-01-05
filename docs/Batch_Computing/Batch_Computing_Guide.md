---
created_at: 2025-12-19
description: Guide to batch computing
tags:
    - slurm
    - ondemand
---

Batch jobs can be submitted via several methods. The most basic is a [simple Slurm job](#slurm-job-basics).
Slurm can also run [jobs arrays](Job_Arrays.md).
We also provide access to a [Globus Compute](Globus_Compute.md) endpoint which can be used to submit jobs.

The Slurm scheduler utilises [Fair Share](Fair_Share.md) to help with [job prioritisation](Job_prioritisation.md). We also impose [general limits on the size and number of jobs](Job_Limits.md) submitted by any user.

Depending on the needs of your batch jobs, you may need to specify the partition you want the job to run on. Please see the [Hardware](Hardware.md) page for specifics about the system. If you need to use GPUs, the [Using GPUs](Using_GPUs.md) page will provide generic information to get started.

## Slurm job basics

Please see [Submitting your first job](Submitting_your_first_job.md) for a detailed tutorial with instructions and examples.

### Batch scripts

Jobs on the HPC are submitted in the form of a *batch script* (`.sl`) containing the code you want to run and a header of information needed by our job scheduler *Slurm*.

The following is a template batch script with both the minimum requirements and some additional best practice options included.

```sl
#!/bin/bash -e

#SBATCH --account       <projectcode>   # needed for members of multiple projects
#SBATCH --job-name      BatchJob       # job name (shows up in the queue)
#SBATCH --time          00:01:00        # Walltime (HH:MM:SS)
#SBATCH --mem           512MB           # Memory in MB
#SBATCH --cpus-per-task 1               # CPUs
#SBATCH --output        log/%x.%j.out   # saves the output as <job-id>.<job-name>.out
#SBATCH --error         log/%x.%j.err   # saves the error output as <job-id>.<job-name>.err

# print the contents of the batch script at the top of the output file for reference
cat $0

# purge and load needed modules
module purge
module load <module-name>

<code to be run goes here>
```

### Submitting

Jobs are submitted to the scheduler using:

```bash
sbatch myjob.sl
```

You should receive an output:

```bash
Submitted batch job 1234567
```

`sbatch` can take command line arguments similar to those used in the shell script through SBATCH pragmas.

You can find more details on its use on the [Slurm Documentation](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/sbatch.html).

## Managing and reviewing your Slurm jobs

### Job Queue

All currently queued jobs can be checked using

```bash
squeue
```

You can filter to just your jobs by adding the flag

```bash
squeue -u usr1234
```

You can also filter to just your jobs using

```bash
squeue --me
```

You can find more details on its use on the [Slurm Documentation](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/squeue.html).

### Completed jobs

You can check all jobs submitted by you in the past day using:

```bash
sacct
```

Or since a specified date using:

```bash
sacct -S YYYY-MM-DD
```

Each job will show as multiple lines, one line for the parent job and then additional lines for each job step.

!!! tip
    - `sacct -X` Only show parent processes.
    - `sacct --state=PENDING/RUNNING/FAILED/CANCELLED/TIMEOUT` Filter jobs by state.

You can find more details on its use on the [Slurm Documentation](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/sacct.html).

### Cancelling

`scancel <jobid>` will cancel the job described by `<jobid>`.
You can obtain the job ID by using `sacct` or `squeue`.

!!! tip
    - `scancel -u [username]` Kill all jobs submitted by you.
    - `scancel {[n1]..[n2]}` Kill all jobs with an id between `[n1]` and `[n2]`.

You can find more details on its use on the [Slurm Documentation](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/scancel.html).

### Checking job efficiency

After a job has completed you can get the basic usage information using `nn_seff <job-id>`.
This will return an output as below:

``` bash
Cluster: hpc
Job ID: 1234567
State: FAILED
Cores: 48
Tasks: 1
Nodes: 1
Job Wall-time:     0.6%  00:00:04 of 00:12:00 time limit
CPU Utilisation:   1.0%  00:00:02 of 00:03:12 core-walltime
Mem Utilisation:   0.0%  0.00 MB of 260.00 GB
```

The CPU utilisation represents the average utilisation over the course of the job.
The Mem utilisation represents the maximum memory utilisation over the course of the job.

To get a better sense of how your job uses the resources allocated, you can use [Slurm Native Profiling](../Software/Profiling_and_Debugging/Slurm_Native_Profiling.md). Add the following to your batch script before running:

``` sl
#SBATCH --profile           task
#SBATCH --acctg-freq        30    # sampling frequency in seconds
```

After the job finishes running you can get plots of the resource utilisation by running `profile_plot <jobid>`.
