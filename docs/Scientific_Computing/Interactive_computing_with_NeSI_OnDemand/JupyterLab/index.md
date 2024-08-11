# JupyterLab via OnDemand

## Introduction

NeSI supports the use of [Jupyter](https://jupyter.org/) for
[interactive computing](../../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Slurm_Interactive_Sessions.md).
Jupyter allows you to create notebooks that contain live code,
equations, visualisations and explanatory text. There are many uses for
Jupyter, including data cleaning, analytics and visualisation, machine
learning, numerical simulation, managing [Slurm job
submissions](../../../Getting_Started/Next_Steps/Submitting_your_first_job.md)
and workflows and much more.

!!! prerequisite "See also"
     -   See the [Jupyter kernels - Tool-assisted management](Jupyter_kernels_Tool_assisted_management.md)
         (recommended) and [Jupyter kernels - Manual management](Jupyter_kernels_Manual_management.md)
         pages for adding kernels.

## Accessing Jupyter on NeSI

Jupyter at NeSI can be accessed via [NeSI OnDemand](https://ondemand.nesi.org.nz/) and launching the JupyterLab application there.

When you log in with your [NeSI credentials](../../../Getting_Started/Accessing_the_HPCs/Setting_Up_and_Resetting_Your_Password.md)
you will be taken to the "NeSI OnDemand" page, where you can choose from many different interactive applications, including JupyterLab.
When you select the JupyterLab application you will be presented with certain options, such as how many CPU cores and how much memory you
require for you interactive session. After launching your session you should be presented with an option to "Connect to JupyterLab", which
will take you to the JupyterLab web interface.


## Jupyter user interface

### JupyterLab

Once the "Connect to JupyterLab" button is available and you have clicked it you will be redirected to
[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/). JupyterLab
is the next generation of the Jupyter user interface and provides a way
to use notebooks, text editor, terminals and custom components together.

### File systems

!!! danger

    This section will need updating

Your Jupyter server will start in a new directory created within your
home directory for that specific Jupyter job. Within that directory, you
will find symbolic links to your home directory and to the project and
nobackup directories of your active projects. We do not recommend that
you store files in this initial directory because next time you launch
Jupyter you will be starting in a different directory, instead switch to
one of your home, project or nobackup directories first.

### Jupyter terminal

!!! danger

    Suggest use the ondemand terminal for NeSI cluster access instead (doesn't require launching an app), once the slurm cluster is configured in ondemand, and remove this section?

JupyterLab provides a terminal that can be an alternative means of
gaining command line access to NeSI systems instead of using an SSH
client. Some things to note are:

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

### Installing prebuilt extensions 

If the extension is packaged as a prebuilt extension (e.g. as a pip
package), then you can install it from the JupyterLab terminal by
running:

``` sh
pip install --user <packagename>
```

For example, the [Dask
extension](https://github.com/dask/dask-labextension#jupyterlab-30-or-greater)
can be installed with the following:

``` sh
pip install --user dask-labextension
```

### Installing source extensions

Installing source extensions requires a rebuild of the JupyterLab web
application. Since this requires write permissions, you will need to set
the JupyterLab [application directory](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#advanced-usage)
to a location that you can write to. To do this you need to create a
file named *~/.jupyterlab3\_dir* in your home directory with the full
path to your desired JupyterLab application directory and then run some
commands to initialise the JupyterLab application directory.

Running the following commands will create the JupyterLab application
directory in your home directory:

``` sh
module load JupyterLab
echo $HOME/.local/share/jupyter/lab > ~/.jupyterlab3_dir
export JUPYTERLAB_DIR=$HOME/.local/share/jupyter/lab
jupyter lab build
```

These changes will only take effect after relaunching your Jupyter
server and then you should be able to install JupyterLab extensions as
you please.

!!!note
     The above commands will put the JupyterLab application directory in
     your home directory. The application directory often requires at least
     1-2GB of disk space and 30,000 inodes (file count), so make sure you
     have space available in your home directory first (see
     [NeSI File Systems and Quotas](../../../Storage/File_Systems_and_Quotas/NeSI_File_Systems_and_Quotas.md))
     or request a larger quota.

You could change the path to point to a location in your project
directory, especially if multiple people on your project will share the
same JupyterLab application directory, e.g.:

``` sh
module load JupyterLab
echo /nesi/project/<project_code>/$USER/jupyter/lab > ~/.jupyterlab_dir
export JUPYTERLAB_DIR=/nesi/project/<project_code>/$USER/jupyter/lab
jupyter lab build
```

## Log files

The log file of a Jupyter server session is saved in the OnDemand session directory
that is linked in the NeSI OnDemand web interface and is named *session.log*.

## External documentation

- [Jupyter](https://jupyter.readthedocs.io/en/latest/)
- [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
