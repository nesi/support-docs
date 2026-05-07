---
created_at: '2020-04-19T22:59:58Z'
tags:
- gpu
- slurm
---

This page provides generic information about how to access GPUs through the Slurm scheduler.

## When to use a GPU

You should consider using a GPU for your work if:

* Your job has GPU support/functionality, and
* You job is substantially large or will run for a long time without GPU support
* Or you are performing a task that needs a GPU (e.g. work with large language models, some machine learning methods such as neural networks)

!!! warning
    Your first stop when looking into using GPUs should be the documentation
    of the application you are using.  
    Not every process can use a GPU, and how to use them effectively varies greatly!  
    There is a list of commonly used GPU supporting software at the bottom of this page.

## Request GPU resources using Slurm

To request a GPU for your [Slurm job](Tutorial:_Submitting_your_first_job.md), add
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

!!! note
     Recall, memory associated with the GPUs is the VRAM, and is a separate resource from the RAM requested by Slurm. The memory values listed below are VRAM values.

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

## Live monitoring your job's GPU(s)

It is possible to visually inspect your job's GPU usage live. To do this:

1. Obtain the job id for your job of interest by typing `squeue --me` into the terminal.

    ```bash
    user.name@login03:$ squeue --me
    JOBID         USER     ACCOUNT   NAME        CPUS MIN_MEM PARTITI START_TIME     TIME_LEFT STATE    NODELIST(REASON)    
    5826164       user.nam nesi99999 Example_GPU_   8     24G genoa   Apr 30 17:36  9-23:58:08 RUNNING  g09               
    ```

2. Jump onto the node your job is running by typing `jump_into <JobId>`, where you replace `<JobId>` with your Job of interest.

    ```bash
    user.name@login03:$ jump_into 5826164
    Jumping to node: g09 (job 5826164)    
    ```

3. Type into the terminal `nvtop`. This will open an interface that will allow you to inspect how your job run on the GPU.

    ![nvtop](../assets/images/GPU_nvtop.png){ width="800" }

## Measuring GPU efficiency after a job has finished

It is possible to measure your GPU's processing and memory efficiency in two ways:

### 1. Using `nn_seff`

Once your job has finished, it is possible to use `nn_seff` to get a measure of the GPU processing and memory efficiency. To use this feature, type into the terminal

```bash
nn_seff <JobID>
```

Where `<JobID>` is the job ID for the job of interest. For example:

```bash
user.name@login03:$ nn_seff 5831746
Cluster: hpc
Job ID: 5831746
State: CANCELLED
Cores: 4
Tasks: 1
Nodes: 1
Job Wall-time:     0.1%  00:09:02 of 10-00:00:00 time limit
CPU Utilisation:  98.4%  00:35:34 of 00:36:08 core-walltime
Mem Utilisation:   1.2%  284.37 MB of 24.00 GB
GPU Utilisation:  55  %
GPU Memory:        2.2%  510.00 MB of 23 GB
```

### 2. Using Slurm Native Profiling

Before you begin your slurm job, include the following line somewhere at the start of your slurm submission file:

```bash
#SBATCH --profile task
```

Then allow your job to run. Once your job has finished, type in to the terminal

```bash
profile_plot <JobID>
```

Where `<JobID>` is the job ID for the job of interest. For example:

```bash
user.name@login03:$ nn_seff 5831962
```

This will create a file called `<JobID>_profile.png`, which will look something like this:

![5831962_profile.png](../assets/images/GPU_5831962_profile.png)

See [Slurm Native Profiling](../Software/Profiling_and_Debugging/Slurm_Native_Profiling.md) for more information on this feature. 

## Look up the GPU availability and queue

It is possible to check how many GPUs are available and what the GPU queue looks like using the `gpu_avail` command:

```bash
user.weal@login03:$ gpu_avail -h
usage: gpu_avail [-h] [-q] [-d] [-t TYPE]

Show GPU availability per node (sinfo) and/or GPU queue per type (squeue).

options:
  -h, --help            show this help message and exit
  -q, --queue           Queue-only output. With -d, show detailed queue-only output.
  -d, --detailed        Detailed output.
  -t TYPE, --type TYPE  Comma-separated GPU types to include (e.g., a100,l4,h100).
```

If you type into the terminal:

```bash
gpu_avail
```

