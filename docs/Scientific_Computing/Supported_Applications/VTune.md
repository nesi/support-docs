---
created_at: '2020-01-15T21:56:01Z'
hidden: false
position: 14
tags: []
title: VTune
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001332675
zendesk_section_id: 360000040076
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

## What is VTune?

VTune is a tool that allows you to quickly identify where most of the
execution time of a program is spent. This is known as profiling. It is
good practice to profile a code before attempting to modify the code to
improve its performance. VTune collects key profiling data and presents
them in an intuitive way.  Another tool that provides similar
information is [ARM
MAP](../../Scientific_Computing/Profiling_and_Debugging/Profiler-ARM_MAP.md).

## How to use VTune

We'll show how to profile a C++ code with VTune - feel free to choose
your own code instead. Start with 

``` sh
git clone https://github.com/pletzer/fidibench
```

and build the code using the "gimkl" tool chain

``` sh
cd fidibench
mkdir build
cd build
module load gimkl CMake
cmake ..
make
```

This will compile a number of executables. Note that VTune does not
require one to apply a special compiler switch to profile. You can
profile an existing executable if you like. We choose "upwindCxx" as the
executable to profile. It is under upwind/cxx, so

``` sh
cd upwind/cxx
```

Run the executable with

``` sh
module load VTune
srun --ntasks=1 --cpus-per-task=2 --hint=nomultithread amplxe-cl -collect hotspots -result-dir vtune-res ./upwindCxx -numCells 256 -numSteps 10
```

Executable "upwindCxx" takes arguments "-numCells 256" (the number of
cells in each dimension) and  "-numSteps 10" (the number of time
steps). Note the command "amplxe-cl -collect hotspots -result-dir" which
was inserted before the executable. The output may look like

Top Hotspots

Function                                    Module          CPU Time

------------------------------------------  --------------  --------

Upwind&lt;(unsigned long)3&gt;::advect.\_omp\_fn.1  upwindCxx       
25.979s

\_int\_free                                   libc.so.6         9.170s

operator new                                libstdc++.so.6    6.521s

free                                        libmpi.so.12      0.300s

indicating that the vast majority of time is spent in the "advect"
method (26s), with significant amounts of time spent allocating (6.5s)
and deallocating (9.2s) memory.

##  Drilling further into the code

Often this is enough to give you a feel for where the code can be
improved. To explore further you can fire up

``` sh
amplxe-gui &
```

Go to the bottom and select "Open Result...", choose the directory where
the profiling results are saved and click on the .amplxe file. The
summary will look similar to the above table. However, you can now dive
into selected functions to get more information. Below we see that 16.5
out of 26 seconds were spent starting the two OpenMP threads.
