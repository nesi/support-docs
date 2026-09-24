---
description: 
status: tutorial
tags:
- tutorial
- perf
- profiling
---


!!! time ""

!!! objectives
    - review the resource utilisation of a previous job
    - identify areas for improvement in job efficiency

!!! info "Prerequisites"
    This tutorial assumes familiarity with Mahuika and the use of HPCs. You should be able to:
    
    - find and load software
    - write a SLURM batch script
    - submit batch jobs to SLURM
    - check on the status of queued and completed SLURM jobs

    These tasks are covered in the [Introduction to HPC tutorials](../Introduction_To_HPC/What_Is_an_HPC.md).

## Summary and Setup

This tutorial aims to give you hands on experience evaluating and improving job efficiency.
To do that, we are going to work with an example workflow from genomics, but no genomics knowledge is needed for the tutorial.
The example used here is based on materials from the [Data Carpentry Data Wrangling and Processing for Genomics](https://datacarpentry.github.io/wrangling-genomics/02-quality-control.html#bioinformatic-workflows) if you want more information.
There are 3 broad steps that need to run in this workflow:

1. Quality control
2. Alignment
3. Variant calling

To begin, we will be working with some example scripts that can be found in `/opt/nesi/examples/intermediate_hpc`.
You will want to have these files in your `nobackup` directory.
Let's make a directory to work from and copy the files in.

```bash
cd /nesi/nobackup/<project_id>/
mkdir -p intermed_hpc_<username>
cd intermed_hpc_<username>
cp -r /opt/nesi/examples/intermediate_hpc .
ls
```

## Looking at a previous job and its efficiency

The example script `01_script.sl` has already been run as a batch job and has the job ID `{{ intermediate_hpc_job_id }}`.
Let's take a look at the status of that job before we even start looking at the script and see what we can learn.

```bash
sacct -j {{ intermediate_hpc_job_id }}
```

```output
JobID           JobName    Elapsed     AveCPU     MinCPU   TotalCPU Al NT     MaxRSS      State 
------------ ---------- ---------- ---------- ---------- ---------- -- -- ---------- ---------- 
9296168      intermed-+   00:29:10                        29:56.822  8                COMPLETED 
9296168.bat+      batch   00:29:10   00:29:57   00:29:57  29:56.822  8  1   1439444K  COMPLETED 
9296168.ext+     extern   00:29:10                         00:00:00  8  1             COMPLETED
```

!!! tip "Changing what `sacct` shows you by default"
    format flags that might be helpful
    
    stick this in bash profile

The basic `sacct` tells us a little about the job: the runtime, how many CPUs were allocated, the final job state.
But this information doesn't really help us evaluate how well the job ran.
To look at the efficiency of our job, we can use the command `seff` (short for **s**lurm **eff**iciency):

```bash
seff 9296168
```

```output
Job ID: 9296168
State: COMPLETED
Cores: 4
Job Wall-time:         12%  00:29:10 of 04:00:00 time limit
Avg CPU Utilisation:   26%  00:29:57 of 01:56:40 core-walltime
Peak Mem Utilisation:  27%  1.37 GB of 5.00 GB
```

`seff` gives us a lot of the same information but with a bit more context.

!!! question "What resources would you request if resubmitting the job based only on this information?"
    
    

??? solution "Resources for next time"
    We can probably lower the memory and CPUs requested, but if we are doing so, it might be best to leave the job time alone so if the job runs a little slower it doesn't timeout.

This is a good first step, we noticed that we are requesting more resources than we need and can make some quick adjustments.
But this assumes that the resources being used are fairly stable over the script.
The CPU utilisation is just an average, so we don't know if there was a portion of the job that did use all the CPUs we allocated to the job.

## Using job profiling

SLURM has the ability to conduct 'profiling' on jobs being submitted.
This stores extra data about the resources the job uses at various times throughout the job and can let you assess your efficiency in more detail.
To enable profiling in a batch job, you need to add the following to your SLURM header:

```sl
#SBATCH --profile=task
```

Luckily for us, this was included in our script when it was run previously, so we can access this data about our job.
We can run `profile_plot {{ intermediate_hpc_job_id }}` to produce a PNG with plots of the CPU, memory and I/O utilisation over the course of our job.

![Profile plot for job ID `{{ intermediate_hpc_job_id }}`](../../assets/images/intermediate_hpc_profile_plot.png)
