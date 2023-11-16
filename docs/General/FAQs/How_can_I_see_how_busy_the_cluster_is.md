---
created_at: '2019-09-22T20:20:07Z'
hidden: false
position: 0
tags: []
title: How can I see how busy the cluster is?
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001176756
zendesk_section_id: 360000039036
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

You can get the current status of all nodes on a cluster using the
command `sinfo`, you will get a printout like the following. 

*The nodelist column has been truncated for readability.*

``` sl
PARTITION AVAIL JOB_SIZE TIMELIMIT    CPUS S:C:T    NODES   STATE    NODELIST
large*    up    1-infini 3-00:00:00     72 2:18:2       1   down*      wbn128
large*    up    1-infini 3-00:00:00     72 2:18:2     133   mixed      wbn[009-020...
large*    up    1-infini 3-00:00:00     72 2:18:2       7   allocated  wbn[031,038
large*    up    1-infini 3-00:00:00     72 2:18:2      85   idle       wbn[021,037...
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
```

Each partition has a row for every state it's nodes are currently in.

For example, the `large` partition currently has  **1** `down` node, 
**133** `mixed` nodes,  **7** `allocated` nodes and  **85** `idle`
nodes.

The most common node states you are likely to see are:

|             |                                                                                                                                                           |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `idle`      | All CPUs on this node are unallocated and available for use.                                                                                              |
| `allocated` | All CPUs on this node are currently allocated.                                                                                                            |
| `mixed`     | Some CPUs on this node are unallocated, smaller jobs are likely to land here.                                                                             |
| `down`      | The node is unavailable for use                                                                                                                           |
| `reserved`  | This node has been reserved, and is only available for some users (in the case of the igpu partition, please contact NeSI support if you wish to use it). |
| `draining`  | Jobs are currently running on this node, but is not available for new jobs.                                                                               |

A full list of node states can be found
[here](https://slurm.schedmd.com/sinfo.html#lbAG).

If you are interested in the state of one partition in particular you
may want to use the command `squeue -p <partition>` to get the current
queue of the partition `<partition>`

 
