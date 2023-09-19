---
created_at: '2019-04-07T23:56:57Z'
hidden: false
label_names:
- slurm
position: 5
title: Finding Job Efficiency
vote_count: 8
vote_sum: 8
zendesk_article_id: 360000903776
zendesk_section_id: 360000189716
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <h1>On Job Completion</h1>
<p><span style="font-weight: 400;">It is good practice to have a look at the resources your job used on completion, this way you can improve your job specifications in the future.</span></p>
<p><span style="font-weight: 400;">Once your job has finished check the relevant details using the tools: <code>nn_seff</code> or <code>sacct</code> For example:<br></span></p>
<p><strong>nn_seff</strong></p>
<pre><strong><span style="font-weight: 400;">nn_seff 30479534</span></strong></pre>
<pre><span style="font-weight: 400;">Job ID: 1936245<br>Cluster: mahuika<br>User/Group: user/group<br>State: COMPLETED (exit code 0)<br>Cores: 1<br>Tasks: 1<br>Nodes: 1<br>Job Wall-time: 7.67% 00:01:09 of 00:15:00 time limit<br>CPU Efficiency: 98.55% 00:01:08 of 00:01:09 core-walltime<br>Mem Efficiency: 10.84% 111.00 MB of 1.00 GB</span></pre>
<p><span style="font-weight: 400;">Notice that the CPU efficiency was high but the memory efficiency was very low and consideration should be given to reducing memory requests for similar jobs.  If in doubt, please contact <a href="mailto:support@nesi.org.nz">support@nesi.org.nz</a> for guidance.</span></p>
<p> </p>
<p><strong>sacct</strong></p>
<pre><code>sacct --format="JobID,JobName,Elapsed,AveCPU,MinCPU,TotalCPU,Alloc,NTask,MaxRSS,State" -j &lt;jobid&gt;
</code></pre>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tip</h3>
<p><em>If you want to make this your default </em><code>sacct</code><em> setting, run;</em></p>
<pre><code>echo 'export SACCT_FORMAT="JobID,JobName,Elapsed,AveCPU,MinCPU,TotalCPU,Alloc%2,NTask%2,MaxRSS,State"' &gt;&gt; ~/.bash_profile
source ~/.bash_profile</code></pre>
</blockquote>
<hr>
<p>Below is an output for reference:</p>
<pre><code>       JobID    JobName    Elapsed     AveCPU     MinCPU   TotalCPU  AllocCPUS   NTasks     MaxRSS      State
------------ ---------- ---------- ---------- ---------- ---------- ---------- -------- ---------- ----------
3007056      rfm_ANSYS+   00:27:07                         03:35:55         16                      COMPLETED
3007056.bat+      batch   00:27:07   03:35:54   03:35:54   03:35:55         16        1  13658349K  COMPLETED
3007056.ext+     extern   00:27:07   00:00:00   00:00:00   00:00:00         16        1        89K  COMPLETED
</code></pre>
<p><em>All of the adjustments below still allow for a degree of variation. There may be factors you have not accounted for.</em></p>
<hr>
<h2><strong>Walltime</strong></h2>
<p>From the <code>Elapsed</code> field we may want to update our next run to have a more appropriate walltime.</p>
<pre><code>#SBATCH --time=00:40:00</code></pre>
<h2><strong>Memory</strong></h2>
<p>The <code>MaxRSS</code> field shows the maximum memory used by each of the job steps, so in this case 13 GB. For our next run we may want to set:</p>
<pre><code>#SBATCH --mem=15G</code></pre>
<h2><strong>CPU's</strong></h2>
<p><code>TotalCPU</code> is the number of computation hours, in the best case scenario the computation hours would be equal to <code>Elapsed</code> x <code>AllocCPUS</code>.</p>
<p>In this case our ideal <code>TotalCPU</code> would be 07:12:00, as our job only managed 03:35:55 we can estimate the CPU usage was around 50%<br>It might be worth considering reducing the number of CPUs requested, however bear in mind there are other factors that affect CPU efficiency.</p>
<pre><code>#SBATCH --cpus-per-task=10</code></pre>
<p> </p>
<p>Note: When using sacct to determine the amount of memory your job used - in order to reduce memory wastage - please keep in mind that Slurm reports the figure as RSS (Resident Set Size) when in fact the metric being displayed is PSS (Proportional Set Size). This is an issue with Slurm and cannot currently be fixed. PSS is a more accurate measure of memory usage than RSS - RSS shows the sum of memory used including shared libraries, therefore this gives a figure that is more often than not greater than the actual amount of memory used by your job. PSS provides a more accurate measure.</p>
<p>Further technical notes for those interested in commonly used memory usage metrics on linux systems:</p>
<p><strong>VSS</strong> &gt;= <strong>RSS</strong> &gt;= <strong>PSS</strong> &gt;= <strong>USS</strong><br><strong>VSS-Virtual Set Size</strong> - Virtual memory consumption (contains memory consumed by shared libraries)<br><strong>RSS-Resident Set Size</strong> - Used physical memory (contains memory consumed by shared libraries)<br><strong>PSS-Proportional Set Size</strong> - Actual physical memory used (proportional allocation of memory consumed by shared libraries)<br><strong>USS-Unique Set Size</strong> - Process consumed physical memory alone (does not contain the memory occupied by the shared library)<br><code class="c-mrkdwn__code" data-stringify-type="code">PSS = USS + (RSS/# shared processes)</code></p>
<h1>During Runtime</h1>
<p>In order to check in on a job that is running, you will need to ssh to the compute node where it it running.</p>
<h2>Finding Job Node</h2>
<p>If 'nodelist' is not one of the fields in the output of your <code>sacct</code> or <code>squeue</code> commands you can find the node a job is running on using the command; <code>squeue -h -o %N
  -j &lt;jobid&gt;</code> The node will look something like <code>wbn123</code> on Mahuika or <code>nid00123</code> on Maui.</p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>If your job is using MPI it may be running on multiple nodes</p>
</blockquote>
<h2>htop </h2>
<pre>ssh -t wbn175 htop -u $USER</pre>
<p>If it is your first time connecting to that particular node, you may be prompted:</p>
<pre><code>The authenticity of host can't be established <br>Are you sure you want to continue connecting (yes/no)?</code></pre>
<p>Reply <code>yes</code>. Y alone (upper or lower case) is not sufficient.</p>
<p>Focusing on the lower panel, you will see a printout of all of your current processes running on that node. If you have multiple jobs on the same node, they will all be shown (you can tell them apart by their parent process).</p>
<p>Processes in green can be ignored</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360003952836/how_to_read_htop.png" alt="how_to_read_htop.png" width="929" height="252"></p>
<p><strong>RES</strong> - Current memory being used (same thing as 'RSS' from sacct)</p>
<p><strong>S</strong> - State, what the thread is currently doing.</p>
<ul>
<li>R - Running</li>
<li>S - Sleeping, waiting on another thread to finish.</li>
<li>D - Sleeping</li>
<li>Any other letter - Something has gone wrong!</li>
</ul>
<p><strong>CPU%</strong> - Percentage CPU utilisation.</p>
<p><strong>MEM% </strong>Percentage Memory utilisation.</p>
<p> </p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Warning</h3>
<p>If the job finishes, or is killed you will be kicked off the node. If htop freezes, type <code>reset</code> to clear your terminal.</p>
</blockquote>
<h1>Limitations of using CPU Efficiency</h1>
<p>CPU efficiency, as described here, only represents the <em>percentage of time </em>the CPUs are in use. This is not enough to get a picture of overall job efficiency, as required CPU time <em>may vary by number of CPU</em>s.</p>
<p>The only way to get the full context, is to compare walltime performance between jobs at different scale. See <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000728016" target="_self">Job Scaling</a> for more details.</p>
<h2>Example</h2>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360003953876/qdyn_eff.png" alt="qdyn_eff.png"></p>
<p>From the above plot of CPU efficiency, you might decide a 5% reduction of CPU efficiency is acceptable and scale your job up to 18 CPU cores . </p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360003804135/qdyn_walltime.png" alt="qdyn_walltime.png"></p>
<p>However, when looking at a plot of walltime it becomes apparent that performance gains per CPU added drop significantly after 4 CPUs, and in fact absolute performance losses (negative returns) are seen after 8 CPUs.</p>