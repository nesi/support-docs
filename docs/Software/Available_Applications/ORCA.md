---
title: ORCA
created_at: '2015-11-09T21:20:24Z'
tags:
- chemistry
vote_count: 6
vote_sum: 4
description: ORCA quantum chemistry on Mahuika, with example batch scripts, NUMA settings, benchmarking and checkpointing
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

ORCA is a flexible, efficient and easy-to-use general purpose tool for
quantum chemistry with specific emphasis on spectroscopic properties of
open-shell molecules. It features a wide variety of standard quantum
chemical methods ranging from semiempirical methods to DFT to single-
and multireference correlated *ab initio* methods. It can also treat
environmental and relativistic effects.

The ORCA home page is
at [https://orcaforum.kofo.mpg.de](https://orcaforum.kofo.mpg.de)

## Licensing requirements

ORCA is released as precompiled binaries at no cost, pursuant to a
closed-source licence.  Users are advised that the terms of [the ORCA
licence](https://orcaforum.kofo.mpg.de/app.php/dlext/?view=detail&df_id=41)
allow its use in the course of academic research only, and that each
research group is expected to register with the ORCA developers. If you
have any questions regarding your eligibility to access ORCA or any
particular version of it, please  {% include "partials/support_request.html" %}.

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

Your input file must ask for the same number of cores as `--ntasks`
(see [Requesting a parallel run](#requesting-a-parallel-run)).
To choose that number, see [Benchmark your ORCA jobs](#benchmark-your-orca-jobs).

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

## Further notes

### Requesting a parallel run

ORCA must be told how many cores to use in its input file, as well as in the batch script.
Add a line like this to the input file:

``` sh
%pal nprocs 16 end
```

Replace `16` with the number you gave `--ntasks`.

### Checkpointing

!!! warning "Checkpointing"
     We strongly recommend the use of [checkpointing](../../Batch_Computing/Job_Checkpointing.md) for any job running for more than a day.

ORCA provides for saving of checkpoint data, especially molecular
orbital information, in a file with extension ".gbw" (short for
Geometry-Basis-Wavefunction). Given an input filename of "foo.inp" or
some equivalent, the GBW file will be named "foo.gbw". The GBW file,
like temporary and other output files, will be written in the same
directory from which the ORCA executable is invoked.

To restart from an existing GBW file, you should do the following:

1. Ensure that the GBW file you want to start from is renamed so that
    it does not have the same base name as your intended input file.
    Otherwise, it will be overwritten and destroyed as soon as ORCA
    starts running.
2. In your input file, specify the following lines, replacing
    "checkpoint.gbw" with the name of the GBW file you intend to read
    from:

    ``` sh
    ! moread
    % moinp "checkpoint.gbw"
    ```

3. Run the calculation.

For more information about restarting from an older GBW file, including
how to restart from GBW files produced using earlier versions of ORCA,
please consult the ORCA manual.
