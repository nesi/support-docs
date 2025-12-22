---
created_at: '2020-01-05T21:43:18Z'
tags: 
  - interactive
  - scheduling
description: How to run an interactive session on the NeSI cluster.
---

A SLURM interactive session reserves resources on compute nodes allowing
you to use them interactively as you would the login node.

There are two main commands that can be used to make a session, `srun`
and `salloc`.  Both `srun` and `salloc` share most of the same options as `sbatch` (see [our Slurm Reference Sheet](../Getting_Started/Cheat_Sheets/Slurm-Reference_Sheet.md)).

## Getting Started

### Using `srun`

`srun` will add your resource request to the queue. When the allocation
starts, a new bash session will start up on one of the compute nodes.

For example;

```bash
srun --account nesi12345 --pty bash
```

This is the minimum required to start and interactive job.  The `--pty` requests a terminal session be created, omitting this will simply run bash in the background and will not be interactive.  Be aware that the above command requests minimal resources, which may not be sufficient for your needs.  Request the proper amount of CPU, memory and time for your job.  Once you have typed the above command, you will receive a message similar to this:

```out
srun: job 10256812 queued and waiting for resources
```

Depending on the resources requested and the load on the cluster, it may take some time for the job to start, when it does start you will receive a new prompt similar to: 

```out
srun: job 10256812 has been allocated resources
[c004 ~ SUCCESS ]$
```

You can see from the prompt you are running on a different host as it is showing:
`c004` instead of a login node.

For a full description of `srun` and its options, see the
[documentation](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/srun.html).

### Using `salloc`

`salloc` functions similarly `srun --pty bash` in that it will add your
resource request to the queue. However the allocation starts, a new bash
session will start up on **the login node.** This is useful for running
a GUI on the login node, but your processes on the compute nodes.

For example:

```bash
salloc --account nesi12345 --cpus-per-task 8 --mem-per-cpu 15M --time 2:00:00
```

You will receive a message.

```out
salloc: Pending job allocation 10256925
salloc: job 10256925 queued and waiting for resources
```

And when the job starts;

```out
salloc: job 10256925 has been allocated resources
salloc: Granted job allocation 10256925 
salloc: Nodes c038 are ready for job
[login03 ~ SUCCESS ]$
```

Note the that you are still on the login node `login03`, however you
will now have permission to `ssh` to the nodes mendtioned in the output or from `squeue --me`, in the above case, the node is `c038`, and now we can:

```bash
ssh c038
```

For a full description of `salloc` and its options, see
[documentation](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/salloc.html).

### Running a GUI application

