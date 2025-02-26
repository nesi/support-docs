---
created_at: '2019-01-31T01:17:22Z'
tags:
- scaling
title: Job Scaling - Ascertaining job dimensions
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000728016
zendesk_section_id: 360000189716
---

When you run software in an interactive environment such as your
ordinary workstation (desktop PC or laptop), the software is able to
request from the operating system whatever resources it needs from
moment to moment. By contrast, on our HPC platforms, you must request
your needed resources *when you submit the job*, so that the scheduler
can make sure enough resources are available for your job during the
whole time it is running, and also knows what resources will be free for
others to use at the same time.

The three resources that every single job submitted on the platforms
needs to request are:

- CPUs (i.e. logical CPU cores), and
- Memory (RAM), and
- Time.

Some jobs will also need to request GPUs.

## What happens if I ask for the wrong resources?

When you are initially trying to set up your jobs it can be difficult to
ascertain how much of each of these resources you will need.
Asking for too little or too much, however, can both cause problems:
your jobs will
be at increased risk of taking a long time in the queue or failing, and
your project's [fair share score](../Mahuika_Cluster/Next_Steps/Fair_Share.md)
is likely to suffer.
Your project's fair share score will be reduced in
view of compute time spent regardless of whether you obtain a result or
not.

| Resource | Asking for too much | Not asking for enough |
|---|---|---|
| CPUs | The job may wait in the queue for longer. Your fair share score will fall rapidly (your project will be charged for CPU cores that it reserved but didn't use) | The job will run more slowly than expected, and so may run out of time and get killed for exceeding its time limit. |
| Memory | The job may wait in the queue for longer. Your fair share score will fall more than necessary. | Your job will fail, probably with an 'OUT OF MEMORY' error, segmentation fault or bus error. This may not happen immediately. |
| Wall time | The job may wait in the queue for longer than necessary | The job will run out of time and get killed. |

***See [What is an allocation?](../Mahuika_Cluster/Next_Steps/What_is_an_allocation.md) for more details on how each resource effects your compute usage.***

It is therefore important to try and make your jobs resource requests
reasonably accurate. In this article we will discuss how you can scale
your jobs to help you better estimate your jobs resource needs.

## Job Scaling

Before you start submitting the main bulk of your jobs, it is advisable
to first submit a *test job*.

A test job should be representative of the main body of your work,
scaled down (e.g. a small subset of your data or a low number of job
steps). Aim for your test job to run for around 10 minutes, too much
shorter and your job will be spending a high proportion of its time on
overhead and therefore be less accurate for the purposes of scaling.

Keeping your test job small ensures a short queue time, short run time
and that minimal resources are expended.

When scaling your jobs, one of the most beneficial things you can do is
to first scale down your data and calculations to as small as you can.
Whether this means only computing on a few rows and columns of your
data, or only doing a subset of the calculations you intend to do in the
complete jobs, cutting your initial test jobs down in size means that
they will both queue faster and run for less time. Also, if one of these
jobs fails due to not asking for enough resources, a small scale job
will not have waited for hours or days in the queue
beforehand.

!!! example
     - [Multithreading Scaling](Multithreading_Scaling_Example.md)
     - [MPI Scaling](MPI_Scaling_Example.md)
