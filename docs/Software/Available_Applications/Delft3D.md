---
created_at: '2020-06-26T06:09:34Z'
tags:
 - hydrodynamics
 - morphodynamics
 - particle modelling
 - water quality testing
 - wave modelling
---

{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}

## Example scripts

=== "Serial"

    For when only one CPU is required, generally as part of a [job array](../../Getting_Started/Next_Steps/Parallel_Execution.md#job-arrays).

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      Delft3D
    #SBATCH --time          00:05:00       # Walltime
    #SBATCH --mem           512M           # Total Memory
    #SBATCH --hint          nomultithread  # Hyperthreading disabled
    module load Delft3D/{{app.default}}
    d_hydro test_input.xml
    ```

=== "Shared Memory"

    For domain based decompositions. Use `--cpus-per-task` to allocate resources.
    Each subdomain runs in a separate thread, inside one executable. Limited to one node.

    ```sl
    #!/bin/bash -e
    
    #SBATCH --job-name      Delft3D
    #SBATCH --time          00:05:00       # Walltime
    #SBATCH --cpus-per-task 4
    #SBATCH --mem           2G             # Total Memory
    #SBATCH --hint         nomultithread  # Hyperthreading disabled
    
    module load Delft3D/{{app.default}}
    
    srun d_hydro test_input.xml
    ```

=== "Distributed Memory"

    Domain is split automatically in stripwise partitions.
    Can run across multiple nodes. Use `--ntasks` to allocate resources.

    Cannot be used in conjunction with:
    - DomainDecomposition
    - Fluid mud
    - Coup online
    - Drogues and moving observation points
    - Culverts
    - Power stations with inlet and outlet in different partitions
    - Non-hydrostatic solvers
    - Walking discharges
    - 2D skewed weirs
    - max(mmax,nmax)/npart ≤ 4
    - Roller model
    - Mormerge
    - Mass balance polygons

    ```sl
    #!/bin/bash -e

    #SBATCH --job-name      Delft3D_distributed
    #SBATCH --time          00:05:00       # Walltime
    #SBATCH --mem-per-cpu   1G             
    #SBATCH --hint          nomultithread  # Hyperthreading disabled

    module load Delft3D/{{app.default}}
    srun d_hydro test_input.xml
    ```

!!! warning
    Trying to use more tasks than there are partitions in your model will cause failure.
