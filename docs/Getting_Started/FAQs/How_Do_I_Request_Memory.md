---
created_at: '2019-08-14T05:49:00Z'
tags:
- slurm
- troubleshooting
description: Instructions for requesting memory
---

- `--mem`: Memory per node
- `--mem-per-cpu`: Memory per [logical CPU](../../Software/Parallel_Computing/Simultaneous_Multithreading.md)

In most circumstances, you should request memory using `--mem`. The
exception is if you are running an MPI job that could be placed on more
than one node, with tasks divided up randomly, in which case
`--mem-per-cpu` is more appropriate. More detail is in the following
table, including how you can tell what sort of job you're submitting.

<!-- increase column width to make the table readable -->
<style>
.md-typeset table:not([class]) th {
  min-width: 8rem;
}
</style>
<div role="region" aria-labelledby="table-caption" tabindex="0" style="overflow-x: auto;">
<table>
<caption id="table-caption">Memory request by job type</caption>
<thead>
<tr>
<th scope="col">Job type</th>
<th scope="col">Requested tasks<br> (<code>-n</code>, <code>--ntasks</code>)</th>
<th scope="col">Requested logical CPUs per task<br> (<code>--cpus-per-task</code>)</th>
<th scope="col">Requested nodes (<code>-N</code>, <code>--nodes</code>)</th>
<th scope="col">Requested tasks per node<br> (<code>--ntasks-per-node</code>)</th>
<th scope="col">Preferred memory format</th>
<th scope="col">Ideal value</th>
</tr>
</thead>
<tbody>
<tr>
<th scope="row">Serial</th>
<td>1 (or unspecified)</td>
<td>1 (or unspecified)</td>
<td>(Irrelevant, but should not be specified)<a href="#fn1" id="ref1" aria-describedby="footnote-label"><sup>1</sup></a></td>
<td>(Irrelevant, but should not be specified)<a href="#fn2" id="ref2" aria-describedby="footnote-label"><sup>2</sup></a></td>
<td><code>--mem=</code></td>
<td>Peak memory<a href="#fn3" id="ref3" aria-describedby="footnote-label"><sup>3</sup></a> needed by the program</td>
</tr>
<tr>
<th scope="row">Multithreaded (e.g. OpenMP), but not MPI</th>
<td>1 (or unspecified)</td>
<td>&gt; 1</td>
<td>(Irrelevant, but should not be specified)<a href="#fn1" id="ref1" aria-describedby="footnote-label"><sup>1</sup></a></td>
<td>(Irrelevant, but should not be specified)<a href="#fn2" id="ref2" aria-describedby="footnote-label"><sup>2</sup></a></td>
<td><code>--mem=</code></td>
<td>Peak memory<a href="#fn3" id="ref3" aria-describedby="footnote-label"><sup>3</sup></a> needed by the program</td>
</tr>
<tr>
<th scope="row">MPI, evenly split between nodes (recommended method)</th>
<td>Unspecified<a href="#fn4" id="ref4" aria-describedby="footnote-label"><sup>4</sup></a></td>
<td>≥ 1 (or unspecified)</td>
<td>≥ 1<a href="#fn5" id="ref5" aria-describedby="footnote-label"><sup>5</sup></a></td>
<td>≥ 1<a href="#fn5" id="ref5" aria-describedby="footnote-label"><sup>5</sup></a></td>
<td><code>--mem=</code></td>
<td>(Peak memory<a href="#fn3" id="ref3" aria-describedby="footnote-label"><sup>3</sup></a> needed per MPI task)&nbsp;× (number of tasks per node)</td>
</tr>
<tr>
<th scope="row">MPI, evenly split between nodes (discouraged method)</th>
<td>&gt; 1</td>
<td>≥ 1 (or unspecified)</td>
<td>Either 1 or the number of tasks<a href="#fn6" id="ref6" aria-describedby="footnote-label"><sup>6</sup></a></td>
<td>(Irrelevant, but should not be specified)<a href="#fn4" id="ref4" aria-describedby="footnote-label"><sup>4</sup></a></td>
<td><code>--mem=</code></td>
<td>(Peak memory<a href="#fn3" id="ref3" aria-describedby="footnote-label"><sup>3</sup></a> needed per MPI task)&nbsp;× (number of tasks per node)&nbsp;</td>
</tr>
<tr>
<th scope="row">MPI, randomly placed</th>
<td>&gt; 1</td>
<td>≥ 1 (or unspecified)</td>
<td>&gt; 1; &lt; number of tasks<a href="#fn6" id="ref6" aria-describedby="footnote-label"><sup>6</sup></a> (or unspecified)</td>
<td>(Irrelevant, but should not be specified)<a href="#fn4" id="ref4" aria-describedby="footnote-label"><sup>4</sup></a></td>
<td><code>--mem-per-cpu=</code></td>
<td>(Peak memory<a href="#fn3" id="ref3" aria-describedby="footnote-label"><sup>3</sup></a> needed per MPI task)&nbsp;÷ (number of logical CPUs per MPI task)</td>
</tr>
</tbody>
</table>
</div>

<aside style="margin-top: 20px;">
  <h2 id="footnote-label" style="font-size: 1.2em;">Footnotes</h2>
  <ol>
    <li id="fn1">
      <p>If your job consists of only one task there's no reason to request a specific number of nodes, and requesting more than one node will cause you to be charged too much for your job. A one-task job will be assigned one node by default. <a href="#ref1" aria-label="Back to reference 1">↩</a></p>
    </li>
    <li id="fn2">
      <p>If you don't request a specific number of nodes, it makes no sense to request a specific number of tasks per node. <a href="#ref2" aria-label="Back to reference 2">↩</a></p>
    </li>
    <li id="fn3">
      <p>It's usually a good idea to request a little more memory from Slurm than your program absolutely needs, to give your job a buffer in case its behaviour varies slightly from run to run. <a href="#ref3" aria-label="Back to reference 3">↩</a></p>
    </li>
    <li id="fn4">
      <p>If either `-n` or `--ntasks` is used along with `--ntasks-per-node`, `--ntasks-per-node` will be silently ignored. <a href="#ref4" aria-label="Back to reference 4">↩</a></p>
    </li>
    <li id="fn5">
      <p>An MPI job that is evenly split between two or more nodes and that doesn't specify a total number of tasks will need either `-N` (or `--nodes`) or `--ntasks-per-node`, or both, to be greater than 1; and both must be positive integers. <a href="#ref5" aria-label="Back to reference 5">↩</a></p>
    </li>
    <li id="fn6">
      <p>If you set `-N` (or `--nodes`) to 1, that is effectively the same as setting`--ntasks-per-node` the same as`-n` (or `--ntasks`), and the job is guaranteed to run on a single node. On the other hand, if you  request `-N` (or `--nodes`) to be the same as `-n` (or `--ntasks`), that is effectively the same as setting `--ntasks-per-node=1`, and the job will be evenly split between nodes. In either of these cases, `--mem` is better than`--mem-per-cpu`. Meanwhile, requesting more nodes than tasks never makes sense. <a href="#ref6" aria-label="Back to reference 6">↩</a></p>
    </li>
  </ol>
</aside>
