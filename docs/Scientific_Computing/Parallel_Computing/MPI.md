---
created_at: 2025-02-21
---




MPI stands for *Message Passing Interface*, and is a communication protocol used to achieve distributed parallel computation.

Similar in some ways to multi-threading, MPI does not have the limitation of requiring shared memory and thus can be used across multiple nodes, but has higher communication and memory overheads.

For MPI jobs you need to set `--ntasks` to a value larger than 1, or if you want all nodes to run the same number of tasks, set `--ntasks-per-node` and `--nodes` instead.

MPI programs require a launcher to start the *ntasks* processes on multiple CPUs, which may belong to different nodes.
On Slurm systems like ours, the preferred launcher is `srun` rather than `mpi-run`.

Since the distribution of tasks across different nodes may be unpredictable, `--mem-per-cpu` should be used instead of `--mem`.

``` sl
#!/bin/bash -e
#SBATCH --job-name=MPIJob       # job name (shows up in the queue)
#SBATCH --time=00:01:00         # Walltime (HH:MM:SS)
#SBATCH --mem-per-cpu=512MB     # memory/cpu in MB (half the actual required memory)
#SBATCH --cpus-per-task=4       # 2 Physical cores per task.
#SBATCH --ntasks=2              # number of tasks (e.g. MPI)

srun pwd                        # Prints  working directory
```

The expected output being

```txt
/home/user001/demo
/home/user001/demo
```

!!! warning
    For non-MPI programs, either set `--ntasks=1` or do not use `srun` at all.
    Using `srun` in conjunction with `--cpus-per-task=1` will cause `--ntasks` to default to 2.
