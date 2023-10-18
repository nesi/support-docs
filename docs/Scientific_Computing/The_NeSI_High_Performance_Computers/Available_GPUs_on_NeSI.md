---
created_at: '2022-06-13T04:54:38Z'
hidden: false
label_names: []
position: 6
title: Available GPUs on NeSI
vote_count: 2
vote_sum: 2
zendesk_article_id: 4963040656783
zendesk_section_id: 360000034335
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
NeSI has a range of Graphical Processing Units (GPUs) to accelerate
compute-intensive research and support more analysis at scale. Depending
on the type of GPU, you can access them in different ways, such as via
batch scheduler (Slurm), interactively (using [Jupyter on
NeSI](https://support.nesi.org.nz/hc/en-gb/articles/360001555615)), or
Virtual Machines (VMs). 

The table below outlines the different types of GPUs, who can access
them and how, and whether they are currently available or on the future
roadmap.

If you have any questions about GPUs on NeSI or the status of anything
listed in the table, [contact
Support](https://support.nesi.org.nz/hc/en-gb/requests/new).

 

<table>
<thead>
<tr class="header">
<th>GPGPU</th>
<th>Purpose</th>
<th>Location</th>
<th>Access mode</th>
<th>Who can access</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>9 NVIDIA Tesla P100 PCIe 12GB cards (1 node with 1 GPU, 4 nodes with
2 GPUs)</td>
<td> </td>
<td><a
href="https://support.nesi.org.nz/hc/en-gb/articles/360000163575">Mahuika</a></td>
<td>Slurm and <a
href="https://support.nesi.org.nz/hc/en-gb/articles/360001555615">Jupyter</a></td>
<td>NeSI users</td>
<td>Currently available</td>
</tr>
<tr class="even">
<td>7 NVIDIA A100 PCIe 40GB cards (4 nodes with 1 GPU, 2 nodes with 2
GPUs)</td>
<td>Machine Learning (ML) applications</td>
<td><a
href="https://support.nesi.org.nz/hc/en-gb/articles/360000163575">Mahuika</a></td>
<td>Slurm</td>
<td>NeSI users</td>
<td>Currently available</td>
</tr>
<tr class="odd">
<td>7 A100-1g.5gb instances (1 NVIDIA A100 PCIe 40GB card divided into
<a
href="https://www.nvidia.com/en-us/technologies/multi-instance-gpu/">7
MIG GPU slices</a> with 5GB memory each)</td>
<td>Development and debugging</td>
<td><a
href="https://support.nesi.org.nz/hc/en-gb/articles/360000163575">Mahuika</a></td>
<td>Slurm and <a
href="https://support.nesi.org.nz/hc/en-gb/articles/360001555615">Jupyter</a></td>
<td>NeSI users</td>
<td>Currently available</td>
</tr>
<tr class="even">
<td>5 NVIDIA Tesla P100 PCIe 12GB (5 nodes with 1 GPU)</td>
<td>Post-processing</td>
<td><a
href="https://support.nesi.org.nz/hc/en-gb/articles/360000203776-M%C4%81ui-Ancillary-Nodes">Māui
Ancil</a></td>
<td>Slurm</td>
<td>NeSI users</td>
<td>Currently available</td>
</tr>
<tr class="odd">
<td>4 NVIDIA HGX A100 (4 GPUs per board with 80GB memory each, 16 A100
GPUs in total)</td>
<td>Large-scale Machine Learning (ML) applications</td>
<td><a
href="https://support.nesi.org.nz/hc/en-gb/articles/360000163575">Mahuika</a></td>
<td>Slurm</td>
<td>NeSI users</td>
<td>Available as part of the <a
href="https://support.nesi.org.nz/knowledge/articles/6367209795471">Milan
Compute Nodes</a></td>
</tr>
<tr class="even">
<td>4 NVIDIA A40 with 48GB memory each (2 nodes with 2 GPUs, but
capacity for 6 additional GPUs already in place)</td>
<td>Teaching / training</td>
<td>Flexible HPC</td>
<td><a
href="https://support.nesi.org.nz/hc/en-gb/articles/360001555615">Jupyter</a>,
VM, or bare metal tenancy possible (flexible)</td>
<td>Open to conversations with groups who could benefit from these</td>
<td>In development.</td>
</tr>
</tbody>
</table>
