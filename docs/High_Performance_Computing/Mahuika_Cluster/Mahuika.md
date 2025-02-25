---
created_at: '2018-04-22T21:09:28Z'
tags:
- hpc
- mahuika
- cs400
title: Mahuika
vote_count: 7
vote_sum: 3
zendesk_article_id: 360000163575
zendesk_section_id: 360000034335
---

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

## Notes

1. The Cray Programming Environment on Mahuika, differs from that on
    Māui.
2. The `/home, /nesi/project`, and `/nesi/nobackup`
    [filesystems](The_NeSI_High_Performance_Computers/NeSI_File_Systems_and_Quotas.md)
    are mounted on Mahuika.
3. Read about how to compile and link code on Mahuika in section
    entitled: [Compiling software on Mahuika.](The_NeSI_High_Performance_Computers/Compiling_software_on_Mahuika.md)
4. An extension to Mahuika with additional, upgraded resources is also
    available. see [Milan Compute Nodes](The_NeSI_High_Performance_Computers/Milan_Compute_Nodes.md)
    for details on access

