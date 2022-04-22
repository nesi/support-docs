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

Māui Supercomputer (Cray XC50)
------------------------------

  --------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------
  [**Login nodes** (also known as eLogin nodes)]{.wysiwyg-font-size-medium}   [80 cores in 2 × Skylake (Gold 6148, 2.4 GHz, dual socket 20 cores per socket) nodes]{.wysiwyg-font-size-medium}
  [**Compute nodes**]{.wysiwyg-font-size-medium}                              [18,560 cores in 464 × Skylake (Gold 6148, 2.4 GHz, dual socket 20 cores per socket) nodes;]{.wysiwyg-font-size-medium}
  [**Hyperthreading**]{.wysiwyg-font-size-medium}                             [Enabled (accordingly, SLURM will see 37,120 cores)]{.wysiwyg-font-size-medium}
  [**Theoretical Peak Performance**]{.wysiwyg-font-size-medium}               [1.425 PFLOPS]{.wysiwyg-font-size-medium}
  [**Memory capacity per compute node**]{.wysiwyg-font-size-medium}           [232 nodes have 96 GB, the remaining 232 have 192 GB each]{.wysiwyg-font-size-medium}
  [**Memory capacity per login (build) node**]{.wysiwyg-font-size-medium}     [768 GB]{.wysiwyg-font-size-medium}
  [**Total System memory**]{.wysiwyg-font-size-medium}                        [66.8 TB]{.wysiwyg-font-size-medium}
  [**Interconnect**]{.wysiwyg-font-size-medium}                               [Cray Aries, Dragonfly topology]{.wysiwyg-font-size-medium}
  [**Workload Manager**]{.wysiwyg-font-size-medium}                           [Slurm (Multi-Cluster)]{.wysiwyg-font-size-medium}
  [**Operating System**]{.wysiwyg-font-size-medium}                           [Cray Linux Environment (SLES 12 SP2), and CLE 6.0 UP06]{.wysiwyg-font-size-medium}
  --------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------

Storage (IBM ESS)
-----------------

  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [**Scratch Capacity** (accessible from all Māui, Mahuika, and Ancillary nodes).]{.wysiwyg-font-size-medium}     [4,412 TB (IBM Spectrum Scale, version 5.0). Total I/O bandwidth to disks is 130 GB/s]{.wysiwyg-font-size-medium}
  [**Persistent storage** (accessible from all Māui, Mahuika, and Ancillary nodes).]{.wysiwyg-font-size-medium}   [1,765 TB (IBM Spectrum Scale, version 5.0) Shared Storage. Total I/O bandwidth to disks is 65 GB/s (i.e. the /home and /nesi/project filesystems)]{.wysiwyg-font-size-medium}
  [**Offline storage** (accessible from all Māui, Mahuika, and Ancillary nodes).]{.wysiwyg-font-size-medium}      [Of the order of 100 PB (compressed)]{.wysiwyg-font-size-medium}
  --------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

 
