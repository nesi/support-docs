---
created_at: 2026-10-13
description: How to make a Slurm job wait for other jobs with --dependency, run the stages of a workflow in order, and resubmit failed job array tasks.
tags:
    - slurm
    - workflow
---

!!! prerequisite
    - You can write and submit a batch script. If not, start with [Submitting Your First Job](../Tutorials/Introduction_To_HPC/Submitting_Your_First_Job.md).

A job dependency tells Slurm not to start a job until other jobs have reached a given state, for example finished successfully.
Use dependencies to run the stages of a workflow in order, without waiting for each stage to finish before you submit the next.
The dependent job is queued straight away, and becomes eligible to start as soon as its dependency is met.

## Add a dependency

Give `--dependency` a condition and the job ID of the job to wait for, either on the command line:

```sh
sbatch --dependency afterok:JOB_ID second_job.sl
```

or in the header of the batch script:

```sh
#SBATCH --dependency afterok:JOB_ID
```

Replace `JOB_ID` with the ID of the job to wait for, as output by `sbatch`, or by `squeue --me`.

The condition decides what the job waits for:

| Condition | The job can start when the listed jobs have |
| --------- | ------------------------------------------- |
| `afterok:JOB_ID` | finished successfully (exit code zero). |
| `afternotok:JOB_ID` | finished in a failed state (non-zero exit code, timed out, node failure, and so on). |
| `afterany:JOB_ID` | finished, in any state. |
| `after:JOB_ID` | started, or been cancelled. |
| `aftercorr:JOB_ID` | For job arrays only: each task can start when the task with the same index in the listed array has finished successfully. |
| `singleton` | finished, for all your earlier jobs with the same `--job-name`. Only one of your jobs with that name runs at a time. |

To combine conditions:

- **Several jobs:** separate the job IDs with `:`. `afterok:JOB_ID_1:JOB_ID_2` waits for both jobs to finish successfully.
- **All of several conditions:** separate them with `,`. `afterok:JOB_ID_1,afterany:JOB_ID_2` waits for job 1 to succeed and job 2 to finish.
- **Any one of several conditions:** separate them with `?`. `afterok:JOB_ID_1?afterok:JOB_ID_2` waits for either job to succeed.

Use only one kind of separator, `,` or `?`, in a dependency.

!!! warning "Dependencies that can never be met"
    If a job your job depends on ends in the wrong state, for example `afterok` on a job that failed, **your job will never run**,
    even if the failed job is run again and then succeeds.
    It may stay in the queue, pending with the reason `DependencyNeverSatisfied`, until you cancel it.
    Add `--kill-on-invalid-dep=yes` to have Slurm cancel it instead.

Submit a job with `afterok` or `afternotok` while the job it depends on is still queued or running, or soon after it ends.
Slurm only keeps a record of finished jobs for a short time, after which it can no longer check them.

## Get the job ID

`sbatch --parsable` prints only the job ID, so you can save it in a variable and use it in the next submission:

```sh
first=$(sbatch --parsable first_job.sl)
sbatch --dependency afterok:${first} second_job.sl
```

## Submit from inside a job

A batch script can submit the job that follows it, using its own job ID from `SLURM_JOB_ID`:

```sh
sbatch --dependency afterok:${SLURM_JOB_ID} second_job.sl
```

Put this line near the **start of the first script**, so the second job is queued while the first one runs.
For a job that resubmits itself to continue long work, see [Job Checkpointing](Job_Checkpointing.md).

## Run a workflow

A short submission script can queue every stage of a workflow at once, each stage waiting for the one before.
This example prepares the inputs, processes them in a [job array](Job_Arrays.md), then combines the results:

```sh
#!/bin/bash -e

# Queue each stage of the workflow. Each one waits for the stage before.
prepare=$(sbatch --parsable prepare.sl)
process=$(sbatch --parsable --dependency afterok:${prepare} process.sl)
sbatch --dependency afterok:${process} combine.sl
```

Save it as `submit_workflow.sh` and run it on the login node with `bash submit_workflow.sh`.
It only submits the jobs, so it finishes straight away. The stages then run in order as each one finishes successfully.

When the job you depend on is a job array, `afterok` waits for every task in the array to finish successfully.
If the next stage is also an array, with the same indices, `aftercorr` starts each task as soon as the matching task finishes,
without waiting for the whole array:

```sh
sbatch --dependency aftercorr:${process} postprocess.sl
```

## Resubmit failed array tasks

When some tasks in a job array fail, for example because a few inputs need more memory, you can rerun just those tasks.
For a job array, `afternotok` is met once every task has finished and at least one of them failed.
A small follow-up job with that dependency can look up the failed tasks and resubmit them with more memory.

Save this script as `resubmit_failed.sh`. It finds the tasks of the job array that failed, ran out of memory or timed out,
and resubmits only those tasks of `process.sl`, with 4 GB of memory:

```sh
#!/bin/bash -e

# Find the failed tasks of the job array with ID $1, as a list like "3,17,42".
failed=$(sacct --jobs "$1" --array --allocations --noheader \
    --parsable2 --format JobID,State |
    grep -E 'FAILED|OUT_OF_MEMORY|TIMEOUT' |
    cut -d '|' -f 1 | cut -d '_' -f 2 | paste -sd ,)

if [ -n "${failed}" ]; then
    sbatch --array "${failed}" --mem 4G process.sl
fi
```

Then submit the job array, followed by a follow-up job that only runs if some of its tasks failed:

```sh
array=$(sbatch --parsable process.sl)
sbatch --dependency afternotok:${array} --job-name resubmit \
    --time 00:05:00 --mem 512M --wrap "bash resubmit_failed.sh ${array}"
```

`--wrap` submits a single command as a job, without a batch script.
Options given on the `sbatch` command line override the same options in the script's header,
so the resubmitted tasks use the new `--array` and `--mem`.
If any resubmitted task fails again, nothing more happens, so check the results with `sacct`.

See the Slurm documentation for more on [`--dependency`](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/sbatch.html#OPT_dependency)
and [dependencies on job arrays](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/job_array.html#dependencies).
