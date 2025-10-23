---
created_at: '2022-06-13T04:54:38Z'
description:  This page below outlines the available hardware.
tags:
 - gpu
 - compute
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
        <td>Core</td>
        <td colspan="2">Memory</td>
        <td>GPGPU</td>
        <td>Nodes</td>
    </tr>
    <tr>
        <td rowspan="3">2 x AMD Milan 7713 CPU</br>└ 8 x Chiplets<br>&nbsp;&nbsp;&nbsp;&nbsp;└ 8 x Cores</td>
        <td rowspan="3">126</td>
        <td>512GB</td>
        <td><em>(4GB / Core)</em></td>
        <td>-</td>
        <td>54</td>
    </tr>
    <tr>
        <td rowspan="2">1024GB</td>
        <td rowspan="2"><em>(8GB / Core)<em></td>
        <td>-</td>
        <td>8</td>
    </tr>
    <tr id="gpu-milan-a100">
        <td>4 x NVIDIA HGX A100</td>
        <td>4</td>
    </tr>
    <tr>
        <td rowspan="5">2 x AMD Genoa 9634 CPU</br>└ 12 x Chiplets</br>&nbsp;&nbsp;&nbsp;&nbsp;└ 7 x Cores</td>
        <td rowspan="5">166</td>
        <td>358GB</td>
        <td><em>(1GB / Core)</em></td>
        <td>-</td>
        <td>44</td>
    </tr>
    <tr id="gpu-genoa-a100">
        <td>716GB</td>
        <td><em>(2GB / Core)</em></td>
        <td>2 x NVIDIA A100</td>
        <td>4</td>
    </tr>
    <tr>
        <td rowspan="3">1432GB</td>
        <td rowspan="3"><em>(4GB / Core)</em></td>
        <td>-</td>
        <td>8</td>
    </tr>
    <tr id="gpu-genoa-h100">
        <td>2 x NVIDIA H100</td>
        <td>4</td>
    </tr>
    <tr id="gpu-genoa-l4">
        <td>4 x NVIDIA L4</td>
        <td>4</td>
    </tr>
</table>

## GPGPUs

NeSI has a range of Graphical Processing Units (GPUs) to accelerate compute-intensive research and support more analysis at scale.

Depending on the type of GPU, you can access them in different ways, such as via batch scheduler (Slurm),
or Virtual Machines (VMs).

For information about how to request these GPUs in a Slurm job, see [GPU Use](GPU_Use.md).

<table>
    <tr>
        <td>Architecture</td>
        <td>Purpose/Note</td>
        <td>VRAM</td>
        <td>GPUs on Node</td>
        <td colspan="2">Nodes</td>
    </tr>
    <tr>
        <td rowspan="2">NVIDIA A100</td>
        <td rowspan="2">Machine Learning</td>
        <td>80GB</td>
        <td>4</td>
        <td><a href="#gpu-milan-a100">Milan</a></td>
        <td>4</td>
    </tr>
    <tr>
        <td>40GB</td>
        <td>2</td>
        <td><a href="#gpu-genoa-a100">Genoa</a></td>
        <td>4</td>
    </tr>
    <tr>
        <td>NVIDIA H100</td>
        <td>Large-scale Machine Learning</td>
        <td>96GB</td>
        <td>2</td>
        <td><a href="#gpu-genoa-h100">Genoa</a></td>
        <td>4</td>
    </tr>
    <tr>
        <td>NVIDIA L4</td>
        <td>No fp64 double precision</td>
        <td>24GB</td>
        <td>4</td>
        <td><a href="#gpu-genoa-l4">Genoa</a></td>
        <td>4</td>
    </tr>
    <tr>
        <td>NVIDIA A40</td>
        <td>Teaching / training</td>
        <td>48GB</td>
        <td><a href="https://docs.nesi.org.nz/Scientific_Computing/Research_Developer_Cloud/User_Guides">RDC</a></td>
        <td></td>
        <td>4</td>
    </tr>
</table>

If you have any questions about hardware or the status of anything listed in the table,
{% include "partials/support_request.html" %}.
