---
created_at: 2025-01-24
description: How to set up your own custom kernels for use on Mahuika JupyterHub
tags: 
    - JupyterHub
    - Python
    - R
---

# Jupyter kernels - Manual management

## Introduction

Jupyter kernels execute the code that you write. Mahuika provides a number of
Python and R kernels by default, which can be selected from the Launcher.

Many packages are preinstalled in our default Python and R environments
and these can be extended further as described on the
[Python](../../../../Software/Available_Applications/Python.md) and
[R](../../../../Software/Available_Applications/R.md) support
pages.

## Adding a Custom Python kernel

!!! note "see also"
     See the [Jupyter kernels - Tool-assisted management](./Jupyter_kernels_Tool_assisted_management.md)
     page for the **preferred** way to register kernels, which uses the
     `nesi-add-kernel` command line tool to automate most of these manual
     steps.

You can configure custom Python kernels for running your Jupyter
notebooks. This could be necessary and/or recommended in some
situations, including:

- If you wish to load a different combination of environment modules
    than those we load in our default kernels
- If you would like to activate a virtual environment or conda
    environment before launching the kernel

The following example will create a custom kernel based on the
Miniconda3 environment module (but applies to other environment modules
too).

First, change directory into the path that you would like to place your
conda environment.

- **If you would like to share this environment with other users**, change directory
into your project folder using `cd /nesi/project/<project-code>`. Do not use the path
that includes `00_nesi_projects` or `home` in the name as this causes issues.

Second, in a terminal run the following commands to load a Miniconda environment
module:

``` sh
module purge
module load Miniconda3
```

Now create a conda environment named "my-conda-env" using Python 3.11.
The *ipykernel* Python package is required but you can change the names
of the environment, version of Python and install other Python packages
as required.

``` sh
conda create --prefix ./my-conda-env python=3.11
source $(conda info --base)/etc/profile.d/conda.sh
conda activate ./my-conda-env
conda install ipykernel
# you can pip/conda install other packages here too
```

Third, we will create a wrapper for your conda environment.
Change directory into your `my-conda-env` folder:

```sh
cd my-conda-env
```

And add the following as `wrapper.sh` into your `my-conda-env` folder:

``` sh
#!/usr/bin/env bash

# load required modules here
module purge
module load Miniconda3

# activate conda environment
source $(conda info --base)/etc/profile.d/conda.sh 
conda deactivate  # workaround for https://github.com/conda/conda/issues/9392
conda activate my-conda-env

# run the kernel
exec python $@
```

Make the wrapper script executable:

``` sh
chmod +x wrapper.sh
```

Fourth, create a Jupyter kernel based on your new conda environment:

``` sh
python -m ipykernel install --user --name my-conda-env --display-name="My Conda Env"
```

We must now edit the kernel to load the required environment
modules before the kernel is launched. Change to the directory the
kernelspec was installed to
`~/.local/share/jupyter/kernels/my-conda-env`, (assuming you kept
`--name my-conda-env` in the above command):

``` sh
cd ~/.local/share/jupyter/kernels/my-conda-env
```

and edit the *kernel.json* to change the first element of the argv list
to point to the wrapper script we just created. The file should look
like this:

```json
{
 "argv": [
 "<full_path_to_your_wrapper_file>/wrapper.sh",
 "-m",
 "ipykernel_launcher",
 "-f",
 "{connection_file}"
 ],
 "display_name": "My Conda Env",
 "language": "python"
}
```

After refreshing JupyterLab your new kernel should show up in the
Launcher as "My Conda Env".

## Sharing your custom kernal with your project team members

You can also configure a shared Python kernel that others with access to
the same project will be able to load.

* To do this, you must make sure it also exists in a shared location
(other users cannot see your home directory).

First, **you** need to perform the steps in [Adding a Custom Python kernel](#adding-a-custom-python-kernel)

Second, **your team members** need to run the following commands in the terminal:

``` sh
# change directory into the path that contains your conda environment
cd <full_path_to_your_conda_environment>

# load Miniconda3
module purge
module load Miniconda3

# Activate your shared conda environment
source $(conda info --base)/etc/profile.d/conda.sh
conda activate ./my-conda-env
```

Third, get **your team members** to create a Jupyter kernel based on your python/conda environment:

``` sh
python -m ipykernel install --user --name my-conda-env --display-name="My Conda Env"
```

**Your project members** must now edit the kernel in their home directories
to load the required environment modules before the kernel is launched.
Change to the directory the kernelspec was installed to
`~/.local/share/jupyter/kernels/my-conda-env`, (assuming you kept
`--name my-conda-env` in the above command):

``` sh
cd ~/.local/share/jupyter/kernels/my-conda-env
```

and edit the *kernel.json* to change the first element of the argv list
to point to the wrapper script we just created. The file should look
like this:

```json
{
 "argv": [
 "<full_path_to_your_wrapper_file>/wrapper.sh",
 "-m",
 "ipykernel_launcher",
 "-f",
 "{connection_file}"
 ],
 "display_name": "My Conda Env",
 "language": "python"
}
```

After refreshing JupyterLab your new kernel should show up in the
Launcher as "My Conda Env".

## Custom kernel in a Singularity container

An example showing setting up a custom kernel running in a Singularity
container can be found on our [Lambda Stack](../../../../Software/Available_Applications/Lambda_Stack.md#lambda-stack-via-jupyter)
support page.

## Adding a custom R kernel

You can configure custom R kernels for running your Jupyter notebooks.
The following example will create a custom kernel based on the
R/3.6.2-gimkl-2020a environment module and will additionally load an
MPFR environment module (e.g. if you wanted to load the Rmpfr package).

In a terminal run the following commands to load the required
environment modules:

``` sh
module purge
module load IRkernel/1.1.1-gimkl-2020a-R-3.6.2
module load Python/3.8.2-gimkl-2020a
```

The IRkernel module loads the R module as a dependency and provides the
R kernel for Jupyter. Python is required to install the kernel (since
Jupyter is written in Python).

Now create an R Jupyter kernel based on your new conda environment:

``` sh
R -e "IRkernel::installspec(name='myrwithmpfr', displayname = 'R with MPFR', user = TRUE)"
```

We must now to edit the kernel to load the required environment
modules when the kernel is launched. Change to the directory the
kernelspec was installed to
(~/.local/share/jupyter/kernels/myrwithmpfr, assuming you kept `--name
myrwithmpfr` in the above command):

``` sh
cd ~/.local/share/jupyter/kernels/myrwithmpfr
```

Now create a wrapper script in that directory, called *wrapper.sh*, with
the following contents:

``` sh
#!/usr/bin/env bash

# load required modules here
module purge
module load MPFR/4.0.2-GCCcore-9.2.0
module load IRkernel/1.1.1-gimkl-2020a-R-3.6.2

# run the kernel
exec R $@
```

Make the wrapper script executable:

``` sh
chmod +x wrapper.sh_
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
```

After refreshing JupyterLab your new R kernel should show up in the
Launcher as "R with MPFR".
