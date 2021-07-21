> ### Note {#prerequisites}
>
> This service is available for users with a current allocation on
> Mahuika only.\
> [Please contact us to request a suitable
> allocation.](https://support.nesi.org.nz/hc/en-gb/requests/new).

Introduction
============

NeSI supports the use of [Jupyter](https://jupyter.org/) for interactive
computing. Jupyter allows you to create notebooks that contain live
code, equations, visualisations and explanatory text. There are many
uses for Jupyter, including data cleaning, analytics and visualisation,
machine learning, numerical simulation, managing [Slurm job
submissions](https://support.nesi.org.nz/hc/en-gb/articles/360000684396)
and workflows and much more.

Accessing Jupyter on NeSI
=========================

*Jupyter at NeSI is powered by [JupyterHub](https://jupyter.org/hub), a
multi-user hub that spawns, manages and proxies multiple instances of
the single-user Jupyter server.*

Access NeSI\'s JupyterHub here:

<https://jupyter.nesi.org.nz>

When you log in with your [NeSI
credentials](https://support.nesi.org.nz/hc/en-gb/articles/360000335995)
you will be taken to the \"Server Options\" page, where typical job
configuration options can be selected to allocate the resources that
will be used to run Jupyter. Typical jobs, not requesting a GPU, should
be up and running within one to two minutes. Requesting a GPU can
increase this time significantly as there are only a small number of
GPUs available at NeSI.

> ### Tip {#prerequisites}
>
> If your server appears to not have started within 3 minutes please
> reload the browser window and check again, otherwise contact
> [support\@nesi.org.nz](mailto:support@nesi.org.nz?subject=Jupyter%20on%20NeSI).

Feedback
========

A dedicated
[portal](https://portal.productboard.com/2k2ojgehbq7ovnyzmcjp1nxg) is
available to share feedback and ideas with NeSI.\
See also [How to submit feedback or a new idea using a product
portal?](https://support.nesi.org.nz/hc/en-gb/articles/360001504596)

Jupyter user interface
======================

JupyterLab
----------

Once your server has started you will be redirected to
[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/). JupyterLab
is the next generation of the Jupyter user interface and provides a way
to use notebooks, text editor, terminals and custom components together.
If you would prefer to use the classic Notebook interface, then select
\"Launch Classic Notebook\" from the JupyterLab Help menu, or change the
URL from */lab* to */tree* once the server is running.

File systems
------------

Your Jupyter server will start in a new directory created within your
home directory for that specific Jupyter job. Within that directory, you
will find symbolic links to your home directory and to the project and
nobackup directories of your active projects. We do not recommend that
you store files in this initial directory because next time you launch
Jupyter you will be starting in a different directory, instead switch to
one of your home, project or nobackup directories first.

Jupyter terminal
----------------

JupyterLab provides a terminal that can be an alternative means of
gaining command line access to NeSI systems instead of using an SSH
client. Some things to note are:

-   when you launch the terminal application some environment modules
    are already loaded, so you may want to run a *module purge*
-   processes launched directly in the JupyterLab terminal will probably
    be killed when you Jupyter session times out
-   you may run into issues trying to submit a job with *sbatch* from
    the JupyterLab terminal, to avoid this we recommend not passing the
    environment through to the Slurm job by setting the following in
    your batch script:
    -   #SBATCH --export=NONE

    -   ``` {.c-mrkdwn__pre data-stringify-type="pre"}
        export SLURM_EXPORT_ENV=ALL
        ```

Jupyter kernels
===============

Jupyter kernels execute the code that you write. The following Jupyter
kernels are installed by default and can be selected from the Launcher:

-   Python 3.8.2
-   Python 3.8.1
-   Python 3.7.3
-   Anaconda3
-   R 4.0.1
-   R 3.6.1

Many packages are preinstalled in our default Python and R environments
and these can be extended further as described on the
[Python](https://support.nesi.org.nz/hc/en-gb/articles/207782537) and
[R](https://support.nesi.org.nz/hc/en-gb/articles/209338087) support
pages.

Adding a custom Python kernel
-----------------------------

You can configure custom Python kernels for running your Jupyter
notebooks; this could be necessary and/or recommended in some
situations, including:

-   if you wish to load a different combination of environment modules
    than those we load in our default kernels
-   if you would like to activate a virtual environment or conda
    environment before launching the kernel

The following example will create a custom kernel based on the
Miniconda3 environment module (but applies to other environment modules
too).

In a terminal run the following commands to load a Miniconda environment
module:

    $ module purge
    $ module load Miniconda3/4.8.2

Now create a conda environment named \"my-conda-env\" using Python 3.6.
The *ipykernel* Python package is required but you can change the names
of the environment, version of Python and install other Python packages
as required.

    $ conda create --name my-conda-env python=3.6
    $ source $(conda info --base)/etc/profile.d/conda.sh
    $ conda activate my-conda-env
    $ conda install ipykernel
    $ # you can pip/conda install other packages here too

Now create a Jupyter kernel based on your new conda environment:

    $ python -m ipykernel install --user --name my-conda-env --display-name="My Conda Env"

We must now edit the kernel to load the required NeSI environment
modules before the kernel is launched. Change to the directory the
kernelspec was installed to
(\~/.local/share/jupyter/kernels/my-conda-env,* *assuming you kept
*\--name my-conda-env* in the above command):

    $ cd ~/.local/share/jupyter/kernels/my-conda-env

Now create a wrapper script, called *wrapper.sh*, with the following
contents:

    #!/usr/bin/env bash

    # load required modules here
    module purge
    module load Miniconda3/4.8.2

    # activate conda environment
    source $(conda info --base)/etc/profile.d/conda.sh 
    conda deactivate  # workaround for https://github.com/conda/conda/issues/9392
    conda activate my-conda-env

    # run the kernel
    exec python $@

Make the wrapper script executable:

    $ chmod +x wrapper.sh

Next edit the *kernel.json* to change the first element of the argv list
to point to the wrapper script we just created. The file should look
like this (change \<username\> to your NeSI username):

    {
     "argv": [
     "/home/<username>/.local/share/jupyter/kernels/my-conda-env/wrapper.sh",
     "-m",
     "ipykernel_launcher",
     "-f",
     "{connection_file}"
     ],
     "display_name": "My Conda Env",
     "language": "python"
    }

After refreshing JupyterLab your new kernel should show up in the
Launcher as \"My Conda Env\".

Sharing a Python kernel with your project team members
------------------------------------------------------

You can also configure a shared Python kernel that others with access to
the same NeSI project will be able to load. If this kernel is based on a
Python virtual environment, Conda environment or similar, you must make
sure it also exists in a shared location (other users cannot see your
home directory).

The example below shows creating a shared Python kernel based on the
*Python/3.8.2-gimkl-2020a* module and also loads the
*ETE/3.1.1-gimkl-2020a-Python-3.8.2* module.

In a terminal run the following commands to load the Python and ETE
environment modules:

    $ module purge
    $ module load Python/3.8.2-gimkl-2020a
    $ module load ETE/3.1.1-gimkl-2020a-Python-3.8.2

Now create a Jupyter kernel within your project directory, based on your
new virtual environment:

    $ python -m ipykernel install --prefix=/nesi/project/<project_code>/.jupyter --name shared-ete-env --display-name="Shared ETE Env"

Next change to the kernel directory, which for the above command would
be:

    $ cd /nesi/project/<project_code>/.jupyter/share/jupyter/kernels/shared-ete-env

Create a wrapper script, *wrapper.sh*, with the following contents:

    #!/usr/bin/env bash

    # load necessary modules here
    module purge
    module load Python/3.8.2-gimkl-2020a
    module load ETE/3.1.1-gimkl-2020a-Python-3.8.2

    # run the kernel
    exec python $@

Note we also load the ETE module so that we can use that from our
kernel.

Make the wrapper script executable:

    chmod +x wrapper.sh

Next, edit the *kernel.json* to change the first element of the argv
list to point to the wrapper script we just created. The file should
look like this (change \<project\_code\> to your NeSI project code):

    {
     "argv": [
     "/nesi/project/<project_code>/.jupyter/share/jupyter/kernels/shared-ete-env/wrapper.sh",
     "-m",
     "ipykernel_launcher",
     "-f",
     "{connection_file}"
     ],
     "display_name": "Shared Conda Env",
     "language": "python"
    }

After refreshing JupyterLab your new kernel should show up in the
Launcher as \"Shared Virtual Env\".

Custom kernel in a Singularity container
----------------------------------------

An example showing setting up a custom kernel running in a Singularity
container can be found on our [Lambda
Stack](https://support.nesi.org.nz/hc/en-gb/articles/360002558216-Lambda-Stack#lambda_stack_via_jupyter)
support page.

Adding a custom R kernel
------------------------

You can configure custom R kernels for running your Jupyter notebooks.
The following example will create a custom kernel based on the
R/3.6.2-gimkl-2020a environment module and will additionally load an
MPFR environment module (e.g. if you wanted to load the Rmpfr package).

In a terminal run the following commands to load the required
environment modules:

    $ module purge
    $ module load IRkernel/1.1.1-gimkl-2020a-R-3.6.2
    $ module load Python/3.8.2-gimkl-2020a

The IRkernel module loads the R module as a dependency and provides the
R kernel for Jupyter. Python is required to install the kernel (since
Jupyter is written in Python).

Now create an R Jupyter kernel based on your new conda environment:

    $ R -e "IRkernel::installspec(name='myrwithmpfr', displayname = 'R with MPFR', user = TRUE)"

We must now to edit the kernel to load the required NeSI environment
modules when the kernel is launched. Change to the directory the
kernelspec was installed to
(\~/.local/share/jupyter/kernels/myrwithmpfr,* *assuming you kept
*\--name myrwithmpfr* in the above command):

    $ cd ~/.local/share/jupyter/kernels/myrwithmpfr

Now create a wrapper script in that directory, called *wrapper.sh*, with
the following contents:

    #!/usr/bin/env bash

    # load required modules here
    module purge
    module load MPFR/4.0.2-GCCcore-9.2.0
    module load IRkernel/1.1.1-gimkl-2020a-R-3.6.2

    # run the kernel
    exec R $@

Make the wrapper script executable:

    $ chmod +x wrapper.sh

Next edit the *kernel.json* to change the first element of the argv list
to point to the wrapper script we just created. The file should look
something like this (change \<username\> to your NeSI username):

    {
     "argv": [
     "/home/<username>/.local/share/jupyter/kernels/myrwithmpfr/wrapper.sh",
     "--slave",
     "-e",
     "IRkernel::main()",
     "--args",
     "{connection_file}"
     ],
     "display_name": "R with MPFR",
     "language": "R"
    }

After refreshing JupyterLab your new R kernel should show up in the
Launcher as \"R with MPFR\".

Spark
-----

At the time of writing, the latest stable version of Spark does not
support Python 3.8. If you wish to use Spark (e.g. PySpark) make sure
you select one of our Python 3.7.3 or Anaconda3 kernels.

Installing JupyterLab extensions
================================

JupyterLab supports many extensions that enhance its functionality. At
NeSI we package some extensions into the default JupyterLab environment.
Keep reading if you need to install extensions yourself.

Note, there were some changes related to extensions in JupyterLab 3.0
and there are now multiple methods to install extensions. More details
about JupyterLab extensions can be found
[here](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html).
Check the extension\'s documentation to find out the supported
installation method for that particular extension.

Installing prebuilt extensions 
-------------------------------

If the extension is packaged as a prebuilt extension (e.g. as a pip
package), then you can install it from the JupyterLab terminal by
running:

    $ pip install --user <packagename>

For example, the [Dask
extension](https://github.com/dask/dask-labextension#jupyterlab-30-or-greater)
can be installed with the following:

    $ pip install --user dask-labextension

Installing source extensions
----------------------------

Installing source extensions requires a rebuild of the JupyterLab web
application. Since this requires write permissions, you will need to set
the JupyterLab [application
directory](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#advanced-usage)
to a location that you can write to. To do this you need to create a
file named *\~/.jupyterlab3\_dir* in your home directory with the full
path to your desired JupyterLab application directory and then run some
commands to initialise the JupyterLab application directory.

Running the following commands will create the JupyterLab application
directory in your home directory:

    $ module load JupyterLab
    $ echo $HOME/.local/share/jupyter/lab > ~/.jupyterlab3_dir
    $ export JUPYTERLAB_DIR=$HOME/.local/share/jupyter/lab
    $ jupyter lab build

These changes will only take effect after relaunching your Jupyter
server and then you should be able to install JupyterLab extensions as
you please.

> ### Note {#prerequisites}
>
> The above commands will put the JupyterLab application directory in
> your home directory. The application directory often requires at least
> 1-2GB of disk space and 30,000 inodes (file count), so make sure you
> have space available in your home directory first (see [NeSI File
> Systems and
> Quotas](https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas))
> or request a larger quota.

You could change the path to point to a location in your project
directory, especially if multiple people on your project will share the
same JupyterLab application directory, e.g.:

    $ module load JupyterLab
    $ echo /nesi/project/<project_code>/$USER/jupyter/lab > ~/.jupyterlab_dir
    $ export JUPYTERLAB_DIR=/nesi/project/<project_code>/$USER/jupyter/lab
    $ jupyter lab build

RStudio via Jupyter
===================

See the [RStudio via Jupyter on
NeSI](https://support.nesi.org.nz/hc/en-gb/articles/360004337836) page
for launching a RStudio instance.

Virtual desktop via Jupyter
===========================

See the [Virtual Desktop via Jupyter on
NeSI](https://support.nesi.org.nz/hc/en-gb/articles/360001600235) page
for launching a virtual desktop on NeSI via our Jupyter service.

Ending your interactive session and logging out
===============================================

To end a JupyterLab session, please select \"Control Panel\" under the
File menu and then \"Stop My Server\". If you click Logout without
stopping your server, the server will continue to run until the Slurm
job reaches its maximum wall time.

Log files
=========

The log file of a Jupyter server session is saved either in the project
directory of the project you selected on the \"Server Options\"
JupyterHub page, or in your home directory, and is named
\".jupyterhub\_\<username\>\_\<job\_id\>.log*\"* (note the leading \".\"
which means the log file is hidden). If you encounter problems with your
Jupyter session, the contents of this file can be a good first clue to
debug the issue.

Further documentation
=====================

-   [Jupyter](https://jupyter.readthedocs.io/en/latest/)
-   [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/)
-   [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)
