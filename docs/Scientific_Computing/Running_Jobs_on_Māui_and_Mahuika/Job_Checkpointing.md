Job/[Application
Checkpointing](https://en.wikipedia.org/wiki/Application_checkpointing) is
the snapshotting of a programs state, so that it can be restarted from
that point in case of failure. This is especially important in long
running jobs.

How checkpointing can be implemented depends on the application/code
being used, some will have inbuilt methods whereas others might require
some scripting.

Queueing 
=========

Checkpointing code has the added advantage that it allows you to split
your work into smaller jobs, allowing them to move through the queue
faster. 

Below is an example of submitting the same job again, if previous has
run successfully.

    # Slurm header '#SBATCH etc etc

    sbatch --dependency=afterok:${SLURM_JOB_ID} "slurm_script.sl"

    # Code that implements checkpointing

This has the advantage of adding the next job to the queue *before*
starting, saving queue time in between jobs.

Examples
========

Matlab
------

    % If checkpoint file, load from there.
    checkpoint='checkpoint_2020-03-09T0916.mat';
    if exist(checkpoint,'file')==2, load(checkpoint);startindex=i;else startindex=1;end

    for i = startindex:100
        % Long running process

        % Save workspace at end of each loop.
        save(['checkpoint_', datestr(now, 'yyyy-mm-ddTHHMM')])
    end

 

> ### Tip {#prerequisites}
>
> We ***strongly*** recommend implementing checkpointing on any job
> running longer than 3 days!
