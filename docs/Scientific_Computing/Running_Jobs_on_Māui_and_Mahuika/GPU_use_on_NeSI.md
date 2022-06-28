This page provides generic information about how to access NeSI\'s GPU
cards.

For application specific settings (e.g. OpenMP, Tensorflow on GPU,
\...), please have a look at the dedicated pages listed at the end of
this page.

> ### Important {#prerequisites}
>
> An overview of available GPU cards is available in the [Available GPUs
> on NeSI](https://support.nesi.org.nz/hc/en-gb/articles/4963040656783)
> support page.
>
> Details about[ ]{.diff-removed-string}GPU cards for each system[
> ]{.diff-removed-string}and [usage]{.diff-added-string} limits are in
> the [Mahuika Slurm
> Partitions](https://support.nesi.org.nz/hc/en-gb/articles/360000204076)
> and [Māui\_Ancil (CS500) Slurm
> Partitions](https://support.nesi.org.nz/hc/en-gb/articles/360000204116#_Toc514341606)
> support pages.
>
> Details about pricing in terms of compute units can be found in the
> [What is an
> allocation?](https://support.nesi.org.nz/hc/en-gb/articles/360001385735)
> page.

Request GPU resources using Slurm
=================================

To request a GPU for your [Slurm
job](https://support.nesi.org.nz/hc/en-gb/articles/360000684396-Submitting-your-first-job),
add the following option at the beginning of your submission script:

    #SBATCH --gpus-per-node=1

You can specify the type of GPU you need, depending on which ones you
have access to with your allocation. If you wish to use the A100 GPUs
please [contact our support
team](https://support.nesi.org.nz/hc/requests/new) to learn more about
getting access to the A100 GPU cards.

For example, to access a P100 card, use the following option:

    #SBATCH --gpus-per-node=P100:1

On Mahuika, you can request 2 GPUs per node using:

    #SBATCH --gpus-per-node=P100:2

Conversely, to request A100 GPU devices, do this:

-   To use one A100:

        #SBATCH --gpus-per-node=A100:1

-   To use two A100s:

        #SBATCH --gpus-per-node=A100:2

To access an A100-1g.5gb GPU, use:

    #SBATCH --gpus-per-node=A100-1g.5gb:1

If not specified, the default GPU type is *P100*.

You can also use the `--gpus-per-node`option in [Slurm interactive
sessions](https://support.nesi.org.nz/hc/en-gb/articles/360001316356),
with the `srun` and `salloc` commands. For example:

    srun --job-name "InteractiveGPU" --gpus-per-node 1 --cpus-per-task 8 --mem 2GB --time 00:30:00 --pty bash

will request and then start a bash session with access to a GPU, for a
duration of 30 minutes.

> ### Important {#prerequisites}
>
> When you use the `--gpus-per-node`option, Slurm automatically sets the
> `CUDA_VISIBLE_DEVICES` environment variable inside your job
> environment to list the index/es of the allocated GPU card/s on each
> node.
>
>     $ srun --job-name "GPUTest" --gpus-per-node=P100:2 --time 00:05:00 --pty bash
>     srun: job 20015016 queued and waiting for resources
>     srun: job 20015016 has been allocated resources
>     $ echo $CUDA_VISIBLE_DEVICES
>     0,1

> ### Note {#prerequisites}
>
> On Māui Ancillary Nodes, you also need to request the *nesi\_gpu*
> partition to have access to the GPU.
>
>     #SBATCH --partition=nesi_gpu

Load CUDA and cuDNN modules
===========================

To use an Nvidia GPU card with your application, you need to load the
driver and the CUDA toolkit via the [environment
modules](https://support.nesi.org.nz/hc/en-gb/articles/360001113076-The-HPC-environment-)
mechanism:

    module load CUDA/11.0.2

You can list the available versions using:

    module spider CUDA

Please contact us at <support@nesi.org.nz> if you need a version not
available on the platform.

> ### Note {#prerequisites}
>
> On Māui Ancillary Nodes, use `module avail CUDA` to list available
> versions.

The CUDA module also provides access to additional command line tools:

-   [**nvidia-smi**](https://developer.nvidia.com/nvidia-system-management-interface)
    to directly monitor GPU resource utilisation,
-   [**nvcc**](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html)to
    compile CUDA programs,
-   [**cuda-gdb**](https://docs.nvidia.com/cuda/cuda-gdb/index.html) to
    debug CUDA applications.

In addition, the [cuDNN](https://developer.nvidia.com/cudnn) (NVIDIA
CUDA® Deep Neural Network library) library is accessible via its
dedicated module:

    module load cuDNN/8.0.2.39-CUDA-11.0.2

which will automatically load the related CUDA version. Available
versions can be listed using:

    module spider cuDNN

Example Slurm script
====================

The following Slurm script illustrates a minimal example to request a
GPU card, load the CUDA toolkit and query some information about the
GPU:

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

Save this in a `test_gpu.sl` file and submit it using:

    sbatch test_gpu.sl

The content of job output file would look like:

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

> ### Note {#prerequisites}
>
> CUDA\_VISIBLE\_DEVICES=0 indicates that this job was allocated to CUDA
> GPU index 0 on this node. It is not a count of allocated GPUs.

NVIDIA Nsight Systems and Compute profilers
===========================================

[Nsight Systems](https://developer.nvidia.com/nsight-systems) is a
system-wide analysis tool, particularly good for profiling CPU-GPU
interactions. It is provided on Mahuika via the `Nsight-Systems` module:

    $ module load Nsight-Systems/2020.5.1
    Load `PyQt/5.12.1-gimkl-2020a-Python-3.8.2` module prior to running `nsys-ui`
    $ nsys --version
    NVIDIA Nsight Systems version 2020.5.1.85-5ee086b

This module gives you access to the
[nsys](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#cli-profiling)
command line tool or the
[nsys-ui](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#gui-profiling)
graphical interface.

[Nsight Compute](https://developer.nvidia.com/nsight-compute) is a
profiler for CUDA kernels. It is accessible on Mahuika using the
`Nsight-Compute` module:

    $ module load Nsight-Compute/2020.3.0
    Load `PyQt/5.12.1-gimkl-2020a-Python-3.8.2` module prior to running `nsys-ui`
    $ ncu --version
    NVIDIA (R) Nsight Compute Command Line Profiler
    Copyright (c) 2018-2020 NVIDIA Corporation
    Version 2020.3.0.0 (build 29307467) (public-release)

Then you can use the
[ncu](https://docs.nvidia.com/nsight-compute/NsightComputeCli/) command
line tool or the
[ncu-ui](https://docs.nvidia.com/nsight-compute/NsightCompute/index.html)
graphical interface.

> ### Important {#prerequisites}
>
> The `nsys-ui` and `ncu-ui` tools require access to a display server,
> either via
> [X11](https://support.nesi.org.nz/hc/en-gb/articles/360001075975-X11-on-NeSI)
> or a [Virtual
> Desktop](https://support.nesi.org.nz/hc/en-gb/articles/360001600235-Virtual-Desktop-via-Jupyter-on-NeSI).
> You also need to load the `PyQt` module beforehand:
>
>     module load PyQt/5.12.1-gimkl-2020a-Python-3.8.2
>     module load Nsight-Systems/2020.5.1
>     nsys-ui  # this will work only if you have a graphical session

Application and toolbox specific support pages
==============================================

The following pages provide additional information for supported
applications:

-   [ABAQUS](https://support.nesi.org.nz/hc/en-gb/articles/212457807-ABAQUS#gpus)
-   [GROMACS](https://support.nesi.org.nz/hc/en-gb/articles/360000792856-GROMACS#nvidia_gpu_container)
-   [Lambda
    Stack](https://support.nesi.org.nz/hc/en-gb/articles/360002558216-Lambda-Stack)
-   [Matlab](https://support.nesi.org.nz/hc/en-gb/articles/212639047-MATLAB#GPU)
-   [TensorFlow on
    GPUs](https://support.nesi.org.nz/hc/en-gb/articles/360000990436-TensorFlow-on-GPUs)

And programming toolkits:

-   [Offloading to GPU with
    OpenMP](https://support.nesi.org.nz/hc/en-gb/articles/360001127856-Offloading-to-GPU-with-OpenMP-)
-   [Offloading to GPU with OpenACC using the Cray
    compiler](https://support.nesi.org.nz/hc/en-gb/articles/360001131076-Offloading-to-GPU-with-OpenACC-using-the-Cray-compiler)
-   [NVIDIA GPU
    Containers](https://support.nesi.org.nz/hc/en-gb/articles/360001500156-NVIDIA-GPU-Containers)
