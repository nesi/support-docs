Job resource usage can be determined on job completion by checking the
following sacct columns;

-   MaxRSS - Peak memory usage.
-   TotalCPU - Check *Elapsed* x *Alloc *≈*TotalCPU* 

However if you want to examine resource usage over the run-time of your
job,\
the line `#SBATCH --profile task` can be added to your SLURM header.

That will cause profile data to be recorded every 30 seconds throughout
the job. For jobs which take much less/more than a day to run we
recommend increasing/decreasing that sampling frequency, so for example
when profiling a job of less than 1 hour it would be OK to sample every
second by adding `#SBATCH --acctg-freq=1`, and for a week long job the
rate should be reduced to once every 5
minutes: `#SBATCH --acctg-freq=300`.\
\
On completion of your job, collate the data into an HDF5 file using the
command `sh5util -j <jobid>`, then contact us for help analysing the
data, or use one of these scripts for plotting the HDF5 data.  

-   [Python](https://github.com/nesi/slurm_native_h5_plotter_python)
-   [MATLAB](https://github.com/CallumWalley/slurm_native_h5_plotter)
