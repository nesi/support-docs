---
created_at: '2020-06-26T06:09:34Z'
hidden: false
position: 11
tags:
 - hydrodynamics
title: Delft3D
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001593096
zendesk_section_id: 360000040076
---

## Example scripts

=== "Serial Job"

For when only one CPU is required, generally as part of
a [job
array](https://support.nesi.org.nz/hc/en-gb/articles/360000690275-Parallel-Execution#t_array).

    ```
    #!/bin/bash -e

    #SBATCH --job-name      Delft3D
    #SBATCH --time          00:05:00       # Walltime</span></span>
    #SBATCH --mem           512M           # Total Memory</span></span>
    #SBATCH --hint          nomultithread  # Hyperthreading disabled
    module load Delft3D/{{applications.ABAQUS.machines.mahuika.versions | last}}
    d_hydro test_input.xml
=== "Shared Memory Job"
For domain based decompositions. Use `--cpus-per-task` to allocate
resources.
Each subdomain runs in a separate
thread, inside one executable. Limited to one node.

   ```sl
    #!/bin/bash -e
    
    #SBATCH --job-name      Delft3D
    #SBATCH --time          00:05:00       # Walltime
    #SBATCH --cpus-per-task 4
    #SBATCH --mem           2G             # Total Memory
    #SBATCH --hint         nomultithread  # Hyperthreading disabled
    
    module load Delft3D/{{applications.Delft3D.machines.mahuika.versions | last}}
    
    srun d_hyrdo test_input.xml
    ```
 
 === "Distributed Memory Job"

    Domain is split automatically in stripwise partitions. Can run
across multiple nodes. Use `--ntasks` to allocate resources.
    Cannot be used in conjunction with:
<ul>
<li>DomainDecomposition</li>
<li>Fluid mud</li>
<li>Coup online</li>
<li>Drogues and moving observation points</li>
<li>Culverts</li>
<li>Power stations with inlet and outlet in different partitions</li>
<li>Non-hydrostatic solvers</li>
<li>Walking discharges</li>
<li><span>2D skewed weirs</span></li>
<li>max(mmax,nmax)/npart ≤ 4</li>
<li>Roller model</li>
<li>Mormerge</li>
<li>Mass balance polygons</li>

    ```
    #!/bin/bash -e
    #SBATCH --job-name      Delft3D_distributed
    #SBATCH --time          00:05:00       # Walltime
    #SBATCH --mem-per-cpu   1G             #SBATCH --hint          nomultithread  # Hyperthreading disabled
    module load Delft3D/{{applications.Delft3D.machines.mahuika.versions | last}}
    srun d_hyrdo test_input.xml
    ```

!!!  warning 
     Trying to use more tasks than there are partitions in your model will
     cause failure.
