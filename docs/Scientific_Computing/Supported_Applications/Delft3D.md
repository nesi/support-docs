---
created_at: '2020-06-26T06:09:34Z'
hidden: false
label_names: []
position: 11
title: Delft3D
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001593096
zendesk_section_id: 360000040076
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <h1 id="example-scripts">Example scripts</h1>
<table>
<tbody>
<tr>
<td style="width: 506px;">
<h2>Serial</h2>
<hr>
<p>For when only <dfn class="dictionary-of-numbers">one CPU is required</dfn>, generally as part of an <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000690275-Parallel-Execution#t_array" target="_self">job array</a>.</p>
</td>
<td style="width: 163px;">
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      Delft3D<br>#SBATCH --time          00:05:00       # Walltime
#SBATCH --mem           512M           # Total Memory
#SBATCH --hint          nomultithread  # Hyperthreading disabled<br>
module load Delft3D<br>
d_hydro test_input.xml<br></code></pre>
</td>
</tr>
<tr>
<td style="width: 506px;">
<h2>Multi-threaded </h2>
<hr>
<p><span class="wysiwyg-color-black">For domain based decompositions.</span></p>
<p><span class="wysiwyg-color-black">Use <code class="bash">cpus-per-task</code> to allocate resources.</span></p>
<p>Each subdomain runs in a separate<br>thread, inside <dfn class="dictionary-of-numbers">one executable</dfn>. <em>Limited to <dfn class="dictionary-of-numbers">one node</dfn>.</em></p>
</td>
<td style="width: 163px;">
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      Delft3D <br>#SBATCH --time          00:05:00       # Walltime
#SBATCH --<span class="wysiwyg-color-red">cpus-per-task </span>4              
#SBATCH --mem           2G             # Total Memory
#SBATCH --hint          nomultithread  # Hyperthreading disabled

module load Delft3D<br><br>d_hyrdo test_input.xml</code></pre>
</td>
</tr>
<tr>
<td style="width: 506px;">
<h2>MPI</h2>
<hr>
<p>Domain is split automatically in stripwise partitions. <em>Can run across multiple nodes.</em></p>
<p>Use <code class="bash">ntasks</code> to allocate resources.</p>
<p><strong>Cannot</strong> be used in conjunction with:</p>
<ul>
<li>DomainDecomposition</li>
<li>Fluid mud</li>
<li>Coup online</li>
<li>Drogues and moving observation points</li>
<li>Culverts</li>
<li>Power stations with inlet and outlet in different partitions</li>
<li>Non-hydrostatic solvers</li>
<li>Walking discharges</li>
<li><dfn class="dictionary-of-numbers">2D skewed weirs</dfn></li>
<li>max(mmax,nmax)/npart ≤ 4</li>
<li>Roller model</li>
<li>Mormerge</li>
<li>Mass balance polygons</li>
</ul>
</td>
<td style="width: 163px;">
<pre><code class="bash">#!/bin/bash -e

#SBATCH --job-name      Delft3D <br>#SBATCH --time          00:05:00       # Walltime
#SBATCH --<span class="wysiwyg-color-red">ntasks       </span> 4              
#SBATCH --<span class="wysiwyg-color-red">mem-per-cpu</span>   1G             
#SBATCH --hint          nomultithread  # Hyperthreading disabled

module load Delft3D<br><br><span class="wysiwyg-color-red">srun</span> d_hyrdo test_input.xml</code></pre>
</td>
</tr>
</tbody>
</table>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Note</h3>
<p>Trying to use more tasks than there are partitions in your model will cause failure.</p>
</blockquote>