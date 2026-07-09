---
created_at: '2026-07-08'
description: How to run TUFLOW Classic and TUFLOW FV hydrodynamic modelling on NeSI.
tags:
- hydrodynamics
- flood modelling
- hydraulics
---

{% set app_name = "TUFLOW" %}
{% set app = applications[app_name] %}

{{ app.description }}
{% include "partials/app/app_homepage.html" -%}
{% include "partials/app/app_warnings.html" -%}

!!! note "Solvers"
    The `TUFLOW` module provides two executables:

    - **TUFLOW Classic** (`tuflow-idp`, `tuflow-isp`): 1D/2D hydrodynamic solver using structured grids, controlled by a `.tcf` file. `tuflow-idp` for double floating point precision, `tuflow-isp` for single point.
    - **TUFLOW FV** (`tuflowfv`): flexible-mesh (finite volume) 2D/3D solver, controlled by a `.fvc` file.

## Available Modules

{% include "partials/app/app_version.html" -%}

## Licence Connection

TUFLOW requires a background licence daemon to be manually launched before the solver.
If you are using a network cloud licence, you will have to register it first.

```sh
CodeMeterLin -v &
sleep 10 && cmu --import --file ~/my_licence_key.wbc
```

## Example Scripts

### TUFLOW Classic

!!! note "Useful Links"

    [Full list of command line flags](https://docs.tuflow.com/classic-hpc/manual/2025.1/Running-Simulations-1.html#tab:tab-TUFLOWOptions)

    [Full list of `.tcf` command file arguments](https://docs.tuflow.com/classic-hpc/manual/2025.0/TCFCommands-1.html) 

=== "Shared Memory"

    Make sure your `.tcf` file includes;
    
    ```tcf
    Solution Scheme == HPC
    Hardware == CPU
    ```

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      TUFLOW
    #SBATCH --account       nesi99991
    #SBATCH --time          01:00:00       # Walltime
    #SBATCH --cpus-per-task 8
    #SBATCH --mem           4G             # Total Memory

    module purge
    module load TUFLOW/{{ app.default }}

    CodeMeterLin -v &
    sleep 10 && cmu --import --file ~/my_licence_key.wbc

    tuflow-idp  -nt $SLURM_CPUS_PER_TASK  -b -nmb my_model.tcf
    ```

=== "GPU"

    Make sure your `.tcf` control file includes; 

    ```tcf
    Solution Scheme == HPC
    Hardware == GPU
    ```

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      TUFLOW
    #SBATCH --account       nesi99991
    #SBATCH --time          01:00:00       # Walltime
    #SBATCH --mem           4G             # Total Memory
    #SBATCH --gpus-per-node 1:a100

    module purge
    module load CUDA
    module load TUFLOW/{{ app.default }}

    CodeMeterLin -v &
    sleep 10 && cmu --import --file ~/my_licence_key.wbc

    tuflow-idp -b -nmb model.tcf
    ```

### TUFLOW FV


!!! note "Useful Links"

    [Full list of `.fvc` control File commands.](https://docs.tuflow.com/fv/wqm/manual/2025.2/TFVCommands-2.html)

=== "Shared Memory"

    Make sure your `.fvc` control file includes;

    ```fvc
    Solution Scheme == HPC
    Hardware == CPU
    ```

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      TUFLOW-FV
    #SBATCH --account       nesi99991
    #SBATCH --time          01:00:00       # Walltime
    #SBATCH --mem           4G             # Total Memory

    module purge
    module load TUFLOW/{{ app.default }}

    CodeMeterLin -v &
    sleep 10 && cmu --import --file ~/my_licence_key.wbc

    tuflowfv my_model.fvc
    ```

=== "Distributed Memory"

    Make sure your `.fvc` control file includes;

    ```fvc
    Solution Scheme == HPC
    Hardware == CPU
    ```

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      TUFLOW-FV
    #SBATCH --account       nesi99991      # project code
    #SBATCH --time          01:00:00       # Walltime
    #SBATCH --ntasks        8
    #SBATCH --mem-per-cpu   2G

    module purge
    module load TUFLOW/{{ app.default }}

    CodeMeterLin -v &
    sleep 10 && cmu --import --file ~/my_licence_key.wbc

    srun tuflowfv my_model.fvc
    ```

=== "GPU"

    Make sure your `.fvc` control file includes;

    ```fvc
    Solution Scheme == HPC
    Hardware == GPU
    ```

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      TUFLOW-FV
    #SBATCH --account       nesi99991
    #SBATCH --time          01:00:00       # Walltime
    #SBATCH --mem           4G             # Total Memory
    #SBATCH --gpus-per-node 1:a100

    module purge
    module load CUDA
    module load TUFLOW/{{ app.default }}

    CodeMeterLin -v &
    sleep 10 && cmu --import --file ~/my_licence_key.wbc

    tuflowfv my_model.fvc
    ```
