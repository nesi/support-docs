---
created_at: '2018-11-21T03:32:30Z'
hidden: true
label_names: []
position: 36
title: 'MATLAB: Introduction'
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000577576
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

More general information can be found on MATLAB
[here.](https://support.nesi.org.nz/hc/en-gb/articles/212639047-MATLAB)

# Setup

Load MATLAB with the command.

``` sl
module load MATLAB
```

Help can be found with

``` sl
matlab -nodisplay -help
```

# X11 and -nodisplay

By default MATALB will attempt to open a virtual desktop version of
MATLAB, this will only work if X11 forwarding is enabled `-y`) and you
have a suitable X11 application installed (MobaXterm, Xming, Quartz,
Xorg).

------------------------------------------------------------------------

To run the desktop version of MATLAB enter:

``` sl
matlab
```

This can be useful as an introduction for those not familiar with the
command line environment, however this is **not recommended** as your
primary method of running MATLAB** **as it is significantly slower than
running with `-nodisplay` and does not help familiarize you with the
commands necessary for submitting batch jobs.

Appending the command with;

``` sl
matlab -nodisplay
```

Will force MATLAB to open as the command line version.

------------------------------------------------------------------------

# Running MATLAB interactively

Using MATLAB interactively can be useful for testing but **should not be
used for large jobs** (anything with multiple CPU's or multiple hours).

## CMD MATLAB

To start the command line version of MATLAB run:

``` sl
matlab -nodisplay
```

This will function identically to the Command Window in the desktop
version of MATLAB.

## There should be an image here but it couldn't be loaded.

Enter 'quit' to leave the MATLAB session or ctrl + z to kill it.

# Running MATLAB batch jobs

For your job to be submittable as a Slurm script you must be able to
initiate it from the bash command line. This can be done in 2 ways.

## Piping

A .m script can be piped into MATLAB using.

``` sl
matlab -nodisplay < myScript.m
```

This will open MATLAB then run your script. 

## Functions

MATLAB also accepts command window inputs using '-r'. Note ';' used for
line-breaks.

``` sl
matlab -nodisplay -r "x=(1:10); y=(1:10); z=x'*y; disp(z);exit;"
```

Will give the output

There should be an image here but it couldn't be loaded.

then exit.

To run a function in the current directory.

``` sl
matlab -nodisplay -r "myFunction(15);"
```

A script can also be run using this method.

``` sl
matlab -nodisplay -r "myScript;"
```

## Paths

By default only files in the same directory as you called MATLAB from
will be included in the directory (no sub-directories).  
A single directory can be added to path with;

``` sl
addpath('your_directory') 
```

``` sl
addpath(genpath('your_directory'))
```

## Output

Output from your job can be obtained multiple ways

### Terminal output

The output of the terminal can be sent to a file using -logfile, e.g:

``` sl
matlab -nodisplay -r "myScript; exit;"
```

*Note: This is mostly made redundant by Slurm logs.*

### MATLAB outputs

Any outputs made from terminal output logging will be in plain-text
meaning it may be more useful to create your output files inside your
MATLAB code (e.g fprintf);

### Java.Log

MATLAB also creates java.log files (generally useless) information about
the job run. By default these will be created in your home directory,
this can be changed by editing the environment variable MATLAB\_LOG\_DIR

e.g.

``` sl
export MATLAB_LOG_DIR=logs
```

## Slurm

Creating a file job.sl to add everything in the the parent directory
'parentDirectory' to the path and then run the function 'myFunction()'

``` sl
#!/bin/bash -e

#SBATCH --job-name MATLAB_test        #Name to appear in squeue
#SBATCH --time          06:00:00      #Max walltime
#SBATCH --mem-per-cpu   1500          #Max memory per logical core
#SBATCH --ntasks=1                    #No MPI
#SBATCH --output=%x_out.log           #Location of output log
#SBATCH --error=%x_error.err          #Location of error log

module load MATLAB
#OR specific version with;
#module load MATLAB/2017b

#Job run
matlab -nodisplay -r "addpath(genpath('../parentDirectory'));myFunction(5,20)"
```

 

This can then be submitted with

``` sl
sbatch job.sl
```

 

## Other stuff

handy for deleting log files in your home directory

``` sl
rm java.log*
```
