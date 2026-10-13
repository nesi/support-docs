---
created_at: '2019-02-05T03:58:21Z'
tags:
  - account
  - slurm
  - fairshare
  - troubleshooting
description: How Fairshare sets your project's job priority on Mahuika, why steady use keeps it high, and how to check and improve your project's Fairshare score.
---

Fairshare is the largest part of a job's [priority](Job_Prioritisation.md).
It compares how much of the cluster your project has used recently with how much it is expected to use, based on its allocation.
Projects that have used less than expected get a higher priority, and projects that have used more get a lower one.

To keep your priority high, submit work at a steady rate through your allocation period.
You cannot save priority up by not running jobs, and a burst of work lowers your priority just when most of your jobs are waiting.

## How the score is calculated

Each project has a Fairshare score between 0 and 1, and a higher score means a higher priority.
The score adds up to {{ slurm_limits.priority.fairshare_points }} points to the priority of each of the project's jobs, shown in the `FairShare` column of `sprio`.

The score compares:

- **Expected use:** your project's share of the cluster.
  Each institution has a share of the cluster, and your project gets part of its institution's share in proportion to the size of its [allocation](../Getting_Started/Allocations/What_is_an_allocation.md).
- **Actual use:** what your project's jobs have recently used.

Institutions are compared with each other first, then projects within each institution.
A project at an institution that is using less than its share gets a higher score than one at an institution using more.

Recent use counts most. Usage has a half-life of {{ slurm_limits.priority.half_life_days }} days:
use from {{ slurm_limits.priority.half_life_days }} days ago counts half as much as use today, and use from twice as long ago counts a quarter.

Your share also depends on other allocations.
If other projects at your institution get larger allocations, your project's share gets smaller, even though your own allocation is the same.

Using all of your allocation does not stop your jobs running. It only lowers your score.

For the full algorithm, see the [Slurm Fairshare documentation](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/priority_multifactor.html#fairshare).

## Check your project's score

```sh
sshare -U
```

The `FairShare` column shows the score for each project you belong to.
Scores belong to projects, not to users, so everyone in a project has the same score.

## Improve a low score

After a burst of work, your score recovers by itself as that usage decays.

{% include "partials/support_request.html" %} if you have more work than your allocation covers and need an early allocation increase, or if your score looks wrong.
