---
created_at: 2026-10-15
description: Split a Slurm job into parts with their own resources, make each wait for the one before with --dependency, and queue a whole workflow from one script.
status: tutorial
tags:
- tutorial
- slurm
- workflow
---

!!! time "45 Minutes"

!!! objectives
    - Split a job into parts that each request only the resources they need.
    - Make a job wait for another job with `--dependency`.
    - Queue a whole workflow from one submission script.

!!! prerequisite
    - You can find why a job failed. See [Debugging Failed Jobs](Debugging_Failed_Jobs.md).
    - The profile from [Measuring Job Efficiency](Measuring_Job_Efficiency.md) is the starting point for the split.

??? info "Skipped ahead? Set up here"
    <!-- Write: copy the example directory and checkpoints/04_debugging/. -->

## Split by resource needs

<!-- Write: indexing runs once with one CPU, the per-sample work needs more. Rename pipeline.sl to prepare.sl.
Source: "Splitting tasks by resource needs" exercise in Evaluating_Job_Efficiency.md. Size each part from seff,
with the 20 to 30% headroom from the intro, and say why the alignment step still uses mostly one CPU. -->

## Read and write less

<!-- Write: keep the trimmed reads compressed and pipe bwa-mem2 into samtools sort, so the .sam and unsorted .bam
are never written. Re-profile and compare the I/O panel (scoreboard). Link Temporary Directories for scratch space. -->

## Make a job wait for another

<!-- Write: --dependency afterok, the conditions table restated, and what happens when a dependency can never be met.
Source: "Slurm Dependencies" episode of slurm-bash-workflows, corrected; Job Dependencies page. -->

<quiz>
<p class=admonition-title>Dependencies</p>

Job `1001` is running and job `1002` has failed. Which of these jobs can start once their dependency is checked?

- [x] `--dependency after:1001`
> `after` only needs job `1001` to have started.
- [] `--dependency afterok:1002`
> Job `1002` failed, so this job will never start.
- [x] `--dependency afternotok:1002`
> `afternotok` waits for the job to fail, which it has.
- [] `--dependency afterok:1001`
> Job `1001` is still running. This job waits until it finishes successfully.
</quiz>

## Queue a whole workflow

<!-- Write: submit.sh with --parsable, queueing prepare.sl then sample.sl for each sample in samples.txt.
End state: checkpoints/05_chaining/. End on the problem: one job ID per sample, which job arrays fix. -->

!!! question "Why queue every stage at once?"
    <!-- Write: what is gained by queueing the later stages straight away, rather than waiting to submit them by hand? -->

??? question "Solution"
    <!-- Write: each stage is eligible to start as soon as the one before succeeds, without you being there to
    submit it. Do not say the scheduler reserves resources for jobs that are still waiting on a dependency. -->

!!! keypoints
    - Split a job where its parts need different resources.
    - `--dependency afterok:JOB_ID` makes a job wait for another to finish successfully.
    - `sbatch --parsable` gives the job ID, so a script can queue a whole workflow.

!!! postrequisite "What next"
    - Next lesson: [Job Arrays](Job_Arrays.md).
    - For reference: [Job Dependencies](../../Batch_Computing/Job_Dependencies.md)
      and [Temporary Directories](../../Batch_Computing/Temporary_Directories.md).
