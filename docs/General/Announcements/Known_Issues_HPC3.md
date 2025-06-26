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
     - Globus Endpoint added - `NeSI HPC3 Storage`
     - New `profile_plot` command is available, replacing `sh5util`.

## Login
Currently, when logging into the new platform using a proxy you will be prompted for authentication twice.

## MobaXterm
The session login process of MobaXterm is not compatible with Tuakiri 2-factor authentication.

ssh through a terminal will still be possible with MobaXterm, but it is recommended to use [OnDemand](https://ondemand.nesi.org.nz/) for file browsing, file transfer (for files under 9.8 GB) and terminal access if you would normally have used MobaXterm. [Watch a demo of how to use MobaXterm on the new platform](https://youtu.be/EDBx24Aeel4?si=9uSHdajDG3qBuhUH).

## Login nodes
The initial login nodes are smaller than the Mahuika ones, have slower disk I/O, and may not yet have per-user CPU, memory, and `/tmp` disk limits.

## OnDemand (including Jupyter)
The resources dedicated to interactive work via a web browser are smaller, and so computations requiring large amounts of memory or many CPU cores are not yet supported. 

Slurm jobs can be submitted, but only from the `Clusters > NeSI HPC SHell Access` dropdown menu which opens a standard terminal window in the browser. [Watch a demo here](https://youtu.be/bkq6tpRrAwc?si=kS2KBifnCf4d6tWz).

## Compute nodes
So far there are all the new Genoa nodes but **only two** of the Milan nodes present, the rest of those being still in Mahuika, or in transit. So please only use the limited Milan resource for small benchmarking tests.  

None of the 3 Mahuika hugemem nodes are present yet, but the largest of the new Genoa nodes do have 1.5 TB of memory.

## GPUs
No A100 GPUs have been moved yet, so only the new H100 and L4 GPUs are available. To specify the GPU type, use `#SBATCH --gpus-per-node=H100:1` (or `L4:1`)

## Software

[**MATLAB**](../../Scientific_Computing/Supported_Applications/MATLAB.md), [**ANSYS**](../../Scientific_Computing/Supported_Applications/ANSYS.md), [**ABAQUS**](../../Scientific_Computing/Supported_Applications/ABAQUS.md), and [**COMSOL**](../../Scientific_Computing/Supported_Applications/COMSOL.md) make use of external license servers, so won't work until institutional IT department firewall rules have been updated to match out new IP address range.

Check the documentation for the specific software to see if your institution has access, and feel free to contact support if it isn't.


**Cylc** has not been installed. You can use [these instructions](https://cylc.github.io/cylc-doc/stable/html/installation.html) to install it.

**QChem** and any other software using node locked licences won't work on nodes which are not yet registered with that license.

**Delft3D_FM** wasn't working in Mahuika's Milan partition so probably needs rebuilding.

As was already the case on the Milan nodes in Mahuika (where they had a Rocky 8 OS), some of our environment modules cause system software to stop working, e.g: load `module load Perl` and `svn` stops working. This is usually the case if they load `LegacySystem/7` as a dependency. The solutions are to ask us to re-build the problem environment module, or just don't have it loaded while doing other things.

**MPI** software using 2020 or earlier toolchains eg intel-2020a, may not work correctly across nodes. Trying with more recent toolchains is recommended eg intel-2022a. Please let us know if you find any problems.

## email
Slurm option `--mail-type` is not yet effective.

## ssh into Slurm jobs
You cannot yet `ssh` into compute nodes, even if you are running jobs there.  That will break any software which depends on ssh to reach remote compute nodes.

## WEKA Filesystems 
The filesystems on the new platform are not yet as fast as they will be.
