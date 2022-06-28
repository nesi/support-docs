There are three commands with which a OpenSees job can be launched.

-   OpenSees - For running a job in serial (single CPU).
-   OpenSeesSP - Intended for the single analysis of very large models.
-   OpenSeesMP - For advanced parametric studies.

 

More info can be found about running OpenSees in parallel
[here](http://opensees.berkeley.edu/OpenSees/parallel/TNParallelProcessing.pdf).

+-----------------------------------+-----------------------------------+
| ### Serial                        |     #!/bin/bash -e                |
|                                   |                                   |
| -------------------------------   |     #SBATCH --job-name      OpenS |
|                                   | ees-Serial                        |
| Single *process* with a single    |     #SBATCH --time          00:05 |
| *thread.*                         | :00          # Walltime           |
|                                   |     #SBATCH --cpus-per-task 1     |
| Usually submitted as part of an   |              # Double if hyperthr |
| array, as in the case of          | eading enabled                    |
| parameter sweeps.                 |     #SBATCH --mem           512MB |
|                                   |              # total mem          |
|                                   |     #SBATCH --hint          nomul |
|                                   | tithread     # Hyperthreading dis |
|                                   | abled                             |
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

 

 
