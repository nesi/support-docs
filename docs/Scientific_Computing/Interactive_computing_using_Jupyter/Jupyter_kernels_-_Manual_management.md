---
created_at: '2022-01-31T20:45:43Z'
hidden: false
label_names: []
position: 5
title: Jupyter kernels - Manual management
vote_count: 1
vote_sum: 1
zendesk_article_id: 4414951820559
zendesk_section_id: 360001189255
---

# Introduction

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

# Adding a custom Python kernel

> ### See also
>
> See the [Jupyter kernels - Tool-assisted
> management](https://support.nesi.org.nz/hc/en-gb/articles/4414958674831)
> page for the **preferred** way to register kernels, which uses the
> `nesi-add-kernel` command line tool to automate most of these manual
> steps.

You can configure custom Python kernels for running your Jupyter
notebooks. This could be necessary and/or recommended in some
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

Now create a conda environment named "my-conda-env" using Python 3.6.
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
(~/.local/share/jupyter/kernels/my-conda-env,* *assuming you kept
*--name my-conda-env* in the above command):

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
like this (change &lt;username&gt; to your NeSI username):

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
Launcher as "My Conda Env".

# Sharing a Python kernel with your project team members

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
look like this (change &lt;project\_code&gt; to your NeSI project code):

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
Launcher as "Shared Virtual Env".

# Custom kernel in a Singularity container

An example showing setting up a custom kernel running in a Singularity
container can be found on our [Lambda
Stack](https://support.nesi.org.nz/hc/en-gb/articles/360002558216-Lambda-Stack#lambda_stack_via_jupyter)
support page.

# Adding a custom R kernel

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
(~/.local/share/jupyter/kernels/myrwithmpfr,* *assuming you kept *--name
myrwithmpfr* in the above command):

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
something like this (change &lt;username&gt; to your NeSI username):

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
Launcher as "R with MPFR".

# Spark

At the time of writing, the latest stable version of Spark does not
support Python 3.8. If you wish to use Spark (e.g. PySpark) make sure
you select one of our Python 3.7.3 or Anaconda3 kernels.
