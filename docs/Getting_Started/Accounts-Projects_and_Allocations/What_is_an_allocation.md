---
created_at: '2020-02-25T02:35:13Z'
tags: 
    - Allocation
    - Allocations
    - Compute
title: What is an allocation?
---

Because NeSI's resources are limited, we manage access to our resources
through allocations. Typically, an allocation is a grant of a certain
amount of a resource, or of a rate at which a resource can be consumed,
during a defined period of time. Different types of resource have
different allocation criteria.

An allocation will come from one of our allocation classes. We will
decide what class of allocation is most suitable for you and your
research programme, however you're welcome to review
[our article on allocation classes](../Policy/Allocation_classes.md)
to find out what class you're likely eligible for.

## An important note on CPU hour allocations

You may continue to submit jobs even if you have used all your CPU-hour
allocation. The effect of 0 remaining CPU hours allocation is a
[lower fairshare](../../Batch_Computing/Fair_Share.md),
not the inability to use CPUs. Your ability to submit jobs will only be
removed when your project's allocation expires, not when core-hours are
exhausted.

## HPC Platform allocations

The form of NeSI allocation you may be most familiar with is an
allocation of computing power. We currently offer three sorts of compute
allocations, of which your project needs at least two (online storage
plus one kind of compute allocation) in order to be valid and active.

Compute allocations are expressed in terms of a number of units, to be
consumed or reserved between a set start date and time and a set end
date and time. For allocations of computing power, we use [Fair
Share](../../Batch_Computing/Fair_Share.md)
to balance work between different projects. NeSI allocations and the
relative "prices" of resources used by those allocations should not be
taken as any indicator of the real NZD costs of purchasing or running
the associated infrastructure and services.

### Allocations

Allocations are measured in compute units, with the price of hardware in terms of compute units shown in the
following table.

|  Hardware type         |    Fair Share Price                     |
|------------------------|-----------------------------------------|
| Milan CPU              | 0.9 compute units per physical-CPU-hour |
| Milan Memory (RAM)     | 0.13 compute units per GB-hour          |
| Genoa CPU              | 1.4 compute units per physical-CPU-hour |
| Genoa Memory (RAM)     | 0.20 compute units per GB-hour          |
| A100 GPU device        | 18.0 compute units per device-hour      |
| A100-1g.5gb GPU device | 3.0 compute units per device-hour       |
| L4 GPU device          | 4.0 compute units per device-hour       |
| H100 GPU device        | 40.0 compute units per device-hour      |

The total compute unit cost of a job is the sum of these three
components. Once the job has finished running, this composite price is
what affects your project's Fair Share score. However, whether your
institution will be charged based on the composite price or based on
your job's CPU core hour consumption alone, or on some other basis, will
depend on your contractual arrangements with NeSI.

### Online storage allocations

An online storage allocation, unlike compute allocations, is more like a
lease than a rate of consumption. It is an amount of disk space and,
concurrently, a number of inodes (directory entries, i.e. files etc.)
that have been made available for your project team to use on our online
high-performance filesystem. An online storage allocation is typically
granted to your persistent project directory.

We do not yet have a ratio of online storage disk space or inodes to
compute units.

## Data storage allocations

### Freezer storage allocations

A Freezer storage allocation, like online storage allocations but
unlike compute allocations, is more like a lease than a rate of
consumption. It is an amount of space and, concurrently, a number of
inodes (directory entries, i.e. files etc.) that have been made
available for your project team to use on our nearline apparatus.

We do not yet have a ratio of nearline storage tape space or inodes to
compute units.

## Consultancy allocations

A consultancy allocation is for a number of scientific programmer hours
between two dates, or is sometimes expressed as a fraction of an FTE
between the same two dates. This reflects the commitment of NeSI
scientific programming expertise to your project.

We do not yet have a ratio of consultancy hours to compute
units.
