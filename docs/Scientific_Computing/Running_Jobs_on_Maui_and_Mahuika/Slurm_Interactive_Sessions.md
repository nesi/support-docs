---
created_at: '2020-01-05T21:43:18Z'
hidden: false
position: 5
tags: []
title: Slurm Interactive Sessions
vote_count: 7
vote_sum: 1
zendesk_article_id: 360001316356
zendesk_section_id: 360000030876
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

A SLURM interactive session reserves resources on compute nodes allowing
you to use them interactively as you would the login node.

There are two main commands that can be used to make a session, `srun`
and `salloc`, both of which use most of the same options available to
`sbatch` (see [our Slurm Reference
Sheet](https://support.nesi.org.nz/hc/en-gb/articles/360000691716)).
!!! prerequisite Warning
An interactive session will, once it starts, use the entire requested
block of CPU time and other resources unless earlier exited from, even
if unused. To avoid unnecessary charges to your project, don't forget
to exit an interactive session once finished.

## Using 'srun --pty bash'

`srun` will add your resource request to the queue. When the allocation
starts, a new bash session will start up on **one of the granted
nodes.**

For example;

``` sl
srun --account nesi12345 --job-name "InteractiveJob" --cpus-per-task 8 --mem-per-cpu 1500 --time 24:00:00 --pty bash
```

You will receive a message.

``` sl
srun: job 10256812 queued and waiting for resources
```

And when the job starts:

``` sl
srun: job 10256812 has been allocated resources
[wbn079 ~ SUCCESS ]$
```

Note the host name in the prompt has changed to the compute node
`wbn079`.

For a full description of `srun` and its options, see
[here](https://slurm.schedmd.com/srun.html).

## Using 'salloc'

`salloc` functions similarly `srun --pty bash` in that it will add your
resource request to the queue. However the allocation starts, a new bash
session will start up on **the login node.** This is useful for running
a GUI on the login node, but your processes on the compute nodes.

For example:

``` sl
salloc --account nesi12345 --job-name "InteractiveJob" --cpus-per-task 8 --mem-per-cpu 1500 --time 24:00:00
```

You will receive a message.

``` sl
salloc: Pending job allocation 10256925
salloc: job 10256925 queued and waiting for resources
```

And when the job starts;

``` sl
salloc: job 10256925 has been allocated resources
salloc: Granted job allocation 10256925
[mahuika01~ SUCCESS ]$
```

Note the that you are still on the login node `mahuika01`, however you
will now have permission to `ssh` to any node you have a session on .

For a full description of `srun` and its options, see
[here](https://slurm.schedmd.com/salloc.html).

### Requesting a postponed start

`salloc` lets you specify that a job is not to start before a specified
time, however the job may still be delayed if requested resources are
not available. You can request a start time using the `--begin` flag.

The `--begin` flag takes either absolute or relative times as values.
!!! prerequisite Warning
If you specify absolute dates and/or times, Slurm will interpret those
according to your environment's current time zone. Ensure that you
know what time zone your environment is using, for example by running
`date` in the same terminal session.

-   `--begin=16:00` means start the job no earlier than 4 p.m. today.
(Seconds are optional, but the time must be given in 24-hour
format.)
-   `--begin=11/05/20` means start the job on (or after) 5
November 2020. Note that Slurm uses American date formats.
`--begin=2020-11-05` is another Slurm-acceptable way of saying the
same thing, and possibly easier for a New Zealander.
-   `--begin=2020-11-05T16:00:00` means start the job on (or after) 4
p.m. on 5 November 2020.
-   `--begin=now+1hour` means wait at least one hour before starting the
job.
-   `--begin=now+60` means wait at least one minute before starting the
job.

If no `--begin` argument is given, the default behaviour is to start as
soon as possible.

### While you wait

It's quite common to have to wait for some time before your interactive
session starts, even if you specified, expressly or by implication, that
the job is to start as soon as possible.

While you're waiting, you will not have use of that shell prompt. **Do
not use `Ctrl`-`C` to get the prompt back, as doing so will cancel the
job.** If you need a shell prompt, detach your `tmux` or `screen`
session, or switch to (or open) another terminal session to the same
cluster's login node.

In the same way, before logging out (for example, if you choose to shut
down your workstation at the end of the working day), be sure to detach
the `tmux` or `screen` session. In fact, we recommend detaching whenever
you leave your workstation unattended for a while, in case your computer
turns off or goes to sleep or its connection to the internet is
disrupted while you're away.



## Setting up a detachable terminal
!!! prerequisite Warning
If you don't request your interactive session from within a detachable
terminal, any interruption to the controlling terminal, for example by
your computer going to sleep or losing its connection to the internet,
will permanently cancel that interactive session and remove it from
the queue, whether it has started or not.

1.  Log in to a Mahuika, Māui or Māui-ancil login node.
2.  Start up `tmux` or `screen`.

## Modifying an existing interactive session

Whether your interactive session is already running or is still waiting
in the queue, you can make a range of changes to it using the `scontrol`
command. Some changes are off limits for ordinary users, such as
increasing the maximum permitted wall time, or unsafe, like decreasing
the memory request. But many other changes are allowed.

### Postponing the start of an interactive job

Suppose you submitted an interactive job just after lunch, and it's
already 4 p.m. and you're leaving in an hour. You decide that even if
the job starts now, you won't have time to do everything you need to do
before the office shuts and you have to leave. Even worse, the job might
start at 11 p.m. after you've gone to bed, and you'll get to work at
9:00 the next morning and find that it has wasted ten wall-hours of
time.

Slurm offers an easy solution: Identify the job, and use `scontrol` to
postpone its start time.
!!! prerequisite Note
Job IDs are unique to each cluster but not across the whole of NeSI.
Therefore, `scontrol` must be run on a node belonging to the cluster
where the job is queued.

The following command will delay the start of the job with numeric ID
12345678 until (at the earliest) 9:30 a.m. the next day:

``` sl
scontrol update jobid=12345678 StartTime=tomorrowT09:30:00
```

This variation, if run on a Friday, will delay the start of the same job
until (at the earliest) 9:30 a.m. on Monday:

``` sl
scontrol update jobid=12345678 StartTime=now+3daysT09:30:00
```
!!! prerequisite Warning
Don't just set `StartTime=tomorrow` with no time specification unless
you like the idea of your interactive session starting at midnight or
in the wee small hours of the morning.

### Bringing forward the start of an interactive job

In the same way, you can use scontrol to set a job's start time to
earlier than its current value. A likely application is to allow a job
to start immediately even though it stood postponed to a later time:

``` sl
scontrol update jobid=12345678 StartTime=now
```

### Other changes using `scontrol`

There are many other changes you can make by means of `scontrol`. For
further information, please see [the `scontrol`
documentation](https://slurm.schedmd.com/scontrol.html) (off site).

## Modifying multiple interactive sessions at once

In the same way, if you have several interactive sessions waiting to
start on the same cluster, you might want to postpone them all using a
single command. To do so, you will first need to identify them, hence
the earlier suggestion to something specific to interactive jobs in the
job name.

For example, if all your interactive job names start with the text "IJ",
you could do this:

``` sl
# -u $(whoami) restricts the search to my jobs only.
# The --states=PD option restricts the search to pending jobs only.
#
# Each <tab> string should be replaced with a literal tab character. If you
# can't insert one by pressing the tab key on your keyboard, you should be
# able to insert one by pressing Ctrl-V followed immediately by Ctrl-I.
#
squeue -u $(whoami) --states=PD -o "%A<tab>%j" | grep "<tab>IJ"
```

The above command will return a list of your jobs whose names *start*
with the text "IJ". In this respect, it's more flexible than the `-n`
option to `squeue`, which requires the entire job name string in order
to identify a match.

In order to use `scontrol`, we need to throw away all of the line except
for the job ID, so let's use `awk` to do this, and send the output to
`scontrol` via `xargs`:

``` sl
squeue -u $(whoami) --states=PD -o "%A<tab>%j" | grep "<tab>IJ" | \
awk '{print $1}' | \
xargs -I {} scontrol update jobid={} StartTime=tomorrowT09:30:00
```

If you want to do this automatically every working day and you have a
consistent element that you use in the name of all your interactive
jobs, you can set up cron jobs on Māui, Mahuika and/or Māui-ancil login
nodes. This is left as an exercise for the reader, having regard to the
following:

-   **Time zone:** Even if your environment is set up to use a different
time zone (commonly New Zealand time, which adjusts for daylight
saving as needed), time schedules in the crontab itself are
interpreted in UTC. So if you want something to run at 4:30 p.m. New
Zealand time regardless of the time of year, the cron job will need
to run at 4:30 a.m. UTC (during winter) or 3:30 a.m. UTC (during
summer), and you will need to edit the crontab every six months or
so.
-   **Weekends:** If you just have a single cron job that postpones
pending interactive jobs until the next day, interactive jobs
pending on a Friday afternoon will be postponed until Saturday
morning, which is probably not what you want. Either your cron job
detects the fact of a Friday and postpones jobs until Monday, or you
have two cron jobs, one that runs on Mondays to Thursdays, and a
different cron job running on Fridays.

## Cancelling an interactive session

You can cancel a pending interactive session by attaching the relevant
session, putting the job in the foreground (if necessary) and pressing
`Ctrl`-`C` on your keyboard.

To cancel all your queued interactive sessions on a cluster in one fell
swoop, a command like the following should do the trick:

``` sl
squeue -u $(whoami) --states=PD -o "%A<tab>%j" | grep "<tab>IJ" | \
awk '{print $1}' | \
xargs -I {} scancel {}
```

If you frequently use interactive jobs, we recommend doing this before
you go away on leave or fieldwork or other lengthy absence.