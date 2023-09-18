---
created_at: '2019-03-26T00:36:24Z'
hidden: false
label_names:
- engineering
- COMSOL
position: 27
title: COMSOL
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000871556
zendesk_section_id: 360000040076
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <div id="append_ver">
<pre><code>comsol --help</code></pre>
<p>Will display a list of COMSOL batch commands.</p>
</div>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Useful Links</h3>
<ul>
<li><a href="https://www.comsol.com/support/knowledgebase/1001/" target="_self">Running COMSOL in parallel on clusters.</a></li>
<li><a href="https://www.comsol.com/support/knowledgebase/1250/" target="_self">Running parametric sweeps, batch sweeps, and cluster sweeps from the command line.</a></li>
<li><a href="https://www.comsol.com/support/knowledgebase/1096/" target="_self">COMSOL and Multithreading.</a></li>
</ul>
</blockquote>
<div>
<h1>Batch Submission</h1>
<p>When using COMSOL batch the following flags can be used to control distribution. </p>
<table style="width: 635px;">
<tbody>
<tr>
<td style="width: 185.953px;"><code>-mpibootstrap slurm</code></td>
<td style="width: 256.047px;"> Instructs COMSOL to get it's settings from SLURM</td>
</tr>
<tr>
<td style="width: 185.953px;"><code>-np &lt;cpus&gt;</code></td>
<td style="width: 256.047px;">Number of CPUs to use in each task. Equivalent to slurm input <code>--cpus-per-task</code> or environment variable <code>${SLURM_CPUS_PER_TASK}</code>
</td>
</tr>
<tr>
<td style="width: 185.953px;"><code>-nn &lt;tasks&gt;</code></td>
<td style="width: 256.047px;">Number of tasks total. <code>--ntasks</code> or <code>${SLURM_NTASKS}</code>
</td>
</tr>
<tr>
<td style="width: 185.953px;"><code>-nnhost &lt;tasks&gt;</code></td>
<td style="width: 256.047px;">Number of tasks per node. <code>--ntasks-per-node</code> <code>${SLURM_NTASKS_PER_NODE}</code>
</td>
</tr>
<tr>
<td style="width: 185.953px;"><code>-f &lt;path to hostlist&gt;</code></td>
<td style="width: 256.047px;">Host file. You wont't need to set this in most circumstances.</td>
</tr>
</tbody>
</table>
<h1> </h1>
<h1 id="example-script">Example Scripts</h1>
</div>
<hr>
<table style="height: 481px; width: 811px;">
<tbody>
<tr>
<td style="width: 506px;">
<h2>Serial Example</h2>
<hr>
<p>Single <em>process</em> with a single <em>thread</em></p>
<p>Usually submitted as part of an array, as in the case of parameter sweeps.</p>
</td>
<td style="width: 163px;">
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      COMSOL-serial<br>#SBATCH --licenses      comsol@uoa_foe <br>#SBATCH --time          00:05:00          # Walltime
#SBATCH --<span class="wysiwyg-color-black">mem</span>           1512               # total mem

module load COMSOL/5.5
<br>comsol batch -inputfile my_input.mph<br></code></pre>
</td>
</tr>
<tr>
<td style="width: 506px;">
<h2>Shared Memory Example</h2>
<hr>
<p> </p>
</td>
<td style="width: 163px;">
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      COMSOL-shared<br>#SBATCH --licenses      <a href="mailto:comsol@uoa_foe">comsol@</a>uoa_foe <br>#SBATCH --time          00:05:00        # Walltime<br>#SBATCH <span class="wysiwyg-color-red">--cpus-per-task</span> <span class="wysiwyg-color-red">8</span>
#SBATCH --<span class="wysiwyg-color-black">mem</span>           4G              # total mem

module load COMSOL/5.5
<br>comsol batch -mpibootstrap slurm -inputfile my_input.mph<br></code></pre>
</td>
</tr>
<tr>
<td style="width: 506px;">
<h2>Distributed Memory Example</h2>
<hr>
<p> </p>
</td>
<td style="width: 163px;">
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      COMSOL-distributed <br>#SBATCH --licenses      comsol@uoa_foe <br>#SBATCH --time          00:05:00            # Walltime<br>#SBATCH <span class="wysiwyg-color-red">--ntasks</span>        <span class="wysiwyg-color-red">8</span>           
#SBATCH <span class="wysiwyg-color-red">--mem-per-cpu</span>   <span class="wysiwyg-color-red">1500               </span> # mem per cpu

module load COMSOL/5.5<br>
comsolbatch -mpibootstrap slurm -inputfile my_input.mph<br></code></pre>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-left" style="width: 506px;">
<h2>Hybrid Example</h2>
<hr>
<p> </p>
</td>
<td style="width: 163px;">
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name         COMSOL-hybrid <br>#SBATCH --licenses         comsol@uoa_foe<br>#SBATCH --time             00:05:00          # Walltime<br>#SBATCH <span class="wysiwyg-color-red">--<font color="#000000">ntasks         </font>  4 </span>                # total mem<br>#SBATCH <span class="wysiwyg-color-red">--cpus-per-task</span>    <span class="wysiwyg-color-red">16</span>
#SBATCH --<span class="wysiwyg-color-black">mem-per-cpu</span>      1500B             # total mem

module load COMSOL/5.5
<br>comsol batch -mpibootstrap slurm -inputfile my_input.mph<br></code></pre>
</td>
</tr>
</tbody>
</table>
<blockquote class="blockquote-warning">
<h3>Important</h3>
<p>If no output file is set, using <code>--output</code> the input file will be updated instead.</p>
</blockquote>
<h1>Interactive Use</h1>
<p>Providing you have <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001075975" target="_self">set up X11</a>, you can open the COMSOL GUI by running the command <code>comsol</code>.</p>
<p>Large jobs should not be run on the login node.</p>
<h1>Recommendations</h1>
<p>COMSOL is relatively smart with it's use of resources, if possible it is preferable to use <code>--cpus-per-task</code> over <code>--ntasks</code></p>
<!--
<h1 id="best-practices">Resource requirements</h1>
<hr>
<p>
  COMSOL does not support MPI therefore <code>#SBATCH --ntasks</code> should never
  be greater than 1.
</p>
<p>
  Memory requirements depend on job type, but will scale up with number of CPUs
  ≈ linearly.
</p>
<p>
  Hyper-threading can benefit jobs using less than
  <dfn class="dictionary-of-numbers">8 CPUs</dfn>, but is not recommended on larger
  jobs.
</p>
<p>
  <em>Performance is highly depended on the model used. The above should only be used as a very rough guide.</em>
</p>
<p>
  <img src="https://support.nesi.org.nz/hc/article_attachments/360002021216/speedup_smoothed.png" alt="speedup_smoothed.png" width="1001" height="576">
</p>
-->