---
title: "What is Parallel Computing"
teaching: 20
exercises: 10
questions:
- "How do we execute a task in parallel?"
- "What benefits arise from parallel execution?"
- "What are the limits of gains from execution in parallel?"
- "What is the difference between implicit and explicit parallelisation."
objectives:
- "Prepare a job submission script for the parallel executable."
keypoints:
- "Parallel programming allows applications to take advantage of
  parallel hardware; serial code will not 'just work.'"
- "There are multiple ways you can run "
---

## Methods of Parallel Computing

To understand the different types of Parallel Computing we first need to clarify some terms.

{% include figure.html url="" max-width="40%"
   file="/fig/clusterDiagram.png"
   alt="Node anatomy" caption="" %}

**CPU**: Unit that does the computations.

**Task**: One or more CPUs that share memory.

**Node**: The physical hardware. The upper limit on how many CPUs can be in a task.

**Shared Memory**: When multiple CPUs are used within a single task.

**Distributed Memory**: When multiple tasks are used.

Which methods are available to you is largely dependent on the nature of the problem and software being used.

### Shared-Memory (SMP)

Shared-memory multiproccessing divides work among _CPUs_ or _threads_, all of these threads require access to the same memory.

Often called *Multithreading*.

This means that all CPUs must be on the same node, most Mahuika nodes have 72 CPUs.

Shared memory parallelism is used in our example script `{{ site.example.script }}`.

Number of threads to use is specified by the Slurm option `--cpus-per-task`.

### Distributed-Memory (MPI)

Distributed-memory multiproccessing divides work among _tasks_, a task may contain multiple CPUs (provided they all share memory, as discussed previously).

Message Passing Interface (MPI) is a communication standard for distributed-memory multiproccessing. While there are other standards, often 'MPI' is used synonymously with Distributed parallelism.  

Each task has it's own exclusive memory, tasks can be spread across multiple nodes, communicating via and _interconnect_. This allows MPI jobs to be much larger than shared memory jobs. It also means that memory requirements are more likely to increase proportionally with CPUs.

Distributed-Memory multiproccessing predates shared-memory multiproccessing, and is more common with classical high performance applications (older computers had one CPU per node).

Number of tasks to use is specified by the Slurm option `--ntasks`, because the number of tasks ending up on one node is variable you should use `--mem-per-cpu` rather than `--mem` to ensure each task has enough.

Tasks cannot share cores, this means in most circumstances leaving `--cpus-per-task` unspecified will get you `2`.

Using a combination of Shared and Distributed memory is called _Hybrid Parallel_.

### GPGPU's

GPUs compute large number of simple operations in parallel, making them well suited for Graphics Processing (hence the name), or any other large matrix operations.

On NeSI, GPU's are specialised pieces of hardware that you request in addition to your CPUs and memory.

