---
created_at: '2015-10-12T00:28:38Z'
tags:
- mahuika
- engineering
- gpu
- mpi
- omp
- fea
title: ABAQUS
vote_count: 2
vote_sum: 0
zendesk_article_id: 212457807
zendesk_section_id: 360000040076
---

{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}

{{ app.description }}

{% include "partials/app/app_homepage.html" -%}
{% include "partials/app/app_warnings.html" -%}

!!! tip
    For a list of ABAQUS commands type:

    ```sh
    abaqus help
    ```

## Available Modules

{% include "partials/app/app_version.html" -%}

## Licences

The following network licence servers can be accessed from the NeSI cluster.

{% include "partials/app/app_network_licence.html" -%}

If you do not have access, or want a server connected {% include "partials/support_request.html" %}.

You can force ABAQUS to use a specific licence type by setting the
parameter `academic=TEACHING` or `academic=RESEARCH` in a relevant
[environment file](#environment-file).

!!! tip
     Required ABAQUS licences can be determined by this simple and
     intuitive formula <code>⌊ 5 x N<sup>0.422</sup> ⌋</code> where `N` is number
     of CPUs.

[Hyperthreading](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Hyperthreading.md)
can provide significant speedup to your computations, however
hyperthreaded CPUs will use twice the number of licence tokens. It may
be worth adding `#SBATCH --hint nomultithread` to your slurm script if
licence tokens are your main limiting factor.

## Solver Compatibility

Not all solvers are compatible with all types of parallelisation.

|                   |                    |           |        |         |
|-------------------|--------------------|-----------|--------|---------|
|                   | Element operations | Iterative | Direct | Lanczos |
| `mp_mode=threads` | ✖                  | ✔        | ✔     | ✔       |
| `mp_mode=mpi`     | ✔                  | ✔        | ✖     | ✖       |

!!! warning
     If your input files were created using an older version of ABAQUS you
     will need to update them using the command,
     ``` sh
     abaqus -upgrade -job new_job_name -odb old.odb
     ```
     or
     ``` sh
     abaqus -upgrade -job new_job_name -inp old.inp
     ```

## Examples

=== "Serial"
    For when only one CPU is required, generally as part of
    a [job array](../../Getting_Started/Next_Steps/Parallel_Execution.md#job-arrays)

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      ABAQUS-serial
    #SBATCH --time          00:05:00 # Walltime
    #SBATCH --cpus-per-task 1
    #SBATCH --mem           1500          # total mem
    module load ABAQUS/{{app.default}}
    abaqus job="propeller_s4rs_c3d8r" verbose=2 interactive
    ```

=== "Shared Memory"
    `mp_mode=threads`
    Uses a nodes shared memory for communication.
    May have a small speedup compared to MPI when using a low number of
    CPUs, scales poorly. Needs significantly less memory than MPI.
    Hyperthreading may be enabled if using shared memory but it is not
    recommended.

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      ABAQUS-Shared
    #SBATCH --time          00:05:00       # Walltime
    #SBATCH --cpus-per-task 4
    #SBATCH --mem           2G             # total mem
    module load ABAQUS/{{app.default}}
    abaqus job="propeller_s4rs_c3d8r cpus=${SLURM_CPUS_PER_TASK} \
        mp_mode=threads verbose=2 interactive
    ```

=== "UDF"
    Shared memory run with user defined function (fortran or C).
    Function will be compiled at start of run.
    You may need to chance the function suffix if you usually compile on windows.

    ```sl
    #!/bin/bash -e
    
    #SBATCH --job-name      ABAQUS-SharedUDF
    #SBATCH --time          00:05:00       # Walltime
    #SBATCH --cpus-per-task 4
    #SBATCH --mem           2G         # total mem

    module load imkl
    module  load ABAQUS/{{app.default}}
    abaqus job="propeller_s4rs_c3d8r" user=my_udf.f90 \
        cpus=${SLURM_CPUS_PER_TASK} mp_mode=threads verbose=2 interactive
    ```

=== "Distributed Memory"
    `mp_mode=mpi`
    Multiple processes each with a single *thread*. Not limited to one node.
    Model will be segmented into `-np` pieces which
    should be equal to `--ntasks`
    Each task could be running on a different node leading to increased
    communication overhead. Jobs can be limited to a single node by adding `--nodes=1` however this will increase your time in the
    queue as contiguous cpu's are harder to schedule.
    This is the default method if `mp_mode` is left
    unspecified.

    ```sl
    #!/bin/bash -e
    
    #SBATCH --job-name      ABAQUS-Distributed 
    #SBATCH --time          00:05:00       # Walltime</span></span>
    #SBATCH --ntasks        8
    #SBATCH --mem-per-cpu   1500          # Each CPU needs it&#39;s own.
    #SBATCH --nodes         1
    
    module load ABAQUS/{{app.default}}
    abaqus job="propeller_s4rs_c3d8r" cpus=${SLURM_NTASKS} mp_mode=mpi \
        verbose=2 interactive
    ```

=== "GPUs"
    The GPU nodes are limited to 16 CPUs
    In order for the GPUs to be worthwhile, you should see a speedup
    equivalent to 56 CPU's per GPU used. GPU modes will
    generally have less memory/cpus.

    ```sl
    #!/bin/bash -e
    
    #SBATCH --job-name      ABAQUS-gpu
    #SBATCH --time          00:05:00       # Walltime</span></span>
    #SBATCH --cpus-per-task 4
    #SBATCH --mem           4G         # total mem</span></span>
    #SBATCH --gpus-per-node
    module load ABAQUS/{{app.default}}
    module load CUDA
    abaqus job="propeller_s4rs_c3d8r" cpus=${SLURM_CPUS_PER_TASK} \
    gpus=${SLURM_GPUS_PER_NODE} mp_mode=threads \
    verbose=2 interactive
    ```

## User Defined Functions

User defined functions (UDFs) can be included on the command line with
the argument `user=<filename>` where `<filename>` is the C or fortran
source code.

Extra compiler options can be set in your local `abaqus_v6.env` [file](#environment-file).

The default compile commands are for `imkl`, other compilers can be
loaded with `module load`, you may have to change the [compile
commands](../../Scientific_Computing/HPC_Software_Environment/Compiling_software_on_Mahuika.md)
in your local `.env` file.

## Environment file

The [ABAQUS environment
file](http://media.3ds.com/support/simulia/public/v613/installation-and-licensing-guides/books/sgb/default.htm?startat=ch04s01.html) contains
a number of parameters that define how the your job will run, some of
these you may with to change.

These parameters are read in the following order of preference,

`../ABAQUS/SMA/site/abaqus_v6.env` Set by NeSI and cannot be changed.

`~/abaqus_v6.env` (your home directory) If exists, will be used in all
jobs submitted by you.

`<working directory>/abaqus_v6.env` If exists, will used in this job
only.

You may want to include this short snippet when making changes specific
to a job.

``` sh
# Before starting abaqus
echo "parameter=value
parameter=value
parameter=value" > "abaqus_v6.env"

# After job is finished.
rm "abaqus_v6.env"
```

## Performance

![ABAQUS\_speedup\_SharedVMPI.png](../../assets/images/ABAQUS.png)

*Note: Hyperthreading off, testing done on small mechanical FEA model.
Results highly model dependant. Do your own tests.*

## Common Issues

### Unable to create temporary directory

This may be caused by using a path for the `job` parameter. e.g.

```sh
abaqus job="/nesi/project/nesi99999/my_input.inp"
```

ABAQUS cannot create subdirectories, leading to the error message about permissions.
This can be fixed by using the `input` parameter, e.g.

```sh
abaqus input="/nesi/project/nesi99999/my_input.inp" job="my_input"
```
