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

## Looking at a previous job

The example script `???.sl` has already been run as a batch job and has the job ID `???????`.
Let's take a look at the status of that job.

```bash
sacct -j 
```
