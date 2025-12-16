---
created_at: '2020-03-08T20:06:48Z'
tags:
  - slurm
description: How to impliment checkpointing on the REANNZ HPC
---

!!! tip
     We recommend implementing checkpointing on any job
     running longer than a day!

[Job/Application Checkpointing](https://en.wikipedia.org/wiki/Application_checkpointing) is
the capturing of a programs state, so that it can be restarted from
that point in case of failure. This is especially important in long
running jobs.

How checkpointing can be implemented depends on the application/code
being used, some will have inbuilt methods whereas others might require
some scripting.

!!! warning
    Checkpointing may add to the runtime of a job, especially if you are using large amounts of memory.

Before implementing checkpointing consider

- Possible additional runtime.
- Length of the job being checkpointed.
- Time taken to implement checkpointing.
- How many times you will reuse this method.

The application specific documentation should be the first place you look when trying to implement checkpointing!

## Queuing

Checkpointing code has the added advantage that it allows you to split
your work into smaller jobs, allowing them to move through the queue
faster, and **allows you to run work for longer than the job maximum time limit**.

This can be most easily implemented by splitting the work into smaller chunks,
then in your script loading and saving to disk at the start and end of the job respectively.

Below is an example of submitting the same job again, if previous has
run successfully.

``` sh
# Slurm header #SBATCH etc etc

sbatch --dependency=afterok:${SLURM_JOB_ID} "$0" 
# "$0" is equal to the name of this script.

# Read data from disk

# Do work

# Write data back to disk.
```

This job will resubmit itself **forever** until stopped

If writing your own code, you could exit with a non-zero code once all the work has been done.

<!-- Another example for a job requiring explicit step inputs.

```sl
# Slurm header '#SBATCH etc etc

n_steps=1000
starting_step=${1:-0} # Will be equal to first argument, or '0' if unset.
ending_step=$(( starting_step + n_steps )) 

# Submit next step with starting step equal to ending step of this job.
sbatch --dependency=afterok:${SLURM_JOB_ID} "$0" ${ending_step}

my-program --nfirst ${starting_step} --nlast ${ending_step}
``` -->

The use of `--dependency` has the advantage of adding the next job to
the queue *before* starting, saving queue time in between jobs.

## Examples

- [ANSYS](../Software/Available_Applications/ANSYS.md#checkpointing)
- [MATLAB](../Software/Available_Applications/MATLAB.md#checkpointing)
- [GROMACS](../Software/Available_Applications/GROMACS.md#checkpointing)
- [ORCA](../Software/Available_Applications/ORCA.md#checkpointing)
