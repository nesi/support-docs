---
created_at: '2019-01-18T01:56:15Z'
hidden: false
label_names: []
position: 12
title: 'SLURM: Best Practice'
vote_count: 2
vote_sum: 2
zendesk_article_id: 360000705196
zendesk_section_id: 360000030876
---

### Bash Header

We recommend using `#!/bin/bash -e` instead of plain `#!/bin/bash`, so
that the failure of any command within the script will cause your job to
stop immediately rather than attempting to continue on with an
unexpected environment or erroneous intermediate data.  It also ensures
that your failed jobs show a status of FAILED in *sacct* output.

### Resources 

Don't request more resources (CPUs, memory, GPUs) than you will need. In
addition to using your core hours faster, resources intensive jobs will
take longer to queue. Use the information provided at the completion of
your job (eg: via the *sacct* command) to better define resource
requirements.

### Wall-time

Long jobs will spend more time in the queue, as there are more
opportunities for the scheduler to find a time slot to run shorter jobs.
So consider using job check-pointing or, where possible, more
parallelism, to get job durations down to a few hours, or at worst,
days.

Leave some headroom for safety and run-to-run variability on the system
but try to be as accurate as possible.

If you have very many jobs of less than 5 minutes then they should
probably be combined into larger jobs using a simple loop in the batch
script so as to amortise the overheads of each job (starting, accounting
etc).

### Memory (RAM)

If you request more memory (RAM) than you need for your job, it [will
wait longer in the queue and will be more expensive when it
runs](https://support.nesi.org.nz/hc/en-gb/articles/360000737555). On
the other hand, if you don't request enough memory, the job may be
killed for attempting to exceed its allocated memory limits.

We recommend that you request a little more RAM, but not much more, than
your program will need at peak memory usage.

We also recommend using `--mem` instead of `--mem-per-cpu` in most
cases. There are a few kinds of jobs for which `--mem-per-cpu` is more
suitable. See [our article on how to request
memory](https://support.nesi.org.nz/hc/en-gb/articles/360001108756) for
more information.

### Parallelism

In general only MPI jobs should set *ntasks* greater than 1 or use
*srun*.  If you don't know whether your program supports MPI, it
probably doesn't.

Only multithreaded jobs should set *cpus-per-task*.  If you don't know
whether your program supports multithreading, try benchmarking with 2
CPUs and with 4 CPUs and see if there is a 2-fold difference in elapsed
job time.

[Job arrays](https://slurm.schedmd.com/job_array.html) are an efficient
mechanism of managing a collection of batch jobs with identical resource
requirements. Most Slurm commands can manage job arrays either as
individual elements (tasks) or as a single entity (e.g. delete an entire
job array in a single command)

### Fairshare

A low fairshare score will affect your jobs priority in the queue, learn
more about how to effectively use your allocation
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000205035).

### Cross machine submission

Jobs can be submitted from one machine to another by using the
`--cluster` option. E.g. submitting a job from Māui\_Ancil to Māui.

By default the environment (modules and variables) will be inherited
from the submitting shell into the job environment. But the environments
vary between our different machines, including module names, location of
slurm tools, etc., which could cause issues in this inheriting case. We
suggest to use the environment variable `SBATCH_EXPORT=NONE` (do NOT us
`--export=none` option) in the submitting shell. Therefore we suggest to
submit a job, e.g. to Māui using:

    SBATCH_EXPORT=NONE sbatch --cluster=maui job.sl

Please note: Above we only discussed the transition from your submitting
environment to the job environment. The latter is the one your job
script is running in. There is another environment created for your
parallel application (when called srun). There we want to inherit from
the job environment to have PATHs and setting available. Therefore,
avoid setting `SBATCH_EXPORT=NONE` in your job script or in .bashrc or
.profile for all cases. The slurm `--export=none` option would prevent
inhering environments in both transitions. Another note: Alternatively
you can set `SLURM_EXPORT_ENV=ALL` in your job script to enable the
environment forwarding to the srun environment.
