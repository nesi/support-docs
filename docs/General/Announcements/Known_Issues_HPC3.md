---
created_at: 2025-04-28
description: List of features currently missing from HPC3.
tags: 
    - hpc3
    - refresh
---

Known issues in HPC3 - the hope is to have these resolved by the end of May or as soon as possible. This is intended to be a temporary page.

## Login

Loging in requires authenticating twice.

## OnDemand (including Jupyter)

The resources dedicated to interactive work via a web browser are smaller, and so computations requiring large amounts of memory or many CPU cores are not yet supported. 

Slurm jobs can not yet be submitted from within OnDemand.

## Login Authentication

Currently, when logging into HPC3 using a proxy you will be prompted for authentication twice.

## Filesystem Snapshots

You can not recover any deleted files.

## Login

The initial login nodes are smaller than the Mahuika ones, have slower disk I/O, and may not yet have per-user CPU and memory limits.

Mobaxterm - configuration may not be possible currently due to name lengths. ssh through a terminal will still be possible.  

## Compute Nodes

So far there are only the new Genoa and two of the Milan nodes present (the rest are still in Mahuika, or in transit). There are no hugemem nodes either, but the largest of the Genoa nodes do have 1.5 TB of memory.

## GPUs

No A100 GPUs have been moved yet, so only the new H100 and L4 GPUs are available.

## Internet

As at 7th May Internet connectivity from compute nodes is available but may change and should not be relied upon. Downloads can be done from login nodes as normal.

## Node-local SSD access

Our custom Slurm option `--gres=ssd` does not yet work.

## Software

**MATLAB**, **ANSYS**, **ABAQUS**, and **COMSOL** make use of external license servers, so won't work until we have a stable IP address for internet access from compute nodes and institutional IT department firewall rules have been updated to match it.

**Cylc** has not been installed. You can use [these instructions](https://cylc.github.io/cylc-doc/stable/html/installation.html) to install it.

**QChem** and any other software using node locked licences won't work on nodes which are not yet registered with that license.

**Delft3D_FM** wasn't working in Mahuika's milan partition so probably needs rebuilding.

As was already the case on the Milan nodes in Mahuika (where they had a Rocky 8 OS), some of our environment modules cause system software to stop working, e.g: load `module load Perl` and `svn` stops working. This is usually the case if they load `LegacySystem/7` as a dependency. The solutions are to ask us to re-build the problem environment module, or just don't have it loaded while doing other things.

## Globus

There are currently no endpoints configured, workflows that make use of Globus will not work

## email

Slurm options `--mail-type` is not yet effective.

## ssh into Slurm jobs

You cannot yet `ssh` into compute nodes, even if you are running jobs there.  That will break any software which depends on ssh to reach remote compute nodes.

## Slurm configuration

Slurm settings may change without notice during the first couple of weeks, including the limits on job sizes and the default for `--threads-per-core`, ie: hyperthreading.

## Slurm native profiling

The Slurm option `--profile` will generate profile data, but that data is as yet only visible to NeSI staff.


