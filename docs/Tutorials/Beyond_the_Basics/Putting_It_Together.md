---
created_at: 2026-10-15
description: Run the whole example pipeline from one submission script, compare its efficiency with the original job, and see when to move to a workflow manager.
status: tutorial
tags:
- tutorial
- slurm
- workflow
---

!!! time "30 Minutes"

!!! objectives
    - Run a whole pipeline, from preparation to a summary, from one submission script.
    - Compare the pipeline's resource use with the job you started with.
    - Recognise when a workflow manager would serve you better than Slurm scripts.

!!! prerequisite
    - You can run a job array and chain jobs with dependencies. See [Job Arrays](Job_Arrays.md)
      and [Splitting and Chaining Jobs](Splitting_and_Chaining_Jobs.md).

??? info "Skipped ahead? Set up here"
    <!-- Write: copy the example directory and checkpoints/06_arrays/. -->

## The finished pipeline

<!-- Write: add summarise.sl, which waits for the whole job array with afterok, and run submit.sh.
Walk through what each job does and when it starts. End state: checkpoints/07_together/. -->

## Compare with where you started

<!-- Write: complete the seff scoreboard and compare total core-hours and memory with the original pipeline.sl job.
Show the numbers from the recorded runs. -->

!!! question "Where did the savings come from?"
    <!-- Write: learners match each improvement to the lesson that made it. -->

??? question "Solution"
    <!-- Write: answer. -->

## When to use a workflow manager

<!-- Write: when submission scripts get hard to manage (many stages, reruns of only what changed, other clusters),
move to a workflow manager. Show the same pipeline as a rule graph and point to Snakemake and Nextflow. -->

<quiz>
<p class=admonition-title>Choosing a tool</p>

Which of these suggests it is time to move to a workflow manager?

- [x] You often need to rerun only the stages whose inputs changed.
- [x] Your submission script has grown to many stages, with different dependencies between them.
- [] You need to run the same command on 50 input files.
> A single job array handles that well.
</quiz>

!!! keypoints
    - A short submission script can queue a whole pipeline, with each stage sized for its own needs.
    - Measure before and after: the same work can use far fewer resources.
    - Workflow managers take over when pipelines outgrow scripts.

!!! postrequisite "What next"
    - [Snakemake](../../Software/Available_Applications/snakemake.md) and [Nextflow](../../Software/Available_Applications/Nextflow.md) on Mahuika.
    - For reference: [Job Dependencies](../../Batch_Computing/Job_Dependencies.md) and [Job Arrays](../../Batch_Computing/Job_Arrays.md).
