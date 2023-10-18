---
created_at: '2015-10-15T02:15:46Z'
hidden: false
label_names:
- mahuika
- application
- engineering
position: 24
title: ANSYS
vote_count: 3
vote_sum: 3
zendesk_article_id: 212642617
zendesk_section_id: 360000040076
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->
<div id="append_lic">
<h2>License Types</h2>
<p>The three main ANSYS licenses are;</p>
<ul>
<li>
<strong>ANSYS Teaching License </strong>(aa_t)
<p>This is the default license type, it can be used on up to 6 CPUs on models with less than <span style="font-style: italic;">512k nodes</span></p>
</li>
<li>
<strong>ANSYS Research license</strong> (aa_r)
<p>No node restrictions. Can be used on up to 16 CPUs, for every additional CPU over 16 you must request additional 'aa_r_hpc' licenses.</p>
</li>
<li>
<strong>ANSYS HPC License </strong>(aa_r_hpc)<strong><br></strong>One of these is required for each CPU over 16 when using a research license.</li>
</ul>
<h2>License Order</h2>
<p>Whether to use a teaching or research license <strong>must be set manually</strong>. If your job is greater than the node limit, not switching to the research license before submitting a job will <strong>cause the job to fail</strong>.</p>
<p>The license order can be changed in workbench under tools &gt; license preferences (provided you have X11 forwarding set up), or by running either of the following (ANSYS module must be loaded first using <code>module load ANSYS</code>).</p>
<pre><code>prefer_research_license</code></pre>
<pre><code>prefer_teaching_license</code></pre>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Note</h3>
<p>License preferences are individually tracked by <em>each version of ANSYS. </em>Make sure you set preferences using the same version as in your script.</p>
</blockquote>
</div>
<h1>Journal files</h1>
<p>Some ANSYS applications take a 'journal' text file as input. It is of<dfn class="dictionary-of-numbers">ten useful to create </dfn>this journal file in your SLURM script (tidiness, submitting jobs programmatically, etc). This can be d<dfn class="dictionary-of-numbers">one by using </dfn><code>cat</code> to make a file from a '<a href="http://tldp.org/LDP/abs/html/here-docs.html" target="_self">heredoc</a>'.</p>
<p>Below is an example of this from a fluent script.</p>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      Fluent_Array
#SBATCH --time          01:00:00          # Wall time
#SBATCH --mem           512MB             # Memory per node
#SBATCH --licenses      aa_r:1       # One license token per CPU, less 16<br>#SBATCH --array         1-100 <br>#SBATCH --hint          nomultithread     # No hyperthreading

