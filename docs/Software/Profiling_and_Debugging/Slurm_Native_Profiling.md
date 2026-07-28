---
created_at: '2019-02-24T23:26:19Z'
tags:
- slurm
- profiling
---

Job resource usage can be determined on job completion by checking the
following `sacct` columns;

- MaxRSS - Peak memory usage.
- TotalCPU - Check: *Elapsed* x *Alloc*≈*TotalCPU*

However if you want to examine resource usage over the run-time of your
job,  
the line `#SBATCH --profile task` can be added to your script.

That will cause profile data to be recorded every 30 seconds throughout
the job. For jobs which take much less than a day to run we
recommend increasing that sampling frequency, so for example
when profiling a job of less than 1 hour it would be OK to sample every
second by adding `#SBATCH --acctg-freq=1`.

The `profile_plot` command can then be used to generate an image with the results.
`profile_plot <jobid>` will produce `<jobid>_profile.png`.  
See `profile_plot --help` for its options.

We keep the profile data for at least 30 days. Profiles older than that may 
be deleted or incomplete.

