---
created_at: '2022-06-13T04:54:38Z'
description:  This page below outlines the different types of GPUs available on NeSI
tags:
 - gpu
---


NeSI has a range of Graphical Processing Units (GPUs) to accelerate compute-intensive research and support more analysis at scale.
Depending on the type of GPU, you can access them in different ways, such as via batch scheduler (Slurm), interactively (using Jupyter on NeSI),
or Virtual Machines (VMs).

The table below outlines the different types of GPUs,
who can access them and how, and whether they are currently available or on the future roadmap.

If you have any questions about GPUs on NeSI or the status of anything listed in the table,
{% include "partials/support_request.html" %}.

| GPGPU | Purpose/Note | Location | Access mode | Who can access | Status |
|-------|---------|----------|-------------|----------------|--------|
| 8 NVIDIA A100 PCIe 40GB cards (4 nodes with 1 GPU, 2 nodes with 2 GPUs) | Machine Learning (ML) applications | Mahuika | Slurm | NeSI users | Currently available |
| 4 NVIDIA HGX A100 (4 GPUs per board with 80GB memory each, 16 A100 GPUs in total) | Large-scale Machine Learning (ML) applications | Mahuika | Slurm | NeSI users | Available as part of the Milan Compute Nodes |
| 8 NVIDIA H100 96GB (4 nodes 2 GPUs)/node | Large-scale Machine Learning (ML) applications | Mahuika | Slurm | NeSI users | Available as part of the genoa Compute Nodes |
| 16 NVIDIA L4 (4 nodes 4 GPUs)/node | no fp64 double precision | Mahuika | Slurm | NeSI users | Available as part of the genoa Compute Nodes |
| 4 NVIDIA A40 with 48GB memory each (2 nodes with 2 GPUs, but capacity for 6 additional GPUs already in place) | Teaching / training | Flexible HPC | Jupyter, VM, or bare metal tenancy possible (flexible) | Open to conversations with groups who could benefit from these | In development. |
