---
created_at: '2020-09-04T02:01:07Z'
hidden: false
label_names: []
position: 9
title: "Improvements to Fair Share job prioritisation on M\u0101ui"
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001829555
zendesk_section_id: 200732737
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
*On Thursday 3 September 2020, NeSI updated the way we prioritise jobs
on the Māui HPC platform.*

## Background

Since the start of the year, we have been using Slurm's Fair Tree
algorithm on Māui (*not yet on Mahuika*) to prioritise jobs. This
provides a hierarchical structure to Slurm's account management, with
the hierarchy representing shares of a total cluster under Slurm's
control. This enables control of higher level or aggregate account
considerations, such as ensuring a group of projects within a research
programme or institution are ensured access to their share of a cluster.

Under our Fair Tree implementation, each of [NeSI's four collaborating
institutions](https://www.nesi.org.nz/about-us) is assigned a percentage
share of Māui, alongside a percentage share for MBIE's Merit allocations
(including Postgraduate and Proposal Development allocations), and the
remainder as a share to allocations coming from subscriptions.

These six shares, or what we in NeSI call national pools, are then
ranked in order, starting with the pool that has been using at the
lowest rate compared to its allocated percentage share. *See [this
page](https://slurm.schedmd.com/fair_tree.html) (off site) for more
details about Slurm's Fair Tree algorithm.*

Previously, we had given each pool a hard-coded share of Māui use. These
hard-coded shares did not reflect ongoing rounds of allocations given to
projects, and so some researchers were suffering from deprioritised
jobs. These jobs ended up delayed in the queue, sometimes excessively.

## What has changed?

We have now recalculated the shares for each pool to take into account
the following:

-   The investments into HPC platforms by the various collaborating
    institutions and by MBIE;
-   The capacity of each HPC platform;
-   The split of requested time (allocations) by project teams between
    the Māui and Mahuika HPC platforms, both overall and within each
    institution's pool.

Under this scheme, any job's priority is affected by the behaviour of
other workload within the same project team, but also other project
teams drawing on the same pool. In particular, even if your project team
has been under-using compared to your allocation, your jobs may still be
held up if:

-   Other project teams at your institution (within your pool) have been
    over-using compared to their allocations, or
-   Your institution has approved project allocations totalling more
    time than it is entitled to within its pool's share.

## What will I notice?

If your institution or pool's ranking has not changed, nothing much will
immediately change for you.

However, if your institution or pool's assigned share of the machine has
increased, it will become easier to move up the priority rankings, at
least in the short term.

Conversely, if your institution or pool's assigned share of the machine
has decreased, it will become easier to move down the rankings. This
change is one you are more likely to notice over time.

Whenever your institution or pool's ranking changes, whether because of
usage or because we adjust the assigned shares based on ongoing rounds
of allocations, your job priorities will alter almost immediately.
Moving up the rankings will increase your job priorities. Moving down
the rankings will decrease your job priorities.

## What other changes are NeSI planning on making?

We are looking at introducing Fair Tree on Mahuika as well, though not
on Māui ancillary nodes. We will announce this change well ahead of any
planned introduction.

We will also adjust the assigned Fair Tree shares on Māui routinely so
we don't diverge from allocations across HPC platforms again.
