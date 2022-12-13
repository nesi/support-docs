> ### Important
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

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

### Limits

As a consequence of the above limit on the node-hours reserved by your
running jobs (*GrpTRESRunMins* in Slurm documentation, shown in `squeue`
output when you hit it as the reason "*AssocGrpCPURunMinutes"* ) you can
occupy more nodes simultaneously if your jobs request a shorter time
limit:

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
<tr class="even">
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

 

<table style="width:100%;">
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

 
