---
created_at: '2019-01-31T01:17:22Z'
hidden: false
label_names:
- scaling
position: 3
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
your needed resources *when you submit the job*, so that the scheduler
can make sure enough resources are available for your job during the
whole time it is running, and also knows what resources will be free for
others to use at the same time.

The three resources that every single job submitted on the platforms
needs to request are:

-   CPUs (i.e. logical CPU cores), and
-   Memory (RAM), and
-   Time.

Some jobs will also need to request GPUs.

# What happens if I ask for the wrong resources?

When you are initially trying to set up your jobs it can be difficult to
ascertain how much of each of these resources you will need. Asking for
too little or too much, however, can both cause problems: your jobs will
be at increased risk of taking a long time in the queue or failing, and
your project's [fair share
score](https://support.nesi.org.nz/hc/en-gb/articles/360000743536) is
likely to suffer.  Your project's fair share score will be reduced in
view of CPU time spent regardless of whether you obtain a result or
not. 

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

It is therefore important to try and make your jobs resource requests
reasonably accurate. In this article we will discuss how you can scale
your jobs to help you better estimate your jobs resource needs.

# Job Scaling

Before you start submitting the main bulk of your jobs, it is <span
class="SDZsVb">advisable to first submit a *test job*. </span>

<span class="SDZsVb">A test job should be representative of the main
body of your work, scaled down (e.g. a small subset of your data or a
low number of job steps). Aim for your test job to run for around 10
minutes, too much shorter and your job will be spending a high
proportion of its time on overhead and therefore be less accurate for
the purposes of scaling.</span>

<span class="SDZsVb">Keeping your test job small ensures a short queue
time, short run time and that minimal resources are expended.</span>

When scaling your jobs, one of the most beneficial things you can do is
to first scale down your data and calculations to as small as you can.
Whether this means only computing on a few rows and columns of your
data, or only doing a subset of the calculations you intend to do in the
complete jobs, cutting your initial test jobs down in size means that
they will both queue faster and run for less time. Also, if one of these
jobs fails due to not asking for enough resources, a small scale job
will (hopefully) not have waited for hours or days in the queue
beforehand.

> ### Examples
>
> [Multithreading
> Scaling](https://support.nesi.org.nz/hc/en-gb/articles/360001173895)
>
> [MPI
> Scaling](https://support.nesi.org.nz/hc/en-gb/articles/360001173875)
