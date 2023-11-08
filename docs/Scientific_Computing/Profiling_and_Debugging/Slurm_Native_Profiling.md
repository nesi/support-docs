---
created_at: '2019-02-24T23:26:19Z'
hidden: false
label_names:
- slurm
- profiling
position: 0
title: Slurm Native Profiling
vote_count: 4
vote_sum: 4
zendesk_article_id: 360000810616
zendesk_section_id: 360000278935
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

Job resource usage can be determined on job completion by checking the
following sacct columns;

-   MaxRSS - Peak memory usage.
-   TotalCPU - Check *Elapsed* x *Alloc *≈*TotalCPU* 

However if you want to examine resource usage over the run-time of your
job,  
the line `#SBATCH --profile task` can be added to your script.

That will cause profile data to be recorded every 30 seconds throughout
the job. For jobs which take much less/more than a day to run we
recommend increasing/decreasing that sampling frequency, so for example
when profiling a job of less than 1 hour it would be OK to sample every
second by adding `#SBATCH --acctg-freq=1`, and for a week long job the
rate should be reduced to once every 5
minutes: `#SBATCH --acctg-freq=300`.  
  
On completion of your job, collate the data into an HDF5 file using
`sh5util -j <jobid>`, this will collect the results from the nodes where
your job ran and write into an HDF5 file named: `job_<jobid>.h5`

You can plot the contents of this file with the command
`nn_profile_plot job_<jobid>.h5`, this will generate a file named
`job_<jobid>_profile.png`.

Alternatively you could use one of the following scripts. 

-   [Python](https://github.com/nesi/nesi-tools/blob/main/.dev_nn_profile_plot.py)
-   [MATLAB](https://github.com/CallumWalley/slurm_native_h5_plotter)

Any GPU usage will also be recorded in the profile, so long as the
process was executed via *srun*.
