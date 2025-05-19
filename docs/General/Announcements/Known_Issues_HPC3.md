---
created_at: 2025-04-28
description: List of features currently missing from HPC3.
tags: 
    - hpc3
    - refresh
---

Known issues in HPC3 - the hope is to have these resolved by the end of May or as soon as possible. This is intended to be a temporary page.

See also the more permanent [differences from Mahuika](../../General/FAQs/Mahuika_HPC3_Differences.md).


!!!Recently fixed
     - The low stack size limit of 8kB has been fixed with an increase in `ulimits`
     - The `--ntasks` option no longer defaults to 1 when it shouldn't
     - The `nn_` commands are available. eg `nn_seff <jobid>`.
     - Snapshots are available.


## Login
Currently, when logging into HPC3 using a proxy you will be prompted for authentication twice.

Mobaxterm - configuration may not be possible currently due to name lengths. ssh through a terminal will still be possible.  

## Login nodes
The initial login nodes are smaller than the Mahuika ones, have slower disk I/O, and may not yet have per-user CPU and memory limits.

## OnDemand (including Jupyter)
The resources dedicated to interactive work via a web browser are smaller, and so computations requiring large amounts of memory or many CPU cores are not yet supported. 

Slurm jobs can be only submitted from the `Clusters > NeSI HPC SHell Access` dropdown menu which opens a standard terminal window in the browser

## Globus
There are currently no endpoints configured, workflows that make use of Globus will not work yet.

## Filesystem Snapshots
Snapshots are happening (eg: `ls /home/.snapshots/`) but we don't yet have the convenience of symlinks to them from inside a `$HOME/.snapshots` directory.

## Slurm configuration
Slurm settings may change without notice during the first couple of weeks, including the limits on job sizes, memory, cpus and nodes you can use along with the default for `--threads-per-core`, ie: hyperthreading. The maximum job time limit will stay at 7 days until approximately Monday 26th May.

## Compute nodes
So far there are only the new Genoa and two of the Milan nodes present (the rest are still in Mahuika, or in transit). There are no hugemem nodes yet either, but the largest of the Genoa nodes do have 1.5 TB of memory.

## GPUs
No A100 GPUs have been moved yet, so only the new H100 and L4 GPUs are available. To specify the GPU type, use `#SBATCH --gpus-per-node=H100:1` (or L4:1)

## Node-local SSD access
Our custom Slurm option `--gres=ssd` does not yet work.

## Software
**MATLAB**, **ANSYS**, **ABAQUS**, and **COMSOL** make use of external license servers, so won't work until we are using the above stable IP address for internet access from compute nodes and institutional IT department firewall rules have been updated to match.

**Cylc** has not been installed. You can use [these instructions](https://cylc.github.io/cylc-doc/stable/html/installation.html) to install it.

**QChem** and any other software using node locked licences won't work on nodes which are not yet registered with that license.

**Delft3D_FM** wasn't working in Mahuika's milan partition so probably needs rebuilding.

As was already the case on the Milan nodes in Mahuika (where they had a Rocky 8 OS), some of our environment modules cause system software to stop working, e.g: load `module load Perl` and `svn` stops working. This is usually the case if they load `LegacySystem/7` as a dependency. The solutions are to ask us to re-build the problem environment module, or just don't have it loaded while doing other things.

**MPI** software using 2020 or earlier toolchains eg intel-2020a, may not work correctly across nodes. Trying with more recent toolchains is recommended eg intel-2022a. Please let us known if you find any problems.

## email
Slurm options `--mail-type` is not yet effective.

## Internet
As at 7th May Internet connectivity from compute nodes is available but may change and should not be relied upon. Downloads can be done from login nodes as normal.

## ssh into Slurm jobs
You cannot yet `ssh` into compute nodes, even if you are running jobs there.  That will break any software which depends on ssh to reach remote compute nodes.

## Slurm native profiling
The Slurm option `--profile` will generate profile data, but that data is as yet only visible to NeSI staff.

## WEKA Filesystems 
The Filesystems on HPC3 are not yet as fast as they will be
