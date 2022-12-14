---
created_at: '2019-01-07T01:10:28Z'
hidden: false
label_names:
- slurm
- scheduler
position: 1
title: Submitting your first job
vote_count: 6
vote_sum: 6
zendesk_article_id: 360000684396
zendesk_section_id: 360000189716
---

## Environment Modules

Modules are a convenient  way to provide access to applications  on the
cluster. They prepare the environment you need to run an application.

For a full list of module commands run <kbd>man module</kbd>

<table>
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

## Slurm

Jobs on Mahuika and Māui are submitted* *in the form of a *batch
script *containing the code you want to run and a header of information
needed by our job scheduler *Slurm.*

## Creating a batch script

Create a new file and open it with <kbd>nano myjob.sl</kbd>

    #!/bin/bash -e
    #SBATCH --job-name=SerialJob # job name (shows up in the queue)
    #SBATCH --time=00:01:00      # Walltime (HH:MM:SS)
    #SBATCH --mem=512MB          # Memory in MB
    #SBATCH --qos=debug          # debug QOS for high priority job tests

    pwd # Prints working directory

Copy in the above text and save and exit the text editor with 'ctrl +
x'.

Note:`#!/bin/bash`is expected by Slurm

Note: if you are a member of multiple accounts you should add the line
`#SBATCH --account=<projectcode>`

## Testing

We recommend testing your job using the debug Quality of Service (QOS). 
The debug QOS can be gained by adding the `sbatch` command line option
`--qos=debug`.  
This adds 5000 to the job priority so raises it above all non-debug
jobs, but is limited to one small job per user at a time: no more than
15 minutes and no more than 2 nodes.

> ### Warning
>
> Please do not run your code on the login node.  Any processes running
> on the login node for long periods of time or using large numbers of
> CPUs will be terminated.

## Submitting

Jobs are submitted to the scheduler using:

    sbatch myjob.sl

You should receive an output

Submitted batch job 1748836

`sbatch`can take command line arguments similar to those used in the
shell script through SBATCH pragmas

You can find more details on its use on the [Slurm
Documentation](https://slurm.schedmd.com/sbatch.html)

## Job Queue

The currently queued jobs can be checked using 

    squeue

You can filter to just your jobs by adding the flag

    squeue -u usr9999

You can also filter to just your jobs using

    squeue --me

You can find more details on its use on the [Slurm
Documentation](https://slurm.schedmd.com/squeue.html)

You can check all jobs submitted by you in the past day using:

    sacct

Or since a specified date using:

    sacct -S YYYY-MM-DD

Each job will show as multiple lines, one line for the parent job and
then additional lines for each job step.

> ### Tips
>
> <kbd>sacct -X</kbd> Only show parent processes.
>
> <kbd>sacct --state=PENDING/RUNNING/FAILED/CANCELLED/TIMEOUT</kbd>
> Filter jobs by state.

You can find more details on its use on the [Slurm
Documentation](https://slurm.schedmd.com/sacct.html)

##  Cancelling

<kbd>scancel &lt;jobid&gt;</kbd> will cancel the job described by
<kbd>&lt;jobid&gt;</kbd>. You can obtain the job ID by using
<kbd>sacct</kbd> or <kbd>squeue</kbd>.

> ### Tips
>
> <kbd>scancel -u \[username\]</kbd> Kill all jobs submitted by you.
>
> <kbd>scancel {\[n1\]..\[n2\]}</kbd> Kill all jobs with an id between
> <kbd>\[n1\]</kbd> and <kbd>\[n2\]</kbd>

You can find more details on its use on the [Slurm
Documentation](https://slurm.schedmd.com/scancel.html)

## Job Output

When the job completes, or in some cases earlier, two files will be
added to the directory in which you were working when you submitted the
job:

`slurm-[jobid].out` containing standard output.

`slurm-[jobid].err` containing standard error.
