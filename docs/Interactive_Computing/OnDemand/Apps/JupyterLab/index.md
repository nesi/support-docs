# JupyterLab via OnDemand


## Introduction

NeSI supports the use of [Jupyter](https://jupyter.org/) for interactive computing.
Jupyter allows you to create notebooks that contain live code,
equations, visualisations and explanatory text. There are many uses for
Jupyter, including data cleaning, analytics and visualisation, machine
learning, numerical simulation, managing
[Slurm job submissions](../../../../Tutorials/Introduction_To_HPC/Submitting_Your_First_Job.md)
and workflows and much more.

## Accessing Jupyter on NeSI


Jupyter at NeSI can be accessed via [NeSI OnDemand](https://ondemand.nesi.org.nz/) and launching the JupyterLab application there.
For more details see the [how-to guide](../../how_to_guide.md).

## Jupyter user interface

### JupyterLab

[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
is the next generation of the Jupyter user interface and provides a way
to use notebooks, text editor, terminals and custom components together.

### filesystems

Your JupyterLab session will start in your home directory the first time you launch it. On subsequent launches it may remember your previous working directory and start there.

NeSI will auto generate a directory within your home folder called `00_nesi_projects`, you will find symbolic links to projects and nobackup directories of your active projects. We do not recommend that you store files in this initial directory because next time you log into OnDemand the directory will be repopulated based on your user groups, instead switch to your home, project or nobackup directories first.

If you wish to not have this folder recreated upon login then please place the following file in your HOME directory `.00_nesi_projects.stop` and this will stop the folder from being recreated upon login.

### Jupyter kernels

NeSI provides some default Python and R kernels that are available to all users and are based on some
of environment modules. It's also possible to create additional kernels that are visible only to
you (they can optionally be made visible to other members of a specific NeSI project that you belong to). See:

- [Jupyter kernels - Tool-assisted management](./Jupyter_kernels_Tool_assisted_management.md) (recommended)
- [Jupyter kernels - Manual management](./Jupyter_kernels_Manual_management.md)

### Jupyter terminal

Some things to note about the JupyterLab terminal are:

- when you launch the terminal application some environment modules
  are already loaded, so you may want to run `module purge`
- processes launched directly in the JupyterLab terminal will probably
  be killed when you Jupyter session times out

## Installing JupyterLab extensions

JupyterLab supports many extensions that enhance its functionality. At
NeSI we package some extensions into the default JupyterLab environment.
Keep reading if you need to install extensions yourself.

Note, there were some changes related to extensions in JupyterLab 3.0
and there are now multiple methods to install extensions. More details
about JupyterLab extensions can be found
[here](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html).
Check the extension's documentation to find out the supported
installation method for that particular extension.

On NeSI OnDemand we support installing prebuilt extensions (i.e. pip installable
packages) from the terminal application.
First ensure you have the latest JupyterLab module loaded:

```sh
module purge
module load JupyterLab
```

Then install the extension by running (the upstream documentation for the package
you are installing should specify the "packagename" that you should use):

``` sh
pip install --user <packagename>
```

For example, the [Dask extension](https://github.com/dask/dask-labextension#jupyterlab-4x)
can be installed with the following:

``` sh
pip install --user dask-labextension
```

Note that we need to specify the `--user` option on the `pip install` command because you don't
have permission to install packages in the system directory. Adding `--user` installs the package
into your home directory instead.

## Log files

The log file of a JupyterLab session is saved in the OnDemand session directory
(a subdirectory under the *ondemand* directory in your home directory).
You can reach the session directory in the OnDemand file browser by clicking
the link in the session card under "My Interactive Sessions" in the NeSI
OnDemand web interface. The log file is named *session.log* within the session
directory.

## External documentation

- [Jupyter](https://jupyter.readthedocs.io/en/latest/)
- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
