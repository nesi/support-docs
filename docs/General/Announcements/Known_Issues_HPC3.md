---
created_at: 2025-04-28
description: List of features currently missing from HPC3.
tags: 
    - hpc3
    - refresh
---

!!! warning "EARLY ACCESS ONLY"
    This is only relevant to those with early access to HPC3.

What's not working yet

## pam_slurm_adopt

You cannot `ssh` to compute nodes, even if you are running jobs there.  That will break any software which depends on ssh to reach remote compute nodes, e.g: ORCA, some versions of PEST.

## Filesystem Snapshots

You will not be able to recover any deleted files.

## Nodes

So far there are only 2 Milan nodes present (the rest are still in Mahuika, or in transit), along with all the new Genoa nodes.  There are no hugemem nodes either, but the largest of the Genoa nodes do have 1.5 TB of memory.

## GPUs

No A100 GPUs have been moved yet, so only H100 and L4 GPUs are available.

## Node-local SSD access

Our custom Slurm option `--gres=ssd` does not yet work.

## Slurm native profiling

The Slurm option `--profile` will run, but the profiles generated are only visible to NeSI staff.

## Cylc workflow engine

Cylc has not been installed. You can use [these instructions](https://cylc.github.io/cylc-doc/stable/html/installation.html) to install cylc.

## Internet

You will not be able to connect to the internet from compute node. In particular that will affect software which uses an externally hosted license server, such as MATLAB and ANSYS.
In addition functions such as `wget` and `curl` or access to external databases such as NCBI won't work.

## email

Slurm options `--mail-type` is not yet effective.

## Software

- Any software using node locked licences (QChem).
- Any software using an external licence server,  (MATLAB, ANSYS, ABAQUS, COMSOL).
- Some software will need to be recompiled (Delft3D_FM).

