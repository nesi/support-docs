---
created_at: '2020-04-19T22:59:58Z'
tags:
- gpu
title: GPU use on NeSI
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001471955
zendesk_section_id: 360000030876
---

This page provides generic information about how to access NeSI's GPU
cards.

For application specific settings (e.g. OpenMP, Tensorflow on GPU, ...),
please have a look at the dedicated pages listed at the end of this
page.

!!! warning
     An overview of available GPU cards is available in the [Available GPUs on NeSI](../../Scientific_Computing/The_NeSI_High_Performance_Computers/Available_GPUs_on_NeSI.md)
     support page.
     Details about GPU cards for each system and usage limits are in the
     [Mahuika Slurm Partitions](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Mahuika_Slurm_Partitions.md)
     and [Māui\_Ancil (CS500) Slurm Partitions](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Maui_Slurm_Partitions.md#_Toc514341606)
     support pages.
     Details about pricing in terms of compute units can be found in the
     [What is an allocation?](../../Getting_Started/Accounts-Projects_and_Allocations/What_is_an_allocation.md)
     page.

## Request GPU resources using Slurm

To request a GPU for your [Slurm job](../../Getting_Started/Next_Steps/Submitting_your_first_job.md), add
the following option at the beginning of your submission script:

```sl
#SBATCH --gpus-per-node=1
```

You can specify the type and number of GPU you need using the following
syntax

``` sl
#SBATCH --gpus-per-node=<gpu_type>:<gpu_number>
```

If not specified, the default GPU type is `P100`. For some types of GPU,
you also need to specify a partition. Here is a summary of typical use
cases:

- 1 P100 GPU on Mahuika

    ``` sl
    #SBATCH --gpus-per-node=P100:1
    ```

- 1 P100 GPU on Māui Ancillary Nodes

    ``` sl
    #SBATCH --partition=nesi_gpu
    #SBATCH --gpus-per-node=1
    ```

- 2 P100 GPUs per node on Mahuika

    ``` sl
    #SBATCH --gpus-per-node=P100:2
    ```

    *You cannot ask for more than 2 P100 GPU per node on Mahuika.*

- 1 A100 (40GB) GPU on Mahuika

    ``` sl
    #SBATCH --gpus-per-node=A100:1
    ```

- 2 A100 (40GB) GPUs on Mahuika

    ``` sl
    #SBATCH --gpus-per-node=A100:2
    ```

    *You cannot ask for more than 2 A100 (40GB) GPUs per node on
    Mahuika.*

- 1 A100-1g.5gb GPU on Mahuika

    ``` sl
    #SBATCH --gpus-per-node=A100-1g.5gb:1
    ```

    *This type of GPU is limited to 1 job per user and recommended for
    development and debugging.*

- 1 A100 (80GB) GPU on Mahuika

    ``` sl
    #SBATCH --partition=hgx
    #SBATCH --gpus-per-node=A100:1
    ```

    *These GPUs are on Milan nodes, check the [dedicated support
    page](https://support.nesi.org.nz/knowledge/articles/6367209795471/)
    for more information.*

- 4 A100 (80GB & NVLink) GPU on Mahuika

    ``` sl
    #SBATCH --partition=hgx
    #SBATCH --gpus-per-node=A100:4
    ```

    *These GPUs are on Milan nodes, check the [dedicated support
    page](https://support.nesi.org.nz/knowledge/articles/6367209795471/)
    for more information.*

    *You cannot ask for more than 4 A100 (80GB) GPUs per node on
    Mahuika.*

- 1 A100 GPU on Mahuika, regardless of the type

    ``` sl
    #SBATCH --partition=gpu,hgx
    #SBATCH --gpus-per-node=A100:1
    ```

    *With this configuration, your job will spend less time in the
    queue, using whichever A100 GPU is available. It may land on a
    regular Mahuika node (A100 40GB GPU) or on a Milan node (A100 80GB
    GPU).*

You can also use the `--gpus-per-node`option in [Slurm interactive sessions](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Slurm_Interactive_Sessions.md),
with the `srun` and `salloc` commands. For example:

``` sh
srun --job-name "InteractiveGPU" --gpus-per-node 1 --cpus-per-task 8 --mem 2GB --time 00:30:00 --pty bash
```

will request and then start a bash session with access to a GPU, for a
duration of 30 minutes.

!!! warning
     When you use the `--gpus-per-node`option, Slurm automatically sets the
     `CUDA_VISIBLE_DEVICES` environment variable inside your job
     environment to list the index/es of the allocated GPU card/s on each
     node.

     ``` sh
     srun --job-name "GPUTest" --gpus-per-node=P100:2 --time 00:05:00 --pty bash
     ```
     
     ```out
     srun: job 20015016 queued and waiting for resources
     srun: job 20015016 has been allocated resources
     $ echo $CUDA_VISIBLE_DEVICES
     0,1
     ```

## Load CUDA and cuDNN modules

To use an Nvidia GPU card with your application, you need to load the
driver and the CUDA toolkit via the [environment
modules](../../Getting_Started/Next_Steps/The_HPC_environment.md)
mechanism:

``` sh
module load CUDA/11.0.2
```

You can list the available versions using:

``` sh
module spider CUDA
```

Please{% include "partials/support_request.html" %} if you need a version not
available on the platform.

!!! note
     On Māui Ancillary Nodes, use `module avail CUDA` to list available
     versions.

The CUDA module also provides access to additional command line tools:

- [nvidia-smi](https://developer.nvidia.com/nvidia-system-management-interface)
            to directly monitor GPU resource utilisation,
- [nvcc](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html)
            to compile CUDA programs,
- [cuda-gdb](https://docs.nvidia.com/cuda/cuda-gdb/index.html)
            to debug CUDA applications.

In addition, the [cuDNN](https://developer.nvidia.com/cudnn) (NVIDIA
CUDA® Deep Neural Network library) library is accessible via its
dedicated module:

``` sh
module load cuDNN/8.0.2.39-CUDA-11.0.2
```

which will automatically load the related CUDA version. Available
versions can be listed using:

``` sh
module spider cuDNN
```

## Example Slurm script

The following Slurm script illustrates a minimal example to request a
GPU card, load the CUDA toolkit and query some information about the
GPU:

``` sl
#!/bin/bash -e
#SBATCH --job-name=GPUJob   # job name (shows up in the queue)
#SBATCH --time=00-00:10:00  # Walltime (DD-HH:MM:SS)
#SBATCH --gpus-per-node=1   # GPU resources required per node
#SBATCH --cpus-per-task=2   # number of CPUs per task (1 by default)
#SBATCH --mem=512MB         # amount of memory per node (1 by default)

# load CUDA module
module purge
module load CUDA/11.0.2

# display information about the available GPUs
nvidia-smi

# check the value of the CUDA_VISIBLE_DEVICES variable
echo "CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES}"
```

Save this in a `test_gpu.sl` file and submit it using:

``` sl
sbatch test_gpu.sl
```

The content of job output file would look like:

``` sl
$ cat slurm-20016124.out

The following modules were not unloaded:
   (Use "module --force purge" to unload all):

  1) slurm   2) NeSI
Wed May 12 12:08:27 2021
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.32.03    Driver Version: 460.32.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  On   | 00000000:05:00.0 Off |                    0 |
| N/A   29C    P0    23W / 250W |      0MiB / 12198MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
CUDA_VISIBLE_DEVICES=0
```

!!! note
    `CUDA_VISIBLE_DEVICES=0` indicates that this job was allocated to CUDA
     GPU index 0 on this node. It is not a count of allocated GPUs.

## NVIDIA Nsight Systems and Compute profilers

[Nsight Systems](https://developer.nvidia.com/nsight-systems) is a
system-wide analysis tool, particularly good for profiling CPU-GPU
interactions. It is provided on Mahuika via the `Nsight-Systems` module:

``` sh
module load Nsight-Systems/2020.5.1
```

```out
Load `PyQt/5.12.1-gimkl-2020a-Python-3.8.2` module prior to running `nsys-ui`
```

```sh
nsys --version
```

```out
NVIDIA Nsight Systems version 2020.5.1.85-5ee086b
```

This module gives you access to the
[nsys](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#cli-profiling)
command line tool or the
[nsys-ui](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#gui-profiling)
graphical interface.

[Nsight Compute](https://developer.nvidia.com/nsight-compute) is a
profiler for CUDA kernels. It is accessible on Mahuika using the
`Nsight-Compute` module:

``` sh
module load Nsight-Compute/2020.3.0
```

```out
Load `PyQt/5.12.1-gimkl-2020a-Python-3.8.2` module prior to running `nsys-ui`
```

```sh
ncu --version
```

```out
NVIDIA (R) Nsight Compute Command Line Profiler
Copyright (c) 2018-2020 NVIDIA Corporation
Version 2020.3.0.0 (build 29307467) (public-release)
```

Then you can use the
[ncu](https://docs.nvidia.com/nsight-compute/NsightComputeCli/) command
line tool or the
[ncu-ui](https://docs.nvidia.com/nsight-compute/NsightCompute/index.html)
graphical interface.

!!! warning
     The `nsys-ui` and `ncu-ui` tools require access to a display server,
     either via
     [X11](../../Scientific_Computing/Terminal_Setup/X11_on_NeSI.md) or a
     [Virtual Desktop](../../Scientific_Computing/Interactive_computing_using_Jupyter/Virtual_Desktop_via_Jupyter_on_NeSI.md).
     You also need to load the `PyQt` module beforehand:

     ```sh
     module load PyQt/5.12.1-gimkl-2020a-Python-3.8.2
     module load Nsight-Systems/2020.5.1
     nsys-ui  # this will work only if you have a graphical session
     ```

## Application and toolbox specific support pages

The following pages provide additional information for supported
applications:

- [ABAQUS](../../Scientific_Computing/Supported_Applications/ABAQUS.md#gpus)
- [GROMACS](../../Scientific_Computing/Supported_Applications/GROMACS.md#nvidia_gpu_container)
- [Lambda Stack](../../Scientific_Computing/Supported_Applications/Lambda Stack.md)
- [Matlab](../../Scientific_Computing/Supported_Applications/MATLAB.md#GPU)
- [TensorFlow on GPUs](../../Scientific_Computing/Supported_Applications/TensorFlow_on_GPUs.md)

And programming toolkits:

- [Offloading to GPU with OpenMP](../../Scientific_Computing/HPC_Software_Environment/Offloading_to_GPU_with_OpenMP.md)
- [Offloading to GPU with OpenACC using the Cray compiler](https://support.nesi.org.nz/hc/en-gb/articles/360001131076-Offloading-to-GPU-with-OpenACC-using-the-Cray-compiler)
- [NVIDIA GPU Containers](../../Scientific_Computing/HPC_Software_Environment/NVIDIA_GPU_Containers.md)
