---
created_at: 2025-12-19
description: Guide to batch computing on REANNZ HPC
tags:
    - slurm
    - interactive
---

Batch jobs can be submitted via several methods. The most basic is a [simple Slurm job](#slurm-job-basics).
Slurm can also run [jobs arrays](Job_Arrays.md).
We also provide access to a [Globus Compute](Globus_Compute.md) endpoint which can be used to submit jobs.

The Slurm scheduler utilises [Fair Share](Fair_Share.md) to help with [job prioritisation](Job_Prioritisation.md). We also impose [general limits on the size and number of jobs](Job_Limits.md) submitted by any user.

Depending on the needs of your batch jobs, you may need to specify the partition you want the job to run on. Please see the [Hardware](Hardware.md) page for specifics about the system. If you need to use GPUs, the [Using GPUs](Using_GPUs.md) page will provide generic information to get started.

## Slurm job basics

Please see [Submitting your first job](../Tutorials/Introduction_To_HPC/Submitting_Your_First_Job.md) for a detailed tutorial with instructions and examples.
We also have a [Slurm reference sheet](../Getting_Started/Cheat_Sheets/Slurm-Reference_Sheet.md).

### Batch scripts

Jobs on the HPC are submitted in the form of a *batch script* (`.sl`) containing the code you want to run and a header of information needed by our job scheduler *Slurm*.

The following is a template batch script with both the minimum requirements and some additional best practice options included.

```sl
#!/bin/bash -e

#SBATCH --account       <projectcode>   # needed if you are in multiple projects
#SBATCH --job-name      BatchJob        # shows up in the queue
#SBATCH --time          00:01:00        # Walltime limit (minutes or HH:MM:SS)
#SBATCH --mem           512MB           # Memory in MB or GB
#SBATCH --cpus-per-task 1               # CPUs
#SBATCH --output        log/%x.%j.out   # send output to the file <job-id>.<job-name>.out

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

`sbatch` options can be given on the command line or (as in the example above) in `#SBATCH` pragmas.

You can find details on its use in the [sbatch manual](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/sbatch.html).

## Managing and reviewing your Slurm jobs

### Job Queue

The whole job queue can be seen using

```bash
squeue
```

Or you can filter to check just your jobs using

```bash
squeue --me
```

You can find details on its use in the [squeue manual](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/squeue.html).

### Completed jobs

You can check all jobs submitted by you in the past day using:

```bash
sacct
```

Or since a specified date using:

```bash
sacct -S YYYY-MM-DD
```

Each job will show as multiple lines, one line for the job and then additional lines for each job step within it.

!!! tip
    - `sacct -X` Only shows the jobs, not the job steps.
    - `sacct --state=PENDING/RUNNING/FAILED/CANCELLED/TIMEOUT` Filter jobs by state.
    - `sacct --format...` changes which fields are displayed out of the 120+ available.

You can find details on its use in the [sacct manual](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/sacct.html).

### Cancelling

`scancel <jobid>` will cancel the job described by `<jobid>`.
You can obtain the job ID by using `sacct` or `squeue`.

!!! tip
    - `scancel --me` Cancel all jobs submitted by you.
    - `scancel {[n1]..[n2]}` Cancel all jobs with an id between `[n1]` and `[n2]`.

You can find details on its use in the [scancel manual](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/scancel.html).

### Checking job efficiency

After a job has completed you can get basic usage information with `seff <job-id>`, which examines the full details about the job from `sacct` to produce a comparison of the actual resource usage against what was requested:

``` out
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

The "CPU Utilisation" represents the average utilisation over the course of the job.
The "Mem Utilisation" represents the maximum memory utilisation over the course of the job.

To get a more detailed sense of how your job uses the resources allocated over time,
you can use [Slurm Native Profiling](../Software/Profiling_and_Debugging/Slurm_Native_Profiling.md).
Add the following to your batch script before running:

``` sl
#SBATCH --profile           task
```

After the job finishes running you can get plots of the resource utilisation by running `profile_plot <jobid>`, or the raw profile data by running `profile_data <jobid>`.  Both programs have formatting options shown by their `--help` option.

