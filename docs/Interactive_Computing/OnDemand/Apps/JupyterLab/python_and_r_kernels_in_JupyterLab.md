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
    environment module, a Python virtual environment, a Conda environment, 
    or an R environment:

    === "Environment module"

        !!! warning

            Your environment module needs to be based on Python. Contact [Mahuika Support](mailto:support@nesi.org.nz)
            if you are unsure about this.

        First you need to open a terminal. It can be from a session on Jupyter
        via OnDemand or from a regular ssh connection on the Mahuika login node.

        - If you use the ssh option, make sure to load the JupyterLab module to
            have access to the `nesi-add-kernel` tool:

            ``` sh
            module purge  # remove all previously loaded modules
            module load JupyterLab
            ```

        Second, use the `nesi-add-kernel` to register a kernel:

        ``` sh
        nesi-add-kernel <KERNEL_NAME> <MODULE>
        ```

        Where:

        - `<KERNEL_NAME>`: The name you want to give the kernel.
        - `<MODULE>`: The environment module to base the kernel on.

        !!! note "Sharing the kernel"

            or if you want to share the environment module with others in your project: 

            ``` sh
            nesi-add-kernel --shared <KERNEL_NAME> <MODULE>
            ```

        ??? tip "Need to add other modules to your kernel"

            If you would like to load other environment modules as well:

            1. Find your environment module kernel

                ``` sh
                geoff.weal@login03:~$ jupyter-kernelspec list
                Available kernels:
                ...
                <KERNEL_NAME>             /home/user.name/.local/share/jupyter/kernels/<KERNEL_NAME>
                ```

            2. Open the `kernel.json` file in the path given above. In this 
            example, this is given by `/home/user.name/.local/share/jupyter/kernels/<KERNEL_NAME>/kernel.json`:

            3. Find the path to the `wrapper.bash` file in `kernel.json`:

                ``` json hl_lines="3"
                {
                    "argv": [
                        "/home/user.name/.local/share/jupyter/kernels/<KERNEL_NAME>/wrapper.bash",
                        "-m",
                        "ipykernel_launcher",
                        "-f",
                        "{connection_file}"
                    ],
                    "display_name": "<KERNEL_NAME>",
                    "language": "python"
                }
                ```

            4. Open the `wrapper.bash` and add the modules you want to load in this file:

                ``` sh hl_lines="10"
                #!/usr/bin/env bash

                set -e

                # start with a clean environment
                module purge

                # load required modules
                module load <MODULE>
                # Add your other modules here

                # run the kernel
                exec python $@
                ```

        !!! example

            Here is an example for adding a TensorFlow module to JupyterLab as a kernel:

            ``` sh
            nesi-add-kernel tf_kernel TensorFlow/2.8.2-gimkl-2022a-Python-3.10.5
            ```

            or if you want to share the kernel:

            ``` sh
            nesi-add-kernel --shared tf_kernel TensorFlow/2.8.2-gimkl-2022a-Python-3.10.5
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

        Second, create a kernel based on your virtual environment:

        ``` sh
        module purge
        module load JupyterLab
        # The module of python you give here must be the same as the version of python you use to make the virtual environment
        nesi-add-kernel <kernel_name> --venv my-venv
        ```

        Where `<kernel_name>` is the name you want to give to the kernel.

        !!! note "Sharing your kernel" 
        
            If you would like to share your kernel with others in your project you will want to include the `--shared` flag in your `nesi-add-kernel` command line.

            ``` sh
            module purge
            module load JupyterLab
            # The module of python you give here must be the same as the version of python you use to make the virtual environment
            nesi-add-kernel --shared <kernel_name> --venv my-venv
            ```

    === "Conda environment"

        First, create your [conda environment](../../../../Software/Available_Applications/Miniforge3.md#module-loading-and-conda-environments-isolation). You will need to begin by loading conda:

        ``` sh
        # Load conda
        module purge && module load Miniforge3
        source $(conda info --base)/etc/profile.d/conda.sh
        export PYTHONNOUSERSITE=1
        ```

        Second, create a kernel based on your newly created conda environment:

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

        !!! note "Sharing your kernel"
        
            If you would like to share your kernel with others in your project you will want to include the `--shared` flag in your `nesi-add-kernel` command line.

            ``` sh
            # Load JupyterLab
            module load JupyterLab

            # Create your conda environment
            conda create --prefix <conda_env_path>/my_conda_env python=3.11

            # Add your conda environment as a kernel to JupyterHub
            nesi-add-kernel --shared <kernel_name> -p <conda_env_path>
            ```

            or

            ``` sh
            # Load JupyterLab
            module load JupyterLab

            # Create your conda environment
            conda create -n <conda_env_name>

            # Add your conda environment as a kernel to JupyterHub
            nesi-add-kernel --shared <kernel_name> -n <conda_env_name>
            ```

    === "R environment"

        First you need to open a terminal. It can be from a session on Jupyter
        via OnDemand or from a regular ssh connection on the Mahuika login node.

        - If you use the ssh option, make sure to load the JupyterLab module to
            have access to the `nesi-add-kernel` tool:

            ``` sh
            module purge  # remove all previously loaded modules
            module load JupyterLab
            ```

        Second, choose which version of `R` you want to use. This will be based 
        on what versions of `IRkernel` are available on Mahuika (`IRkernel` is 
        what allows `R` to run on Jupyterlab). You can see which versions of 
        `IRkernel` (and their associated `R` versions) are available by typing 
        `module avail IRkernel` into the terminal:

        ``` sh
        user.name@login03:~$ module avail IRkernel

        ----------- /opt/nesi/lmod/mahuika -----------
        IRkernel/1.0.1-gimkl-2018b
        IRkernel/1.1.1-gimkl-2020a-R-3.6.2
        IRkernel/1.1.1-gimkl-2020a-R-4.0.1
        IRkernel/1.2-gimkl-2020a-R-4.1.0
        IRkernel/1.3.1-gimkl-2022a-R-4.2.1 (D)

        Where:
        D:  Default Module
        ```

        Third, use the `nesi-add-kernel` to register a kernel:

        ``` sh
        nesi-add-kernel <KERNEL_NAME> <IRKERNEL_MODULE>
        ```

        Where:

        - `<KERNEL_NAME>`: The name you want to give the kernel.
        - `<IRKERNEL_MODULE>`: The `IRkernel` environment module to base the kernel on.

        !!! note "Sharing the kernel"

            or if you want to share the `R` environment module with others in your project: 

            ``` sh
            nesi-add-kernel --shared <KERNEL_NAME> <IRKERNEL_MODULE>
            ```

        ??? tip "Need to add other modules to your R kernel"

            If you would like to load other environment modules as well:

            1. Find your environment module kernel

                ``` sh
                geoff.weal@login03:~$ jupyter-kernelspec list
                Available kernels:
                ...
                <KERNEL_NAME>             /home/user.name/.local/share/jupyter/kernels/<KERNEL_NAME>
                ```

            2. Open the `kernel.json` file in the path given above. In this 
            example, this is given by `/home/user.name/.local/share/jupyter/kernels/<KERNEL_NAME>/kernel.json`:

            3. Find the path to the `wrapper.bash` file in `kernel.json`:

                ``` json hl_lines="3"
                {
                    "argv": [
                        "/home/user.name/.local/share/jupyter/kernels/<KERNEL_NAME>/wrapper.bash",
                        "-m",
                        "ipykernel_launcher",
                        "-f",
                        "{connection_file}"
                    ],
                    "display_name": "<KERNEL_NAME>",
                    "language": "R"
                }
                ```

            4. Open the `wrapper.bash` and add the modules you want to load in this file:

                ``` sh hl_lines="10"
                #!/usr/bin/env bash

                set -e

                # start with a clean environment
                module purge

                # load required modules
                module load <IRKERNEL_MODULE>
                # Add your other modules here

                # run the kernel
                exec R $@
                ```

        !!! example

            Here is an example for adding the `IRkernel/1.3.1-gimkl-2022a-R-4.2.1` module to JupyterLab as a kernel:

            ``` sh
            nesi-add-kernel r_kernel IRkernel/1.3.1-gimkl-2022a-R-4.2.1
            ```

            or if you want to share the kernel:

            ``` sh
            nesi-add-kernel --shared r_kernel IRkernel/1.3.1-gimkl-2022a-R-4.2.1
            ```

    === "Python environment through Container"

        You can also use the `nesi-add-kernel` tool to base a kernel on a
        container. See the [**Tool-Assisted Management → Python kernel**](./containers_as_kernels_in_JupyterLab.md#__tabbed_2_1)
        tab on the [Containers as kernels in JupyterLab](./containers_as_kernels_in_JupyterLab.md)
        page for the full instructions.

    !!! tip

        For more information about `nesi-add-kernel`, type into the terminal:

        ``` sh
        nesi-add-kernel --help
        ```

=== "Manual Management"

    If you need more control than the `nesi-add-kernel` tool provides, you can
    set up a custom kernel by hand.

    The following examples create a custom kernel based on an environment module, 
    a Python virtual environment, a Conda environment, or an R environment:

    === "Environment module"

        !!! warning

            Your environment module needs to be based on Python. Contact [Mahuika Support](mailto:support@nesi.org.nz)
            if you are unsure about this.

        First, change directory into the path where you would like to place your
        virtual environment.

        - If you would like to share it with other members of your project, use
            your project folder (`cd /nesi/project/<project-code>`)
        - avoid paths that include `00_nesi_projects` or `home`, as these cause
            issues.
        
        Second, add the following as `wrapper.sh` into your directory:

        ``` sh
        #!/usr/bin/env bash

        # load required modules here
        module purge
        module load <MODULE_NAME>

        # run the kernel
        exec python $@
        ```

        Where `<MODULE_NAME>` is the name of the module you would like to use. 

        Third, make the wrapper script executable:

        ``` sh
        chmod +x wrapper.sh
        ```

        Fourth, create a directory for your kernel:

        ``` sh
        mkdir -p ~/.local/share/jupyter/kernels/my-environment
        cd ~/.local/share/jupyter/kernels/my-environment
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
         "display_name": "My environment module",
         "language": "python"
        }
        ```

        - Change `display_name` to what you would like to call your kernel by.

        After refreshing JupyterLab your new kernel should show up in the
        Launcher as "My environment module".

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

        Third, create a Python virtual environment named `my-venv`.
        The *ipykernel* Python package is required but you can change the name
        of the environment and install other Python packages as required.

        ``` sh
        python3 -m venv ./my-venv
        source ./my-venv/bin/activate
        pip install --upgrade pip
        pip install ipykernel
        # you can pip install other packages here too
        ```

        Fourth, we will create a wrapper for your virtual environment.
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

        Fifth, create a directory for your kernel:

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

        Third, create a conda environment named `my-conda-env` using Python 3.11.
        The *ipykernel* Python package is required but you can change the names
        of the environment, version of Python and install other Python packages
        as required.

        ``` sh
        conda create --prefix ./my-conda-env python=3.11
        conda activate ./my-conda-env
        conda install ipykernel
        # you can pip/conda install other packages here too
        ```

        Fourth, we will create a wrapper for your conda environment.
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

        Fifth, create a directory for your kernel:

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

    === "R environment"

        First, change directory into the path where you would like to place your
        custom R environment kernel.

        - If you would like to share it with other members of your project, use
            your project folder (`cd /nesi/project/<project-code>`)
        - Avoid paths that include `00_nesi_projects` or `home`, as these cause
            issues.

        Second, write the following as `wrapper.sh` in your selected directory:

        ``` sh
        #!/usr/bin/env bash

        # load required modules here
        module purge
        module load IRkernel/1.1.1-gimkl-2020a-R-3.6.2
        # Add other modules you would like to load here as well, e.g.: module load MPFR/4.0.2-GCCcore-9.2.0

        # run the kernel
        exec R $@
        ```

        Make the wrapper script executable:

        ``` sh
        chmod +x wrapper.sh
        ```

        Third, create a directory for your kernel:

        ``` sh
        mkdir -p ~/.local/share/jupyter/kernels/my-r-environment
        cd ~/.local/share/jupyter/kernels/my-r-environment
        ```

        and create a file called *kernel.json*. It points the first element of
        the argv list at the wrapper script we just created. The file should look
        like this:

        ```json
        {
         "argv": [
         "<full_path_to_your_wrapper_file>/wrapper.sh",
         "--slave",
         "-e",
         "IRkernel::main()",
         "--args",
         "{connection_file}"
         ],
         "display_name": "R with XYZ",
         "language": "R"
        }
        ```

        - Change `display_name` to what you would like to call your kernel by.

        After refreshing JupyterLab your new kernel should show up in the
        Launcher as "R with XYZ".

    === "Python environment through Container"

        You can also set up a kernel by hand that uses a container's version of
        Python. See the [**Manual Management → Python kernel**](./containers_as_kernels_in_JupyterLab.md#__tabbed_3_1)
        tab on the [Containers as kernels in JupyterLab](./containers_as_kernels_in_JupyterLab.md)
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
    
    Notes about how to share kernels with other project members can be found in the
    [Tool-Assisted Management](#__tabbed_1_1) tab of the Adding a Kernel to JupyterLab
    Section

=== "Manual Management"

    For a manually-created kernel, you must make sure it also exists in a shared
    location (other users cannot see your home directory).

    First, **you** need to create the kernel yourself, following the manual steps
    in the [**Manual Management**](#__tabbed_1_2) tab earlier on this page.

    **Your team members** then need to set up the kernel on their side. The
    exact steps depend on the type of environment you created, so follow the
    steps in the tab that matches it:

    === "Environment module"

        The `wrapper.sh` script and the environment module it loads already live
        in the shared project folder, so **your team members** only need to
        know the path to the kernel's `wrapper.sh` file.

        Second, get **your team members** to create a directory for the kernel in
        their home directories:

        ``` sh
        mkdir -p ~/.local/share/jupyter/kernels/my-environment
        cd ~/.local/share/jupyter/kernels/my-environment
        ```

        and create a file called *kernel.json*. It points the first element of
        the argv list at the shared wrapper script. The file should look like
        this:

        ```json
        {
         "argv": [
         "<full_path_to_your_wrapper_file>/wrapper.sh",
         "-m",
         "ipykernel_launcher",
         "-f",
         "{connection_file}"
         ],
         "display_name": "My environment module",
         "language": "python"
        }
        ```

        - Change `<full_path_to_your_wrapper_file>` to the path of the `wrapper.sh` file for the kernel. 
        - Change `display_name` to what you would like to call your kernel by.

        After refreshing JupyterLab the new kernel should show up in the
        Launcher as "My environment module".

    === "Python virtual environment"

        The `wrapper.sh` script and the virtual environment it activates already
        live in the shared project folder, so **your team members** only need to
        know the path to the kernel's `wrapper.sh` file.

        Second, get **your team members** to create a directory for the kernel in
        their home directories:

        ``` sh
        mkdir -p ~/.local/share/jupyter/kernels/my-venv
        cd ~/.local/share/jupyter/kernels/my-venv
        ```

        and create a file called *kernel.json*. It points the first element of
        the argv list at the shared wrapper script. The file should look
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

        - Change `<full_path_to_your_wrapper_file>` to the path of the `wrapper.sh` file for the kernel. 
        - Change `display_name` to what you would like to call your kernel by.

        After refreshing JupyterLab your new kernel should show up in the
        Launcher as "My Venv".

    === "Conda environment"

        The `wrapper.sh` script and the conda environment it activates already
        live in the shared project folder, so **your team members** only need to
        know the path to the kernel's `wrapper.sh` file.

        Second, get **your team members** to create a directory for the kernel in
        their home directories:

        ``` sh
        mkdir -p ~/.local/share/jupyter/kernels/my-conda-env
        cd ~/.local/share/jupyter/kernels/my-conda-env
        ```

        and create a file called *kernel.json*. It points the first element of
        the argv list at the shared wrapper script. The file should look
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

        - Change `<full_path_to_your_wrapper_file>` to the path of the `wrapper.sh` file for the kernel. 
        - Change `display_name` to what you would like to call your kernel by.

        After refreshing JupyterLab your new kernel should show up in the
        Launcher as "My Conda Env".

    === "R environment"

        The `wrapper.sh` script and the R environment modules it loads already
        live in the shared project folder, so **your team members** only need to
        know the path to the kernel's `wrapper.sh` file.

        Second, get **your team members** to create a directory for the kernel in
        their home directories:

        ``` sh
        mkdir -p ~/.local/share/jupyter/kernels/my-r-environment
        cd ~/.local/share/jupyter/kernels/my-r-environment
        ```

        and create a file called *kernel.json*. It points the first element of
        the argv list at the shared wrapper script. The file should look like
        this:

        ```json
        {
         "argv": [
         "<full_path_to_your_wrapper_file>/wrapper.sh",
         "--slave",
         "-e",
         "IRkernel::main()",
         "--args",
         "{connection_file}"
         ],
         "display_name": "R with XYZ",
         "language": "R"
        }
        ```

        - Change `<full_path_to_your_wrapper_file>` to the path of the `wrapper.sh` file for the kernel. 
        - Change `display_name` to what you would like to call your kernel by.

        After refreshing JupyterLab the new kernel should show up in the
        Launcher as "R with XYZ".

    === "Python environment through Container"

        For a container-based kernel, see the [**Manual Management → Python kernel**](./containers_as_kernels_in_JupyterLab.md#__tabbed_6_1)
        tab of the *Sharing a kernel* section on the
        [Containers as kernels in JupyterLab](./containers_as_kernels_in_JupyterLab.md)
        page for the full instructions.

## Removing a kernel

<h3 id="remove-a-user-specific-kernel">Remove a user-specific kernel</h3>

To delete a user-specific kernel, run:

``` sh
module purge
module load JupyterLab
jupyter-kernelspec list
jupyter-kernelspec remove <kernel_name>
```

where `<kernel_name>` is the name of the kernel to delete, as shown by
`jupyter-kernelspec list`.

<h3 id="remove-a-shared-kernel">Remove a shared kernel</h3>

If the kernel was shared with your project, it instead lives in the project
folder. Delete the kernel's directory:

``` sh
rm -r /nesi/project/<ACCOUNT_ID>/.jupyter/share/jupyter/kernels/<KERNEL_NAME>
```

where `<ACCOUNT_ID>` is your project's account code and `<KERNEL_NAME>` is the name of
the kernel to delete.
