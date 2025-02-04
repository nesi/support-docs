---
created_at: '2019-11-11T21:40:21Z'
tags: []
title: "Mahuika - M\u0101ui Differences"
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001244876
zendesk_section_id: 360000039036
---

Aside from differences in software stack there are a few other
differences between the platforms to be aware of.

## Logging in

Both Mahuika and Māui require logging in to the Lander node first.

```sh
ssh user123@lander.nesi.org.nz
```

As you log in to the Lander node, you can expect to receive the
following prompts:

```sh
Login Password (First Factor):
```

```sh
Authenticator Code (Second Factor):
```

Note that being prompted for `Authenticator Code (Second Factor)` does
not prove that the system has accepted your
`Login Password (First Factor)` as correct. If you enter either
incorrectly, you will be prompted again for both.

### Mahuika

Mahuika follows the same procedure as the lander node, except that it
doesn't ask for a second factor.

```sh
ssh login.mahuika.nesi.org.nz
```

You will be prompted:

```sh
Login Password:
```

At this prompt, enter only your password (a.k.a. first factor).

### Māui

Māui differs slightly in how you are authenticated the first time.

```sh
ssh login.maui.nesi.org.nz
```

You will be prompted.

```sh
Password:
```

At this prompt, enter only your password (a.k.a. first factor).

## Job Limits

Both Māui and Mahuika have limits on the size and types of jobs you can
run, but the limits on each machine is different.

### Mahuika

Currently, Mahuika has Intel Broadwell and [AMD Milan../../Scientific_Computing_old/Running_Jobs_on_Maui_and_Mahuika/Milan_Compute_Nodes.md
CPUs](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Milan_Compute_Nodes.md).
To run on the faster AMD Milan CPUs you will need to specify
"--partition=milan" in your Slurm script.

Mahuika is made up of several [partitions which have different resources../../Scientific_Computing_old/Running_Jobs_on_Maui_and_Mahuika/Mahuika_Slurm_Partitions.md
and different
limits](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Mahuika_Slurm_Partitions.md).
A job can request up to 20,000 CPU core hours, running up to 3 weeks
with up to 576 CPU cores (equivalent to eight full nodes). Furthermore,
there are special nodes available with high memory (up to 6 TB) or GPUs.

Depending on what resources you are requesting and for how long, your
jobs will be automatically assigned to the most suitable partition on
any of the Intel Broadwell partitions. (You will still need to specify
--partition=milan to run on the AMD Milan nodes.)

Mahuika allows the submission of jobs with variable numbers of CPUs and
amounts of RAM (memory). The nodes your job is running on will probably
be shared with other jobs.

### Māui

Māui only has a [single partition to which NeSI users are permitted to../../Scientific_Computing_old/Running_Jobs_on_Maui_and_Mahuika/Maui_Slurm_Partitions.md
submit
work](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Maui_Slurm_Partitions.md).
For your job, you can request a maximum of 24 hours or a maximum of 240
nodes, however no job may request more than 1,200 Māui node-hours in
total. (This means that if you request more than 50 nodes, your maximum
allowed time will start decreasing.) Māui only allows submission of jobs
in units of nodes, so the smallest possible job takes a whole node, and
there can never be more than one job on a node at a time.

Additionally, projects with valid allocations on Māui will also have
access to [Māui's ancillary../../Scientific_Computing_old/The_NeSI_High_Performance_Computers/Maui_Ancillary.md
nodes,](../../Scientific_Computing/The_NeSI_High_Performance_Computers/Maui_Ancillary.md)
where jobs requiring up to 768 GB of memory or jobs that require GPUs
can be run. When submitting a job to the Māui ancillary nodes you may
also request parts of nodes, rather than needing to use the entire node.
Because there are relatively few Māui ancillary nodes, if you require
substantial amounts of time on nodes like the Māui ancillary nodes, we
may grant your project an additional allocation on Mahuika. If we do so,
we will not forbid you from using the Māui ancillary nodes while your
Māui allocation remains valid and you are permitted to access NeSI
clusters.
