---
created_at: '2015-10-12T00:28:38Z'
hidden: false
label_names:
- mahuika
- engineering
- gpu
- mpi
- omp
position: 21
title: ABAQUS
vote_count: 2
vote_sum: 0
zendesk_article_id: 212457807
zendesk_section_id: 360000040076
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
 !!! Info
     This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->
<div id="append_ver">
<p>A list of commands can be found with:</p>
<pre><code>abaqus help</code></pre>
</div>
<p><a href="https://support.nesi.org.nz/hc/en-gb/articles/360000568236" target="_self">Hyperthreading</a> can provide significant speedup to your computations, however hyperthreaded CPUs will use twice the number of licence tokens. It may be worth adding  <code>#SBATCH --hint nomultithread</code> to your slurm script if licence tokens are your main limiting factor.</p>
<div></div>
<div>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tips</h3>
<p>Required ABAQUS licences can be determined by this simple and intuitive formula <code>⌊ 5 x N<sup>0.422</sup> ⌋</code> where <code>N</code> is number of CPUs.</p>
</blockquote>
</div>
<p>You can force ABAQUS to use a specific licence type by setting the parameter <code>academic=TEACHING</code> or <code>academic=RESEARCH</code> in a relevant <a href="#env_file" target="_self">environment file</a>.</p>
<h1 id="solvers">Solver Compatibility</h1>
<p>Not all solvers are compatible with all types of parallelisation.</p>
<table style="margin-left: 0px; margin-right: auto;">
<tbody>
<tr>
<td class="wysiwyg-text-align-right" style="width: 143px;"> </td>
<td class="wysiwyg-text-align-center" style="width: 95px;">Element operations</td>
<td class="wysiwyg-text-align-center" style="width: 77px;">Iterative solver</td>
<td class="wysiwyg-text-align-center" style="width: 112px;">Direct solver</td>
<td class="wysiwyg-text-align-center" style="width: 175px;">Lanczos solver</td>
</tr>
<tr>
<td class="wysiwyg-text-align-right" style="width: 143px;"><code>mp_mode=threads</code></td>
<td class="wysiwyg-text-align-center" style="width: 95px;">✖</td>
<td class="wysiwyg-text-align-center" style="width: 77px;">✔</td>
<td class="wysiwyg-text-align-center" style="width: 112px;">✔</td>
<td class="wysiwyg-text-align-center" style="width: 175px;">✔</td>
</tr>
<tr>
<td class="wysiwyg-text-align-right" style="width: 143px;"><code>mp_mode=mpi</code></td>
<td class="wysiwyg-text-align-center" style="width: 95px;">✔</td>
<td class="wysiwyg-text-align-center" style="width: 77px;">✔</td>
<td class="wysiwyg-text-align-center" style="width: 112px;">✖</td>
<td class="wysiwyg-text-align-center" style="width: 175px;">✖</td>
</tr>
</tbody>
</table>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>If your input files were created using an older version of ABAQUS you will need to update them using the command,</p>
<pre><code>abaqus -upgrade -job <em>new_job_name</em> -odb <em>old.odb</em></code></pre>
<p>or</p>
<pre><code>abaqus -upgrade -job <em>new_job_name</em> -inp <em>old.inp</em></code></pre>
</blockquote>
<table>
<tbody>
<tr>
<td style="width: 506px;">
<h2>Serial</h2>
<hr>
<p>For when only <dfn class="dictionary-of-numbers">one CPU is required</dfn>, generally as part of an <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000690275-Parallel-Execution#t_array" target="_self">job array</a>.</p>
<p> </p>
</td>
<td style="width: 163px;">
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      ABAQUS-Shared<br>#SBATCH --time          00:05:00       # Walltime
#SBATCH --<span class="wysiwyg-color-red">cpus-per-task</span> 1              
#SBATCH --<span class="wysiwyg-color-red">mem</span>           1500          # total mem

module load ABAQUS/2019<br>
abaqus job="propeller_s4rs_c3d8r" verbose=2 interactive <br></code></pre>
</td>
</tr>
<tr>
<td style="width: 506px;">
<h2>Shared Memory</h2>
<hr>
<code>mp_mode=threads</code>
<p>Uses a nodes shared memory for communication. </p>
<p>May have a small speedup compared to MPI when using a low number of CPUs, scales poorly. Needs significantly less memory than MPI.</p>
<em>Hyperthreading may be enabled if using shared memory but it is not recommended.</em>
</td>
<td style="width: 163px;">
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      ABAQUS-Shared<br>#SBATCH --time          00:05:00       # Walltime
#SBATCH --<span class="wysiwyg-color-red">cpus-per-task</span> 4              
#SBATCH --<span class="wysiwyg-color-red">mem</span>           2G        # total mem

