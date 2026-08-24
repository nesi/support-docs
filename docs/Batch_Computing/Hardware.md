---
created_at: '2022-06-13T04:54:38Z'
description:  This page below outlines the available hardware.
tags:
 - gpu
---

A list of the currently available hardware.

If you are looking for information on maximum resource requests, see [Job Limits](Job_Limits.md).

## Compute Nodes

Your jobs will land on appropriately sized nodes automatically based on your CPU to memory ratio. For example in the Genoa partition:

- A job requesting ≤ 2 GB/core will run on a 2 GB/core node, or if full, a 4 GB/core node.
- A job requesting ≤ 4 GB/core will run on a 4 GB/core node, or if full, a 8 GB/core node.

And so on.
You will always get the amount of memory you requested, even if running on a node with a higher ratio.

<table>
    <tr>
        <td>Architecture</td>
        <td>Cores</td>
        <td colspan="2">Memory</td>
        <td>GPU</td>
        <td>Nodes</td>
    </tr>
    <tr>
        <td rowspan="2">2 x AMD Milan 7713 CPU<br>└ 8 x Chiplets<br>&nbsp;&nbsp;&nbsp;&nbsp;└ 8 x Cores</td>
        <td rowspan="2">128</td>
        <td>512GB</td>
        <td><em>(4GB / Core)</em></td>
        <td>-</td>
        <td>55</td>
    </tr>
    <tr>
        <td>1024GB</td>
        <td><em>(8GB / Core)</em></td>
        <td>-</td>
        <td>8</td>
    </tr>
    <tr id="gpu-milan-a100">
        <td>1 x AMD Milan 7713P CPU<br>└ 8 x Chiplets<br>&nbsp;&nbsp;&nbsp;&nbsp;└ 8 x Cores</td>
        <td>64</td>
        <td>512GB</td>
        <td><em>(8GB / Core)</em></td>
        <td>4 x NVIDIA HGX A100</td>
        <td>4</td>
    </tr>
    <tr>
        <td rowspan="5">2 x AMD Genoa 9634 CPU<br>└ 12 x Chiplets<br>&nbsp;&nbsp;&nbsp;&nbsp;└ 7 x Cores</td>
        <td rowspan="5">168</td>
        <td>384GB</td>
        <td><em>(2GB / Core)</em></td>
        <td>-</td>
        <td>44</td>
    </tr>
    <tr id="gpu-genoa-rtx6000">
        <td>768GB</td>
        <td><em>(4GB / Core)</em></td>
        <td>2 x NVIDIA RTX PRO 6000</td>
        <td>4</td>
    </tr>
    <tr>
        <td rowspan="3">1536GB</td>
        <td rowspan="3"><em>(8GB / Core)</em></td>
        <td>-</td>
        <td>8</td>
    </tr>
    <tr id="gpu-genoa-h100">
        <td>2 x NVIDIA H100 NVL</td>
        <td>4</td>
    </tr>
    <tr id="gpu-genoa-l4">
        <td>4 x NVIDIA L4</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2 x Intel Xeon Gold 6230 CPU<br>&nbsp;&nbsp;&nbsp;&nbsp;(Cascade Lake)</td>
        <td>40</td>
        <td>1.5TB</td>
        <td><em>(38GB / Core)</em></td>
        <td>-</td>
        <td>2</td>
    </tr>
    <tr>
        <td>4 x Intel Xeon Gold 6238M CPU<br>&nbsp;&nbsp;&nbsp;&nbsp;(Cascade Lake)</td>
        <td>88</td>
        <td>6TB</td>
        <td><em>(69GB / Core)</em></td>
        <td>-</td>
        <td>1</td>
    </tr>
</table>

!!! note "Memory figures"
    Memory shown is the amount physically installed. A small amount is reserved for the operating system,
    so the memory actually available to jobs is a few percent lower — for example a 512GB Milan node offers
    480GB to Slurm. A job requesting exactly the full per-core ratio across every core of a node will
    therefore not fit. Run `sinfo -o '%n %m'` for the exact schedulable figures.

!!! warning "hugemem"
    Jobs will not automatically land on the Intel 'hugemem' nodes. You must specifically request `--partition hugemem`.
    The CPU architecture is different enough from the milan and genoa nodes, you will probably have to recompile your software.


## GPUs

REANNZ HPC has a range of Graphical Processing Units (GPUs) to accelerate compute-intensive research and support more analysis at scale.

Depending on the type of GPU, you can access them in different ways, such as via batch scheduler (Slurm),
or Virtual Machines (VMs).

For information about how to request these GPUs in a Slurm job, see [Using GPUs](Using_GPUs.md).

<table>
    <tr>
        <td>Architecture</td>
        <td>Purpose/Note</td>
        <td>VRAM</td>
        <td>GPUs on Node</td>
        <td colspan="2">Nodes</td>
    </tr>
    <tr>
        <td>NVIDIA A100 SXM4</td>
        <td></td>
        <td>80GB</td>
        <td>4</td>
        <td><a href="#gpu-milan-a100">Milan</a></td>
        <td>4</td>
    </tr>
    <tr>
        <td>NVIDIA RTX PRO 6000</td>
        <td>Very limited double precision floating point (fp64)</td>
        <td>96GB</td>
        <td>2</td>
        <td><a href="#gpu-genoa-rtx6000">Genoa</a></td>
        <td>4</td>
    </tr>
    <tr>
        <td>NVIDIA H100 NVL</td>
        <td></td>
        <td>94GB</td>
        <td>2</td>
        <td><a href="#gpu-genoa-h100">Genoa</a></td>
        <td>4</td>
    </tr>
    <tr>
        <td>NVIDIA L4</td>
        <td>No double precision floating point (fp64)</td>
        <td>24GB</td>
        <td>4</td>
        <td><a href="#gpu-genoa-l4">Genoa</a></td>
        <td>4</td>
    </tr>
</table>



If you have any questions about hardware or the status of anything listed in the table,
{% include "partials/support_request.html" %}.
