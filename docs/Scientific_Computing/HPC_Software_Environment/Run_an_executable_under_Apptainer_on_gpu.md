---
created_at: '2025-01-24T13:20:00Z'
tags:
- gpu
- apptainer
- container
description: Instructions on how to run an executable under Apptainer on GPU
---

This article describes how to run an application that was compiled in an [Apptainer](https://apptainer.org/) environment on a GPU.

## Example application

We'll use the fidibench set of benchmarks to illustrate the process. On mahuika,

```sh
git clone https://github.com/pletzer/fidibench
cd fidibench
mkdir build-nv
cd build-nv
```

A container with NVIDIA compilers can be obtained here `/nesi/nobackup/pletzera/ngarch_nvhpc.sif`. To launch the container:

```sh
module purge
module load CUDA/12.6.3 Apptainer/1.2.5
apptainer shell --nv /nesi/nobackup/pletzera/ngarch_nvhpc.sif
```

Note the `--nv` option which exposes the GPU hardware to the container.

We can now build an application using the `nvc++` compiler inside the container:

```sh
Apptainer> CXX=nvc++ cmake -DOPENACC=1 ..
Apptainer> cd upwind/cxx
Apptainer> make upwindAccCxx
Apptainer> exit
```

The application (`upwindAccCxx`) contains OpenACC directives to offload to a GPU.

## Run the application

```sh
srun --gpus-per-node=A100-1g.5gb:1 apptainer exec --nv \
     /nesi/nobackup/pletzera/ngarch_nvhpc.sif ./upwind/cxx/upwindAccCxx
```

should print

```sh
number of cells:  128 128 128
number of time steps: 10
check sum: 1
```
