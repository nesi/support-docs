---
created_at: '2018-05-01T23:29:39Z'
hidden: false
weight: 1
tags:
- hpc
- info
title: Overview
vote_count: 2
vote_sum: 0
zendesk_article_id: 360000175735
zendesk_section_id: 360000034335
---

The NeSI High Performance Computers
[Māui](Maui.md) and
[Mahuika](Mahuika.md) provide
the New Zealand research community with access to a national
data-centric and data intensive research computing environment built on
leading edge high performance computing (HPC) systems.

- Māui, which in Maori mythology is credited with catching a giant
    fish using a fishhook taken from his grandmother's jaw-bone; the
    giant fish would become the North Island of New Zealand, provides a
    Capability (i.e. Supercomputer) HPC resource on which researchers
    can run simulations and calculations that require large numbers
    (e.g. thousands) of processing cores working in a tightly-coupled,
    parallel fashion.
- Mahuika, which in Maori mythology, is a fire deity, from whom Māui
    obtained the secret of making fire, provides a Capacity (i.e.
    Cluster) HPC resource to allow researchers to run many small (e.g.
    from 1 core to a few hundred cores) compute jobs simultaneously
    (aka  High Throughput Computing).

Māui and Mahuika share the same high performance filesystems,
accordingly, data created on either system are visible on the other
(i.e. without the need to copy data between systems). However, they have
different processors (Skylake on Māui, and Broadwell on Mahuika), and
different flavours of Linux (SLES on Māui and CentOS on Mahuika), so
shared applications should be explicitly compiled and linked for each
architecture. These systems and Ancillary Nodes on Mahuika and
on [Māui](Maui.md)  provide
the research community with:

- Leading edge HPCs (both Capacity and Capability) via a single point
    of access;
- New user facing services that can act on the data held within the NeSI HPC infrastructure, including:
  - Pre- and post-processing systems to support workflows;
  - Virtual Laboratories that provide interactive access to science domain specific tools \[Coming soon\];
  - Remote visualisation services \[Coming soon\];
  - Advanced data analytics tools, and
  - The ability to seamlessly move data between high performance disk storage and offline tape.
- Offsite replication of critical data (both online and offline).

These systems are
[accessed](../../Getting_Started/Accessing_the_HPCs/Choosing_and_Configuring_Software_for_Connecting_to_the_Clusters.md)
via a “lander” node using [two-factor
authentication](../../Getting_Started/Accessing_the_HPCs/Setting_Up_Two_Factor_Authentication.md).

NeSI researchers have access to all compute nodes on Mahuika, and 316
compute nodes on Māui.
