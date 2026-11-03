---
created_at: 2026-10-15
description: Find out why a Slurm job failed from its state, exit code and error output, and test a fix quickly.
status: tutorial
tags:
- tutorial
- slurm
---

!!! time "placeholder"

!!! objectives
    - Find why a job failed, using its state, exit code and output files.
    - Tell apart a script error, running out of memory, and running out of time.
    - Test a fix quickly, without wasting resources or misusing the debug QoS.

!!! prerequisite
      See [Using Variables](Using_Variables.md).


## Where to look

The first is `sacct`, which shows how the job ended:

```sh
sacct -j JOB_ID --format JobID,JobName,State,ExitCode,Elapsed
```

Replace `JOB_ID` with the job ID that `sbatch` printed.

- `State` says how the job ended: `COMPLETED`, `FAILED`, `OUT_OF_MEMORY`, `TIMEOUT` and so on.
- `ExitCode` is the exit code of the script, then the signal that stopped it. `1:0` means the script exited with an error.

The second is the job's output. Since [Using Variables](Using_Variables.md#output-files), `pipeline.sl` writes it to `log/`,
named after the job name and job ID, with error messages in the same file.
Because of the `-e` in `#!/bin/bash -e`, the script stops at the first command that fails,
so the message that explains the failure is usually near the end:

```sh
tail log/pipeline_JOB_ID.out
```

!!! info "The message about `NeSI/zen3`"
    Every output file starts with a message that the module `NeSI/zen3` was not unloaded.
    It comes from `module purge`, and is not an error.

## Common failures

Start with the failed run of `pipeline.sl`. `sacct` shows it as `FAILED`, and the end of its output says:

```txt
gzip: trimed/SRR2584863_2.trim.fastq.gz: No such file or directory
```

!!! question "Find the mistake"
    Which script, and which line, made `gunzip` look for that file?

??? question "Solution"
    The path says `trimed`, not `trimmed`. `gunzip` was run by `align.sh`, which sets the path in the variable `fq2`:

    ```bash
    fq2=trimed/${base}_2.trim.fastq
    ```

    Because the path is set once, in a variable, there is only one place to fix it.
    `set -u` didn't catch this: `fq2` was set, just to the wrong value.


## Test a fix

Once you have a fix, test it before running everything again:

- Test on the smallest input that shows the problem, such as one sample instead of all of them.
- For a one-off test, the [debug QoS](../../Batch_Computing/Debug_QoS.md) gives a short job high priority,
  so it usually starts within a few minutes. Debug jobs are limited to {{ slurm_limits.debug.minutes }} minutes:

    ```sh
    sbatch --qos=debug --time=00:15:00 pipeline.sl
    ```

    The options on the command line override the ones in the script, as in [Using Variables](Using_Variables.md).

    Only use it for one-off tests, never as a regular part of a workflow.
- To try commands one at a time on a compute node, use an [interactive session](../../Interactive_Computing/Slurm_Interactive_Sessions.md).

!!! keypoints
    - A job's output files, state and exit code together usually show why it failed.
    - `OUT_OF_MEMORY` and `TIMEOUT` mean the job needs more memory or time, not a change to the script.
    - Check inputs at the start of a script, so it fails early with a clear message.
    - Test fixes on a small input. Only use the debug QoS for one-off tests.

!!! postrequisite "What next"
    - Next lesson: [Job Dependencies](Job_Dependencies.md).
    - For reference: [Debug QoS](../../Batch_Computing/Debug_QoS.md)
      and [Slurm Interactive Sessions](../../Interactive_Computing/Slurm_Interactive_Sessions.md).
