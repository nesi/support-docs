---
created_at: 2025-05-07
description: This article presents an overview comparison of the differences between the NeSI Mahuika cluster and the new cluster.
status: new
tags: 
    - hpc3
    - refresh
---

This article presents an overview comparison of the differences between the NeSI Mahuika cluster and the new cluster (often referred to in documentation under the provisional name HPC3).
It is not a comprehensive view of the differences and where appropriate individual support pages will be updated to reflect changes and enhancements.
For example the [Slurm Reference Sheet](../../Getting_Started/Cheat_Sheets/Slurm-Reference_Sheet.md) will have a number of changes made to it along with significant changes to the Slurm Partitions.

This page should be read in conjunction with the Known Issues which are not included here as they are temporary differences to be resolved soon.

If you are moving from Māui rather than Mahuika,
then please see [Preparing your code for use on NeSI's new HPC platform](../Announcements/Preparing_your_code_for_use_on_NeSIs_new_HPC_platform.md), and {% include "partials/support_request.html" %} if you require assistance.

## Login

We are now using Tuakiri to provide second-factor authentication, and this changes the login experience.  See [Standard Terminal Setup HPC3](../../Scientific_Computing/Terminal_Setup/Standard_Terminal_Setup_HPC3.md) for the full details.

## Operating System

Rocky Linux 9 rather than Centos 7 (and Rocky 8 on the Mahuika Milan nodes).
Rocky is similar to Centos, both being based on Red Hat Enterprise Linux (RHEL) source code,
but Rocky 9 is a much more recent release,
which brings many minor improvements and is supported by some software which has dropped support for Centos 7,
such as the latest versions of VSCode.

## Storage

### Disk

The GPFS `/home`, `/nesi/project`, and `/nesi/nobackup` file systems have been replaced by WEKA filesystems mounted at the same paths.  There may be some performance differences, mostly positive ones.
One particular feature of WEKA is that it keeps recently accessed files in fast SSD storage while moving other files out to slower disk-based storage.

There will no longer be any exemptions from nobackup autodeletion.
Instead a combination of increased project storage and moving data to Freezer (long term storage) will be used.

### Tape

[Freezer](../../Storage/Freezer_long_term_storage.md) replaces Nearline.

## Access via Web browser

[OnDemand](../../Scientific_Computing/Interactive_computing_with_NeSI_OnDemand/index.md) is replacing JupyterHub.
OnDemand is more flexible and can deliver more GUI based apps.

## Environment Modules

Our Apptainer, nano, s3cmd, and gnuplot environment modules have been depreciated - just use the system version of these tools instead.

The module save and module load commands can be used to save and load your custom sets of modules,
including a “default” one to load at login.
We don't particularly recommend that, except that it is better than loading environment modules in your `~/.bash_profile.`

## External IP address

This has changed, and so any institutional firewalls which let requests from NeSI in to a networked license sever will need updating.

## Slurm

Hyperthreading: All of our CPUs have this feature, so present two virtual CPUs on each CPU core.
On Mahuika mutithreaded jobs placed a thread on each virtual CPU by default,
with the restriction that different tasks would never share a core, so by default single-threaded MPI jobs were not hyperthreaded while single-task multithreaded jobs were.
On HPC3 `--threads-per-core` defaults to `1`, i.e: hyperthreading is avoided, but unlike Mahuika tasks are allowed to share a core if `--threads-per-core` is set to `2`. These settings may yet change, but parallel jobs can explicitly set  `--threads-per-core` to be sure.

Unsuitable memory request now give an error as opposed to a warning.
new HPC:
```
$ srun --partition=genoa2 --mem=20G --pty bash
srun: error: The genoa2 partition does not seem suitable for this job
srun: error: Unable to allocate resources: Job violates accounting/QOS policy (job submit limit, user's size and/or time limits)
```
Mahuika:
```
$ srun --partition=milan --mem=20G --pty bash
srun: "milan" is not the most appropriate partition for this job, which would otherwise default to "bigmem,infill". If you believe this is incorrect then please contact support@nesi.org.nz and quote the Job ID number.
srun: job 54606638 queued and waiting for resources
```
The solution is either remove the `--partition` specification and let Slurm choose the partition or select a partition with more suitable memory-per-CPU.

### Partitions & limits

These have changed.  As on Mahuika, the default should be OK, but if you want to select a particular microarchitecture you can use `-p milan` or `-p genoa`.  The three Cascade Lake “hugemem” nodes will also have their own partition.

### Prioritisation

Jobs with a high count of cores-per-node get a priority boost (visible in the “site factor” of `sprio`).  This is to help whole-node jobs get ahead of large distributed jobs with many tasks spread over many nodes.

There is a per-user limit on the job submit rate which will slow down workflow engines which submit too many jobs.  There are usually solutions to this such as array jobs or Snakemake's “groups” feature.

### Misc

KillOnBadExit is set true, so if one task in an MPI job fails, by default the whole job will be killed.

Each job gets is own `/tmp` & `/dev/shm`  (via Slurm's job_container/tmpfs plugin) so does not need to bother with `$TMPDIR`.

The batch scripts of recent jobs can be rediscovered with `sacct -B -j <jobid>`.  However because those are now being stored, batch script sizes are limited to 64 kB, down from 4 MB.
If that is a problem for your workflow we can probably help turn it into something shorter with appropriate use of loops.

## Hardware

Node sizes are different, so multithreaded jobs will probably have different optimal sizing.  

### Milan nodes

Each Milan node has two AMD Milan 7713 CPUs, each with 4 “I/O quadrants” of 2 "chiplets" of 8 cores and one level 3 cache, so each node has a total of 128 cores or 256 hyperthreaded CPUs.

The memory available to Slurm jobs is 512 GB per node, so approximately 2 GB per CPU.
There are 64 nodes available, 8 of which will have double the memory (1 TB).

### Genoa Nodes

Each Genoa node has two AMD Genoa 9634 CPUs, each with 12 "chiplets" of 7 cores and one level 3 cache, so each node has a total of 168 cores or 336 hyperthreaded CPUs.

The memory available to Slurm jobs on most of those nodes is 358 GB per node, so approximately 1 GB per CPU. There are 64 nodes available, 16 of which have more memory (1.5 TB).

### GPUs

The P100s are being retired.  The A100s will be moved into HPC3 along with the Milan nodes. 8 H100s and 16 L4s are available on various Genoa nodes.
