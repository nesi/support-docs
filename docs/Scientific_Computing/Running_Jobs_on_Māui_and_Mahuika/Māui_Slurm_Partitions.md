---
created_at: '2018-05-21T03:32:04Z'
hidden: false
label_names:
- maui
- slurm
position: 11
title: "M\u0101ui Slurm Partitions"
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000204116
zendesk_section_id: 360000030876
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
 !!! Info
     This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
!!!
>
> Partitions on these systems that may be used for NeSI workloads carry
> the prefix **nesi\_**.

##  

## Definitions

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

##  

## Māui (XC50) Slurm Partitions

Nodes are not shared between jobs on Māui, so the minimum charging unit
is node-hours, where 1 node-hour is 40 core-hours, or 80 Slurm
CPU-hours.

There is only one partition available to NeSI jobs:

<table style="height: 135px; width: 850px;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr class="odd" style="height: 46px;">
<td
style="width: 148.15px; height: 46px"><p><strong> Name </strong></p></td>
<td
style="width: 79.7833px; height: 46px"><p><strong>Nodes</strong></p></td>
<td style="width: 115.8px; height: 46px"><p><strong>Max
Walltime</strong></p></td>
<td style="width: 131.333px; height: 46px"><p><strong>Avail /
Node</strong></p></td>
<td style="width: 131.333px; height: 46px"><p><strong>Max /
Account</strong></p></td>
<td
style="width: 226.6px; height: 46px"><p><strong>Description</strong></p></td>
</tr>
<tr class="even" style="height: 89px;">
<td
style="width: 148.15px; vertical-align: top; height: 89px"><p>nesi_research</p></td>
<td
style="width: 79.7833px; vertical-align: top; height: 89px"><p>316</p></td>
<td style="width: 115.8px; vertical-align: top; height: 89px"><p>24
hours</p></td>
<td style="width: 131.333px; vertical-align: top; height: 89px"><p>80
CPUs</p>
<p>90 or 180 GB RAM</p></td>
<td style="width: 131.333px; vertical-align: top; height: 89px"><p>240
nodes</p>
<p>1200 node-hours running</p></td>
<td
style="width: 226.6px; vertical-align: top; height: 89px"><p>Standard
partition for all NeSI jobs.<br />
<br />
</p></td>
</tr>
</tbody>
</table>

### Limits

As a consequence of the above limit on the node-hours reserved by your
running jobs (*GrpTRESRunMins* in Slurm documentation, shown in `squeue`
output when you hit it as the reason "*AssocGrpCPURunMinutes"* ) you can
occupy more nodes simultaneously if your jobs request a shorter time
limit:

<table style="width: 503.4755859375px;">
<tbody>
<tr class="odd" style="height: 43px;">
<td style="width: 73px; height: 43px"><strong>nodes</strong></td>
<td style="width: 73px; height: 43px"><strong>hours</strong></td>
<td style="width: 120px; height: 43px"><strong>node-hours</strong></td>
<td style="width: 227.4755859375px; height: 43px"><strong>limits
reached</strong></td>
</tr>
<tr class="even" style="height: 14.453857421875px;">
<td style="width: 73px; height: 14.453857421875px">1</td>
<td style="width: 73px; height: 14.453857421875px">24</td>
<td style="width: 120px; height: 14.453857421875px">24</td>
<td style="width: 227.4755859375px; height: 14.453857421875px">24
hours</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 73px; height: 21px">50</td>
<td style="width: 73px; height: 21px">24</td>
<td style="width: 120px; height: 21px">1200</td>
<td style="width: 227.4755859375px; height: 21px">1200 node-hours, 24
hours</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 73px; height: 21px">100</td>
<td style="width: 73px; height: 21px">12</td>
<td style="width: 120px; height: 21px">1200</td>
<td style="width: 227.4755859375px; height: 21px">1200 node-hours</td>
</tr>
<tr class="odd" style="height: 21px;">
<td style="width: 73px; height: 21px">240</td>
<td style="width: 73px; height: 21px">5</td>
<td style="width: 120px; height: 21px">1200</td>
<td style="width: 227.4755859375px; height: 21px">1200 node-hours, 240
nodes</td>
</tr>
<tr class="even" style="height: 21px;">
<td style="width: 73px; height: 21px">240</td>
<td style="width: 73px; height: 21px">1</td>
<td style="width: 120px; height: 21px">240</td>
<td style="width: 227.4755859375px; height: 21px">240 nodes </td>
</tr>
</tbody>
</table>

