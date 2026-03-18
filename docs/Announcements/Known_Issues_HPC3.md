---
created_at: 2025-04-28
description: List of features currently missing from Mahuika (HPC3).
tags: 
    - hpc3
    - refresh
    - mahuika
---

Below is a list issues that we're actively working on. We hope to have these resolved soon. This is intended to be a temporary page.

For differences between the new platforms and Mahuika, see the more permanent [differences from Mahuika](../Getting_Started/FAQs/Mahuika_HPC3_Differences.md).


## OnDemand Apps
* Firefox Browser will fail to render the _HPC Shell Access_ app correctly.  Please switch to a Chrome or Safari browser until the vendor provides a fix.

* The resources dedicated to interactive work via a web browser are smaller, and so computations requiring large amounts of memory or many CPU cores are not yet supported. 

* Missing user Namespaces in Kubernetes pods will interfere with most Apptainer operations.  One can run `apptainer pull` command, `apptainer exec,run,shell` commands can not be executed.

## UCX ERROR
Multi-node MPI jobs may fail on the four nodes mg[13-16] with errors like `UCX ERROR: no active messages transport`. If you encounter this, add the sbatch option `-x mg[13-16]` to avoid those nodes. Single-task jobs are not affected.

## Core dump files
Contrary to what our documentation says, these are not currently available.

## Slurm

### Requesting GPUs
If you request a GPU without specifying which *type* of GPU, you will get a random one. So please always specify a GPU type. 

### BadConstraints
This uninformative message can appear in the `squeue` output as the reason for a job pending. It does not always reflect a real problem though, just a side-effect of the mechanism we are using to target jobs to the right-sized node(s) together with a small bug in Slurm. If it causes your job to be put on hold (ie: its priority gets appears as zero in output from `squeue --me  -S -p  --Format=jobid:10,partition:13,reason:22,numnodes:.6,prioritylong:.6`) then please try `scontrol release <jobid>` or {% include "partials/support_request.html" %} if the issue persists.
