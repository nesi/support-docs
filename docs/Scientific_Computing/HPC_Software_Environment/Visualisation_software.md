NeSI provides a variety of visualisation software solutions via modules.
Available software and software versions vary between the Mahuika and
Māui Ancil systems. Additional software can be provided upon request,
see section [Supported
Applications](https://support.nesi.org.nz/hc/en-gb/sections/360000040076-Supported-Applications).

Most software only requires a CPU node to run, but some software, in
particular high-performance 3D visualisation software, can utilise a GPU
node for better performance. Where possible, both CPU and GPU variants
of the same software are provided for maximum flexibility; please make
sure to select the correct module version as described below.

Apart from interactive operation, many visualisation solutions also
support batch mode ("headless") operation, allowing users to submit
large visualisation jobs to the HPC.

In the following installed packages are listed for:

-   Scripting Languages with Visualisation Capabilities

-   2D Visualisation Software

-   3D Visualisation Software

# Scripting Languages with Visualisation Capabilities

## Python

The Python language comes with packages such as "matplotlib" for
general-purpose 2D visualisation, or "vtk" (see VTK section on this
page) for 3D visualisation.

### Available Modules

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

##  

## R

The R language comes with built-in 2D plotting capabilities that can be
extended with additional packages.

### Available Modules

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

##  

## NCL

The NCAR Command Language provides visualisation capabilities which are
mostly used in the weather and climate fields.

### Available Modules

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

 

## MATLAB

The MATLAB programming language comes with built-in visualisation
capabilities.

### Available Modules

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

#  

# 2D Visualisation Software

## IRIS

IRIS is a Python-based visualisation tool that is mainly used in the
weather and climate fields.

### Available Modules

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

##  

## Ncview

Ncview is a visual browser for netCDF files.

### Available Modules

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
</tbody>
</table>

##  

## XCONV

XCONV is a visual browser for netCDF and Unified Model format files.

### Available Modules

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

#  

# 3D Visualisation Software

## ParaView

[ParaView](https://www.paraview.org/) is a high-performance 3D
visualisation tool. The headless versions only provide ParaView Server,
which can operate in batch mode, as well as in client-server operation.

For interactive sessions, it is highly recommended to use ParaView with
the NICE DCV cloud visualisation software for best performance.
Client-server mode, where a ParaView GUI runs on a local machine and
connects to a ParaView server on the HPC, is also an option but requires
much more network bandwidth than [NICE
DCV](https://support.nesi.org.nz/hc/en-gb/articles/360000719156) and
thus may be slower.

### Parallelisation

The CPU based versions of ParaView use the OpenSWR rasteriser as well as
the OSPRay ray tracer for rendering graphics. These support parallel
operation for better performance, but are configured to only use a
single core by default. Run the following commands *before* launching
ParaView GUI or ParaView Server if you want to use more cores (depending
on the number of cores available in your session):

    export KNOB_MAX_WORKER_THREADS=<number of cores>
    export OSPRAY_THREADS=<number of cores>

ParaView Server also supports parallel execution using MPI, see "Setting
up Client-Server Mode" below.

### Available Modules

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
</tbody>
</table>

###  

### Setting up Client-Server Mode

If you want to use ParaView in client-server mode, use the following
setup:

-   Load one of the ParaView Server modules listed above and launch the
    server in your interactive visualisation session on the HPC:

<!-- -->

    mpiexec -np <number of MPI ranks> pvserver

-   Create an SSH tunnel for port "11111" from the HPC to your local
    machine using, e.g., the ssh program (Linux and MacOS) or MobaXterm
    (Windows)
-   Launch the ParaView GUI on your local machine and go to "File &gt;
    Connect"
-   Click on "Add Server", choose server type "Client / Server", host
    "localhost" (as we will be using the SSH tunnel), and port "11111",
    then click on "Configure"
-   Select the new server and click on "Connect"

## VisIt

VisIt is a high-performance 3D visualisation tool. At this point, only
GUI-based interactive sessions on CPUs via NICE DCV are supported, GPU
support and client-server operation will be added later.

### Available Modules

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

##  

## VTK

The Visualization ToolKit (VTK) can be used for 3D visualisation in
various programming languages, in particular with the Python scripting
language.

### Available Modules

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
</tbody>
</table>

 
