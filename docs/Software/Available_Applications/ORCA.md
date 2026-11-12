---
title: ORCA
created_at: '2015-11-09T21:20:24Z'
tags:
- chemistry
vote_count: 6
vote_sum: 4
description: Run ORCA quantum chemistry on Mahuika, with example batch scripts, input file settings for cores and memory, NUMA settings, benchmarking and checkpointing
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

## Licensing requirements

ORCA is free, closed-source software, released as precompiled binaries.
Its licence allows it to be used for academic research only,
and each research group is expected to register with the ORCA developers.
If you're unsure whether you can use ORCA, or a particular version of it, {% include "partials/support_request.html" %}.

## Example batch scripts

{% set genoa = slurm_limits.cpu_nodes.genoa %}
{% set milan = slurm_limits.cpu_nodes.milan %}

These batch scripts run ORCA on 16 cores.
Use the one for your partition, as `--cores-per-socket` differs (see [NUMA settings](#numa-settings)).

=== "Genoa"

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name         ORCA_job
    #SBATCH --account          nesi99991
    #SBATCH --time             01:00:00
    #SBATCH --partition        genoa
    #SBATCH --ntasks           16
    #SBATCH --mem-per-cpu      1G
    #SBATCH --cores-per-socket {{ genoa.cores_per_numa_domain }}
    #SBATCH --threads-per-core 1
    #SBATCH --distribution     *:block:*
    #SBATCH --mem-bind         local

    module purge
    module load ORCA/{{ applications.ORCA.default }}

    export OMP_PROC_BIND=true
    export OMP_PLACES=cores

    srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname).\n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""

    # ORCA must be called by its full path
    orca_exe=$(which orca)

    # Don't use srun here: ORCA starts its own MPI processes
    ${orca_exe} MyInput.inp
    ```

=== "Milan"

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name         ORCA_job
    #SBATCH --account          nesi99991
    #SBATCH --time             01:00:00
    #SBATCH --partition        milan
    #SBATCH --ntasks           16
    #SBATCH --mem-per-cpu      1G
    #SBATCH --cores-per-socket {{ milan.cores_per_numa_domain }}
    #SBATCH --threads-per-core 1
    #SBATCH --distribution     *:block:*
    #SBATCH --mem-bind         local

    module purge
    module load ORCA/{{ applications.ORCA.default }}

    export OMP_PROC_BIND=true
    export OMP_PLACES=cores

    srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname).\n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""

    # ORCA must be called by its full path
    orca_exe=$(which orca)

    # Don't use srun here: ORCA starts its own MPI processes
    ${orca_exe} MyInput.inp
    ```

Replace the following:

- `nesi99991` with your project code.
- `MyInput.inp` with your ORCA input file.

## Input file settings

Your ORCA input file must set the number of cores, and the memory for each core in MB:

```txt
%pal nprocs 16 end
%maxcore 800
```

- Set `nprocs` to the value of `--ntasks`.
    To choose it, see [Benchmark your ORCA jobs](#benchmark-your-orca-jobs).
- Set `%maxcore` to about 80% of `--mem-per-cpu`, as ORCA can use more memory than `%maxcore`
    (see ORCA's [Memory Settings](https://www.faccts.de/docs/orca/6.1/tutorials/first_steps/memory.html)).

## NUMA settings

Each Mahuika node is split into [NUMA domains](../Parallel_Computing/NUMA_Domains.md):
groups of cores with the memory closest to them.
If your job's cores are spread over several NUMA domains, ORCA can run slower, and its runtime can vary between runs
(see [When NUMA domains matter](../Parallel_Computing/NUMA_Domains.md#when-numa-domains-matter)).
The example batch scripts have settings to avoid this:

- The last four `#SBATCH` options ask Slurm for cores next to each other, filling one NUMA domain before the next.
- The two `export` lines stop threads moving between cores.

[What the options mean](../Parallel_Computing/NUMA_Domains.md#what-the-options-mean) explains each one.
Only `--cores-per-socket` depends on the partition.
It's the number of cores in one NUMA domain, which Slurm treats as a socket:
{{ genoa.cores_per_numa_domain }} on Genoa and {{ milan.cores_per_numa_domain }} on Milan.

Before starting ORCA, each batch script runs a `print_binding_stats` step,
which prints the cores each task was given and the node's NUMA domains.
[Check a job's NUMA domains](../Parallel_Computing/NUMA_Domains.md#check-a-jobs-numa-domains) explains its output.
If your runtime varies a lot between runs with the same input,
check this output for cores spread over several NUMA domains.

## Benchmark your ORCA jobs

Past a certain number of cores, more cores add little speed, but still use up your project's
[allocation](../../Getting_Started/Allocations/What_is_an_allocation.md).
To find that number for your calculation, use the
[ORCA benchmarking tool](https://github.com/geoffreyweal/orca-benchmarking).
It runs one calculation on a range of core counts, then reports how its speed and CPU efficiency change.
Its GitHub page explains how to install and use it.

You only need to benchmark one calculation that is typical of those you plan to run.

## Checkpointing

!!! warning
    Use [checkpointing](../../Batch_Computing/Job_Checkpointing.md) for any job that runs for more than a day.

ORCA saves checkpoint data, mainly the molecular orbitals, in a GBW (geometry, basis, wavefunction) file.
For the input file `MyInput.inp`, it's `MyInput.gbw`, in the directory ORCA runs in.

To restart from a GBW file:

1. Rename the GBW file so its name differs from your input file's, for example to `checkpoint.gbw`.
    Otherwise ORCA overwrites it as soon as it starts.
2. Add these lines to your input file:

    ```txt
    ! moread
    %moinp "checkpoint.gbw"
    ```

3. Run the calculation.

To restart from a GBW file made by an older version of ORCA, see
[restarting calculations](https://orca-manual.mpi-muelheim.mpg.de/contents/essentialelements/initialguess.html#restarting-scf-calculations)
in the ORCA manual.
