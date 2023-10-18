---
created_at: '2018-07-31T02:05:23Z'
hidden: true
label_names: []
position: 13
title: 'Slurm Usage: A Primer'
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000359576
zendesk_section_id: 360000030876
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
 !!! Info
     This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
## Slurm Scripts

Slurm scripts are text files you will need to create in order to submit
a job to the scheduler. Slurm scripts start with `#!/bin/bash` (with
optional flags) and contain a set of directives (which start with
`#SBATCH`), followed by commands.

    #!/bin/bash -e

    #SBATCH --job-name=JobName      # job name (shows up in the queue)
    #SBATCH --account=nesi99999     # Project Account
    #SBATCH --time=00:10:00         # Walltime (HH:MM:SS)
    #SBATCH --mem-per-cpu=4096      # memory/cpu (in MB)
    #SBATCH --ntasks=2              # number of tasks (e.g. MPI)
    #SBATCH --cpus-per-task=4       # number of cores per task (e.g. OpenMP)
    #SBATCH --partition=long        # specify a partition
    #SBATCH --hint=nomultithread    # don't use hyperthreading
    #SBATCH --output=%x-%j.out      # %x and %j are replaced by job name and ID
    #SBATCH --error=%x-%j.err
    #SBATCH --mail-type=ALL         # Optional: Send email notifications
    #SBATCH --mail-user=jbloggs@example.com     # Use with --mail-type option

    srun [options] <executable> [options]

We strongly recommend using `#!/bin/bash -e` instead of plain
`#!/bin/bash`, so that a command throwing an error will cause your job
to stop, instead of wasting your project's CPU core hours by continuing
to make use of potentially erroneous intermediate data.

There is a long list of different directives, you can  select your
requirements from. Please have a look to the manual page: `man sbatch`

There are various ways to specify the requirements, e.g. you could
request 1GB memory per node using `#``SBATCH --mem=1G` or you specify
the memory per core using `#SBATCH --mem-per-cpu=4096`

Not all directives need to be specified, just the ones you need.

## Commonly Used Slurm Environment variables

These can be useful within Slurm scripts:

-   `$SLURM_JOB_ID` (job id)
-   `$SLURM_NNODES` (number of nodes)
-   `$SLURM_NTASKS` (number of MPI tasks)
-   `$SLURM_CPUS_PER_TASK` (CPUs per MPI task)
-   `$SLURM_SUBMIT_DIR` (directory job was submitted from)
-   `$SLURM_ARRAY_JOB_ID` (job id for the array)
-   `$SLURM_ARRAY_TASK_ID` (job array index value)

## MPI and other distributed jobs

For MPI jobs you need to set `--ntasks` to a value larger than 1, or if
you want all nodes to run the same number of tasks, set
`--ntasks-per-node` and `--nodes` instead.

The Slurm command `srun` sets up the MPI runtime environment needed to
run a parallel program, launching it on multiple CPUs, which can be on
different nodes. `srun` is required for all MPI programs, and should be
used in place of any other MPI launcher such as `aprun` or `mpirun`.

## OpenMP and other multithreaded jobs

For multithreaded jobs you need to set `--cpus-per-task` to a value
larger than 1. Our Slurm prolog will then set OMP\_NUM\_THREADS to equal
that number.  If for any reason you use `srun` with a multi-core but
non-MPI job then also specify `--ntasks=1` to ensure that it is only
launched once.

## Submitting a job

Use `sbatch <script>` to submit the job. All Slurm directives can
alternatively be specified at the command line, e.g.
`sbatch --account=nesi12345 <script>`. This overwrites directives
specified in the script.

## Try submitting a simple job

Submit job `helloworld.sl`:

    #!/bin/bash -e
    #SBATCH --job-name=hello
    #SBATCH --time=00:02:00

    srun echo "Hello, World!"

with `sbatch --account=nesi12345 helloworld.sl` where nesi12345 is your
NeSI project’s code. If you only have one project then you don’t need to
specify it.

## Submitting a job using GPGPU nodes

To submit to the general purpose GPU nodes, you need to add the
following to your SLURM script:

    #SBATCH -p gpu
    #SBATCH --gres=gpu

## Submitting a job between Māui and Māui\_Ancil

Māui consists of the XC50 and the CS500 (Māui\_Ancil) part. To submit a
job from the XC50 part (including Māui login nodes) to the CS500 part
you need to add:

    #SBATCH --clusters=maui_ancil 
    #SBATCH -p nesi_prepost # another of its partions
    #SBATCH --export=NONE

Thus a prepost job submitted to the CS500 nodes from the Māui login node
would look like:

    #!/bin/bash -e
    #SBATCH --job-name=hello
    #SBATCH --time=00:02:00
    #SBATCH --clusters=maui_ancil 
    #SBATCH -p nesi_prepost
    #SBATCH --export=NONE

    module load Anaconda2
    python work_analysis.py

Note: the `--clusters` need to be also specified for the other slurm
tools to monitor other parts.

## Job array

A series of similar jobs can be arranged in a so called job array.
Therefore, the user tells slurm how many instances should be launched
(array size) and slurm provides environment variables to distinguish
between the different instances. For example the user could distinguish
different input files or directories. The following example prints a
hello world statement and the directory name from within 5
sub-directories:

    #!/bin/bash -e
    #SBATCH --job-name=arr_test
    #SBATCH --time=00:02:00
    #SBATCH --array=0-5

    cd inputDir${SLURM_ARRAY_TASK_ID}
    srun echo "Hello from ${SLURM_ARRAY_TASK_ID} of ${SLURM_ARRAY_TASK_COUNT} form $PWD"

More and detailed information can be found
[here](https://slurm.schedmd.com/job_array.html).

## Monitor jobs

You can use `squeue -u $USER` to monitor your job status. Alternatively
you can also use `sview`.

## Checking completed jobs with sacct

Another useful Slurm command is `sacct` which retrieves information
about completed jobs. For example:

    sacct -j 14309

where the argument passed to `-j` is the job ID, will show us something
like:

           JobID    JobName  Partition    Account  AllocCPUS      State ExitCode
    ------------ ---------- ---------- ---------- ---------- ---------- --------
    14309        problem.sh       NeSI  nesi99999         80  COMPLETED      0:0
    14309.batch       batch             nesi99999         80  COMPLETED      0:0
    14309.0         yourapp             nesi99999         80  COMPLETED      0:0

By default `sacct` will list all of your jobs which were (or are)
running on the current day. Each job will show as more than one line
(unless `-X` is specified): an initial line for the job as a whole, and
then an additional line for each job step, i.e.: the batch process which
is your executing script, and then each of the `srun` commands it
executes.

By changing the displayed columns you can gain information about the CPU
and memory utilisation of the job, for example

    sacct -j 14309 --format=jobid,jobname,elapsed,avecpu,totalcpu,alloccpus,maxrss,state

          JobID    JobName    Elapsed     AveCPU   TotalCPU  AllocCPUS     MaxRSS      State
    ------------ ---------- ---------- ---------- ---------- ---------- ---------- ----------
    14309        problem.sh   00:12:42             00:00.012         80             COMPLETED
    14309.batch       batch   00:12:42   00:00:00  00:00.012         80      1488K  COMPLETED
    14309.0         yourapp   00:12:41   00:12:03   16:00:03         80    478356K  COMPLETE

 
