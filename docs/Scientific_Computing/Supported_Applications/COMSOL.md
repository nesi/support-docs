---
created_at: '2019-03-26T00:36:24Z'
hidden: false
position: 27
tags:
- engineering
- COMSOL
title: COMSOL
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000871556
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

``` sl
comsol --help
```

Will display a list of COMSOL batch commands.
!!! prerequisite Useful Links
     -   [Running COMSOL in parallel on
         clusters.](https://www.comsol.com/support/knowledgebase/1001/)
     -   [Running parametric sweeps, batch sweeps, and cluster sweeps from
         the command
         line.](https://www.comsol.com/support/knowledgebase/1250/)
     -   [COMSOL and
         Multithreading.](https://www.comsol.com/support/knowledgebase/1096/)

## Batch Submission

When using COMSOL batch the following flags can be used to control
distribution. 

|                         |                                                                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `-mpibootstrap slurm`   |  Instructs COMSOL to get it's settings from SLURM                                                                                |
| `-np <cpus>`            | Number of CPUs to use in each task. Equivalent to slurm input `--cpus-per-task` or environment variable `${SLURM_CPUS_PER_TASK}` |
| `-nn <tasks>`           | Number of tasks total. `--ntasks` or `${SLURM_NTASKS}`                                                                           |
| `-nnhost <tasks>`       | Number of tasks per node. `--ntasks-per-node` `${SLURM_NTASKS_PER_NODE}`                                                         |
| `-f <path to hostlist>` | Host file. You wont't need to set this in most circumstances.                                                                    |



## Example Scripts

------------------------------------------------------------------------

<table style="height: 481px; width: 811px;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="width: 506px"><h2 id="serial-example">Serial Example</h2>
<hr />
<p>Single <em>process</em> with a single <em>thread</em></p>
<p>Usually submitted as part of an array, as in the case of parameter
sweeps.</p></td>
<td style="width: 163px"><div class="sourceCode" id="cb1"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name      COMSOL-serial</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --licenses      comsol@uoa_foe </span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time          00:05:00          # Walltime</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem           1512               # total mem</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load COMSOL/5.5</span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a><span class="ex">comsol</span> batch <span class="at">-inputfile</span> my_input.mph</span></code></pre></div></td>
</tr>
<tr class="even">
<td style="width: 506px"><h2 id="shared-memory-example">Shared Memory
Example</h2>
<hr />
<p> </p></td>
<td style="width: 163px"><div class="sourceCode" id="cb2"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name      COMSOL-shared</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --licenses      comsol@uoa_foe </span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time          00:05:00        # Walltime</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --cpus-per-task 8</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem           4G              # total mem</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load COMSOL/5.5</span>
<span id="cb2-10"><a href="#cb2-10" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb2-11"><a href="#cb2-11" aria-hidden="true" tabindex="-1"></a><span class="ex">comsol</span> batch <span class="at">-mpibootstrap</span> slurm <span class="at">-inputfile</span> my_input.mph</span></code></pre></div></td>
</tr>
<tr class="odd">
<td style="width: 506px"><h2 id="distributed-memory-example">Distributed
Memory Example</h2>
<hr />
<p> </p></td>
<td style="width: 163px"><div class="sourceCode" id="cb3"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name      COMSOL-distributed </span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --licenses      comsol@uoa_foe </span></span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time          00:05:00            # Walltime</span></span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --ntasks        8           </span></span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem-per-cpu   1500                # mem per cpu</span></span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load COMSOL/5.5</span>
<span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb3-11"><a href="#cb3-11" aria-hidden="true" tabindex="-1"></a><span class="ex">comsolbatch</span> <span class="at">-mpibootstrap</span> slurm <span class="at">-inputfile</span> my_input.mph</span></code></pre></div></td>
</tr>
<tr class="even">
<td class="wysiwyg-text-align-left" style="width: 506px"><h2
id="hybrid-example">Hybrid Example</h2>
<hr />
<p> </p></td>
<td style="width: 163px"><div class="sourceCode" id="cb4"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name         COMSOL-hybrid </span></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --licenses         comsol@uoa_foe</span></span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time             00:05:00          # Walltime</span></span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --ntasks           4                 # total mem</span></span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --cpus-per-task    16</span></span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem-per-cpu      1500B             # total mem</span></span>
<span id="cb4-9"><a href="#cb4-9" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-10"><a href="#cb4-10" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load COMSOL/5.5</span>
<span id="cb4-11"><a href="#cb4-11" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-12"><a href="#cb4-12" aria-hidden="true" tabindex="-1"></a><span class="ex">comsol</span> batch <span class="at">-mpibootstrap</span> slurm <span class="at">-inputfile</span> my_input.mph</span></code></pre></div></td>
</tr>
</tbody>
</table>
!!! prerequisite Important
     If no output file is set, using `--output` the input file will be
     updated instead.

## Interactive Use

Providing you have [set up
X11](../../../Scientific_Computing/Terminal_Setup/X11_on_NeSI), you can
open the COMSOL GUI by running the command `comsol`.

Large jobs should not be run on the login node.

## Recommendations

COMSOL is relatively smart with it's use of resources, if possible it is
preferable to use `--cpus-per-task` over `--ntasks`

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