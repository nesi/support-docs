---
created_at: 'Tue 17 Mar 2026 10:52:33 NZDT'
tags: []
title: 'Tracing MPI applications with Tau'
vote_count: 1
vote_sum: -1
zendesk_article_id: 4405523725583
zendesk_section_id: 360000278935
---


This guide shows how to use the **TAU Performance System** to trace an MPI-based C++ application on the Mahuika HPC cluster. Tracing 
records a time-ordered sequence of events during program execution. Each event is timestamped and written to a trace file so that the exact runtime behaviour of the program can be reconstructed. Events may include entry and exit of functions, MPI communication calls and synchronization events (barriers, waits). Tracing is particularly for identifying load imbalance, communication bottlencks and idle time in appications.

The example uses the **fidibench** benchmark and its `upwindMpiCxx` executable.

The workflow consists of four steps:

1. Build TAU for the desired compiler toolchain.
2. Compile the application using TAU compiler wrappers.
3. Run the application with tracing enabled.
4. Inspect the results with TAU analysis tools.

## Prerequisites

Load the required modules for the compiler toolchain and MPI. TAU should be compiled against the same compiler and MPI toolchain that will be used to build and run the application. Here we use `foss/2023a`, adapt as required.


```bash
module purge
module load foss/2023a CMake
```

Confirm the versions:
```bash
g++ --version
mpicxx --version
```

## 1. Build TAU on Mahuika

Download TAU:
```bash
wget http://tau.uoregon.edu/tau.tgz
tar xf tau.tgz
cd tau-*
wget http://tau.uoregon.edu/ext.tgz
tar xf ext.tgz
wget http://tau.uoregon.edu/pdt_lite.tar.gz
tar xf pdt_lite.tar.gz
cd pdtoolkit*
make && make install
cd ..
```
Set `TAU_HOME`, the location where TAU will be installed (change!), e.g.:
```bash
export TAU_HOME=/nesi/project/nesi99999/$USER/tau
```

Configure TAU for MPI tracing using the GNU toolchain:
```bash
./configure \
  -pdt=$PWD/pdtoolkit-3.25.2 \
  -bfd=download -dwarf=download -unwind=download -iowrapper \
  -prefix=$TAU_HOME \
  -mpi \
  -TRACE \
  -PROFILE \
  -cc=gcc \
  -c++=g++ \
  -fortran=gfortran
```
Build and install:
```bash
make install
```
Add TAU to your environment:
```bash
export PATH=$TAU_HOME/bin:$PATH
```
Locate the TAU MPI makefile:
```bash
ls $HOME/tau/lib/Makefile.tau*
```
Set the environment variable:
```bash
export TAU_MAKEFILE=$HOME/tau/lib/Makefile.tau-mpi-pdt
```
Verify the TAU compiler wrappers are available:
```bash
which tau_cxx.sh
```

## 2. Obtain the example code (fidibench)

Clone the fidibench benchmark repository:
```bash
git clone https://github.com/pletzer/fidibench.git
cd fidibench
mkdir build-tau
cd build-tau
CXX=tau_cxx.sh MPI_CXX=tau_cxx.sh cmake ..
```
The MPI example used in this guide is the executable `upwindMpiCxx`
```bash
cd upwind/cxx
make CXX=tau_cxx.sh VERBOSE=1 upwindMpiCxx
```

## 3. Run the application and analyse the results

```bash
export TAU_TRACE=1
export TAU_PROFILE=0
export TAU_TRACE_DIR=traces
mkdir -p $TAU_TRACE_DIR
mpiexec -n 4 ./upwindMpiCxx
```
