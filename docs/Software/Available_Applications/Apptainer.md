---
created_at: '2025-01-01T00:00:00Z'
description: How to use Apptainer containers on the NeSI HPC.
tags:
    - apptainer
    - container
    - docker
    - portable
    - reproducibility
---

Apptainer simplifies the creation and execution of containers on compute clusters, ensuring software components are portable and reproducible. It is an open-source fork of the Singularity project and shares much of the same functionality. Apptainer is distributed under the [BSD License](https://github.com/apptainer/apptainer/blob/main/LICENSE.md).

## Configure your environment

By default, Apptainer uses your home directory for all storage, creating a hidden directory `~/.apptainer`. Since home directories are limited in size, we recommend changing this to one of your project directories:

```bash
export APPTAINER_CACHEDIR="/nesi/nobackup/nesi12345/apptainer-cache"
export APPTAINER_TMPDIR=${APPTAINER_CACHEDIR}
mkdir -p $APPTAINER_CACHEDIR
```

To make these changed permanent, add them to your `~/.bashrc`:

```bash
echo 'export APPTAINER_CACHEDIR="/nesi/nobackup/nesi12345/apptainer-cache"' >> ~/.bashrc
echo 'export APPTAINER_TMPDIR=${APPTAINER_CACHEDIR}' >> ~/.bashrc
```

## Pulling a container image

Docker images are OCI-compliant and can be pulled as Apptainer SIF (Singularity Image Format) files directly from Docker Hub or other registries. [Docker Hub](https://hub.docker.com) is a good starting point for commonly used research software.

For example, to pull a TensorFlow GPU image from Docker Hub:

1. Find the image on [Docker Hub](https://hub.docker.com) — for TensorFlow, the image is `tensorflow/tensorflow`.
2. Convert the `docker pull` reference to an Apptainer URL by prefixing it with `docker://`, appending a tag for the version you need.
3. Pull the image with `apptainer pull`, using a `.sif` file extension:

```bash
apptainer pull tensorflow.sif docker://tensorflow/tensorflow:latest-gpu
```

## Building a container

`fakeroot` is enabled on both login nodes and compute nodes, allowing you to build containers without root privileges. Since builds can consume significant CPU and memory, we recommend running them as a Slurm job rather than on the login node.

First, create a container definition file:

```bash
cat << EOF > my_container.def
BootStrap: docker
From: ubuntu:20.04
%post
    apt-get -y update
    apt-get install -y wget
    mkdir -p /opt/nesi
EOF
```

Then submit the following script to build the container:

```sl
#!/bin/bash -e

#SBATCH --job-name      apptainer-build
#SBATCH --time          00:30:00
#SBATCH --mem           4GB
#SBATCH --cpus-per-task 2
#SBATCH --account       nesi99991

unset APPTAINER_BIND

export APPTAINER_CACHEDIR="/nesi/nobackup/$SLURM_JOB_ACCOUNT/$USER/apptainer_cache"
export APPTAINER_TMPDIR=${APPTAINER_CACHEDIR}
mkdir -p ${APPTAINER_CACHEDIR}

apptainer build my_container.sif my_container.def
```

!!! warning
    NeSI systems bind `/opt/nesi` into running containers. If your base image does not include this directory, the build will fail with a mount error.
    We recommend `unset APPTAINER_BIND` before you build. Alternatively you can add `mkdir -p /opt/nesi` to your `%post` section (as above) prevents this.

    If you see the following error, it is likely caused by a bad upstream image on Docker Hub. Try an older version or a different base image:

    ```stderr
    error fetching image to cache: while building SIF from layers: conveyor failed to get: 
    unsupported image-specific operation on artifact with type "application/vnd.docker.container.image.v1+json"
    ```

    The `fakeroot` build method does not work for all container types. If you encounter other issues, {% include "partials/support_request.html" %}.

## Running a container

### Interactive shell

Connect to a container interactively with `apptainer shell`. Your prompt will change to `Apptainer>` when inside the container:

```bash
apptainer shell tensorflow.sif
```

Exit the container with `exit`.

### Inspecting a container

To view metadata and configuration details about a container image:

```bash
apptainer inspect tensorflow.sif
```

### Running commands

Use `apptainer exec` to run a specific command inside a container without entering an interactive shell:

```bash
apptainer exec tensorflow.sif python --version
```

Use `apptainer run` to execute the container's default runscript as defined by its creator:

```bash
apptainer run tensorflow.sif
```

### Slurm batch job

```sl
#!/bin/bash -e

#SBATCH --job-name      container-job
#SBATCH --time          01:00:00
#SBATCH --mem           4G
#SBATCH --cpus-per-task 4
#SBATCH --account       nesi12345

apptainer exec tensorflow.sif python my_script.py
```

## Binding directories

By default, Apptainer only mounts your home directory inside the container. To access data in your project or nobackup directories, bind them explicitly using the `--bind` flag:

```bash
apptainer exec --bind /nesi/project/nesi12345:/project tensorflow.sif python /project/my_script.py
```

The format is `--bind <host-path>:<container-path>`. You can bind multiple directories in a single command:

```bash
apptainer exec \
    --bind /nesi/project/nesi12345:/project \
    --bind /nesi/nobackup/nesi12345:/nobackup \
    tensorflow.sif python /project/my_script.py
```

Alternatively, set `APPTAINER_BIND` as an environment variable to apply binds automatically to every `apptainer` call in your session:

```bash
export APPTAINER_BIND="/nesi/project/nesi12345:/project,/nesi/nobackup/nesi12345:/nobackup"
```

## GPU access

### Running on GPU

If your Slurm job has requested a GPU (see [GPU use on Mahuika](../../Batch_Computing/Using_GPUs.md)), pass the `--nv` flag to give the container transparent access to it:

```sl
#!/bin/bash -e

#SBATCH --job-name      gpu-container-job
#SBATCH --time          01:00:00
#SBATCH --mem           8G
#SBATCH --cpus-per-task 4
#SBATCH --gpus-per-node 1
#SBATCH --account       nesi12345

apptainer exec --nv --bind /nesi/project/nesi12345:/project \
    tensorflow-latest-gpu.sif python /project/my_script.py
```

### Building with GPU compilers

To compile code using GPU compilers inside a container, start an interactive shell with the `--nv` flag to expose the GPU hardware:

```bash
apptainer shell --nv tensorflow-latest-gpu.sif
```

GPU compilers such as `nvc++` are then available inside the container:

```bash
Apptainer> CXX=nvc++ cmake -DOPENACC=1 ..
Apptainer> make
Apptainer> exit
```

The compiled binary can be run via a GPU Slurm job:

```bash
srun --gpus-per-node=1 apptainer exec --nv \
    tensorflow-latest-gpu.sif ./my_application
```

## MPI

Running MPI applications inside a container requires the MPI implementation inside the container to match the host MPI version. For best performance, the host MPI library is bound into the container and the job is launched by the host's `mpiexec`.

The following example uses Intel MPI. Set `I_MPI_ROOT` to the path of the Intel MPI installation on the host, then bind it into the container:

```sl
#!/bin/bash -e

#SBATCH --job-name      mpi-container-job
#SBATCH --time          00:05:00
#SBATCH --ntasks        8
#SBATCH --nodes         2
#SBATCH --account       nesi12345

module purge
module load impi

mpiexec -n ${SLURM_NTASKS} --bind-to none --map-by slot \
    apptainer exec --bind $I_MPI_ROOT:$I_MPI_ROOT my_mpi_app.sif \
    /path/to/my_application
```

!!! note
    The MPI version inside the container must be compatible with the host MPI. {% include "partials/support_request.html" %} if you need help identifying the correct host MPI path.

## Tips and best practices

- Configure software to run in user space — Apptainer supports some privileged features on certain systems, but relying on them reduces portability across HPC platforms.
- If your container runs an MPI application, ensure the MPI distribution inside the container is compatible with the cluster's MPI version.
- Write output data and log files to the HPC filesystem via a bound directory rather than inside the container image. This keeps the image immutable, ensures logs are available for debugging, and avoids inflating the image file size.

??? note "Network isolation"

    The `--net` flag isolates the container's network to a loopback interface, preventing communication with the host or external networks:

    ```bash
    apptainer exec --net --network=none my_container.sif
    ```

    To run a network service (e.g. a web server) from within a container, configure it to use an unprivileged port (above 1024). For example, to run Nginx on port 8080:

    ```singularity
    Bootstrap: docker
    From: nginx
    Includecmd: no

    %post
        sed -i 's/80/8080/' /etc/nginx/conf.d/default.conf

    %startscript
    nginx
    ```

    Start and stop the container instance with:

    ```bash
    apptainer instance start nginx.sif nginx
    apptainer instance stop nginx
    ```

## Further documentation

- [Apptainer documentation](https://apptainer.org/docs/)
- [BioContainers registry](https://biocontainers.pro/)
- [Docker Hub](https://hub.docker.com)
