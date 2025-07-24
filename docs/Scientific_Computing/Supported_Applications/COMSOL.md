---
created_at: '2019-03-26T00:36:24Z'
tags:
- engineering
- cae
- multiphysics
- cfd
- fea
description: Running COMSOL multiphysics on the NeSI cluster.
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000871556
zendesk_section_id: 360000040076
---

{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}

```sh
comsol --help
```

Will display a list of COMSOL batch commands.

!!! tip "Useful Links"
    - [Running COMSOL in parallel on clusters.](https://www.comsol.com/support/knowledgebase/1001/)
    - [Running parametric sweeps, batch sweeps, and cluster sweeps from the command line.](https://www.comsol.com/support/knowledgebase/1250/)
    - [COMSOL and Multithreading.](https://www.comsol.com/support/knowledgebase/1096/)

## Batch Submission

When using COMSOL batch the following flags can be used to control
distribution.

|                         |                                                                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `-mpibootstrap slurm`   |  Instructs COMSOL to get it's settings from SLURM                                                                                |
| `-np <cpus>`            | Number of CPUs to use in each task. Equivalent to Slurm input `--cpus-per-task` or environment variable `${SLURM_CPUS_PER_TASK}` |
| `-nn <tasks>`           | Number of tasks total. `--ntasks` or `${SLURM_NTASKS}`                                                                           |
| `-nnhost <tasks>`       | Number of tasks per node. `--ntasks-per-node` `${SLURM_NTASKS_PER_NODE}`                                                         |
| `-f <path to hostlist>` | Host file. You won't need to set this in most circumstances.                                                                    |

## Example Scripts

=== "Serial Job"
    Single *process* with a single *thread*
    Usually submitted as part of an array, as in the case of parameter sweeps.

    ```sl
    #!/bin/bash -e
    
    #SBATCH --job-name      COMSOL-serial
    #SBATCH --licenses      comsol@uoa_foe
    #SBATCH --time          00:05:00          # Walltime
    #SBATCH --mem           1512               # total mem

    module load COMSOL/{{app.default}}
    comsol batch -inputfile my_input.mph
    ```

=== "Shared Memory Job"

    ```sl
    #!/bin/bash -e
    #SBATCH --job-name      COMSOL-shared
    #SBATCH --licenses      comsol@uoa_foe
    #SBATCH --time          00:05:00        # Walltime
    #SBATCH --cpus-per-task 8
    #SBATCH --mem           4G              # total mem
    module load COMSOL/{{app.default}}
    comsol batch -mpibootstrap slurm -inputfile my_input.mph 
    ```

=== "Distributed Memory Job"

    ```sl
    #!/bin/bash -e
    
    #SBATCH --job-name      COMSOL-distributed
    #SBATCH --licenses      comsol@uoa_foe
    #SBATCH --time          00:05:00            # Walltime
    #SBATCH --ntasks        8         
    #SBATCH --mem-per-cpu   1500                # mem per cpu
    
    module load COMSOL/{{app.default}}
    comsol batch -mpibootstrap slurm -inputfile my_input.mph
    ```

=== "Hybrid Job"

    ```sl
    #!/bin/bash -e
    #SBATCH --job-name         COMSOL-hybrid
    #SBATCH --licenses         comsol@uoa_foe
    #SBATCH --time             00:05:00          # Walltime
    #SBATCH --ntasks           4                 
    #SBATCH --cpus-per-task    16
    #SBATCH --mem-per-cpu      1500B             # total mem
 
    module load COMSOL/{{app.default}}
    comsol batch -mpibootstrap slurm -inputfile my_input.mph
    ```

=== "LiveLink"

    ```sl

    #!/bin/bash -e
    #SBATCH --job-name         COMSOL-livelink
    #SBATCH --licenses         comsol@uoa_foe
    #SBATCH --time             00:05:00
    #SBATCH --cpus-per-task    16
    #SBATCH --mem-per-cpu      1500
 
    module purge

    module load COMSOL/{{app.default}}
    module load MATLAB/2021b

    comsol mphserver -silent &
    matlab -batch "addpath('/opt/nesi/share/COMSOL/comsol154/multiphysics/mli/');mphstart;MyScript"
    ```

!!! warning
     If no output file is set, using `--output` the input file will be
     updated instead.

## Interactive Use

Providing you have [set up X11](../../Scientific_Computing/Terminal_Setup/X11_on_NeSI.md), you can
open the COMSOL GUI by running the command `comsol`.

Large jobs should not be run on the login node.

## LiveLink

If you are using COMSOL LiveLink, you will need to load a MATLAB module (in addition to the COMSOL module), e.g.

```sh
module load MATLAB/2021b
```

Then

```sh
comsol matlab -mlroot <path>
```

Where `<mlpath>` is the root directory of the MATLAB version you are using (`dirname $(dirname $(which matlab))`).

## Performance

COMSOL is relatively smart with it's use of resources, if possible it is
preferable to use `--cpus-per-task` over `--ntasks`

Memory requirements depend on job type, but will scale up with number of CPUs ≈ linearly.

Multithreading will benefit jobs using less than
8 CPUs, but is not recommended on larger jobs.

*Performance is highly depended on the model used. The above should only be used as a rough guide.*
![Speedup](../../assets/images/speedup_smoothed.png)

## Tmpdir

If you find yourself receiving the error 'Disk quota exceeded', yet `nn_storage_quota` shows plenty of room in your filesystem, you may be running out of tmpdir.
This can be fixed by using the `--tmpdir` flag in the comsol command line, e.g. `comsol --tmpdir /nesi/nobackup/nesi99991/comsoltmp`, or by exporting `TMPDIR` before running the command, e.g. `export TMPDIR=/nesi/nobackup/nesi99991/comsoltmp`.

You may also want to set this at the Java level with `export _JAVA_OPTIONS=-Djava.io.tmpdir=/nesi/nobackup/nesi99991/comsoltmp`

