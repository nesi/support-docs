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
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p dir="auto">Job resource usage can be determined on job completion by checking the following sacct columns;</p>
<ul>
<li dir="auto">MaxRSS - Peak memory usage.</li>
<li dir="auto">TotalCPU - Check <em>Elapsed</em> x <em>Alloc </em>≈<em>TotalCPU</em> </li>
</ul>
<p dir="auto">However if you want to examine resource usage over the run-time of your job,<br> the line <code>#SBATCH --profile task</code> can be added to your SLURM header.</p>
<p>That will cause profile data to be recorded every 30 seconds throughout the job. For jobs which take much less/more than a day to run we recommend increasing/decreasing that sampling frequency, so for example when profiling a job of less than 1 hour it would be OK to sample every second by adding <code>#SBATCH --acctg-freq=1</code>, and for a week long job the rate should be reduced to once every 5 minutes: <code>#SBATCH --acctg-freq=300</code>.<br> <br> On completion of your job, collate the data into an HDF5 file using the command <code>sh5util -j &lt;jobid&gt;</code>, then contact us for help analysing the data, or use one of these scripts for plotting the HDF5 data.  </p>
<ul>
<li class="wysiwyg-indent1"><a href="https://github.com/nesi/slurm_native_h5_plotter_python" target="_self">Python</a></li>
<li class="wysiwyg-indent1"><a href="https://github.com/CallumWalley/slurm_native_h5_plotter" target="_self">MATLAB</a></li>
</ul>