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
support batch mode (\"headless\") operation, allowing users to submit
large visualisation jobs to the HPC.

In the following installed packages are listed for:

-   Scripting Languages with Visualisation Capabilities

-   2D Visualisation Software

-   3D Visualisation Software

# Scripting Languages with Visualisation Capabilities

## Python

The Python language comes with packages such as \"matplotlib\" for
general-purpose 2D visualisation, or \"vtk\" (see VTK section on this
page) for 3D visualisation.

### Available Modules

  ------------------------------- ------------- ---------------- -------------------------------------------
  **Module Name**                 **Mahuika**   **Māui Ancil**   **Comment**
  Anaconda2/5.2.0-GCC-7.1.0                     ✔                Anaconda distribution of Python 2
  Anaconda2/2019.10-GCC-7.1.0                   ✔                Anaconda distribution of Python 2
  Anaconda3/5.2.0-GCC-7.1.0                     ✔                Anaconda distribution of Python 3
  Anaconda3/2019.03                             ✔                Anaconda distribution of Python 3
  Anaconda3/2019.07-gimkl-2018b                 ✔                Anaconda distribution of Python 3
  Anaconda3/2020.02-GCC-7.1.0                   ✔                Anaconda distribution of Python 3
  Miniconda3/4.4.10               ✔                              Minimal Anaconda distribution of Python 3
  Miniconda3/4.5.12               ✔                              Minimal Anaconda distribution of Python 3
  Miniconda3/4.7.10               ✔                              Minimal Anaconda distribution of Python 3
  Miniconda3/4.8.2                ✔                              Minimal Anaconda distribution of Python 3
  Miniconda3/4.8.3                ✔                              Minimal Anaconda distribution of Python 3
  Miniconda3/4.9.2                ✔                              Minimal Anaconda distribution of Python 3
  Python-GPU/3.6.3-gimkl-2017a    ✔                              GPU-enabled Python 3
  Python-Geo/2.7.14-gimkl-2017a   ✔                              Python 2 for geospatial applications
  Python-Geo/2.7.16-gimkl-2018b   ✔                              Python 2 for geospatial applications
  Python-Geo/3.6.3-gimkl-2017a    ✔                              Python 3 for geospatial applications
  Python-Geo/3.7.3-gimkl-2018b    ✔                              Python 3 for geospatial applications
  Python-Geo/3.8.2-gimkl-2020a    ✔                              Python 3 for geospatial applications
  Python/2.7.14-gimkl-2017a       ✔                              Python 2 base packages
  Python/2.7.16-gimkl-2018b       ✔                              Python 2 base packages
  Python/2.7.16-intel-2018b       ✔                              Python 2 base packages
  Python/2.7.18-gimkl-2020a       ✔                              Python 2 base packages
  Python/3.6.3-gimkl-2017a        ✔                              Python 3 base packages
  Python/3.7.3-gimkl-2018b        ✔                              Python 3 base packages
  Python/3.8.1-gimkl-2018b        ✔                              Python 3 base packages
  Python/3.8.2-gimkl-2020a        ✔                              Python 3 base packages
  Python/3.9.5-gimkl-2020a        ✔                              Python 3 base packages
  ------------------------------- ------------- ---------------- -------------------------------------------

##  

## R

The R language comes with built-in 2D plotting capabilities that can be
extended with additional packages.

### Available Modules

  ------------------------- ------------- ---------------- -------------------------------
  **Module Name**           **Mahuika**   **Māui Ancil**   **Comment**
  R/3.4.2-gimkl-2017a        ✔                             R base package
  R/3.5.0-gimkl-2017a        ✔                             R base package
  R/3.5.1-gimkl-2017a       ✔                              R base package
  R/3.5.3-gimkl-2018b       ✔                              R base package
  R/3.6.1-gimkl-2018b       ✔                              R base package
  R/3.6.2-gimkl-2020a       ✔                              R base package
  R/4.0.1-gimkl-2020a       ✔                              R base package
  R/3.5.1-gimkl-2018b                     ✔                R base package
  R/3.6.1-gimkl-2018b                     ✔                R base package
  R-Geo/3.6.1-gimkl-2018b   ✔                              R for geospatial applications
  R-Geo/3.6.2-gimkl-2020a   ✔                              R for geospatial applications
  R-Geo/4.0.1-gimkl-2020a   ✔                              R for geospatial applications
  Rstudio/1.1.456                         ✔                Rstudio IDE
  ------------------------- ------------- ---------------- -------------------------------

##  

## NCL

The NCAR Command Language provides visualisation capabilities which are
mostly used in the weather and climate fields.

### Available Modules

  ----------------------- ------------- ---------------- ------------------
  **Module Name**         **Mahuika**   **Māui Ancil**   **Comment**
  NCL/6.2.0-GCC-7.1.0                    ✔               NCL base package
  NCL/6.4.0-GCC-7.1.0                    ✔               NCL base package
  NCL/6.6.2-intel-2018b    ✔                             NCL base package
  ----------------------- ------------- ---------------- ------------------

 

## MATLAB

The MATLAB programming language comes with built-in visualisation
capabilities.

