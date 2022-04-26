Example scripts
===============

+-----------------------------------+-----------------------------------+
| Serial                            |     #!/bin/bash -e                |
| ------                            |                                   |
|                                   |                                   |
| -------------------------------   |   #SBATCH --job-name      Delft3D |
|                                   |     #SBATCH --time                |
| For when only one CPU is          |         00:05:00       # Walltime |
| required, generally as part of an |     #SBATCH --mem                 |
| [job                              |     512M           # Total Memory |
| array](https://support.nesi.      |                                   |
| org.nz/hc/en-gb/articles/36000069 |   #SBATCH --hint          nomulti |
| 0275-Parallel-Execution#t_array). | thread  # Hyperthreading disabled |
|                                   |                                   |
|                                   |     module load Delft3D           |
|                                   |                                   |
|                                   |     d_hydro test_input.xml        |
+-----------------------------------+-----------------------------------+
| Multi-threaded                    |     #!/bin/bash -e                |
| ---------------                   |                                   |
|                                   |                                   |
| -------------------------------   |  #SBATCH --job-name      Delft3D  |
|                                   |     #SBATCH --time                |
| [For domain based                 |         00:05:00       # Walltime |
| decom                             |     #SBATC                        |
| positions.]{.wysiwyg-color-black} | H --cpus-per-task 4               |
|                                   |     #SBATCH --mem                 |
| [Use `#!['bash']cpus-per-task` to |     2G             # Total Memory |
| allocate                          |                                   |
| resources.]{.wysiwyg-color-black} |   #SBATCH --hint          nomulti |
|                                   | thread  # Hyperthreading disabled |
| Each subdomain runs in a          |                                   |
| separate\                         |     module load Delft3D           |
| thread, inside one executable.    |                                   |
| *Limited to one node.*            |     d_hyrdo test_input.xml        |
+-----------------------------------+-----------------------------------+
| MPI                               |     #!/bin/bash -e                |
| ---                               |                                   |
|                                   |                                   |
| -------------------------------   |  #SBATCH --job-name      Delft3D  |
|                                   |     #SBATCH --time                |
| Domain is split automatically in  |         00:05:00       # Walltime |
| stripwise partitions. *Can run    |     #SBATC                        |
| across multiple nodes.*           | H --ntasks        4               |
|                                   |     #SBATC                        |
| Use `#!['bash']ntasks` to         | H --mem-per-cpu   1G              |
| allocate resources.               |                                   |
|                                   |   #SBATCH --hint          nomulti |
| **Cannot** be used in conjunction | thread  # Hyperthreading disabled |
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
