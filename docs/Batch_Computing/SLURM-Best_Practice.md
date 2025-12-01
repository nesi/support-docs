---
created_at: '2019-01-18T01:56:15Z'
tags: 
    - slurm
    - tips
title: 'SLURM: Best Practice'
description: Some tips on how to get more out of the job sceduler.
---

## Bash Header

We recommend using `#!/bin/bash -e` instead of plain `#!/bin/bash`, so
that the failure of any command within the script will cause your job to
stop immediately rather than attempting to continue on with an
unexpected environment or erroneous intermediate data. It also ensures
that your failed jobs show a status of FAILED in `sacct` output.

## Resources

Don't request more resources (CPUs, memory, GPUs) than you will need. In
addition to using your core hours faster, resources intensive jobs will
take longer to queue. Use the information provided at the completion of
your job (e.g: via the `sacct` command) to better define resource
requirements.

<!-- insert link to scaling docs here -->

### Wall-time

Long jobs will spend more time in the queue, as there are more
opportunities for the scheduler to find a time slot to run shorter jobs.
So consider using job check-pointing or, where possible, more
parallelism, to get job duration down to a few hours, or at worst,
days.

Leave some headroom for safety and run-to-run variability on the system
but try to be as accurate as possible.

If you have many jobs of less than 5 minutes then they should
probably be combined into larger jobs using a simple loop in the batch
script so as to amortise the overheads of each job (starting, accounting
etc).

### Memory (RAM)

If you request more memory (RAM) than you need for your job, it
[will wait longer in the queue and will be more expensive when it runs](../Getting_Started/FAQs/Why_is_my_job_taking_a_long_time_to_start.md).
On the other hand, if you don't request enough memory, the job may be
killed for attempting to exceed its allocated memory limits.

We recommend that you request a little more RAM, but not much more, than
your program will need at peak memory usage.

We also recommend using `--mem` instead of `--mem-per-cpu` in most
cases. There are a few kinds of jobs for which `--mem-per-cpu` is more
suitable. See [our article on how to request memory](../Getting_Started/FAQs/How_do_I_request_memory.md)
for more information.

## Parallelism

In general only MPI jobs should set `--ntasks` greater than 1 or use
`srun`. If you don't know whether your program supports MPI, it
probably doesn't.

Only multithreaded jobs should set `--cpus-per-task`. If you don't know
whether your program supports multithreading, try benchmarking with 2
CPUs and with 4 CPUs and see if there is a 2-fold difference in elapsed
job time.

[Job arrays](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/job_array.html) are an efficient
mechanism of managing a collection of batch jobs with identical resource
requirements. Most Slurm commands can manage job arrays either as
individual elements (tasks) or as a single entity (e.g. delete an entire
job array in a single command)

## Fairshare

A low fairshare score will affect your jobs priority in the queue, learn
more about how to effectively use your allocation,
[Fair Share](Fair_Share.md).
