---
created_at: '2018-05-01T23:29:39Z'
tags:
- hpc
- info
title: Mahuika
---

Mahuika is NeSI's High Performance Computing Cluster.


## Getting Started

Something pointing to [Connecting]()

## Hardware

<table style="width: 700px; height: 658px;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd" style="height: 55px;">
<td style="height: 55px; width: 240.278px"><p><span><strong>Login
nodes</strong></span></p></td>
<td style="height: 55px; width: 436.389px"><p><span>72 cores in 2×
Broadwell (E5-2695v4, 2.1 GHz, dual socket 18 cores per socket)
nodes</span></p></td>
</tr>
<tr class="even" style="height: 27.4333px;">
<td style="height: 27px; width: 240.278px"><p><span><strong>Compute
nodes</strong></span></p></td>
<td style="height: 27px; width: 436.389px"><p><span>8,136 cores in 226 ×
Broadwell (E5-2695v4, 2.1 GHz, dual socket 18 cores per socket)
nodes;<br />
7,552 cores in 64 <span>HPE Apollo 2000 XL225n nodes (</span><a
href="https://www.amd.com/en/products/cpu/amd-epyc-7713">AMD EPYC Milan
7713</a>) the Milan partition</span></p></td>
</tr>
<tr class="odd" style="height: 22px;">
<td style="height: 22px; width: 240.278px"><p><span><strong>Compute
nodes (reserved for NeSI Cloud)<br />
</strong></span></p></td>
<td style="height: 22px; width: 436.389px"><p><span>288 cores in 8 ×
Broadwell (E5-2695v4, 2.1 GHz, dual socket 18 cores per socket)
nodes</span></p></td>
</tr>
<tr class="even" style="height: 148px;">
<td style="width: 240.278px; height: 148px"><p><span><strong>GPUs<br />
</strong></span></p></td>
<td style="width: 436.389px; height: 148px"><p><span>9 NVIDIA Tesla P100
PCIe 12GB cards (1 node with 1 GPU, </span>4 nodes with 2 GPUs)</p>
<p><span>8 NVIDIA A100 PCIe 40GB cards (4 nodes with 1 GPU, 2 nodes with
2 GPUs)<br />
</span></p>
<p><span>16 NVIDIA A100 HGX 80GB cards (4 nodes with 4 GPU
each)</span><span></span></p></td>
</tr>
<tr class="odd" style="height: 22px;">
<td
style="height: 22px; width: 240.278px"><p><span><strong>Hyperthreading</strong></span></p></td>
<td style="height: 22px; width: 436.389px"><p><span>Enabled
(accordingly, SLURM will see ~31,500 cores)</span></p></td>
</tr>
<tr class="even" style="height: 27px;">
<td style="height: 27px; width: 240.278px"><p><span><strong>Theoretical
Peak Performance</strong></span></p></td>
<td style="height: 27px; width: 436.389px"><p><span>308.6
TFLOPs</span></p></td>
</tr>
<tr class="odd" style="height: 70px;">
<td style="height: 70px; width: 240.278px"><p><span><strong>Memory
capacity per compute node</strong></span></p></td>
<td style="height: 70px; width: 436.389px"><p><span>128
GB</span></p></td>
</tr>
<tr class="even" style="height: 70px;">
<td style="height: 70px; width: 240.278px"><p><span><strong>Memory
capacity per login (build) node</strong></span></p></td>
<td style="height: 70px; width: 436.389px"><p><span>512
GB</span></p></td>
</tr>
<tr class="odd" style="height: 49px;">
<td style="height: 49px; width: 240.278px"><p><span><strong>Total System
memory</strong></span></p></td>
<td style="height: 49px; width: 436.389px"><p><span>84.0
TB</span></p></td>
</tr>
<tr class="even" style="height: 70px;">
<td
style="height: 70px; width: 240.278px"><p><span><strong>Interconnect</strong></span></p></td>
<td style="height: 70px; width: 436.389px"><p><span>FDR (54.5Gb/s)
InfiniBand to EDR (100Gb/s) Core fabric. 3.97:1 Fat-tree
topology</span></p></td>
</tr>
<tr class="odd" style="height: 49px;">
<td style="height: 49px; width: 240.278px"><p><span><strong>Workload
Manager</strong></span></p></td>
<td style="height: 49px; width: 436.389px"><p><span>Slurm
(Multi-Cluster)</span></p></td>
</tr>
<tr class="even" style="height: 49px;">
<td style="height: 49px; width: 240.278px"><p><span><strong>Operating
System</strong></span></p></td>
<td style="height: 49px; width: 436.389px"><p><span>CentOS 7.4 &amp;
Rocky 8.5 on Milan</span></p></td>
</tr>
</tbody>
</table>
