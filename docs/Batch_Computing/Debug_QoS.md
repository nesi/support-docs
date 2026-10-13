---
created_at: 2026-10-13
description: When you may use the debug QoS for one-off tests and debugging, its limits, and how to submit a debug job.
tags:
  - slurm
---

The debug Quality of Service (QoS) is for one-off tests and debugging, when you will use the result straight away to decide what to do next.
Debug jobs get a much higher [priority](Job_Prioritisation.md#quality-of-service) than other jobs, so a small debug job usually starts within a few minutes,
but debug jobs are limited to:

- Jobs per user, queued or running: {{ slurm_limits.debug.jobs }}
- Walltime: {{ slurm_limits.debug.minutes }} minutes
- Size per job: up to {{ slurm_limits.debug.nodes }} nodes, {{ slurm_limits.debug.cores }} CPU cores,
  {{ slurm_limits.debug.memory_gb }} GB of memory and {{ slurm_limits.debug.gpus }} GPUs

Jobs use the normal QoS unless you request the debug QoS.
Use the normal QoS for all your regular work, including production jobs, [job arrays](Job_Arrays.md), workflows,
and tests that are a routine part of your workflow.
For its limits, see [Job Limits](Job_Limits.md).

## When to Use Debug QoS

Good uses include:

- checking that a new or changed job script, module or input file works before you submit the full job,
- re-running a small part of a failed job to find out what went wrong,
- a small, one-off scaling test to choose how many CPUs or which GPU to request.

## When Not to Use Debug QoS

Do not use the debug QoS:

- for regular work, or to make it start sooner,
- for tests that are a routine part of your workflow, such as a short run before every calculation to check its inputs,
  even if they feel like debugging,
- for jobs whose results you won't look at straight away, such as jobs that run overnight or while you are away,
- to submit debug jobs automatically, such as from a script that submits the next job when the last one finishes.

If you won't use the result straight away to decide how to fix or change your work, use the normal QoS.
If you are not sure, {% include "partials/support_request.html" %}.

!!! warning "Misusing the debug QoS"
    Debug jobs start ahead of other users' jobs, so using the debug QoS for regular work holds up their work.
    Under the [Acceptable Use Policy](../Policy/Acceptable_Use_Policy.md#you-agree), you agree not to misuse the REANNZ HPC Services,
    including by "doing anything that might hinder or prevent someone else from using the REANNZ HPC Services".

    We monitor how the debug QoS is used, and may remove your access to it if we find it being misused.
    Your debug jobs will then be rejected with:

    ```txt
    sbatch: error: Batch job submission failed: Invalid qos specification
    ```

    We will restore your access once you confirm that you will follow the Acceptable Use Policy.

## Submitting a Debug Job

Add `--qos debug` to your batch script, and set `--time` to {{ slurm_limits.debug.minutes }} minutes or less:

```sl
#!/bin/bash -e

#SBATCH --job-name      debug_test
#SBATCH --account       nesi99991
#SBATCH --qos           debug       # use the debug QoS
#SBATCH --time          00:15:00    # within the debug QoS limit
#SBATCH --cpus-per-task 2
#SBATCH --mem           2G

module purge
module load Python/{{ applications.Python.default }}

python my_script.py
```

To test a script without editing it, give the options on the command line, which override the script:

```sh
sbatch --qos=debug --time=00:15:00 my_job.sl
```

You can also add `--qos=debug` to `srun` or `salloc` for an [interactive session](../Interactive_Computing/Slurm_Interactive_Sessions.md).
Exit it as soon as you are finished.

When your script works, remove the `--qos` line before you use it for real jobs.
