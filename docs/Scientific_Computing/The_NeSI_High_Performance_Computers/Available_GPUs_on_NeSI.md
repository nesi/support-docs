---
created_at: '2022-06-13T04:54:38Z'
hidden: false
position: 6
tags: []
title: Available GPUs on NeSI
vote_count: 2
vote_sum: 2
zendesk_article_id: 4963040656783
zendesk_section_id: 360000034335
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

NeSI has a range of Graphical Processing Units (GPUs) to accelerate
compute-intensive research and support more analysis at scale. Depending
on the type of GPU, you can access them in different ways, such as via
batch scheduler (Slurm), interactively (using [Jupyter on
NeSI](../../../Scientific_Computing/Interactive_computing_using_Jupyter/Jupyter_on_NeSI)),
or Virtual Machines (VMs). 

The table below outlines the different types of GPUs, who can access
them and how, and whether they are currently available or on the future
roadmap.

If you have any questions about GPUs on NeSI or the status of anything
listed in the table, [contact
Support](https://support.nesi.org.nz/hc/en-gb/requests/new).

 

| GPGPU                                                                                                                                                                      | Purpose                                        | Location                                                                                           | Access mode                                                                                                                                 | Who can access                                                 | Status                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| 9 NVIDIA Tesla P100 PCIe 12GB cards (1 node with 1 GPU, 4 nodes with 2 GPUs)                                                                                               |                                                | [Mahuika](../../../Scientific_Computing/The_NeSI_High_Performance_Computers/Mahuika)               | Slurm and [Jupyter](../../../Scientific_Computing/Interactive_computing_using_Jupyter/Jupyter_on_NeSI)                                      | NeSI users                                                     | Currently available                                                                                          |
| 7 NVIDIA A100 PCIe 40GB cards (4 nodes with 1 GPU, 2 nodes with 2 GPUs)                                                                                                    | Machine Learning (ML) applications             | [Mahuika](../../../Scientific_Computing/The_NeSI_High_Performance_Computers/Mahuika)               | Slurm                                                                                                                                       | NeSI users                                                     | Currently available                                                                                          |
| 7 A100-1g.5gb instances (1 NVIDIA A100 PCIe 40GB card divided into [7 MIG GPU slices](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) with 5GB memory each) | Development and debugging                      | [Mahuika](../../../Scientific_Computing/The_NeSI_High_Performance_Computers/Mahuika)               | Slurm and [Jupyter](../../../Scientific_Computing/Interactive_computing_using_Jupyter/Jupyter_on_NeSI)                                      | NeSI users                                                     | Currently available                                                                                          |
| 5 NVIDIA Tesla P100 PCIe 12GB (5 nodes with 1 GPU)                                                                                                                         | Post-processing                                | [Māui Ancil](https://support.nesi.org.nz/hc/en-gb/articles/360000203776-M%C4%81ui-Ancillary-Nodes) | Slurm                                                                                                                                       | NeSI users                                                     | Currently available                                                                                          |
| 4 NVIDIA HGX A100 (4 GPUs per board with 80GB memory each, 16 A100 GPUs in total)                                                                                          | Large-scale Machine Learning (ML) applications | [Mahuika](../../../Scientific_Computing/The_NeSI_High_Performance_Computers/Mahuika)               | Slurm                                                                                                                                       | NeSI users                                                     | Available as part of the [Milan Compute Nodes](https://support.nesi.org.nz/knowledge/articles/6367209795471) |
| 4 NVIDIA A40 with 48GB memory each (2 nodes with 2 GPUs, but capacity for 6 additional GPUs already in place)                                                              | Teaching / training                            | Flexible HPC                                                                                       | [Jupyter](../../../Scientific_Computing/Interactive_computing_using_Jupyter/Jupyter_on_NeSI), VM, or bare metal tenancy possible (flexible) | Open to conversations with groups who could benefit from these | In development.                                                                                              |