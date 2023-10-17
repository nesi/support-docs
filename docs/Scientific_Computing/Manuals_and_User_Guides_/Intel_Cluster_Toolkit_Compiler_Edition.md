---
created_at: '2016-03-14T03:05:27Z'
hidden: true
label_names: []
position: 0
title: Intel Cluster Toolkit Compiler Edition
vote_count: 0
vote_sum: 0
zendesk_article_id: 217566368
zendesk_section_id: 360000040036
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
 !!! Info
     This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->

<div class="toc">
<ul>
<li><a href="#description">Description</a></li>
<li>
<a href="#available-modules">Available modules</a><ul>
<li><a href="#packages-with-modules">Packages with modules</a></li>
</ul>
</li>
<li><a href="#licensing-requirements">Licensing requirements</a></li>
<li><a href="#usage">Usage</a></li>
<li>
<a href="#example-scripts">Example scripts</a><ul>
<li><a href="#example-script-to-compile-code-on-the-pan-cluster">Example script to compile code on the Pan cluster</a></li>
<li><a href="#example-script-to-run-intel-compiled-code-on-the-pan-cluster">Example script to run Intel-compiled code on the Pan cluster</a></li>
</ul>
</li>
</ul>
</div>
<h1 id="description">Description</h1>
<p>The Intel Cluster Toolkit Compiler Edition provides Intel C/C++ and Fortran
compilers, Intel MPI &amp; Intel MKL.</p>
<p>The Intel Cluster Toolkit Compiler Edition home page is at
<a href="http://software.intel.com/en-us/intel-cluster-toolkit-compiler">http://software.intel.com/en-us/intel-cluster-toolkit-compiler</a>.</p>
<h1 id="available-modules">Available modules</h1>
<h2 id="packages-with-modules">Packages with modules</h2>
<table>
  <tr>
    <th>Module</th>
    <th>NeSI Cluster</th>
  </tr>
  <tr>
    <td>intel/2017a</td>
    <td>pan</td>
  </tr>
  <tr>
    <td>intel/2015a</td>
    <td>pan</td>
  </tr>
  <tr>
    <td>intel/2015.02</td>
    <td>pan</td>
  </tr>
  <tr>
    <td>intel/ics-2013</td>
    <td>pan</td>
  </tr>
  <tr>
    <td>intel/2011-64bit</td>
    <td>pan</td>
  </tr>
</table>

<h1 id="licensing-requirements">Licensing requirements</h1>
<p>The Intel Cluster Toolkit has been made available to all NeSI users under the
terms of a commercial, closed-source licence agreement. Any authorised user of
the Pan cluster may use the Intel Cluster Toolkit at no cost, subject to the
terms of the licence. For more information, please get in touch with
<a href="mailto:support@nesi.org.nz">our support desk</a>.</p>
<h1 id="usage">Usage</h1>
<p>The Intel Cluster Toolkit contains some executables, but is not a conventional
software package. Instead, it contains compilers and libraries. Accordingly, it
is most useful when either you wish to use it to compile a program or a library
from source code, or you intend to run a program or library that has been
compiled with it. In the latter case, the main purpose of loading the Intel
Cluster Toolkit is to set up your runtime environment appropriately.</p>
<p>You can use a batch submission script to compile code, in which case you might
use the compiler command (<code>icc</code>, <code>icpc</code>, <code>ifort</code>, etc.) directly, or more likely
you will use a dedicated building workflow package such as <code>make</code> or <code>cmake</code>.
Either way, the compilation will then run on a compute node as if it were a
normal job. Alternatively, you are welcome to build and test your code on one of
the build nodes, bearing in mind that if your package is very large or has
time-consuming tests, it may not finish within the time limits set on the build
nodes.</p>
<p>If you are not compiling a program or library, but are instead running
previously compiled code, it is normally sufficient for you to load the Intel
Cluster Toolkit's module. If the program or library you are running has its own
module, it is likely that the Intel module will be loaded automatically as a
required dependency, and that no further action will be required on your part.</p>
<p>If you load another module, you can always check whether it has loaded the Intel
Compiler module by running</p>
<pre><code class="bash">module list
</code></pre>

<p>and having a look for loaded modules with names such as "intel" and "icc".</p>
<h1 id="example-scripts">Example scripts</h1>
<h2 id="example-script-to-compile-code-on-the-pan-cluster">Example script to compile code on the Pan cluster</h2>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      Compilation_job
#SBATCH --account       nesi99999
#SBATCH --time          01:00:00
#SBATCH --mem-per-cpu   4G
#SBATCH --output        Compilation_job.%j.out # Include the job ID in the names
#SBATCH --error         Compilation_job.%j.err # of the output and error files

module load intel/2015a

# This is a basic compiler command and does not represent the full range of
# compilation options available.
srun icc -o myprog.exe myprog.c

# Perhaps you are building using a Makefile.
srun make
</code></pre>

<h2 id="example-script-to-run-intel-compiled-code-on-the-pan-cluster">Example script to run Intel-compiled code on the Pan cluster</h2>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      Execution_job
#SBATCH --account       nesi99999
#SBATCH --time          01:00:00
#SBATCH --mem-per-cpu   4G
#SBATCH --output        Execution_job.%j.out # Include the job ID in the names
#SBATCH --error         Execution_job.%j.err # of the output and error files

module load intel/2015a

# This command is given for example purposes only and does not suggest that all
# programs compiled with the Intel compilers should be invoked in this manner.
srun myprog.exe inputfile.dat
</code></pre>