---
created_at: '2018-05-17T23:35:36Z'
hidden: false
label_names: []
position: 8
title: Job prioritisation
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000201636
zendesk_section_id: 360000030876
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
 !!! Info
     This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
Each queued job has a priority score.  Jobs start when sufficient
resources (CPUs, GPUs, memory, licenses) are available and not already
reserved for jobs with a higher priority.

To see the priorities of your currently pending jobs you can use the
command `sprio -u $USER`.

Priority scores are determined by a number of factors:

### 1) Quality of Service

The "debug" Quality of Service can be gained by adding the `sbatch`
command line option `--qos=debug`.  
This adds 5000 to the job priority so raises it above all non-debug
jobs, but is limited to one small job per user at a time: no more than
15 minutes and no more than 2 nodes.

### 2) Fair Share

Job priority decreases whenever the project uses more core-hours than
expected, across all partitions. This [Fair
Share](https://support.nesi.org.nz/hc/en-gb/articles/360000743536)
policy means that projects that have consumed many CPU core hours in the
recent past compared to their expected rate of use (either by submitting
and running many jobs, or by submitting and running large jobs) will
have a lower priority, and projects with little recent activity compared
to their expected rate of use will see their waiting jobs start sooner.
 Fair Share contributes up to 1000 points to the job priority. To see
the recent usage and current fair-share score of a project, you can use
the command nn\_corehour\_usage.

### 3) Job Age

Job priority slowly rises with time as a pending job gets older - 1
point per hour for up to 3 weeks.

### 4) Job Size or "TRES" (Trackable RESources)

This slightly favours jobs which request a larger count of CPUs (or
memory or GPUs) as a means of countering their otherwise inherently
longer wait times.

### 5) Project Allocation Class

This depends on which "allocation class" entitles your project to use
NeSI.

<table style="margin-left: 0px; margin-right: auto;">
<tbody>
<tr class="odd">
<td><strong>Project class</strong></td>
<td><strong>Class Priority Score </strong></td>
</tr>
<tr class="even">
<td>Proposal Development</td>
<td class="wysiwyg-text-align-right">10</td>
</tr>
<tr class="odd">
<td>Postgraduate</td>
<td class="wysiwyg-text-align-right">20</td>
</tr>
<tr class="even">
<td>Collaborator</td>
<td class="wysiwyg-text-align-right">30</td>
</tr>
<tr class="odd">
<td>Merit</td>
<td class="wysiwyg-text-align-right">40</td>
</tr>
<tr class="even">
<td>Commercial</td>
<td class="wysiwyg-text-align-right">40</td>
</tr>
</tbody>
</table>

###  

### 6) Nice values

It is possible to give a job a "nice" value which is subtracted from its
priority. You can do that with the `--nice` option of `sbatch` or the
`scontrol update` command.  The command `scontrol top <jobid>` adjusts
nice values to increase the priority of one of your jobs at the expense
of any others you have in the same partition.

### 7) Holds

Jobs with a priority of 0 are in a "held" state and will never start
without further intervention.  You can hold jobs with the command
`scontrol hold <jobid>` and release them with
`scontrol release <jobid>`.  Jobs can also end up in this state when
they get requeued after a node failure. 

## Other Limits

Cluster and partition-specific limits can sometimes prevent jobs from
starting regardless of their priority score.  For details see the pages
on [Mahuika](https://support.nesi.org.nz/hc/en-gb/articles/360000204076) or [Māui.](https://support.nesi.org.nz/hc/en-gb/articles/360000204116)

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

More information about backfill can be found
[here](https://slurm.schedmd.com/sched_config.html).

 
