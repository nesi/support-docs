---
created_at: '2019-08-14T05:49:00Z'
hidden: false
weight: 6
tags: []
title: How do I request memory?
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001108756
zendesk_section_id: 360000039036
---

- `--mem`: Memory per node
- `--mem-per-cpu`: Memory per [logical CPU](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Hyperthreading.md)

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

<table>
<tbody>
<tr>
<th>Job type</th>
<th>Requested tasks<br> (<code>-n</code>, <code>--ntasks</code>)</th>
<th>Requested logical CPUs per task<br> (<code>--cpus-per-task</code>)</th>
<th>Requested nodes (<code>-N</code>, <code>--nodes</code>)</th>
<th>Requested tasks per node<br> (<code>--ntasks-per-node</code>)</th>
<th>Preferred memory format</th>
<th>Ideal value</th>
</tr>
<tr>
<td>Serial</td>
<td>1 (or unspecified)</td>
<td>1 (or unspecified)</td>
<td>(Irrelevant, but should not be specified)<sup>1</sup></td>
<td>(Irrelevant, but should not be specified)<sup>2</sup></td>
<td><code>--mem=</code></td>
<td>Peak memory<sup>3</sup> needed by the program</td>
</tr>
<tr>
<td>Multithreaded (e.g. OpenMP), but not MPI</td>
<td>1 (or unspecified)</td>
<td>&gt; 1</td>
<td>(Irrelevant, but should not be specified)<sup>1</sup></td>
<td>(Irrelevant, but should not be specified)<sup>2</sup></td>
<td><code>--mem=</code></td>
<td>Peak memory<sup>3</sup> needed by the program</td>
</tr>
<tr>
<td>MPI, evenly split between nodes (recommended method)</td>
<td>Unspecified<sup>4</sup></td>
<td>≥ 1 (or unspecified)</td>
<td>≥ 1<sup>5</sup></td>
<td>≥ 1<sup>5</sup></td>
<td><code>--mem=</code></td>
<td>(Peak memory<sup>3</sup> needed per MPI task)&nbsp;× (number of tasks per node)</td>
</tr>
<tr>
<td>MPI, evenly split between nodes (discouraged method)</td>
<td>&gt; 1</td>
<td>≥ 1 (or unspecified)</td>
<td>Either 1 or the number of tasks<sup>6</sup></td>
<td>(Irrelevant, but should not be specified)<sup>4</sup></td>
<td><code>--mem=</code></td>
<td>(Peak memory<sup>3</sup> needed per MPI task)&nbsp;× (number of tasks per node)&nbsp;</td>
</tr>
<tr>
<td>MPI, randomly placed</td>
<td>&gt; 1</td>
<td>≥ 1 (or unspecified)</td>
<td>&gt; 1; &lt; number of tasks<sup>6</sup> (or unspecified)</td>
<td>(Irrelevant, but should not be specified)<sup>4</sup></td>
<td><code>--mem-per-cpu=</code></td>
<td>(Peak memory<sup>3</sup> needed per MPI task)&nbsp;÷ (number of logical CPUs per MPI task)</td>
</tr>
</tbody>
</table>

<sup>1</sup> If your job consists of only one task there's no reason to
request a specific number of nodes, and requesting more than one node
will cause you to be charged too much for your job. A one-task job will
be assigned one node by default.

<sup>2</sup> If you don't request a specific number of nodes, it makes
no sense to request a specific number of tasks per node.

<sup>3</sup> It's usually a good idea to request a little more memory
from Slurm than your program absolutely needs, to give your job a buffer
in case its behaviour varies slightly from run to run.

<sup>4</sup> If either `-n` or `--ntasks` is used along with
`--ntasks-per-node`, `--ntasks-per-node` will be silently ignored.

<sup>5</sup> An MPI job that is evenly split between two or more nodes
and that doesn't specify a total number of tasks will need either `-N`
(or `--nodes`) or `--ntasks-per-node`, or both, to be greater than 1;
and both must be positive integers.

<sup>6</sup> If you set `-N` (or `--nodes`) to 1, that is effectively
the same as setting`--ntasks-per-node` the same as`-n` (or `--ntasks`),
and the job is guaranteed to run on a single node. On the other hand, if
you request `-N` (or `--nodes`) to be the same as `-n` (or `--ntasks`),
that is effectively the same as setting `--ntasks-per-node=1`, and the
job will be evenly split between nodes. In either of these cases,
`--mem` is better than`--mem-per-cpu`. Meanwhile, requesting more nodes
than tasks never makes sense.
