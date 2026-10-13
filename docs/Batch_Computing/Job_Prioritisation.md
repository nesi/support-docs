---
created_at: '2018-05-17T23:35:36Z'
description: The factors that set a job's priority on Mahuika, including QoS, Fair Share, job age and job size.
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

### Fair Share

Job priority decreases whenever the project uses more core-hours than
expected, across all partitions.
This [Fair Share](Fair_Share.md)
policy means that projects that have consumed many core-hours in the
recent past compared to their expected rate of use (either by submitting
and running many jobs, or by submitting and running large jobs) will
have a lower priority, and projects with little recent activity compared
to their expected rate of use will see their waiting jobs start sooner.
Fair Share contributes up to {{ slurm_limits.priority.fairshare_points }} points to the job priority.
To see the current Fair Share score of a project, use the command `sshare`. To see recent usage, use `nn_corehour_usage`.

### Job Age

Job priority slowly rises as a pending job gets older:
{{ slurm_limits.priority.age_points_per_hour }} point per hour, for up to {{ slurm_limits.priority.age_days }} days.

### Job Size or "TRES" (Trackable RESources)

This slightly favours jobs which request a larger count of CPUs (or
memory or GPUs) as a means of countering their otherwise inherently
longer wait times.

Whole-node jobs and others with a similarly high count of cores-per-node will get a priority boost (visible in the "site factor" of `sprio`).
This is to help whole-node jobs get ahead of large distributed jobs with many tasks spread over many nodes.

### Nice Values

A nice value lowers a job's priority by that many points, so other jobs start first. Use it for jobs that are not urgent.
Set it with `sbatch --nice=<points>`, or on a pending job with `scontrol update JobId=<jobid> Nice=<points>`.
You can only lower priority this way, not raise it.

To move one of your pending jobs ahead of your others in the same partition, account and QoS, use `scontrol top <jobid>`.

### Quality of Service

A Quality of Service (QoS) adds to a job's priority and sets limits on its size and length.
Every job runs under one QoS, `normal` the default, or `debug` requested with `--qos=debug`. It adds {{ slurm_limits.debug.priority }} to the priority,
but has much smaller limits and is only for one-off tests and debugging.
See [Debug QoS](Debug_QoS.md) for when you may use it.

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
