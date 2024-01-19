---
created_at: '2020-02-25T02:35:13Z'
tags: []
title: What is an allocation?
vote_count: 3
vote_sum: -1
zendesk_article_id: 360001385735
zendesk_section_id: 360000196195
---

Because NeSI's resources are limited, we manage access to our resources
through allocations. Typically, an allocation is a grant of a certain
amount of a resource, or of a rate at which a resource can be consumed,
during a defined period of time. Different types of resource have
different allocation criteria.

An allocation will come from one of our allocation classes. We will
decide what class of allocation is most suitable for you and your
research programme, however you're welcome to review [our article on
allocation classes](../../General/NeSI_Policies/Allocation_classes.md)
to find out what class you're likely eligible for.

## HPC Platform allocations

The form of NeSI allocation you may be most familiar with is an
allocation of computing power. We currently offer three sorts of compute
allocations, of which your project needs at least two (online storage
plus one kind of compute allocation) in order to be valid and active.

Compute allocations are expressed in terms of a number of units, to be
consumed or reserved between a set start date and time and a set end
date and time. For allocations of computing power, we use [Fair
Share](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Fair_Share.md)
to balance work between different projects. NeSI allocations and the
relative "prices" of resources used by those allocations should not be
taken as any indicator of the real NZD costs of purchasing or running
the associated infrastructure and services.

### Mahuika allocations

Allocations on
[Mahuika](../../Scientific_Computing/The_NeSI_High_Performance_Computers/Mahuika.md)
are measured in Mahuika compute units. A job uses one Mahuika compute
unit if it runs for one hour on one physical Mahuika CPU core (two
logical CPUs), using 3 GB of RAM and no GPU devices. This means a single
Mahuika compute unit is equivalent to what we previously called a "Fair
Share adjusted core-hour" on Mahuika's standard compute nodes.

The price of hardware in terms of compute units is shown in the
following table.

|  Hardware type         |    Fair Share Price                     |
|------------------------|-----------------------------------------|
| CPU                    | 0.35 compute units per logical-CPU-hour |
| Memory (RAM)           | 0.10 compute units per GB-hour          |
| P100 GPU device        | 7.0 compute units per device-hour       |
| A100 GPU device        | 18.0 compute units per device-hour      |
| A100-1g.5gb GPU device | 3.0 compute units per device-hour       |

The total compute unit cost of a job is the sum of these three
components. Once the job has finished running, this composite price is
what affects your project's Fair Share score. However, whether your
institution will be charged based on the composite price or based on
your job's CPU core hour consumption alone, or on some other basis, will
depend on your contractual arrangements with the NeSI host.

Note that the minimum number of logical cores a job can take on Mahuika
is two
(see [Hyperthreading](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Hyperthreading.md) for
details). Therefore:

- the lowest possible price for a CPU-only job is 0.70 compute units
    per hour, plus memory (RAM).
- the lowest possible price for a CPU + P100 GPU job is 7.70 compute
    units per hour, plus memory (RAM).
- the lowest possible price for a CPU + A100 GPU job is 18.70 compute
    units per hour, plus memory (RAM).

In reality, every job must request at least some RAM.

### Māui allocations

The compute capacity of the
[Māui](../../Scientific_Computing/The_NeSI_High_Performance_Computers/Maui.md)
supercomputer is allocated by node-hours. Though some Māui nodes have
more RAM than others, we do not currently distinguish between low-memory
and high-memory nodes for allocation, billing or Fair Share purposes.

Each allocation on Māui includes an entitlement to use the Māui
ancillary nodes equally with other NeSI projects having Māui allocations
at that time.

One Māui node hour is roughly equivalent to 40 Mahuika compute units.

### Online storage allocations

An online storage allocation, unlike compute allocations, is more like a
lease than a rate of consumption. It is an amount of disk space and,
concurrently, a number of inodes (directory entries, i.e. files etc.)
that have been made available for your project team to use on our online
high-performance file system. An online storage allocation is typically
granted to your persistent project directory.

We do not yet have a ratio of online storage disk space or inodes to
Mahuika compute units.

## Data storage allocations

### Nearline storage allocations

A nearline storage allocation, like online storage allocations but
unlike compute allocations, is more like a lease than a rate of
consumption. It is an amount of space and, concurrently, a number of
inodes (directory entries, i.e. files etc.) that have been made
available for your project team to use on our nearline apparatus.

We do not yet have a ratio of nearline storage tape space or inodes to
Mahuika compute units.

## Consultancy allocations

A consultancy allocation is for a number of scientific programmer hours
between two dates, or is sometimes expressed as a fraction of an FTE
between the same two dates. This reflects the commitment of NeSI
scientific programming expertise to your project.

We do not yet have a ratio of consultancy hours to Mahuika compute
units.