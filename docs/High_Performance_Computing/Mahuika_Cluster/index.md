---
created_at: '2018-05-01T23:29:39Z'
tags:
- hpc
- info
title: Mahuika Cluster
hide:
  - toc
---

Mahuika is NeSI's High Performance Computing Cluster.

## Getting Started

<div class="grid cards" markdown>

-   ![](../../assets/icons/material/account-details.svg) __NeSI Accounts__

    ---

    You will need a __NeSI account__, and be a __member of an active project__ before you can access the NeSI HPC.

    - [Creating a NeSI Account](Creating_a_NeSI_Account_Profile.md)
    - [Applying For a New NeSI Project](Applying_for_a_new_NeSI_project.md)
    - [Applying to Join a NeSI Project](Applying_to_join_an_existing_NeSI_project.md)

-   ![](../../assets/icons/material/compass.svg) __Cluster Access__

    ---
    Once you have your account sorted, learn how to connect to the cluster.

    - [Connect Via Open OnDemand](../Open_OnDemand/index.md) - Best for new users. Or using [OnDemand Apps]().
    - [Connect With SSH](Terminal_Setup/index.md) - For those familiar with command line, and accessing machines remotely.

</div>

## Hardware

|     |     |
| --- | --- |
| __Login nodes__ | 72 cores in 2× Broadwell (E5-2695v4, 2.1 GHz, dual socket 18 cores per socket) nodes |
| __Compute nodes__ | 8,136 cores in 226 × Broadwell (E5-2695v4, 2.1 GHz, dual socket 18 cores per socket) nodes;<br>7,552 cores in 64 HPE Apollo 2000 XL225n nodes ([AMD EPYC Milan 7713](https://www.amd.com/en/products/cpu/amd-epyc-7713)) the Milan partition |
| __Compute nodes (reserved for NeSI Cloud)  <br>__ | 288 cores in 8 × Broadwell (E5-2695v4, 2.1 GHz, dual socket 18 cores per socket) nodes |
| __GPUs__ | 9 NVIDIA Tesla P100 PCIe 12GB cards (1 node with 1 GPU, 4 nodes with 2 GPUs)<br><br>7 NVIDIA A100 PCIe 40GB cards (3 nodes with 1 GPU, 2 nodes with 2 GPUs) <br><br>7 A100-1g.5gb instances (1 NVIDIA A100 PCIe 40GB card divided into [7 MIG GPU slices](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) with 5GB memory each)<br><br>4 NVIDIA HGX A100 (4 GPUs per board with 80GB memory each, 16 A100 GPUs in total)<br><br>4 NVIDIA A40 with 48GB memory each (2 nodes with 2 GPUs, but capacity for 6 additional GPUs already in place)|
| __Hyperthreading__ | Enabled (accordingly, SLURM will see ~31,500 cores) |
| __Theoretical Peak Performance__ | 308.6 TFLOPs |
| __Memory capacity per compute node__ | 128 GB |
| __Memory capacity per login (build) node__ | 512 GB |
| __Total System memory__ | 84.0 TB |
| __Interconnect__ | FDR (54.5Gb/s) InfiniBand to EDR (100Gb/s) Core fabric. 3.97:1 Fat-tree topology |
| __Workload Manager__ | Slurm (Multi-Cluster) |
| __Operating System__ | CentOS 7.4 & Rocky 8.5 on Milan |