### Available Modules

  ----------------- ------------- ---------------- -------------
  **Module Name**   **Mahuika**   **Māui Ancil**   **Comment**
  MATLAB/2016b      ✔             ✔                 
  MATLAB/2017b      ✔             ✔                 
  MATLAB/2018b      ✔             ✔                 
  MATLAB/2019b      ✔             ✔                 
  MATLAB/2020a      ✔                               
  MATLAB/2020b      ✔                               
  MATLAB/2021a      ✔                               
  ----------------- ------------- ---------------- -------------

#  

# 2D Visualisation Software

## IRIS

IRIS is a Python-based visualisation tool that is mainly used in the
weather and climate fields.

### Available Modules

  ----------------------------- ------------- ---------------- ------------------
  **Module Name**               **Mahuika**   **Māui Ancil**   **Comment**
  Anaconda2/5.2.0-GCC-7.1.0                    ✔               IRIS v1.13.0
  Anaconda2/2019.10-GCC-7.1.0                 ✔                IRIS v2.2.1.dev0
  Anaconda3/5.2.0-GCC-7.1.0                    ✔               IRIS v1.13.0 
  Anaconda3/2019.03                           ✔                IRIS v1.13.0
  Anaconda3/2020.02-GCC-7.1.0                 ✔                IRIS v2.4.0
  ----------------------------- ------------- ---------------- ------------------

##  

## Ncview

Ncview is a visual browser for netCDF files.

### Available Modules

  -------------------------- ------------- ---------------- -------------
  **Module Name**            **Mahuika**   **Māui Ancil**   **Comment**
  ncview/2.1.7-gimkl-2018b   ✔                               
  NCVIEW/2.1.8-GCC-7.1.0                    ✔                
  -------------------------- ------------- ---------------- -------------

##  

## XCONV

XCONV is a visual browser for netCDF and Unified Model format files.

### Available Modules

  ----------------- ------------- ---------------- -------------
  **Module Name**   **Mahuika**   **Māui Ancil**   **Comment**
  XCONV/1.93                       ✔                
  ----------------- ------------- ---------------- -------------

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

ParaView Server also supports parallel execution using MPI, see
\"Setting up Client-Server Mode\" below.

### Available Modules

  ------------------------------------------ ------------- ---------------- ---------------------------------------------
  **Module Name**                            **Mahuika**   **Māui Ancil**   **Comment**
  ParaView/5.3.0-gimkl-2017a                 ✔                               
  ParaView/5.4.1-gimkl-2017a-Python-2.7.14   ✔                               
  ParaView/5.4.1-gimkl-2018b-Python-2.7.16   ✔                               
  ParaView/5.4.1-gimpi-2018b                 ✔                               
  ParaView/5.5.2-gimpi-2018a-Server-EGL                    ✔                Headless version for GPUs, no GUI operation
  ParaView/5.5.2-gimpi-2018b-GUI-Mesa                      ✔                GUI version for CPUs, no headless operation
  ParaView/5.5.2-gimpi-2018b-Server-OSMesa                 ✔                Headless version for CPUs, no GUI operation
  ParaView/5.6.0-gimkl-2018b-Python-3.7.3                                    
  ParaView/5.6.0-gimpi-2017a-Server-OSMesa   ✔                              Headless version for CPUs, no GUI operation
  ParaView/5.6.0-gimpi-2018b                 ✔                               
  ParaView/5.6.0-gimkl-2018b-Python-3.7.3    ✔                               
  ParaView/5.9.0-gimkl-2020a-Python-3.8.2    ✔                               
  ------------------------------------------ ------------- ---------------- ---------------------------------------------

###  

### Setting up Client-Server Mode

If you want to use ParaView in client-server mode, use the following
setup:

-   Load one of the ParaView Server modules listed above and launch the
    server in your interactive visualisation session on the HPC:

<!-- -->

    mpiexec -np <number of MPI ranks> pvserver

-   Create an SSH tunnel for port \"11111\" from the HPC to your local
    machine using, e.g., the ssh program (Linux and MacOS) or MobaXterm
    (Windows)
-   Launch the ParaView GUI on your local machine and go to \"File \>
    Connect\"
-   Click on \"Add Server\", choose server type \"Client / Server\",
    host \"localhost\" (as we will be using the SSH tunnel), and port
    \"11111\", then click on \"Configure\"
-   Select the new server and click on \"Connect\"

## VisIt

VisIt is a high-performance 3D visualisation tool. At this point, only
GUI-based interactive sessions on CPUs via NICE DCV are supported, GPU
support and client-server operation will be added later.

### Available Modules

  ----------------------------------- ------------- ---------------- ----------------------
  **Module Name**                     **Mahuika**   **Māui Ancil**   **Comment**
  VisIt/2.13.3-gimpi-2018b-GUI-Mesa                 ✔                GUI version for CPUs
  ----------------------------------- ------------- ---------------- ----------------------

##  

## VTK

The Visualization ToolKit (VTK) can be used for 3D visualisation in
various programming languages, in particular with the Python scripting
language.

### Available Modules

  ------------------------------------- ------------- ---------------- ---------------------------
  **Module Name**                       **Mahuika**   **Māui Ancil**   **Comment**
  VTK/6.3.0-gimkl-2017a-Python-2.7.14   ✔                              VTK6 with Python bindings
  VTK/7.1.1-gimkl-2018b-Python-2.7.16   ✔                              VTK7 with Python bindings
  VTK/8.1.1-GCC-7.1.0-Anaconda2-5.2.0                 ✔                VTK8 with Python bindings
  ------------------------------------- ------------- ---------------- ---------------------------

 