module load ANSYS/19.2
<br>JOURNAL_FILE=fluent_${SLURM_JOB_ID}.in<br>cat &lt;&lt;EOF &gt; ${JOURNAL_FILE}<br>/file/read-case-data testCase${SLURM_ARRAY_TASK_ID}.cas<br>/solve/dual-time-iterate 10<br>/file/write-case-data testOut${SLURM_ARRAY_TASK_ID}.cas<br>/exit yes<br>EOF<br>
# Use one of the -v options 2d, 2ddp, 3d, or 3ddp
fluent -v3ddp -g -i ${JOURNAL_FILE}<br>rm ${JOURNAL_FILE}</code></pre>
<p><code class="bash">JOURNAL_FILE</code> is a variable holding the name of a file, the next line <code>cat</code> creates the file then writes a block of text into it. The block of text writ<dfn class="dictionary-of-numbers">ten is everything between an </dfn>arbitrary string (in this case <code>EOF</code>) and its next occurrence.</p>
<p>In this case (assuming it is the first run of the array and the jobid=1234567), the file  <code>fluent_1234567.in</code> will be created:</p>
<pre><code class="bash">/file/read-case-data testCase1<br>; This will read testCase1.cas and testCase1.dat<br>; Inputs can be read separately with 'read-case' and 'read-data'<br><br>/solve/dual-time-iterate 10<br>; Solve 10 time steps<br><br>/file/write-case-data testCase1 ok<br>; Since our output name is the same as our input, we have to provide conformation to overwrite, 'ok' <br><br>exit yes<br>; Not including 'exit yes' will cause fluent to exit with an error. (Everything will be fine, but SLURM will read it as FAILED).)</code></pre>
<p>then called as an input <code class="bash">fluent -v3ddp -g -i fluent_1234567.in</code>,<br>then deleted <code class="bash">rm fluent_1234567.in</code></p>
<p>This can be used with variable substitution to great effect as it allows the use of variables in what might otherwise be a fixed input.</p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>Comments can be added to journal files using a <code>;</code>. For example:</p>
<pre><code>; This is a comment</code></pre>
</blockquote>
<h1 id="ansys-fluent">Fluent</h1>
<p><a href="https://docs.hpc.shef.ac.uk/en/latest/referenceinfo/ANSYS/fluent/writing-fluent-journal-files.html" target="_blank" rel="noopener">Some great documentation on journal files</a></p>
<p><code>fluent -help</code> for a list of commands.</p>
<p>Must have <dfn class="dictionary-of-numbers">one of these flags</dfn>. </p>
<table>
<tbody>
<tr>
<td style="width: 105px;"><code>2d</code></td>
<td style="width: 271px;">
<dfn class="dictionary-of-numbers">2D solver</dfn>, single point precision.</td>
</tr>
<tr>
<td style="width: 105px;"><code>3d</code></td>
<td style="width: 271px;">
<dfn class="dictionary-of-numbers">3D solver</dfn>, single point precision.</td>
</tr>
<tr>
<td style="width: 105px;"><code>2ddp</code></td>
<td style="width: 271px;">
<dfn class="dictionary-of-numbers">2D solver</dfn>, double point precision.</td>
</tr>
<tr>
<td style="width: 105px;"><code>3ddp</code></td>
<td style="width: 271px;">
<dfn class="dictionary-of-numbers">3D solver</dfn>, double point precision.</td>
</tr>
</tbody>
</table>
<p> </p>
<table>
<tbody>
<tr>
<td>
<h2>Serial Example</h2>
<hr>
<p>Single <em>process</em> with a single <em>thread </em><dfn class="dictionary-of-numbers">(2 threads if hyperthreading </dfn>enabled).</p>
<p>Usually submitted as part of an array, as in the case of parameter sweeps.</p>
</td>
<td>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      Fluent-Serial<br>#SBATCH --licenses      aa_r@uoa_foe:1 #One research license.<br>#SBATCH --time          00:05:00          # Walltime
#SBATCH --cpus-per-task <span class="wysiwyg-color-red">1</span>                 # Double if hyperthreading enabled
#SBATCH --<span class="wysiwyg-color-red">mem</span>           512MB             # total memory (per node)
#SBATCH --hint          nomultithread     # Hyperthreading disabled

module load ANSYS/19.2<br>
JOURNAL_FILE=/share/test/ansys/fluent/wing.in
fluent 3ddp -g -i ${JOURNAL_FILE}<br></code></pre>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-left">
<h2>Distributed Memory Example</h2>
<hr>
<p>Multiple<em> processes</em> each with a single <em>thread</em>.</p>
<p>Not limited to <dfn class="dictionary-of-numbers">one node</dfn>.<br>Model will be segmented into <code>-t</code> pieces which should be equal to <code>--ntasks</code>.</p>
<p>Each task could be running on a different node leading to increased communication overhead. Jobs can be limited to a single node by adding  <code style="font-size: 14px;">--nodes=1</code> however this will increase your time in the queue as contiguous cpu's are harder to schedule.</p>
</td>
<td>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name          Fluent-Dis
#SBATCH --time              00:05:00          # Walltime<br>#SBATCH --licenses          aa_r@uoa_foe:1,aa_r_hpc@uoa_foe:20<br>##One research license, (ntasks-16) hpc licenses<br>#SBATCH --<span class="wysiwyg-color-red">nodes</span>             1                 # Limit to n nodes (Optional)
#SBATCH --<span class="wysiwyg-color-red">ntasks</span>            8                 # Number processes<br>#SBATCH --cpus-per-task     <span class="wysiwyg-color-red">1</span>                 # Double if hyperthreading enabled
#SBATCH --mem<span class="wysiwyg-color-red">-per-cpu</span>       1500              # Fine for small jobs; increase if needed
#SBATCH --hint              nomultithread     # Hyperthreading disabled

module load ANSYS/19.2
JOURNAL_FILE=/share/test/ansys/fluent/wing.in
fluent 3ddp -g -t ${SLURM_NTASKS} -i ${JOURNAL_FILE}<br></code></pre>
</td>
</tr>
</tbody>
</table>
<blockquote class="blockquote-tip">
<h3>Useful Links</h3>
<ul>
<li><a href="https://www.sharcnet.ca/Software/Ansys/16.2.3/en-us/help/flu_gs/flu_ug_sec_startup_option.html" target="_self">All command line options.</a></li>
</ul>
</blockquote>
<h2>Interactive</h2>
<p>While it will always be more time and resource efficient using a slurm script as shown above, there are occasions where the GUI is required. If you only require a few CPUs for a short while you may run the fluent on the login node, otherwise use of an <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001316356" target="_self">slurm interactive session</a> is recommended. </p>
<p>For example.</p>
<pre><code>salloc --job-name flUI --nodes 4 --ntasks-per-node 8 --mem-per-cpu 1500 --time 04:00:00</code></pre>
<p>Will return;</p>
<pre><samp>  salloc: Pending job allocation 10270935
  salloc: job 10270935 queued and waiting for resources
  salloc: job 10270935 has been allocated resources
  salloc: Granted job allocation 10270935
  salloc: Waiting for resource configuration
  salloc: Nodes wbn[053-056] are ready for job
