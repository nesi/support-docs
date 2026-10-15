---
created_at: 2026-10-15
description: Find out why a Slurm job failed from its state, exit code and error output, and test a fix quickly.
status: tutorial
tags:
- tutorial
- slurm
---

!!! time "45 Minutes"

!!! objectives
    - Find why a job failed, using its state, exit code and output files.
    - Tell apart a script error, running out of memory, and running out of time.
    - Test a fix quickly, without wasting resources or misusing the debug QoS.

!!! prerequisite
    - You can pass arguments to a batch script and override its options when you submit.
      See [Reusable Job Scripts](Reusable_Job_Scripts.md).

??? info "Skipped ahead? Set up here"
    <!-- Write: copy the example directory and checkpoints/03_reusable_scripts/. -->

## Where to look

<!-- Write: the .out and .err files (where --output and --error put them), then sacct with State and ExitCode.
What the exit code means, and why #!/bin/bash -e matters for it. -->

## Common failures

<!-- Write: learners cause each failure themselves from the command line, then diagnose it.
Commands are in the README of the example files:
- a sample name that does not exist (FAILED, the message in .err)
- --mem far too small (OUT_OF_MEMORY)
- --time far too short (TIMEOUT)
- no log/ directory (no output files at all)
End state: checkpoints/04_debugging/sample.sl, which checks its inputs and gives a clear message. -->

!!! question "Diagnose the failure"
    <!-- Write: show sacct and .err output for one failure and ask what went wrong and how to fix it. -->

??? question "Solution"
    <!-- Write: answer. -->

<quiz>
<p class=admonition-title>Job states</p>

`sacct` shows your job's state as `OUT_OF_MEMORY`. What should you change?

- [x] Request more memory with `--mem`, using `seff` from the failed job as a guide.
- [] Request more time with `--time`.
> That fixes `TIMEOUT`.
- [] Request more CPUs with `--cpus-per-task`.
> More CPUs do not give a job more memory when it requests a fixed amount with `--mem`.
</quiz>

## Test a fix

<!-- Write: test with a small input and short time first. One-off test jobs can use the debug QoS
(max {{ slurm_limits.debug.minutes }} minutes), but not as a regular part of a workflow: follow the Debug QoS page.
For trying commands interactively, use an interactive session. -->

!!! keypoints
    - A job's output files, state and exit code together usually show why it failed.
    - `OUT_OF_MEMORY` and `TIMEOUT` mean the job needs more memory or time, not a change to the script.
    - Check inputs at the start of a script, so it fails early with a clear message.
    - Test fixes on a small input. Only use the debug QoS for one-off tests.

!!! postrequisite "What next"
    - Next lesson: [Splitting and Chaining Jobs](Splitting_and_Chaining_Jobs.md).
    - For reference: [Debug QoS](../../Batch_Computing/Debug_QoS.md)
      and [Slurm Interactive Sessions](../../Interactive_Computing/Slurm_Interactive_Sessions.md).
