---
created_at: '2018-04-22T23:01:48Z'
status: deprecated
tags:
- hpc
- info
- maui
- XC50
- cs500
title: "M\u0101ui"
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000163695
zendesk_section_id: 360000034335
---


Māui is a Cray XC50 supercomputer featuring Skylake Xeon nodes, Aries
interconnect and IBM ESS Spectrum Scale Storage. NeSI has access to 316
compute nodes on Māui.

Māui is designed as a capability high-performance computing resource for
simulations and calculations that require large numbers of CPUs working
in a tightly-coupled parallel fashion, as well as interactive data
analysis. To support workflows that are primarily single core jobs, for
example pre- and post-processing work, and to provide virtual lab
services, we offer a small number [Māui ancillary nodes](../The_NeSI_High_Performance_Computers/Maui_Ancillary.md).

!!! tips
     The computing capacity of the Māui ancillary nodes is limited. If you
     think you will need large amounts of computing power for small jobs in
     addition to large jobs that can run on Māui, please {% include "partials/support_request.html" %} about getting an
     allocation on
     [Mahuika](Mahuika.md),
     our high-throughput computing cluster.

The login or build nodes maui01 and maui02 provide access to the full
Cray Programming Environment (e.g. editors, compilers, linkers, debug
tools). Typically, users will access these nodes via SSH from the NeSI
lander node. Jobs can be submitted to the HPC from these nodes.

## Important Notes

1.  The Cray Programming Environment on the XC50 (supercomputer) differs
    from that on Mahuika and the Māui Ancillary nodes.
2.  The `/home, /nesi/project`, and `/nesi/nobackup` [file systems](../../Storage/File_Systems_and_Quotas/NeSI_File_Systems_and_Quotas.md) are
    mounted on Māui.
3.  The I/O subsystem on the XC50 can provide high bandwidth to disk
    (large amounts of data), but not many separate reading or writing
    operations. If your code performs a lot of disk read or write
    operations, it should be run on either the [Māui ancillary
    nodes](../../Scientific_Computing/The_NeSI_High_Performance_Computers/Maui_Ancillary.md) or [Mahuika](../../Scientific_Computing/The_NeSI_High_Performance_Computers/Mahuika.md).

All Māui resources are indicated below, and the the Māui Ancillary Node
resources
[here](../../Scientific_Computing/The_NeSI_High_Performance_Computers/Maui_Ancillary.md).

## Māui Supercomputer (Cray XC50)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td width="186"><p><span><strong>Login nodes</strong> (also known as
eLogin nodes)</span></p></td>
<td width="418"><p><span>80 cores in 2 × Skylake (Gold 6148, 2.4 GHz,
dual socket 20 cores per socket) nodes</span></p></td>
</tr>
<tr class="even">
<td width="186"><p><span><strong>Compute nodes</strong></span></p></td>
<td width="418"><p><span>18,560 cores in 464 × Skylake (Gold 6148, 2.4
GHz, dual socket 20 cores per socket) nodes;</span></p></td>
</tr>
<tr class="odd">
<td width="186"><p><span><strong>Hyperthreading</strong></span></p></td>
<td width="418"><p><span>Enabled (accordingly, SLURM will see 37,120
cores)</span></p></td>
</tr>
<tr class="even">
<td width="186"><p><span><strong>Theoretical Peak
Performance</strong></span></p></td>
<td width="418"><p><span>1.425 PFLOPS</span></p></td>
</tr>
<tr class="odd">
<td width="186"><p><span><strong>Memory capacity per compute
node</strong></span></p></td>
<td width="418"><p><span>232 nodes have 96 GB, the remaining 232 have
192 GB each</span></p></td>
</tr>
<tr class="even">
<td width="186"><p><span><strong>Memory capacity per login (build)
node</strong></span></p></td>
<td width="418"><p><span>768 GB</span></p></td>
</tr>
<tr class="odd">
<td width="186"><p><span><strong>Total System
memory</strong></span></p></td>
<td width="418"><p><span>66.8 TB</span></p></td>
</tr>
<tr class="even">
<td width="186"><p><span><strong>Interconnect</strong></span></p></td>
<td width="418"><p><span>Cray Aries, Dragonfly topology</span></p></td>
</tr>
<tr class="odd">
<td width="186"><p><span><strong>Workload
Manager</strong></span></p></td>
<td width="418"><p><span>Slurm (Multi-Cluster)</span></p></td>
</tr>
<tr class="even">
<td width="186"><p><span><strong>Operating
System</strong></span></p></td>
<td width="418"><p><span>Cray Linux Environment CLE7.0UP04<br />
SUSE Linux Enterprise Server 15 SP3<br />
</span></p></td>
</tr>
</tbody>
</table>

## Storage (IBM ESS)

|                                                                                  |                                                                                                                                                   |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Scratch Capacity** (accessible from all Māui, Mahuika, and Ancillary nodes).   | 4,412 TB (IBM Spectrum Scale, version 5.0). Total I/O bandwidth to disks is 130 GB/s                                                              |
| **Persistent storage** (accessible from all Māui, Mahuika, and Ancillary nodes). | 1,765 TB (IBM Spectrum Scale, version 5.0) Shared Storage. Total I/O bandwidth to disks is 65 GB/s (i.e. the /home and /nesi/project filesystems) |
| **Offline storage** (accessible from all Māui, Mahuika, and Ancillary nodes).    | Of the order of 100 PB (compressed)                                                                                                               |

 

 
