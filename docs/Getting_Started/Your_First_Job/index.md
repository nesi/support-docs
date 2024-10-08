---
created_at: '2019-01-07T01:10:28Z'
tags:
- slurm
- scheduler
vote_count: 8
vote_sum: 8
zendesk_article_id: 360000684396
zendesk_section_id: 360000189716
---

# File Transfer

## Software

One of the first things you will need to do once you have access to the cluster will be finding, or installing the software you require for your research, the most straightforward way is through the use of [Environment Modules](link to page)

## Slurm

Jobs on Mahuika and Māui are submitted in the form of a *batch script* containing the code you want to run and a header of information needed by our job scheduler *Slurm*.

## Creating a batch script

Create a new file and open it with `nano myjob.sl`

```sl
#!/bin/bash -e
#SBATCH --job-name=SerialJob # job name (shows up in the queue)
#SBATCH --time=00:01:00      # Walltime (HH:MM:SS)
#SBATCH --mem=512MB          # Memory in MB
#SBATCH --qos=debug          # debug QOS for high priority job tests

pwd # Prints working directory
```

Copy in the above text and save and exit the text editor with 'ctrl + x'.

Note: `#!/bin/bash` is expected by Slurm.

Note: if you are a member of multiple accounts you should add the line

```sl
#SBATCH --account=<projectcode>
```

## Testing

We recommend testing your job using the debug Quality of Service (QOS).
The debug QOS can be gained by adding the `sbatch` command line option `--qos=debug`.  
This adds 5000 to the job priority so raises it above all non-debug jobs, but is limited to one small job per user at a time: no more than 15 minutes and no more than 2 nodes.

!!! warning
    Please do not run your code on the login node.
    Any processes running on the login node for long periods of time or using large numbers of CPUs will be terminated.

## Submitting

Jobs are submitted to the scheduler using:

```bash
sbatch myjob.sl
```

You should receive an output

Submitted batch job 1748836

`sbatch` can take command line arguments similar to those used in the shell script through SBATCH pragmas

You can find more details on its use on the [Slurm Documentation](https://slurm.schedmd.com/sbatch.html)

## Job Queue

The currently queued jobs can be checked using

```bash
squeue
```

You can filter to just your jobs by adding the flag

```bash
squeue -u usr9999
```

You can also filter to just your jobs using

```bash
squeue --me
```

You can find more details on its use on the [Slurm Documentation](https://slurm.schedmd.com/squeue.html).

You can check all jobs submitted by you in the past day using:

```bash
sacct
```

Or since a specified date using:

```bash
sacct -S YYYY-MM-DD
```

Each job will show as multiple lines, one line for the parent job and then additional lines for each job step.

!!! tip
    - `sacct -X` Only show parent processes.
    - `sacct --state=PENDING/RUNNING/FAILED/CANCELLED/TIMEOUT` Filter jobs by state.

You can find more details on its use on the [Slurm Documentation](https://slurm.schedmd.com/sacct.html).

## Cancelling

`scancel <jobid>` will cancel the job described by `<jobid>`.
You can obtain the job ID by using `sacct` or `squeue`.

!!! tip
    - `scancel -u [username]` Kill all jobs submitted by you.
    - `scancel {[n1]..[n2]}` Kill all jobs with an id between `[n1]` and `[n2]`.

You can find more details on its use on the [Slurm Documentation](https://slurm.schedmd.com/scancel.html).

## Job Output

When the job completes, or in some cases earlier, two files will be
added to the directory in which you were working when you submitted the
job:

`slurm-[jobid].out` containing standard output.

`slurm-[jobid].err` containing standard error.
