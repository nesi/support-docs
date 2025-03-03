---
created_at: 2025-02-21
---

Many scientific software applications are written to take advantage of multiple CPUs in some way. But often this must be specifically requested by the user at the time they run the program, rather than happening automatically.

The are three types of parallel execution we will cover are [Multi-Threading](#multi-threading), [Distributed (MPI)](#mpi) and [Job Arrays](#job-arrays).

!!! note
    Whenever Slurm mentions CPUs it is referring to *logical* CPU's (**2** *logical* CPU's = **1** *physical* core).  
    - `--cpus-per-task=4` will give you 4 *logical* cores.
    - `--mem-per-cpu=512MB` will give 512 MB of RAM per *logical* core.
    - If `--hint=nomultithread` is used then `--cpus-per-task` will now refer to physical cores, but `--mem-per-cpu=512MB` still refers to logical cores.

See [our article on hyperthreading](../Mahuika_Cluster/Next_Steps/Hyperthreading.md) for more information.
