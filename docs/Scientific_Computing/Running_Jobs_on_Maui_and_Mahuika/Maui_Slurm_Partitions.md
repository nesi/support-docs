---
created_at: '2018-05-21T03:32:04Z'
hidden: false
weight: 11
tags:
- maui
- slurm
title: "M\u0101ui Slurm Partitions"
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000204116
zendesk_section_id: 360000030876
---

!!! tip
     Partitions on these systems that may be used for NeSI workloads carry
     the prefix `nesi_`.

<!-- ## Definitions

**CPU** - A logical core, also known as a hardware thread. Referred to
as a "CPU" in the Slurm documentation.  Since
[Hyperthreading](https://support.nesi.org.nz/hc/en-gb/articles/360000568236/)
is enabled, there are two CPUs per physical core, and every task— and
therefore every job — is allocated an even number of CPUs.

**Job:** A running batch script and any other processes which it might
launch with *srun*.

**Node: **A single computer within the cluster with its own CPUs and RAM
(memory), and sometimes also GPUs. A node is analogous to a workstation
(desktop PC) or laptop.

**Walltime: **Real world time, as opposed to CPU time (walltime x CPUs).
 -->
## Māui (XC50) Slurm Partitions

Nodes are not shared between jobs on Māui, so the minimum charging unit
is node-hours, where 1 node-hour is 40 core-hours, or 80 Slurm
CPU-hours.

There is only one partition available to NeSI jobs:

<table >
<colgroup>
<col />
<col />
<col />
<col />
<col />
<col />
</colgroup>
<tbody>
<tr >
<td
> Name </td>
<td
>Nodes</td>
<td >Max
Walltime</td>
<td >Avail /
Node</td>
<td >Max /
Account</td>
<td
>Description</td>
</tr>
<tr >
<td
>nesi_research</td>
<td
>316</td>
<td >24
hours</td>
<td >80
CPUs
90 or 180 GB RAM</td>
<td >240
nodes
1200 node-hours running</td>
<td
>Standard
partition for all NeSI jobs.<br />
<br />
</td>
</tr>
</tbody>
</table>

### Limits

As a consequence of the above limit on the node-hours reserved by your
running jobs (*GrpTRESRunMins* in Slurm documentation, shown in `squeue`
output when you hit it as the reason "*AssocGrpCPURunMinutes"* ) you can
occupy more nodes simultaneously if your jobs request a shorter time
limit:

| nodes | hours | node-hours | limits reached             |
| ----- | ----- | ---------- | -------------------------- |
| 1     | 24    | 24         | 24 hours                   |
| 50    | 24    | 1200       | 1200 node-hours, 24 hours  |
| 100   | 12    | 1200       | 1200 node-hours            |
| 240   | 5     | 1200       | 1200 node-hours, 240 nodes |
| 240   | 1     | 240        | 240 nodes                  |

Most of the time [job
priority](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Job_prioritisation.md) will
be the most important influence on how long your jobs have to wait - the
above limits are just backstops to ensure that Māui's resources are not
all committed too far into the future, so that debug and other
higher-priority jobs can start reasonably quickly.

### Debug QoS

Each job has a "QoS", with the default QoS for a job being determined by
the [allocation
class](https://support.nesi.org.nz/hc/en-gb/articles/360000202535-Overview)
of its project. Specifying `--qos=debug` will override that and give the
job high priority, but is subject to strict limits: 15 minutes per
job, and only 1 job at a time per user. Debug jobs are limited to 2
nodes.

## Māui\_Ancil (CS500) Slurm Partitions

<table >
<colgroup>
<col />
<col />
<col />
<col />
<col />
<col />
<col />
</colgroup>
<tbody>
<tr >
<td
>Name</td>
<td
>Nodes</td>
<td >Max
Walltime</td>
<td >Avail /
Node</td>
<td >Max /
Job</td>
<td >Max /
User</td>
<td
>Description</td>
</tr>
<tr >
<td
>nesi_prepost</td>
<td
>4</td>
<td >24
hours</td>
<td >80
CPUs
720 GB RAM</td>
<td >20
CPUs
700 GB RAM</td>
<td >80
CPUs
700 GB RAM</td>
<td >Pre and
post processing tasks.</td>
</tr>
<tr >
<td
>nesi_gpu</td>
<td >4 to
5</td>
<td >72
hours</td>
<td >4
CPUs
12 GB RAM
1 P100 GPU*</td>
<td >4
CPUs
12 GB RAM
1 P100 GPU</td>
<td >4
CPUs
12 GB RAM
1 P100 GPU</td>
<td >GPU
jobs and visualisation. </td>
</tr>
<tr >
<td
>nesi_igpu</td>
<td >0 to
1</td>
<td >2
hours</td>
<td >4
CPUs
12 GB RAM
1 P100 GPU*</td>
<td >4
CPUs
12 GB RAM
1 P100 GPU</td>
<td >4
CPUs
12 GB RAM
1 P100 GPU</td>
<td
>Interactive
GPU access 7am - 8pm.</td>
</tr>
</tbody>
</table>

\* NVIDIA Tesla P100 PCIe 12GB card

### Requesting GPUs

Nodes in the `nesi_gpu` partition have 1 P100 GPU card each. You can
request it using:

``` sl
#SBATCH --partition=nesi_gpu
#SBATCH --gpus-per-node=1
```

Note that you need to specify the name of the partition.  You also need
to specify a number of CPUs and amount of memory small enough to fit on
these nodes.

See [GPU use on NeSI](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/GPU_use_on_NeSI.md)
for more details about Slurm and CUDA settings.
