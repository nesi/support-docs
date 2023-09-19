---
created_at: '2019-01-07T01:10:28Z'
hidden: false
label_names:
- slurm
- scheduler
position: 3
title: Submitting your first job
vote_count: 8
vote_sum: 8
zendesk_article_id: 360000684396
zendesk_section_id: 360000189716
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <h2>Environment Modules</h2>
<p><span style="font-weight: 400;">Modules are a convenient  way to provide access to applications  on the cluster. They prepare the environment you need to run an application.</span></p>
<p><span style="font-weight: 400;">For a full list of module commands run <kbd>man module</kbd></span></p>
<table style="height: 110px; width: 861.4px;">
<tbody>
<tr>
<td style="width: 275px;"><code>module spider [ &lt;string&gt; ]</code></td>
<td style="width: 301.4px;">List all modules whose names, including version strings, contain <code>&lt;string&gt;</code>. If the <code>&lt;string&gt;</code> argument is not supplied, list all available modules. (only on Mahuika)</td>
</tr>
<tr>
<td style="width: 275px;"><code>module show &lt;string&gt;</code></td>
<td style="width: 301.4px;">Show the contents of the module given by <code>&lt;string&gt;</code>. If only the module name (e.g. <code>Python</code>) is given, show the default module of that name. If both name and version are given, show that particular version module.</td>
</tr>
<tr>
<td style="width: 275px;"><code>module load &lt;string&gt;</code></td>
<td style="width: 301.4px;">Load the module (name and version) given by <code>&lt;string&gt;</code>. If no version is given, load the default version.</td>
</tr>
<tr>
<td style="width: 275px;"><code>module list [ &lt;string&gt; ]</code></td>
<td style="width: 301.4px;">List all currently loaded modules whose names, including version strings, contain <code>&lt;string&gt;</code>. If the <code>&lt;string&gt;</code> argument is not supplied, list all currently loaded modules.</td>
</tr>
</tbody>
</table>
<h2>Slurm</h2>
<p>Jobs on Mahuika and Māui are submitted<em> </em>in the form of a <em><span style="font-weight: 400;">batch script </span></em><span style="font-weight: 400;">containing the code you want to run and a header of information needed by our job scheduler <em>Slurm.</em></span></p>
<h2>Creating a batch script</h2>
<p>Create a new file and open it with <kbd>nano myjob.sl</kbd></p>
<pre class="nohighlight"><code>#!/bin/bash -e
#SBATCH --job-name=SerialJob # job name (shows up in the queue)
#SBATCH --time=00:01:00      # Walltime (HH:MM:SS)
#SBATCH --mem=512MB          # Memory in MB
#SBATCH --qos=debug          # debug QOS for high priority job tests<br>
pwd # Prints working directory
</code></pre>
<p>Copy in the above text and save and exit the text editor with 'ctrl + x'.</p>
<p>Note:<code>#!/bin/bash</code>is expected by Slurm</p>
<p>Note: if you are a member of multiple accounts you should add the line <code>#SBATCH --account=&lt;projectcode&gt;</code></p>
<h2>Testing</h2>
<p>We recommend testing your job using the debug Quality of Service (QOS).  The debug QOS can be gained by adding the <code>sbatch</code> command line option <code>--qos=debug</code>.<br>This adds 5000 to the job priority so raises it above all non-debug jobs, but is limited to one small job per user at a time: no more than 15 minutes and no more than 2 nodes.</p>
<blockquote class="blockquote-warning">
<h3>Warning</h3>
<p>Please do not run your code on the login node.  Any processes running on the login node for long periods of time or using large numbers of CPUs will be terminated.</p>
</blockquote>
<h2>Submitting</h2>
<p>Jobs are submitted to the scheduler using:</p>
<pre class="nohighlight"><code>sbatch myjob.sl</code></pre>
<p>You should receive an output</p>
<p>Submitted batch job 1748836</p>
<p><code>sbatch</code>can take command line arguments similar to those used in the shell script through SBATCH pragmas</p>
<p>You can find more details on its use on the <a href="https://slurm.schedmd.com/sbatch.html" target="_self" rel="undefined">Slurm Documentation</a></p>
<h2>Job Queue</h2>
<p>The currently queued jobs can be checked using </p>
<pre class="nohighlight"><kbd>squeue</kbd></pre>
<p>You can filter to just your jobs by adding the flag</p>
<pre><kbd>squeue -u usr9999</kbd></pre>
<p>You can also filter to just your jobs using</p>
<pre><kbd>squeue --me</kbd></pre>
<p>You can find more details on its use on the <a href="https://slurm.schedmd.com/squeue.html" target="_self">Slurm Documentation</a></p>
<p>You can check all jobs submitted by you in the past day using:</p>
<pre><kbd>sacct</kbd></pre>
<p>Or since a specified date using:</p>
<pre><kbd>sacct -S YYYY-MM-DD</kbd></pre>
<p>Each job will show as multiple lines, one line for the parent job and then additional lines for each job step.</p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tips</h3>
<p><kbd>sacct -X</kbd> Only show parent processes.</p>
<p><kbd>sacct --state=PENDING/RUNNING/FAILED/CANCELLED/TIMEOUT</kbd> Filter jobs by state.</p>
</blockquote>
<p>You can find more details on its use on the <a href="https://slurm.schedmd.com/sacct.html" target="_self" rel="undefined">Slurm Documentation</a></p>
<h2>
<br>Cancelling</h2>
<p><kbd>scancel &lt;jobid&gt;</kbd> will cancel the job described by <kbd>&lt;jobid&gt;</kbd>. You can obtain the job ID by using <kbd>sacct</kbd> or <kbd>squeue</kbd>.</p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tips</h3>
<p><kbd>scancel -u [username]</kbd> Kill all jobs submitted by you.</p>
<p><kbd>scancel {[n1]..[n2]}</kbd> Kill all jobs with an id between <kbd>[n1]</kbd> and <kbd>[n2]</kbd></p>
</blockquote>
<p>You can find more details on its use on the <a href="https://slurm.schedmd.com/scancel.html" target="_self" rel="undefined">Slurm Documentation</a></p>
<h2>Job Output</h2>
<p>When the job completes, or in some cases earlier, two files will be added to the directory in which you were working when you submitted the job:</p>
<p><code>slurm-[jobid].out</code> containing standard output.</p>
<p><code>slurm-[jobid].err</code> containing standard error.</p>