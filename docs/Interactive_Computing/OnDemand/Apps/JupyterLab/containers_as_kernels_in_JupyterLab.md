---
title: Containers as kernels in JupyterLab
description: How to use containers as kernels in JupyterLab on Mahuika
tags:
    - JupyterHub
---

To run a container as a kernel in JupyterLab, you first need to set up a Python
virtual environment by hand, in the same way as the Manual Management
approach described on the
[Python and R kernels in JupyterLab](./python_and_r_kernels_in_JupyterLab.md)
page.

In brief, the steps below create a Python virtual environment, install
`bash_kernel` into it, write a wrapper script that points `bash_kernel` at your
container, and then register that wrapper as a Jupyter kernel.

First, change directory into the path where you would like to place your
virtual environment.

- If you would like to share it with other members of your project, use your
    project folder (`cd /nesi/project/<project-code>`).
- Avoid paths that include `00_nesi_projects` or `home`, as these cause issues.

Second, in a terminal run the following commands to load a Python environment
module:

``` sh
module purge
module load Python/3.14.4-foss-2026
```

Now create a Python virtual environment named `my-container-venv`. You can
change the name of the environment and install other Python packages as
required.

``` sh
python3 -m venv ./my-container-venv
source ./my-container-venv/bin/activate
pip install --upgrade pip
```

Third, install `bash_kernel` in your virtual environment.

??? note "What is bash_kernel?"

    `bash_kernel` runs a bash shell as a Jupyter kernel. Here we point that bash shell at your container, so every cell you run in JupyterLab executes inside the container. It feels like a normal JupyterLab session, but the commands run in your container rather than on the host.

``` sh
pip install bash_kernel
```

Fourth, create a wrapper for your virtual environment. Change directory
into your `my-container-venv` folder:

``` sh
cd my-container-venv
```

And add the following as `wrapper.sh` into your `my-container-venv` folder:

``` sh
#!/usr/bin/env bash

# load required modules here
module purge
module load Python/3.14.4-foss-2026

# activate the virtual environment that has bash_kernel installed
source <full_path_to_your_venv>/my-container-venv/bin/activate

# tell bash_kernel to run inside your container instead of a normal bash shell
export BASH_KERNEL_CMD="apptainer exec --nv <full_path_to_your_container> bash"

# run the kernel on the host (it dispatches every command into the container)
exec python3 "$@"
```

The `BASH_KERNEL_CMD` environment variable is what makes this a *container*
kernel: `bash_kernel` itself runs on the host, but every cell you run in
JupyterLab is executed by the `bash` inside the container you point to. Update
the `apptainer exec` line to match your own image, for example:

``` sh
export BASH_KERNEL_CMD="apptainer exec --pwd /opt/PMDM --nv /nesi/project/<project-code>/containers/PMDM/pmdm_cu130.simg bash"
```

Make the wrapper script executable:

``` sh
chmod +x wrapper.sh
```

Fifth, install `bash_kernel` based on your new virtual environment:

``` sh
python3 -m bash_kernel.install --user
```

This installs a kernel into `~/.local/share/jupyter/kernels/bash`. We must now
edit it so the kernel runs through the wrapper script we created above. Change
to the directory the kernelspec was installed to:

``` sh
cd ~/.local/share/jupyter/kernels/bash
```

and edit the *kernel.json* to change the first element of the argv list to point
to the wrapper script we just created. The file should look like this:

```json
{
    "argv": [
        "<path_to_wrapper.sh>/wrapper.sh",
        "-m",
        "bash_kernel",
        "-f",
        "{connection_file}"
    ],
    "display_name": "Container Name",
    "language": "bash"
}
```

After refreshing JupyterLab your new kernel should show up in the Launcher under
the display name you set in `kernel.json` (`Container Name` in the example
above).

