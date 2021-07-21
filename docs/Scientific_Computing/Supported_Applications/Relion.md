Getting started with Relion is most easily done via its X11 GUI, which
is launched with the command \"relion\".  

    $ module load Relion
    $ relion

After the desired options have been selected press the \"Print command\"
button to see the command it constructs in your terminal window. That
command line can then be pasted into a Slurm batch script.

If you leave \"Number of MPI procs\" at 1 then the Relion GUI will
produce a command like

    which relion_run_ctffind ...

That will work but can be simplified to

    relion_run_ctffind ...

If MPI is used then Relion will correctly recommend the MPI version of
the tool, eg:

    which relion_run_ctffind_mpi ...

but MPI programs need to be launched via srun, so that should be:

    srun relion_run_ctffind_mpi ...

You may notice that we have made some effort to integrate the Relion GUI
directly with Slurm so that it could submit Slurm jobs directly, however
this does not work yet.

Relion contains many different tools, some of which depend on programs
which we have not made dependencies of Relion, notably *ctffind* and
*MotionCorr*. these can however be loaded from their own environment
modules and will then work with Relion. For licensing reasons we ask
that you install *MotionCorr2* yourself if you need that.

Some of the Relion tools benefit tremendously from using a GPU.

 

 