You can find an up-to-date(ish) list of GPUs available on NeSI in our [Support Documentation](https://docs.nesi.org.nz/Scientific_Computing/The_NeSI_High_Performance_Computers/Available_GPUs_on_NeSI/)

GPUs can be requested using `--gpus-per-node=<gpu_type>:<gpu_number>`

Depending on the GPU type, we *may* also need to specify a partition using `--partition`.

> ## GPU Job Example
>
> Create a new script called `gpu-job.sl`
>
> ```
> #!/bin/bash -e
>
> #SBATCH --job-name        gpu-job
> #SBATCH --account         {{site.sched.projectcode}} 
> #SBATCH --output          %x.out
> #SBATCH --mem-per-cpu     2G
> #SBATCH --gpu-per-node    P100:1
> 
> module load CUDA
> nvidia-smi  
> ```
> {: .language-bash}
>
> then submit with
>
> ```
> {{ site.remote.prompt }} sbatch gpu-job.sl
> ```
> {: .language-bash}
>
> > ## Solution
> >
> > ```
> > {{ site.remote.prompt }} cat gpu-job.out
> >
> > ```
> > {: .language-bash}
> >
> > ```
> > Tue Mar 12 19:40:51 2024       
> > +-----------------------------------------------------------------------------+
> > | NVIDIA-SMI 525.85.12    Driver Version: 525.85.12    CUDA Version: 12.0     |
> > |-------------------------------+----------------------+----------------------+
> > | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
> > | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
> > |                               |                      |               MIG M. |
> > |===============================+======================+======================|
> > |   0  Tesla P100-PCIE...  On   | 00000000:05:00.0 Off |                    0 |
> > | N/A   28C    P0    24W / 250W |      0MiB / 12288MiB |      0%      Default |
> > |                               |                      |                  N/A |
> > +-------------------------------+----------------------+----------------------+
> >                                                                                
> > +-----------------------------------------------------------------------------+
> > | Processes:                                                                  |
> > |  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
> > |        ID   ID                                                   Usage      |
> > |=============================================================================|
> > |  No running processes found                                                 |
> > +-----------------------------------------------------------------------------+
> > ```
> > {: .output}
> {: .solution}
{: .challenge}

### Job Array

Job arrays are not "multiproccessing" in the same way as the previous two methods.
Ideal for _embarrassingly parallel_ problems, where there are little to no dependencies between the different jobs.

Can be thought of less as running a single job in parallel and more about running multiple serial-jobs simultaneously.
Often this will involve running the same process on multiple inputs.

Embarrassingly parallel jobs should be able to scale without any loss of efficiency. If this type of parallelisation is an option, it will almost certainly be the best choice.

A job array can be specified using `--array`

If you are writing your own code, then this is something you will probably have to specify yourself.

## How to Utilise Multiple CPUs

Requesting extra resources through Slurm only means that more resources will be available, it does not guarantee your program will be able to make use of them.

Generally speaking, Parallelism is either _implicit_ where the software figures out everything behind the scenes, or _explicit_ where the software requires extra direction from the user.

### Scientific Software

The first step when looking to run particular software should always be to read the documentation.
On one end of the scale, some software may claim to make use of multiple cores implicitly, but this should be verified as the methods used to determine available resources are not guaranteed to work.

Some software will require you to specify number of cores (e.g. `-n 8` or `-np 16`), or even type of paralellisation (e.g. `-dis` or `-mpi=intelmpi`).

Occasionally your input files may require rewriting/regenerating for every new CPU combintation (e.g. domain based parallelism without automatic partitioning).

### Writing Code

Occasionally requesting more CPUs in your Slurm job is all that is required and whatever program you are running will automagically take advantage of the additional resources.
However, it's more likely to require some amount of effort on your behalf.

It is important to determine this before you start requesting more resources through Slurm  

If you are writing your own code, some programming languages will have functions that can make use of multiple CPUs without requiring you to changes your code.
However, unless that function is where the majority of time is spent, this is unlikely to give you the performance you are looking for.

*Python: [Multiproccessing](https://docs.python.org/3/library/multiprocessing.html)* (not to be confused with `threading` which is not really parallel.)

*MATLAB: [Parpool](https://au.mathworks.com/help/parallel-computing/parpool.html)*

## Summary

| Name | Other Names | Slurm Option | Pros/cons |
| - | - | - | - |
| Shared Memory Parallelism | Multithreading, Multiproccessing | `--cpus-per-task` |  |
| Distrubuted Memory Parallelism | MPI, OpenMPI |  `--ntasks` and add `srun` before command | |
| Hybrid | | `--ntasks` and `--cpus-per-task` and add `srun` before command | |
| Job Array | | `--array` | |
| General Purpose GPU | | `--gpus-per-node`  | |

> ## Running a Parallel Job.
>
> Pick one of the method of Paralellism mentioned above, and modify your `example.sl` script to use this method.
>
>
> > ## Solution
> >
> > What does the printout say at the start of your job about number and location of node.
> > {: .output}
> {: .solution}
{: .challenge}

{% include links.md %}
