---
created_at: '2019-04-30T00:21:48Z'
hidden: false
position: 1
tags: []
title: 'Profiler: ARM MAP'
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000930396
zendesk_section_id: 360000278935
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

-   [Introduction to profiling](#introduction-to-profiling)
-   [Profiling test cases](#h_23e5a159-4e9c-4f25-9395-53f03e1187f7)
-   [MAP profiler](#h_e444a43e-f0a5-45a5-8ed2-8bd06abae1a9)
-   [MAP “Express Launch”](#using-the-express-launch)
-   [MAP GUI launch](#h_f78992f8-3f55-4b6f-ac5f-8bc82ff16873)
-   [MAP Profile](#map-profile)

The ARM (previously known as Allinea) provides a package called *forge*,
which consists of a debugger, DDT and a profiler, MAP.

# Introduction to profiling

Profiling tools help you understand how much resources are consumed
during run time. This can be time, memory, or MPI communication. One
main goal is to understand in which parts of your code most time is
spent. Depending on the profiler and the applied methods, profiles can
be gathered on basis of functions, loops within functions, or source
code lines. Profiling information is important for optimising code, as
it enables you to focus your efforts on improving the parts of the code
that will result in the biggest gains in performance.

# Profiling test cases

During a optimisation process profiling will be used regularly to
monitor the behaviour and change in behaviour of the code. Therefore, it
is advisable to have a representative but reasonable short test case. It
should trigger all the desired features of the code. But keep in mind
that with a reduced run time (e.g. fewer iterations) other parts of the
code could become more dominant (e.g. initialisation phase).
Furthermore, due to possible overhead from the profiling tool, the code
could run slower than normal.

# MAP profiler

MAP is a commercial product, which can profile parallel, multi-threaded
and single-threaded C/C++, Fortran, as well as Python code. MAP supports
codes with OpenMP threads and/or MPI communication and can be used
without code modification.

MAP can be launched with a graphical user interface (GUI Launch) or
without GUI (Express Launch). With the GUI the user specifies all the
parameters including executables, options and parallelisation parameters
in a guided form, while with the Express Launch a pre-existing script is
modified. The “Express Launch”, is preferable especially for jobs in
complex scripts and workflows.

In either case, the analysis of the profiling data will be undertaken in
the MAP GUI. This conveniently provides access to different metrics and
allows the user to navigate through different levels of details,
browsing through the code, and focusing on specific functions, loops and
source code lines.  See section [MAP profile](#map-profile) below.

There is also an [Arm Forge
Client](https://developer.arm.com/tools-and-software/server-and-hpc/arm-architecture-tools/downloads/download-arm-forge)
you can download to your local machine. Therewith you can browse through
your downloaded profiling data or even start your profiling/debug tasks
from remote (not described in detail here).

**Note:** If you want to use the GUI on the NeSI systems, please
remember to start your ssh session using X11 forwarding (e.g. using the
`ssh -Y` option).

# MAP “Express Launch”

To use MAP we need to load the *forge* module in our batch script and
add `map --profile` in front of the parallel run statements. For
example:

Upon execution, a `.map` file will be generated. The results can be
viewed, for instance, with

(the `.map` file name will vary with each run.) See section [MAP
profile](#map-profile) below for how to interpret the results.

# MAP GUI launch

The GUI can be started after loading `module load forge` and launching

[![Arm MAP
main](../../assets/images/Profiler-_ARM_MAP.png)](https://nesi.github.io/perf-training/python-scatter/images/ARM_MAP_main.png)

Click on “PROFILE”.

![MAP\_profile\_python.PNG](../../assets/images/Profiler-_ARM_MAP.PNG)

In the profile menu we need to specify the *executable/application* (in
this case `python`), the arguments (here `scatter.py` and any additional
options and arguments if necessary). Select the working directory,
number of MPI processes, and OpenMP threads. Furthermore, the “submit to
queue” parameter needs to be checked, for example the
`--hint=nomultithread` can be specified there. In the environment
Variables block, e.g. modules could be loaded or variables defined.

After *submit*ting, MAP will wait until the job is allocated, connect to
the processes, run the program, gather all the data and present the
profile information.

 

# MAP Profile

By default the profile window is divided into the following three main
sections (click on picture to enlarge).

[![example-map-scatter](../../assets/images/Profiler-_ARM_MAP_0.png)](https://nesi.github.io/perf-training/python-scatter/images/ARM_MAP_scatter_mpi.png)

On top, various metrics can be selected in the “Metrics” menu. In the
middle part, a source code navigator connects line by line source code
with its profiling data. Most interesting is the profiling table at the
bottom, which sorts the most time consuming parts of the program,
providing function names, source code and line numbers.

There are various options to get even more information.

In the top part the metrics graphs can be changed to:

-   Activity timeline
-   CPU instructions
-   CPU Time
-   IO
-   Memory
-   MPI

using the *Metrics* Menu*.*

As an example, “CPU instructions” presents the usage of different
instruction sets during the program run time.

[![example-map-scatter\_CPU](../../assets/images/Profiler-_ARM_MAP_1.png)](https://nesi.github.io/perf-training/python-scatter/images/ARM_MAP_scatter_mpi_CPU.png)

The lower part can also be used to check the *application output* or
show statistics on basis of *files* or *functions*.

**Note:** often you can get additional information while hovering with
your mouse over a certain item.
