---
created_at: '2021-09-21T00:16:50Z'
hidden: true
label_names: []
position: 2
title: Repeating jobs
vote_count: 0
vote_sum: 0
zendesk_article_id: 4406771973007
zendesk_section_id: 360000030876
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
## Re-submitting a job script from within itself

Jobs can submit additional jobs. To avoid any risk of a runaway
explosion of jobs, there should be no more than one such
self-resubmission.  Doing this reliably can be a bit complicated.
 Potentially useful tools include:

-   Various sbatch options:
    -   "--depend=afterok:$SLURM\_JOB\_ID"
    -   "--depend=singleton"
    -   "--begin=now+1days"
    -   "--signal=USR1@120"
-   Using bash traps to execute something on job exit

## Cron

Cron is the standard Unix way of performing a task at a fixed time every
hour, day, or week.  It is possible to use it on most interactive NeSI
nodes, however there are some complications and limitations:

-   We don't want too much heavy calculation or memory use happening on
    the login nodes since they are shared will all other users. So large
    scheduled tasks should be run indirectly - with the *cron* script
    merely submitting a Slurm job, or one of the other mechanisms
    described here should be used.
-   The main clusters each have two login nodes and when one has
    problems we switch to the other being the default, so you need to
    keep track of which node's cron you are using.
-   The stored *crontab* files will be deleted whenever we have to
    reboot the node in question, so this example crontab file backs
    itself up every week:

<!-- -->

    CRON_TZ=NZ
    PATH=/usr/bin

    # min    hr    dom   month      dow         command
       30    12    *       *        sun         crontab -l > $HOME/.crontab.backup

Scripts run via cron should generally start like:

    #!/bin/bash
    source /etc/profile >/dev/null 2>&1

That sets up the environment as if you had logged in, including the
*module *command. Except that it doesn't use your *.bash\_profile* or
*.bashrc* files, so you need to source those too if you define anything
you need in them.

For general instructions see:

    man crontab

## Scron

*scrontab* is Slurm's analogue of *crontab*.  Rather than running
directly on the login node it submits Slurm jobs at the scheduled times.
 At present is is only available on Mahuika.  In general we think it is
superior to cron, particularly if the job requires significant
resources.  But it does also have it's own particular drawbacks:

-   It does not support the CRON\_TZ setting, so all times (and dates)
    must be UTC ones.
-   The exact start time of jobs is not be guaranteed as the jobs must
    still queue. However short, serial jobs usually start promptly, and
    if you need more certainty please ask us as we could arrange higher
    priority for *scron* jobs.

Job options which would normally be given as \#SBATCH directives are
instead given as \#SCRON directives directly in the *scrontab* file, eg:

    #SCRON -t 10
    #SCRON -J my_weekly_scron_job
    # min    hr    dom   month      dow         command
       30    12    *       *        sun         bash /home/me/weekly_script.sh

For general instructions see:

    man scrontab

## Cylc

Cylc is NIWA's system for running cylic workflows such as those used in
weather forecasting. 
