---
created_at: 2026-11-03
description: What NUMA domains are, why they matter more on Mahuika than on your desktop, how Mahuika nodes are split into them, and how to keep a job's threads and MPI tasks close to their data.
tags:
- parallel
- slurm
- openmp
- mpi
---
{#- Used by the table of node types in "NUMA domains on Mahuika". #}
{% macro size(gb) %}{% if gb >= 1000 %}{{ (gb / 1024) | round(1) }} TB{% else %}{{ gb | round | int }} GB{% endif %}{% endmacro %}
{% set gpu_names = {"pro_6000": "RTX PRO 6000", "h100": "H100", "l4": "L4", "a100": "A100"} %}

Inside a Mahuika node, some of the memory is closer to some of the cores than the rest.
If a job's work and its data end up far apart, the job can run slower than it should,
and its runtime can change from one run to the next.

## Near and far memory

A node's cores do the calculations, and its memory holds the data they work on.
A core has to fetch each number from memory before it can use it, and how long that takes depends on where the data is.
A program that uses several cores runs one thread or MPI task on each (see [Parallel Computing](Parallel_Computing.md)),
and Slurm decides which cores and memory your job gets.

Picture a node as two buildings joined by a footbridge.
Each building has four labs, and each lab has a few scientists and a fridge full of samples.
The scientists are the cores, and the fridges are the memory.

A scientist who needs a sample gets it fastest from the fridge in their own lab.
Fetching one from a lab down the corridor takes longer,
and fetching one from the other building, across the footbridge, takes longest of all.

![Two buildings joined by a footbridge, each with four labs. Every lab has a few scientists and a fridge. One scientist in lab 0 needs a sample. Path 1 goes to the fridge in their own lab and is the quickest. Path 2 goes to the fridge in lab 1, down the corridor, and is slower. Path 3 crosses the footbridge to the fridge in lab 4, in the other building, and is the slowest.](../../assets/images/NUMA_Domains_Lab_Story.svg)

In a node, each lab is a NUMA domain: a group of cores along with the part of the memory closest to them.
NUMA is short for [non-uniform memory access](https://en.wikipedia.org/wiki/Non-uniform_memory_access),
which means that some memory takes longer to reach than other memory.

## NUMA domains on Mahuika

A real node is laid out the same way.
The two buildings are the node's two sockets, each holding one processor chip,
and the link between the sockets does the job of the footbridge.

![A Genoa node laid out like the labs. Two sockets of 84 cores are joined by a socket link. Each socket is split into four NUMA domains, numbered 0 to 7, and each NUMA domain has 21 cores and its own memory.](../../assets/images/NUMA_Domains_Genoa_Node.svg)

Milan nodes are split the same way, with fewer cores in each NUMA domain.

![A Milan node laid out the same way. Two sockets of 64 cores are joined by a socket link. Each socket is split into four NUMA domains, numbered 0 to 7, and each NUMA domain has 16 cores and its own memory.](../../assets/images/NUMA_Domains_Milan_Node.svg)

The memory is shared out evenly between a node's NUMA domains.
The table below lists every type of node. [Hardware](../../Batch_Computing/Hardware.md) has more about each one.

<table>
    <thead>
        <tr><th>Partition</th><th>GPUs</th><th>Cores</th><th>Memory</th><th>NUMA domains</th><th>Cores per domain</th><th>Memory per domain</th></tr>
    </thead>
    <tbody>
{#- A row per type of node, with each cell joined to an identical one above it. #}
{%- for partition in ["genoa", "milan", "hugemem"] %}
{%- set ns = namespace(rows=[]) %}
{%- for t in slurm_limits.nodes | sort(attribute="memory_gb") | sort(attribute="cores", reverse=true) if partition in t.partitions %}
{%- set gpus %}{% for g, n in t.gpus | dictsort %}{{ n }} x {{ gpu_names.get(g, g) }}{% for f in t.features if f.startswith(g ~ "_") %} (<code>{{ f }}</code>){% endfor %}{% else %}-{% endfor %}{% endset %}
{%- set few = slurm_limits.nodes | selectattr("partitions", "eq", t.partitions) | selectattr("gpus", "eq", t.gpus) | selectattr("memory_gb", "eq", t.memory_gb) | map(attribute="usable_cores_per_numa_domain") | min %}
{%- set row = [gpus, t.cores ~ " (" ~ t.usable_cores ~ ")", size(t.memory_gb), t.numa_domains, t.cores_per_numa_domain ~ " (" ~ few ~ ")", size(t.memory_per_numa_domain_gb)] %}
{%- if row not in ns.rows %}{% set ns.rows = ns.rows + [row] %}{% endif %}
{%- endfor %}
{%- set top = ' style="border-top: .25rem double"' if partition != "genoa" else "" %}
{%- for row in ns.rows %}{% set i = loop.index0 %}
        <tr>{% if i == 0 %}<td rowspan="{{ ns.rows | length }}"{{ top }}><code>{{ partition }}</code></td>{% endif %}
{%- for c in range(6) if i == 0 or ns.rows[i - 1][c] != row[c] %}
{%- set run = namespace(n=0, on=true) %}
{%- for r in ns.rows[i:] %}{% set run.on = run.on and r[c] == row[c] %}{% set run.n = run.n + run.on %}{% endfor -%}
<td{% if run.n > 1 %} rowspan="{{ run.n }}"{% endif %}{{ top if i == 0 else "" }}>{{ row[c] }}</td>
{%- endfor %}</tr>
{%- endfor %}
{%- endfor %}
    </tbody>
</table>

Memory is what jobs can use, which is a little less than the memory installed, as some is kept back for the operating system.
Slurm also keeps a few cores on each node for the system.
They come out of one or two NUMA domains, which then have fewer cores for jobs.
The numbers in brackets are the cores jobs can use: in the whole node, and in the NUMA domain with the fewest.

## Your desktop and Mahuika

You've probably never had to think about NUMA domains on your own desktop or laptop.
Most of them have one processor, and all of their memory is the same distance from every core.

![A desktop processor and a Genoa node, drawn to the same scale. The desktop has one processor, about 4 cm across, with four memory slots on one side, all wired to the same part of the processor, so every core reaches the memory the same way and there is one NUMA domain. The Genoa node has two processors, each about 7.5 cm across and joined by a link, with six memory slots on each side of each processor. Each quarter of a Genoa processor, with its chips of cores and the memory slots wired to it, is one NUMA domain, so the node has 8.](../../assets/images/NUMA_Domains_Desktop_vs_Genoa.svg)

Mahuika's nodes are different in a few ways that can make NUMA domains matter.

- They're physically much bigger. A Genoa node has two large processors with 168 cores between them.
  The memory slots surround each processor, and each slot is wired to the part of the processor on its side,
  so the cores on that side reach it fastest.
  Memory attached to the other processor is further still, as data from it has to cross the link between the two processors.
  Every extra step on the way adds a little time.
- You often share them. Unless your job uses a whole node, other people's jobs run on the rest of it.
  Slurm gives your job cores from whatever is free, and they can end up spread over several NUMA domains.
- Jobs run for much longer, and their time is counted. If a job runs 20% slower than it could,
  a one-minute program on your laptop finishes 12 seconds later, but a two-day job on Mahuika finishes nearly ten hours later
  and uses more of your project's [allocation](../../Getting_Started/Allocations/What_is_an_allocation.md).

## When NUMA domains matter

Even on Mahuika, most jobs never need to think about NUMA domains.
They make a difference for programs that run many threads or MPI tasks and move a lot of data in and out of memory.
These jobs usually lose time in one of two ways.

![Two pictures of one Genoa socket with 4 NUMA domains. In the first, marked good and fast, a job's cores are all in NUMA domain 0 and its data is in domain 0's memory, so every fetch is from its own domain. In the second, marked bad and slower, the job's cores are spread over domains 0, 1 and 3, and most of its data is in domain 0's memory, so the cores in domains 1 and 3 fetch from another domain.](../../assets/images/NUMA_Domains_Cores_Spread.svg)

**The first is when the job's cores are spread over several NUMA domains.**
Linux stores each piece of data in the memory of the NUMA domain whose core first uses it,
so the job's data ends up spread over the memory of several domains.
Whenever a core needs data that's stored in another domain, the fetch takes longer.
Slurm doesn't guarantee that a job's cores are all in one NUMA domain, even when they would fit in one.

![Two pictures of one Genoa socket with 4 NUMA domains. In the first, marked good and fast, a thread in domain 0 stores its data in domain 0's memory, so every fetch is from its own domain. In the second, marked bad and slower, the operating system has moved the thread to domain 1, but its data is still in domain 0's memory, so every fetch now comes from another domain.](../../assets/images/NUMA_Domains_Thread_Moves.svg)

**The second is when a thread moves.**
To keep all of your job's cores evenly busy, the operating system can move a thread from one core to another.
If the new core is in another NUMA domain, the thread's data stays behind in the old domain's memory.
From then on, every fetch of that data comes from another domain's memory.

If your job's runtime changes a lot between runs with the same input, one of these may be the reason.

## Check a job's NUMA domains

To see which cores each task of your job is using, and which NUMA domains they're in,
put this command in your batch script before the line that runs your program:

```sh
srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname).\n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""
```

Each task prints a report like this one, from a task on a Genoa node:

```txt
Task #0 is running on node c001.
c001 has the following NUMA configuration:
NUMA node(s):                            8
NUMA node0 CPU(s):                       0-20,168-188
NUMA node1 CPU(s):                       21-41,189-209
NUMA node2 CPU(s):                       42-62,210-230
NUMA node3 CPU(s):                       63-83,231-251
NUMA node4 CPU(s):                       84-104,252-272
NUMA node5 CPU(s):                       105-125,273-293
NUMA node6 CPU(s):                       126-146,294-314
NUMA node7 CPU(s):                       147-167,315-335
Task #0 has 4 CPUs, their core IDs are 8-11
===========================================
```

In this report, a CPU is a core, and a NUMA node is a NUMA domain, not a whole node.

- The `NUMA node` lines list the cores in each NUMA domain.
  For example, NUMA domain 0 has cores 0 to 20.
  The numbers 168 to 188 are the same 21 cores again, as each core can run two threads at once
  (see [Simultaneous Multithreading](Simultaneous_Multithreading.md)).
- The last line lists the cores the task can use, here cores 8 to 11.

To find a task's NUMA domains, look for its cores in the `NUMA node` lines.
Cores 8 to 11 are all in NUMA domain 0, so this task is in one NUMA domain.
A task with cores 19 to 22 would be spread over two:
cores 19 and 20 are in NUMA domain 0, and cores 21 and 22 are in NUMA domain 1.

## Keep jobs in a NUMA domain

The example batch scripts below keep each task's work close to its data.
They're set up for the Genoa nodes, and [Other types of node](#other-types-of-node) says what to change for the rest.
[What the options mean](#what-the-options-mean) explains the options they use, and
[OpenMP Settings](OpenMP_Settings.md) and [Thread Placement and Thread Affinity](Thread_Placement_and_Thread_Affinity.md)
go into more detail.

!!! note "Sockets in Slurm"
    On Mahuika, Slurm treats each NUMA domain as a socket, so it shows a Genoa node as
    {{ slurm_limits.cpu_nodes.genoa.numa_domains }} sockets of {{ slurm_limits.cpu_nodes.genoa.cores_per_numa_domain }} cores rather than 2 sockets.
    When a Slurm option or Slurm's output mentions sockets, it means NUMA domains.

{% set genoa = slurm_limits.cpu_nodes.genoa %}
=== "CPU nodes"

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name         numa-mpi
    #SBATCH --account          nesi99991
    #SBATCH --time             01:00:00
    #SBATCH --partition        genoa
    #SBATCH --ntasks           8
    #SBATCH --cpus-per-task    1
    #SBATCH --mem-per-cpu      2G
    #SBATCH --cores-per-socket {{ genoa.cores_per_numa_domain }}
    #SBATCH --threads-per-core 1
    #SBATCH --distribution     *:block:*
    #SBATCH --mem-bind         local

    export OMP_PROC_BIND=true
    export OMP_PLACES=cores

    srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname).\n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""

    srun MY_PROGRAM
    ```

=== "GPU nodes"

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name         numa-gpu
    #SBATCH --account          nesi99991
    #SBATCH --time             01:00:00
    #SBATCH --gpus-per-node    h100:1
    #SBATCH --ntasks           8
    #SBATCH --cpus-per-task    1
    #SBATCH --mem-per-cpu      8G
    #SBATCH --cores-per-socket {{ genoa.cores_per_numa_domain }}
    #SBATCH --threads-per-core 1
    #SBATCH --distribution     *:block:*
    #SBATCH --mem-bind         local
    #SBATCH --gres-flags       enforce-binding
    #SBATCH --gpu-bind         closest

    export OMP_PROC_BIND=true
    export OMP_PLACES=cores

    srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname).\n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""

    srun MY_PROGRAM
    ```

### Other types of node

To run a batch script on another type of node, change these options.
The numbers come from the [table of node types](#numa-domains-on-mahuika).

- `--partition`: on a CPU node, the node's partition, such as `milan`.
- `--cores-per-socket`: the node's cores per domain, the first number rather than the one in brackets.
- `--gpus-per-node`: on a GPU node, the type of GPU, such as `a100` (see [Using GPUs](../../Batch_Computing/Using_GPUs.md)).
- `--constraint`: on an A100 node, add `--constraint a100_80gb` or `--constraint a100_40gb` to pick the type of A100.
- `--ntasks`: on a GPU node, no more than the node's cores per domain, so all the tasks fit in the GPU's NUMA domain.
  On the A100 40 GB nodes, that's 6.

### What the options mean

These options and variables keep each task, its threads and its memory in one NUMA domain.

- `--cores-per-socket` only lets the job run on nodes whose NUMA domains have at least this many cores.
  It only limits which nodes the job can use, and doesn't change how many cores it gets.
- `--threads-per-core 1` gives each task a core of its own, without [Simultaneous Multithreading](Simultaneous_Multithreading.md).
- `--distribution *:block:*` puts tasks on cores next to each other, and fills one NUMA domain before starting on the next.
  Without it, Slurm puts each task in the next NUMA domain in turn.
- `--mem-bind local` keeps each task's memory in its own NUMA domain.
- `OMP_PROC_BIND=true` pins each thread, so the operating system can't move it to another core or NUMA domain.
- `OMP_PLACES=cores` pins each thread to a whole core.
  These two only matter if you give each task more than one core with `--cpus-per-task`,
  as Slurm sets `OMP_NUM_THREADS` to that number.

The GPU batch script asks for one GPU.
These options keep the tasks next to their GPU:

- `--gres-flags enforce-binding` only gives the job cores in the NUMA domain its GPU is attached to.
  The job may wait longer to start.
- `--gpu-bind closest` gives each task the GPU in its own NUMA domain.
