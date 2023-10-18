---
created_at: '2015-09-02T20:55:32Z'
hidden: true
label_names:
- mahuika
- tier1
- biology
position: 25
title: BEAST
vote_count: 0
vote_sum: 0
zendesk_article_id: 208367078
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

<div class="toc">
<ul>
<li><a href="#description">Description</a></li>
<li>
<a href="#available-modules">Available modules</a><ul>
<li><a href="#packages-with-modules">Packages with modules</a></li>
</ul>
</li>
<li><a href="#license">License</a></li>
<li>
<a href="#example-scripts">Example scripts</a><ul>
<li><a href="#example-script-for-the-pan-cluster">Example script for the Pan cluster</a></li>
<li><a href="#memory">Memory</a></li>
<li><a href="#long-beast-runs">Long BEAST runs</a></li>
</ul>
</li>
</ul>
</div>
<h1 id="description">Description</h1>
<p>Bayesian Evolutionary Analysis Sampling Trees is a cross-platform program for
Bayesian analysis of molecular sequences using MCMC.  The program is orientated
toward (strict and relaxed) molecular clock analyses. It can be used as a method
of constructing phylogenies, but it is also intended for testing evolutionary
hypotheses without conditioning on a single tree topology.  BEAST uses MCMC to
average over tree space, so that each tree is weighted proportional to its
posterior probability. It uses an XML input format  that allows the user to
design and run a large range of models. We also include a program that can
convert NEXUS files into this format.</p>
<p>The BEAST home page is at <a href="http://beast2.org">http://beast2.org</a>.</p>
<h1 id="available-modules">Available modules</h1>
<h2 id="packages-with-modules">Packages with modules</h2>
<table>
  <tr>
    <th>Module</th>
    <th>NeSI Cluster</th>
  </tr>
  <tr>
    <td>BEAST/2.4.7</td>
    <td>pan</td>
  </tr>
  <tr>
    <td>BEAST/1.8.2-goolf-1.5.14</td>
    <td>pan</td>
  </tr>
  <tr>
    <td>BEAST/1.8.4-gimkl-2017a-no-beagle</td>
    <td>pan</td>
  </tr>
  <tr>
    <td>BEAST/2.2.1</td>
    <td>pan</td>
  </tr>
  <tr>
    <td>BEAST/2.4.3</td>
    <td>pan</td>
  </tr>
</table>

<h1 id="license">License</h1>
<p>BEAST is released at no cost under the terms of
<a href="http://www.gnu.org/licenses/lgpl-2.1.html">the GNU Lesser General Public Licence</a>.</p>
<h1 id="example-scripts">Example scripts</h1>
<h2 id="example-script-for-the-pan-cluster">Example script for the Pan cluster</h2>
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      MyBEASTJob
#SBATCH --account       nesi99999
#SBATCH --time          01:00:00
#SBATCH --cpus-per-task 16
#SBATCH --mem-per-cpu   4G
#SBATCH --output        MyBEASTJob.%j.out   # Include the job ID in the names
#SBATCH --error         MyBEASTJob.%j.err   # of the output and error files

module load BEAST/2.2.1

# Here Java is told it can use ( cpus-per-task * mem-per-cpu - 2GB ) = 62GB
export _JAVA_OPTS="-Xms62g -Xmx62g" 

srun beast -beagle -beagle_SSE -threads $SLURM_CPUS_PER_TASK input.xml
</code></pre>

<h2 id="memory">Memory</h2>
<p>Please note the Java options in the above script.  BEAST is a Java program, and Java will not automatically use all the memory which Slurm has allocated for it unless told to do so.</p>
<h2 id="long-beast-runs">Long BEAST runs</h2>
<p>If your Slurm job ends too early you can continue its calculation in a second job by way of the <code>-resume</code> option of BEAST2. For very long BEAST runs it may even make sense to deliberately break it into 1-week segments to get around our limits on maximum job duration.</p>