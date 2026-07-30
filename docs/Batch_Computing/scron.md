---
created_at: '2026-07-30'
tags:
  - cron
  - scrontab
  - scron
description: How to use scron (Slurm cron) to schedule jobs
---

*cron* is a linux service that provides users a method to run a task (job) at a set time or interval. *scron* is the Slurm version of this service that allows users to setup jobs using the well-documented cron syntax along with Slurm job configuration.  

## scrontab

To make use of the *scron* service, you will use the `scrontab` utility. 

To view your current *scron* scheduled jobs, type:  `scrontab -l`.  To edit or add an entry using your default editor type: `scrontab -e`.   Running `scrontab -e` will open the users default editor.  This is defined with the `$EDITOR` environment variable.  By default this will be `nano`.

For more detailed information about using *scron*, type `man scrontab` to view the manual.

_Example_

The following `scrontab` entry will run the `hostname` command, once an hour at the top of the hour, eg 09:00, 10:00, 11:00, etc.  It will do this until you remove the entry:

```
$ scrontab -e

# Welcome to scrontab, Slurm's cron-like interface.
#
# Edit this file to submit recurring jobs to be run by Slurm.
#
# Note that jobs will be run based on the Slurm controller's
# time and timezone.
#
# Lines must either be valid entries, comments (start with '#'),
# or blank.
#
# Lines starting with #SCRON will be parsed for options to use
# with the next cron line. E.g., "#SCRON --time 1" would request
# a one minute timelimit be applied. See the sbatch man page for
# options, although note that not all options are supported here.
#
# For example, the following line (when uncommented) would request
# a job be run at 5am each day.
# 0 5 * * * /my/script/to/run
#
# min hour day-of-month month day-of-week command

0 * * * * hostname >> ~/hostname_log.txt
```

Notice the comment `min hour day-of-month month day-of-week`  These are reminders of what the columns represent. In our example we added a `0` in the `min` column.  The other colums are marked with a `*` meaning *all*.   This translates to:  At 0 minutes, of every hour of every day, of every month, run the command `hostname` and redirect the output to a file in my home directory called `hostname_log.txt`




## scron parameters

What sets `scron` from regular `cron` is the fact that you can define Slurm parameters.  Similar to a `sbatch` submit script, but instead of using `#SBATCH` in your script, you employ `#SCRON`, adding to our example from above:

```
# Welcome to scrontab, Slurm's cron-like interface.
#
# Edit this file to submit recurring jobs to be run by Slurm.
#
# Note that jobs will be run based on the Slurm controller's
# time and timezone.
#
# Lines must either be valid entries, comments (start with '#'),
# or blank.
#
# Lines starting with #SCRON will be parsed for options to use
# with the next cron line. E.g., "#SCRON --time 1" would request
# a one minute timelimit be applied. See the sbatch man page for
# options, although note that not all options are supported here.
#
# For example, the following line (when uncommented) would request
# a job be run at 5am each day.
# 0 5 * * * /my/script/to/run
#
# min hour day-of-month month day-of-week command

#SCRON --job-name=hostname-log --time=0:05:00
0 * * * * hostname >> ~/hostname_log.txt
```

We added the line starting with `#SCRON` to include slurm paramaters, we configure a job name and a max runtime of 5 minutes.

You can add more than one scheduled job, eg.

```
# min hour day-of-month month day-of-week command

#SCRON --job-name=hostname-log --time=0:05:00
0 * * * * hostname >> ~/hostname_log.txt

#SCRON --job-name=update-model --time=1:00:00 --partition=genoa
0 3 15 * * model-refresh.py
```

We added a new scheduled job to run our model refresh script on the fifteenth of every month at 03:00.  Note that we are requesting the job to run on a genoa node.  Most, but not all sbatch parameters are available in *scron*

## Slurm Queue

Once you have setup your scron job.  You will notice it is listed in `squeue`

```
JOBID    PARTITION     NAME     USER    ST       TIME  NODES NODELIST(REASON)
12345432 milan,genoa   hostname  mrbar  PD       0:00      1         (BeginTime)
```

`(BeginTime)` is one indication that this is a scheduled scron job, it means the job is scheduled in the future. 



## Disable *scron* job


To disable a job in your scrontab, you can remove the line or add a `#` (comment character) before the line.  Any line beginning with `#SCRON` can be disabled in the same way, eg.

```
##SCRON --job-name=update-model --time=1:00:00 --partition=genoa
#0 3 15 * * model-refresh.py
```

