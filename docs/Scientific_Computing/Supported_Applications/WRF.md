---
created_at: '2020-11-02T23:31:38Z'
hidden: false
position: 9
tags: []
title: WRF
vote_count: 1
vote_sum: 1
zendesk_article_id: 360002109696
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

# WRF

The Weather Research and Forecasting (WRF) Model is a next-generation
mesoscale numerical weather prediction system designed for both
atmospheric research and operational forecasting applications. It
features two dynamical cores, a data assimilation system, and a software
architecture supporting parallel computation and system extensibility.
The model serves a wide range of meteorological applications across
scales from tens of meters to thousands of kilometres.

 

Download WRF:

``` sl
cd /nesi/project/<your_project_code>
wget https://github.com/wrf-model/WRF/archive/v4.1.1.tar.gz
tar xf v4.1.1.tar.gz
```

This guide is based on WRF 4.1.1 and WPS 4.2 (it was also tested with
Polar WRF 4.1.1 but for that, you would need to apply the Polar WRF and
WPS patches before compiling).

WRF needs NetCDF, NetCDF-Fortran, PnetCDF and their dependencies to be
installed. On Māui, these are available as modules. On Mahuika, we
recommend to download these packages and build them by hand
(instructions are provided below).

 

# WRF on Mahuika

 

## Environment on Mahuika

We'll use the Intel compiler and Intel MPI library. 

``` sl
module purge
module load HDF5/1.12.2-iimpi-2022a
```

Although NeSI has NetCDF modules installed, WRF wants the C and Fortran
NetCDF libraries, include files and modules all installed under the same
root directory. Hence we build those by hand.

 

## Building WRF dependencies on Mahuika

Copy-paste the commands below to build WRF on Mahuika:

``` sl
# create build directory for WRF's dependencies
export WRF_DEPS_DIR=$PWD/wrf-deps
mkdir $WRF_DEPS_DIR
cd $WRF_DEPS_DIR

# required for building and running
export LD_LIBRARY_PATH=$WRF_DEPS_DIR/lib:$LD_LIBRARY_PATH

# to access the nc-config anf nf-config commands
export PATH=$WRF_DEPS_DIR/bin:$PATH

# set the compilers
export CC=icc
export CXX=icc
export FC=ifort
export F77=ifort
export MPICC=mpiicc
export MPICXX=mpiicc
export MPIF77=mpiifort
export MPIF90=mpiifort

# now install the dependencies

# netcdf-c
wget https://downloads.unidata.ucar.edu/netcdf-c/4.9.2/netcdf-c-4.9.2.tar.gz
tar xf netcdf-c-4.9.2.tar.gz
cd netcdf-c-4.9.2/
./configure --prefix=$WRF_DEPS_DIR
make & make install
cd ..

# netcdf-fortran
wget https://downloads.unidata.ucar.edu/netcdf-fortran/4.6.1/netcdf-fortran-4.6.1.tar.gz
tar xf netcdf-fortran-4.6.1.tar.gz
cd netcdf-fortran-4.6.1
CPPFLAGS="$(../bin/nc-config --cflags)" LDFLAGS="$(../bin/nc-config --libs)" \
./configure --prefix=$WRF_DEPS_DIR
make & make install
cd ..

# pnetcdf
wget https://parallel-netcdf.github.io/Release/pnetcdf-1.12.3.tar.gz
tar xf pnetcdf-1.12.3.tar.gz
cd pnetcdf-1.12.3
./configure --prefix=$WRF_DEPS_DIR --with-netcdf4=$WRF_DEPS_DIR
make & make install
cd ..

# back to the top directory
cd ..
```

 

Then proceed to configure WRF by setting

``` sl
export NETCDF=$WRF_DEPS_DIR
export HDF5=$WRF_DEPS_DIR
export PNETCDF=$WRF_DEPS_DIR
```

``` sl
cd WRF-4.1.1
./configure
[select 15]
```

and build the code with

``` sl
./compile em_real >& log.compile
```

This may take several hours to compile. Check the log file to ensure
that the compilation was successful. 

 

## Running WRF on Mahuika

 

An example Slurm script for running WRF on Mahuika extension, which can
be submitted with *sbatch name\_of\_script.sl*:

``` sl
#!/bin/bash -e
#SBATCH --job-name=wrf
#SBATCH --time=01:00:00
#SBATCH --ntasks=240
#SBATCH --hint=nomultithread
#SBATCH --partition=milan

module purge
module load HDF5/1.12.2-iimpi-2022a
module list
export LD_LIBRARY_PATH=$WRF_DEPS_DIR/lib:$LD_LIBRARY_PATH

# run real
srun --output=real.log ./real.exe

# run wrf
srun --output=wrf.log ./wrf.exe
```

###  

 

# WRF on Māui

## Building WRF

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

``` sl
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

``` sl
./compile em_real >& log.compile
```

It is important to check the output in *log.compile* as the command will
not exit with an error if it fails. Check the end of the log file for a
message saying compilation was successful. You could also check the
timestamps of the executables in the *main* subdirectory
(*main/wrf.exe*, *main/real.exe*, etc).

## Running WRF

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
srun --output=real.log ./real.exe

# run wrf
srun --output=wrf.log ./wrf.exe
```

### Parallel netCDF

For some model configurations enabling parallel IO can be beneficial. By
default WRF uses serial netCDF IO, which can be verified by looking in
the *namelist.input* file for the *io\_form\_\** variables (these will
mostly be in the *time\_control* section of the namelist). If these
variables are set to "2" then they will use serial netCDF. Setting them
to 11 will use parallel netCDF instead. It is also recommended (possibly
required) to set *nocolons = .true.* in the *time\_control* section of
the namelist when using parallel IO.

## Building WPS

Download WPS:

``` sl
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

``` sl
./configure
# choose option 39 - Cray XC Intel parallel build
```

This creates the *configure.wps* file, which can be edited in a similar
way to *configure.wrf* above, if desired.

Now compile WPS:

``` sl
./compile >& log.compile
```

Check that the executables were successfully created: *geogrid.exe*,
*ungrib.exe* and *metgrid.exe*.

## Running WPS

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
