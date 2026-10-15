---
created_at: 2026-10-15
description: Measure how a Slurm job used its CPUs and memory with sacct, seff, profiling and job steps, to find where it wastes resources.
status: tutorial
tags:
- tutorial
- profiling
- slurm
---

!!! time "45 Minutes"

!!! objectives
    - Compare the resources a job requested with what it used, using `sacct` and `seff`.
    - Profile a job to see how its CPU, memory and I/O use change over time.
    - Run commands as job steps, to measure each part of a job separately.

!!! prerequisite
    - You can write and submit a batch script, and check on it with `squeue` and `sacct`.
      These are covered in the [Introduction to HPC](../Introduction_To_HPC/What_Is_an_HPC.md) tutorials.

<!-- Write: introduce the series. One genomics pipeline (no genomics knowledge needed) is improved
lesson by lesson, from one long job to a job array. Keep a scoreboard of `seff` results at the end of each lesson. -->

## Set up

<!-- Write: copy the example directory to nobackup and cd into it. Use nesi99991 and username, not <...>.
Source: setup box in Evaluating_Job_Efficiency.md. Mention that pipeline.sl has already been run
(job {{ intermediate_hpc_job_id_01 }}), and that learners can submit their own copy now to compare later. -->

## Check a finished job

<!-- Write: sacct with an explicit --format (so learners see the same columns as the page), then `seff`.
Restate what each line of `seff` means: this lesson must stand alone.
Source: "sacct" and "seff" sections of Evaluating_Job_Efficiency.md. -->

!!! question "What would you request next time?"
    <!-- Write: based only on the `seff` output. -->

??? question "Solution"
    <!-- Write: fewer CPUs and less memory, keep the time limit for now. -->

<quiz>
<p class=admonition-title>Reading <code>seff</code></p>

`seff` reports `Avg CPU Utilisation: 26%` for a job that requested 4 CPUs. What does that mean?

- [x] On average, the job kept about one of its four CPUs busy.
- [] Each CPU was busy for 26% of the job, so the job needed all four.
> Not necessarily: an average can hide a short burst that used all four CPUs, or long stretches using one.
- [] The job ran for 26% of its time limit.
> That is the `Job Wall-time` line.
</quiz>

## See resource use over time

<!-- Write: --profile task, profile_plot, and how to read the CPU, memory and I/O panels.
Source: "Job profiling" section of Evaluating_Job_Efficiency.md and intermediate_hpc_profile_plot_01.png.
Give the plot alt text that describes what it shows. -->

!!! question "What stands out?"
    <!-- Write: learners look at the plot before reading on. -->

??? question "Solution"
    <!-- Write: phases with different needs, mostly about 1 CPU in use, heavy I/O. -->

## Run commands as job steps

<!-- Write: put srun in front of each command in pipeline.sl and resubmit.
Each step gets its own line in sacct and its own colour in profile_plot.
Source: intermediate_hpc_profile_plot_02.png (step-split run). End state: checkpoints/01_measuring/pipeline.sl. -->

<quiz>
<p class=admonition-title>Job steps</p>

Inside a batch script, what does putting `srun` in front of a command do?

- [x] Runs the command as a job step, which `sacct` and `profile_plot` report separately.
- [] Submits the command as a new job, which waits in the queue.
> That is what `sbatch` does. Inside a job, `srun` uses the job's own resources.
- [] Runs the command on the login node.
</quiz>

## What the profile tells us

<!-- Write: summarise the findings that the rest of the series fixes:
the alignment phase mostly uses one CPU, the same work repeats for each sample, and the script is hard to read.
Record the first row of the `seff` scoreboard. -->

!!! keypoints
    - `sacct` and `seff` compare what a job requested with what it used, but only as totals and averages.
    - Profiling shows how use changes over time, and job steps split it by command.
    - Different parts of a job can need different resources.

!!! postrequisite "What next"
    - Next lesson: [Loops and Variables](Loops_and_Variables.md).
    - For reference: [checking job efficiency](../../Batch_Computing/Batch_Computing_Guide.md#checking-job-efficiency)
      and [Slurm Native Profiling](../../Software/Profiling_and_Debugging/Slurm_Native_Profiling.md).