This will show the total number of free GPUs at any one time

```bash
user.name@login03:$ gpu_avail
Cluster GPU summary
  - A100 (40GB): free 0 / total 8 (used 8, unavailable 0)
  - A100 (80GB): free 0 / total 16 (used 16, unavailable 0)
  - H100 (96GB): free 0 / total 8 (used 8, unavailable 0)
  - L4 (24GB): free 0 / total 16 (used 16, unavailable 0)
```

You can see more what jobs are running and pending in the GPU queue for each GPU by typing into the terminal:

```bash
gpu_avail -q
```

This will show all jobs that have requested GPUs, and give you a better idea of the availability of GPUs

```bash
user.name@login03:$ gpu_avail -q
GPU queue detailed report (per GPU type)

A100 (40GB)
  Running jobs: 8 (GPUs: 8)
  Pending jobs: 2 (GPUs: 2)
  Estimated availability for 1 A100 (40GB) GPU: 2026-04-30 18:55:36 NZST

  Running jobs:
    JOBID        USER       PART         NODE             CPU    Memory     START               LEFT         TRES                                                    
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------
    1234567      abcd123    genoa        g02              16     8 GB       Apr 29 08:04        13:37:14     gres/gpu:a100:1                                         
    1234568      abcd123    genoa        g04              16     4 GB       Apr 29 20:44        2:17:13      gres/gpu:a100:1                                         
    1234569      abcd123    genoa        g03              16     4 GB       Apr 30 09:15        14:47:41     gres/gpu:a100:1                                         
    1234570      abcd123    genoa        g03              16     4 GB       Apr 30 09:15        14:48:11     gres/gpu:a100:1                                         
    1234571      abcd123    genoa        g01              4      16 GB      Apr 30 16:55        27:59        gres/gpu:a100:1                                         
    1234572      abcd123    genoa        g01              8      32 GB      Apr 30 16:56        29:15        gres/gpu:a100:1                                         
    1234573      abcd123    genoa        g04              4      32 GB      Apr 30 17:20        9:23:01      gres/gpu:a100:1                                         
    1234574      abcd123    genoa        g02              8      32 GB      Apr 30 17:25        58:03        gres/gpu:a100:1                                         
  
  Pending jobs:
    JOBID        USER       PART         CPU    Memory     START               LIMIT        TRES                                                     REASON                
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    1234575      abcd123    genoa        1      20 GB      May 06 11:45        4:45:00      gres/gpu:a100:1                                          (Priority)            
    1234576      abcd123    genoa        1      20 GB      May 06 16:30        4:45:00      gres/gpu:a100:1                                          (Priority)            

A100 (80GB)
...
```

Note that there might be your or other peoples jobs pending in the queue, even if there is a free GPU available. This may be because a GPU node might not have enough CPUs or memory resources available.

To see the CPU and memory resources available on each of the GPU nodes, type into the terminal:

```bash
gpu_avail -n
```

This will show all the resources available for each GPU node, ordered by GPU type:

```bash
user.name@login03$ gpu_avail -d
GPU nodes report

=== A100 (40GB) ===

- Node:          g01   State: mixed-
  CPU idle/total: 6/164 (alloc 162, other 0)
  Mem free/total: 113.0 GB / 717.2 GB
  GPUs: A100 (40GB): free 0 / total 2 (used 2)

- Node:          g02   State: allocated
  CPU idle/total: 2/164 (alloc 166, other 0)
  Mem free/total: 74.9 GB / 717.2 GB
  GPUs: A100 (40GB): free 0 / total 2 (used 2)

- Node:          g03   State: allocated
  CPU idle/total: 2/164 (alloc 166, other 0)
  Mem free/total: 385.5 GB / 717.2 GB
  GPUs: A100 (40GB): free 0 / total 2 (used 2)

- Node:          g04   State: mixed-
  CPU idle/total: 8/164 (alloc 160, other 0)
  Mem free/total: 112.1 GB / 717.2 GB
  GPUs: A100 (40GB): free 0 / total 2 (used 2)

=== A100 (80GB) ===
...
```


## Application and toolbox specific support pages

See the [Supported Applications](../Software/Available_Applications/index.md) for more information on what softwares have GPU support, as well as programming toolkits:

- [NVIDIA GPU Containers](../Software/Containers/NVIDIA_GPU_Containers.md)
