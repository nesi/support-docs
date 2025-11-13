---
created_at: '2019-02-24T23:26:19Z'
tags:
- slurm
- profiling
description: Information on Slurm native profiling
---

Job resource usage can be determined on job completion by checking the
following sacct columns;

- MaxRSS - Peak memory usage.
- TotalCPU - Check *Elapsed* x *Alloc*≈*TotalCPU*

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

The `profile_plot` command can then be used to generate an image with the results.

See `profile_plot --help` for more info.

Alternatively you could use one of the following scripts.

- [Python](https://github.com/nesi/nesi-tools/blob/main/.nn_profile_plot.py)
- [MATLAB](https://github.com/CallumWalley/slurm_native_h5_plotter)

Any GPU usage will also be recorded in the profile, so long as the
process was executed via *srun*.
