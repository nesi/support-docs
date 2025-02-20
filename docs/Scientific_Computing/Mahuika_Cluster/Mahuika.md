---
created_at: '2018-04-22T21:09:28Z'
tags:
- hpc
- mahuika
- cs400
title: Mahuika
vote_count: 7
vote_sum: 3
zendesk_article_id: 360000163575
zendesk_section_id: 360000034335
---

Mahuika is a Cray CS400 cluster featuring Intel Xeon Broadwell nodes,
FDR InfiniBand interconnect, and NVIDIA GPGPUs.

Mahuika is designed to provide a capacity, or high throughput, HPC
resource that allows researchers to run many small (from one to a few
hundred CPU cores) compute jobs simultaneously, and to conduct
interactive data analysis. To support jobs that require large (up to
500GB) or huge (up to 4 TB) memory, or GPGPUs, and to provide virtual
lab services, Mahuika has additional nodes optimised for this purpose.

The Mahuika login (or build) nodes, mahuika01 and mahuika02, provide
access to GNU, Intel and Cray programming environments, including
editors, compilers, linkers, and debugging tools. Typically, users will
ssh to these nodes after logging onto the NeSI lander node.

## Notes

1. The Cray Programming Environment on Mahuika, differs from that on
    Māui.
2. The `/home, /nesi/project`, and `/nesi/nobackup`
    [filesystems](The_NeSI_High_Performance_Computers/NeSI_File_Systems_and_Quotas.md)
    are mounted on Mahuika.
3. Read about how to compile and link code on Mahuika in section
    entitled: [Compiling software on Mahuika.](The_NeSI_High_Performance_Computers/Compiling_software_on_Mahuika.md)
4. An extension to Mahuika with additional, upgraded resources is also
    available. see [Milan Compute Nodes](The_NeSI_High_Performance_Computers/Milan_Compute_Nodes.md)
    for details on access

## Mahuika HPC Cluster (Cray CS400)

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

##  Storage (IBM ESS)

|                        |                                                                                                                                                                     |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Scratch storage**    | 4,412 TB (IBM Spectrum Scale, version 5.0). Total I/O bandwidth to disks is ~130 GB/s                                                                               |
| **Persistent storage** | 1,765 TB (IBM Spectrum Scale, version 5.0). Shared between Mahuika and Māui Total I/O bandwidth to disks is ~65 GB/s (i.e. the /home and /nesi/project filesystems) |
| **Offline storage**    | Of the order of 100 PB (compressed)                                                                                                                                 |

Scratch and persistent storage are accessible from Mahuika, as well as
from Māui and the ancillary nodes. Offline storage will in due course be
accessible indirectly, via a dedicated service.
