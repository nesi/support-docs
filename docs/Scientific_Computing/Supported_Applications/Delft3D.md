# Example scripts

+-----------------------------------+-----------------------------------+
| ## Serial                         |     #!/bin/bash -e                |
|                                   |                                   |
| -------------------------------   |     #SBATCH --job-name      Delft |
|                                   | 3D                                |
| For when only                     |     #SBATCH --time          00:05 |
| <dfn class="dictionary-of-numbers | :00       # Walltime              |
| ">one                             |     #SBATCH --mem           512M  |
| CPU is required</dfn>, generally  |           # Total Memory          |
| as part of an [job                |     #SBATCH --hint          nomul |
| array](https://support.nesi.org.n | tithread  # Hyperthreading disabl |
| z/hc/en-gb/articles/360000690275- | ed                                |
| Parallel-Execution#t_array).      |                                   |
|                                   |     module load Delft3D           |
|                                   |                                   |
|                                   |     d_hydro test_input.xml        |
+-----------------------------------+-----------------------------------+
| ## Multi-threaded                 |     #!/bin/bash -e                |
|                                   |                                   |
| -------------------------------   |     #SBATCH --job-name      Delft |
|                                   | 3D                                |
| [For domain based                 |     #SBATCH --time          00:05 |
| decompositions.]{.wysiwyg-color-b | :00       # Walltime              |
| lack}                             |     #SBATCH --cpus-per-task 4     |
|                                   |                                   |
| [Use `#!['bash']cpus-per-task` to |     #SBATCH --mem           2G    |
| allocate                          |           # Total Memory          |
| resources.]{.wysiwyg-color-black} |     #SBATCH --hint          nomul |
|                                   | tithread  # Hyperthreading disabl |
| Each subdomain runs in a          | ed                                |
| separate\                         |                                   |
| thread, inside                    |     module load Delft3D           |
| <dfn class="dictionary-of-numbers |                                   |
| ">one                             |     d_hyrdo test_input.xml        |
| executable</dfn>. *Limited to     |                                   |
| <dfn class="dictionary-of-numbers |                                   |
| ">one                             |                                   |
| node</dfn>.*                      |                                   |
+-----------------------------------+-----------------------------------+
| ## MPI                            |     #!/bin/bash -e                |
|                                   |                                   |
| -------------------------------   |     #SBATCH --job-name      Delft |
|                                   | 3D                                |
| Domain is split automatically in  |     #SBATCH --time          00:05 |
| stripwise partitions. *Can run    | :00       # Walltime              |
| across multiple nodes.*           |     #SBATCH --ntasks        4     |
|                                   |                                   |
| Use `#!['bash']ntasks` to         |     #SBATCH --mem-per-cpu   1G    |
| allocate resources.               |                                   |
|                                   |     #SBATCH --hint          nomul |
| **Cannot** be used in conjunction | tithread  # Hyperthreading disabl |
| with:                             | ed                                |
|                                   |                                   |
| -   DomainDecomposition           |     module load Delft3D           |
| -   Fluid mud                     |                                   |
| -   Coup online                   |     srun d_hyrdo test_input.xml   |
| -   Drogues and moving            |                                   |
|     observation points            |                                   |
| -   Culverts                      |                                   |
| -   Power stations with inlet and |                                   |
|     outlet in different           |                                   |
|     partitions                    |                                   |
| -   Non-hydrostatic solvers       |                                   |
| -   Walking discharges            |                                   |
| -   <dfn class="dictionary-of-num |                                   |
| bers">2D                          |                                   |
|     skewed weirs</dfn>            |                                   |
| -   max(mmax,nmax)/npart ≤ 4      |                                   |
| -   Roller model                  |                                   |
| -   Mormerge                      |                                   |
| -   Mass balance polygons         |                                   |
+-----------------------------------+-----------------------------------+

> ### Note {#prerequisites}
>
> Trying to use more tasks than there are partitions in your model will
> cause failure.
