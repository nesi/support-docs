---
title: VASP
created_at: '2015-09-08T03:11:50Z'
tags:
- chemistry
description: Atomic-scale materials modelling with VASP on the cluster
---

[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

The Vienna Ab initio Simulation Package (VASP) is a programme for atomic-scale materials modelling.

VASP computes an approximate solution to the many-body Schrödinger equation of a chemical system using Density Functional Theory, Hartree-Fock, or both via hybrid functionals. Periodic boundary conditions make VASP particularly useful for studying materials bulk properties.

For more information on what you can do with VASP see the [official documentation](https://www.vasp.at/info/about/).

## Examples

{% set genoa = slurm_limits.cpu_nodes.genoa %}
{% set milan = slurm_limits.cpu_nodes.milan %}

!!! warning
    Our Genoa and Milan partitions need different values of `--cores-per-socket`: {{ genoa.cores_per_numa_domain }} on Genoa and {{ milan.cores_per_numa_domain }} on Milan, the number of cores in one of their NUMA domains. See [How do we decrease the latency (and increase speed) of calculations?](#how-do-we-decrease-the-latency-and-increase-speed-of-calculations) for more information.

=== "VASP6"
    VASP6 parallelises using both MPI (`ntasks`) and OpenMP (`cpus-per-task`). The `NCORE` flag is ignored.
    The GPU node batch scripts use a GPU build of VASP6 and one MPI task per GPU (see [GPU versions of VASP6](#gpu-versions-of-vasp6)).

    === "Genoa"

        === "CPU nodes"

            ``` sl
            #!/bin/bash -e

            #SBATCH --job-name         my_VASP6_job
            #SBATCH --account          nesi12345
            #SBATCH --time             01:00:00
            #SBATCH --partition        genoa
            #SBATCH --ntasks           8
            #SBATCH --cpus-per-task    4
            #SBATCH --mem-per-cpu      1G
            #SBATCH --cores-per-socket {{ genoa.cores_per_numa_domain }}
            #SBATCH --threads-per-core 1
            #SBATCH --distribution     *:block:*
            #SBATCH --mem-bind         local
            #SBATCH --profile          task

            module purge 2> /dev/null
            module load VASP/6.5.1-foss-2023a

            export OMP_PROC_BIND=true
            export OMP_PLACES=cores

            srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname).\n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""

            srun vasp_std
            ```

        === "GPU nodes"

            ``` sl
            #!/bin/bash -e

            #SBATCH --job-name         my_VASP6_job
            #SBATCH --account          nesi12345
            #SBATCH --time             01:00:00
            #SBATCH --gpus-per-node    h100:1
            #SBATCH --ntasks           1
            #SBATCH --cpus-per-task    1
            #SBATCH --mem-per-cpu      8G
            #SBATCH --cores-per-socket {{ genoa.cores_per_numa_domain }}
            #SBATCH --threads-per-core 1
            #SBATCH --distribution     *:block:*
            #SBATCH --mem-bind         local
            #SBATCH --gres-flags       enforce-binding
            #SBATCH --gpu-bind         closest
            #SBATCH --profile          task

            module purge 2> /dev/null
            module load VASP/6.5.1-nvofbf-2023b

            export OMP_PROC_BIND=true
            export OMP_PLACES=cores

            srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname).\n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""

            srun vasp_std
            ```

    === "Milan"

        === "CPU nodes"

            ``` sl
            #!/bin/bash -e

            #SBATCH --job-name         my_VASP6_job
            #SBATCH --account          nesi12345
            #SBATCH --time             01:00:00
            #SBATCH --partition        milan
            #SBATCH --ntasks           8
            #SBATCH --cpus-per-task    4
            #SBATCH --mem-per-cpu      1G
            #SBATCH --cores-per-socket {{ milan.cores_per_numa_domain }}
            #SBATCH --threads-per-core 1
            #SBATCH --distribution     *:block:*
            #SBATCH --mem-bind         local
            #SBATCH --profile          task

            module purge 2> /dev/null
            module load VASP/6.5.1-foss-2023a

            export OMP_PROC_BIND=true
            export OMP_PLACES=cores

            srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname).\n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""

            srun vasp_std
            ```

        === "GPU nodes"

            ``` sl
            #!/bin/bash -e

            #SBATCH --job-name         my_VASP6_job
            #SBATCH --account          nesi12345
            #SBATCH --time             01:00:00
            #SBATCH --gpus-per-node    a100:1
            #SBATCH --constraint       a100_80gb
            #SBATCH --ntasks           1
            #SBATCH --cpus-per-task    1
            #SBATCH --mem-per-cpu      8G
            #SBATCH --cores-per-socket {{ milan.cores_per_numa_domain }}
            #SBATCH --threads-per-core 1
            #SBATCH --distribution     *:block:*
            #SBATCH --mem-bind         local
            #SBATCH --gres-flags       enforce-binding
            #SBATCH --gpu-bind         closest
            #SBATCH --profile          task

            module purge 2> /dev/null
            module load VASP/6.5.1-nvofbf-2023b

            export OMP_PROC_BIND=true
            export OMP_PLACES=cores

            srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname).\n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""

            srun vasp_std
            ```

=== "VASP5"
    VASP5 parallelises using MPI only (`ntasks`), so `cpus-per-task` is left at 1. The work of individual Kohn-Sham orbitals is shared across MPI processes by setting the `NCORE` flag in the `INCAR` (for example `NCORE = 4`).

    === "Genoa"

        ``` sl
        #!/bin/bash -e

        #SBATCH --job-name         my_VASP5_job
        #SBATCH --account          nesi12345
        #SBATCH --time             01:00:00
        #SBATCH --partition        genoa
        #SBATCH --ntasks           32
        #SBATCH --cpus-per-task    1
        #SBATCH --mem-per-cpu      1G
        #SBATCH --cores-per-socket {{ genoa.cores_per_numa_domain }}
        #SBATCH --threads-per-core 1
        #SBATCH --distribution     *:block:*
        #SBATCH --mem-bind         local
        #SBATCH --profile          task

        module purge 2> /dev/null
        module load VASP/5.4.4-intel-2020a

        export OMP_PROC_BIND=true
        export OMP_PLACES=cores

        srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname).\n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""

        srun vasp_std
        ```

    === "Milan"

        ``` sl
        #!/bin/bash -e

        #SBATCH --job-name         my_VASP5_job
        #SBATCH --account          nesi12345
        #SBATCH --time             01:00:00
        #SBATCH --partition        milan
        #SBATCH --ntasks           32
        #SBATCH --cpus-per-task    1
        #SBATCH --mem-per-cpu      1G
        #SBATCH --cores-per-socket {{ milan.cores_per_numa_domain }}
        #SBATCH --threads-per-core 1
        #SBATCH --distribution     *:block:*
        #SBATCH --mem-bind         local
        #SBATCH --profile          task

        module purge 2> /dev/null
        module load VASP/5.4.4-intel-2020a

        export OMP_PROC_BIND=true
        export OMP_PLACES=cores

        srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname).\n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""

        srun vasp_std
        ```

Before starting VASP, each batch script runs a `print_binding_stats` job step, which prints the CPUs and NUMA domains each task was given. [Check a job's NUMA domains](../Parallel_Computing/NUMA_Domains.md#check-a-jobs-numa-domains) explains its output.

## Licences

A VASP licence is managed at the research group level. Which versions you have access to depends on what version your research group leader has purchased. You will have access to either VASP4, VASP5, or VASP6. Minor releases are included under the major release licence, for example VASP6.?.? is available to those who have a VASP6 licence.

If your research group has a valid licence, please {% include "partials/support_request.html" %} and CC the group leader. The Support Team will grant you permission to using VASP on Mahuika. You may be asked to provide proof of your licence if you are not from a known group or if the licence is new.

## Assessing VASP Efficiency

VASP is CPU-hungry, so assessing the efficiency of your calculations is critical: it lets you perform more calculations at a lower cost. For how to begin using VASP itself, the [VASP manual](https://www.vasp.at/wiki/index.php/The_VASP_Manual) is the best place to go.

!!! note
    You only need to perform these steps on a representative system. You can assume all other similar systems will have the same optimisation parameters.

### Step 1: INCAR & KPOINTS Benchmarking

Test various parameters in your `INCAR` and `KPOINTS` files, and **choose them such that the energy of the system converges across your parameter space**: the energy does not decrease dramatically when you increase or decrease a parameter.

* If you underestimate parameters, you get the wrong energy for your system.
* If you overestimate parameters, your calculation takes longer to run, and so requires more computational resources to complete.

We have created the **[`vasp-parameter-benchmarking` tool](https://github.com/geoffreyweal/vasp-parameter-benchmarking) to help you easily choose the ideal parameters for your `INCAR` and `KPOINTS`**, such as your `ENCUT` value or whether to set `LREAL` to true or false. Its GitHub page has a guide on how to use it.

### Step 2: Core Benchmarking

VASP6 uses two technologies to parallelise calculations across CPUs:

* MPI (`ntasks` in your batch script) is the main one. It calculates the bands/orbitals in your chemical system across CPUs or groups of CPUs.
* OpenMP (`cpus-per-task` in your batch script) is secondary. It lets a group of CPUs work together to calculate a single band/orbital faster.

By changing the ratio of MPI to OpenMP, you can increase the speed of your calculation using the same number of CPUs. Determining the ideal ratio requires testing, so we have created the **[`vasp-core-benchmarking` tool](https://github.com/geoffreyweal/vasp-core-benchmarking), which sweeps across a range of `ntasks` and `cpus-per-task` values with minimal effort on your part**. It then helps you determine which values minimise the time required to perform an electronic step. Its GitHub page has a guide on how to use it, and [The theory behind VASP efficiency](#the-theory-behind-vasp-efficiency) explains how MPI and OpenMP work together.

## GPU versions of VASP6

VASP modules containing *\*-nvofbf-\** in the name have been built with GPU support (see the [OpenACC GPU port of VASP](https://www.vasp.at/wiki/index.php/OpenACC_GPU_port_of_VASP)). The [examples](#examples) include GPU batch scripts for Genoa and Milan.

VASP can run really well on GPUs, but how much you benefit depends on the specific calculation you are running. Before running larger production simulations, run some smaller benchmarks with different GPU and CPU-only configurations, and take both performance and compute unit cost into account when choosing a configuration.

See [Using GPUs](../../Batch_Computing/Using_GPUs.md) for further instructions, and [Hardware](../../Batch_Computing/Hardware.md#gpus) for full GPU specifications.

* There is no longer a `vasp_gpu` executable. The VASP executables (`vasp_std`, `vasp_gam`, `vasp_ncl`) are all built with OpenACC GPU support.
* Always select one MPI process (Slurm task) per GPU.
* If you see memory errors like `call to cuMemAlloc returned error 2: Out of memory`, you probably ran out of GPU memory. Try requesting more GPUs (so the total amount of available memory is higher), GPUs with more memory, or both. GPU memory is distinct from the memory you request for your job with `#SBATCH --mem` or similar: when you are allocated a GPU, you get access to all the GPU memory on that device.

## Useful VASP Information

* Higher levels of theory and more complicated exchange correlation functionals often require more FFTs, so they may benefit more from increasing `cpus-per-task` than from increasing `ntasks`. Test this out using the [`vasp-core-benchmarking`](https://github.com/geoffreyweal/vasp-core-benchmarking) tool.
* If you include a number of k-points in your `KPOINTS` file, try increasing `KPAR`. It sets the number of k-points calculated in parallel upon the same band/orbital, and must divide evenly into the total number of MPI processes.
* For VASP, turn [hyperthreading](../Parallel_Computing/Simultaneous_Multithreading.md) off with `--threads-per-core 1` (`2` turns it on). This is the default on Mahuika, and the example batch scripts set it.
* For visualising VASP structure files like the `POSCAR` and `CONTCAR`, use the [Atomic Simulation Environment (ASE)](https://docs.ase-lib.org/). See [ASE GUI basics](https://docs.ase-lib.org/ase/gui/basics.html) to learn more about visualising your chemical systems in ASE.

## VASP extensions

If you are wondering what extensions our VASP modules have been built with, please email the {% include "partials/support_request.html" %}. You can also check what precompiler options (used to activate/deactivate certain code features at the time of compilation) were included when the module was built by loading a module and running `vasp_std --cpp-options`.

## The theory behind VASP efficiency

This section covers in detail how MPI and OpenMP are used to increase the speed of calculations in VASP. You do not need to read it to measure VASP efficiency: it is just for interest.

### Useful Nomenclature

* *MPI (Message Passing Interface)* lets VASP spread a calculation across multiple CPUs. Crucially, *memory is not shared between CPUs*: each CPU holds its own private copy, and the CPUs coordinate by passing messages to one another.
* *OpenMP* lets a group of CPUs work on the same piece of a calculation simultaneously, where the *memory is shared between them*.
* *Rank*, *task* and *process* all mean the same thing in MPI: a single, self-contained piece of work that your program is carrying out.
* A rank is *multithreaded* when several OpenMP *threads* work on parts of it at the same time. Think of a rank as building a wall: several builders (threads) working along the wall at once finish sooner than one builder laying every brick in sequence.
* *Wavefunction*, *Kohn-Sham orbital* and *band* all refer to the same thing in VASP, since each Kohn-Sham orbital is a single-electron wavefunction. Their total number is given by `NBANDS` in the `OUTCAR`.

### How parallelisation works in VASP

In Density Functional Theory (DFT), Kohn-Sham orbitals represent the orbitals that electrons can reside in. VASP spreads the calculation of these orbitals across CPUs using two methods at once:

1. Assign CPUs to different orbitals, so that VASP calculates multiple orbitals simultaneously.
2. Assign multiple CPUs to the same orbital, so that VASP calculates a single orbital faster than with 1 CPU.

In the various versions of VASP:

* **VASP5** uses MPI for both 1 and 2, where `NCORE` sets the number of CPUs assigned to an individual orbital.
* **VASP6** uses MPI for 1 and OpenMP for 2.

### What happens when calculating an orbital in VASP

To represent the wavefunction, VASP uses a plane-wave basis set. Plane waves are naturally defined in reciprocal space (also known as k-space), where some terms of the Hamiltonian are computed, while other terms are computed in real space. Converting the plane waves between real and reciprocal space requires the [Fast Fourier Transform (FFT) algorithm](https://en.wikipedia.org/wiki/Fast_Fourier_transform).

CPUs work together on these conversions, so they need low latency: passing messages (or information) between each other, and reading memory from the RAM, in a short amount of time.

### How do we decrease the latency (and increase speed) of calculations?

Latency is lowest when CPUs that constantly communicate are close to each other, and close to the memory they are constantly reading from.

On Mahuika, each node is split into [NUMA domains](../Parallel_Computing/NUMA_Domains.md): groups of CPUs together with the part of the node's memory closest to them, which they can read faster than memory in other domains. A Genoa node has {{ genoa.numa_domains }} NUMA domains of {{ genoa.cores_per_numa_domain }} cores, and a Milan CPU node has {{ milan.numa_domains }} of {{ milan.cores_per_numa_domain }} cores ([NUMA domains on Mahuika](../Parallel_Computing/NUMA_Domains.md#numa-domains-on-mahuika) lists every type of node).

VASP loses time when its CPUs are spread over several NUMA domains, or when a thread moves to another NUMA domain and leaves its data behind (see [When NUMA domains matter](../Parallel_Computing/NUMA_Domains.md#when-numa-domains-matter)). To avoid both, the example batch scripts *pin* the tasks and threads working on each orbital to CPUs in one NUMA domain, along with the memory they read from:

=== "Genoa"

    ```sh
    #SBATCH --cores-per-socket {{ genoa.cores_per_numa_domain }}
    #SBATCH --threads-per-core 1
    #SBATCH --distribution     *:block:*
    #SBATCH --mem-bind         local

    export OMP_PROC_BIND=true
    export OMP_PLACES=cores
    ```

=== "Milan"

    ```sh
    #SBATCH --cores-per-socket {{ milan.cores_per_numa_domain }}
    #SBATCH --threads-per-core 1
    #SBATCH --distribution     *:block:*
    #SBATCH --mem-bind         local

    export OMP_PROC_BIND=true
    export OMP_PLACES=cores
    ```

Slurm treats each NUMA domain as a socket, so `--cores-per-socket` only lets your job run on nodes whose NUMA domains have at least this many cores. `--distribution *:block:*` is the crucial option: it gives VASP CPUs that are next to each other, filling one NUMA domain before starting on the next. [What the options mean](../Parallel_Computing/NUMA_Domains.md#what-the-options-mean) explains the others.

If your VASP runtime changes a lot between runs with the same input, check where your tasks were placed in the output of the `print_binding_stats` step in the [example batch scripts](#examples).

### My job is spread across different nodes — is this a problem?

Usually not, and you do not need to do anything: Slurm determines what nodes to use based on your value of `ntasks` and the availability of CPUs on Mahuika.

* The CPUs that perform FFTs together *on the same band/orbital* (those in `cpus-per-task`) must be close to each other. Slurm places them on the same node, and the options above aim to keep them in the same NUMA domain.
* The CPUs working on different bands (the groups of CPUs given by `ntasks`) do not need to be close together. It is nice to have, but not critical to performance, because the only information passed between bands/orbitals is the total charge density, which is only exchanged per electronic step. These groups can usually be safely spread across nodes.

## References

* [Basic parallelisation](https://www.vasp.at/wiki/index.php/Category:Parallelization)
* [Optimising the parallelisation](https://www.vasp.at/wiki/index.php/Optimizing_the_parallelization#Optimizing_the_parallelization)
