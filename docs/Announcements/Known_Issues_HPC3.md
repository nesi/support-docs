---
created_at: 2025-04-28
description: List of features currently missing from HPC3.
tags: 
    - hpc3
    - refresh
---

Below is a list issues that we're actively working on. We hope to have these resolved soon. This is intended to be a temporary page.

For differences between the new platforms and Mahuika, see the more permanent [differences from Mahuika](../Getting_Started/FAQs/Mahuika_HPC3_Differences.md).


!!! info "Recently fixed"
     - Emails can now be sent by Slurm when you set `--mail-user`.

## Access

### OnDemand (including Jupyter)
The resources dedicated to interactive work via a web browser are smaller, and so computations requiring large amounts of memory or many CPU cores are not yet supported. 

Slurm jobs can be submitted, but only from the `Clusters > NeSI HPC SHell Access` dropdown menu which opens a standard terminal window in the browser. [Watch a demo here](https://youtu.be/bkq6tpRrAwc?si=kS2KBifnCf4d6tWz).

## Software
As was already the case on the Milan nodes in Mahuika (where they had a Rocky 8 OS), some of our environment modules cause system software to stop working, e.g: load `module load Perl` and `svn` stops working. This is usually the case if they load `LegacySystem/7` as a dependency. The solutions are to ask us to re-build the problem environment module, or just don't have it loaded while doing other things.

**Delft3D_FM** wasn't working in Mahuika's Milan partition so probably needs rebuilding.

**MPI** software using 2020 or earlier toolchains eg intel-2020a, may not work correctly across nodes. Trying with more recent toolchains is recommended eg intel-2022a. 

Please let us know if you find any additional problems.

## Slurm

### GPUs
If you request a GPU without specifying which *type* of GPU, you will get a random one. So please always specify a GPU type. 

### BadConstraints
This uninformative message can appear as a reason for a job pending in the `squeue` output when the job is submitted to both `milan` and `genoa` partitions (which is the default behaviour). It does not appear to reflect a real problem though, just a side-effect of the mechanism we are using to target jobs to the right-sized node(s). 

