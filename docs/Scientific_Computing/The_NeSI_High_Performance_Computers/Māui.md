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

> ### Tips {#mahuika}
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

+-----------------------------------+-----------------------------------+
| [**Login nodes** (also known as   | [80 cores in 2 × Skylake (Gold    |
| eLogin                            | 6148, 2.4 GHz, dual socket 20     |
| nodes)]{.wysiwyg-font-size-medium | cores per socket)                 |
| }                                 | nodes]{.wysiwyg-font-size-medium} |
+-----------------------------------+-----------------------------------+
| [**Compute                        | [18,560 cores in 464 × Skylake    |
| nodes**]{.wysiwyg-font-size-mediu | (Gold 6148, 2.4 GHz, dual socket  |
| m}                                | 20 cores per socket)              |
|                                   | nodes;]{.wysiwyg-font-size-medium |
|                                   | }                                 |
+-----------------------------------+-----------------------------------+
| [**Hyperthreading**]{.wysiwyg-fon | [Enabled (accordingly, SLURM will |
| t-size-medium}                    | see 37,120                        |
|                                   | cores)]{.wysiwyg-font-size-medium |
|                                   | }                                 |
+-----------------------------------+-----------------------------------+
| [**Theoretical Peak               | [1.425                            |
| Performance**]{.wysiwyg-font-size | PFLOPS]{.wysiwyg-font-size-medium |
| -medium}                          | }                                 |
+-----------------------------------+-----------------------------------+
| [**Memory capacity per compute    | [232 nodes have 96 GB, the        |
| node**]{.wysiwyg-font-size-medium | remaining 232 have 192 GB         |
| }                                 | each]{.wysiwyg-font-size-medium}  |
+-----------------------------------+-----------------------------------+
| [**Memory capacity per login      | [768                              |
| (build)                           | GB]{.wysiwyg-font-size-medium}    |
| node**]{.wysiwyg-font-size-medium |                                   |
| }                                 |                                   |
+-----------------------------------+-----------------------------------+
| [**Total System                   | [66.8                             |
| memory**]{.wysiwyg-font-size-medi | TB]{.wysiwyg-font-size-medium}    |
| um}                               |                                   |
+-----------------------------------+-----------------------------------+
| [**Interconnect**]{.wysiwyg-font- | [Cray Aries, Dragonfly            |
| size-medium}                      | topology]{.wysiwyg-font-size-medi |
|                                   | um}                               |
+-----------------------------------+-----------------------------------+
| [**Workload                       | [Slurm                            |
| Manager**]{.wysiwyg-font-size-med | (Multi-Cluster)]{.wysiwyg-font-si |
| ium}                              | ze-medium}                        |
+-----------------------------------+-----------------------------------+
| [**Operating                      | [Cray Linux Environment (SLES 12  |
| System**]{.wysiwyg-font-size-medi | SP2), and CLE 6.0                 |
| um}                               | UP06]{.wysiwyg-font-size-medium}  |
+-----------------------------------+-----------------------------------+

## Storage (IBM ESS)

+-----------------------------------+-----------------------------------+
| [**Scratch Capacity** (accessible | [4,412 TB (IBM Spectrum Scale,    |
| from all Māui, Mahuika, and       | version 5.0). Total I/O bandwidth |
| Ancillary                         | to disks is 130                   |
| nodes).]{.wysiwyg-font-size-mediu | GB/s]{.wysiwyg-font-size-medium}  |
| m}                                |                                   |
+-----------------------------------+-----------------------------------+
| [**Persistent storage**           | [1,765 TB (IBM Spectrum Scale,    |
| (accessible from all Māui,        | version 5.0) Shared Storage.      |
| Mahuika, and Ancillary            | Total I/O bandwidth to disks is   |
| nodes).]{.wysiwyg-font-size-mediu | 65 GB/s (i.e. the /home and       |
| m}                                | /nesi/project                     |
|                                   | filesystems)]{.wysiwyg-font-size- |
|                                   | medium}                           |
+-----------------------------------+-----------------------------------+
| [**Offline storage** (accessible  | [Of the order of 100 PB           |
| from all Māui, Mahuika, and       | (compressed)]{.wysiwyg-font-size- |
| Ancillary                         | medium}                           |
| nodes).]{.wysiwyg-font-size-mediu |                                   |
| m}                                |                                   |
+-----------------------------------+-----------------------------------+

 

 
