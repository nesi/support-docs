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

### Notes:

1.  The `/home, /nesi/project`, and `/nesi/nobackup`
    [filesystems](https://support.nesi.org.nz/hc/articles/360000177256)
    are mounted on the Māui Ancillary Nodes.
2.  The Māui Ancillary nodes have Skylake processors, while the Mahuika
    nodes use Broadwell processors.

## Ancillary Node Specifications

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

 

The Māui\_Ancil nodes have different working environment than the Māui
(login) nodes. Therefore a CS500 login node is provided, to create and
submit your jobs on this architecture. To use you need to login from
Māui login nodes to:

    w-mauivlab01.maui.nesi.org.nz

If you are looking for accessing this node from your local machine you
could add the following section to `~/.ssh/config` (extending the
[recommended terminal
setup](https://support.nesi.org.nz/hc/en-gb/articles/360000625535-Recommended-Terminal-Setup))

    Host w-mauivlab01 
      User <username> 
      Hostname w-mauivlab01.maui.nesi.org.nz 
      ProxyCommand ssh -W %h:%p maui 
      ForwardX11 yes
      ForwardX11Trusted yes
      ServerAliveInterval 300
      ServerAliveCountMax 2
