Example scripts
===============

+-----------------------------------+-----------------------------------+
| Serial                            |     #!/bin/bash -e                |
| ------                            |                                   |
|                                   |     #SBATCH --job-name      Delft |
| -------------------------------   | 3D                                |
|                                   |     #SBATCH --time          00:05 |
| For when only one CPU is          | :00       # Walltime              |
| required, generally as part of an |     #SBATCH --mem           512M  |
| [job                              |           # Total Memory          |
| array](https://support.nesi.org.n |     #SBATCH --hint          nomul |
| z/hc/en-gb/articles/360000690275- | tithread  # Hyperthreading disabl |
| Parallel-Execution#t_array).      | ed                                |
|                                   |                                   |
|                                   |     module load Delft3D           |
|                                   |                                   |
|                                   |     d_hydro test_input.xml        |
+-----------------------------------+-----------------------------------+
| Multi-threaded                    |     #!/bin/bash -e                |
| ---------------                   |                                   |
|                                   |     #SBATCH --job-name      Delft |
| -------------------------------   | 3D                                |
|                                   |     #SBATCH --time          00:05 |
| [For domain based                 | :00       # Walltime              |
| decompositions.]{.wysiwyg-color-b |     #SBATCH --cpus-per-task 4     |
| lack}                             |                                   |
|                                   |     #SBATCH --mem           2G    |
| [Use `cpus-per-task`{.bash} to    |           # Total Memory          |
| allocate                          |     #SBATCH --hint          nomul |
| resources.]{.wysiwyg-color-black} | tithread  # Hyperthreading disabl |
|                                   | ed                                |
| Each subdomain runs in a          |                                   |
| separate\                         |     module load Delft3D           |
| thread, inside one executable.    |                                   |
| *Limited to one node.*            |     d_hyrdo test_input.xml        |
+-----------------------------------+-----------------------------------+
| MPI                               |     #!/bin/bash -e                |
| ---                               |                                   |
|                                   |     #SBATCH --job-name      Delft |
| -------------------------------   | 3D                                |
|                                   |     #SBATCH --time          00:05 |
| Domain is split automatically in  | :00       # Walltime              |
| stripwise partitions. *Can run    |     #SBATCH --ntasks        4     |
| across multiple nodes.*           |                                   |
|                                   |     #SBATCH --mem-per-cpu   1G    |
| Use `ntasks`{.bash} to allocate   |                                   |
| resources.                        |     #SBATCH --hint          nomul |
|                                   | tithread  # Hyperthreading disabl |
| **Cannot** be used in conjunction | ed                                |
| with:                             |                                   |
|                                   |     module load Delft3D           |
| -   DomainDecomposition           |                                   |
| -   Fluid mud                     |     srun d_hyrdo test_input.xml   |
| -   Coup online                   |                                   |
| -   Drogues and moving            |                                   |
|     observation points            |                                   |
| -   Culverts                      |                                   |
| -   Power stations with inlet and |                                   |
|     outlet in different           |                                   |
|     partitions                    |                                   |
| -   Non-hydrostatic solvers       |                                   |
| -   Walking discharges            |                                   |
| -   2D skewed weirs               |                                   |
| -   max(mmax,nmax)/npart ≤ 4      |                                   |
| -   Roller model                  |                                   |
| -   Mormerge                      |                                   |
| -   Mass balance polygons         |                                   |
+-----------------------------------+-----------------------------------+

> ### Note {#prerequisites}
>
> Trying to use more tasks than there are partitions in your model will
> cause failure.
