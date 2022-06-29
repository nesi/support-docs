> ### Important {#prerequisites}
>
> Partitions on these systems that may be used for NeSI workloads carry
> the prefix **nesi\_**.

 
-

Definitions
-----------

**CPU** - A logical core, also known as a hardware thread. Referred to
as a \"CPU\" in the Slurm documentation.  Since
[Hyperthreading](https://support.nesi.org.nz/hc/en-gb/articles/360000568236/)
is enabled, there are two CPUs per physical core, and every task--- and
therefore every job --- is allocated an even number of CPUs.

**Job:** A running batch script and any other processes which it might
launch with *srun*.

**Node: **A single computer within the cluster with its own CPUs and RAM
(memory), and sometimes also GPUs. A node is analogous to a workstation
(desktop PC) or laptop.

**Walltime: **Real world time, as opposed to CPU time (walltime x CPUs).

 
-

Māui (XC50) Slurm Partitions
----------------------------

Nodes are not shared between jobs on Māui, so the minimum charging unit
is node-hours, where 1 node-hour is 40 core-hours, or 80 Slurm
CPU-hours.

There is only one partition available to NeSI jobs:

+-----------+-----------+-----------+-----------+-----------+-----------+
| ** Name * | **Nodes** | **Max     | **Avail / | **Max /   | **Descrip |
| *         |           | Walltime* | Node**    | Account** | tion**    |
|           |           | *         |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| nesi\_res | 316       | 24 hours  | 80 CPUs   | 240 nodes | Standard  |
| earch     |           |           |           |           | partition |
|           |           |           | 90 or 180 | 1200      | for all   |
|           |           |           | GB RAM    | node-hour | NeSI      |
|           |           |           |           | s         | jobs.\    |
|           |           |           |           | running   | \         |
+-----------+-----------+-----------+-----------+-----------+-----------+

### Limits

As a consequence of the above limit on the node-hours reserved by your
running jobs (*GrpTRESRunMins* in Slurm documentation, shown in `squeue`
output when you hit it as the reason \"*AssocGrpCPURunMinutes\"* ) you
can occupy more nodes simultaneously if your jobs request a shorter time
limit:

  ----------- ----------- ---------------- ----------------------------
  **nodes**   **hours**   **node-hours**   **limits reached**
  1           24          24               24 hours
  50          24          1200             1200 node-hours, 24 hours
  100         12          1200             1200 node-hours
  240         5           1200             1200 node-hours, 240 nodes
  240         1           240              240 nodes 
  ----------- ----------- ---------------- ----------------------------

Most of the time [job
priority](https://support.nesi.org.nz/hc/en-gb/articles/360000201636) will
be the most important influence on how long your jobs have to wait - the
above limits are just backstops to ensure that Māui\'s resources are not
all committed too far into the future, so that debug and other
higher-priority jobs can start reasonably quickly.

### Debug QoS

Each job has a \"QoS\", with the default QoS for a job being determined
by the [allocation
class](https://support.nesi.org.nz/hc/en-gb/articles/360000202535-Overview)
of its project. Specifying `--qos=debug` will override that and give the
job very high priority, but is subject to strict limits: 15 minutes per
job, and only 1 job at a time per user. Debug jobs are limited to 2
nodes.[]{#_Toc514341606}

 
-

Māui\_Ancil (CS500) Slurm Partitions
------------------------------------

 

+---------+---------+---------+---------+---------+---------+---------+
| **Name* | **Nodes | **Max   | **Avail | **Max / | **Max / | **Descr |
| *       | **      | Walltim | /       | Job**   | User**  | iption* |
|         |         | e**     | Node**  |         |         | *       |
+---------+---------+---------+---------+---------+---------+---------+
| nesi\_p | 4       | 24      | 80 CPUs | 20 CPUs | 80 CPUs | Pre and |
| repost  |         | hours   |         |         |         | post    |
|         |         |         | 720 GB  | 700 GB  | 700 GB  | process |
|         |         |         | RAM     | RAM     | RAM     | ing     |
|         |         |         |         |         |         | tasks.  |
+---------+---------+---------+---------+---------+---------+---------+
| nesi\_g | 4 to 5  | 72      | 4 CPUs  | 4 CPUs  | 4 CPUs  | GPU     |
| pu      |         | hours   |         |         |         | jobs    |
|         |         |         | 12 GB   | 12 GB   | 12 GB   | and vis |
|         |         |         | RAM     | RAM     | RAM     | ualisat |
|         |         |         |         |         |         | ion.    |
|         |         |         | 1 P100  | 1 P100  | 1 P100  |         |
|         |         |         | GPU\*   | GPU     | GPU     |         |
+---------+---------+---------+---------+---------+---------+---------+
| nesi\_i | 0 to 1  | 2 hours | 4 CPUs  | 4 CPUs  | 4 CPUs  | Interac |
| gpu     |         |         |         |         |         | tive    |
|         |         |         | 12 GB   | 12 GB   | 12 GB   | GPU     |
|         |         |         | RAM     | RAM     | RAM     | access  |
|         |         |         |         |         |         | 7am -   |
|         |         |         | 1 P100  | 1 P100  | 1 P100  | 8pm.    |
|         |         |         | GPU\*   | GPU     | GPU     |         |
+---------+---------+---------+---------+---------+---------+---------+

\* NVIDIA Tesla P100 PCIe 12GB card

### Requesting GPUs {#req_gpu}

Nodes in the `nesi_gpu` partition have 1 P100 GPU card each. You can
request it using:

    #SBATCH --partition=nesi_gpu
    #SBATCH --gpus-per-node=1

Note that you need to specify the name of the partition.  You also need
to specify a number of CPUs and amount of memory small enough to fit on
these nodes.

See [GPU use on
NeSI](https://support.nesi.org.nz/hc/en-gb/articles/360001471955) for
more details about Slurm and CUDA settings.

 