It is possible to run GUI applications interactively on the cluster.  Along with the `--pty` flag, one should also include the `--x11` flag and have a properly configured X server.  More information can be found here:  [https://docs.nesi.org.nz/Getting_Started/Accessing_the_HPCs/X11/](https://docs.nesi.org.nz/Getting_Started/Accessing_the_HPCs/X11/)

Depending on the GUI application and resource requirements, it may be beneficial to run a Virtual Desktop from our OnDemand service instead of using X forwarding: [https://ondemand.nesi.org.nz/pun/sys/dashboard](https://ondemand.nesi.org.nz/pun/sys/dashboard)

### Setting up a detachable terminal

It's quite common to have to wait for some time before your interactive
session starts. For an interactive session, or any other long-running process, 
it is recommended you use a terminal multiplexor such as `tmux`.  This
allows your session to be detached from the running terminal so you can re-connect if your
laptop goes to sleep, the network drops or any other event that could sever the connection.
You can even re-attach from a different computer.

We have a reference page for `tmux`, [here](https://docs.nesi.org.nz/Getting_Started/Cheat_Sheets/tmux-Reference_sheet/)

!!! warning
     Once an interactive session starts, it will run for the entire requested
     block of time, unless exited earlier. To avoid unnecessary billing to your allocation, 
     don't forget to exit an interactive session once finished.

## Advanced Topics

### Requesting a postponed start

`salloc` lets you specify that a job is not to start before a specified
time, however the job may still be delayed if requested resources are
not available. You can request a start time using the `--begin` flag.

The `--begin` flag takes either absolute or relative times as values.


- `--begin=16:00` means start the job no earlier than 4 p.m. today.
    (Seconds are optional, but the time must be given in 24-hour
    format.)
- `--begin=11/05/20` means start the job on (or after) 5
    November 2020. Note that Slurm uses American date formats.
    `--begin=2020-11-05` is another Slurm-acceptable way of saying the
    same thing, and possibly easier for a New Zealander.
- `--begin=2020-11-05T16:00:00` means start the job on (or after) 4
    p.m. on 5 November 2020.
- `--begin=now+1hour` means wait at least one hour before starting the
    job.
- `--begin=now+60` means wait at least one minute before starting the
    job.

If no `--begin` argument is given, the default behaviour is to start as
soon as possible.

If you specify absolute dates and/or times, Slurm will interpret those
according to your environment's current time zone. Ensure that you
know what time zone your environment is using, for example by running
`date` in the same terminal session.


### Modifying an existing interactive session

Whether your interactive session is already running or is still waiting
in the queue, you can make a range of changes to it using the `scontrol`
command. Some changes are off limits for ordinary users, such as
increasing the maximum permitted wall time, or unsafe, like decreasing
the memory request. But many other changes are allowed.

#### Postponing the start of an interactive job

Suppose you submitted an interactive job just after lunch, and it's
already 4 p.m. and you're leaving in an hour. You decide that even if
the job starts now, you won't have time to do everything you need to do
before the office shuts and you have to leave. Even worse, the job might
start at 11 p.m. after you've gone to bed, and you'll get to work at
9:00 the next morning and find that it has wasted ten wall-hours of
time.

Slurm offers an easy solution: Identify the job, and use `scontrol` to
postpone its start time.

!!! note
     Job IDs are unique to each cluster but not across the whole of NeSI.
     Therefore, `scontrol` must be run on a node belonging to the cluster
     where the job is queued.

The following command will delay the start of the job with numeric ID
12345678 until (at the earliest) 9:30 a.m. the next day:

```sh
scontrol update jobid=12345678 StartTime=tomorrowT09:30:00
```

This variation, if run on a Friday, will delay the start of the same job
until (at the earliest) 9:30 a.m. on Monday:

```sh
scontrol update jobid=12345678 StartTime=now+3daysT09:30:00
```

!!! warning
     Don't just set `StartTime=tomorrow` with no time specification unless
     you like the idea of your interactive session starting at midnight or
     in the wee hours of the morning.

#### Bringing forward the start of an interactive job

In the same way, you can use scontrol to set a job's start time to
earlier than its current value. A likely application is to allow a job
to start immediately even though it stood postponed to a later time:

```sh
scontrol update jobid=12345678 StartTime=now
```

#### Other changes using `scontrol`

There are many other changes you can make by means of `scontrol`. For
further information, please see
[the `scontrol` documentation](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/scontrol.html).

### Modifying multiple interactive sessions at once

In the same way, if you have several interactive sessions waiting to
start on the same cluster, you might want to postpone them all using a
single command. To do so, you will first need to identify them, hence
the earlier suggestion to something specific to interactive jobs in the
job name.

For example, if all your interactive job names start with the text "InteractiveJob",
you could do this:

```sh
# -u $(whoami) restricts the search to my jobs only.
# The --states=PD option restricts the search to pending jobs only.
#
squeue -u $(whoami) --states=PD -o "%A %j" | grep "InteractiveJob"
```

The above command will return a list of your jobs whose names *start*
with the text "InteractiveJob". In this respect, it's more flexible than the `-n`
option to `squeue`, which requires the entire job name string in order
to identify a match.

In order to use `scontrol`, we need to throw away all of the line except
for the job ID, so let's use `awk` to do this, and send the output to
`scontrol` via `xargs`:

```sh
squeue -u $(whoami) --states=PD -o "%A %j" | grep "InteractiveJob" | \
awk '{print $1}' | \
xargs -I {} scontrol update jobid={} StartTime=tomorrowT09:30:00
```

<!-- If you want to do this automatically every working day and you have a
consistent element that you use in the name of all your interactive
jobs, you can set up cron jobs on Māui, Mahuika and/or Māui-ancil login
nodes. This is left as an exercise for the reader, having regard to the
following:

- **Time zone:** Even if your environment is set up to use a different
    time zone (commonly New Zealand time, which adjusts for daylight
    saving as needed), time schedules in the crontab itself are
    interpreted in UTC. So if you want something to run at 4:30 p.m. New
    Zealand time regardless of the time of year, the cron job will need
    to run at 4:30 a.m. UTC (during winter) or 3:30 a.m. UTC (during
    summer), and you will need to edit the crontab every six months or
    so.
- **Weekends:** If you just have a single cron job that postpones
    pending interactive jobs until the next day, interactive jobs
    pending on a Friday afternoon will be postponed until Saturday
    morning, which is probably not what you want. Either your cron job
    detects the fact of a Friday and postpones jobs until Monday, or you
    have two cron jobs, one that runs on Mondays to Thursdays, and a
    different cron job running on Fridays. -->

### Cancelling an interactive session

You can cancel a pending interactive session by attaching the relevant
session, putting the job in the foreground (if necessary) and pressing
`Ctrl`-`C` on your keyboard.

To cancel all your queued interactive sessions on a cluster in one fell
swoop, a command like the following should do the trick:

```sh
squeue -u $(whoami) --states=PD -o "%A %j" | grep "InteractiveJob" | \
awk '{print $1}' | \
xargs -I {} scancel {}
```

To cancel all your running interactive sessions on a cluster in one fell
swoop, a command like the following should do the trick:

```sh
squeue -u $(whoami) --states=R -o "%A %j" | grep "InteractiveJob" | \
awk '{print $1}' | \
xargs -I {} scancel {}
```

If you frequently use interactive jobs, we recommend doing this before
you go away on leave or fieldwork or other lengthy absence.
