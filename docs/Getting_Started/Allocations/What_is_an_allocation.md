---
created_at: '2020-02-25T02:35:13Z'
tags:
    - account
title: What Is an Allocation?
description: What compute, online storage and Freezer allocations are and how they are granted
---

{% include 'partials/status-no-pro.md' %}

Because the HPC platform resources are limited, we manage access to our resources
through allocations. Typically, an allocation is a grant of a certain
amount of a resource, or of a rate at which a resource can be consumed,
during a defined period of time. Different types of resource have
different allocation criteria.

An allocation will come from one of our allocation classes. We will
decide what class of allocation is most suitable for you and your
research programme, however you're welcome to review
[our article on allocation classes](../../Policy/Allocation_Classes.md)
to find out what class you're likely eligible for.

## HPC Platform allocations

The form of our allocation you may be most familiar with is an
allocation of computing power. We currently offer three sorts of compute
allocations, of which your project needs at least two (online storage
plus one kind of compute allocation) in order to be valid and active.

Compute allocations are expressed in terms of a number of units, to be
consumed or reserved between a set start date and time and a set end
date and time. For allocations of computing power, we use [Fair
Share](../../Batch_Computing/Fair_Share.md)
to balance work between different projects.

### Compute allocations

These are measured in REANNZ Service Units (RSUs), with the price of hardware in terms of RSUs shown in the
following table.

|  Hardware type         |    Fair Share Price              |
|------------------------|----------------------------------|
| Milan CPU              | 0.9 RSUs per CPU-core-hour       |
| Milan Memory (RAM)     | 0.1286 RSUs per GB-hour          |
| Genoa CPU              | 1.4 RSUs per CPU-core-hour       |
| Genoa Memory (RAM)     | 0.20 RSUs per GB-hour            |
| A100 GPU device        | 36.0 RSUs per device-hour        |
| L4 GPU device          | 8.0 RSUs per device-hour         |
| H100 GPU device        | 162.0 RSUs per device-hour       |

The total RSU cost of a job is the sum of the costs of the
hardware it uses. Once the job has finished running, this composite price is
what affects your project's Fair Share score.

!!! note "Using up your compute allocation"
    You may continue to submit jobs even if you have used all of your
    compute allocation. The effect of having no RSUs remaining is a
    [lower Fair Share](../../Batch_Computing/Fair_Share.md),
    not the inability to use CPUs. Your ability to submit jobs will only be
    removed when your project's allocation expires, not when your RSUs are exhausted.

### Online storage allocations

An online storage allocation, unlike compute allocations, functions more
like a lease than a rate‑of‑consumption model. It provides your project
team with a fixed amount of disk space and a corresponding number of inodes
(directory entries, i.e., files and metadata) on our high‑performance online filesystems.
The inode limit is not normally visible to users, as the default allocation
is sufficient for most workflows. Online storage is typically granted to
both your persistent project directory and your temporary project directory.

## Freezer allocations

A Freezer storage allocation, like online storage allocations but
unlike compute allocations, is more like a lease than a rate of
consumption. It provides your project team with a defined amount
of storage space and a corresponding number of inodes (directory
entries, i.e., files and metadata) on our Tape system.

## Consultancy allocations

A consultancy allocation is for a number of scientific programmer hours
between two dates, or is sometimes expressed as a fraction of an FTE
between the same two dates. This reflects the commitment of our
scientific programming expertise to your project.

If you would like to discuss a consultancy allocation for your project,
please {% include "partials/support_request.html" %}.
