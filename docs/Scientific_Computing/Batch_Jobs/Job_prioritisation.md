---
created_at: '2018-05-17T23:35:36Z'
description: What factors are used to determine a jobs prioroty.
tags: 
 - Slurm
 - accounting
 - Fair Share
---

Each queued job has a priority score. Jobs start when sufficient
resources (CPUs, GPUs, memory, licenses) are available and not already
reserved for jobs with a higher priority.

To see the priorities of your currently pending jobs you can use the
command `sprio -u $USER`.

## Factors

Priority scores are determined by a number of factors:

### Quality of Service

The "debug" Quality of Service can be gained by adding the `sbatch`
command line option `--qos=debug`.  
This adds 5000 to the job priority so raises it above all non-debug
jobs, but is limited to one small job per user at a time: no more than
15 minutes and no more than 2 nodes.

### Fair Share

Job priority decreases whenever the project uses more core-hours than
expected, across all partitions.
This [Fair Share](../../Scientific_Computing/Batch_Jobs/Fair_Share.md)
policy means that projects that have consumed many CPU core hours in the
recent past compared to their expected rate of use (either by submitting
and running many jobs, or by submitting and running large jobs) will
have a lower priority, and projects with little recent activity compared
to their expected rate of use will see their waiting jobs start sooner.
Fair Share contributes up to 1000 points to the job priority. To see the current fair-share score of a project you can use the command `sshare`, for seeing recent usage use `nn_corehour_usage`.

### Job Age

Job priority slowly rises with time as a pending job gets older -1
point per hour for up to 3 weeks.

### Job Size or "TRES" (Trackable RESources)

This slightly favours jobs which request a larger count of CPUs (or
memory or GPUs) as a means of countering their otherwise inherently
longer wait times.

Whole-node jobs and others with a similarly high count of cores-per-node will get a priority boost (visible in the “site factor” of `sprio`).
This is to help whole-node jobs get ahead of large distributed jobs with many tasks spread over many nodes.

### Nice values

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

## Backfill

Backfill is a scheduling strategy that allows small, short jobs to run
immediately if by doing so they will not delay the expected start time
of any higher-priority jobs. Since the expected start time of pending
jobs depends upon the expected completion time of running jobs it is
important that you set reasonably accurate job time limits if backfill
is to work well.

While the kinds of jobs that can be backfilled will also get a low job
size score, it is our general experience that an ability to be
backfilled is on the whole more useful when it comes to getting work
done on the HPCs.

See the [Slurm documentation](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/sched_config.html) for more info on backfilling.
