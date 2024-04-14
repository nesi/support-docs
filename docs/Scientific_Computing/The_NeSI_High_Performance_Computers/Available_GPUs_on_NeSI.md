---
created_at: '2022-06-13T04:54:38Z'
tags: |
    gpu
title: Available GPUs on NeSI
vote_count: 3
vote_sum: 3
zendesk_article_id: 4963040656783
zendesk_section_id: 360000034335
---


NeSI has a range of Graphical Processing Units (GPUs) to accelerate compute-intensive research and support more analysis at scale.
Depending on the type of GPU, you can access them in different ways, such as via batch scheduler (Slurm), interactively (using [Jupyter on
NeSI](../Interactive_computing_using_Jupyter/Jupyter_on_NeSI.md)),
or Virtual Machines (VMs).

The table below outlines the different types of GPUs,
who can access them and how, and whether they are currently available or on the future roadmap.

If you have any questions about GPUs on NeSI or the status of anything listed in the table,  {% include "partials/support_request.html" %}.

| GPGPU                                                                                                                                                                      | Purpose                                        | Location                                                                                           | Access mode                                                                                                                                 | Who can access                                                 | Status                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| 9 NVIDIA Tesla P100 PCIe 12GB cards (1 node with 1 GPU, 4 nodes with 2 GPUs)                                                                                               |                                                | [Mahuika](../The_NeSI_High_Performance_Computers/Mahuika.md)               | Slurm and [Jupyter](../Interactive_computing_using_Jupyter/Jupyter_on_NeSI.md)                                      | NeSI users                                                     | Currently available                                                                                          |
| 7 NVIDIA A100 PCIe 40GB cards (4 nodes with 1 GPU, 2 nodes with 2 GPUs)                                                                                                    | Machine Learning (ML) applications             | [Mahuika](../The_NeSI_High_Performance_Computers/Mahuika.md)               | Slurm                                                                                                                                       | NeSI users                                                     | Currently available                                                                                          |
| 7 A100-1g.5gb instances (1 NVIDIA A100 PCIe 40GB card divided into [7 MIG GPU slices](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) with 5GB memory each) | Development and debugging                      | [Mahuika](Mahuika.md)               | Slurm and [Jupyter](../Interactive_computing_using_Jupyter/Jupyter_on_NeSI.md)                                      | NeSI users                                                     | Currently available                                                                                          |
| 5 NVIDIA Tesla P100 PCIe 12GB (5 nodes with 1 GPU)                                                                                                                         | Post-processing                                | [Māui Ancil](Maui_Ancillary.md) | Slurm                                                                                                                                       | NeSI users                                                     | Currently available                                                                                          |
| 4 NVIDIA HGX A100 (4 GPUs per board with 80GB memory each, 16 A100 GPUs in total)                                                                                          | Large-scale Machine Learning (ML) applications | [Mahuika](Mahuika.md)               | Slurm                                                                                                                                       | NeSI users                                                     | Available as part of the [Milan Compute Nodes](../Running_Jobs_on_Maui_and_Mahuika/Milan_Compute_Nodes.md) |
| 4 NVIDIA A40 with 48GB memory each (2 nodes with 2 GPUs, but capacity for 6 additional GPUs already in place)                                                              | Teaching / training                            | Flexible HPC                                                                                       | [Jupyter](../Interactive_computing_using_Jupyter/Jupyter_on_NeSI.md), VM, or bare metal tenancy possible (flexible) | Open to conversations with groups who could benefit from these | In development.                                                                                              |
