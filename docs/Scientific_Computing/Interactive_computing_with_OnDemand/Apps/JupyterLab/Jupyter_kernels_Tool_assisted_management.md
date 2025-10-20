# Jupyter kernels - Tool-assisted management

!!! warning

    NeSI OnDemand is in development and accessible to early access users only.
    If you are interested in helping us test it please [contact us](mailto:support@nesi.org.nz).

## Introduction

Jupyter can execute code in different computing environments using
*kernels*. Some kernels are provided by default (Python, R, etc.) but
you may want to register your computing environment to use it in
notebooks. For example, you may want to load a specific environment
module in your kernel or use a Conda environment.

To register a Jupyter kernel, you can follow the steps highlighted in
the [Jupyter kernels - Manual management](./Jupyter_kernels_Manual_management.md)
or use the `nesi-add-kernel` tool provided within the [Jupyter on NeSI service](https://jupyter.nesi.org.nz).
This page details the latter option, which we recommend.

## Getting started

First you need to open a terminal. It can be from a session on Jupyter
on NeSI or from a regular ssh connection on Mahuika login node. If you
use the ssh option, make sure to load the JupyterLab module to have
access to the `nesi-add-kernel` tool:

``` sh
module purge  # remove all previously loaded modules
module load JupyterLab
```

Then, to list all available options, use the `-h` or `--help` options as
follows:

``` sh
nesi-add-kernel --help
```

Here is an example to add a TensorFlow kernel, using NeSI’s module:

``` sh
nesi-add-kernel tf_kernel TensorFlow/2.8.2-gimkl-2022a-Python-3.10.5
```

!!! warning
    The name given to your kernal in `nesi-add-kernal KERNAL_NAME MODULE` must only include lowercase letters, underscores, and dashes. 

and to share the kernel with other members of your NeSI project:

``` sh
nesi-add-kernel --shared tf_kernel_shared TensorFlow/2.8.2-gimkl-2022a-Python-3.10.5 
```

To list all the installed kernels, use the following command:

``` sh
jupyter-kernelspec list
```

and to delete a specific kernel:

``` sh
jupyter-kernelspec remove <kernel_name>
```

where `<kernel_name>` stands for the name of the kernel to delete.

## Conda environment

First, make sure the `JupyterLab` module is loaded:

``` sh
module purge
module load JupyterLab
```

To add a Conda environment created using
`conda create -p <conda_env_path>`, use:

``` sh
nesi-add-kernel my_conda_env -p <conda_env_path>
```

otherwise if created using `conda create -n <conda_env_name>`, use:

``` sh
nesi-add-kernel my_conda_env -n <conda_env_name>
```

## Virtual environment

If you want to use a Python virtual environment, don’t forget to specify
which Python module you used to create it.

For example, if we create a virtual environment named `my_test_venv`
using Python 3.10.5:

``` sh
module purge
module load Python/3.10.5-gimkl-2022a
python -m venv my_test_venv
```

to create the corresponding `my_test_kernel` kernel, we need to use the
command:

``` sh
module purge
module load JupyterLab
nesi-add-kernel my_test_kernel Python/3.10.5-gimkl-2022a --venv my_test_venv
```

## Singularity container

!!! danger

    This section has not been tested on NeSI OnDemand

To use a Singularity container, use the `-c` or `--container` options as
follows:

``` sh
module purge
module load JupyterLab
nesi-add-kernel my_test_kernel -c <container_image.sif>
```

where `<container_image.sif>` is a path to your container image.

Note that your container **must** have the `ipykernel` Python package
installed in it to be able to work as a Jupyter kernel.

Additionally, you can use the `--container-args` option to pass more
arguments to the `singularity exec` command used to instantiate the
kernel.

Here is an example instantiating a NVIDIA NGC container as a kernel.
First, we need to pull the container:

``` sh
module purge
module load Singularity/3.11.3
singularity pull nvidia_tf.sif docker://nvcr.io/nvidia/tensorflow:21.07-tf2-py3
```

then we can instantiate the kernel, using the `--nv` singularity flag to
ensure that the GPU will be found at runtime (assuming our Jupyter
session has access to a GPU):

``` sh
module purge
module load JupyterLab
nesi-add-kernel nvidia_tf -c nvidia_tf.sif --container-args "'--nv'"
```

Note that the double-quoting of `--nv` is needed to properly pass the
options to `singularity exec`.