module load ABAQUS/2019<br>
abaqus job="propeller_s4rs_c3d8r" verbose=2 interactive \<br>    cpus=${<span class="wysiwyg-color-red">SLURM_CPUS_PER_TASK</span>} <span class="wysiwyg-color-black">mp_mode=</span><span class="wysiwyg-color-red">threads</span><br><br></code></pre>
</td>
</tr>
<tr>
<td style="width: 506px;">
<h2>UDF</h2>
<hr>
<p>Shared memory run with user defined function (fortran or C). </p>
<p><code>user=&lt;name_of_function&gt;</code> </p>
<p>Function will be compiled at start of run. </p>
<p><em>You may need to chance the function suffix if you usually compile on windows.</em></p>
</td>
<td style="width: 163px;">
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      ABAQUS-SharedUDF<br>#SBATCH --time          00:05:00       # Walltime
#SBATCH --cpus-per-task 4              
#SBATCH --mem           2G         # total mem
<br><span class="wysiwyg-color-red">module load imkl</span>
module load ABAQUS/2019<br>
abaqus job="propeller_s4rs_c3d8r" <span class="wysiwyg-color-red">user=my_udf.f90</span> verbose=2 interactive \<br>    cpus=${SLURM_CPUS_PER_TASK} mp_mode=threads<br><br></code></pre>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-left" style="width: 506px;">
<h2>Distributed Memory</h2>
<hr>
<code>mp_mode=mpi</code>
<p>Multiple<em> processes</em> each with a single <em>thread</em>.</p>
<p>Not limited to <dfn class="dictionary-of-numbers">one node</dfn>.<br>Model will be segmented into <code>-np</code> pieces which should be equal to <code>--ntasks</code>.</p>
<p>Each task could be running on a different node leading to increased communication overhead<br>.Jobs can be limited to a single node by adding  <code style="font-size: 14px;">--nodes=1</code> however this will increase your time in the queue as contiguous cpu's are harder to schedule.</p>
<p>This is the default method if <code>mp_mode</code> is left unspecified.</p>
</td>
<td style="width: 163px;">
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      ABAQUS-Distributed <br>#SBATCH --time          00:05:00       # Walltime
#SBATCH --<span class="wysiwyg-color-red">ntasks</span>        8              
#SBATCH --<span class="wysiwyg-color-red">mem-per-cpu</span>   1500          # Each CPU needs it's own.<br>#SBATCH --nodes         1

module load ABAQUS/2019<br>
abaqus job="propeller_s4rs_c3d8r" verbose=2 interactive \<br>    cpus=${<span class="wysiwyg-color-red">SLURM_NTASKS</span>} <span class="wysiwyg-color-black">mp_mode=</span><span class="wysiwyg-color-red">mpi</span><br><br></code></pre>
</td>
</tr>
<tr>
<td style="width: 506px;">
<h2>GPUs</h2>
<hr>
<p>The GPU nodes are limited to <dfn class="dictionary-of-numbers">16 CPUs</dfn></p>
<p>In order for the GPUs to be worthwhile, you should see a speedup equivalent to <dfn class="dictionary-of-numbers">56 CPU</dfn>'s per GPU used. GPU modes will generally have less memory/cpus</p>
</td>
<td style="width: 163px;">
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      ABAQUS-gpu<br>#SBATCH --time          00:05:00       # Walltime
#SBATCH --<span class="wysiwyg-color-red">cpus-per-task</span> 4              
#SBATCH --<span class="wysiwyg-color-red">mem</span>           4G         # total mem<br>#SBATCH <span class="wysiwyg-color-red">--gpus-per-node 1</span>

module load ABAQUS/2019 <br>module load CUDA<br>
abaqus job="propeller_s4rs_c3d8r" verbose=2 interactive \<br>    cpus=<span class="wysiwyg-color-black">${</span><span class="wysiwyg-color-red">SLURM_CPUS_PER_TASK</span><span class="wysiwyg-color-black">}</span> <span class="wysiwyg-color-red">gpus=${SLURM_GPUS_PER_NODE}</span> <span class="wysiwyg-color-black">mp_mode=</span><span class="wysiwyg-color-red">threads</span></code></pre>
</td>
</tr>
</tbody>
</table>
<h1>User Defined Functions </h1>
<p>User defined functions (UDFs) can be included on the command line with the argument <code>user=&lt;filename&gt;</code> where <code>&lt;filename&gt;</code> is the C or fortran source code.</p>
<p>Extra compiler options can be set in your local <code>abaqus_v6.env</code> file.</p>
<p>The default compile commands are for <code>imkl</code>, other compilers can be loaded with <code>module load</code>, you may have to change the<a href="https://support.nesi.org.nz/hc/en-gb/articles/360000329015" target="_self"> compile commands</a> in your local <code>.env</code> file.</p>
<h1 id="env_file">Environment file</h1>
<p>The <a style="background-color: #ffffff; font-size: 15px;" href="http://media.3ds.com/support/simulia/public/v613/installation-and-licensing-guides/books/sgb/default.htm?startat=ch04s01.html" target="_self">ABAQUS environment file</a> contains a number of parameters that define how the your job will run, some of these you may with to change.</p>
<p>These parameters are read, </p>
<p><code>../ABAQUS/SMA/site/abaqus_v6.env</code> Set by NeSI and cannot be changed.</p>
<p><code>~/abaqus_v6.env</code> (your home directory) If exists, will be used in all jobs submitted by you.</p>
<p><code>&lt;working directory&gt;/abaqus_v6.env</code> If exists, will used in this job only.</p>
<p>You may want to include this short snippet when making changes specific to a job.</p>
<pre><code># Before starting abaqus
echo "parameter=value
parameter=value
parameter=value" &gt; "abaqus_v6.env"

# After job is finished.
rm "abaqus_v6.env"
</code></pre>
<p> </p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Useful Links</h3>
<ul>
<li><a href="https://www.sharcnet.ca/Software/Abaqus610/Documentation/docs/v6.10/books/usb/default.htm?startat=pt01ch03s02abx02.html" target="_self">Command line options for standard submission.</a></li>
</ul>
</blockquote>
<p> </p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360002123695/ABAQUS_speedup_SharedVMPI.png" alt="ABAQUS_speedup_SharedVMPI.png"></p>
<p> </p>
<p><em>Note: Hyperthreading off, testing d<dfn class="dictionary-of-numbers">one on small mechanical </dfn>FEA model. Results highly model dependant. Do your own tests.</em></p>