Most of the time [job
priority](https://support.nesi.org.nz/hc/en-gb/articles/360000201636) will
be the most important influence on how long your jobs have to wait - the
above limits are just backstops to ensure that Māui's resources are not
all committed too far into the future, so that debug and other
higher-priority jobs can start reasonably quickly.

### Debug QoS

Each job has a "QoS", with the default QoS for a job being determined by
the [allocation
class](https://support.nesi.org.nz/hc/en-gb/articles/360000202535-Overview)
of its project. Specifying `--qos=debug` will override that and give the
job very high priority, but is subject to strict limits: 15 minutes per
job, and only 1 job at a time per user. Debug jobs are limited to 2
nodes.

##  

## Māui\_Ancil (CS500) Slurm Partitions

 

<table style="height: 242px; width: 850px;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<tbody>
<tr class="odd" style="height: 46px;">
<td
style="height: 49px; width: 104.55px"><p><strong>Name</strong></p></td>
<td
style="height: 49px; width: 64.35px"><p><strong>Nodes</strong></p></td>
<td style="height: 49px; width: 110.567px"><p><strong>Max
Walltime</strong></p></td>
<td style="height: 49px; width: 110.567px"><p><strong>Avail /
Node</strong></p></td>
<td style="height: 49px; width: 111.583px"><p><strong>Max /
Job</strong></p></td>
<td style="height: 49px; width: 110.583px"><p><strong>Max /
User</strong></p></td>
<td
style="height: 49px; width: 159.8px"><p><strong>Description</strong></p></td>
</tr>
<tr class="even" style="height: 91px;">
<td
style="height: 36px; width: 104.55px; vertical-align: top"><p>nesi_prepost</p></td>
<td
style="height: 36px; width: 64.35px; vertical-align: top"><p>4</p></td>
<td style="height: 36px; width: 110.567px; vertical-align: top"><p>24
hours</p></td>
<td style="height: 36px; width: 110.567px; vertical-align: top"><p>80
CPUs</p>
<p>720 GB RAM</p></td>
<td style="height: 36px; width: 111.583px; vertical-align: top"><p>20
CPUs</p>
<p>700 GB RAM</p></td>
<td style="height: 36px; width: 110.583px; vertical-align: top"><p>80
CPUs</p>
<p>700 GB RAM</p></td>
<td style="height: 36px; width: 159.8px; vertical-align: top"><p>Pre and
post processing tasks.</p></td>
</tr>
<tr class="odd" style="height: 103.2337646484375px;">
<td
style="height: 87px; width: 104.55px; vertical-align: top"><p>nesi_gpu</p></td>
<td style="height: 87px; width: 64.35px; vertical-align: top"><p>4 to
5</p></td>
<td style="height: 87px; width: 110.567px; vertical-align: top"><p>72
hours</p></td>
<td style="height: 87px; width: 110.567px; vertical-align: top"><p>4
CPUs</p>
<p>12 GB RAM</p>
<p>1 P100 GPU*</p></td>
<td style="height: 87px; width: 111.583px; vertical-align: top"><p>4
CPUs</p>
<p>12 GB RAM</p>
<p>1 P100 GPU</p></td>
<td style="height: 87px; width: 110.583px; vertical-align: top"><p>4
CPUs</p>
<p>12 GB RAM</p>
<p>1 P100 GPU</p></td>
<td style="height: 87px; width: 159.8px; vertical-align: top"><p>GPU
jobs and visualisation. </p></td>
</tr>
<tr class="even" style="height: 70px;">
<td
style="height: 70px; width: 104.55px; vertical-align: top"><p>nesi_igpu</p></td>
<td style="height: 70px; width: 64.35px; vertical-align: top"><p>0 to
1</p></td>
<td style="height: 70px; width: 110.567px; vertical-align: top"><p>2
hours</p></td>
<td style="height: 70px; width: 110.567px; vertical-align: top"><p>4
CPUs</p>
<p>12 GB RAM</p>
<p>1 P100 GPU*</p></td>
<td style="height: 70px; width: 111.583px; vertical-align: top"><p>4
CPUs</p>
<p>12 GB RAM</p>
<p>1 P100 GPU</p></td>
<td style="height: 70px; width: 110.583px; vertical-align: top"><p>4
CPUs</p>
<p>12 GB RAM</p>
<p>1 P100 GPU</p></td>
<td
style="height: 70px; width: 159.8px; vertical-align: top"><p>Interactive
GPU access 7am - 8pm.</p></td>
</tr>
</tbody>
</table>

\* NVIDIA Tesla P100 PCIe 12GB card

### Requesting GPUs

Nodes in the `nesi_gpu` partition have 1 P100 GPU card each. You can
request it using:

    #SBATCH --partition=nesi_gpu
    #SBATCH --gpus-per-node=1

Note that you need to specify the name of the partition.  You also need
to specify a number of CPUs and amount of memory small enough to fit on
these nodes.

See [GPU use on
NeSI](https://support.nesi.org.nz/hc/en-gb/articles/360001471955) for
more details about Slurm and CUDA settings.

 
