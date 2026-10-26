---
created_at: 2026-10-15
description: Split a Slurm job into parts with their own resources, make each wait for the one before with --dependency, and queue a whole workflow from one script.
status: tutorial
tags:
- tutorial
- slurm
- workflow
---

!!! time "45 Minutes"

!!! objectives
    - Split a job into parts that each request only the resources they need.
    - Make a job wait for another job with `--dependency`.
    - Queue a whole workflow from one submission script.

!!! prerequisite
    - You can find why a job failed. See [Debugging Failed Jobs](Debugging_Failed_Jobs.md).
    - The profile from [Evaluating Job Efficiency](Evaluating_Job_Efficiency.md) is the starting point for the split.

??? info "Skipped ahead? Set up here"
    Follow the setup steps in [Evaluating Job Efficiency](Evaluating_Job_Efficiency.md#setup) to get the example files.
    This lesson starts from the step scripts at the end of [Debugging Failed Jobs](Debugging_Failed_Jobs.md).

## Split by resource needs

The steps of `pipeline.sl` have different resource needs:

1. Quality control
2. Indexing the reference genome
3. Alignment and variant calling

Since [Using Variables](Using_Variables.md), each step is already a script of its own, but `pipeline.sl` still runs them all in one job,
holding 4 CPUs, 5 GB and 4 hours for every step.

!!! question "Splitting tasks by resource needs"
    Let's give each step script (`qc.sh`, `index.sh` and `align.sh`) an appropriate resource request,
    based on the profile from [Evaluating Job Efficiency](Evaluating_Job_Efficiency.md), so each can run as a separate job.

??? question "Solution: updated scripts"
    There is no one correct answer here! But here is one option.
    The profile plot in [Evaluating Job Efficiency](Evaluating_Job_Efficiency.md#reviewing-our-job-script) shows the steps of the job:
    quality control first, a short blip that is probably indexing the reference genome, then alignment and variant calling.

    So we can give the three scripts better resource requests. Each now runs for one sample at a time,
    and writes its output to `log/`, like `pipeline.sl` after [Debugging Failed Jobs](Debugging_Failed_Jobs.md).

    **Quality control**:`qc.sh` requests fewer CPUs, less memory and much less time.

    ```bash
    --8<-- "docs/assets/workshops/hpc102/.qc_1.sh"
    ```

    **Reference genome indexing**: `index.sh` requests less CPUs, memory, and time.

    ```bash
    --8<-- "docs/assets/workshops/hpc102/.index_1.sh"
    ```

    **Alignment and variant calling**: `align.sh` requests the same CPUs but less memory and time.

    ```bash
    --8<-- "docs/assets/workshops/hpc102/.align_2.sh"
    ```

Quality control requests two CPUs, indexing one, and alignment four.
Indexing doesn't need the results of quality control either, so those two jobs can run at the same time.

<!-- Write: re-record these three plots with one sample's jobs from submit.sh, and update the text below to match. -->

Here are the profile plots of the three steps, run as jobs `{{ intermediate_hpc_job_id_03a }}`,
`{{ intermediate_hpc_job_id_03b }}` and `{{ intermediate_hpc_job_id_03c }}`:

![Profile plot for job {{ intermediate_hpc_job_id_03a }}, quality control. CPU use is one, then about three while trimming. Memory peaks at about 2 GB.](../../assets/images/intermediate_hpc_profile_plot_03a.png)

![Profile plot for job {{ intermediate_hpc_job_id_03b }}, indexing the reference genome, which takes only a few seconds.](../../assets/images/intermediate_hpc_profile_plot_03b.png)

![Profile plot for job {{ intermediate_hpc_job_id_03c }}, alignment and variant calling. CPU use is mostly one, with short spikes to about four. Memory peaks at about 1.5 GB.](../../assets/images/intermediate_hpc_profile_plot_03c.png)

Once each script has run, check it with `seff` and adjust its request, leaving 20 to 30% spare as in the
[Introduction to HPC](../Introduction_To_HPC/Resources.md).

## Read and write less

The profile plot showed reading and writing files growing steadily through alignment.
For each sample, `align.sh` writes a `.sam` file (`${sam}`), converts it to a `.bam` file (`${bam}`), then sorts that into another (`${sorted_bam}`).
Only the sorted file is used afterwards.

!!! question "Skip the intermediate files"
    `samtools sort` can read from a pipe (`|`) as well as from a file.
    How could the alignment write straight into `samtools sort`, without the `.sam` and unsorted `.bam` files?

??? question "Solution"
    Pipe `bwa-mem2` into `samtools sort`, which reads from the pipe when given `-` as its input file:

    ```bash
    bwa-mem2 mem -t ${SLURM_CPUS_PER_TASK} ${ref_genome} ${fq1} ${fq2} \
        | samtools sort -@ ${SLURM_CPUS_PER_TASK} -m 256M -o ${sorted_bam} -
    ```

    Both commands now run at the same time, so the job needs more memory.
    In our tests this step used up to about 2.5 GB, so request `--mem 3G`.

For large temporary files, see also [Temporary Directories](../../Batch_Computing/Temporary_Directories.md).

## Make a job wait for another

Alignment can only start once quality control and indexing have finished.
Rather than waiting to submit `align.sh` by hand, we can submit it straight away and tell Slurm to wait, with `--dependency`:

```sh
sbatch --dependency afterok:JOB_ID align.sh
```

Replace `JOB_ID` with the job ID of the job to wait for.
To wait for more than one job, separate the job IDs with `:`, for example `afterok:JOB_ID_1:JOB_ID_2`.

The condition decides what the job waits for:

| Condition | The job can start when the listed jobs have |
| --------- | ------------------------------------------- |
| `afterok` | finished successfully. |
| `afternotok` | finished in a failed state. |
| `afterany` | finished, in any state. |
| `after` | started. |

If a job you depend on fails, a job waiting with `afterok` can never run, and Mahuika cancels it.

<quiz>
<p class=admonition-title>Dependencies</p>

Job `1001` is running and job `1002` has failed. Which of these jobs can start once their dependency is checked?

- [x] `--dependency after:1001`
> `after` only needs job `1001` to have started.
- [] `--dependency afterok:1002`
> Job `1002` failed, so this job can never start. Mahuika cancels it.
- [x] `--dependency afternotok:1002`
> `afternotok` waits for the job to fail, which it has.
- [] `--dependency afterok:1001`
> Job `1001` is still running. This job waits until it finishes successfully.
</quiz>

## Queue a whole workflow

`sbatch --parsable` prints only the job ID, so a script can save it and use it in the next submission.
This submission script indexes the reference genome once, then submits quality control and alignment for each sample.
Each alignment job waits for its own sample's quality control, and for indexing:

```sh
--8<-- "docs/assets/workshops/hpc102/.submit_1.sh"
```

Save it as `submit.sh` next to the three scripts and `samples.txt`, and run it on the login node with `bash submit.sh`.
It only submits the jobs, so it finishes straight away.
`squeue --me` then shows the alignment jobs waiting, with the reason `(Dependency)`, until the jobs they depend on have finished.

!!! question "Why queue every step at once?"
    What is gained by submitting the later steps straight away, rather than waiting to submit them by hand?

??? question "Solution"
    Each step can start as soon as the steps it depends on have succeeded, without you being there to submit it.
    The whole workflow runs from one command.

For three samples, that is seven jobs, each with its own job ID. With hundreds of samples, it soon becomes hard to manage.
The next lesson runs each step for every sample as a single job array.

!!! keypoints
    - Split a job where its parts need different resources.
    - `--dependency afterok:JOB_ID` makes a job wait for another to finish successfully.
    - `sbatch --parsable` gives the job ID, so a script can queue a whole workflow.

!!! postrequisite "What next"
    - Next lesson: [Job Arrays](Job_Arrays.md).
    - For reference: [Job Dependencies](../../Batch_Computing/Job_Dependencies.md)
      and [Temporary Directories](../../Batch_Computing/Temporary_Directories.md).
