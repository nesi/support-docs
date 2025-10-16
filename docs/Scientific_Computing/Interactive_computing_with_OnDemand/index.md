# Interactive computing with NeSI OnDemand

## Overview

OnDemand empowers students, researchers, and industry professionals with remote and interactive web access to the HPC platforms.

## Connecting to OnDemand

!!! prerequisite
     Requires [an account](https://www.nesi.org.nz/researchers/apply-access-our-services).

Connect to OnDemand: [https://ondemand.nesi.org.nz](https://ondemand.nesi.org.nz/).

For more information see the [How-to guide](how_to_guide.md).

## Interactive applications

A number of interactive applications can be accessed through OnDemand, including:

- [JupyterLab](Apps/JupyterLab/index.md)
- [RStudio](Apps/RStudio.md)
- [Code server](Apps/code_server.md)
- [Virtual desktop](Apps/virtual_desktop.md)
- [MATLAB](Apps/MATLAB.md) - currently under development, let us know if this is of interest

## Changes from Jupyter on NeSI

- JupyterLab is no longer the main user interface but is just another application to be launched via the OnDemand interface
- RStudio, MATLAB and Virtual Desktop applications are accessed directly from OnDemand instead of via JupyterLab

## Known Issues

| Limitation                                |  What are the missing functions/commands associated with this|
--------------------------------------------|--------------------------------------------------------------|
|1. OnDemand apps are not exposed to HPC3 Slurm | Commands such as `sbatch`, `sacct`, `squeue` , `scancel` will not work from OnDemand apps|
|2. Missing user Namespaces in Kubernetes pods will interfere with some Apptainer operations| Although we can run `apptainer pull` command, `apptainer exec,run,shell` commands can not be executed due to missing user Namespaces|

!!! info ""

    🙋 If you to come across above limitations, please consider switching to the new HPC login node via `Cluster` > `NeSI HPC Shell access` via OnDemand home page

    [OnDemand how to access login shell.](../../assets/images/OOD_howtoaccesslogin_node_shell.png)

## Release notes

Release notes can be found [here](Release_Notes/index.md).

## Acknowledgements

We acknowledge the work of the Open OnDemand team in providing the underlying platform used for this service, as described in the following paper:

[Hudak et al., (2018). Open OnDemand: A web-based client portal for HPC centers. Journal of Open Source Software, 3(25), 622, https://doi.org/10.21105/joss.00622](https://doi.org/10.21105/joss.00622)
