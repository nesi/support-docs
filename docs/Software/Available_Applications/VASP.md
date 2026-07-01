---
created_at: '2015-09-08T03:11:50Z'
tags:
- chemistry
- Density Functional Theory
- Molecular Dynamics
- Computational Chemistry
title: VASP
---

[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

The Vienna Ab initio Simulation Package (VASP) is a programme for atomic scale materials modelling.

VASP computes an approximate solution to the many-body Schrödinger equation of a chemical system using Density Functional Theory, Hartree-Fock, or both via hybrid functionals. Periodic boundary conditions make VASP particularly useful for studying materials bulk properties.

For more information on what you can do with VASP see the [official documentation](https://www.vasp.at/info/about/).

## Examples

=== "VASP6"
    VASP6 parallelises using both MPI (`--ntasks`) and OpenMP (`--cpus-per-task`). The `NCORE` flag is ignored.

    ``` sl
    #!/bin/bash -e

    #SBATCH --job-name=my_VASP6_job
    #SBATCH --account=nesi99991
    #SBATCH --time=01:00:00
    #SBATCH --ntasks=8
    #SBATCH --cpus-per-task=4
    #SBATCH --mem-per-cpu=1GB
    #SBATCH --extra-node-info=1:*:1     # Restrict node selection to nodes with at least 1 completely free socket and turn off simultaneous multithreading (Hyperthreading).
    #SBATCH --distribution=*:block:*    # Bind tasks to CPUs on the same socket, and fill that socket before moving to the next consecutive socket.
    #SBATCH --mem-bind=local
    #SBATCH --profile=task

    module purge 2> /dev/null
    module load VASP/6.4.2-foss-2023a

    # update a VASP job log once the job starts running.
    echo "Job ${SLURM_JOB_ID} was submitted on $(date) from directory $(pwd)" >> ~/VASP_job_log.txt

    # Start two job steps, one that prints MPI process CPU binding and another that starts VASP.
    srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname). \n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""
    echo -e "\n====== Finished printing CPU binding information, now launching VASP ======\n"

    srun vasp_std
    ```

=== "VASP5"
    VASP5 parallelises using MPI only (`--ntasks`), so `--cpus-per-task` is left at 1. The work of individual Kohn-Sham orbitals is shared across MPI processes by setting the `NCORE` flag in the `INCAR` (for example `NCORE = 4`).

    ``` sl
    #!/bin/bash -e

    #SBATCH --job-name=my_VASP5_job
    #SBATCH --account=nesi99991
    #SBATCH --time=01:00:00
    #SBATCH --ntasks=32
    #SBATCH --cpus-per-task=1
    #SBATCH --mem-per-cpu=1GB
    #SBATCH --extra-node-info=1:*:1     # Restrict node selection to nodes with at least 1 completely free socket and turn off simultaneous multithreading (Hyperthreading).
    #SBATCH --distribution=*:block:*    # Bind tasks to CPUs on the same socket, and fill that socket before moving to the next consecutive socket.
    #SBATCH --mem-bind=local
    #SBATCH --profile=task

    module purge 2> /dev/null
    module load VASP/5.4.4-intel-2018b

    # update a VASP job log once the job starts running.
    echo "Job ${SLURM_JOB_ID} was submitted on $(date) from directory $(pwd)" >> ~/VASP_job_log.txt

    # Start two job steps, one that prints MPI process CPU binding and another that starts VASP.
    srun --job-name=print_binding_stats bash -c "echo -e \"Task #\${SLURM_PROCID} is running on node \$(hostname). \n\$(hostname) has the following NUMA configuration:\n\$(lscpu | grep -i --color=none numa)\nTask #\${SLURM_PROCID} has \$(nproc) CPUs, their core IDs are \$(taskset -c -p \$\$ | awk '{print \$NF}')\n===========================================\""
    echo -e "\n====== Finished printing CPU binding information, now launching VASP ======\n"

    srun vasp_std
    ```

## Licences

A VASP license is managed at the research group level. Which versions you have access to depends on what version your research group leader has purchased. You will have access to either VASP4, VASP5, or VASP6. Minor releases are included under the major release licence, for example VASP6.?.? is available to those who have a VASP6 license.

If your research group has a valid licence, please {% include "partials/support_request.html" %} and CC the group leader. The Support Team will add the relevant permissions to your HPC UID which will allow you to access the VASP modules. You may be asked to provide proof of your license if you are not from a known group or if the license is new.

## Assessing VASP Efficiency

VASP is a very CPU hungry piece of software. Therefore, being able to assess your VASP calculation's efficiency is critical and can allow you perform more calculations for less price. In general, the [VASP manual](https://www.vasp.at/wiki/index.php/The_VASP_Manual) is the best place to go for information on how to begin using VASP.

Below covers the steps to take to best optimise the efficiency of your VASP calculation(s).

!!! note
    You only need to perform these steps on a representative system. You can assume all other similar systems will have the same optimisation parameters.

### Step 1: INCAR & KPOINTS Benchmarking

The first step to optimising your system in VASP is to test various parameters in your `INCAR` and `KPOINTS` files. Here you want to **choose your parameters such that the energy of the system converges across your parameter space**. This means that the energy of your system does not decrease dramatically by increasing/decreasing a parameter of your `INCAR`/`KPOINTS` file. The purpose of doing this is that:

* You do not want to under-estimate parameters such that you get the wrong energy for your system, but
* You do not want to over-estimate parameters such that your calculation takes longer to run (and thus requires more computational resources to complete).

To figure out what the best `INCAR` (and `KPOINTS`) parameters to use, we have created the **`vasp-parameter-benchmarking` tool to help you easily choose the ideal parameters for your `INCAR` and `KPOINTS`**. This can include setting up your `ENCUT` value, determining whether to set `LREAL` to true or false, etc.

* See the [`vasp-parameter-benchmarking` Github page](https://github.com/geoffreyweal/vasp-parameter-benchmarking) for a guide on how to use the `vasp-parameter-benchmarking` tool to optimise your `INCAR` and `KPOINTS` files for your system. 

### Step 2: Core Benchmarking

VASP 6 uses two technologies to parallelise calculations across CPUs. These are:

* MPI (`ntasks` in your slurm script): This is the main way that tasks are parallelised over CPUs or groups of CPUs.
* OpenMP (`cpus-per-task` in your slurm script): This is a secondary method of parallelising such that a group of CPU work together on a single task. 

VASP 6 uses MPI and OpenMP in different ways to speed up your calculation

* MPI (`ntasks`) is used to calculate each band/orbital in your chemical system.
* OpenMP (`cpus-per-task`) is used to allow a group of CPUs to increase the speed of calculating a single band/orbital in your chemical system.

By changing the ratio of MPI/OpenMP used, you can increase the speed of your calculation using the same number of CPUs. 

Determining the ideal ratio of MPI/OpenMP requires testing. To make it easier to perform all these tests, we have created the `vasp-core-benchmarking` tool. **The  `vasp-core-benchmarking` tool is designed to sweep across a region of `ntasks` and `cpus-per-task` values with minimal effort on your part**. This tool then helps you determine which values of `ntasks` and `cpus-per-task` minimise the time required to perform an electronic step. 

* See the [`vasp-core-benchmarking` Github page](https://github.com/geoffreyweal/vasp-benchmarking) for a guide on how to use the `vasp-core-benchmarking` tool to optimise your values of `ntasks` and `cpus-per-task` in your slurm script.

## The theory behind VASP efficiency

In this section, we will cover in detail how MPI and OpenMP are used to increase the speed of calculations in VASP. 

### Useful Nomenclature

* *MPI (Message Passing Interface)*: The technology that lets VASP spread a calculation across multiple CPUs. Crucially, *memory is not shared between CPUs* — each CPU holds its own private copy, and the CPUs coordinate by passing messages to one another.
* *OpenMP*: A technology that lets a group of CPUs work on the same piece of a calculation simultaneously, where the *memory is shared between them*.
* In MPI you will come across the words *rank*, *task*, and *process* — these all mean the same thing. A rank/task/process is a single, self-contained piece of work that your program is carrying out.
* A rank can be broken down further so that parts of it are worked on at the same time. When it is, we call the rank *multithreaded*: it contains several OpenMP *threads* that work on it simultaneously.
    * Think of a rank as building a wall. Rather than one builder laying every brick in sequence, several builders (threads) can work along the wall at once, so the job finishes sooner.

* In VASP, the terms *wavefunction*, *Kohn-Sham orbital*, and *band* all refer to the same thing, since each Kohn-Sham orbital is a single-electron wavefunction. Their total number is given by `NBANDS` in the `OUTCAR`.

### How Parallelisation works in VASP

In Density Functional Theory (DFT), Kohn-Sham orbitals represent the orbitals that electrons can reside in. VASP uses multiple CPUs to perform the calculations across all the Kohn-Sham orbitals in a chemical system. There are two main methods used concurrently to use CPUs to calculate Kohn-Sham orbitals  

1. Assign CPUs to different orbitals. This allows VASP to calculate multiple orbitals simultaneously. 
2. Assign multiple CPUs to the same orbital. This allows VASP to calculate a single orbital faster than just using 1 orbital.  

In the various versions of VASP:

* In **VASP 5**: MPI (Message Passing Interface) is used for both 1 and 2, where `NCORE` determines the number of CPUs assigned to 1 orbital.
* In **VASP 6**: MPI is used for 1, while OpenMP is used for 2. 

### What happens when calculating an orbital in VASP

VASP uses a plane-wave basis set to represent the wavefunction. These plane-waves are naturally defined in reciprocal space. Some terms of the Hamiltonian are computed in this reciprocal space (also known as k-space) and other terms are computed in real-space. Converting the plane waves between real and reciprocal space requires the [Fast Fourier Transform (FFT) algorithm](https://en.wikipedia.org/wiki/Fast_Fourier_transform).

CPUs work together to convert the Hamiltonian between real and reciprocal space. Because of this, they need to be very good at passing messages (or information) between each other, as well as reading memory from the RAM. The measure of "very good" is low latency, i.e. pass messages and read memory in a short amount of time. 

### How do we decrease the latency (and increase speed) of calculations?

The best way to decrease the latency of a calculation is to:

1. Decrease the distance between CPUs that constantly communicate with each other, and
2. Decrease the distance between the CPU and the memory it is constantly reading from.

To do this, we can assign or *pin* orbitals to CPUs that are close to each other and the memory they read from on the physical die. 

On Mahuika, our dies contain [Non-uniform memory access (NUMA)](https://en.wikipedia.org/wiki/Non-uniform_memory_access) domains. These NUMA domains contain a small group of CPUs as well as a small amount of very fast memory that lie near each other (this very fast memory is called L3 cache). We can make sure that our calculations run with low latency by pinning orbitals to a NUMA or several nearby NUMA domains. This is done by Slurm using the following commands:

```sl
#SBATCH --extra-node-info=1:*:1     # Restrict node selection to nodes with at least 1 completely free socket and turn off simultaneous multithreading (Hyperthreading).
#SBATCH --distribution=*:block:*    # Bind tasks to CPUs on the same socket, and fill that socket before moving to the next consecutive socket.
```

Here, `--distribution=*:block:*` crucially makes slurm assign CPUs to VASP that are as close as possible. We note that other jobs are likely to also be running on the die at the same time on Mahuika, so Slurm does this as best as possible considering the circustances.

### Some CPUs do not need to lie as close to each other as others 

It is critical that those CPUs that are performing FFTs together *on the same band/orbital* be close to each other. These are those CPUs involved in `--cpus-per-task`.

Those CPUs that are performing calculations on different bands do not necessarily need to be close together. It's a nice to have, but not critical to performance. This is because the only information that needs to be passed between bands/orbtials is the total charge density, which only needs to be exchanged per electronic step.

### My job is spread across different nodes, is this a problem

By using the `cpus-per-task` tag in slurm, those CPUs that need to be in constant communication with each other will located on the same node (and using the `--extra-node-info=1:*:1` and `--distribution=*:block:*` tags will hopefully be located on the same NUMA domain). The groups of CPUs (given by `ntasks`) can (usually) be safety spread across nodes if needed.

* **You do not need to do anything**: Slurm will determine what nodes to use based on your value of `ntasks` and the availability of CPUs on Mahuika. 

## Useful VASP Information

* Higher levels of theory and more complicated exchange correlation functionals often require more FFTs. For this reason, you may find that these functionals benefit from increasing `cpus-per-task` (compared with increasing `ntasks`). Again, test this out using the [`vasp-core-benchmarking`](https://github.com/geoffreyweal/vasp-benchmarking) tool. 
* If you include a number of **k**-points in your `KPOINTS` file, you could try increasing the number of kpoint calculations that are done in parallel. This is controlled by `KPAR`, where increasing `KPAR` increases the number of kpoints being performed in parallel upon the same band/orbital. 

!!! note
    KPAR must divide evenly into the total number of MPI processes.

* If you come across `--threads-per-core=1` or `--threads-per-core=2`, this indicates whether you want to use [hyperthreading or not](https://docs.nesi.org.nz/Software/Parallel_Computing/Simultaneous_Multithreading/). For VASP, turn hyperthreading off (i.e. set `--threads-per-core=1`. This is the default on Mahuika). 
* For visualising structures from ASE like the `POSCAR`, `OSZICAR`, etc, use the [Atomic Simulation Environment (ASE)](https://docs.ase-lib.org/). See [ASE GUI basics](https://docs.ase-lib.org/ase/gui/basics.html) to learn more about visualising your chemical systems in ASE. 

## VASP extensions

If you are wondering what extensions our VASP modules have been built with, please email the [Support Team](mailto:support@nesi.org.nz). You can also check what precompilier options (used to activate/deactivate certain code features at the time of compilation) were included when the module was built by loading a module and running `vasp_std --cpp-options`.

## References

* Basic parallisation: https://www.vasp.at/wiki/index.php/Category:Parallelization
* Optimising the parallelisation: https://www.vasp.at/wiki/index.php/Optimizing_the_parallelization#Optimizing_the_parallelization


## GPU versions of VASP6 (to edit)

VASP modules containing *\*-NVHPC-\** in the name have been built with GPU support.

<https://www.vasp.at/wiki/index.php/OpenACC_GPU_port_of_VASP>

VASP can run really well on GPUs, although how much you will benefit
from GPUs largely depends on the specific simulation/calculation that
you are running. As usual, it could be useful to run some smaller benchmarks with different GPU and CPU-only
configurations in your Slurm scripts, before moving on to run larger
production simulations. When considering which configuration to use for
production you should take into account performance and compute unit
cost.

See [Using GPUs](../../Batch_Computing/Using_GPUs.md), for further instructions, and
[Hardware](../../Batch_Computing/Hardware.md#gpgpus) for full GPU specifications.

Some additional notes specific to running VASP on GPUs:

- There is no longer a `vasp_gpu` executable. The VASP executables (`vasp_std`, `vasp_gam`, `vasp_ncl`) are all built with OpenACC GPU support.
- Always select one MPI process (Slurm task) per GPU.
- if you see memory errors like
    `call to cuMemAlloc returned error 2: Out of memory` you
    probably ran out of GPU memory. You could try requesting more
    GPUs (so the total amount of available memory is higher) and/or
    moving to GPUs with more memory (note: GPU memory is distinct
    from the usual memory you have to request for your job via
    `#SBATCH --mem` or similar; when you are allocated a GPU you get
    access to all the GPU memory on that device)
