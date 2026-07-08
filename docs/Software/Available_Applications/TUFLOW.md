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

    - **TUFLOW Classic** (`tuflow`): 1D/2D hydrodynamic solver using structured grids, controlled by a `.tcf` file.
    - **TUFLOW FV** (`tuflowfv`): flexible-mesh (finite volume) 2D/3D solver, controlled by a `.fvc` file.

## Available Modules

{% include "partials/app/app_version.html" -%}

## Licence Connection

TUFLOW requires a background licence daemon to be manually launched before the solver.
If you are using a cloud key, you will have to register it first.

```sh
CodeMeterLin -v &
sleep 10 && cmu --import --file ~/my_licence_key.wbc
```

## Example Scripts

### TUFLOW Classic

=== "Serial"

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      TUFLOW
    #SBATCH --account       nesi99991
    #SBATCH --time          01:00:00       # Walltime
    #SBATCH --mem           4G             # Total Memory

    module load TUFLOW/{{ app.default }}

    CodeMeterLin -v &
    sleep 10 && cmu --import --file ~/my_licence_key.wbc

    tuflow -b -nmb model.tcf
    ```

=== "GPU"

    GPU acceleration for TUFLOW Classic is enabled in the `.tcf` control file
    (e.g. `GPU == ON`) rather than via a command-line flag.

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      TUFLOW
    #SBATCH --account       nesi99991
    #SBATCH --time          01:00:00       # Walltime
    #SBATCH --mem           4G             # Total Memory
    #SBATCH --gpus-per-node 1:a100

    module load TUFLOW/{{ app.default }}

    CodeMeterLin -v &
    sleep 10 && cmu --import --file ~/my_licence_key.wbc

    tuflow -b -nmb model.tcf
    ```

### TUFLOW FV

=== "Serial"

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      TUFLOW-FV
    #SBATCH --account       nesi99991
    #SBATCH --time          01:00:00       # Walltime
    #SBATCH --mem           4G             # Total Memory

    module load TUFLOW/{{ app.default }}

    CodeMeterLin -v &
    sleep 10 && cmu --import --file ~/my_licence_key.wbc

    tuflowfv model.fvc
    ```

=== "Distributed Memory"

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      TUFLOW-FV
    #SBATCH --account       nesi99991      # project code
    #SBATCH --time          01:00:00       # Walltime
    #SBATCH --ntasks        8
    #SBATCH --mem-per-cpu   2G

    module load TUFLOW/{{ app.default }}

    CodeMeterLin -v &
    sleep 10 && cmu --import --file ~/my_licence_key.wbc

    srun tuflowfv model.fvc
    ```

=== "GPU"

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      TUFLOW-FV
    #SBATCH --account       nesi99991
    #SBATCH --time          01:00:00       # Walltime
    #SBATCH --mem           4G             # Total Memory
    #SBATCH --gpus-per-node 1:a100

    module load TUFLOW/{{ app.default }}

    CodeMeterLin -v &
    sleep 10 && cmu --import --file ~/my_licence_key.wbc

    tuflowfv -gpu model.fvc
    ```
