---
created_at: '2018-05-21T03:28:20Z'
tags:
- mahuika
- slurm
vote_count: 11
vote_sum: 9
zendesk_article_id: 360000204076
zendesk_section_id: 360000030876
---

## General Limits

- No individual job can request more than 20,000 CPU hours. This has
    the consequence that a job can request more CPUs if it is shorter
    (short-and-wide vs long-and-skinny).
- No user can have more than 1,000 jobs in the queue at a time.

These limits are defaults and can be altered on a per-account basis if
there is a good reason. For example we will increase the limit on queued
jobs for those who need to submit large numbers of jobs, provided that
they undertake to do so with job arrays.

## Partitions

A partition can be specified via the appropriate [sbatch option](Slurm-Reference_Sheet.md),
e.g.:

``` sl
#SBATCH --partition=milan
```

However on Mahuika there is generally no need to do so, since the
default behaviour is that your job will be assigned to the most suitable
partition(s) automatically, based on the resources it requests,
including particularly its memory/CPU ratio and time limit.

The `milan` partition is currently an exception - since it has a
different operating system version it is currently configured to be
opt-in only - your job will not land there it unless you request it.

If you do specify a partition and your job is not a good fit for that
partition then you may receive a warning, please do not ignore this.
E.g.:

```out
sbatch: `bigmem` is not the most appropriate partition for this job, which would otherwise default to `large`. If you believe this is incorrect then contact support and quote the Job ID number.
```

<table><tbody>
<tr>
<th>Name</th>
<th>Max Walltime</th>
<th>Nodes</th>
<th>CPUs/Node</th>
<th>GPUs/Node</th>
<th>Available Mem/CPU</th>
<th>Available Mem/Node</th>
<th>Max CPUs/job</th>
<th>Description</th>
</tr>
<tr>
<td>long</td>
<td>3 weeks</td>
<td>69</td>
<td>72</td>
<td>None</td>
<td>1500 MB</td>
<td>105 GB</td>
<td>720</td>
<td>Jobs longer than 3 days.</td>
</tr>
<tr>
<td>large</td>
<td>3 days</td>
<td><em>long+</em>157</td>
<td>72</td>
<td>None</td>
<td>1500 MB</td>
<td>105 GB</td>
<td>288</td>
<td>Default partition.</td>
</tr>
<tr>
<td rowspan=2>milan</td>
<td rowspan=2>7 days</td>
<td>56</td>
<td>256</td>
<td rowspan=2>None</td>
<td>1850 MB</td>
<td>460 GB</td>
<td rowspan=2>2560</td>
<td rowspan=2><a href="./Milan_Compute_Nodes.md">Jobs using Milan Nodes</a></td>
</tr>
<td>8</td>
<td>256</td>
<td>3800 MB</td>
<td>960 GB</td>
</tr>
<tr>
<td>bigmem</td>
<td>7 days</td>
<td>6</td>
<td>72</td>
<td>None</td>
<td>6300 MB</td>
<td>460 GB</td>
<td>288</td>
<td>Large amounts of memory.</td>
</tr>
<tr>
<td>infill</td>
<td>7 days</td>
<td>6</td>
<td>54</td>
<td>None</td>
<td>5500 MB</td>
<td>300 GB</td>
<td></td>
<td></td>
</tr>
<tr>
<td>hugemem</td>
<td>7 days</td>
<td>2<br/>
1<br/>
1</td>
<td>80<br/>
128<br/>
176</td>
<td></td>
<td>18 GB<br/>
30 GB<br/>
35 GB</td>
<td>1,500 GB<br />
4,000 GB<br/>
6,000 GB</td>
<td>256</td>
<td>Very large amounts of memory.</td>
</tr>
<tr>
<td>gpu</td>
<td>7 days</td>
<td>1</p>
<p>4</p>
<p>2</p>
<p>2</p>
<p>1</td>
<td>18, plus 54 shared with
<em>infill</em></td>
<td>1 P100</p>
<p>2 P100</p>
<p>1 A100</p>
<p>2 A100</p>
<p>7 A100-1g.5gb</td>
<td>6300 MB</td>
<td>160 GB, plus 300 GB
shared with <em>infill</em></td>
<td>64</td>
<td>Nodes with GPUs. See
below for more info.</td>
</tr>
<tr>
<td>hgx</td>
<td>7 days</td>
<td>4</td>
<td>128</td>
<td>4 A100</td>
<td>6300 MB</td>
<td>460 GB</td>
<td>64</td>
<td>Part of
<a href="./Milan_Compute_Nodes.md">Milan Nodes</a>. See below.</td>
</tr>
</tbody>
</table>

## Quality of Service

Orthogonal to the partitions, each job has a "Quality of Service", with
the default QoS for a job being determined by the allocation class of
its project. There are other QoSs which you can select with the
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

|                        |                                                                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **GPU code**           | **GPU type**                                                                                                                                   |
| P100                   | NVIDIA Tesla P100 PCIe 12GB cards                                                                                                              |
| A100 (`gpu` partition) | NVIDIA Tesla A100 PCIe 40GB cards                                                                                                              |
| A100-1g.5gb            | 1 NVIDIA Tesla A100 PCIe 40GB card divided into [7 MIG GPU slices](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) (5GB each).  |
| A100 (`hgx` partition) | NVIDIA Tesla A100 80GB, on a HGX baseboard with NVLink GPU-to-GPU interconnect between the 4 GPUs                                              |

The default GPU type is P100, of which you can request 1 or 2 per node:

``` sl
#SBATCH --gpus-per-node=1     # or equivalently, P100:1
```

To request A100 GPUs, use instead:

``` sl
#SBATCH --gpus-per-node=A100:1
```

See [GPU use on NeSI](GPU_use_on_NeSI.md)
for more details about Slurm and CUDA settings.

### Limits on GPU Jobs

- There is a per-project limit of 6 GPUs being used at a time.
- There is also a per-project limit of 360 GPU-hours being allocated
    to running jobs. This reduces the number of GPUs available for
    longer jobs, so for example you can use 2 GPUs at a time if your
    jobs run for a week, 5 GPUs for two days, or 6 GPUs for one day
    jobs. The intention is to guarantee that all users can get their GPU
    debugging jobs running in a reasonably timely manner.
- Each GPU job can use no more than 64 CPUs. This is to ensure that
    GPUs are not left idle just because their node has no remaining free
    CPUs.
- There is a limit of one A100-1g.5gb GPU job per user.

### Accessing A100 GPUs in the `hgx` partition

The A100 GPUs in the `hgx` partition are designated for workloads
requiring large memory (up to 80GB) or multi-GPU computing (up to 4 GPUs
connected via
[NVLink](https://www.nvidia.com/en-us/data-center/nvlink/)):

- Explicitly specify the partition to access them, with
    `--partition=hgx`.
- Hosting nodes are Milan nodes. Check the [dedicated support page](Milan_Compute_Nodes.md)
    for more information about the Milan nodes' differences from
    Mahuika's Broadwell nodes.

## Mahuika Infiniband Islands

Mahuika is divided into “islands” of 26 nodes (or 1,872 CPUs).
Communication between two nodes on the same island is faster than
between two nodes on different islands. MPI jobs placed entirely within
one island will often perform better than those split among multiple
islands.

You can request that a job runs within a single InfiniBand island by
adding:

``` sl
#SBATCH --switches=1
```

Slurm will then run the job within one island provided that this does
not delay starting the job by more than the maximum switch waiting time,
currently configured to be 5 minutes. That waiting time limit can be
reduced by adding `@<time>` after the number of switches e.g:

``` sl
#SBATCH --switches=1@00:30:00
```
