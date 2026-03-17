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

## 1. Build TAU on Mahuika

Load the required modules for the compiler toolchain and MPI. TAU should be compiled against the same compiler and MPI toolchain that will be used to build and run the application. Here we use `foss/2023a`, adapt as required.


```bash
module purge
module load gimkl/2022a CMake
```

Confirm the versions:
```bash
g++ --version
mpicxx --version
```

We'll use `spack` to install TAU. Refer to https://spack.readthedocs.io/en/latest/getting_started.html on how to install `spack`. We recommend that you intall `spack` in your project directory. Once installed:
```bash
spack install tau@2.34.1 %gcc@11.3.0
```
then load your environment
```bash
spack load tau@2.34.1
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
# required otherwise cmake hangs 
export TAU_OPTIONS="-optNoRevert -optVerbose -optCompInst"
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
export TRACEDIR=traces
mkdir -p $TRACEDIR
mpiexec -n 4 ./upwindMpiCxx
cd $TRACEDIR
tau_treemerge.pl
rm -f tau.trc tau.edf
tau_treemerge.pl
tau2slog2 tau.trc tau.edf -o upwindMpiCxx.slog2
jumpshot upwindMpiCxx.slog2
```