</samp></pre>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>Include all the commands you would usually use in your slurm header here.</p>
</blockquote>
<p>Once you have your allocation, run the command</p>
<pre><code>fluent
</code></pre>
<p>You will then be presented with the launcher, make any necessary changes then click launch.</p>
<p>If everything has set up correctly you should see a printout of the hostnames with the resources requested. Note: 'host' should be mahuika0[1-2].</p>
<pre><code>n24-31 wbn056 8/72 Linux-64 71521-71528 Intel(R) Xeon(R) E5-2695 v4
 n16-23 wbn055 8/72 Linux-64 52264-52271 Intel(R) Xeon(R) E5-2695 v4
 n8-15 wbn054 8/72 Linux-64 177090-177097 Intel(R) Xeon(R) E5-2695 v4
 n0-7 wbn053 8/72 Linux-64 48376-48384 Intel(R) Xeon(R) E5-2695 v4
 host mahuika01 Linux-64 185962 Intel(R) Xeon(R) E5-2695 v4
</code></pre>
<blockquote class="blockquote-warning">
<h3>Important</h3>
<p>Closing the fluent GUI will not end the SLURM interactive session. Use <code>exit</code> or <code>scancel <em>jobid</em></code> when finished, else you will continue to 'use' the requested CPUs.</p>
</blockquote>
<h2>Checkpointing</h2>
<p>It is best practice when running long jobs to enable autosaves.</p>
<pre><span>/file/autosave/data-frequency &lt;n&gt;</span></pre>
<p>Where <code>&lt;n&gt;</code> is the number of iterations to run before creating a save.</p>
<p>In order to save disk space you may also want to include the line </p>
<div class="highlight-default notranslate">
<div class="highlight">
<pre><span class="n">/file</span><span class="o">/</span><span class="n">auto</span><span class="o">-</span><span class="n">save</span><span class="o">/</span><span class="n">retain</span><span class="o">-</span><span class="n">most</span><span class="o">-</span><span class="n">recent</span><span class="o">-</span><span class="n">files</span> <span class="n">yes</span>
</pre>
</div>
</div>
<h2>Interrupting</h2>
<p>Including the following code at the top of your journal file will allow you to interrupt the job.</p>
<pre>(set! checkpoint/exit-filename "./exit-fluent")</pre>
<p>Creating a file named <code>exit-fluent</code> in the run directory will cause the job to save the current state and exit (<code>touch exit-fluent</code>). This will also write a new journal file called <code>restart.inp</code> that restarts the simulation at that point.</p>
<h2>User Defined Functions</h2>
<p>When compiling code, make sure to <code>module load gimkl</code> in addition to the ANSYS module.</p>
<h3>Case Definition</h3>
<p>When setting up the case file on your local machine, make sure you select 'Compiled UDF', and select the `.c` source file. You can also specify the name of the library, the default being 'libudf', if possible you should stick with the default name.</p>
<p>Make sure all names follows unix naming conventions (no spaces or special characters) and are the same on the cluster as when you defined it.</p>
<p>It will also save you time if the that the path to your UDF source is <em>relative</em>. The easiest way to do this is to have the source file in the same directory as your <code>.cas</code> file, then specify <em>only the name as your UDF source</em>.</p>
<p>When calling a function, make sure you select the compiled NOT the interpreted version.</p>
<p>`udf funcName` is funcName as being interpreted directly from your `.c` source file.</p>
<p>`udf funcName::libudf` is funcName as compiled in library `libudf`</p>
<h3>Compilation</h3>
<p>When running in a new environment for the first time (local machine, Mahuika, Maui), the C code will have to first be compiled. The compiled code will be placed in a directory with the name of the library (by default this will be <code>libudf/</code>.</p>
<p><em>If you copied the compiled library from a different environment, you will have to delete this directory first.</em></p>
<p>If the compiled library with the name specified in the case file (e.g. <code>libudf/</code>) is not found, fluent will try to compile it from the specified source file.</p>
<p>If for some reason the UDF does not compile automatically, you can manually build it with the following command in your fluent journal file (should go before loading model).</p>
<pre><code>define/user-defined/compiled-functions compile "&lt;libname&gt;" yes "&lt;source_file_1&gt;" "&lt;source_file_n&gt;" "&lt;header_file_1&gt;" "&lt;header_file_n&gt;" "" ""</code></pre>
<p>Note, the command must end with two <code>""</code> to indicate there are no more files to add. </p>
<p>As an example </p>
<pre><code>define/user-defined/compiled-functions compile "libudf" yes "myUDF.c" "" ""</code></pre>
<p>Will compile the code <code>myUDF.c</code> into a library named <code>libudf</code></p>
<h3>Loading File</h3>
<pre><code>define/user-defined/compiled-functions load libudf</code></pre>
<p>Will load the library <code>libudf</code> to be accessible by ANSYS.</p>
<h3>UDF errors</h3>
<pre><code>Error: chip-exec: function</code></pre>
<p>might be using interpreted func</p>
<p>solution specify as relative path, or unload compiled lib before saving .cas file.</p>
<h1 id="ansys-CFX">CFX</h1>
<p><code>cfx5solve -help</code> for a list of commands.</p>
<table>
<tbody>
<tr>
<td>
<h2>Serial Example</h2>
<hr>
<p>Single <em>process</em> with a single <em>thread </em><dfn class="dictionary-of-numbers">(2 threads if hyperthreading </dfn>enabled).</p>
<p>Usually submitted as part of an array, as in the case of parameter sweeps.</p>
</td>
<td>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      CFX-serial<br>#SBATCH --licenses      aa_r@uoa_foe:1 #One research license.<br>#SBATCH --time          00:05:00          # Walltime
#SBATCH --cpus-per-task <span class="wysiwyg-color-red">1</span>                 # Double if hyperthreading enabled
#SBATCH --<span class="wysiwyg-color-black">mem</span>           512MB             # total mem
#SBATCH --hint          nomultithread     # Hyperthreading disabled

module load ANSYS/19.2
input=/share/test/ansys/cfx/pump.def
cfx5solve -batch -def "$input"</code></pre>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-left">
<h2>Distributed Memory Example</h2>
<hr>
<p>Multiple<em> processes</em> each with a single <em>thread</em>.</p>
<p>Not limited to <dfn class="dictionary-of-numbers">one node</dfn>.<br>Model will be segmented into <code>-np</code> pieces which should be equal to <code>--ntasks</code>.</p>
<p>Each task could be running on a different node leading to increased communication overhead<br>.Jobs can be limited to a single node by adding  <code style="font-size: 14px;">--nodes=1</code> however this will increase your time in the queue as contiguous cpu's are harder to schedule.</p>
</td>
<td>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name          ANSYS-Dis
#SBATCH --time              00:05:00          # Walltime<br>#SBATCH --licenses          aa_r@uoa_foe:1,aa_r_hpc@uoa_foe:20<br>##One research license, (ntasks-16) hpc licenses<br>#SBATCH --<span class="wysiwyg-color-red">nodes</span>             1                 # Limit to n nodes (Optional)
#SBATCH --<span class="wysiwyg-color-red">ntasks</span>            36                # Number processes<br>#SBATCH --cpus-per-task     <span class="wysiwyg-color-red">1</span>                 # Double if hyperthreading enabled
#SBATCH --mem<span class="wysiwyg-color-red">-per-cpu</span>       512MB             # Standard for large partition
#SBATCH --hint              nomultithread     # Hyperthreading disabled

module load ANSYS/19.2
input=/share/test/ansys/mechanical/structural.dat
cfx5solve -batch -def "$input" -part $SLURM_NTASKS<br><br></code></pre>
</td>
</tr>
</tbody>
</table>
<blockquote class="blockquote-tip">
<h3>Tip</h3>
<p>Initial values path specified in '.def' file can be overridden using the <code>-ini &lt;initial-file-path&gt;</code> flag.</p>
</blockquote>
<h2>CFX-Post</h2>
<p>Even when running headless (without a GUI) CFX-Post requires connection to a graphical output. For some cases it may be suitable running CFX-Post on the login node and using your X<dfn class="dictionary-of-numbers">-11 display</dfn>, but for larger batch compute jobs you will need to make use of a dummy X<dfn class="dictionary-of-numbers">-11 server</dfn>.</p>
<p>This is as simple as prepending your command with the X Virtual Frame Buffer command.</p>
<pre><code>xvfb-run cfx5post input.cse</code></pre>
<h1 id="ansys-MAPDL">Mechanical APDL</h1>
<table>
<tbody>
<tr>
<td>
<h2>Serial Example</h2>
<hr>
<p>Single <em>process</em> with a single <em>thread </em><dfn class="dictionary-of-numbers">(2 threads if hyperthreading </dfn>enabled).</p>
<p>Usually submitted as part of an array, as in the case of parameter sweeps.</p>
</td>
<td>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      ANSYS-serial<br><span class="hljs-comment">#SBATCH --licenses aa_r@uoa_foe:1</span>
#SBATCH --time          00:05:00          # Walltime
#SBATCH --<span class="wysiwyg-color-black">mem</span>           1500M             # total mem
#SBATCH --hint          nomultithread     # Hyperthreading disabled

module load ANSYS/2021R2
input=${ANSYS_ROOT}/ansys/data/verif/vm263.dat
mapdl -b -i "$input"</code></pre>
</td>
</tr>
<tr>
<td>
<h2>Shared Memory Example</h2>
<hr>
<p>Single <em>process</em> multiple <em>threads.</em></p>
<p>All threads must be on the same node, limiting scalability.<br>Number of threads is set by <code>-np</code> and should be equal to <code>--cpus-per-task</code>.</p>
<p><br>Not recommended if using more than 8 cores (16 CPUs if hyperthreading enabled).</p>
</td>
<td>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      ANSYS-Shared<br><span class="hljs-comment">#SBATCH --licenses aa_r@uoa_foe:1</span>
#SBATCH --time          00:05:00          # Walltime
#SBATCH <span class="wysiwyg-color-red">--cpus-per-task</span> <span class="wysiwyg-color-red">8</span>                 # Double if hyperthreading enabled
#SBATCH --mem<font color="#ff0000">           12G </font>              # 8 threads at 1500 MB per thread
#SBATCH --hint          nomultithread     # Hyperthreading disabled

module load ANSYS/2021R2
input=${ANSYS_ROOT}/ansys/data/verif/vm263.dat
mapdl -b <span class="wysiwyg-color-red">-np ${SLURM_CPUS_PER_TASK}</span> -i "$input"</code></pre>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-left">
<h2>Distributed Memory Example</h2>
<hr>
<p>Multiple<em> processes</em> each with a single <em>thread</em>.</p>
<p>Not limited to <dfn class="dictionary-of-numbers">one node</dfn>.<br>Model will be segmented into <code>-np</code> pieces which should be equal to <code>--ntasks</code>.</p>
<p>Each task could be running on a different node leading to increased communication overhead<br>.Jobs can be limited to a single node by adding  <code style="font-size: 14px;">--nodes=1</code> however this will increase your time in the queue as contiguous cpu's are harder to schedule.</p>
<p><strong>Distributed Memory Parallel is currently not supported on Māui.</strong></p>
</td>
<td>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name          ANSYS-Dis<br><span class="hljs-comment">#SBATCH --licenses aa_r@uoa_foe:1,aa_r_hpc@uoa_foe:4</span>
#SBATCH --time              00:05:00          # Walltime<br>#SBATCH --<span class="wysiwyg-color-red">nodes</span>             1                 # (OPTIONAL) Limit to n nodes
#SBATCH --<span class="wysiwyg-color-red">ntasks</span>            <span class="wysiwyg-color-red">16</span>                # Number processes<br>#SBATCH --mem<span class="wysiwyg-color-red">-per-cpu</span>       1500
#SBATCH --hint              nomultithread     # Hyperthreading disabled

module load ANSYS/2021R2
input=${ANSYS_ROOT}/ansys/data/verif/vm263.dat
mapdl -b <span class="wysiwyg-color-red">-dis</span> -np <span class="wysiwyg-color-red">${SLURM_NTASKS}</span> -i "$input"</code></pre>
</td>
</tr>
<tr>
<td>
<h2>Distributed Memory Example</h2>
<hr>
<p>Multiple<em> processes</em> each with a single <em>thread</em></p>
</td>
<td> </td>
</tr>
</tbody>
</table>
<p>Not all MAPDL solvers work using distributed memory. </p>
<table style="height: 214px;" width="758">
<tbody>
<tr>
<td style="width: 249.132px;">Sparse</td>
<td style="width: 249.132px;">✔</td>
</tr>
<tr>
<td style="width: 249.132px;">PCG</td>
<td style="width: 249.132px;">✔</td>
</tr>
<tr>
<td style="width: 249.132px;">ICCG</td>
<td style="width: 249.132px;">✖</td>
</tr>
<tr>
<td style="width: 249.132px;">JCG</td>
<td style="width: 249.132px;">✖</td>
</tr>
<tr>
<td style="width: 249.132px;">QMR</td>
<td style="width: 249.132px;">✖</td>
</tr>
<tr>
<td style="width: 249.132px;">Block Lanczos eigensolver</td>
<td style="width: 249.132px;">✖</td>
</tr>
<tr>
<td style="width: 249.132px;">PCG Lanczos eigensolver</td>
<td style="width: 249.132px;">✔</td>
</tr>
<tr>
<td style="width: 249.132px;">Supernode eigensolver</td>
<td style="width: 249.132px;">✖</td>
</tr>
<tr>
<td style="width: 249.132px;">Subspace eigensolver</td>
<td style="width: 249.132px;">✔</td>
</tr>
<tr>
<td style="width: 249.132px;">Unsymmetric eigensolver</td>
<td style="width: 249.132px;">✔</td>
</tr>
<tr>
<td style="width: 249.132px;">Damped eigensolver</td>
<td style="width: 249.132px;">✔</td>
</tr>
<tr>
<td style="width: 249.132px;">QRDAMP eigensolver</td>
<td style="width: 249.132px;">✖</td>
</tr>
<tr>
<td style="width: 249.132px;">Element formulation</td>
<td style="width: 249.132px;">✔</td>
</tr>
<tr>
<td style="width: 249.132px;">Results calculation</td>
<td style="width: 249.132px;">✔</td>
</tr>
<tr>
<td style="width: 249.132px;">Pre/Postprocessing</td>
<td style="width: 249.132px;">✖</td>
</tr>
</tbody>
</table>
<blockquote class="blockquote-tip">
<h3>Useful Links</h3>
<ul>
<li><a href="https://www.sharcnet.ca/Software/Ansys/17.0/en-us/help/ans_ope/Hlp_G_OPE3_1.html" target="_self">All command line options.</a></li>
<li><a href="https://www.sharcnet.ca/Software/Fluent14/help/ans_cmd/Hlp_C_CmdTOC.html" target="_self">All MAPDL commands.</a></li>
<li><a href="https://www.sharcnet.ca/Software/Ansys/16.2.3/en-us/help/ans_prog/S7K4r190lcd.html" target="_self">Debug options.</a></li>
<li><a href="https://www.sharcnet.ca/Software/Ansys/16.2.3/en-us/help/ans_dan/dantoc.html" target="_self">MAPDL Parallel Processing Guide</a></li>
</ul>
</blockquote>
<h1 id="ansys-ls-dyna">LS-DYNA</h1>
<h2 id="ansys-fluid-structure-interaction">Fluid-Structure Example</h2>
<pre><code class="bash">#!/bin/bash -e
#SBATCH --job-name      LS-DYNA
#SBATCH --account       nesi99999         # Project Account
#SBATCH --time          01:00:00          # Walltime
#SBATCH --ntasks        16                # Number of CPUs to use
#SBATCH --mem-per-cpu   512MB             # Memory per cpu
#SBATCH --hint          nomultithread     # No hyperthreading

module load ANSYS/18.1
input=3cars_shell2_150ms.k
lsdyna -dis -np $SLURM_NTASKS i="$input" memory=$(($SLURM_MEM_PER_CPU/8))M
</code></pre>
<h1 id="ansys-multiphysics">Multiphysics</h1>
<h3>Example - MAPDL Fluent Interaction</h3>
<pre><code class="bash">#!/bin/bash -e
#SBATCH --job-name      ANSYS_FSI
#SBATCH --account       nesi99999         # Project Account
#SBATCH --time          01:00:00          # Walltime
#SBATCH --ntasks        16                # Number of CPUs to use
#SBATCH --mem-per-cpu   2GB               # Memory per CPU
#SBATCH --hint          nomultithread     # No hyperthreading

module load ANSYS/18.1

COMP_CPUS=$((SLURM_NTASKS-1))
MECHANICAL_CPUS=1
FLUID_CPUS=$((COMP_CPUS-MECHANICAL_CPUS))
export SLURM_EXCLUSIVE="" # don't share CPUs
echo "CPUs: Coupler:1 Struct:$MECHANICAL_CPUS Fluid:$FLUID_CPUS"

echo "STARTING SYSTEM COUPLER"

cd Coupling

# Run the system coupler in the background.
srun -N1 -n1 $WORKBENCH_CMD \
    ansys.services.systemcoupling.exe \
    -inputFile coupling.sci || scancel $SLURM_JOBID &amp;
cd ..
serverfile="$PWD/Coupling/scServer.scs"

while [[ ! -f "$serverfile" ]] ; do
    sleep 1 # waiting for SC to start
done
sleep 1

echo "PARSING SYSTEM COUPLER CONFIG"

{
    read hostport
    port=${hostport%@*}
    node=${hostport#*@}
    read count
    for solver in $(seq $count)
    do
        read solname
        read soltype
        case $soltype in 
            Fluid) fluentsolname=$solname;;
            Structural) mechsolname=$solname;;
        esac
    done
} &lt; "$serverfile"

