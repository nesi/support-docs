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

You cannot SSH to compute nodes, even if you are running jobs.

## snapshots

You will not be able to recover deleted files.

## Nodes

The current nodes are not accessible.

    milan nodes (wmc[005-014,017-060],wml[061-068])
    hugemem nodes (wbh001,wch001,wcl[001-002])


    the Slurm option `--gres=ssd` will not work.

## Slurm native profiling

The Slurm option `--profile` will not work.

## Internet

You will not be able to connect to the internet.

## email

## Software

- Delft3D_FM
- Ans software using node locked licences (QChem).
- Any software using an external licence server,  (MATLAB, ANSYS, ABAQUS, COMSOL).
