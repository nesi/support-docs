---
created_at: 2025-02-21
description: 
---

Multi-threading is a method of parallelisation whereby the initial single thread of a process forks into a number of parallel threads, generally *via* a library such as OpenMP (Open MultiProcessing), TBB (Threading Building Blocks), or pthread (POSIX threads).

![serial](../Mahuika_Cluster/Next_Steps/parallel_execution_serial.png)  

![parallel](../Mahuika_Cluster/Next_Steps/Parallel_Execution.png)  
Multi-threading involves dividing the process into multiple 'threads' which can be run across multiple cores.

Multi-threading is limited in that it requires shared memory, so all CPU cores used must be on the same node. However, because all the CPUs share the same memory environment things only need to be loaded into memory once, meaning that memory requirements will usually not increase proportionally to the number of CPUs.

Example script:

``` sl
#!/bin/bash -e
#SBATCH --job-name=MultithreadingTest    # job name (shows up in the queue)
#SBATCH --time=00:01:00                  # Walltime (HH:MM:SS)
#SBATCH --mem=2048MB                     # memory in MB 
#SBATCH --cpus-per-task=4                # 2 physical cores per task.

taskset -c -p $$                         #Prints which CPUs it can use
```

The expected output being

```txt
pid 13538's current affinity list: 7,9,43,45
```
