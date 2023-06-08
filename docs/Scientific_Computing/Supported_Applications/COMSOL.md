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

    comsol --help

Will display a list of COMSOL batch commands.

> ### Useful Links
>
> -   [Running COMSOL in parallel on
>     clusters.](https://www.comsol.com/support/knowledgebase/1001/)
> -   [Running parametric sweeps, batch sweeps, and cluster sweeps from
>     the command
>     line.](https://www.comsol.com/support/knowledgebase/1250/)
> -   [COMSOL and
>     Multithreading.](https://www.comsol.com/support/knowledgebase/1096/)

# Batch Submission

When using COMSOL batch the following flags can be used to control
distribution. 

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
</tbody>
</table>

#  

# Example Scripts

------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

> ### Important
>
> If no output file is set, using `--output` the input file will be
> updated instead.

# Interactive Use

Providing you have [set up
X11](https://support.nesi.org.nz/hc/en-gb/articles/360001075975), you
can open the COMSOL GUI by running the command `comsol`.

Large jobs should not be run on the login node.

# Recommendations

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
