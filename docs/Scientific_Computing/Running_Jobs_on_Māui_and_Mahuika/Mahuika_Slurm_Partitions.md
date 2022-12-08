## Definitions

**CPU:** A logical core, also known as a hardware thread. Referred to as
a \"CPU\" in the Slurm documentation.  Since
[Hyperthreading](https://support.nesi.org.nz/hc/en-gb/articles/360000568236/)
is enabled, there are two CPUs per physical core, and every task--- and
therefore every job --- is allocated an even number of CPUs.

**Fairshare Weight:** CPU hours are multiplied by this factor to
determine usage for the purpose of calculating a project\'s [fair-share
score](https://support.nesi.org.nz/hc/en-gb/articles/360000743536/).

**Job:** A running batch script and any other processes which it might
launch with *srun*.

**Node: **A single computer within the cluster with its own CPUs and RAM
(memory), and sometimes also GPUs. A node is analogous to a workstation
(desktop PC) or laptop.

**Task:** An instance of a running computer program, consisting of one
or more threads. All of a task\'s threads must run within the same node.

**Thread:** A sequence of instructions executed by a CPU.

**Walltime: **Real world time, as opposed to CPU time (walltime x CPUs).

## General Limits

-   No individual job can request more than 20,000 CPU hours. This has
    the consequence that a job can request more CPUs if it is shorter
    (short-and-wide vs long-and-skinny).
-   No individual job can request more than 576 CPUs (8 full nodes),
    since larger MPI jobs are scheduled less efficiently and are
    probably suitable for running on Māui.
-   No user can have more than 1,000 jobs in the queue at a time.

These limits are defaults and can be altered on a per-account basis if
there is a good reason. For example we will increase the limit on queued
jobs for those who need to submit large numbers of jobs, provided that
they undertake to do so with job arrays.

## Partitions

A partition can be specified via the appropriate [sbatch
option](https://support.nesi.org.nz/hc/en-gb/articles/360000691716/),
e.g.:

    #SBATCH --partition=milan

However on Mahuika there is generally no need to do so, since the
default behaviour is that your job will be assigned to the most suitable
partition(s) automatically, based on the resources it requests,
including particularly its memory/CPU ratio and time limit.

The *milan* partition is currently an exception - since it has a
different operating system version it is currently configured to be
opt-in only - your job will not land there it unless you request it.

If you do specify a partition and your job is not a good fit for that
partition then you may receive a warning, please do not ignore this.
E.g.:

    sbatch: "bigmem" is not the most appropriate partition for this job, which would otherwise default to "large". If you believe this is incorrect then please contact support@nesi.org.nz and quote the Job ID number.

 

+--------+--------+--------+--------+--------+--------+--------+--------+
| **Name | **Max  | **Node | **CPUs | **GPUs | **Avai | **Avai | **Desc |
| **     | Wallti | s**    | /Node* | /Node\ | lable  | lable  | riptio |
|        | me**   |        | *      | **     | Mem/CP | Mem/No | n**    |
|        |        |        |        |        | U**    | de**   |        |
+--------+--------+--------+--------+--------+--------+--------+--------+
| long   | 3      | 69     | 72     |        | 1500   | 105 GB | For    |
|        | weeks  |        |        |        | MB     |        | jobs   |
|        |        |        |        |        |        |        | that   |
|        |        |        |        |        |        |        | need   |
|        |        |        |        |        |        |        | to run |
|        |        |        |        |        |        |        | for    |
|        |        |        |        |        |        |        | longer |
|        |        |        |        |        |        |        | than 3 |
|        |        |        |        |        |        |        | days.  |
+--------+--------+--------+--------+--------+--------+--------+--------+
| large  | 3 days | *long* | 72     |        | 1500   | 105 GB | Defaul |
|        |        | + 157  |        |        | MB     |        | t      |
|        |        |        |        |        |        |        | partit |
|        |        |        |        |        |        |        | ion.   |
+--------+--------+--------+--------+--------+--------+--------+--------+
| milan  | 7 days | 29\    | 256\   |        | 1850   | 460    | [Curre |
|        |        |  2     | 256    |        | MB     | GB\    | ntly   |
|        |        |        |        |        |        | 960 GB | opt    |
|        |        |        |        |        | 3800   |        | in.    |
|        |        |        |        |        | MB     |        | Newer  |
|        |        |        |        |        |        |        | OS and |
|        |        |        |        |        |        |        | AMD    |
|        |        |        |        |        |        |        | Milan  |
|        |        |        |        |        |        |        | CPUs]( |
|        |        |        |        |        |        |        | https: |
|        |        |        |        |        |        |        | //supp |
|        |        |        |        |        |        |        | ort.ne |
|        |        |        |        |        |        |        | si.org |
|        |        |        |        |        |        |        | .nz/kn |
|        |        |        |        |        |        |        | owledg |
|        |        |        |        |        |        |        | e/arti |
|        |        |        |        |        |        |        | cles/5 |
|        |        |        |        |        |        |        | 286956 |
|        |        |        |        |        |        |        | 022159 |
|        |        |        |        |        |        |        | ).     |
+--------+--------+--------+--------+--------+--------+--------+--------+
| bigmem | 7 days | 6      | 72     |        | 6300   | 460 GB | Jobs   |
| /      |        |        |        |        | MB     |        | requir |
|        |        | 6      | 54     |        |        | 300 GB | ing    |
| infill |        |        |        |        | 5500   |        | large  |
|        |        |        |        |        | MB     |        | amount |
|        |        |        |        |        |        |        | s      |
|        |        |        |        |        |        |        | of     |
|        |        |        |        |        |        |        | memory |
|        |        |        |        |        |        |        | .      |
+--------+--------+--------+--------+--------+--------+--------+--------+
| hugeme | 7 days | 4      | 80\    |        | 18 GB\ | 1,500  | Jobs   |
| m      |        |        | 128\   |        | 30 GB\ | GB\    | requir |
|        |        |        | 176    |        | 35 GB  | 4,000  | ing    |
|        |        |        |        |        |        | GB\    | very   |
|        |        |        |        |        |        | 6,000  | large  |
|        |        |        |        |        |        | GB     | amount |
|        |        |        |        |        |        |        | s      |
|        |        |        |        |        |        |        | of     |
|        |        |        |        |        |        |        | memory |
|        |        |        |        |        |        |        | .      |
+--------+--------+--------+--------+--------+--------+--------+--------+
| gpu    | 3 days | 1      | 18,    | 1      | 6300   | 160    | See    |
|        |        |        | plus   | P100\* | MB     | GB,    | below  |
|        |        | 4      | 54     |        |        | plus   | for    |
|        |        |        | shared | 2      |        | 300 GB | more   |
|        |        | 2      | with   | P100\* |        | shared | info.  |
|        |        |        | *infil |        |        | with   |        |
|        |        | 2      | l*     | 1      |        | *infil |        |
|        |        |        |        | A100\* |        | l*     |        |
|        |        | 1      |        | \*     |        |        |        |
|        |        |        |        |        |        |        |        |
|        |        |        |        | 2      |        |        |        |
|        |        |        |        | A100\* |        |        |        |
|        |        |        |        | \*     |        |        |        |
|        |        |        |        |        |        |        |        |
|        |        |        |        | 7      |        |        |        |
|        |        |        |        | A100-1 |        |        |        |
|        |        |        |        | g.5gb\ |        |        |        |
|        |        |        |        | *\*\*  |        |        |        |
+--------+--------+--------+--------+--------+--------+--------+--------+

\* NVIDIA Tesla P100 PCIe 12GB cards

\*\* NVIDIA Tesla A100 PCIe 40GB cards

\*\*\* 1 NVIDIA Tesla A100 PCIe 40GB card divided into [7 MIG GPU
slices](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/)
(5GB each)

## Quality of Service

Orthogonal to the partitions, each job has a \"Quality of Service\",
with the default QoS for a job being determined by the allocation class
of its project.  There are other QoSs which you can select with the
`--qos`option:

### Debug

Specifying `--qos=debug` will give the job very high priority, but is
subject to strict limits: 15 minutes per job, and only 1 job at a time
per user. Debug jobs may not span more than two nodes.

### Interactive

Specifying `--qos=interactive` will give the job very high priority, but
is subject to some limits: up to 4 jobs, 16 hours duration, 4 CPUs, 128
GB, and 1 GPU.

## Requesting GPUs {#req_gpu}

Nodes in the `gpu` partition have 2 P100 GPU cards each, so you can
request 1 or 2 GPUs per node:

    #SBATCH --gpus-per-node=1

Some nodes in the `bigmem` partition have 1 to 2 A100 GPU cards. **If
you have been granted access** to these GPUs, you can request them
explicitly using:

    #SBATCH --gpus-per-node=A100:1

Please contact us at <support@nesi.org.nz> to learn more about getting
access to the A100 GPU cards.

See [GPU use on
NeSI](https://support.nesi.org.nz/hc/en-gb/articles/360001471955) for
more details about Slurm and CUDA settings.

### Additional limits for jobs in the `gpu` partition

-   In addition to GPUs, you can request up to four CPUs and up to 54 GB
    of RAM.
-   There is a per-project limit of 6 GPUs being used at a time.
-   There is also a per-project limit of 100 GPU-hours being allocated
    to running jobs. This allows you to use more GPUs if your jobs are
    shorter, and so guarantees that all users can at least get short
    debugging jobs on to a GPU in a reasonably timely manner. For
    example you can have: one 3-day 1-GPU job, one 2-day 2-GPU job, or 6
    GPUs used by jobs of 15 hours or less.
-   There is a limit of 1 A100-1g.5gb GPU job per user.

## Mahuika Infiniband Islands

Mahuika is divided into "islands" of 26 nodes (or 1,872 CPUs).
Communication between two nodes on the same island is faster than
between two nodes on different islands. MPI jobs placed entirely within
one island will often perform better than those split among multiple
islands.

You can request that a job runs within a single InfiniBand island by
adding:

    #SBATCH --switches=1

Slurm will then run the job within one island provided that this does
not delay starting the job by more than the maximum switch waiting time,
currently configured to be 5 minutes. That waiting time limit can be
reduced by adding `@<time>` after the number of switches e.g:

    #SBATCH --switches=1@00:30:00
