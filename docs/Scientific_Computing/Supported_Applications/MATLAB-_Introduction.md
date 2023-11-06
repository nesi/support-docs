---
created_at: '2018-11-21T03:32:30Z'
hidden: true
label_names: []
position: 36
title: 'MATLAB: Introduction'
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000577576
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>More general information can be found on MATLAB <a href="https://support.nesi.org.nz/hc/en-gb/articles/212639047-MATLAB">here.</a></p>
<h1>Setup</h1>
<p>Load MATLAB with the command.</p>
<pre><code>module load MATLAB</code></pre>
<p>Help can be found with</p>
<pre><code>matlab -nodisplay -help</code></pre>
<h1>X11 and -nodisplay</h1>
<p>By default MATALB will attempt to open a virtual desktop version of MATLAB, this will only work if X11 forwarding is enabled <code>-y</code>) and you have a suitable X11 application installed (MobaXterm, Xming, Quartz, Xorg).</p>
<hr>
<p>To run the desktop version of MATLAB enter:</p>
<pre><code>matlab</code></pre>
<p>This can be useful as an introduction for those not familiar with the command line environment, however this is <strong>not recommended</strong> as your primary method of running MATLAB<strong> </strong>as it is significantly slower than running with <code>-nodisplay</code> and does not help familiarize you with the commands necessary for submitting batch jobs.</p>
<p>Appending the command with;</p>
<pre><code>matlab -nodisplay</code></pre>
<p>Will force MATLAB to open as the command line version.</p>
<hr>
<h1>Running MATLAB interactively</h1>
<p>Using MATLAB interactively can be useful for testing but <strong>should not be used for large jobs</strong> (anything with multiple CPU's or multiple hours).</p>
<h2>CMD MATLAB</h2>
<p>To start the command line version of MATLAB run:</p>
<pre><code>matlab -nodisplay</code></pre>
<p>This will function identically to the Command Window in the desktop version of MATLAB.</p>
<h2><img src="https://support.nesi.org.nz/hc/article_attachments/360001327855"></h2>
<p>Enter 'quit' to leave the MATLAB session or ctrl + z to kill it.</p>
<h1>Running MATLAB batch jobs</h1>
<p>For your job to be submittable as a Slurm script you must be able to initiate it from the bash command line. This can be done in 2 ways.</p>
<h2>Piping</h2>
<p>A .m script can be piped into MATLAB using.</p>
<pre><code>matlab -nodisplay &lt; myScript.m</code></pre>
<p>This will open MATLAB then run your script. </p>
<h2>Functions</h2>
<p>MATLAB also accepts command window inputs using '-r'. Note ';' used for line-breaks.</p>
<pre><code>matlab -nodisplay -r "x=(1:10); y=(1:10); z=x'*y; disp(z);exit;"</code></pre>
<p>Will give the output</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360001330035"></p>
<p>then exit.</p>
<p>To run a function in the current directory.</p>
<pre><code>matlab -nodisplay -r "myFunction(15);"</code></pre>
<p>A script can also be run using this method.</p>
<pre><code>matlab -nodisplay -r "myScript;"</code></pre>
<h2>Paths</h2>
<p>By default only files in the same directory as you called MATLAB from will be included in the directory (no sub-directories).<br> A single directory can be added to path with;</p>
<pre><code>addpath('your_directory') </code></pre>
<pre><code>addpath(genpath('your_directory'))</code></pre>
<h2>Output</h2>
<p>Output from your job can be obtained multiple ways</p>
<h3>Terminal output</h3>
<p>The output of the terminal can be sent to a file using -logfile, e.g:</p>
<pre><code>matlab -nodisplay -r "myScript; exit;"</code></pre>
<p><em>Note: This is mostly made redundant by Slurm logs.</em></p>
<h3>MATLAB outputs</h3>
<p>Any outputs made from terminal output logging will be in plain-text meaning it may be more useful to create your output files inside your MATLAB code (e.g fprintf);</p>
<h3>Java.Log</h3>
<p>MATLAB also creates java.log files (generally useless) information about the job run. By default these will be created in your home directory, this can be changed by editing the environment variable MATLAB_LOG_DIR</p>
<p>e.g.</p>
<pre><code>export MATLAB_LOG_DIR=logs</code></pre>
<h2>Slurm</h2>
<p>Creating a file job.sl to add everything in the the parent directory 'parentDirectory' to the path and then run the function 'myFunction()'</p>
<pre><code>#!/bin/bash -e

#SBATCH --job-name MATLAB_test        #Name to appear in squeue<br>#SBATCH --time          06:00:00      #Max walltime
#SBATCH --mem-per-cpu   1500          #Max memory per <em>logical</em> core
#SBATCH --ntasks=1                    #No MPI
#SBATCH --output=%x_out.log           #Location of output log
#SBATCH --error=%x_error.err          #Location of error log

module load MATLAB<br>#OR specific version with;<br>#module load MATLAB/2017b

#Job run
matlab -nodisplay -r "addpath(genpath('../parentDirectory'));myFunction(5,20)"</code></pre>
<p> </p>
<p>This can then be submitted with</p>
<pre><code>sbatch job.sl</code></pre>
<p> </p>
<h2>Other stuff</h2>
<p>handy for deleting log files in your home directory</p>
<pre><code>rm java.log*</code></pre>