---
created_at: '2018-04-23T00:52:59Z'
hidden: false
label_names:
- info
- software
- application
- cs400
- XC50
position: 19
title: Programming environment differences between Maui and Mahuika
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000164576
zendesk_section_id: 360000040056
---

The compile environment of Māui and Mahuika have various similarities,
but also significant differences. Both systems are configured with the
Cray Programming Environment (CPE), but these vary in detail. In general
we distinguish, between the XC50 part of Māui and the CS (Mahuika,
Mahuika Ancillary Nodes, and Māui Ancillary nodes) systems.

Table 1: The Cray Programming Environment on Māui and Mahuika. Black
text indicates components common to both systems, green to components
only available on Mahuika, and blue to components only available on Māui
XC part.  

<table class="table table-striped table-bordered">
<thead>
<tr>
<th>
Programming Languages

</th>
<th>
Programming Models

</th>
<th>
Compilers

</th>
<th>
Tools

</th>
<th>
Optimised Scientific Libraries

</th>
<th>
I/O Libraries

</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">
Fortran

C

C++

Chapel

</td>
<td>
Distributed Memory:

MPI Support:

· Intel MPI<sup>1</sup>

· MVAPICH2<sup>1</sup>

· OpenMPI<sup>1</sup>

· MPICH<sup>1</sup>

· Cray-MVAPICH2<sup>1</sup> 

Cray MPT<sup>2</sup>:

· MPI

</td>
<td>
· Cray Compiling Environment (CCE)

· GNU

· Intel

</td>
<td>
Performance Analysis:

· CrayPat & Cray Apprentice2

· Allinea MAP

· Intel Vtune Amplifier XE, Advisor, Trace Analyser & Collector

</td>
<td>
Dense:

· BLAS

· LAPACK

· ScaLAPACK

· Iterative Refinement Tool

</td>
<td rowspan="4">
NetCDF<sup>2</sup>

HDF<sup>2</sup>

</td>
</tr>
<tr>
<td>
Shared Memory

· OpenMP 4.0

· OpenACC 2.0

</td>
<td>
Environment Setup

· Modules

· Lmod<sup>1</sup>

 

</td>
<td>
Porting Tools:

· Reveal

· CCDB

</td>
<td>
FFT:

· FFTW

</td>
</tr>
<tr>
<td>
PGAS

· UPC

· CAF

· CoArray C++

</td>
<td>
 

</td>
<td>
Debuggers:

· lgdb

· Allinea DDT

· ATP<sup>2</sup>

· STAT<sup>2</sup>

</td>
<td>
Sparse:

· Cray PETSc (with CASK)<sup>2</sup>

· Cray Trilinos (with CASK)<sup>2</sup>

</td>
</tr>
<tr>
<td>
 

</td>
<td>
 

</td>
<td>
Data Analytics

· Urika XC Data Analytics<sup>2</sup>

· Cray Graph Engine<sup>2</sup>

</td>
<td>
 

</td>
</tr>
</tbody>
</table>
**Notes:**

1.  <sup>1</sup>Only available on Mahuika HPC Cluster, Mahuika Ancillary
    Nodes and Māui Ancillary nodes
2.  <sup>2</sup>Only available on Māui Supercomputer.
3.  On Māui (XC50) the Modules framework is used to simplify access to
    the various compiler suites and libraries. To access a particular
    compiler suite, you simply load (or switch to) the appropriate
    programming environment module using the command PrgEnv-X (where X
    is one of gnu, intel, or cray). This facility is not available on
    the Mahuika HPC Cluster, Mahuika Ancillary Nodes and Māui Ancillary
    nodes.
4.  [Intel Parallel Studio XE Cluster
    Edition](https://software.intel.com/en-us/node/685016) for Linux
    will be installed on the Mahuika HPC Cluster, Mahuika Ancillary
    Nodes and Māui Ancillary nodes.
5.  Intel Parallel Studio XE Professional Edition for CLE will be
    installed installed on Māui.

## Key Similarities  between CPE on XC50 and CS400/500s

As shown in the table above, Cray provides a list of tools, libraries,
and compilers for both platforms. The Cray compiler environment comes
with the compiler, basic numeric libraries, automatically including
compile and link flags for system architecture and libraries
(enabled/disabled by loading modules), and the Cray performance analysis
tools (CrayPAT)

## Key Differences between CPE on XC50 and CS400/500s

There are many similarities between the XC and CS programming
environments (compilers and many tools and libraries are the same or at
least similar), but also some important differences that affect how a
user interacts with the system when building an application code:

-   The XC platform uses compiler drivers (“ftn”, “cc”, “CC”), users
    should not use compilers directly. The CS platforms have compiler
    drivers only for Cray compiler. For GNU and Intel compilers, users
    run “gfortran”, “ifort”, “gcc”, “icc” etc.;
-   On the XC platform, a compiler is chosen by switching to its
    corresponding “PrgEnv-xxx” module. This will also switch
    automatically the version of the loaded Cray provided libraries,
    e.g., the cray-netcdf and cray-fftw library modules – no equivalent
    is available on the CS platforms; On the CS platforms the main
    software stack is based on Easybuild toolchains. The default one is
    “gimkl”, including GCC, Intel MPI, and Intel MKL.
-   The XC platform requires everyone to use Cray-MPI, but on the CS
    platform, users can choose to use various MPI libraries;
-   Getting rid of all modules via “module purge” renders an XC session
    unusable (a list of ~20 modules are necessary to guarantee
    operation). On CS there are only few modules necessary, the main one
    is called “NeSI”, providing the NeSI software stack and slurm
    module;
-   The XC platform defaults to static linking, the CS platform to
    dynamic linking;

In summary, compilers, as well as various tools and libraries are common
across both platforms. However, there are important differences in how
the programming environment is used, requiring users to familiarise
themselves with each platform. For more information see the specific
user guides for [Mahuika (and Ancillary
nodes)](https://nesi.github.io/hpc_training/lessons/maui-and-mahuika/building-code-mahuika)
and [ Māui
XC50](https://nesi.github.io/hpc_training/lessons/maui-and-mahuika/building-code-maui).

 

 

 

 

 
