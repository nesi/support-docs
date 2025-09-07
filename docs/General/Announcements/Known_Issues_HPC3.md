---
created_at: 2025-04-28
description: List of features currently missing from HPC3.
tags: 
    - hpc3
    - refresh
---

Below is a list issues that we're actively working on. We hope to have these resolved soon. This is intended to be a temporary page.

For differences between the new platforms and Mahuika, see the more permanent [differences from Mahuika](../../General/FAQs/Mahuika_HPC3_Differences.md).


!!! info "Recently fixed"
     - New login node "login03" fixes previous performance problems.
     - The Milan compute nodes are now available, including the 4 nodes with the 80GB A100 GPUs.
     - MaxRSS is now the same number as it was on the old cluster - just the ordinary (ie: "anon") memory use without caches etc.

## Access

### OnDemand (including Jupyter)
The resources dedicated to interactive work via a web browser are smaller, and so computations requiring large amounts of memory or many CPU cores are not yet supported. 

Slurm jobs can be submitted, but only from the `Clusters > NeSI HPC SHell Access` dropdown menu which opens a standard terminal window in the browser. [Watch a demo here](https://youtu.be/bkq6tpRrAwc?si=kS2KBifnCf4d6tWz).

### Login via ssh

#### Authentication
Currently, when logging into the new platform using a proxy you will be prompted for authentication twice, unless you have set up an ssh key.

#### MobaXterm
The session login process of MobaXterm is not compatible with Tuakiri 2-factor authentication.

ssh through a terminal will still be possible with MobaXterm, but it is recommended to use [OnDemand](https://ondemand.nesi.org.nz/) for file browsing, file transfer (for files under 9.8 GB) and terminal access if you would normally have used MobaXterm. [Watch a demo of how to use MobaXterm on the new platform](https://youtu.be/EDBx24Aeel4?si=9uSHdajDG3qBuhUH).

## Software
As was already the case on the Milan nodes in Mahuika (where they had a Rocky 8 OS), some of our environment modules cause system software to stop working, e.g: load `module load Perl` and `svn` stops working. This is usually the case if they load `LegacySystem/7` as a dependency. The solutions are to ask us to re-build the problem environment module, or just don't have it loaded while doing other things.

**QChem** and any other software using node locked licences won't work on nodes which are not yet registered with that license.

**Delft3D_FM** wasn't working in Mahuika's Milan partition so probably needs rebuilding.

**MPI** software using 2020 or earlier toolchains eg intel-2020a, may not work correctly across nodes. Trying with more recent toolchains is recommended eg intel-2022a. 

Please let us know if you find any additional problems.

## Slurm

### Compute nodes
None of the 3 Mahuika hugemem nodes are present yet, but the largest of the new Genoa nodes do have 1.5 TB of memory.

### GPUs
If you request a GPU without specifying which *type* of GPU, you will get a random one. So please always specify a GPU type. 

### $TMPDIR
On some of the Genoa nodes the size limit on this per-job in-memory directory is currently only 70 TB per node in total across all jobs. So if you need to use more than about 5 TB of it per node then please use `--partition=milan` to avoid the Genoa nodes or `--gres=ssd` to get your job's $TMPDIR placed on a fast SSD instead.

### BadConstraints
This uninformative message can appear as a reason for a job pending in the `squeue` output when the job is submitted to both `milan` and `genoa` partitions (which is the default behaviour). It does not appear to reflect a real problem though, just a side-effect of the mechanism we are using to target jobs to the right-sized node(s). 

### email
Slurm option `--mail-type` is not yet effective.

### ssh into Slurm jobs
You cannot yet `ssh` into some of the the Genoa compute nodes, even if you are running jobs there.  That will break any software which depends on ssh to reach remote compute nodes.

## WEKA Filesystems 
From some of the Genoa compute nodes, the cluster-wide filesystems (_/home_, _/nesi/project_, _/nesi/nobackup_, and _/opt/nesi_) are not yet as fast as they should be.

## Freezer Filesystems
If you have a large number files the `s3cmd du`command will fail. If you wish to receive information from `s3cmd du` we advise using a compression command such as `tar` to reduce the total number of files before adding them to Freezer.
