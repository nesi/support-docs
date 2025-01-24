---
created_at: '2025-01-24T13:20:00Z'
tags: []
title: Run an executable under Apptainer on GPU
---

This article describes how to run an applicatiopn that was compiled in an [Apptainer](https://apptainer.org/) environment on a GPU.

## Example application

We'll use the fidibench set of benchmarks to illustrate the process
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
```
The application (`upwindAccCxx`) contains OpenACC directives to offload to a GPU.

## Run the application

```sh
srun --gpus-per-node=A100-1g.5gb:1 apptainer exec --nv /nesi/nobackup/pletzera/ngarch_nvhpc.sif ./upwindAccCxx
```
should print 
```
number of cells:  128 128 128
number of time steps: 10
check sum: 1
```

