---
created_at: '2019-01-18T01:56:15Z'
hidden: false
label_names: []
position: 14
title: 'SLURM: Best Practice'
vote_count: 3
vote_sum: 1
zendesk_article_id: 360000705196
zendesk_section_id: 360000030876
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<h3 id="01H8ANN6F571KEA80CG0FQHX6M">Bash Header</h3>
<p>We recommend using <code class="highlighter-rouge">#!/bin/bash -e</code> instead of plain <code class="highlighter-rouge">#!/bin/bash</code>, so that the failure of any command within the script will cause your job to stop immediately rather than attempting to continue on with an unexpected environment or erroneous intermediate data.  It also ensures that your failed jobs show a status of FAILED in <em>sacct</em> output.</p>
<h3 id="01H8ANN6F5FDTFCY2SZFMAPW8Y">Resources </h3>
<p>Don't request more resources (CPUs, memory, GPUs) than you will need. In addition to using your core hours faster, resources intensive jobs will take longer to queue. Use the information provided at the completion of your job (eg: via the <em>sacct</em> command) to better define resource requirements.</p>
<h3 id="01H8ANN6F5EFWKSS0MZVGQ6PQP">Wall-time</h3>
<p>Long jobs will spend more time in the queue, as there are more opportunities for the scheduler to find a time slot to run shorter jobs. So consider using job check-pointing or, where possible, more parallelism, to get job durations down to a few hours, or at worst, days.</p>
<p>Leave some headroom for safety and run-to-run variability on the system but try to be as accurate as possible.</p>
<p>If you have very many jobs of less than 5 minutes then they should probably be combined into larger jobs using a simple loop in the batch script so as to amortise the overheads of each job (starting, accounting etc).</p>
<h3 id="01H8ANN6F527CCYP03TGRYGQM0">Memory (RAM)</h3>
<p>If you request more memory (RAM) than you need for your job, it <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000737555" target="_self">will wait longer in the queue and will be more expensive when it runs</a>. On the other hand, if you don't request enough memory, the job may be killed for attempting to exceed its allocated memory limits.</p>
<p>We recommend that you request a little more RAM, but not much more, than your program will need at peak memory usage.</p>
<p>We also recommend using <code>--mem</code> instead of <code>--mem-per-cpu</code> in most cases. There are a few kinds of jobs for which <code>--mem-per-cpu</code> is more suitable. See <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001108756" target="_self">our article on how to request memory</a> for more information.</p>
<h3 id="01H8ANN6F5MH722W3AD9Y5SH3X">Parallelism</h3>
<p>In general only MPI jobs should set <em>ntasks</em> greater than 1 or use <em>srun</em>.  If you don't know whether your program supports MPI, it probably doesn't.</p>
<p>Only multithreaded jobs should set <em>cpus-per-task</em>.  If you don't know whether your program supports multithreading, try benchmarking with 2 CPUs and with 4 CPUs and see if there is a 2-fold difference in elapsed job time.</p>
<p><a href="https://slurm.schedmd.com/job_array.html">Job arrays</a> are an efficient mechanism of managing a collection of batch jobs with identical resource requirements. Most Slurm commands can manage job arrays either as individual elements (tasks) or as a single entity (e.g. delete an entire job array in a single command)</p>
<h3 id="01H8ANN6F5CSFFFWPE4CBQMG3P">Fairshare</h3>
<p>A low fairshare score will affect your jobs priority in the queue, learn more about how to effectively use your allocation <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000743536" target="_blank" rel="noopener noreferrer">here</a>.</p>
<h3 id="01H8ANN6F5H1MH8WP8Z1B8ZF50">Cross machine submission</h3>
<p>Jobs can be submitted from one machine to another by using the <code>--cluster</code> option. E.g. submitting a job from Māui_Ancil to Māui.</p>
<p>By default the environment (modules and variables) will be inherited from the submitting shell into the job environment. But the environments vary between our different machines, including module names, location of slurm tools, etc., which could cause issues in this inheriting case. We suggest to use the environment variable <code>SBATCH_EXPORT=NONE</code> (do NOT us <code>--export=none</code> option) in the submitting shell. Therefore we suggest to submit a job, e.g. to Māui using:</p>
<pre><code>SBATCH_EXPORT=NONE sbatch --cluster=maui job.sl</code></pre>
<p>Please note: Above we only discussed the transition from your submitting environment to the job environment. The latter is the one your job script is running in. There is another environment created for your parallel application (when called srun). There we want to inherit from the job environment to have PATHs and setting available. Therefore, avoid setting <code>SBATCH_EXPORT=NONE</code> in your job script or in .bashrc or .profile for all cases. The slurm <code>--export=none</code> option would prevent inhering environments in both transitions. Another note: Alternatively you can set <code>SLURM_EXPORT_ENV=ALL</code> in your job script to enable the environment forwarding to the srun environment.</p>