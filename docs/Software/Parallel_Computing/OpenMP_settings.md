---
created_at: '2019-07-22T03:46:24Z'
tags: []
---

[OpenMP](https://en.wikipedia.org/wiki/OpenMP) is an application
programming interface that lets you write parallel programs on shared
memory platforms. In a parallel section, OpenMP code can create multiple
threads that run on separate CPU cores, executing their shares of the total
workload concurrently.

The environment variable that controls the number of threads is
`OMP_NUM_THREADS`. At the start of a Slurm job we automatically set
`OMP_NUM_THREADS` equal to `$SLURM_CPUS_PER_TASK` if it isn't already set, so
all that is necessary to get 16 OpenMP threads is:

```sl
#SBATCH --cpus-per-task=16
```

in your Slurm script - although this can sometimes be more complicated,
e.g., with
[TensorFlow on CPUs](../Available_Applications/TensorFlow_on_CPUs.md).

In order to achieve good and consistent parallel scaling, additional
settings may be required. This is particularly true on Mahuika where
nodes are generally shared between different Slurm jobs. Following are some
settings that can help improve scaling and/or make your timings more
consistent, additional information can be found in our article
[Thread Placement and Thread Affinity](./Thread_Placement_and_Thread_Affinity.md).

1. `--threads-per-core=2`. Use this option to tell srun or sbatch to
that you want to use [Hyperthreading](Hyperthreading.md),
so use both of the virual CPUs available on each physical core,
halving the number of physical cores you occupy.
If you use hyperthreading, you will be charged for the number of physical cores that
you requested - the second logical CPU on a physical CPU core is free,
although Slurm always reports both CPUs.  The older option `--hint=multithread` is also equivalent to `--threads-per-core=2`.

3. `OMP_PROC_BIND`. Set this environment variable to "true" to pin the threads down during
program execution. By default, threads may migrate from one core to
another, depending on the load on the node. In an HPC setting, it is
generally advisable to pin the threads to avoid delays caused by thread
migration.

4. `OMP_PLACES`. Set this to "cores" if you want to pin the threads to
physical cores, or to "threads" if you want to use hyperthreading.

The effect of each setting is illustrated below. In this experiment we
measured the execution time twice of the finite difference
code [upwindCxx -numCells 256 -numSteps 10.](https://github.com/pletzer/fidibench) The code was built with the
gimpi/2018b toolchain on Mahuika.

| Number of physical cores |  | `OMP_PROC_BIND=true`, `OMP_PLACES=cores` | `--threads-per-core=2`, `OMP_PROC_BIND=true`. `OMP_PLACES=threads` |
|--------------------|----------------------|----------------------|---------------------|
| 1 | 1m43s, 1m42s | 1m42s, 1m42s | 1m30s, 1m30s |
| 2 | 1m30s, 1m31s | 1m03, 55s | 56s, 56s |
| 4 | <span style="color:red">58s, 1m27s</span> | <span style="color:blue">45s, 41s</span> | <span style="color:green">27s, 28s</span> |
| 8 | 24s, 27s | 18s, 17s | 16s, 16s |

So by explicitly using `--threads-per-core` and setting `OMP_PROC_BIND` and `OMP_PLACES`.
In many cases we expect one of the following to work best:

| --threads-per-core | `OMP_PROC_BIND=` | `OMP_PLACES=` |
|--------------------|------------------|--------------|
| 1                  | true             | cores        |
| 2                  | true             | threads      |

Let us know if you find other settings to work better for you.
