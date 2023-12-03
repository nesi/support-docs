---
created_at: '2019-08-15T05:48:41Z'
hidden: false
position: 42
tags: []
title: OpenSees
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001111156
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

There are three commands with which a OpenSees job can be launched.

-   OpenSees - For running a job in serial (single CPU).
-   OpenSeesSP - Intended for the single analysis of very large models.
-   OpenSeesMP - For advanced parametric studies.

 

More info can be found about running OpenSees in parallel
[here](http://opensees.berkeley.edu/OpenSees/parallel/TNParallelProcessing.pdf).

<table style="height: 481px; width: 811px;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="width: 506px"><h3 id="serial">Serial</h3>
<hr />
<p>Single <em>process</em> with a single <em>thread.</em></p>
<p>Usually submitted as part of an array, as in the case of parameter
sweeps.</p></td>
<td style="width: 163px"><div class="sourceCode" id="cb1"><pre
class="sourceCode bash"><code class="sourceCode bash"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">#!/bin/bash -e</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --job-name      OpenSees-Serial</span></span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --time          00:05:00          # Walltime</span></span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --cpus-per-task 1                 # Double if hyperthreading enabled</span></span>
<span id="cb1-6"><a href="#cb1-6" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --mem           512MB             # total mem</span></span>
<span id="cb1-7"><a href="#cb1-7" aria-hidden="true" tabindex="-1"></a><span class="co">#SBATCH --hint          nomultithread     # Hyperthreading disabled</span></span>
<span id="cb1-8"><a href="#cb1-8" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-9"><a href="#cb1-9" aria-hidden="true" tabindex="-1"></a><span class="ex">module</span> load OpenSees</span>
<span id="cb1-10"><a href="#cb1-10" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb1-11"><a href="#cb1-11" aria-hidden="true" tabindex="-1"></a><span class="va">input</span><span class="op">=</span><span class="st">&quot;frame.tcl&quot;</span></span>
<span id="cb1-12"><a href="#cb1-12" aria-hidden="true" tabindex="-1"></a><span class="ex">OpenSees</span> <span class="va">${input}</span></span></code></pre></div></td>
</tr>
</tbody>
</table>



## Input from Shell

Information can be passed from the bash shell to a Tcl script by use of
environment variables.

Set in Slurm script:

``` bash
export MY_VARIABLE="Hello World!"
```

Retrieved in Tcl script:

``` sl
puts $::env(MY_VARIABLE)
```

 

 