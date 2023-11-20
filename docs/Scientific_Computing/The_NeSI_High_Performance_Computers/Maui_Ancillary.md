---
created_at: '2018-05-21T01:43:06Z'
hidden: false
position: 5
tags:
- maui
- XC50
- cs500
title: "M\u0101ui Ancillary"
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000203776
zendesk_section_id: 360000034335
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

The Māui Ancillary Nodes provide access to a Virtualised environment
that supports:

1.  Pre- and post-processing of data for jobs running on the
    [Māui](https://support.nesi.org.nz/hc/articles/360000163695)
    Supercomputer or
    [Mahuika](https://support.nesi.org.nz/hc/articles/360000163575) HPC
    Cluster. Typically, as serial processes on a Slurm partition running
    on a set of Ancillary node VMs or baremetal servers.
2.  Virtual laboratories that provide interactive access to data stored
    on the Māui (and Mahuika) storage together with domain analysis
    toolsets (e.g. Seismic, Genomics, Climate, etc.). To access the
    Virtual Laboratory nodes, users will first logon to the NeSI Lander
    node, then ssh to the relevant Virtual Laboratory. Users may submit
    jobs to Slurm partitions from Virtual Laboratory nodes.
3.  Remote visualisation of data resident on the filesystems.
4.  GPGPU computing.

Scientific Workflows may access resources across the Māui Supercomputer
and any (multi-cluster) Slurm partitions on the Māui or Mahuika systems.

## Notes:

1.  The `/home, /nesi/project`, and `/nesi/nobackup`
    [filesystems](https://support.nesi.org.nz/hc/articles/360000177256)
    are mounted on the Māui Ancillary Nodes.
2.  The Māui Ancillary nodes have Skylake processors, while the Mahuika
    nodes use Broadwell processors.

## Ancillary Node Specifications

|                                            |                                                                                                                                             |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Multi-Purpose nodes**                    | 1,120 cores in 28 × Skylake (Gold 6148, 2.4 GHz, dual socket 20 cores per socket) nodes, which will appear as 2,240 logical cores.          |
| **Hyperthreading**                         | Enabled                                                                                                                                     |
| **Local Disk**                             | 1.2TB SSD                                                                                                                                   |
| **Operating System**                       | CentOS 7.4                                                                                                                                  |
| **GPGPUs**                                 | 5 NVIDIA Tesla P100 PCIe 12GB (5 nodes with 1 GPU)                                                                                          |
| **Remote Visualisation**                   | [NICE DCV](https://www.nice-software.com/products/dcv)                                                                                      |
| **Memory capacity per Multi-Purpose node** | 768 GB                                                                                                                                      |
| **Interconnect**                           | EDR (100 Gb/s) InfiniBand                                                                                                                   |
| **Workload Manager**                       | Slurm (Multi-Cluster)                                                                                                                       |
| **OpenStack**                              | The Cray CS500 Ancillary nodes will normally be presented to users as Virtual Machines, provisioned from the physical hardware as required. |

 

The Māui\_Ancil nodes have different working environment than the Māui
(login) nodes. Therefore a CS500 login node is provided, to create and
submit your jobs on this architecture. To use you need to login from
Māui login nodes to:

``` sl
w-mauivlab01.maui.nesi.org.nz
```

If you are looking for accessing this node from your local machine you
could add the following section to `~/.ssh/config` (extending the
[recommended terminal
setup](https://support.nesi.org.nz/hc/en-gb/articles/360000625535-Recommended-Terminal-Setup))

``` sl
Host w-mauivlab01 
  User <username> 
  Hostname w-mauivlab01.maui.nesi.org.nz 
  ProxyCommand ssh -W %h:%p maui 
  ForwardX11 yes
  ForwardX11Trusted yes
  ServerAliveInterval 300
  ServerAliveCountMax 2
```