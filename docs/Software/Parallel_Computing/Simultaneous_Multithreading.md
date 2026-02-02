---
created_at: '2018-11-15T22:10:10Z'
tags: 
   - hyperthreading
   - hyper-threading
   - multithreading
   - simultaneous
   - SMT
description: How to use simultaneous multithreading (hyper-threading) on NeSI.
---

As CPU technology advanced engineers realised that including multiple *logical* *processors* within each physical CPU core
(conventionally, a CPU) can allow some computation to occur simultaneously.
The name for this technology is [Simultaneous Multithreading](https://en.wikipedia.org/wiki/Simultaneous_multithreading) (SMT).

!!! note "Hyper-Threading"
    *Hyper-Threading* is Intel's proprietary implementation of Simultaneous Multithreading (SMT).
    The term is often used informally to refer to SMT in general,
    even though Intel's is not the only implementation of SMT.

CPUs capable of SMT consists of multiple (in practice, two) logical processors per
physical core. Having those two logical processors allows the core
to run two threads simultaneously, but they share most of their computational hardware with their partners.
So for example if both are doing intense floating-point calculations they will be
keeping their shared floating-point hardware full and so may be no faster overall than a single
thread would be. On the other hand, if the threads are spending most of their time waiting for data to
arrive from memory, then two threads may well get twice as much work done as one.

SMT is enabled on NeSI machines, however our Slurm is configured to
use only one thread per physical core by default.

## SMT with Slurm

A Slurm job which requests `--ntasks=N` and `--cpus-per-task=C`
(both of which default to 1) will run a total of N ✕ C threads and so need that number of logical cores.  
Slurm has another option `--threads-per-core` which we have set to default to 1.
and so jobs will by default use only one of the two logical processors
on each core. Since cores are never shared with other jobs, the unused spare logical processors
are still accounted as being occupied by the job and commands such as `sacct` will show the job
having occupied N ✕ C ✕ 2 CPUs.

If you set `--threads-per-core=2` (or almost equivalently `--hint=multithread`) then Slurm will make both logical processors
available to the job on each core, so will pack the job on to only half as many cores - N ✕ C ÷ 2 (rounded up if N ✕ C is an odd number)
which may well be more efficient overall.

## When to use SMT

SMT increases the efficiency of some parallel jobs, so we recommend trying it
if you are running many of those. But since it complicates the
mathematics at small levels of parallel scaling (e.g: a 1-thread job and a 2-thread SMT job
both use 1 core, a 3- or 4-thread SMT job uses 2 cores) it might be simplest to first find
your optimum number of threads without SMT, and then see what happens when you
add `--threads-per-core=2`. If the performance is better than 50% of what it was
(or better than 100% when also doubling `--threads-per-task` to get back
to the same quantity of physical hardware) then you are benefiting from SMT.

## Memory Usage

Enabling SMT changes the outcome of the flag `--mem-per-cpu`, if SMT is disabled `--mem-per-cpu` is memory per physical core, if SMT is enabled `--mem-per-cpu` is memory per thread, i.e. double the memory.

```sh
#SBATCH --ntasks       1
#SBATCH --mem-per-cpu  1G
```

Will get you 1G of memory.

```sh
#SBATCH --ntasks       1
#SBATCH --mem-per-cpu  1G
#SBATCH --hint         multithread
```

Will get you 2G of memory.

## Licences

Sometimes enabling SMT will make software that requires licences on a per core basis to require twice as many.
