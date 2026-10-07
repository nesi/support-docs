---
created_at: 2026-10-07
description: Mahuika has a normal queue for everyday jobs and workflows, and a debug queue for short tests and debugging when you need the results straight away.
tags:
    - slurm
    - fairshare
---

Mahuika has two job queues:

- The [normal queue](#normal-queue) is for everyday jobs and workflows. Your jobs go here unless you ask for the debug queue.
- The [debug queue](#debug-queue) is for short tests and debugging when you need the results straight away.

The two queues differ in how soon a job starts, how big and long it can be, and what you may use it for.

## Normal Queue

Use the normal queue for all your regular work, including:

- production jobs, [job arrays](Job_Arrays.md) and workflows,
- tests and checks that are a routine part of your workflow, such as a short run before each calculation to check its input or measure how much memory it needs,
- any job whose results you don't need as soon as it finishes.

Jobs in the normal queue start in order of [priority](Job_Prioritisation.md), which mainly depends on your project's [Fair Share](Fair_Share.md) score and how long the job has been waiting.
For the largest job you can run and the most jobs you can queue, see [Job Limits](Job_Limits.md).

## Debug Queue

The debug queue is for short tests and debugging when you need the results straight away.
Debug jobs get a much higher priority than jobs in the normal queue, so a small debug job usually starts within a few minutes.

A debug job can use at most:

- 2 hours (120 minutes) of wall time,
- 2 nodes.

You can only have one debug job at a time.

The debug queue is for:

- testing or debugging your code or program, while it runs or as soon as it finishes, and
- deciding straight away what to do next, such as fixing your script and trying again.

It is for one-off tests, not daily use. Good uses include:

- checking that a new or changed job script, module or input file works before you submit the full job,
- re-running a small part of a failed job to find out what went wrong,
- a small, one-off scaling test to choose how many CPUs or which GPU to request.

### When Not to Use It

Do not use the debug queue:

- for normal jobs, or to make regular work start sooner,
- for tests that are a routine part of your workflow, such as a short run before every calculation to check its input or measure its memory use.
  Even if this feels like debugging, it is part of your normal workflow and does not need a higher priority.
- for jobs whose results you won't look at straight away, such as jobs that run overnight or while you are away,
- to submit debug jobs automatically, one after another, such as from a script that submits the next job when the last one finishes.

If you are not sure, ask yourself: will I use this result straight away to decide how to fix or change my work?
If not, or if the job is a normal step in your workflow, use the normal queue.
If you are still not sure, {% include "partials/support_request.html" %}.

!!! warning "Misusing the debug queue"
    We monitor how the debug queue is used.
    Using it for normal work goes against the [Acceptable Use Policy](../Policy/Acceptable_Use_Policy.md#you-agree).
    If we find this, we may remove your access to the debug queue, and your debug jobs will be rejected with:

    ```txt
    sbatch: error: Batch job submission failed: Invalid qos specification
    ```

    We will restore your access once you confirm that you will follow the Acceptable Use Policy.

### Submitting a Debug Job

The debug queue is a Slurm Quality of Service (QoS), so you request it with the `--qos` option.
Add `--qos debug` to your batch script, and set `--time` to 2 hours or less:

```sl
#!/bin/bash -e

#SBATCH --job-name      debug_test
#SBATCH --account       nesi99991
#SBATCH --qos           debug       # use the debug queue
#SBATCH --time          00:15:00    # 2 hours or less
#SBATCH --cpus-per-task 2
#SBATCH --mem           2G

module purge
module load Python/{{ applications.Python.default }}

python my_script.py
```

To test a script without editing it, give the options on the command line instead, as these override the values in the script:

```sh
sbatch --qos=debug --time=00:15:00 my_job.sl
```

You can also add `--qos=debug` to `srun` or `salloc` to debug in an [interactive session](../Interactive_Computing/Slurm_Interactive_Sessions.md).
Exit the session as soon as you are finished.

When your script works, remove the `--qos` line before you use it for your real jobs.
