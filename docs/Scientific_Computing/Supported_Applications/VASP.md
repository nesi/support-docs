---
created_at: '2015-09-08T03:11:50Z'
tags:
- chemistry
- Density Functional Theory
- Molecular Dynamics
- Computational Chemistry
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

## Description

The Vienna Ab initio Simulation Package (VASP) is a programme for atomic
scale materials modelling.

VASP computes an approximate solution to the many-body Schrödinger
equation of a chemical system using Density Functional Theory or Hartree-Fock, or both (hybrid functionals). Periodic boundary conditions make VASP particularly useful for studying the bulk-like properties of materials.

For more information on what you can do with VASP see the (official documentation)[https://www.vasp.at/info/about/].


## Availability

VASP is currently available on the Mahuika cluster.

## Licences

A VASP license is managed at the reasearch group level. Which versions you have access to depends on what version your reasearch group leader has purchased. You will have access to either VASP4, VASP5, or VASP6. Minor releases are included under the major release license, for example VASP6.?.? is available to those who have a VASP6 license.

If your research group has a valid license, please {% include "partials/support_request.html" %} and CC the group leader. NeSI support will add the relevent permissions to your NeSI UID which will allow you to access the VASP modules. You may be asked to provide proof of your license if you
are not from a known group or if the license is new.

## Tips for running your VASP calculations

Parallelising your VASP calculation appropriately requires some thought and testing. VASP6 and newer impliments OpenMP parallelisation.

### Example script

``` sl
#!/bin/bash -e

#SBATCH --job-name        MyVASPJob
#SBATCH --time            01:00:00
#SBATCH --nodes           1
#SBATCH --ntasks          16               # start 16 MPI tasks
#SBATCH --mem             20G
#SBATCH --hint            nomultithread

module purge
module load VASP/6.4.1-intel-2022a

# Use the -K switch so that, if any of the VASP processes exits with an
# error, the entire job will stop instead of continuing to waste core
# hours on a defunct run.
srun -K1 vasp_std
```

### Avoid hyperthreading

We and several researchers have found that VASP doesn't behave well with
hyperthreading, and will run at a third to a half of its expected speed.
To disable hyperthreading, please use either

``` bash
#SBATCH --hint nomultithread
```

or, equivalently,

``` bash
#SBATCH --hint=nomultithread
```

as shown in our example script above.

### How many cores should I request?

Unsurprisingly, the number of cores used in a VASP calculation
significantly influences on how long the calculation takes to finish.
The more cores a problem can parallelise over, the more it can do at
once. However, this parallelisation carries with it some communication
costs. Too many cores for too small a problem can decrease efficiency
and speed (not to mention waste resources), as the cost of communicating
tasks/threads becomes greater than the cost of the calculation itself.

To determine an appropriate number of cores to request for a VASP
calculation, it helps to know how VASP distributes its work. VASP
parallelises its workload by allocating each KS orbital (enumerated by
[`NBANDS`](https://www.vasp.at/wiki/index.php/NBANDS)) to the available
cores in a round-robin fashion. In other words, each band is allocated
to a single MPI task sequentially until all bands are assigned (more
details on MPI are provided later). Each core must be allocated at least
one orbital, and ideally will have “a small integer” (2-8) orbitals to
work on. As a rule of thumb, requesting 1/8th the number of
[`NBANDS`](https://www.vasp.at/wiki/index.php/NBANDS) is a reasonable
starting point which hopefully achieves this 2 to 8 bands-per-core
suggestion.

Requesting cores is best done with `--ntasks` in your Slurm script. To
determine the value of
[`NBANDS`](https://www.vasp.at/wiki/index.php/NBANDS) (and other
parameters such as the number of **k**-points), you can perform a “dry
run” of your calculation by setting `ALGO=None` in the `INCAR`. This
will set up the calculation, but does not go into solving ionic or
electronic loops. The calculation will finish quickly, and you can then
pull the value of [`NBANDS`](https://www.vasp.at/wiki/index.php/NBANDS)
from the `OUTCAR`.

### Fill a node before working across nodes

You may find that packing your entire job onto a single node will make
it run faster. Distributing a job across multiple nodes may also put the
job at greater risk of node failure. You can request a single node with
`--nodes=1`for jobs of up to `--ntasks=128`, which is enough for most
VASP calculations. If you would like help making a large job more
efficient, please contact our support
team {% include "partials/support_request.html" %}.

### VASP runs faster on Milan nodes

[Milan compute nodes](../../Scientific_Computing/Batch_Jobs/Milan_Compute_Nodes.md)
are not only our most powerful compute nodes, but often have shorter
queues! These nodes are still opt-in at the moment, meaning you need to
specify `--partition=milan` in your Slurm script, which we strongly
encourage everyone to do!

### MPI and OpenMP with VASP

VASP6 can now parallelise work using the message passing interface (MPI)
*and* OpenMP at the same time. Where MPI parallelises on a per-orbital
basis, OpenMP can create multiple threads of work nested within an MPI
task, and so is a lower level, intra-node, form of communication. In
other words, OpenMP parallelises/distributes the work of a single
orbital. If you have large functions (for example, many plane waves and
a small number of bands), you may wish to experiment with assigning
multiple threads to each MPI task. This can be done by setting
`--cpus-per-task=2` - which will start 2 OpenMP threads for everyone 1
MPI task.

VASP may be further parallelised by treating **k**-points in parallel
(controlled with [`KPAR`](https://www.vasp.at/wiki/index.php/KPAR)), and
parallelisation the FFTs (controlled with
[`NPAR`](https://www.vasp.at/wiki/index.php/NPAR) for VASP5 only). To
optimise your VASP job parallelisation in these ways, see the following
links:

[Basic
parallisation](https://www.vasp.at/wiki/index.php/Category:Parallelization)

[Optimising the
parallelisation](https://www.vasp.at/wiki/index.php/Optimizing_the_parallelization#Optimizing_the_parallelization)

### Our VASP5 modules do not support OpenMP

Our VASP5 modules do not support OpenMP and therefore cannot use OpenMP
threading. VASP5 can perform an analogous form of parrellisation using
the [`NPAR`](https://www.vasp.at/wiki/index.php/NPAR) tag in the
`INCAR`, however. For more information on how to use
[`NPAR`](https://www.vasp.at/wiki/index.php/NPAR) see VASP’s
documentation page.

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

In general, unless you require otherwise for the sake of consistency
with earlier work or you rely on a removed feature, we recommend the
most recent version for which you have a license.

We have previously used version suffixes such as "-BEEF" and "-VTST" to
indicate the presence of various VASP extensions, but are now moving
away from that as the number of such extensions has grown and we have
not found any disadvantage in always including them.

### VASP5

If you do not have a license to use VASP 6 then use either
*VASP/5.4.4-CrayIntel-23.02-19-VTST-sol* on Māui, or
*VASP/5.4.4-intel-2020a* on Mahuika. Despite the lack of a version
suffix, this build  includes the BEEF, VTST and VASP-Sol extensions, and
also CUDA versions of the VASP executables.

Our testing suggests that OpenMP is not working in our VASP 5 builds,
and so it doesn't pay to set `--cpus-per-task` greater than one.

#### VASP 6

For most purposes we recommend *VASP/6.3.2-intel-2022a* on Mahuika,
which includes the BEEF, VTST, VASP-Sol, DFT-D4, LIBXC, and HDF5
extensions, and has functioning OpenMP support.

VASP6 has reimplemented its GPU support in such a way that it now makes
sense to build the GPU version separately, so to try the latest GPU
version of VASP, we have *VASP/6.3.2-NVHPC-22.3-GCC-11.3.0-CUDA-11.6.2*.

On Māui our only VASP 6 environment module is
*VASP/6.3.2-CrayIntel-23.02-19*.

### Extensions

There are a number of 3rd party extensions to VASP which we include.
None of them affect VASP unless specified in your `INCAR` file.

#### VTST

The [VASP Transition State
Tools](http://theory.cm.utexas.edu/vtsttools/), a third-party package
for finding transition states and computing rate constants.

#### BEEF

Our recent non-CUDA VASP executables all include BEEF ([Bayesian Error
Estimation
Functionals](http://suncat.stanford.edu/#/theory/facility/software/functional/)).

#### VASP-Sol

[VASPsol](https://github.com/henniggroup/VASPsol) is an implicit
solvation model that describes the effect of electrostatics, cavitation,
aa dispersion on the interaction between a solute and solvent into the
plane-wave DFT

#### DFT-D4

Building on the very popular D3 model, DFT-D4 is the newest update to
the dispersion-corrected Dnsity Functional Theory (DFT-D4 Van der Waals
functional. This method is available for VASP6 only and is applied by
setting IVDW=13 in the INCAR. If dispersion forces are important in your
calculation, DFT-D4 offers a good way of describing these.

#### LIBXC

LIBXC is a library which contains over 400 functionals from all rungs on
Jacob's ladder. Each functional is assigned an integer number ID which
can be found on
[this](https://www.tddft.org/programs/libxc/functionals/) website.

To use one of the LIBXC functionals, the following must be set in your
`INCAR`

GGA=LIBXC

LIBXC1 = \[string\] or \[integer\]

and sometimes,

LIBXC2 = \[string\] or \[integer\]

As per the VASP documentation, "LIBXC2can be used only if the functional
specified
with[LIBXC1](https://www.vasp.at/wiki/index.php/LIBXC1 "LIBXC1")
corresponds to only exchange and not to exchange and correlation." For
more information on correct usage of LIBXC please see[VASP's
documentation](https://www.vasp.at/wiki/index.php/LIBXC1) on this.

### Which VASP executable should I use?

VASP is unusual among scientific software packages in that some of its
execution options are controlled neither by the nature of the input
data, nor by command line flags, but by the executable itself. We offer
a range of VASP executables, each built with a different set of
compile-time options so that the resulting binary is optimised for a
particular sort of problem.

The different VASP executables are as follows:

|                |                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Name           | Description                                                                                                                       |
| `vasp_ncl`     | The most demanding VASP executable, suitable for non-collinear calculations (i.e., with spin-orbit coupling)                      |
| `vasp_std`     | A VASP executable with intermediate memory demands, suitable for collinear calculations without spin-orbit coupling               |
| `vasp_gam`     | A VASP executable with low memory demands, suitable for gamma-point calculations                                                  |
| `vasp_gpu`     | Like `vasp_std`, but with GPU support included. Only in VASP 5, because in VASP 6 the GPU build is a separate environment module. |
| `vasp_gpu_ncl` | Like `vasp_ncl`, but with GPU support included. Only in VASP 5, because in VASP 6 the GPU build is a separate environment module. |

### OpenACC GPU version of VASP6

There is now an official OpenACC GPU version of VASP, replacing the
older CUDA GPU version. See the official VASP documentation about the
OpenACC version of VASP:

<https://www.vasp.at/wiki/index.php/OpenACC_GPU_port_of_VASP>

The *\*-NVHPC-\** versions of the VASP modules on mahuika have been
built with OpenACC support.

VASP can run really well on GPUs, although how much you will benefit
from GPUs largely depends on the specific simulation/calculation that
you are running (simulation type, parameters, number of atoms, etc).
Therefore, it could be useful to run some smaller benchmarks (e.g.
reduced number of time steps) with different GPU and CPU-only
configurations in your Slurm scripts, before moving on to run larger
production simulations. When considering which configuration to use for
production you should take into account performance and compute unit
cost.

General information about using GPUs on NeSI can be found
[here](../../Scientific_Computing/Batch_Jobs/GPU_use_on_NeSI.md)
and details about the available GPUs on NeSI
[here](../Batch_Jobs/Available_GPUs_on_NeSI.md).

Here are some additional notes specific to running VASP on GPUs on NeSI:

- The command that you use to run VASP does not change - unlike
    the previous CUDA version, which had a `vasp_gpu` executable,
    with the OpenACC version the usual VASP executables (`vasp_std`,
    `vasp_gam`, `vasp_ncl`) are all built with OpenACC GPU support
    in the *\*-NVHPC-\** modules, so just use those as usual
- Always select one MPI process (Slurm task) per GPU, for example:
    - Running on 1 P100 GPU  

        ```bash
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=1  # 1 task per node as we set 1 GPU per node below
        #SBATCH --cpus-per-task=1
        #SBATCH --gpus-per-node=P100:1
        ```

    - Running on 4 HGX A100 GPUs on a single node  

        ```bash
        #SBATCH --nodes=1
        #SBATCH --ntasks-per-node=4  # 4 tasks per node as we set 4 GPUs per node below
        #SBATCH --cpus-per-task=1
        #SBATCH --gpus-per-node=A100:4
        #SBATCH --partition=hgx  # required to get the HGX A100s instead of PCI A100s
        ```

- Multiple threads per MPI process (`--cpus-per-task`) might be
    beneficial for performance but you should start by setting this
    to 1 to get a baseline
- VASP will scale better across multiple GPUs when they are all on
    the same node compared to across multiple nodes
- if you see memory errors like
    `call to cuMemAlloc returned error 2: Out of memory` you
    probably ran out of GPU memory. You could try requesting more
    GPUs (so the total amount of available memory is higher) and/or
    moving to GPUs with more memory (note: GPU memory is distinct
    from the usual memory you have to request for your job via
    `#SBATCH --mem` or similar; when you are allocated a GPU you get
    access to all the GPU memory on that device)
    - P100 GPUs have 12 GB GPU memory and you can have a maximum
            of 2 per node
    - PCI A100 GPUs have 40 GB GPU memory and you can have a
            maximum of 2 per node
    - HGX A100 GPUs have 80 GB GPU memory and you can have a
            maximum of 4 per node
- the HGX GPUs have a faster interconnect between the GPUs within
        a single node; if using multiple GPUs you may get better
        performance with the HGX A100s than with the PCI A100s
- A100 GPUs have more compute power than P100s so will perform
        better if your simulation can take advantage of the extra power
