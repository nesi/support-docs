---
created_at: '2020-03-08T20:06:48Z'
hidden: false
tags: []
title: Job Checkpointing
vote_count: 2
vote_sum: 2
zendesk_article_id: 360001413096
zendesk_section_id: 360000030876
---


[Job/Application Checkpointing](https://en.wikipedia.org/wiki/Application_checkpointing) is
the capturing of a programs state, so that it can be restarted from
that point in case of failure. This is especially important in long
running jobs.

How checkpointing can be implemented depends on the application/code
being used, some will have inbuilt methods whereas others might require
some scripting.

## Queuing

Checkpointing code has the added advantage that it allows you to split
your work into smaller jobs, allowing them to move through the queue
faster.

Below is an example of submitting the same job again, if previous has
run successfully.

``` sl
# Slurm header #SBATCH etc etc

sbatch --dependency=afterok:${SLURM_JOB_ID} "$0" 
# "$0" is equal to the name of this script.

# Code that implements checkpointing
```

This job will resubmit itself forever until stopped.

Another example for a job requiring explicit step inputs.

```sl
# Slurm header '#SBATCH etc etc

n_steps=1000
starting_step=${1:-0} # Will be equal to first argument, or '0' if unset.
ending_step=$(( starting_step + n_steps )) 

# Submit next step with starting step equal to ending step of this job.
sbatch --dependency=afterok:${SLURM_JOB_ID} "$0" ${ending_step}

my-program --nfirst ${starting_step} --nlast ${ending_step}
```

The use of `--dependency` has the advantage of adding the next job to
the queue *before* starting, saving queue time in between jobs.

## Examples

### Matlab

``` m
% If checkpoint file, load from there.
checkpoint='checkpoint_2020-03-09T0916.mat';
if exist(checkpoint,'file')==2, load(checkpoint);startindex=i;else startindex=1;end

for i = startindex:100
    % Long running process

    % Save workspace at end of each loop.
    save(['checkpoint_', datestr(now, 'yyyy-mm-ddTHHMM')])
end
```

!!! tip
     We ***strongly*** recommend implementing checkpointing on any job
     running longer than 3 days!
