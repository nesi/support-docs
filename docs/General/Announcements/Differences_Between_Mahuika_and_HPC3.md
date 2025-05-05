---
created_at: 2025-05-05
description: What to expect when moving to HPC3. 
tags: 
    - refresh
    - hpc3
---

{% include "partials/hpc3_disclaimer.html" %}

# Preface 

This article presents an overview comparison of the differences between the NeSI Mahuika platforms and the new HPC3 (needs name) that Researchers have used in various capacities. It is not a comprehensive view of the differences and where appropriate individual support pages will be update to reflect changes and enhancements. For example the [Slurm Reference](https://docs.nesi.org.nz/Getting_Started/Cheat_Sheets/Slurm-Reference_Sheet/) Sheet will have a number of changes made to it along with significant changes to the [Slurm Partitions](https://docs.nesi.org.nz/Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Mahuika_Slurm_Partitions/). 

This page should be read in conjunction with the [Known Issues](https://docs.nesi.org.nz/General/Announcements/Known_Issues_HPC3/) which are not represented here as they are to be implemented/fixed.

Maui is being decommissioned so is not presented here. If you require help with transferring your code please email support@nesi.org.nz . There is additional information pertaining to Maui at [Preparing your code for use on NeSI's new HPC platform](https://docs.nesi.org.nz/General/Announcements/Preparing_your_code_for_use_on_NeSIs_new_HPC_platform/)

# What's Changing

### Login
ssh/2fa/lander
OOD (Open OnDemand) instead of JupyterHub

### Storage
WEKA vs GPFS - describe WEKA theory, ie: files faster to retrieve for the first X days after last access?
Nobackup autodeletion - any changes?
Freezer instead of Nearline

### Partitions
Genoa nodes: size and shape and price. Around 60% faster than Milan.

### Slurm
partitions & limits

job prioritisation - higher priority for whole-node jobs (via 5 points per core-per-node requested)

KillOnBadExit

$TMPDIR & /tmp & /dev/shm - using Slurm’s job_container/tmpfs plugin so jobs can use /tmp and not bother with $TMP_DIR

AccountingStoreFlags - so sacct -B and sacct --env-vars

max_script_size of 64 kB, down from 4 MB (so learn loops, ask support)

rl_enable limiting job submit rate, (so snakemake might need to use its groups feature)

### Lmod
module spider should (might) find extensions too

module sets can be saved/restored
