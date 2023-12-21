---
created_at: '2022-03-22T02:16:17Z'
hidden: false
weight: 0
tags:
- general
title: Slurm upgrade to version 21.8
vote_count: 0
vote_sum: 0
zendesk_article_id: 4544913401231
zendesk_section_id: 200732737
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

-   Added `--me` option, equivalent to` --user=$USER`.
-   Added "pendingtime" as a option for --Format.
-   Put sorted start times of "N/A" or 0 at the end of the list.

<!-- -->

-   Add time specification: "now-" (i.e. subtract from the present)
-   AllocGres and ReqGres were removed. Alloc/ReqTres should be used
    instead. 

<!-- -->

-   MAGNETIC flag on reservations. Reservations the user doesn't have to
    even request.
-   The LicensesUsed line has been removed from `scontrol show config` .
    Please use updated `scontrol show licenses` command as an
    alternative.

<!-- -->

-    `--threads-per-core` now influences task layout/binding, not just
    allocation.
-   `--gpus-per-node` can be used instead of `--gres=GPU`
-   `--hint=nomultithread` can now be replaced
    with `--threads-per-core=1`
-   The inconsistent terminology and environment variable naming for
    Heterogeneous Job ("HetJob") support has been tidied up.
-   The correct term for these jobs are "HetJobs", references to
    "PackJob"   have been corrected.
-   The correct term for the separate constituent jobs are
    "components",   references to "packs" have been corrected.

<!-- -->

-   Added support for an "Interactive Step", designed to be used with
    salloc to launch a terminal on an allocated compute node
    automatically. Enable by setting "use\_interactive\_step" as part of
    LaunchParameters.

<!-- -->

-    By default, a step started with srun will be granted exclusive (or
    non- overlapping) access to the resources assigned to that step. No
    other parallel step will be allowed to run on the same resources at
    the same time. This replaces one facet of the '--exclusive' option's
    behavior, but does not imply the '--exact' option described below.
    To get the previous default behavior - which allowed parallel steps
    to share all resources - use the new srun '--overlap' option.
-   In conjunction to this non-overlapping step allocation behavior
    being the new default, there is an additional new option for step
    management '--exact', which will allow a step access to only those
    resources requested by the step. This is the second half of the
    '--exclusive' behavior. Otherwise, by default all non-gres resources
    on each node in the allocation will be used by the step, making it
    so no other parallel step will have access to those resources unless
    both steps have specified '--overlap'.

<!-- -->

-   New command which permits crontab-compatible job scripts to be
    defined. These scripts will recur automatically (at most) on the
    intervals described.