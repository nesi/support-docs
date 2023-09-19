---
created_at: '2019-09-22T20:20:07Z'
hidden: false
label_names: []
position: 0
title: How can I see how busy the cluster is?
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001176756
zendesk_section_id: 360000039036
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p>You can get the current status of all nodes on a cluster using the command <code>sinfo</code>, you will get a printout like the following. </p>
<p><em>The nodelist column has been truncated for readability.</em></p>
<pre><code>PARTITION AVAIL JOB_SIZE TIMELIMIT    CPUS S:C:T    NODES   STATE    NODELIST<br><span class="wysiwyg-color-red">large*</span>    up    1-infini 3-00:00:00     72 2:18:2       <span class="wysiwyg-color-red">1   down*</span>      wbn128
<span class="wysiwyg-color-red">large*</span>    up    1-infini 3-00:00:00     72 2:18:2     <span class="wysiwyg-color-red">133   mixed</span>      wbn[009-020...
<span class="wysiwyg-color-red">large*</span>    up    1-infini 3-00:00:00     72 2:18:2       <span class="wysiwyg-color-red">7   allocated</span>  wbn[031,038
<span class="wysiwyg-color-red">large*</span>    up    1-infini 3-00:00:00     72 2:18:2     <span class="wysiwyg-color-red"> 85   idle</span>       wbn[021,037...
long      up    1-infini 21-00:00:0     72 2:18:2      64   mixed      wbn[009-020...
long      up    1-infini 21-00:00:0     72 2:18:2       5   allocated  wbn[031,077...
gpu       up    1-infini 3-00:00:00      8  8:1:1       1   reserved   vgpuwbg004
gpu       up    1-infini 3-00:00:00      8  8:1:1       3   idle       vgpuwbg[001-003]
igpu      up    1-infini 3-00:00:00      8  8:1:1       1   reserved   vgpuwbg004
prepost   up    1-infini    3:00:00     72 2:18:2       2   down*      wbl[003,005]
prepost   up    1-infini    3:00:00     72 2:18:2       2   mixed      wbl[002,010]
prepost   up    1-infini    3:00:00     72 2:18:2       5   allocated  wbl[001,004...
bigmem    up    1-infini 7-00:00:00     72 2:18:2       1   down*      wbl003
bigmem    up    1-infini 7-00:00:00     72 2:18:2       2   mixed      wbl[002,010]
bigmem    up    1-infini 7-00:00:00     72 2:18:2       5   allocated  wbl[001,004...
hugemem   up    1-infini 7-00:00:00    128 4:16:2       1   mixed      wbh001
</code></pre>
<p>Each partition has a row for every state it's nodes are currently in.</p>
<p>For example, the <code>large</code> partition currently has  <strong>1</strong> <code>down</code> node,  <strong>133</strong> <code>mixed</code> nodes,  <strong>7</strong> <code>allocated</code> nodes and  <strong>85</strong> <code>idle</code> nodes.</p>
<p>The most common node states you are likely to see are:</p>
<table style="height: 193px; width: 691px;">
<tbody>
<tr>
<td style="width: 148px;"><code>idle</code></td>
<td style="width: 537px;">All CPUs on this node are unallocated and available for use.</td>
</tr>
<tr>
<td style="width: 148px;"><code>allocated</code></td>
<td style="width: 537px;">All CPUs on this node are currently allocated.</td>
</tr>
<tr>
<td style="width: 148px;"><code>mixed</code></td>
<td style="width: 537px;">Some CPUs on this node are unallocated, smaller jobs are likely to land here.</td>
</tr>
<tr>
<td style="width: 148px;"><code>down</code></td>
<td style="width: 537px;">The node is unavailable for use</td>
</tr>
<tr>
<td style="width: 148px;"><code>reserved</code></td>
<td style="width: 537px;">This node has been reserved, and is only available for some users (in the case of the igpu partition, please contact NeSI support if you wish to use it).</td>
</tr>
<tr>
<td style="width: 148px;"><code>draining</code></td>
<td style="width: 537px;">Jobs are currently running on this node, but is not available for new jobs.</td>
</tr>
</tbody>
</table>
<p>A full list of node states can be found <a href="https://slurm.schedmd.com/sinfo.html#lbAG" target="_self">here</a>.</p>
<p>If you are interested in the state of one partition in particular you may want to use the command <code>squeue -p &lt;partition&gt;</code> to get the current queue of the partition <code>&lt;partition&gt;
</code></p>
<p> </p>