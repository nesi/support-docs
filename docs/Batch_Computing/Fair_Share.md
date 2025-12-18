---
created_at: '2019-02-05T03:58:21Z'
tags:
  - accounting
  - Slurm
  - Fairshare
  - Fair Share
  - Job priority
  - Long queue time
  - Queing
  - long wait time
description: How balancing your workload lets you make the most of your allocation.
---

The fair-share system is designed to encourage users to balance their
use of resources over their allocation period. Fair-share is the largest
factor in determining priority, but not the only one. For more details
see [Job Prioritisation](Job_prioritisation.md).

## Fair Share Score

Your *Fair Share score* is a number between **0** and **1**. Projects
with a **larger** Fair Share score receive a **higher priority** in the
queue.

A project is given an [allocation of compute units](../Getting_Started/Allocations/What_is_an_allocation.md)
over a given **period**. An institution also has a percentage **Fair Share entitlement**
of the cluster's deliverable capacity over that same period.

- **Your project's expected rate of use** = (**your institution's Fair
    Share entitlement** × **your project's allocation**) / (**sum of
    your institution's allocations** × **period**)
- **Your institution's expected rate of use** = your institution's
    **Fair Share entitlement** on that machine

If an entity — an institution or project team — is using the machine
more slowly than expected, for Fair Share purposes it is considered a
light user. By contrast, one using the machine faster than expected is a
heavy user.

- Projects at lightly using institutions get a higher Fair Share score
    than those at heavily using institutions.
- Within each institution, lightly using projects get a higher Fair
    Share score than heavily using projects.
- Using **faster** than your **expected rate of usage** will usually
    cause your Fair Share score to **decrease**. The more extreme the
    overuse, the more severe the likely drop.
- Using **slower** than your **expected rate of usage** will usually
    cause your Fair Share score to **increase**. The more extreme the
    under-use, the greater the Fair Share bonus.
- Using the cluster **unevenly** will cause your Fair Share score to
    **decrease**.

## What is Fair Share?

Fair Share is a mechanism to set job priorities. It is based on a share
of the cluster, that is, a fraction of the cluster's overall computing
capacity.

A project's expected rate of use is based on that project's
percentage share of all then-current allocations awarded to that
project's institution on the cluster. This percentage share is in turn
derived from the sizes (in compute units) and duration (in
days) — and thus the expected rates of use of those same allocations.

Therefore:

- If the size of your allocation increases, your project's share of
    the cluster will increase. Conversely, if the size of your
    allocation decreases, your project's share of the cluster will
    decrease.
- If the size of another project's allocation increases, your
    project's share of the cluster will decrease, since, even though
    your allocation's size has remained the same, the total size of
    other allocations has increased and thus your allocation's share has
    decreased. Conversely, if the size of the other project's allocation
    decreases, your project's share of the cluster will increase.
- If the cluster gets larger (e.g. we purchase and install more
    computing capacity), your project's share of the cluster will not
    change, but that share of the cluster will correspond to a higher
    rate of compute usage. This situation will only last until more
    allocations are issued, or existing allocations are made larger, to
    take advantage of the increased capacity. The opposite will occur if
    the cluster shrinks, though cluster shrinkage is not expected to
    occur.

Fair Share is not designed to ensure
that all project teams get the same share of the cluster.

## How does Fair Share work?

The starting point for a Fair Share calculation is a comparison of the
project's actual share of use to the expected share of use. This share
of use is based on what all users of the cluster have actually used
during the relevant period of time, not what the cluster was capable of
delivering during that same period. Currently, each period is five
minutes.

Because five minutes is a short time, Fair Share aggregates the
ratio of actual share to expected share since records began on that
cluster. But as the time gets further back from the present, each
five-minute window has slightly less influence on fair share scores. Our
current configuration has it that after two weeks (that is, 4,032
successive five-minute windows), the effect of the ratio for that
five-minute slice is worth only half of what it was worth initially;
after four weeks, it is worth a quarter; after six weeks, one eighth;
and so on. The effect of this decay curve is that over-use or under-use in
the recent past has a greater effect on your project's fair share score
than the same extent of overuse or under-use long ago.

One important implication of Fair Share is that allocations are
implicitly aged: you cannot bank core hours by refraining from
submitting work. If, for example, you expect to have a lot of
computational work to carry out in September, you can't get a
significant priority boost in September by refraining from carrying out
computational work in March. In fact, you will get the best advantage
from Fair Share by submitting work at close to a constant rate.

If you expect that your project team will need widely varying rates of
computer use during your allocation period and you can predict when your
busy and quiet periods will be, please {% include "partials/support_request.html" %} to enquire
about splitting your project's allocation up into parts. Please be aware
that we cannot guarantee this option will be available for any given
project, and that we are most likely to be able to accommodate such a
request for projects that expect to use the cluster heavily on average,
can predict when they will need their heaviest use with a high degree of
confidence, and give us plenty of notice.

See the [Slurm documentation](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/priority_multifactor.html#fairshare) for full details on Slurm's Fair share mechanism

## How do I check my project's Fair Share score?

The `sshare` command, on a Mahuika login node, will show the fair
    share tree. A related command, `nn_sshare_sorted`, will show
    projects in order from the highest fair share score to the lowest.

In our current configuration, Fair Share scores are attached to
projects, not to individual users.

## My project's Fair Share score is too low. How can I improve it?

If you have just carried out an unusually large spike of work, your fair
share score will naturally be lowered for a while, and should come back
to normal after a few days.

If, on the other hand, you have more work to do than expected, please
{% include "partials/support_request.html" %} to apply for an early allocation increase.

If you believe your project's fair share score has become corrupted, or
your ability to get work done is affected by a low Fair Share
entitlement for your institution on that cluster, please {% include "partials/support_request.html" %}.
