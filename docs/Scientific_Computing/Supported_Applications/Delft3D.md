---
created_at: '2020-06-26T06:09:34Z'
hidden: false
position: 11
tags: []
title: Delft3D
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001593096
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

# Example scripts

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="width: 506px"><h2 id="serial">Serial</h2>
<hr />
<p>For when only <span>one CPU is required</span>, generally as part of
an <a
href="https://support.nesi.org.nz/hc/en-gb/articles/360000690275-Parallel-Execution#t_array">job
array</a>.</p></td>
<td style="width: 163px"><div class="sourceCode" id="cb1"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name      Delft3D</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time          00:05:00       # Walltime</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem           512M           # Total Memory</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --hint          nomultithread  # Hyperthreading disabled</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load Delft3D</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="ex">d_hydro</span> test_input.xml</span></code></pre></div></td>
</tr>
<tr class="even">
<td style="width: 506px"><h2 id="multi-threaded">Multi-threaded </h2>
<hr />
<p><span>For domain based decompositions.</span></p>
<p><span>Use <code class="sl">cpus-per-task</code> to allocate
resources.</span></p>
<p>Each subdomain runs in a separate<br />
thread, inside <span>one executable</span>. <em>Limited to <span>one
node</span>.</em></p></td>
<td style="width: 163px"><div class="sourceCode" id="cb2"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name      Delft3D </span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time          00:05:00       # Walltime</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --cpus-per-task 4              </span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem           2G             # Total Memory</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --hint          nomultithread  # Hyperthreading disabled</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load Delft3D</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a><span class="ex">d_hyrdo test_input.xml</span></span></code></pre></div></td>
</tr>
<tr class="odd">
<td style="width: 506px"><h2 id="mpi">MPI</h2>
<hr />
<p>Domain is split automatically in stripwise partitions. <em>Can run
across multiple nodes.</em></p>
<p>Use <code class="sl">ntasks</code> to allocate resources.</p>
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
<li><span>2D skewed weirs</span></li>
<li>max(mmax,nmax)/npart ≤ 4</li>
<li>Roller model</li>
<li>Mormerge</li>
<li>Mass balance polygons</li>
</ul></td>
<td style="width: 163px"><div class="sourceCode" id="cb3"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name      Delft3D </span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time          00:05:00       # Walltime</span></span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --ntasks        4              </span></span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem-per-cpu   1G             </span></span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --hint          nomultithread  # Hyperthreading disabled</span></span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load Delft3D</span>
<span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-11"><a href="#cb3-11" aria-hidden="true" tabindex="-1"></a><span class="ex">srun d_hyrdo test_input.xml</span></span></code></pre></div></td>
</tr>
</tbody>
</table>
!!! prerequisite Note
     Trying to use more tasks than there are partitions in your model will
     cause failure.
