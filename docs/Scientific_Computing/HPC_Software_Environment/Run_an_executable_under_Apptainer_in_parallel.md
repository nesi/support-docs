---
created_at: '2024-01-15T13:20:00Z'
tags:
- apptainer
- container
- mpi
description: Instructions on how to run an executable under Apptainer in parallel
---

This article describes how to run an [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) program that was compiled in an [Apptainer](https://apptainer.org/) environment in parallel, using the host MPI library. While an Apptainer environment encapsulates the dependencies of an application, including MPI, it is often beneficial, to delegate the MPI calls within the container to the host to achieve best performance.

In general, the MPI version inside and outside of the container need to match. How to convince an application to use the host MPI depends on the MPI library and the level of integration with SLURM. Here we
show how to channel the MPI calls of a containerised application built with Intel MPI to the host. We'll use the [fidibench](https://github.com/pletzer/fidibench) application as an example.

## Intel MPI

The definition file can be fetched from

```sh
wget https://raw.githubusercontent.com/pletzer/fidibench/refs/heads/master/fidibench_intel.def
```

You can build the container on most Linux platform with Apptainer installed

```sh
apptainer build --force fidibench_intel.aif fidibench_intel.def
```

Test that the container is working with the command

```sh
apptainer exec fidibench_intel.aif mpiexec -n 4 /software/fidibench/bin/upwindMpiCxx
Number of procs: 4
global dimensions: 128 128 128
...
Check sum: 1
```

So far we used the (Intel) MPI library inside the container.

To use the host MPI, create a SLURM script `fidibench_intel.sl` containing

```sh
#!/bin/bash -e
#SBATCH --job-name=fidibench                                                          
#SBATCH --time 00:05:00                                                                                                       
#SBATCH --ntasks=8                                                                        
#SBATCH --nodes=2                                                                                               
module purge
export I_MPI_ROOT=/opt/nesi/CS400_centos7_bdw/impi/2021.5.1-intel-compilers-2022.0.2/mpi/2021.5.1
export PATH=$I_MPI_ROOT/bin:$PATH
export LD_LIBRARY_PATH=$I_MPI_ROOT/lib:$LD_LIBRARY_PATH
mpiexec -n ${SLURM_NTASKS} --bind-to none --map-by slot \
        apptainer exec --bind $I_MPI_ROOT:$I_MPI_ROOT fidibench_intel.aif \
        /software/fidibench/bin/upwindMpiCxx
```

and submit the script with

```sh
sbatch fidibench_intel.sl
```
