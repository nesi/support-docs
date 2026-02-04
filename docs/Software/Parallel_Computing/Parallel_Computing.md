---
created_at: '2019-01-10T03:02:11Z'
tags:
  - parallel
description: How to take advantage of multiple CPUs in high performance computing.
---

To properly utilise high performance computing hardware, you need to be able to utilise multiple CPUs.
Many scientific software applications support parallel execution,
but this often requires explicit configuration rather than happening automatically.

Some definitions that will help you understand this page: 

- **CPU**: The hardware that performs computations
- **Task**: An independent process that is run using one or more CPUs. All CPUs assigned to a task share the same memory.
- **Node**: The physical hardware. Each node contains memory and a number of CPUs.
- **Shared Memory**: Multiple CPUs used within a single task
- **Distributed Memory**: Multiple tasks used across nodes

## Utilizing Multiple CPUs

Requesting extra resources through Slurm doesn't guarantee your program will use them. 
Always consult the software specific documentation first when trying to determine what types of parallel computing to use (and how).
Software may:

- Claim implicit multi-core support (verify this works)
- Require explicit core specification in command line (e.g., `-n 8`, `-np 16`)
- Need parallelization type specified in command line (e.g., `-dis`, `-mpi=intelmpi`)
- Require input file regeneration to be configured in a particular way, (partitioning into same number of domains as tasks, etc).
- Give estimates on initial resource requirements.

### Quick Reference

| Method | Also Called | Slurm Options | Usage |
|--------|------------------|---------------|-------------------|
| [Shared Memory](#shared-memory) | Multithreading, SMP | `--cpus-per-task` | Limited to single node; efficient memory use |
| [Distributed Memory](#distributed-memory) | MPI | `--ntasks` | Scales across nodes; higher overhead |
| [Hybrid](#hybrid-parallel) | - | `--ntasks` + `--cpus-per-task` | Combines both approaches |
| [Job Array](#job-arrays) | - | `--array` | Best for independent tasks |
| [GPU](#gpus) | GPGPU | `--gpus-per-node` | Specialized hardware for matrix operations |

## Shared Memory

Shared Memory Parallelism, or multi-threading, parallelises itself by forking (duplicating) a single process into multiple parallel threads via libraries like OpenMP (OMP), TBB, or pthread.

A non-parallalised (series) program works like this:

![serial](../../assets/images/parallel_execution_serial.png)  

In contrast, a shared memory parallelised program works like this:

![parallel](../../assets/images/Parallel_Execution.png)  

A shared memory parallelised program:

- Requires shared memory (so all CPUs must be on same node)
- Limited by node capacity (e.g., On Mahuika the maximum number of CPUs that can be requested for a shared memory job is 166 (or twice that with simultaneous multithreading (SMP)))
- Uses `--cpus-per-task` to specify thread count

### Example Script

```sl
#!/bin/bash -e

#SBATCH --job-name       MultithreadingTest
#SBATCH --account        nesi99991
#SBATCH --time           00:01:00
#SBATCH --mem            2048MB
#SBATCH --cpus-per-task  4

taskset -c -p $$  # Prints available CPUs
```

!!! note "See also"
    - [Multiththreading](Multithreading_Scaling_Example.md)
    - [Python Multiprocessing](https://docs.python.org/3/library/multiprocessing.html) (not `threading`, which isn't truly parallel in Python).
    - [MATLAB Parpool](https://au.mathworks.com/help/parallel-computing/parpool.html)

## Distributed Memory

Distributed memory parellelism, generally implemented with the Message Passing Interface (MPI), enables distributed parallel computation across multiple nodes through inter-process communication.

A distributed memory parallelisation program:

- Does not require shared memory (Each task has its own memory).
- Can utilise multiple nodes.
- Has higher communication and memory overhead than multi-threading
- Memory requirements typically scale with CPU count
- Predates shared-memory parallelism; common in classical HPC applications

- Use `--ntasks` (>1), or `--ntasks-per-node` together with `--nodes`
- Use `--mem-per-cpu` instead of `--mem` to ensure consistent memory regardless of how Slurm packs tasks onto nodes.
- Launched via `mpirun` or preferably Slurm's `srun`.

### Example Script

```sl
#!/bin/bash -e

#SBATCH --job-name       MPIJob
#SBATCH --account        nesi99991
#SBATCH --time           00:01:00
#SBATCH --mem-per-cpu    512MB
#SBATCH --ntasks         4

srun bash -c 'taskset -c -p $$'  # Prints CPU available to each task
```

!!! warning
    For non-MPI programs, either set `--ntasks=1` or do not use `srun` at all.
    Using `srun` in conjunction with `--cpus-per-task=1` will cause `--ntasks` to default to 2.

!!! note "See also"
    - [MPI Scaling Example](MPI_Scaling_Example.md)

## Hybrid Parallel

Combining `--ntasks` and `--cpus-per-task` for distributed tasks each of which is multi-threaded. 
Not commonly supported.

### Example Script

```sl
#!/bin/bash -e

#SBATCH --job-name       HybridJob
#SBATCH --account        nesi99991
#SBATCH --time           00:01:00
#SBATCH --mem-per-cpu    512MB
#SBATCH --cpus-per-task  4
#SBATCH --ntasks         2

srun bash -c 'taskset -c -p $$'  # Prints CPUs available to each task
```

## Job Arrays

Job arrays execute independent tasks simultaneously—ideal for *embarrassingly parallel* problems with no inter-task dependencies (e.g. parameter sweeps).

- Tasks can execute in any order.
- Efficient way to run multiple serial jobs simultaneously rather than applying multiple CPUs to a single job.
- Scales without efficiency loss.
- Use `--array` to specify index range

### Example Script

``` sl
#!/bin/bash -e

#SBATCH --job-name       ArrayJob     # job name (shows up in the queue)
#SBATCH --account        nesi99991    # Project to bill
#SBATCH --time           00:01:00     # Walltime (HH:MM:SS)
#SBATCH --mem            512MB        # Memory
#SBATCH --array          1-2          # Array jobs

echo "This is result ${SLURM_ARRAY_TASK_ID}"
```

!!! note "See also"
    - For more info see the page on [Job Arrays](./Job_Arrays.md)

## GPUs

GPUs excel at large-scale parallel operations on matrices, making them ideal for machine learning, graphics processing and simulating many kinds of physical systems.

- Specialized hardware requested in addition to CPUs and memory.
- Well-suited for large matrix operations and machine learning.
- Use `--gpus-per-node=<gpu_type>:<gpu_number>`

### Example Script

```bash
#!/bin/bash -e

#SBATCH --job-name        gpu-job
#SBATCH --account         nesi99991
#SBATCH --output          %x.out
#SBATCH --mem-per-cpu     2G
#SBATCH --gpus-per-node   P100:1

module load CUDA
nvidia-smi
```

Should print out a summary of GPU utilisation.

!!! note "See also"
    - [Using GPUs](../../Batch_Computing/Using_GPUs.md) for more in depth documentation about GPUs.
    - [Hardware](../../Batch_Computing/Hardware.md) for a full list of available GPUs.

