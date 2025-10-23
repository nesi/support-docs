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

## Description

The Vienna Ab initio Simulation Package (VASP) is a programme for atomic scale materials modelling.

VASP computes an approximate solution to the many-body Schrödinger equation of a chemical system using Density Functional Theory, Hartree-Fock, or both via hybrid functionals. Periodic boundary conditions make VASP particularly useful for studying materials bulk properties.

For more information on what you can do with VASP see the [official documentation](https://www.vasp.at/info/about/).

## Licences

A VASP license is managed at the research group level. Which versions you have access to depends on what version your research group leader has purchased. You will have access to either VASP4, VASP5, or VASP6. Minor releases are included under the major release licence, for example VASP6.?.? is available to those who have a VASP6 license.

If your research group has a valid licence, please {% include "partials/support_request.html" %} and CC the group leader. The Support Team will add the relevant permissions to your HPC UID which will allow you to access the VASP modules. You may be asked to provide proof of your license if you are not from a known group or if the license is new.

## Example script (VASP6)

Effectively parallelising your calculation is a particularly complicated aspect of VASP. VASP6 can parallelise its work using the MPI (set by `--ntasks`) and OpenMP (set by `--cpus-per-task`) protocols concurrently. VASP5 uses the MPI only.

``` sl
#!/bin/bash -e

#SBATCH --ntasks=8
#SBATCH --cpus-per-task=4
#SBATCH --job-name=my_VASP_job
#SBATCH --time=01:00:00
#SBATCH --mem-per-cpu=950
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

Another, more complex `bash` script to submit a VASP job can be downloaded with the following:

``` bash
wget https://raw.githubusercontent.com/Johnryder23/job_submit_scripts/refs/heads/main/VASP/vasp_std_HPC3_submit.sh
```

This more involved script sets up a working directory and can be used to submit CPU or CPU/GPU jobs. In most cases, only the variables under "edit job allocation settings here" need to be adjusted.

## Optimisation tips

!!! note "A note on MPI and OpenMP nomenclature"
    MPI has multiple terms which mean the same thing. A MPI *rank*, *task*, and *process* are synonymous. `#SBATCH --ntasks=n` spawns `n` MPI ranks for your job. Each of these ranks are an independent process that have [their own memory space](https://nesi.github.io/hpc-intro/064-parallel/index.html#distributed-memory-mpi). MPI ranks are *multithreaded* if each rank is given multiple OpenMP *threads*. The number of OpenMP threads is set by `#SBATCH --cpus-per-task`.

VASP is a complex programme with a steep learning curve. The [VASP manual](https://www.vasp.at/wiki/index.php/The_VASP_Manual) is the best place to go for information on how to begin using VASP. The information here relates to running VASP the Mahuika cluster specifically.

**Theory**

!!! note
    Recall the terms "wavefunction", "Kohn-Sham orbital" and "band" are equivalent in VASP as Kohn-Sham orbitals are single electron wavefunctions. The number of wavefunctions/Kohn-Sham orbitals is enumerated by `NBANDS` in the `OUTCAR`.

Kohn-Sham orbitals are distributed over available MPI ranks in a round-robin fashion until all orbitals have a processor (equivalently, a PID) - or group of processors (under a single PID) if running a multithreaded calculation. In VASP5, the work of a single orbital can be parallelised over MPI ranks using the `NCORE` [flag](https://www.vasp.at/wiki/index.php/NCORE) in the `INCAR`. In VASP6, the work of a single orbital can be parallelised across OpenMP threads. In VASP6 The `NCORE` flag will be ignored.

**In summary**

VASP5

- `NCORE` MPI processes share the work of individual Kohn-Sham orbitals.

VASP6

- `--cpus-per-task` OpenMP threads share the work of individual Kohn-Sham orbitals. Any `NCORE` setting will be ignored.

It is critically important that processors sharing the work of an orbital are *near* each other on the processor die. To understand why this is a bit of theory must be understood.

VASP uses a plane-wave basis set to represent the wavefunction. These plane-waves are naturally defined in reciprocal space. Some terms of the Hamiltonian are computed in this reciprocal space (also known as **k**-space) and other terms are computed in real-space. Converting the plane waves between real and reciprocal space requires Fast Fourier Transforms (FFTs). In fact, the computational expense of wavefunction optimisation is dominated by these FFTs. Processors sharing the work of the FFT (i.e., processors the wavefunction is parallelised over) must communicate frequently. In other words, these FFTs require frequent *all-to-all* communication.

Not all processors have equivalent access to the RAM or local cache where the wavefunctions are stored. This processor/node design is called [Non-uniform memory access (NUMA)](https://en.wikipedia.org/wiki/Non-uniform_memory_access), and is why the need for processor locality arises. Processor communication latency must be as low as possible for multithreaded VASP calculations to perform well. Under some conditions, VASP runs orders of magnitude slower if the processors are not pinned to be *near* each other. We pin processors in this way using Slurm options show in the example script above.

The Slurm options show in the example script above ensure a few things which are important for good multithreaded performance.

- bind threads working on a particular wavefunction to cores in the same NUMA domain.
- There is 1 L3 cache per-NUMA-domain. If possible, assign MPI processes to NUMA domains that no other jobs are using so the entire L3 cache is available for wavefunction storage, since reading from cache is faster than reading from RAM.

**In summary**

- VASP expresses Kohn-Sham orbitals as plane waves, i.e., uses a plane-wave basis set.
- Plane-waves are naturally defined in reciprocal space (discretised at special points, **k**).
- Other terms of the Hamiltonian must be computed in real-space. Plane waves are transformed between real and reciprocal space using FFTs.
- FFTs require frequent all-to-all communication. If the latency of this communication is high, VASP performance will be poor.

### Not all VASP calculations benefit from multithreading

Increasing `--cpus-per-task` (or `NCORE` for VASP5) will not speed up all calculations. Higher levels of theory and more complicated exchange correlation functionals bring with them more FFTs and more parallelisable work during the wavefunction optimisation. Therefore, if using hybrid functionals or doing high-precision electronic structure calculations, your calculation will likely benefit from multithreading.

It's best to do some performance testing with a fixed number of electronic and ionic steps. This can be done with the following `INCAR` settings:

``` sl
EDIFFG = 0   # do not stop based on total energy
NSW = 3      # number of ionic steps
NELMIN = 3   # minimum number of electronic self-consistency steps
NELM = 3     # maximum number of electronic self-consistency steps
```

Which will perform exactly 3 ionic and 3 electronic steps. Ensure the number of physical cores is constant while varrying the ratio of MPI ranks to OpenMP threads. For example, `--ntasks=4 --cpus-per-task=4`, `--ntasks=2 --cpus-per-task=8`, and `--ntasks=8 --cpus-per-task=2`, will all have 16 physical cores.

VASP may be further parallelised by additional `INCAR` options. For example, if you have many **k**-points it would be wise to experiment with the `KPAR` setting.

!!! warning
    KPAR must divide evenly into the total number of MPI processes.

For more information on other parallelisable quantities, see the following VASP documentation pages:

[Basic parallisation](https://www.vasp.at/wiki/index.php/Category:Parallelization)

[Optimising the parallelisation](https://www.vasp.at/wiki/index.php/Optimizing_the_parallelization#Optimizing_the_parallelization)

### Avoid hyperthreading

We have found that VASP doesn't benefit from hyperthreading and often runs slower when hyperthreading is enabled. It's best to leave Hyperthreading off as is the case in the example Slurm script above.

### GPU versions of VASP6

VASP modules containing *\*-NVHPC-\** in the name have been built with GPU support.

<https://www.vasp.at/wiki/index.php/OpenACC_GPU_port_of_VASP>

VASP can run really well on GPUs, although how much you will benefit
from GPUs largely depends on the specific simulation/calculation that
you are running. As usual, it could be useful to run some smaller benchmarks with different GPU and CPU-only
configurations in your Slurm scripts, before moving on to run larger
production simulations. When considering which configuration to use for
production you should take into account performance and compute unit
cost.

See [GPU Use](../Batch_Jobs/GPU_Use.md), for further instructions, and
[Hardware](../Batch_Jobs/Hardware.md#gpgpus) for full GPU specifications.

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

### Visualisation with Atomic Simulation Environment's GUI

It is often helpful, or necessary, to visualise your `POSCAR`,
`CONTCAR`, or other files that contain structural information. One easy
way to do this is with the Atomic Simulation Environment's (ASE) GUI.
ASE is a Python library that can script a wide variety of VASP tasks. In
particular ASE's GUI can help visualise structures, set-up supercells,
move atoms, generate `POSCAR`s, and much more. To use the GUI simply add
our latest Python version to your environment with `module load Python`.
Then, call the GUI with `ase-gui` (for a new structure), or
`ase-gui <structure_file>` to open an existing structure. For more
information on how to use ASE see their main page
[here](https://wiki.fysik.dtu.dk/ase/index.html).

## Which VASP environment module should I use?

In general, unless you require otherwise for the result consistency
with earlier work or you rely on a removed feature, we recommend the
most recent version for which you have a license.

We have previously used version suffixes such as "-BEEF" and "-VTST" to
indicate the presence of various VASP extensions, but are now moving
away from that as the number of such extensions has grown and we have
not found any disadvantage in always including them.

### VASP extensions

If you are wondering what extensions our VASP modules have been built with, please email the [Support Team](mailto:support@nesi.org.nz). You can also check what precompilier options (used to activate/deactivate certain code features at the time of compilation) were included when the module was built by loading a module and running `vasp_std --cpp-options`.
