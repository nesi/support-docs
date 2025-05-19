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

This page should be read in conjunction with the [Known Issues](../Announcements/Known_Issues_HPC3.md) which are not included here as they are temporary differences to be resolved soon.

If you are moving from Māui rather than Mahuika,
then please see [Preparing your code for use on NeSI's new HPC platform](../Announcements/Preparing_your_code_for_use_on_NeSIs_new_HPC_platform.md), and {% include "partials/support_request.html" %} if you require assistance.

## Login

We are now using Tuakiri to provide second-factor authentication, and this changes the login experience.  See [Standard Terminal Setup HPC3](../../Scientific_Computing/Terminal_Setup/Standard_Terminal_Setup.md) for the full details.

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

Storage (byte) quotas in WEKA work the same way, but there are no inode (file) quotas.

We have had [automatic compression of some files](../../Storage/File_Systems_and_Quotas/Data_Compression/) enabled in GPFS for some time. We don't have an equivalent enabled in WEKA, and so highly compressable files (such as long output logs with many numbers in them) may appear to expand in size around five-fold without their content changing. To see if that is going to happen to your files you can compare the outputs from `du -h ...` and `du -h --apparent-size ...` on Mahuika. `--apparent-size` will give a larger number if GPFS has stored the file in a compressed state.  Compressing such files explicitly with a tool such as `gzip` would help, but some projects with many such files and small storage quotas might need those quotas raised. 

There will no longer be any exemptions from nobackup autodeletion.
Instead a combination of increased project storage and moving data to Freezer (long term storage) will be used.

### Tape

[Freezer](../../Storage/Freezer_long_term_storage.md) replaces Nearline.

## Access via Web browser

[OnDemand](../../Scientific_Computing/Interactive_computing_with_NeSI_OnDemand/index.md) is replacing JupyterHub.
OnDemand is more flexible and can deliver more GUI based apps.

## Environment Modules

Our *Apptainer*, *nano*, *s3cmd*, and *gnuplot* environment modules have been depreciated - just use the system version of these tools instead.

The `module save` and `module load` commands can be used to save and load your custom sets of modules,
including a “default” one to load at login.
We don't particularly recommend that, except that it is better than loading environment modules in your `~/.bash_profile.`

## External IP address

This has changed to 163.7.147.128/26, i.e. 163.7.147.128 - 163.7.147.191, and so any institutional firewalls which let requests from NeSI in to a networked license sever will need updating.

## Slurm

### Simultaneous multithreading (Hyperthreading)

All of our CPUs have this feature, so present two virtual CPUs on each CPU core.
On Mahuika mutithreaded jobs placed a thread on each virtual CPU by default,
with the restriction that different tasks would never share a core, so by default single-threaded MPI jobs were not hyperthreaded while single-task multithreaded jobs were.

On HPC3 we have made `--threads-per-core` default to `1`, i.e: hyperthreading is avoided, equivalent to `--hint=nomultithread`.  To reenable hyperthreading you can set `--threads-per-core=2`, which is equivalent to `--hint=multithread`.

Unlike Mahuika tasks *are* allowed to share a core if `--threads-per-core` is set to `2`.  To avoid that while still hyperthreading within each task of an MPI job, set `--cpus-per-task` to a mutiple of two or also use the slurm option `--tasks-per-core`. 

### Partitions & limits

These have changed.  

As on Mahuika, the default partition selection should generally be OK. There is no need to set `--partition` unless you need the `hugemem` partition or have a specific reason to choose the microarchitecture, in which case you can specify either the `genoa' or `milan` partition. 

Nodes with different amounts of RAM do not have their own partitions, except in the special case of `hugemem`. Your jobs will land on appropriately sized nodes automatically based on your CPU to memory ratio.

It helps if you can get your memory use under 2 GB/core, since in addition to the Milan nodes (when they are transferred) there are amongst the new Genoa nodes:

  - 44 nodes with 2 GB/core, which are available to jobs using up to 2 GB/core.
  -  4 nodes with 4 GB/core, which are available to jobs using up to 4 GB/core.
  - 16 nodes with 8 GB/core (1.5 TB per node) which are available to jobs using more than 2 GB/core.


### Prioritisation

Jobs with a high count of cores-per-node get a priority boost (visible in the “site factor” of `sprio`).  This is to help whole-node jobs get ahead of large distributed jobs with many tasks spread over many nodes.

There is a per-user limit on the job submit rate which will slow down workflow engines which submit too many jobs.  There are usually solutions to this such as array jobs or Snakemake's “groups” feature.

### Miscellaneous

KillOnBadExit is set true, so if one task in an MPI job fails, by default the whole job will be killed.

Each job gets is own `/tmp` & `/dev/shm`  (via Slurm's job_container/tmpfs plugin) so does not need to bother with `$TMPDIR`.

The batch scripts of recent jobs can be rediscovered with `sacct -B -j <jobid>`.  However because those are now being stored, batch script sizes are limited to 64 kB, down from 4 MB.  If that is a problem for your workflow we can probably help turn it into something shorter with appropriate use of loops.

## Hardware

Node sizes are different, so multithreaded jobs will probably have different optimal sizing.  

### Milan nodes

These are the same nodes as made up the Mahuika Extansion. Each Milan node has two AMD Milan 7713 CPUs, each with 4 “I/O quadrants” of 2 "chiplets" of 8 cores and one level 3 cache, so each node has a total of 128 cores or 256 hyperthreaded CPUs.

The memory available to Slurm jobs on most of the Milan nodes is 512 GB per node, so approximately 2 GB per CPU.
There are 64 of these nodes available, 8 of which will have twice as much memory, so 1 TB.

### Genoa nodes

These nodes are new. Each Genoa node has two AMD Genoa 9634 CPUs, each with 12 "chiplets" of 7 cores and one level 3 cache, so each node has a total of 168 cores or 336 hyperthreaded CPUs.

The memory available to Slurm jobs on most of the Genoa nodes is 358 GB per node, so approximately 1 GB per CPU. 
There are 64 of these nodes available, 16 of which have 4 times as much memory, so 1.5 TB.

### GPUs

The P100s are being retired.  The A100s will be moved into HPC3 along with the Milan nodes. 8 H100s and 16 L4s are available on various Genoa nodes.
