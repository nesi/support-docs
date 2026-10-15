---
description: 
status: tutorial
tags:
- tutorial
- slurm
---

!!! time "wibbly wobbly timey wimey" <!--TODO-->

!!! objectives
    - Convert a SLURM job script into a SLURM job array script

!!! info "Prerequisites"
    This tutorial assumes familiarity with Mahuika and the use of HPCs. You should be able to:
    
    - use the terminal to navigate a filesystem
    - find and load software
    - write a SLURM batch script
    - submit batch jobs to SLURM
    - check on the status of queued and completed SLURM jobs

    These tasks are covered in the [Introduction to HPC tutorials](../Introduction_To_HPC/What_Is_an_HPC.md).

## Summary and Setup

This tutorial aims to give you hands on experience using variables in SLURM job scripts. To do that, we are going to work with an example script from genomics, but no genomics knowledge is needed for the tutorial. The example used here is based on materials from the [Data Carpentry Data Wrangling and Processing for Genomics](https://datacarpentry.github.io/wrangling-genomics/02-quality-control.html#bioinformatic-workflows) if you want more information.

You don't need to have completed the [Evaluating Job Efficiency tutorial](../Beyond_the_Basics/Evaluating_Job_Efficiency.md) but we will be working with one of the scripts set up at the end of that tutorial. If you haven't already, please follow the setup instructions in the box below to get all the files needed to run the scripts in this tutorial.

??? note "Setup instructions"
    We will be working with some example scripts that can be found in `/opt/nesi/examples/intermediate_hpc`.
    You will want to have these files in your `nobackup` directory.
    Let's make a directory to work from and copy the files in.

    ```bash
    cd /nesi/nobackup/<project_id>/
    mkdir -p tutorial_<username>
    cd tutorial_<username>
    cp -r /opt/nesi/examples/tutorials/job_scripting .
    ```


<!-- combine the fastq/trimmomatic and alignment/variant calling for loops into job arrays (one or two, not really sure which is better here) -->

<!-- discuss need to not submit a job array with buttloads of very short jobs! -->
