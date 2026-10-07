---
created_at: '2018-05-17T23:35:36Z'
title: Job Prioritisation and QoS
description: The factors that set a job's priority on Mahuika, and when to use the normal QoS or the debug QoS for short tests and debugging.
tags:
 - slurm
 - account
 - fairshare
---

Each queued job has a priority score. Jobs start when sufficient
resources (CPUs, GPUs, memory, licences) are available and not already
reserved for jobs with a higher priority.

To see the priorities of your currently pending jobs you can use the
command `sprio -u $USER`.

## Factors

Priority scores are determined by a number of factors:

### Quality of Service

Mahuika has two Quality of Service (QoS) levels:

- The [normal QoS](#normal-qos) is for everyday jobs and workflows.
- The [debug QoS](#debug-qos) is for short tests and debugging when you need the results straight away.

Jobs using the debug QoS (`--qos=debug`) get 5000 added to their priority, which raises them above all jobs using the normal QoS.
The two QoS also differ in how big and long a job can be, and in what you may use them for.

### Fair Share

Job priority decreases whenever the project uses more core-hours than
expected, across all partitions.
This [Fair Share](Fair_Share.md)
policy means that projects that have consumed many core-hours in the
recent past compared to their expected rate of use (either by submitting
and running many jobs, or by submitting and running large jobs) will
have a lower priority, and projects with little recent activity compared
to their expected rate of use will see their waiting jobs start sooner.
Fair Share contributes up to 1000 points to the job priority.
To see the current Fair Share score of a project, use the command `sshare`. To see recent usage, use `nn_corehour_usage`.

### Job Age

Job priority slowly rises as a pending job gets older:
1 point per hour, for up to 3 weeks.

### Job Size or "TRES" (Trackable RESources)

This slightly favours jobs which request a larger count of CPUs (or
memory or GPUs) as a means of countering their otherwise inherently
longer wait times.

Whole-node jobs and others with a similarly high count of cores-per-node will get a priority boost (visible in the "site factor" of `sprio`).
This is to help whole-node jobs get ahead of large distributed jobs with many tasks spread over many nodes.

### Nice Values

It is possible to give a job a "nice" value which is subtracted from its
priority. You can do that with the `--nice` option of `sbatch` or the
`scontrol update` command. The command `scontrol top <jobid>` adjusts
nice values to increase the priority of one of your jobs at the expense
of any others you have in the same partition.

### Holds

Jobs with a priority of 0 are in a "held" state and will never start
without further intervention. You can hold jobs with the command
`scontrol hold <jobid>` and release them with
`scontrol release <jobid>`. Jobs can also end up in this state when
they get requeued after a node failure.

## Other Limits

Cluster and partition-specific limits can sometimes prevent jobs from
starting regardless of their priority score.
For the limits on the size and number of jobs, see [Job Limits](Job_Limits.md).

## Backfill

'Backfill' is a scheduling strategy that allows small, short jobs to run
immediately if by doing so they will not delay the expected start time
of any higher-priority jobs. Since the expected start time of pending
jobs depends upon the expected completion time of running jobs it is
important that you set reasonably accurate job time limits if backfill
is to work well.

While the kinds of jobs that can be backfilled will also get a low job
size score, it is our general experience that an ability to be
backfilled is on the whole more useful when it comes to getting work
done on Mahuika.

See the [Slurm documentation](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/sched_config.html) for more info on backfilling.

## Normal QoS

Use the normal QoS for all your regular work, including:

- production jobs, [job arrays](Job_Arrays.md) and workflows,
- tests and checks that are a routine part of your workflow, such as a short run before each calculation to check its inputs,
- any job whose results you don't need as soon as it finishes.

Jobs using the normal QoS start in order of priority, which mainly depends on your project's [Fair Share](#fair-share) score and [how long the job has been waiting](#job-age).
For the largest job you can run and the most jobs you can queue, see [Job Limits](Job_Limits.md).

## Debug QoS

The debug QoS is for short tests and debugging when you need the results straight away.
Debug jobs get a much higher [priority](#quality-of-service) than jobs using the normal QoS, so a small debug job usually starts within a few minutes.

A debug job can use at most:

- 2 hours (120 minutes) of wall time,
- 2 nodes.

You can only have one debug job at a time.

The debug QoS is for:

- testing or debugging your code or program, while it runs or as soon as it finishes, and
- deciding straight away what to do next, such as fixing your script and trying again.

It is for one-off tests, not daily use. Good uses include:

- checking that a new or changed job script, module or input file works before you submit the full job,
- re-running a small part of a failed job to find out what went wrong,
- a small, one-off scaling test to choose how many CPUs or which GPU to request.

### When Not to Use It

Do not use the debug QoS:

- for normal jobs, or to make regular work start sooner,
- for tests that are a routine part of your workflow, such as a short run before every calculation to check its inputs.
  Even though this might feel like debugging, it is part of your normal workflow and does not need a higher priority.
- for jobs whose results you won't look at straight away, such as jobs that run overnight or while you are away,
- to submit debug jobs automatically, one after another, such as from a script that submits the next job when the last one finishes.

<!-- Using the debug QoS for more than one short job counts as abuse.
This includes chaining debug jobs back to back (in a loop, with `scrontab`, with a job that submits its successor, or with `--dependency`),
cancelling a debug job near its limit and resubmitting it, holding GPUs with an idle `salloc`, or splitting a long run into debug-sized pieces.
Use the normal QoS with [checkpointing](Job_Checkpointing.md), or a [job array](Job_Arrays.md), instead. -->

If you are not sure, ask yourself: will I use this result straight away to decide how to fix or change my work?
If not, or if the job is a normal step in your workflow, use the normal QoS.
If you are still not sure, {% include "partials/support_request.html" %}.

!!! warning "Misusing the debug QoS"
    We monitor how the debug QoS is used.
    Using it for normal work goes against the [Acceptable Use Policy](../Policy/Acceptable_Use_Policy.md#you-agree).
    If we find this, we may remove your access to the debug QoS, and your debug jobs will be rejected with:

    ```txt
    sbatch: error: Batch job submission failed: Invalid qos specification
    ```

    We will restore your access once you confirm that you will follow the Acceptable Use Policy.

### Submitting a Debug Job

Request the debug QoS by adding `--qos debug` to your batch script, and set `--time` to 2 hours or less:

```sl
#!/bin/bash -e

#SBATCH --job-name      debug_test
#SBATCH --account       nesi99991
#SBATCH --qos           debug       # use the debug QoS
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
