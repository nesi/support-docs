---
created_at: '2018-07-31T02:05:23Z'
hidden: true
label_names: []
position: 13
title: 'Slurm Usage: A Primer'
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000359576
zendesk_section_id: 360000030876
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<h2 id="where-to-build">Slurm Scripts</h2>
<p>Slurm scripts are text files you will need to create in order to submit a job to the scheduler. Slurm scripts start with <code class="highlighter-rouge"><span class="c">#!/bin/bash</span></code> (with optional flags) and contain a set of directives (which start with <code class="highlighter-rouge">#SBATCH</code>), followed by commands.</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code><span class="c">#!/bin/bash -e<br></span>
<span class="c">#SBATCH --job-name=JobName      # job name (shows up in the queue)</span>
<span class="c">#SBATCH --account=nesi99999     # Project Account</span>
<span class="c">#SBATCH --time=00:10:00         # Walltime (HH:MM:SS)</span>
<span class="c">#SBATCH --mem-per-cpu=4096      # memory/cpu (in MB)</span>
<span class="c">#SBATCH --ntasks=2              # number of tasks (e.g. MPI)</span>
<span class="c">#SBATCH --cpus-per-task=4       # number of cores per task (e.g. OpenMP)</span>
<span class="c">#SBATCH --partition=long        # specify a partition</span>
<span class="c">#SBATCH --hint=nomultithread    # don't use hyperthreading<br></span>#SBATCH --output=%x-%j.out      # %x and %j are replaced by job name and ID<br>#SBATCH --error=%x-%j.err<br>#SBATCH --mail-type=ALL         # Optional: Send email notifications<br>#SBATCH --mail-user=jbloggs@example.com     # Use with --mail-type option

srun <span class="o">[</span>options] &lt;executable&gt; <span class="o">[</span>options]
</code></pre>
</div>
</div>
<p>We strongly recommend using <code class="highlighter-rouge">#!/bin/bash -e</code> instead of plain <code class="highlighter-rouge">#!/bin/bash</code>, so that a command throwing an error will cause your job to stop, instead of wasting your project's CPU core hours by continuing to make use of potentially erroneous intermediate data.</p>
<p>There is a long list of different directives, you can  select your requirements from. Please have a look to the manual page: <code class="highlighter-rouge">man sbatch</code></p>
<p>There are various ways to specify the requirements, e.g. you could request 1GB memory per node using <code class="highlighter-rouge">#<code><span class="c">SBATCH --mem=1G</span></code></code> or you specify the memory per core using <code><span class="c">#SBATCH --mem-per-cpu=4096</span></code></p>
<p>Not all directives need to be specified, just the ones you need.</p>
<h2 id="where-to-build">Commonly Used Slurm Environment variables</h2>
<p>These can be useful within Slurm scripts:</p>
<ul>
<li>
<code class="highlighter-rouge">$SLURM_JOB_ID</code> (job id)</li>
<li>
<code class="highlighter-rouge">$SLURM_NNODES</code> (number of nodes)</li>
<li>
<code class="highlighter-rouge">$SLURM_NTASKS</code> (number of MPI tasks)</li>
<li>
<code class="highlighter-rouge">$SLURM_CPUS_PER_TASK</code> (CPUs per MPI task)</li>
<li>
<code class="highlighter-rouge">$SLURM_SUBMIT_DIR</code> (directory job was submitted from)</li>
<li>
<code class="highlighter-rouge">$SLURM_ARRAY_JOB_ID</code> (job id for the array)</li>
<li>
<code class="highlighter-rouge">$SLURM_ARRAY_TASK_ID</code> (job array index value)</li>
</ul>
<h2 id="where-to-build">MPI and other distributed jobs</h2>
<p>For MPI jobs you need to set <code class="highlighter-rouge">--ntasks</code> to a value larger than 1, or if you want all nodes to run the same number of tasks, set <code class="highlighter-rouge">--ntasks-per-node</code> and <code class="highlighter-rouge">--nodes</code> instead.</p>
<p>The Slurm command <code class="highlighter-rouge">srun</code> sets up the MPI runtime environment needed to run a parallel program, launching it on multiple CPUs, which can be on different nodes. <code class="highlighter-rouge">srun</code> is required for all MPI programs, and should be used in place of any other MPI launcher such as <code class="highlighter-rouge">aprun</code> or <code class="highlighter-rouge">mpirun</code>.</p>
<h2 id="where-to-build">OpenMP and other multithreaded jobs</h2>
<p><span class="wysiwyg-font-size-medium">For multithreaded jobs you need to set <code class="highlighter-rouge">--cpus-per-task</code> to a value larger than 1. Our Slurm prolog will then set OMP_NUM_THREADS to equal that number.  If for any reason you use <code class="highlighter-rouge">srun</code> with a multi-core but non-MPI job then also specify <code class="highlighter-rouge">--ntasks=1</code> to ensure that it is only launched once.</span></p>
<h2 id="submitting-a-job">Submitting a job</h2>
<p>Use <code class="highlighter-rouge">sbatch &lt;script&gt;</code> to submit the job. All Slurm directives can alternatively be specified at the command line, e.g. <code class="highlighter-rouge">sbatch --account=nesi12345 &lt;script&gt;</code>. This overwrites directives specified in the script.</p>
<h2 id="try-submitting-a-simple-job">Try submitting a simple job</h2>
<p>Submit job <code class="highlighter-rouge">helloworld.sl</code>:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code><span class="c">#!/bin/bash -e</span>
<span class="c">#SBATCH --job-name=hello</span>
<span class="c">#SBATCH --time=00:02:00</span>

