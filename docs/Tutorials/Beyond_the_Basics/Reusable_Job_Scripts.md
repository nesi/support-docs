---
created_at: 2026-10-15
description: Make a Slurm batch script reusable with Slurm environment variables, script arguments and options given when you submit.
status: tutorial
tags:
- tutorial
- slurm
---

!!! time "45 Minutes"

!!! objectives
    - Use Slurm environment variables inside a job, such as the number of CPUs it was given.
    - Pass arguments to a batch script, so one script can process any sample.
    - Override the options in a script's header when you submit it.

!!! prerequisite
    - You can use variables and loops in a script. See [Loops and Variables](Loops_and_Variables.md).

??? info "Skipped ahead? Set up here"
    <!-- Write: copy the example directory and checkpoints/02_loops_variables/pipeline.sl. -->

## Slurm environment variables

<!-- Write: the variables Slurm sets, and that they exist only inside a job.
Exercise: print a few from the login node, then from a job, and compare.
Source: environment variable tables in Using_Variables.md. Keep only the variables this series uses. -->

<quiz>
<p class=admonition-title>Where Slurm variables exist</p>

You run `echo ${SLURM_CPUS_PER_TASK}` on the login node. What do you see?

- [x] An empty line.
> Slurm only sets this variable inside a job, and only when the job requests `--cpus-per-task`.
- [] The number of CPUs on the login node.
- [] The number of CPUs your last job requested.
</quiz>

## Match threads to CPUs

<!-- Write: pass ${SLURM_CPUS_PER_TASK} to every multithreaded tool (bwa-mem2 -t, and the thread options of
the other tools), so changing --cpus-per-task is enough.
Source: "Environmental variables" section of Using_Variables.md. -->

## One script for any sample

<!-- Write: move the loop body into sample.sl with the sample as $1, and submit it for one sample.
End state: checkpoints/03_reusable_scripts/. pipeline.sl now only indexes the reference genome. -->

!!! question "Process a second sample"
    <!-- Write: submit sample.sl for another sample, without editing it. -->

??? question "Solution"
    <!-- Write: sbatch sample.sl SRR2584866 -->

## Override options when you submit

<!-- Write: options on the sbatch command line override the header.
Exercise: run sample.sl with --cpus-per-task 1 and 4, then compare with seff (scoreboard). -->

<quiz>
<p class=admonition-title>Command line or header</p>

`sample.sl` has `#SBATCH --mem 2G` in its header. You submit it with `sbatch --mem 4G sample.sl SRR2584863`.
How much memory does the job get?

- [x] 4G, because options on the command line override the header.
- [] 2G, because the header is read last.
- [] 6G, because the two are added together.
</quiz>

## Variables in the header

<!-- Write: #SBATCH lines are read by Slurm, not bash, so variables in them are not expanded.
Use %x (job name) and %j (job ID) in --output instead. Link to the mainline Job Arrays page for %A and %a. -->

!!! keypoints
    - Slurm sets environment variables inside a job, such as `SLURM_CPUS_PER_TASK`.
    - Script arguments let one script process different inputs.
    - Options on the `sbatch` command line override the script's header.
    - Variables do not work in `#SBATCH` lines. Use tokens like `%x` and `%j`.

!!! postrequisite "What next"
    - Next lesson: [Debugging Failed Jobs](Debugging_Failed_Jobs.md).
    - For reference: the [Batch Computing Guide](../../Batch_Computing/Batch_Computing_Guide.md)
      and the [Slurm Reference Sheet](../../Getting_Started/Cheat_Sheets/Slurm-Reference_Sheet.md).
