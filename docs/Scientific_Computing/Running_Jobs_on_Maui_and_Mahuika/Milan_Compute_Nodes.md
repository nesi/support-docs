---
created_at: '2023-02-09T01:30:43Z'
hidden: false
position: 10
tags: []
title: Milan Compute Nodes
vote_count: 0
vote_sum: 0
zendesk_article_id: 6367209795471
zendesk_section_id: 360000030876
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

 

## How to access

To use Mahuika's Milan nodes, you will need to explicitly specify the
`milan` partition in your `sbatch` command line. Jobs are submitted from
the same Mahuika login node that you currently use, and share the same
file system as other cluster nodes. 

``` sl
sbatch -p milan ...
```

Alternatively, the same effect can be achieved by placing a pragma into
the job description file:

``` sl
#SBATCH --partition=milan
```

## Hardware

Each node has two AMD Milan CPUs, each with 8 "chiplets" of 8 cores and
one level 3 cache, so each node has a total of **128 cores** or 256
hyperthreaded CPUs. This represents a significant increase of the number
CPUs per node compared to the Broadwell nodes (36 cores). 

The memory available to Slurm jobs is 512GB per node, so approximately
2GB per CPU. There are 64 nodes available, 8 of which will have double
the memory (1T).

## Software

### Operating System

The existing Mahuika compute nodes use Linux Centos 7.4 while the new
ones use Rocky 8.5.  These are closely related Linux distributions. The
move from 7 to 8 is more significant than the move from Centos to Rocky.

Many system libraries have changed version numbers between versions 7
and 8, so **some software compiled on Centos 7 will not run as-is on
Rocky 8**. This can result in the runtime error
`error while loading shared libraries:... cannot open shared object file`, 
which can be fixed by providing a copy of the old system library.  

We have repaired several of our existing environment modules that way.
For programs which you have compiled yourself, we have installed a new
environment module that provides many of the Centos 7 libraries:

``` sl
module load LegacySystemLibs/7
```

Please [let us know](https://support.nesi.org.nz/hc/en-gb/requests/new)
if that isn't sufficient to get your existing compiled code running on
the new nodes.

Of course you can also recompile code inside a job run in the Milan
partition and so produce an executable linked against the new system
libraries, but then that would be unlikely to work on the old nodes.

In the longer term, all Mahuika nodes will be upgraded to Rocky 8.

### Older Intel and Cray software

The directories `/cm` and `/opt/cray` contain software which was
installed on Mahuika's Broadwell nodes when we purchased it rather than
installed by the NeSI Application Support team. They are not present on
the Milan nodes. As with the system libraries, you could take a copy of
these libraries and carry on, but it is best to migrate away from using
them if possible.

This affects our pre-2020 toolchains such as *intel/2018b*, but we
should have newer versions of such software already installed in most
cases.

### Intel MKL performance

In many ways, Intel's MKL is the best implementation of the BLAS and
LAPACK libraries to which we have access, which is why we use it in our
"*intel*" and "*gimkl*" toolchains.  Unfortunately, recent versions of
MKL deliberately choose not to use the accelerated AVX instructions when
not running on an Intel CPU.  

In order to persuade MKL to use the same fast optimised kernels on the
new AMD Milan CPUs, you can do:

``` sl
module load AlwaysIntelMKL
```

We have set that as the default for our most recent toolchain
*gimkl/2022a*.

Two alternative implementations have also been installed: OpenBLAS and
BLIS. If you try them then please let us know if they work better than
MKL for your application. BLIS is expected to perform well as a BLAS
alternative but not match MKL's LAPACK performance.  

### Do I need to recompile my code?

Except for possible missing shared libraries (see above), you should not
need to recompile your code. Please [let us
know](https://support.nesi.org.nz/hc/en-gb/requests/new) if you
encounter any issues not listed above.

### AOCC compiler suite

AMD provides a compiler based on clang (C/C++) and flang (Fortran) which
might perform better on their hardware. We have installed it but not
integrated it into a high-level toolchain with MPI and BLAS. If you wish
to try it:

``` sl
module load AOCC
```

For more information on AOCC compiler suite please, visit [AMD
Optimizing C/C++ and Fortran Compilers
(AOCC)](https://developer.amd.com/amd-aocc/)

## Network

Access to Mahuika's Milan nodes is currently only possible via the Slurm
`sbatch` and `srun` commands. There is no ssh access, not even to the
nodes where you have a job running. Programs that launch their remote
tasks via ssh (eg: ORCA) are not expected to work. Other arbitrary
connections to the new compute nodes such as might be used by debuggers,
HTTP based progress monitoring, and non-MPI distributed programs such as
Dask or PEST, will generally only work if you use the Infiniband address
of the compute node, eg: *wmc012.ib.hpcf.nesi.org.nz*. This networking
configuration is expected to be addressed in the future.

## Any questions?

Don't hesitate to contact us at <support@nesi.org.nz>. No question is
too big or small. We are available for Zoom sessions or [Weekly Online
Office
Hours](../../../Getting_Started/Getting_Help/Weekly_Online_Office_Hours)
if it's easier to discuss your question in a call rather than via email.