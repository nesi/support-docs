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

### Notes

1.  The Cray Programming Environment on Mahuika, differs from that on
    Māui.
2.  The `/home, /nesi/project`, and `/nesi/nobackup`
    [filesystems](https://support.nesi.org.nz/hc/en-gb/articles/360000177256)
    are mounted on Mahuika.
3.  Read about how to compile and link code on Mahuika in section
    entitled: [Compiling software on
    Mahuika.](https://support.nesi.org.nz/hc/en-gb/articles/360000329015)

Mahuika HPC Cluster (Cray CS400)
--------------------------------

+-----------------------------------+-----------------------------------+
| **Login nodes**                   | 72 cores in 2× Broadwell          |
|                                   | (E5-2695v4, 2.1 GHz, dual socket  |
|                                   | 18 cores per socket) nodes        |
+-----------------------------------+-----------------------------------+
| **Compute nodes**                 | 8,136 cores in 226 × Broadwell    |
|                                   | (E5-2695v4, 2.1 GHz, dual socket  |
|                                   | 18 cores per socket) nodes;       |
+-----------------------------------+-----------------------------------+
| **Compute nodes (reserved for     | 288 cores in 8 × Broadwell        |
| NeSI Cloud)\                      | (E5-2695v4, 2.1 GHz, dual socket  |
| **                                | 18 cores per socket) nodes        |
+-----------------------------------+-----------------------------------+
| **GPGPUs\                         | 8 NVIDIA Tesla P100 PCIe 12GB     |
| **                                | cards (4 nodes with 2 GPUs)       |
|                                   |                                   |
|                                   | 8 NVIDIA A100 PCIe 40GB cards (4  |
|                                   | nodes with 1 GPU, 2 nodes with 2  |
|                                   | GPUs)\                            |
+-----------------------------------+-----------------------------------+
| **Hyperthreading**                | Enabled (accordingly, SLURM will  |
|                                   | see 16,272 cores)                 |
+-----------------------------------+-----------------------------------+
| **Theoretical Peak Performance**  | 308.6 TFLOPs                      |
+-----------------------------------+-----------------------------------+
| **Memory capacity per compute     | 128 GB                            |
| node**                            |                                   |
+-----------------------------------+-----------------------------------+
| **Memory capacity per login       | 512 GB                            |
| (build) node**                    |                                   |
+-----------------------------------+-----------------------------------+
| **Total System memory**           | 31.0 TB                           |
+-----------------------------------+-----------------------------------+
| **Interconnect**                  | FDR (54.5Gb/s) InfiniBand to EDR  |
|                                   | (100Gb/s) Core fabric. 3.97:1     |
|                                   | Fat-tree topology                 |
+-----------------------------------+-----------------------------------+
| **Workload Manager**              | Slurm (Multi-Cluster)             |
+-----------------------------------+-----------------------------------+
| **Operating System**              | CentOS 7.4                        |
+-----------------------------------+-----------------------------------+

 

 Storage (IBM ESS)
------------------

  ------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Scratch storage**      4,412 TB (IBM Spectrum Scale, version 5.0). Total I/O bandwidth to disks is \~130 GB/s
  **Persistent storage**   1,765 TB (IBM Spectrum Scale, version 5.0). Shared between Mahuika and Māui Total I/O bandwidth to disks is \~65 GB/s (i.e. the /home and /nesi/project filesystems)
  **Offline storage**      Of the order of 100 PB (compressed)
  ------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Scratch and persistent storage are accessible from Mahuika, as well as
from Māui and the ancillary nodes. Offline storage will in due course be
accessible indirectly, via a dedicated service.

 

 
