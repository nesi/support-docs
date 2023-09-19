---
created_at: '2019-08-14T05:49:00Z'
hidden: false
label_names: []
position: 6
title: How do I request memory?
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001108756
zendesk_section_id: 360000039036
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p>In Slurm, there are two ways to request memory for your job:</p>
<ul>
<li>
<code>--mem</code>: Memory per node</li>
<li>
<code>--mem-per-cpu</code>: Memory per <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000568236" target="_self">logical CPU</a>
</li>
</ul>
<p>In most circumstances, you should request memory using <code>--mem</code>. The exception is if you are running an MPI job that could be placed on more than one node, with tasks divided up randomly, in which case <code>--mem-per-cpu</code> is more appropriate. More detail is in the following table, including how you can tell what sort of job you're submitting.</p>
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
<td>(Irrelevant, but should not be specified)<sup>1</sup>
</td>
<td>(Irrelevant, but should not be specified)<sup>2</sup>
</td>
<td><code>--mem=</code></td>
<td>Peak memory<sup>3</sup> needed by the program</td>
</tr>
<tr>
<td>Multithreaded (e.g. OpenMP), but not MPI</td>
<td>1 (or unspecified)</td>
<td>&gt; 1</td>
<td>(Irrelevant, but should not be specified)<sup>1</sup>
</td>
<td>(Irrelevant, but should not be specified)<sup>2</sup>
</td>
<td><code>--mem=</code></td>
<td>Peak memory<sup>3</sup> needed by the program</td>
</tr>
<tr>
<td>MPI, evenly split between nodes (recommended method)</td>
<td>Unspecified<sup>4</sup>
</td>
<td>≥ 1 (or unspecified)</td>
<td>≥ 1<sup>5</sup>
</td>
<td>≥ 1<sup>5</sup>
</td>
<td><code>--mem=</code></td>
<td>(Peak memory<sup>3</sup> needed per MPI task) × (number of tasks per node)</td>
</tr>
<tr>
<td>MPI, evenly split between nodes (discouraged method)</td>
<td>&gt; 1</td>
<td>≥ 1 (or unspecified)</td>
<td>Either 1 or the number of tasks<sup>6</sup>
</td>
<td>(Irrelevant, but should not be specified)<sup>4</sup>
</td>
<td><code>--mem=</code></td>
<td>(Peak memory<sup>3</sup> needed per MPI task) × (number of tasks per node) </td>
</tr>
<tr>
<td>MPI, randomly placed</td>
<td>&gt; 1</td>
<td>≥ 1 (or unspecified)</td>
<td>&gt; 1; &lt; number of tasks<sup>6</sup> (or unspecified)</td>
<td>(Irrelevant, but should not be specified)<sup>4</sup>
</td>
<td><code>--mem-per-cpu=</code></td>
<td>(Peak memory<sup>3</sup> needed per MPI task) ÷ (number of logical CPUs per MPI task)</td>
</tr>
</tbody>
</table>
<p><sup>1</sup> If your job consists of only one task there's no reason to request a specific number of nodes, and requesting more than one node will cause you to be charged too much for your job. A one-task job will be assigned one node by default.</p>
<p><sup>2</sup> If you don't request a specific number of nodes, it makes no sense to request a specific number of tasks per node.</p>
<p><sup>3</sup> It's usually a good idea to request a little more memory from Slurm than your program absolutely needs, to give your job a buffer in case its behaviour varies slightly from run to run.</p>
<p><sup>4</sup> If either <code>-n</code> or <code>--ntasks</code> is used along with <code>--ntasks-per-node</code>, <code>--ntasks-per-node</code> will be silently ignored.</p>
<p><sup>5</sup> An MPI job that is evenly split between two or more nodes and that doesn't specify a total number of tasks will need either <code>-N</code> (or <code>--nodes</code>) or <code>--ntasks-per-node</code>, or both, to be greater than 1; and both must be positive integers.</p>
<p><sup>6</sup> If you set <code>-N</code> (or <code>--nodes</code>) to 1, that is effectively the same as setting<code>--ntasks-per-node</code> the same as<code>-n</code> (or <code>--ntasks</code>), and the job is guaranteed to run on a single node. On the other hand, if you request <code>-N</code> (or <code>--nodes</code>) to be the same as <code>-n</code> (or <code>--ntasks</code>), that is effectively the same as setting <code>--ntasks-per-node=1</code>, and the job will be evenly split between nodes. In either of these cases, <code>--mem</code> is better than<code>--mem-per-cpu</code>. Meanwhile, requesting more nodes than tasks never makes sense.</p>