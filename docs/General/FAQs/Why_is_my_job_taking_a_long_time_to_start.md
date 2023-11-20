---
created_at: '2019-02-06T22:27:04Z'
hidden: false
position: 0
tags: []
title: Why is my job taking a long time to start?
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000737555
zendesk_section_id: 360000039036
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

If you think your job is taking unexpectedly long to start running,
there are several possible causes.

-   [Scheduled maintenance](#scheduled-maintenance)
-   [Delays in the queue](#delays-in-the-queue)
    -   [Your job is being beaten by other high-priority
        jobs](#other-high-priority-jobs)
        -   [Your project has a low Fair Share
            score](#low-fair-share-score)
        -   [Your project has a high Fair Share score, but there are
            lots of other jobs from similarly high-priority
            projects](#queue-congestion)
    -   [Your job's resource demands are hard to
        satisfy](#difficult-job)
    -   [Some other problem](#other-problem)

## Scheduled maintenance

First, check our [status page](https://status.nesi.org.nz/) to look for
scheduled maintenance periods. If your job would otherwise run on a
cluster during maintenance work affecting that cluster, your job may be
delayed until after the maintenance work is completed and the cluster
returns to service, depending on the nature of the work to be done.

## Delays in the queue

If your job is not supposed to be affected by a maintenance period, you
can get more information by running this command:

``` sl
nn_my_queued_jobs
```

This command will, for each of your queued jobs, produce an output
looking something like this:

``` sl
$ nn_my_queued_jobs 
ACCOUNT                JOBID NAME                 SUBMIT_TIME         QOS    NODE CPUS MIN_MEMORY PRIORITY START_TIME          REASON
nesi99999           12345678 SomeRandomJob        2019-01-01T12:00:00 collab    1    8         2G     1553        N/A          QOSMaxCpuPerJobLimit
```

One of the most useful columns to look at, far over on the right hand
side, is the "Reason" column. This column tells you why the job is
delayed. Common answers include "Priority", "Resources", "Dependency",
"ReqNodeNotAvail", and others.

-   **Priority** means that the job just isn't in the front of the queue
    yet.
-   **Resources** means that there are not currently enough free
    resources to run the job.
-   **Dependency** means the job is in some way dependent on another,
    and the other job (the dependency) has not yet reached the required
    state.
-   **ReqNodeNotAvail** means that the job has requested some specific
    node that is busy working on other jobs, is out of service, or does
    not exist.

A more comprehensive list of job reason codes is available
[here](https://slurm.schedmd.com/squeue.html#lbAF) (offsite). As noted
on that page, if a job is waiting for execution for several reasons,
only one reason will be displayed, and there is not a documented
importance of reasons. For example, one job could say Priority and
another could say Resources, when in fact both are waiting due to
Priority and Resources at the same time.

### Your job is being beaten by other high-priority jobs

You can check the job's priority relative to other waiting jobs by means
of the following command on a
[Mahuika](https://support.nesi.org.nz/hc/articles/360000163575-Mahuika)
or
[Māui](https://support.nesi.org.nz/hc/articles/360000163695-M%C4%81ui)
login node (as appropriate):

``` sl
nn_job_priorities
```

This command is intended to produce the same results as the native Slurm
command `sprio`, but with jobs sorted in order of priority from highest
to lowest.

The output should look something like this:

``` sl
          JOBID PARTITION   PRIORITY        AGE   FAIRSHARE    JOBSIZE        QOS
         793492 gpu             1553        504        1000         20         30
        2008465 long            1107        336         723         18         30
        2039471 long            1083        312         723         18         30
        2039456 long            1083        312         723         18         30
        2039452 long            1083        312         723         18         30
        2039435 long            1083        312         723         18         30
        2039399 long            1083        312         723         18         30
        2039391 long            1083        312         723         18         30
        2039376 long            1083        312         723         18         30
        2039371 long            1083        312         723         18         30
...
```

The important aspect of this list is not your job's numeric priority
score, but rather its priority ranking compared to other jobs.

#### Your project has a low Fair Share score

If, compared to other jobs in the queue, your job's priority (third
column) and fair share score (fifth column) are both low, this usually
means that your project team has recently been using through CPU core
hours faster than expected. See [this
page](https://support.nesi.org.nz/hc/articles/360000743536) for more
information on Fair Share, how you can check your project's fair share
score, and what you can do about a low project fair share score.

#### Your project has a high Fair Share score, but there are lots of other jobs from similarly high-priority projects

In the unlikely scenario that your job's position in the list is low but
your job's fair share score is high (i.e. nearly 1,000), you will just
have to wait, as this scenario supposes that other jobs like yours are
ahead in the queue because they have similar resource needs and similar
(or even higher) Fair Share scores but have been waiting for even longer
than your job. This condition is called *queue congestion*, and arises
when researchers submit a lot of work at about the same time. Because it
is triggered by aggregate researcher behaviour, there isn't much we can
do about it.

### Your job's resource demands are hard to satisfy

If your job's priority is high compared to other jobs but the job still
won't start, make sure that your resource requests (in your Slurm
script) are appropriate. If the nature of your work allows, you could
try:

-   Being more flexible about where in the cluster CPU cores come from
-   Asking for less memory (RAM)
-   Asking for a shorter wall time

You can use the `scontrol` command to reduce the job's requested wall
time limit, for example the following command will set the wall time
limit of job 12345678 to one hour:

``` sl
$ scontrol update jobid=12345678 TimeLimit=01:00:00
```

The `scontrol update` command does not print out any message to say that
it has succeeded, so you can check its effect using `scontrol show`:

``` sl
$ scontrol show job 12345678 | grep TimeLimit
   RunTime=00:00:00 TimeLimit=00:01:00 TimeMin=N/A
```

Note that you can not yourself use `scontrol` to increase a job's
requested wall time.

You can not adjust the amount of memory (RAM) using `scontrol`, and
altering the number of tasks, nodes or cores requested is unwise without
making corresponding changes in the job submission script, and in some
cases the program's input file as well. For this reason, if you wish to
change the amount of memory (RAM) or the number or arrangement of cores,
you should cancel your queued job using the `scancel` command and then
resubmit it. If your project's fair share score is high, your newly
submitted job should progress quickly through the queue.

### Some other problem

If your job priority is high, your resource requests are low and your
job still won't start, please [send a request to our support
team](https://support.nesi.org.nz/hc/requests/new) and we will look into
the problem.