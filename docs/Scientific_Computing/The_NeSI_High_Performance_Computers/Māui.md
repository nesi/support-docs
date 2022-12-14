---
created_at: '2018-04-22T23:01:48Z'
hidden: false
label_names:
- hpc
- info
- maui
- XC50
- cs500
position: 4
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
services, we offer a small number [Māui ancillary
nodes](https://support.nesi.org.nz/hc/articles/360000203776).

> ### Tips
>
> The computing capacity of the Māui ancillary nodes is limited. If you
> think you will need large amounts of computing power for small jobs in
> addition to large jobs that can run on Māui, please [contact
> us](https://support.nesi.org.nz/hc/requests/new) about getting an
> allocation on
> [Mahuika](https://support.nesi.org.nz/hc/en-gb/articles/360000163575),
> our high-throughput computing cluster.

The login or build nodes maui01 and maui02 provide access to the full
Cray Programming Environment (e.g. editors, compilers, linkers, debug
tools). Typically, users will access these nodes via SSH from the NeSI
lander node. Jobs can be submitted to the HPC from these nodes.

### Important Notes

1.  The Cray Programming Environment on the XC50 (supercomputer) differs
    from that on Mahuika and the Māui Ancillary nodes.
2.  The `/home, /nesi/project`, and `/nesi/nobackup` [file
    systems](https://support.nesi.org.nz/hc/articles/360000177256) are
    mounted on Māui.
3.  The I/O subsystem on the XC50 can provide high bandwidth to disk
    (large amounts of data), but not many separate reading or writing
    operations.** **If your code performs a lot of disk read or write
    operations, it should be run on either the [Māui ancillary
    nodes](https://support.nesi.org.nz/hc/en-gb/articles/360000203776) or [Mahuika](https://support.nesi.org.nz/hc/en-gb/articles/360000163575).

All Māui resources are indicated below, and the the Māui Ancillary Node
resources
[here](https://support.nesi.org.nz/knowledge/articles/360000203776/en-gb?brand_id=30406).

## Māui Supercomputer (Cray XC50)

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

## Storage (IBM ESS)

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
</tbody>
</table>

 

 
