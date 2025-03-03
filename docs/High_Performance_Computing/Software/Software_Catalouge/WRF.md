---
created_at: '2020-11-02T23:31:38Z'
tags: []
title: WRF
vote_count: 2
vote_sum: 2
zendesk_article_id: 360002109696
zendesk_section_id: 360000040076
---

The Weather Research and Forecasting (WRF) Model is a next-generation
mesoscale numerical weather prediction system designed for both
atmospheric research and operational forecasting applications. It
features two dynamical cores, a data assimilation system, and a software
architecture supporting parallel computation and system extensibility.
The model serves a wide range of meteorological applications across
scales from tens of meters to thousands of kilometres.

This guide is based on WRF 4.6.0 and WPS 4.6.0
## WRF on Mahuika
### Building WRF on Mahuika

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

It will take some time for WRF to compile (~30 minutes). You may wish to run this from a [tmux](tmux-Reference_sheet.md) session to minimise the risk of disconnecting. Check the `wrf_build.log` file for any error or warning messages when finished.

### Running WRF on Mahuika

An example Slurm job script for WRF on Mahuika is given below. The job can be submitted with `sbatch` *name\_of\_script.sl*

``` sl
#!/bin/bash -e
#SBATCH --job-name=wrf
#SBATCH --time=01:00:00
#SBATCH --ntasks=36
#SBATCH --hint=nomultithread
#SBATCH --partition=milan

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


### Building and running WPS on Mahuika
The following script will build WPS on Mahuika. Like the WRF build process, this will ask you to specify a compiler from the list of options:

``` sh
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
```
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

## WRF on Māui

### Building WRF Māui

Load environment modules and set up the build environment (here we will
build with the Intel compiler):

``` sl
# load PrgEnv-intel (this assumes you currently have PrgEnv-cray loaded)
module switch PrgEnv-cray PrgEnv-intel

# load dependencies
module load cray-netcdf cray-hdf5 cray-parallel-netcdf

# the following two lines are optional and may improve performance
module switch craype-x86-skylake craype-broadwell
module load craype-hugepages2M

export NETCDF=$NETCDF_DIR
export HDF5=$HDF5_DIR
export PNETCDF=$PNETCDF_DIR
```

Apply patches for Polar WRF if required and then configure WRF:

``` sh
./configure
# choose option 50 - INTEL (ftn/icc) Cray XC (dmpar)
# choose an appropriate nesting option or leave it at the default
```

The configure script takes some options, for example, to configure for a
debug build (no optimisations and debug symbols enabled) you could run
*./configure -d* instead.

The configure script writes out a *configure.wrf* file which can also be
edited manually if desired. For example, if you want an optimised build
with debug symbols included, you could add *-g* to the *FCDEBUG*
variable.

Next compile WRF:

``` sh
./compile em_real >& log.compile
```

It is important to check the output in *log.compile* as the command will
not exit with an error if it fails. Check the end of the log file for a
message saying compilation was successful. You could also check the
timestamps of the executables in the *main* subdirectory
(*main/wrf.exe*, *main/real.exe*, etc).

### Running WRF on Māui

An example Slurm script for running WRF on Māui, which can be submitted
with *sbatch name\_of\_script.sl*:

``` sl
#!/bin/bash -e
#SBATCH --job-name=wrf
#SBATCH --time=01:00:00
#SBATCH --ntasks=240
#SBATCH --hint=nomultithread

# important, required on Maui
export HDF5_USE_FILE_LOCKING=FALSE

# optional, may improve performance
module load craype-hugepages2M

# run real
srun --kill-on-bad-exit --output=real.log ./real.exe

# run wrf
srun --kill-on-bad-exit --output=wrf.log ./wrf.exe
```

The `srun` argument `--kill-on-bad-exit` should ensure the entire job is killed
if any individual task fails. Without this option, the WRF job will stay alive
until the wall limit is reached but won't actually do anything.

#### Parallel netCDF

For some model configurations enabling parallel IO can be beneficial. By
default WRF uses serial netCDF IO, which can be verified by looking in
the *namelist.input* file for the *io\_form\_\** variables (these will
mostly be in the *time\_control* section of the namelist). If these
variables are set to "2" then they will use serial netCDF. Setting them
to 11 will use parallel netCDF instead. It is also recommended (possibly
required) to set *nocolons = .true.* in the *time\_control* section of
the namelist when using parallel IO.


### Building WPS on Māui

Download WPS:

``` sh
wget https://github.com/wrf-model/WPS/archive/v4.2.tar.gz
tar xf v4.2.tar.gz
cd WPS-4.2
```

Load environment modules and set up the build environment (here we will
build with the Intel compiler). We will build WPS using dynamic linking
so that we can link against the system JasPer shared library.

``` sl
# load PrgEnv-intel (this assumes you currently have PrgEnv-cray loaded)
module switch PrgEnv-cray PrgEnv-intel

# load dependencies
module load cray-netcdf cray-hdf5 cray-parallel-netcdf

# the following two lines are optional and may improve performance
module switch craype-x86-skylake craype-broadwell
module load craype-hugepages2M

export NETCDF=$NETCDF_DIR
export HDF5=$HDF5_DIR
export PNETCDF=$PARALLEL_NETCDF_DIR
export JASPERLIB=/usr/lib/libjasper.so.1
export JASPERINC=/usr/include/jasper/jasper.h
export WRF_DIR=../WRF-4.1.1
export CRAYPE_LINK_TYPE=dynamic
```

Configure WPS:

``` sh
./configure
# choose option 39 - Cray XC Intel parallel build
```

This creates the *configure.wps* file, which can be edited in a similar
way to *configure.wrf* above, if desired.

Now compile WPS:

``` sh
./compile >& log.compile
```

Check that the executables were successfully created: *geogrid.exe*,
*ungrib.exe* and *metgrid.exe*.

### Running WPS on Māui

Both *geogrid* and *metgrid* are parallel applications and can be run on
Māui compute nodes. However, *ungrib* is serial and should not be run on
a compute node unless it is very quick to finish. Alternatively you
could run *ungrib* on an interactive/login node if it will not take up
many resources, or you could compile WRF and WPS on a Māui Ancillary
node and run it there.

Note that WPS does a lot of file IO and therefore probably won't scale
up to as many processes as WRF.

This example shows running *geogrid* in a Slurm job:

``` sl
#!/bin/bash -e
#SBATCH --job-name=wps
#SBATCH --time=01:00:00
#SBATCH --ntasks=40
#SBATCH --hint=nomultithread

# need to specify modules as we linked dynamically
module unload PrgEnv-cray PrgEnv-intel PrgEnv-gnu
module load PrgEnv-intel cray-netcdf cray-hdf5 cray-parallel-netcdf

# the following two lines are optional and may improve performance
module switch craype-x86-skylake craype-broadwell
module load craype-hugepages2M

# important, required on Maui
export HDF5_USE_FILE_LOCKING=FALSE

# run geogrid
srun --output=geogrid.log ./geogrid.exe
```
