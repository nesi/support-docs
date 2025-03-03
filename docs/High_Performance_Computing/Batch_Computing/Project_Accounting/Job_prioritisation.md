---
created_at: '2018-05-17T23:35:36Z'
tags: []
title: Job prioritisation
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000201636
zendesk_section_id: 360000030876
---

Each queued job has a priority score.  Jobs start when sufficient
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
This [Fair Share](Fair_Share.md)
policy means that projects that have consumed many CPU core hours in the
recent past compared to their expected rate of use (either by submitting
and running many jobs, or by submitting and running large jobs) will
have a lower priority, and projects with little recent activity compared
to their expected rate of use will see their waiting jobs start sooner.
 Fair Share contributes up to 1000 points to the job priority. To see
the recent usage and current fair-share score of a project, you can use
the command `nn_corehour_usage`.

### Job Age

Job priority slowly rises with time as a pending job gets older -1
point per hour for up to 3 weeks.

### Job Size or "TRES" (Trackable RESources)

This slightly favours jobs which request a larger count of CPUs (or
memory or GPUs) as a means of countering their otherwise inherently
longer wait times.

### Project Allocation Class

This depends on which "allocation class" entitles your project to use
NeSI.

| Project class        | Class Priority Score |
| -------------------- | -------------------- |
| Proposal Development | 10                   |
| Postgraduate         | 20                   |
| Collaborator         | 30                   |
| Merit                | 40                   |
| Commercial           | 40                   |

### Nice values

It is possible to give a job a "nice" value which is subtracted from its
priority. You can do that with the `--nice` option of `sbatch` or the
`scontrol update` command.  The command `scontrol top <jobid>` adjusts
nice values to increase the priority of one of your jobs at the expense
of any others you have in the same partition.

### Holds

Jobs with a priority of 0 are in a "held" state and will never start
without further intervention.  You can hold jobs with the command
`scontrol hold <jobid>` and release them with
`scontrol release <jobid>`.  Jobs can also end up in this state when
they get requeued after a node failure.

## Other Limits

Cluster and partition-specific limits can sometimes prevent jobs from
starting regardless of their priority score.  For details see the pages
on [Mahuika](../Mahuika_Slurm_Partitions.md) or
[Māui.](../Maui_Slurm_Partitions.md)

## Backfill

Backfill is a scheduling strategy that allows small, short jobs to run
immediately if by doing so they will not delay the expected start time
of any higher-priority jobs. Since the expected start time of pending
jobs depends upon the expected completion time of running jobs it is
important that you set reasonably accurate job time limits if backfill
is to work well.

While the kinds of jobs that can be backfilled will also get a low job
size score, it is our general experience that an ability to be
backfilled is on the whole more useful when it comes to getting work
done on the HPCs.

More information about backfill can be found [here](https://slurm.schedmd.com/sched_config.html).