echo " Port number: $port"
echo " Node name: $node"
echo " Fluent name: $fluentsolname"
echo " Mechanical name: $mechsolname"

echo "STARTING ANSYS"

cd Structural

# Run ANSYS in the background, alongside the system coupler and Fluent.
mapdl -b -dis -mpi intel -np $MECHANICAL_CPUS \
    -scport $port -schost $node -scname "$mechsolname" \
    -i "structural.dat" &gt; struct.out || scancel $SLURM_JOBID &amp;
cd ..

sleep 2
echo "STARTING FLUENT"

cd FluidFlow

# Run Fluent in the background, alongside the system coupler and ANSYS.
fluent 3ddp -g -t$FLUID_CPUS \
    -scport=$port -schost=$node -scname="$fluentsolname" \
    -i "fluidFlow.jou" &gt; fluent.out || scancel $SLURM_JOBID &amp;
cd ..

# Before exiting, wait for all background tasks (the system coupler, ANSYS and
# Fluent) to complete.
wait
</code></pre>
<h1 id="fensap">FENSAP-ICE</h1>
<p>FENSAP-ICE is a fully integrated ice-accretion and aerodynamics simulator.</p>
<p>Currently FENSAP-ICE is only available on Mahuika and in ANSYS 19.2.</p>
<p>The following FENSAP solvers are compatible with MPI</p>
<ul>
<li>FENSAP</li>
<li>DROP<dfn class="dictionary-of-numbers">3D</dfn>
</li>
<li>ICE<dfn class="dictionary-of-numbers">3D</dfn>
</li>
<li>C<dfn class="dictionary-of-numbers">3D</dfn>
</li>
<li>OptiGrid</li>
</ul>
<h2>Case setup<span style="font-size: 15px;"> </span>
</h2>
<h2>With GUI</h2>
<p>If you have set up X<dfn class="dictionary-of-numbers">-11 forwarding</dfn>, you may launch the FENSAP ice using the command <code>fensapiceGUI</code> from within your FENSAP project directory. </p>
<table style="height: 44px;" width="590">
<tbody>
<tr>
<td style="width: 291px;">
<p>1. Launch the run and select the desired number of (physical) CPUs.</p>
<p>2. Open the 'configure' panel.</p>
</td>
<td style="width: 292px;"><img src="https://support.nesi.org.nz/hc/article_attachments/360002865836/FENSAP_GUI1.png" alt="FENSAP_GUI1.png"></td>
</tr>
<tr>
<td style="width: 291px;">
<p>3. Under 'Additional mpirun parameters' add your inline SLURM options. You should include at least.</p>
<pre><code>--job-name <em>my_job</em>
--mem-per-cpu <em>memory</em>
--time <em>time</em>
--licenses <em>required licences</em>
--hint nomultithread </code></pre>
<p>Note: All these parameters will be applied to <em>each individual step</em>.</p>
<p>4. Start the job. You can track progress under the 'log' tab.</p>
</td>
<td style="width: 292px;"><img src="https://support.nesi.org.nz/hc/article_attachments/360002865816/FENSAP_GUI2.png" alt="FENSAP_GUI2.png"></td>
</tr>
</tbody>
</table>
<p>You may close your session and the job will continue to run on the compute nodes. You will be able to view the running job at any time by opening the GUI within the project folder.</p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Note</h3>
<p>Submitting your job through the use of the GUI has disadvantages and may not be suitable in all cases.</p>
<ul>
<li>Closing the session or losing connection will prevent the next stage of the job starting (currently executing step will continue to run).  It is a good idea to launch the GUI inside a tmux/screen session then send the process to background to avoid this.</li>
<li>Each individual step will be launched with the same parameters given in the GUI.</li>
<li>By default 'restart' is set to disabled. If you wish to continue a job from a given step/shot you must select so in the dropdown menu.</li>
</ul>
</blockquote>
<h2 id="fensap2slurm">Using fensap<dfn class="dictionary-of-numbers">2slurm</dfn>
</h2>
<p>Set up your model as you would normally, except rather than starting the run just click 'save'. You <em>do not</em> need to set number of CPUs or MPI configuration.<br>Then in your terminal type <code>fensap2slurm path/to/project</code> or run <code>fensap2slurm</code> from inside the run directory.</p>
<p>This will generate a template file for each stage of the job, edit these as you would a normal SLURM script and set the resources requirements.</p>
<p>For your first shot, it is a good idea to set <code>CONTINUE=FALSE</code> for the last stage of the shot, that way you can set more accurate resource requirements for the remainder.</p>
<p>The workflow can then by running <code>.solvercmd</code> e.g <code>bash .solvercmd</code>. Progress can be tracked through the GUI as usual. </p>
<h1 id="ansysEM">ANSYS-Electromagnetic</h1>
<p>ANSYS-EM jobs can be submitted through a slurm script or by <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001316356" target="_blank" rel="noopener">interactive session</a>.</p>
<h2>RSM</h2>
<p>Unlike other ANSYS applications ANSYS-EM requires RSM (remote solver manager) running on all nodes. The command <code>startRSM</code> has been writ<dfn class="dictionary-of-numbers">ten to facilitate this </dfn>and needs to be run <em>after</em> starting the slurm job but <em>before</em> running edt. Please contact NeSI support if the command is not working for you.</p>
<h2>Example Slurm Script</h2>
<div>
<pre><code>#!/bin/bash -e<br><br>#SBATCH --time                04:00:00<br>#SBATCH --nodes               2<br>#SBATCH --ntasks-per-node     36<br>#SBATCH --mem-per-cpu         1500<br><br>module load ANSYS/19.1<br>INPUTNAME="Sim1.aedt"<br>startRSM<br><br>ansysedt -ng -batchsolve -distributed -machinelistfile=".machinefile" -batchoptions "HFSS/HPCLicenseType=Pool" $INPUTNAME<br></code></pre>
</div>
<p>All batch options can be listed using</p>
<pre><code>ansysedt -batchoptionhelp</code></pre>
<p>(Note, this requires a working X-server) </p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Note</h3>
<p>Each batch option must have it's own flag, e.g.</p>
<pre><code>-batchoptions "HFSS/HPCLicenseType=Pool" -batchoptions "Desktop/ProjectDirectory=$PWD" -batchoptions "HFSS/MPIVendor=Intel"</code></pre>
</blockquote>
<h2>Interactive</h2>
<p>First start an interactive slurm session.</p>
<pre><code>salloc --job-name edt_interactive --nodes 2 --ntasks-per-node 36 --mem-per-cpu 1500</code></pre>
<p>Then load your desired version of ANSYS</p>
<pre><code>module load ANSYS/19.2</code></pre>
<p>Run the script to start startRSM, this will start ANSYS remote solver on your requested nodes, and set the environment variable <code>MACHINELIST</code>.</p>
<pre><code>startRSM</code></pre>
<p>Then launch ansys edt with the following flags</p>
<div>
<pre><code>ansysedt -machinelist file=".machinefile" -batchoptions "HFSS/HPCLicenseType=Pool HFSS/MPIVendor=Intel HFSS/UseLegacyElectronicsHPC=1"</code></pre>
</div>
<h1 id="best-practices">Best Practices</h1>
<h2 id="gpu-acceleration-support">GPU acceleration support</h2>
<p>GPUs can be slow for smaller jobs because it takes time to transfer data from the main memory to the GPU memory. We therefore suggest that you only use them for larger jobs, unless benchmarking reveals otherwise.</p>
<h2 id="interactive-use">Interactive use</h2>
<p>It is best to use journal files <em>etc</em> to automate ANSYS so that you can submit batch jobs, but when interactivity is really needed alongside more CPU power and/or memory than is reasonable to take from a login node (maybe postprocessing a large output file) then an alternative which may work is to run the GUI frontend on a login node while the MPI tasks it launches run on a compute node. This requires using <em>salloc</em> instead of <em>sbatch</em>, for example:</p>
<pre><code class="bash">salloc -A nesi99999 -t 30 -n 16 -C avx --mem-per-cpu=512MB bash -c 'module load ANSYS; fluent -v3ddp -t$SLURM_NTASKS' 
</code></pre>
<p>As with any job, you may have to wait a while before the resource is granted and you can begin, so you might want to use the --mail-type=BEGIN and --mail-user= options.</p>
<h2>Hyperthreading</h2>
<p>Utilising hyperthreading (ie: removing the "--hint=nomultithread" sbatch directive and doubling the number of tasks) will give a small speedup on most jobs with less than <dfn class="dictionary-of-numbers">8 cores</dfn>, but also doubles the number of <code>aa_r_hpc</code> license tokens required.</p>