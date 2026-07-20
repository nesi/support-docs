---
title: Python and R Kernels in JupyterLab
description: How to register and manage custom Jupyter kernels on Mahuika JupyterHub
tags:
    - JupyterHub
    - Python
    - R
---

A Jupyter kernel is the actual thing that executes the code in your Jupyter notebook.
Mahuika provides a number of Python and R kernels by default; these can be selected from
the Launcher. These come with many packages preinstalled, and can be extended
further as described on the
[Python](../../../../Software/Available_Applications/Python.md) and
[R](../../../../Software/Available_Applications/R.md) support pages.

## Adding a Kernel to JupyterLab

Sometimes, though, you will want a kernel that runs in your own computing
environment - for example, to load a specific environment module, or to use a
Conda or Python virtual environment. There are two ways to register such a
custom kernel; select the tab that suits you:

- **Tool-Assisted Management**: uses the `nesi-add-kernel` command line tool to
    automate most of the setup. This is the **recommended** approach if possible.
- **Manual Management**: you set up the kernel and its wrapper script by hand. This
    can be useful when you need more control over how the kernel is launched.

=== "Tool-Assisted Management"

    The `nesi-add-kernel` tool automates most of the steps needed to register a
    kernel. **This is the recommended way to register a Jupyter kernel.**

    The exact arguments depend on whether you are basing the kernel on an
    environment module, a Python virtual environment, or a Conda environment:

    === "Environment module"

        First you need to open a terminal. It can be from a session on Jupyter
        via OnDemand or from a regular ssh connection on the Mahuika login node.

        - If you use the ssh option, make sure to load the JupyterLab module to
            have access to the `nesi-add-kernel` tool:

            ``` sh
            module purge  # remove all previously loaded modules
            module load JupyterLab
            ```

        Use the `nesi-add-kernel` to register a kernel:

        ``` sh
        nesi-add-kernel <KERNEL_NAME> <MODULE>
        ```

        Where:

        - `<KERNEL_NAME>`: The name you want to give the kernel.
        - `<MODULE>`: The environment module to base the kernel on.

        Here is an example for adding a TensorFlow module to JupyterLab as a kernel:

        ``` sh
        nesi-add-kernel tf_kernel TensorFlow/2.8.2-gimkl-2022a-Python-3.10.5
        ```

    === "Python virtual environment"

        First, create your [python virtual environment](../../../../Software/Available_Applications/Python.md#installing-packages-in-your-home):

        ``` sh
        module purge
        module load Python/3.14.4-foss-2026  # Change the module to the version of python you want to use
        python3 -m venv ./my-venv
        pip install --upgrade pip
        # you can pip install other packages here too
        ```

        Then create a kernel based on your virtual environment:

        ``` sh
        module purge
        module load JupyterLab
        # The module of python you give here must be the same as the version of python you use to make the virtual environment
        nesi-add-kernel <kernel_name> --venv my-venv
        ```

        Where `<kernel_name>` is the name you want to give to the kernel.

    === "Conda environment"

        First, create your [conda environment](../../../../Software/Available_Applications/Miniforge3.md#module-loading-and-conda-environments-isolation). You will need to begin by loading conda:

        ``` sh
        # Load conda
        module purge && module load Miniforge3
        source $(conda info --base)/etc/profile.d/conda.sh
        export PYTHONNOUSERSITE=1
        ```

        Then create a kernel based on your newly created conda environment:

        ``` sh
        # Load JupyterLab
        module load JupyterLab

        # Create your conda environment
        conda create --prefix <conda_env_path>/my_conda_env python=3.11

        # Add your conda environment as a kernel to JupyterHub
        nesi-add-kernel <kernel_name> -p <conda_env_path>
        ```

        Where `<kernel_name>` is the name for your kernel. Alternatively, you can
        create the environment by name:

        ``` sh
        # Load JupyterLab
        module load JupyterLab

        # Create your conda environment
        conda create -n <conda_env_name>

        # Add your conda environment as a kernel to JupyterHub
        nesi-add-kernel <kernel_name> -n <conda_env_name>
        ```

        Where `<kernel_name>` is the name for your kernel.

    === "Python environment through Container"

        You can also use the `nesi-add-kernel` tool to base a kernel on a
        container. See the **Tool-Assisted Management → Python kernel** tab on the
        [Containers as kernels in JupyterLab](./containers_as_kernels_in_JupyterLab.md)
        page for the full instructions.

    !!! tip

        For more information about `nesi-add-kernel`, type into the terminal:

        ``` sh
        nesi-add-kernel --help
        ```

=== "Manual Management"

    If you need more control than the `nesi-add-kernel` tool provides, you can
    set up a custom kernel by hand.

    You can configure custom kernels for running your Jupyter
    notebooks. This could be necessary and/or recommended in some
    situations, including:

    - If you wish to load a different combination of environment modules
        than those we load in our default kernels
    - If you would like to activate a virtual environment or conda
        environment before launching the kernel

    The following examples create a custom kernel based on a conda environment,
    a Python virtual environment, or an R environment module:

    === "Conda environment"

        First, change directory into the path where you would like to place your
        conda environment.

        - If you would like to share it with other members of your project, use
            your project folder (`cd /nesi/project/<project-code>`)
        - Avoid paths that include `00_nesi_projects` or `home`, as these cause
            issues.

        Second, in a terminal run the following commands to load a
        [Miniforge environment module](../../../../Software/Available_Applications/Miniforge3.md#module-loading-and-conda-environments-isolation):

        ``` sh
        module purge && module load Miniforge3
        source $(conda info --base)/etc/profile.d/conda.sh
        export PYTHONNOUSERSITE=1
        ```

        Now create a conda environment named `my-conda-env` using Python 3.11.
        The *ipykernel* Python package is required but you can change the names
        of the environment, version of Python and install other Python packages
        as required.

        ``` sh
        conda create --prefix ./my-conda-env python=3.11
        conda activate ./my-conda-env
        conda install ipykernel
        # you can pip/conda install other packages here too
        ```

        Third, we will create a wrapper for your conda environment.
        Change directory into your `my-conda-env` folder:

        ``` sh
        cd my-conda-env
        ```

        And add the following as `wrapper.sh` into your `my-conda-env` folder
        (replace `<full_path_to_your_conda_env>` with the absolute path to the
        environment you created):

        ``` sh
        #!/usr/bin/env bash

        # load required modules here
        module purge
        module load Miniforge3

        # activate conda environment
        source $(conda info --base)/etc/profile.d/conda.sh
        conda deactivate  # workaround for https://github.com/conda/conda/issues/9392
        conda activate <full_path_to_your_conda_env>/my-conda-env

        # run the kernel
        exec python $@
        ```

        Make the wrapper script executable:

        ``` sh
        chmod +x wrapper.sh
        ```

        Fourth, create a directory for your kernel:

        ``` sh
        mkdir -p ~/.local/share/jupyter/kernels/my-conda-env
        cd ~/.local/share/jupyter/kernels/my-conda-env
        ```

        and create a file called *kernel.json*. It points the first element of
        the argv list at the wrapper script we just created. The file should look
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

        - Change `display_name` to what you would like to call your kernel by.

        After refreshing JupyterLab your new kernel should show up in the
        Launcher as "My Conda Env".

    === "Python virtual environment"

        First, change directory into the path where you would like to place your
        virtual environment.

        - If you would like to share it with other members of your project, use
            your project folder (`cd /nesi/project/<project-code>`)
        - avoid paths that include `00_nesi_projects` or `home`, as these cause
            issues.

        Second, in a terminal run the following commands to load a Python
        environment module:

        ``` sh
        module purge
        module load Python/3.14.4-foss-2026
        ```

        Now create a Python virtual environment named `my-venv`.
        The *ipykernel* Python package is required but you can change the name
        of the environment and install other Python packages as required.

        ``` sh
        python3 -m venv ./my-venv
        source ./my-venv/bin/activate
        pip install --upgrade pip
        pip install ipykernel
        # you can pip install other packages here too
        ```

        Third, we will create a wrapper for your virtual environment.
        Change directory into your `my-venv` folder:

        ``` sh
        cd my-venv
        ```

        And add the following as `wrapper.sh` into your `my-venv` folder:

        ``` sh
        #!/usr/bin/env bash

        # load required modules here
        module purge
        module load Python/3.14.4-foss-2026

        # activate virtual environment
        source <full_path_to_your_venv>/my-venv/bin/activate

        # run the kernel
        exec python $@
        ```

        Make the wrapper script executable:

        ``` sh
        chmod +x wrapper.sh
        ```

        Fourth, create a directory for your kernel:

        ``` sh
        mkdir -p ~/.local/share/jupyter/kernels/my-venv
        cd ~/.local/share/jupyter/kernels/my-venv
        ```

        and create a file called *kernel.json*. It points the first element of
        the argv list at the wrapper script we just created. The file should look
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
         "display_name": "My Venv",
         "language": "python"
        }
        ```

        - Change `display_name` to what you would like to call your kernel by.

        After refreshing JupyterLab your new kernel should show up in the
        Launcher as "My Venv".

    === "R kernel"

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

        Now create an R Jupyter kernel:

        ``` sh
        R -e "IRkernel::installspec(name='myrwithmpfr', displayname = 'R with MPFR', user = TRUE)"
        ```

        We must now edit the kernel to load the required environment
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
        chmod +x wrapper.sh
        ```

        and edit the *kernel.json* to change the first element of the argv list
        to point to the wrapper script we just created. The file should look
        like this:

        ```json
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
        ```

        - Change `display_name` to what you would like to call your kernel by.

        After refreshing JupyterLab your new R kernel should show up in the
        Launcher as "R with MPFR".

    === "Python environment through Container"

        You can also set up a kernel by hand that uses a container's version of
        Python. See the **Manual Management → Python kernel** tab on the
        [Containers as kernels in JupyterLab](./containers_as_kernels_in_JupyterLab.md)
        page for the full instructions.

## Listing your kernels

To list all the kernels that are currently installed, run:

``` sh
module purge
module load JupyterLab
jupyter-kernelspec list
```

This works for any kernel, regardless of whether it was registered using the
Tool-Assisted Management or Manual Management approach.

## Sharing a kernel

You can also configure a shared kernel that others with access to the same
project will be able to load. How you do this depends on whether you registered
the kernel with the tool-assisted or manual approach:

=== "Tool-Assisted Management"

    To share a kernel, register it with `nesi-add-kernel` as you normally would,
    but add the `--shared` flag so other members of your project can load it.
    Select the tab for the kind of kernel you are sharing:

    === "Environment module"

        First you need to open a terminal. It can be from a session on Jupyter
        via OnDemand or from a regular ssh connection on the Mahuika login node.

        - If you use the ssh option, make sure to load the JupyterLab module to
            have access to the `nesi-add-kernel` tool:

            ``` sh
            module purge  # remove all previously loaded modules
            module load JupyterLab
            ```

        Use the `nesi-add-kernel` command with the `--shared` flag to register a
        shared kernel:

        ``` sh
        nesi-add-kernel --shared <KERNEL_NAME> <MODULE>
        ```

        Where:

        - `<KERNEL_NAME>`: The name you want to give the kernel.
        - `<MODULE>`: The environment module to base the kernel on.

        Here is an example for adding a shared TensorFlow module to JupyterLab as
        a kernel:

        ``` sh
        nesi-add-kernel --shared tf_kernel_shared TensorFlow/2.8.2-gimkl-2022a-Python-3.10.5
        ```

    === "Python virtual environment"

        First, create your [python virtual environment](../../../../Software/Available_Applications/Python.md#installing-packages-in-your-home):

        ``` sh
        module purge
        module load Python/3.14.4-foss-2026  # Change the module to the version of python you want to use
        python3 -m venv ./my-venv
        pip install --upgrade pip
        # you can pip install other packages here too
        ```

        Then create a shared kernel based on your virtual environment:

        ``` sh
        module purge
        module load JupyterLab
        # The module of python you give here must be the same as the version of python you use to make the virtual environment
        nesi-add-kernel --shared <kernel_name> --venv my-venv
        ```

        Where `<kernel_name>` is the name you want to give to the kernel. Note
        the `--shared` flag in the `nesi-add-kernel` command line.

    === "Conda environment"

        First, create your [conda environment](../../../../Software/Available_Applications/Miniforge3.md#module-loading-and-conda-environments-isolation). You will need to begin by loading conda:

        ``` sh
        # Load conda
        module purge && module load Miniforge3
        source $(conda info --base)/etc/profile.d/conda.sh
        export PYTHONNOUSERSITE=1
        ```

        Then create a shared kernel based on your newly created conda environment:

        ``` sh
        # Load JupyterLab
        module load JupyterLab

        # Create your conda environment
        conda create --prefix <conda_env_path>/my_conda_env python=3.11

        # Add your conda environment as a shared kernel to JupyterHub
        nesi-add-kernel --shared <kernel_name> -p <conda_env_path>
        ```

        Where `<kernel_name>` is the name you want to give to the kernel. Note
        the `--shared` flag in the `nesi-add-kernel` command line. Alternatively,
        you can create the environment by name:

        ``` sh
        # Load JupyterLab
        module load JupyterLab

        # Create your conda environment
        conda create -n <conda_env_name>

        # Add your conda environment as a shared kernel to JupyterHub
        nesi-add-kernel --shared <kernel_name> -n <conda_env_name>
        ```

        Where `<kernel_name>` is the name you want to give to the kernel. Note
        the `--shared` flag in the `nesi-add-kernel` command line.

=== "Manual Management"

    For a manually-created kernel, you must make sure it also exists in a shared
    location (other users cannot see your home directory).

    First, **you** need to create the kernel yourself, following the manual steps
    in the **Manual Management** tab earlier on this page.

    Next, **your team members** need to set up the kernel on their side. The
    exact steps depend on the type of environment you created, so follow the
    steps in the tab that matches it:

    === "Conda environment"

        Second, **your team members** need to run the following commands in the
        terminal:

        ``` sh
        # change directory into the path that contains your conda environment
        cd <full_path_to_your_conda_environment>

        # load Miniforge3
        module purge
        module load Miniforge3

        # Activate your shared conda environment
        source $(conda info --base)/etc/profile.d/conda.sh
        conda activate ./my-conda-env
        ```

        Third, get **your team members** to create a directory for the kernel in
        their home directories:

        ``` sh
        mkdir -p ~/.local/share/jupyter/kernels/my-conda-env
        cd ~/.local/share/jupyter/kernels/my-conda-env
        ```

        and create a file called *kernel.json*. It points the first element of
        the argv list at the wrapper script we just created. The file should look
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

        - Change `display_name` to what you would like to call your kernel by.

        After refreshing JupyterLab your new kernel should show up in the
        Launcher as "My Conda Env".

    === "Python virtual environment"

        Second, **your team members** need to run the following commands in the
        terminal:

        ``` sh
        # load the Python environment module
        module purge
        module load Python/3.14.4-foss-2026

        # Activate the shared virtual environment
        source <full_path_to_your_venv>/my-venv/bin/activate
        ```

        Third, get **your team members** to create a directory for the kernel in
        their home directories:

        ``` sh
        mkdir -p ~/.local/share/jupyter/kernels/my-venv
        cd ~/.local/share/jupyter/kernels/my-venv
        ```

        and create a file called *kernel.json*. It points the first element of
        the argv list at the wrapper script we just created. The file should look
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
         "display_name": "My Venv",
         "language": "python"
        }
        ```

        - Change `display_name` to what you would like to call your kernel by.

        After refreshing JupyterLab your new kernel should show up in the
        Launcher as "My Venv".

## Removing a kernel

To delete a specific kernel, run:

``` sh
module purge
module load JupyterLab
jupyter-kernelspec list
jupyter-kernelspec remove <kernel_name>
```

where `<kernel_name>` is the name of the kernel to delete, as shown by
`jupyter-kernelspec list`.
