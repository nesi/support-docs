Environment Modules
-------------------

[Modules are a convenient  way to provide access to applications  on the
cluster. They prepare the environment you need to run an
application.]{style="font-weight: 400;"}

[For a full list of module commands run [man
module]{.kbd}]{style="font-weight: 400;"}

  ------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `module spider [ <string> ]`   List all modules whose names, including version strings, contain `<string>`. If the `<string>` argument is not supplied, list all available modules. (only on Mahuika)
  `module show <string>`         Show the contents of the module given by `<string>`. If only the module name (e.g. `Python`) is given, show the default module of that name. If both name and version are given, show that particular version module.
  `module load <string>`         Load the module (name and version) given by `<string>`. If no version is given, load the default version.
  `module list [ <string> ]`     List all currently loaded modules whose names, including version strings, contain `<string>`. If the `<string>` argument is not supplied, list all currently loaded modules.
  ------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Testing
-------

Before submitting a job to the scheduler it is good practice to run a
small test of your code first to confirm there are no errors.

You are allowed to use the login node for this purpose, provided the
resource usage is minimal.

> ### Warning
>
> Jobs running on the login node for long periods of time or using large
> numbers of CPUs will be killed.

Slurm
-----

Jobs on Mahuika and Māui are submitted* *in the form of a *[batch
script ]{style="font-weight: 400;"}*[containing the code you want to run
and a header of information needed by our job scheduler
*Slurm.*]{style="font-weight: 400;"}

Creating a batch script
-----------------------

Create a new file and open it with [nano myjob.sl]{.kbd}

    #!/bin/bash -e
    #SBATCH --job-name=SerialJob # job name (shows up in the queue)
    #SBATCH --time=00:01:00      # Walltime (HH:MM:SS)
    #SBATCH --mem=512MB          # Memory in MB


    pwd # Prints working directory

Copy in the above text and save and exit the text editor with \'ctrl +
x\'.

Note: if you are a member of multiple accounts you should add the line
`#SBATCH --account=<projectcode>`

Submitting
----------

Jobs are submitted to the scheduler using:

    sbatch myjob.sl

You should receive an output 

`Submitted batch job 1748836`

Job Queue
---------

The currently queued jobs can be checked using 

    squeue

You can filter to just your jobs by adding the flag

    squeue -u usr9999

where \'usr9999\' is replaced with your username.

You can check all jobs submitted by you in the past day using:

    sacct

Or since a specified date using:

    sacct -S YYYY-MM-DD

Each job will show as multiple lines, one line for the parent job and
then additional lines for each job step.

> ### Tips {#prerequisites}
>
> [sacct -X]{.kbd} Only show parent processes.
>
> [sacct \--state=PENDING/RUNNING/FAILED/CANCELLED/TIMEOUT]{.kbd} Filter
> jobs by state.

Cancelling
----------

[scancel \<jobid\>]{.kbd} will cancel the job described by
[\<jobid\>]{.kbd}. You can obtain the job ID by using [sacct]{.kbd} or
[squeue]{.kbd}.

> ### Tips {#prerequisites}
>
> [scancel -u \[username\]]{.kbd} Kill all jobs submitted by you.
>
> [scancel {\[n1\]..\[n2\]}]{.kbd} Kill all jobs with an id between
> [\[n1\]]{.kbd} and [\[n2\]]{.kbd}

Job Output
----------

When the job completes, or in some cases earlier, two files will be
added to the directory in which you were working when you submitted the
job:

`slurm-[jobid].out` containing standard output.

`slurm-[jobid].err` containing standard error.