srun <span class="nb">echo</span> <span class="s2">"Hello, World!"</span>
</code></pre>
</div>
</div>
<p>with <code class="highlighter-rouge">sbatch --account=nesi12345 helloworld.sl</code> where nesi12345 is your NeSI project’s code. If you only have one project then you don’t need to specify it.</p>
<p><code></code><code></code></p>
<p><code></code></p>
<h2>Submitting a job using GPGPU nodes</h2>
<p>To submit to the general purpose GPU nodes, you need to add the following to your SLURM script:</p>
<pre class="highlight"><code><span class="c">#SBATCH -p gpu<br>#SBATCH --gres=gpu</span></code></pre>
<h2>Submitting a job between Māui and Māui_Ancil</h2>
<p>Māui consists of the XC50 and the CS500 (Māui_Ancil) part. To submit a job from the XC50 part (including Māui login nodes) to the CS500 part you need to add:</p>
<pre><code><span class="c">#SBATCH --clusters=maui_ancil 
#SBATCH -p nesi_prepost # another of its partions
#SBATCH --export=NONE</span></code></pre>
<p>Thus a prepost job submitted to the CS500 nodes from the Maui login node would look like:</p>
<pre><code><span class="c">#!/bin/bash -e
#SBATCH --job-name=hello
#SBATCH --time=00:02:00
#SBATCH --clusters=maui_ancil 
#SBATCH -p nesi_prepost
#SBATCH --export=NONE

module load Anaconda2
python work_analysis.py</span></code></pre>
<p>Note: the <code class="highlighter-rouge">--clusters</code> need to be also specified for the other slurm tools to monitor other parts.</p>
<h2>Job array</h2>
<p>A series of similar jobs can be arranged in a so called job array. Therefore, the user tells slurm how many instances should be launched (array size) and slurm provides environment variables to distinguish between the different instances. For example the user could distinguish different input files or directories. The following example prints a hello world statement and the directory name from within 5 sub-directories:</p>
<pre><code><span class="c">
#!/bin/bash -e
#SBATCH --job-name=arr_test
#SBATCH --time=00:02:00
#SBATCH --array=0-5

cd inputDir${SLURM_ARRAY_TASK_ID}
srun echo "Hello from ${SLURM_ARRAY_TASK_ID} of ${SLURM_ARRAY_TASK_COUNT} form $PWD"</span></code></pre>
<p>More and detailed information can be found <a href="https://slurm.schedmd.com/job_array.html">here</a>.</p>
<h2>Monitor jobs</h2>
<p>You can use <code class="highlighter-rouge">squeue -u $USER</code> to monitor your job status. Alternatively you can also use <code class="highlighter-rouge">sview</code>.</p>
<h2 id="checking-completed-jobs-with-sacct">Checking completed jobs with sacct</h2>
<p>Another useful Slurm command is <code class="highlighter-rouge">sacct</code> which retrieves information about completed jobs. For example:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>sacct -j 14309
</code></pre>
</div>
</div>
<p>where the argument passed to <code class="highlighter-rouge">-j</code> is the job ID, will show us something like:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>       JobID    JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
14309        problem.sh       NeSI  nesi99999         80  COMPLETED      0:0
14309.batch       batch             nesi99999         80  COMPLETED      0:0
14309.0         yourapp             nesi99999         80  COMPLETED      0:0
</code></pre>
</div>
</div>
<p>By default <code class="highlighter-rouge">sacct</code> will list all of your jobs which were (or are) running on the current day. Each job will show as more than one line (unless <code class="highlighter-rouge">-X</code> is specified): an initial line for the job as a whole, and then an additional line for each job step, i.e.: the batch process which is your executing script, and then each of the <code class="highlighter-rouge">srun</code> commands it executes.</p>
<p>By changing the displayed columns you can gain information about the CPU and memory utilisation of the job, for example</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>sacct -j 14309 --format=jobid,jobname,elapsed,avecpu,totalcpu,alloccpus,maxrss,state
</code></pre>
</div>
</div>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>      JobID    JobName    Elapsed     AveCPU   TotalCPU  AllocCPUS     MaxRSS      State
------------ ---------- ---------- ---------- ---------- ---------- ---------- ----------
14309        problem.sh   00:12:42             00:00.012         80             COMPLETED
14309.batch       batch   00:12:42   00:00:00  00:00.012         80      1488K  COMPLETED
14309.0         yourapp   00:12:41   00:12:03   16:00:03         80    478356K  COMPLETE</code></pre>
<p> </p>
</div>
</div>