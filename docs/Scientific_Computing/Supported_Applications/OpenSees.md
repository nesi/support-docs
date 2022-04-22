There are three commands with which a OpenSees job can be launched.

-   [OpenSees]{.kbd} - For running a job in serial (single CPU).
-   [OpenSeesSP]{.kbd} - Intended for the single analysis of very large
    models.
-   [OpenSeesMP]{.kbd} - For advanced parametric studies.

 

More info can be found about running OpenSees in parallel
[here](http://opensees.berkeley.edu/OpenSees/parallel/TNParallelProcessing.pdf).

+-----------------------------------+-----------------------------------+
| ### Serial                        |     #!/bin/bash -e                |
|                                   |                                   |
| -------------------------------   |     #SBATC                        |
|                                   | H --job-name      OpenSees-Serial |
| Single *process* with a single    |     #SBATCH --time                |
| *thread.*                         |      00:05:00          # Walltime |
|                                   |     #SBATCH --                    |
| Usually submitted as part of an   | cpus-per-task 1                 # |
| array, as in the case of          |  Double if hyperthreading enabled |
| parameter sweeps.                 |     #SBATCH --mem                 |
|                                   |     512MB             # total mem |
|                                   |     #                             |
|                                   | SBATCH --hint          nomultithr |
|                                   | ead     # Hyperthreading disabled |
|                                   |                                   |
|                                   |     module load OpenSees          |
|                                   |                                   |
|                                   |     input="frame.tcl"             |
|                                   |     OpenSees ${input}             |
+-----------------------------------+-----------------------------------+

 
-

Input from Shell
----------------

Information can be passed from the bash shell to a Tcl script by use of
environment variables.

Set in Slurm script:

    export MY_VARIABLE="Hello World!"

Retrieved in Tcl script:

    puts $::env(MY_VARIABLE)

 

 
