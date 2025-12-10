---
created_at: '2020-04-19T22:59:58Z'
tags:
- gpu
- slurm
---

This page provides generic information about how to access GPUs through the Slurm scheduler.

!!! warning
    Your first stop when looking into using GPUs should be the documentation
    of the application you are using.  
    Not every process can use a GPU, and how to use them effectively varies greatly!  
    There is a list of commonly used GPU supporting software at the bottom of this page.

!!! note
     Recall, memory associated with the GPUs is the VRAM, and is a separate resource from the RAM requested by Slurm. The memory values listed below are VRAM values.

## Request GPU resources using Slurm

To request a GPU for your [Slurm job](Submitting_your_first_job.md), add
the following option in the header of your submission script:

```sl
#SBATCH --gpus-per-node=1
```

You can specify the type and number of GPU you need using the following
syntax

```sl
#SBATCH --gpus-per-node=<gpu_type>:<gpu_number>
```

It is recommended to specify the exact GPU type required; otherwise, the job may be allocated to any available GPU at the time of execution.

<table>
    <tr>
        <td>Architecture</td>
        <td>Note</td>
        <td>VRAM</td>
        <td>Max</td>
        <td>Slurm Header</td>
    </tr>
    <tr>
        <td rowspan="2">NVIDIA A100</td>
        <td rowspan="2"></td>
        <td>80GB</td>
        <td>4</td>
        <td><pre><code>#SBATCH --partition=milan<br>#SBATCH --gpus-per-node=a100:1</code></pre></td>
    </tr>
    <tr>
        <td>40GB</td>
        <td>2</td>
        <td><pre><code>#SBATCH --partition=genoa<br>#SBATCH --gpus-per-node=a100:1</code></pre></td>
    </tr>
    <tr>
        <td>NVIDIA H100</td>
        <td></td>
        <td>96GB</td>
        <td>2</td>
        <td><pre><code>#SBATCH --gpus-per-node=h100:1</code></pre></td>
    </tr>
    <tr>
        <td>NVIDIA L4</td>
        <td>No double precision floating point (fp64)</td>
        <td>24GB</td>
        <td>4</td>
        <td><pre><code>#SBATCH --gpus-per-node=l4:1</code></pre></td>
    </tr>
</table>

You can also use the `--gpus-per-node`option in
[Slurm interactive sessions](../Interactive_Computing/Slurm_Interactive_Sessions.md),
with the `srun` and `salloc` commands. For example:

``` sh
srun --job-name "InteractiveGPU" --gpus-per-node L4:1 --partition genoa --cpus-per-task 8 --mem 2GB --time 00:30:00 --pty bash
```

will request and then start a bash session with access to a L4 GPU, for a
duration of 30 minutes.

!!! warning
     When you use the `--gpus-per-node`option, Slurm automatically sets the
     `CUDA_VISIBLE_DEVICES` environment variable inside your job
     environment to list the index/es of the allocated GPU card/s on each
     node.

     ``` sh
     srun --job-name "GPUTest" --gpus-per-node=L4:2 --time 00:05:00 --pty bash
     ```
     
     ```out
     srun: job 20015016 queued and waiting for resources
     srun: job 20015016 has been allocated resources
     $ echo $CUDA_VISIBLE_DEVICES
     0,1
     ```

## Load CUDA and cuDNN modules

To use an Nvidia GPU card with your application, you need to load the
driver and the CUDA toolkit via the [environment modules](../Software/Available_Applications/index.md)
mechanism:

``` sh
module load CUDA/11.0.2
```

You can list the available versions using:

``` sh
module spider CUDA
```

Please {% include "partials/support_request.html" %} if you need a version not
available on the platform.


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

#SBATCH --job-name       GPUJob      # job name (shows up in the queue)
#SBATCH --account        nesi99991   # Your account
#SBATCH --time           00-00:10:00 # Walltime (DD-HH:MM:SS)
#SBATCH --partition      genoa       # This means the job will land on A100 with 40GB VRAM
#SBATCH --gpus-per-node  A100:1      # GPU resources required per node
#SBATCH --cpus-per-task  2           # number of CPUs per task (1 by default)
#SBATCH --mem            512MB       # amount of memory per node (1 by default)

# load CUDA module
module purge
module load CUDA/11.0.2

# display information about the available GPUs
nvidia-smi

# check the value of the CUDA_VISIBLE_DEVICES variable
echo "CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES}"
```

Save this in a `test_gpu.sl` file and submit it using:

``` sh
sbatch test_gpu.sl
```

The content of job output file would look like:

``` sh
cat slurm-20016124.out
```

```sh
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

## Application and toolbox specific support pages

The following pages provide additional information for supported
applications:

- [ABAQUS](../Software/Available_Applications/ABAQUS.md#examples)
- [GROMACS](../Software/Available_Applications/GROMACS.md)
- [Lambda Stack](../Software/Available_Applications/Lambda_Stack.md)
- [Matlab](../Software/Available_Applications/MATLAB.md#using-gpus)
- [TensorFlow on GPUs](../Software/Available_Applications/TensorFlow_on_GPUs.md)

And programming toolkits:

- [NVIDIA GPU Containers](../Software/Containers/NVIDIA_GPU_Containers.md)
