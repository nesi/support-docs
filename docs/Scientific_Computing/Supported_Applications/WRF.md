---
created_at: '2020-11-02T23:31:38Z'
tags:
- software
description: Supported applications page for WRF
status: deprecated
---

The Weather Research and Forecasting (WRF) Model is a next-generation
mesoscale numerical weather prediction system designed for both
atmospheric research and operational forecasting applications. It
features two dynamical cores, a data assimilation system, and a software
architecture supporting parallel computation and system extensibility.
The model serves a wide range of meteorological applications across
scales from tens of meters to thousands of kilometres.

This guide is based on WRF 4.6.0 and WPS 4.6.0

## Building WRF

The following script will run through the complete install procedure of WRF on Mahuika. You can run the script with `bash` *script\_name.sh*:

``` sh
#!/bin/bash

module purge >& /dev/null
module load netCDF-Fortran/4.6.1-gompi-2023a

# set the compilers and supress warnings
export fallow_argument=-fallow-argument-mismatch
export boz_argument=-fallow-invalid-boz
export FFLAGS="$fallow_argument $boz_argument -m64"
export FCFLAGS="$fallow_argument $boz_argument -m64"
export CC=gcc
export CXX=gcc
export MPICC=mpicc
export MPICXX=mpicxx
export NETCDF=$EBROOTNETCDFMINFORTRAN

git clone --recurse-submodule https://github.com/wrf-model/WRF.git --depth 1 --branch v4.6.0

cd WRF
echo -e "\n\n\033[31m============If you are on Mahuika please select option 34 below============\033[0m"
./configure

echo -e "\n\n\033[31m============Done with configure step. Now compiling WRF. Build log in './WRF/wrf_build.log'============\033[0m"
export J="-j 12"
./compile em_real >& wrf_build.log

```

!!! Note
    Please select option 34 (dmpar gfortran/gccGNU) when asked `Please select from among the following Linux x86_64 options`.

It will take some time for WRF to compile (~30 minutes). You may wish to run this from a [tmux](https://docs.nesi.org.nz/Getting_Started/Cheat_Sheets/tmux-Reference_sheet/) session to minimise the risk of disconnecting. Check the `wrf_build.log` file for any error or warning messages when finished.

## Running WRF

An example Slurm job script for WRF on Mahuika is given below. The job can be submitted with `sbatch` *name\_of\_script.sl*

``` sl
#!/bin/bash -e

#SBATCH --account       nesi12345
#SBATCH --job-name      wrf
#SBATCH --time          01:00:00
#SBATCH --ntasks        36
#SBATCH --hint          nomultithread
#SBATCH --partition     milan

module purge 2> /dev/null
module load netCDF-Fortran/4.6.1-gompi-2023a
module list

# run real
srun --kill-on-bad-exit --output=real.log ./real.exe

# run wrf
srun --kill-on-bad-exit --output=wrf.log ./wrf.exe
```

The `srun` argument `--kill-on-bad-exit` should ensure the entire job is killed
if any individual task fails. Without this option, the WRF job will stay alive
until the wall limit is reached but won't actually do anything.

## Building and running WPS

The following script will build WPS. Like the WRF build process, this will ask you to specify a compiler from the list of options:

```sh
#!/bin/bash

wget https://github.com/wrf-model/WPS/archive/refs/tags/v4.6.0.tar.gz
tar xf v4.6.0.tar.gz
cd WPS-4.6.0

module purge 2> /dev/null
module load netCDF-Fortran/4.6.1-gompi-2023a
module load JasPer/2.0.33-GCC-12.3.0

export NETCDF=$EBROOTNETCDFMINFORTRAN
export NETCDFF=$EBROOTNETCDFMINFORTRAN
export HDF5=$EBROOTHDF5
export JASPERLIB=$EBROOTJASPER/lib64/libjasper.so
export JASPERINC=$EBROOTJASPER/include/jasper/jasper.h
export WRF_DIR='path/to/WRF/directory'

./clean > /dev/null 2>&1

echo -e "\n\033[31m=============On Mahuika, please choose option 1 (serial) or 3 (MPI parallel) below===========\033[0m"
./configure

echo -e "\n\033[31m=============Now compiling WPS. log file is './WPS-4.6.0/WPS_build.log'===========\033[0m"
./compile >& WPS_build.log

```

!!! Note
    Change the `WRF_DIR` directory to the *full path* where you built WRF. Please **choose option 1** (`Linux x86_64, gfortran    (serial)`) to build serial (non MPI) WPS programmes, **choose option 3** (`Linux x86_64, gfortran    (dmpar)` for parallel WPS programmes.

WPS will compile much faster than WRF. Most WPS jobs can be run from the command line on the login node. If you wish to submit a WPS job (`geogrid.exe` for example) to a compute node, it can be done via the following Slurm script:

```sh
#!/bin/bash -e
#SBATCH --job-name=wps
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=1
#SBATCH --hint=nomultithread

module purge 2> /dev/null
module load netCDF-Fortran/4.6.1-gompi-2023a
module load JasPer/2.0.33-GCC-12.3.0

export WRF_DIR='path/to/WRF/build'

# run geogrid
./geogrid.exe

```

Note, just as in the Slurm script above, you will need netCDF and JasPer modules in your environment if you wish to run WPS programmes from the login node.
