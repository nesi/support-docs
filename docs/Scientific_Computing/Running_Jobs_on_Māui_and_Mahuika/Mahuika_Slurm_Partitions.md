---
created_at: '2018-05-21T03:28:20Z'
hidden: false
label_names:
- mahuika
- slurm
position: 9
title: Mahuika Slurm Partitions
vote_count: 11
vote_sum: 9
zendesk_article_id: 360000204076
zendesk_section_id: 360000030876
---

## Definitions

**CPU:** A logical core, also known as a hardware thread. Referred to as
a "CPU" in the Slurm documentation.  Since
[Hyperthreading](https://support.nesi.org.nz/hc/en-gb/articles/360000568236/)
is enabled, there are two CPUs per physical core, and every task— and
therefore every job — is allocated an even number of CPUs.

**Fairshare Weight:** CPU hours are multiplied by this factor to
determine usage for the purpose of calculating a project's [fair-share
score](https://support.nesi.org.nz/hc/en-gb/articles/360000743536/).

**Job:** A running batch script and any other processes which it might
launch with *srun*.

**Node: **A single computer within the cluster with its own CPUs and RAM
(memory), and sometimes also GPUs. A node is analogous to a workstation
(desktop PC) or laptop.

**Task:** An instance of a running computer program, consisting of one
or more threads. All of a task's threads must run within the same node.

**Thread:** A sequence of instructions executed by a CPU.

**Walltime: **Real world time, as opposed to CPU time (walltime x CPUs).

## General Limits

-   No individual job can request more than 20,000 CPU hours. This has
    the consequence that a job can request more CPUs if it is shorter
    (short-and-wide vs long-and-skinny).
-   No individual job can request more than 576 CPUs (8 full nodes),
    since larger MPI jobs are scheduled less efficiently and are
    probably suitable for running on Māui.
-   No user can have more than 1,000 jobs in the queue at a time.

These limits are defaults and can be altered on a per-account basis if
there is a good reason. For example we will increase the limit on queued
jobs for those who need to submit large numbers of jobs, provided that
they undertake to do so with job arrays.

## Partitions

A partition can be specified via the appropriate [sbatch
option](https://support.nesi.org.nz/hc/en-gb/articles/360000691716/),
e.g.:

    #SBATCH --partition=milan

However on Mahuika there is generally no need to do so, since the
default behaviour is that your job will be assigned to the most suitable
partition(s) automatically, based on the resources it requests,
including particularly its memory/CPU ratio and time limit.

The *milan* partition is currently an exception - since it has a
different operating system version it is currently configured to be
opt-in only - your job will not land there it unless you request it.

If you do specify a partition and your job is not a good fit for that
partition then you may receive a warning, please do not ignore this.
E.g.:

    sbatch: "bigmem" is not the most appropriate partition for this job, which would otherwise default to "large". If you believe this is incorrect then please contact support@nesi.org.nz and quote the Job ID number.

 

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
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

\* NVIDIA Tesla P100 PCIe 12GB cards

\*\* NVIDIA Tesla A100 PCIe 40GB cards

\*\*\* 1 NVIDIA Tesla A100 PCIe 40GB card divided into [7 MIG GPU
slices](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/)
(5GB each). 

\*\*\*\* NVIDIA Tesla A100 80GB, on a HGX baseboard with NVLink
GPU-to-GPU interconnect between the 4 GPUs  

## Quality of Service

Orthogonal to the partitions, each job has a "Quality of Service", with
the default QoS for a job being determined by the allocation class of
its project.  There are other QoSs which you can select with the
`--qos`option:

### Debug

Specifying `--qos=debug` will give the job very high priority, but is
subject to strict limits: 15 minutes per job, and only 1 job at a time
per user. Debug jobs may not span more than two nodes.

### Interactive

Specifying `--qos=interactive` will give the job very high priority, but
is subject to some limits: up to 4 jobs, 16 hours duration, 4 CPUs, 128
GB, and 1 GPU.

## Requesting GPUs

The default GPU type is P100, of which you can request 1 or 2 per node:

    #SBATCH --gpus-per-node=1     # or equivalently, P100:1

To request A100 GPUs, use instead:

    #SBATCH --gpus-per-node=A100:1

See [GPU use on
NeSI](https://support.nesi.org.nz/hc/en-gb/articles/360001471955) for
more details about Slurm and CUDA settings.

### Limits on GPU Jobs

-   There is a per-project limit of 8 GPUs being used at a time.
-   There is also a per-project limit of 360 GPU-hours being allocated
    to running jobs. This reduces the number of GPUs available for
    longer jobs, so for example you can use 8 GPUs at a time if your
    jobs run for a day, but only two GPUs if your jobs run for a week.
    The intention is to guarantee that all users can get short debugging
    jobs on to a GPU in a reasonably timely manner.  
-   Each GPU job can use no more than 64 CPUs.  This is to ensure that
    GPUs are not left idle just because their node has no remaining free
    CPUs.
-   There is a limit of one A100-1g.5gb GPU job per user.

### Accessing A100 GPUs in the `hgx` partition

The A100 GPUs in the `hgx` partition are designated for workloads
requiring large memory (up to 80GB) or multi-GPU computing (up to 4 GPUs
connected via
[NVLink](https://www.nvidia.com/en-us/data-center/nvlink/)):

-   Explicitly specify the partition to access them, with
    `--partition=hgx`.
-   Hosting nodes are Milan nodes. Check the[dedicated support
    page](https://support.nesi.org.nz/hc/en-gb/articles/6367209795471)
    for more information about the Milan nodes' differences from
    Mahuika's Broadwell nodes.

## Mahuika Infiniband Islands

Mahuika is divided into “islands” of 26 nodes (or 1,872 CPUs).
Communication between two nodes on the same island is faster than
between two nodes on different islands. MPI jobs placed entirely within
one island will often perform better than those split among multiple
islands.

You can request that a job runs within a single InfiniBand island by
adding:

    #SBATCH --switches=1

Slurm will then run the job within one island provided that this does
not delay starting the job by more than the maximum switch waiting time,
currently configured to be 5 minutes. That waiting time limit can be
reduced by adding `@<time>` after the number of switches e.g:

    #SBATCH --switches=1@00:30:00
