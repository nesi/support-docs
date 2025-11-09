---
created_at: '2019-09-22T20:20:07Z'
tags:
 - slurm
title: How busy is the cluster?
status: []
---

You can get the current status of all nodes on a cluster using the
command `sinfo`, you will get a printout like the following.

*The nodelist column has been truncated for readability*

```sh
PARTITION     AVAIL   TIMELIMIT    S:C:T MEMORY   NODES(A/I) NODELIST
genoa         up    21-00:00:00   2:84:2 366694+  62/0       c[001-044],g[01-12],l[01-08]
milan         up    21-00:00:00  4+:16:2 491520+  52/3       mc[046-091,093-100],mg[13-16],ml[10-16]
hugemem       up    21-00:00:00   4:22:2 6100000  1/0        cl17
maintenance   up    21-00:00:00 2+:16+:2 366694+  115/3      c[001-044],cl17,g[01-12],l[01-08],mc[046-091,093-100],mg[13-16],ml[10-16]
```

Each partition has a row for every state it's nodes are currently in.

For example, the `large` partition currently has  **1** `down` node, 
**133** `mixed` nodes,  **7** `allocated` nodes and  **85** `idle`
nodes.

The most common node states you are likely to see are:

|  State      | Description                                                                                                                                               |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `idle`      | All CPUs on this node are unallocated and available for use.                                                                                              |
| `allocated` | All CPUs on this node are currently allocated.                                                                                                            |
| `mixed`     | Some CPUs on this node are unallocated, smaller jobs are likely to land here.                                                                             |
| `down`      | The node is unavailable for use                                                                                                                           |
| `reserved`  | This node has been reserved, and is only available for some users (in the case of the igpu partition, please contact NeSI support if you wish to use it). |
| `draining`  | Jobs are currently running on this node, but is not available for new jobs.                                                                               |

See the Slurm documentation for a
[full list of node states](https://slurm.schedmd.com/archive/{{ config.extra.slurm }}/sinfo.html#lbAG).

If you are interested in the state of one partition in particular you
may want to use the command `squeue -p <partition>` to get the current
queue of the partition `<partition> `.
