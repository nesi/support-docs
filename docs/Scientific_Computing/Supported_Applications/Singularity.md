---
created_at: '2019-08-13T23:53:13Z'
hidden: false
position: 49
tags:
- containers
- singularity
- docker
title: Singularity
vote_count: 5
vote_sum: 5
zendesk_article_id: 360001107916
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

[Singularity](https://sylabs.io/singularity/) is a science-focused
application containerisation solution that is specifically tailored for
integration with HPC systems and suitable for deployment across a broad
range of science infrastructure environments. Singularity enables a high
level of portability for research applications across various Linux
distributions (and derivatives), from laptops to supercomputers.

Containerisation allows users to package a complete runtime environment
into a single *container image* (typically a single file), including
system libraries of various Linux flavours, custom user software,
configuration files, and most other dependencies. The container image
file can be easily copied and run on any Linux-based computing platform,
enabling simple portability and supporting reproducibility of scientific
results.

Unlike a virtual machine, a running *container instance* shares the host
operating system's kernel, relying heavily on [Linux
namespaces](https://en.wikipedia.org/wiki/Linux_namespaces) (kernel
partitioning and isolation features for previously global Linux system
resources). Resources and data outside of the container can be mapped
into the container to achieve integration, for example, Singularity
makes it simple to expose GPUs to the container and to access
input/output files & directories mounted on the host (such as those on
[shared
filesystems](../../Storage/File_Systems_and_Quotas/NeSI_File_Systems_and_Quotas)).

Contrary to other containerisation tools such as Docker, Singularity
removes the need for elevated privileges ("root access", e.g., via the
"sudo" command) at container runtime. This feature is essential for
enabling containers to run on shared platforms like an HPC, where users
cannot be allowed to elevate privileges for security reasons.
Singularity container images are also read-only by default at runtime,
to help reproducibility of results, and they integrate easily with
scheduling systems like Slurm and with MPI parallelisation.

Containerisation technologies, both the fundamental underlying Linux
kernel features, the various runtime support tools, and associated
cloud-services (such as container libraries, remote builders, and image
signing services), are a broad and fast moving landscape. The
information here is provided as an overview and may not necessarily be
completely up-to-date with the latest available features, however we
will endeavour to ensure it accurately reflects NeSI's currently
supported Singularity version.

## Building a new container

For more general information on building containers please see the
[Singularity
Documentation](https://sylabs.io/guides/3.0/user-guide/build_a_container.html). 

As building a container requires root privileges in general, this cannot
be done directly on any NeSI nodes. You will need to copy a [Singularity
Image Format (SIF)](https://github.com/sylabs/sif) to the cluster from
on a local Linux machine or the cloud. Alternatively you can make use of
a remote build service (currently only the
[syslabs](https://cloud.sylabs.io/builder) builder is available).

However, it is possible to build *some* containers directly on NeSI,
using the Milan compute nodes and [Apptainer](https://apptainer.org/).
Specific instructions are provided in a dedicated support page [Build an
Apptainer container on a Milan compute
node](../../Scientific_Computing/HPC_Software_Environment/Build_an_Apptainer_container_on_a_Milan_compute_node).
Please note **this may fail** to build some containers and encourage you
to contact us at <support@nesi.org.nz> if you encounter an issue.

### Remote Build Service

Running the command `singularity remote login` will provide you with a
link to [syslabs.io](https://cloud.sylabs.io/), once you have logged in
you will be prompted to create a key. Copying the string from your newly
created key into your terminal will authorise remote builds from your
current host.

Specify you want to use the remote builder by adding the `--remote` flag
to the build command.

``` sl
singularity build --remote myContainer.sif myContainer.def
```

### Build Environment Variables

The environment variables `SINGULARITY_TMPDIR` and
`SINGULARITY_CACHEDIR` environment can be used to overwrite the default
location of these directories. By default both of these values are set
to `/tmp` which has limited space, large builds may exceed this
limitation causing the builder to crash.

You may wish to change these values to somewhere in your project or
nobackup directory.

``` sl
export SINGULARITY_TMPDIR=/nesi/nobackup/nesi99999/.s_tmpdir
setfacl -b "$SINGULARITY_TMPDIR"  # avoid Singularity issues due to ACLs set on this folder
```

``` sl
export SINGULARITY_CACHEDIR=/nesi/nobackup/nesi99999/.s_cachedir
```

Please Sir, may I have a build node?

## Moving a container to NeSI

A container in Singularity's SIF format can be easily moved to the HPC
filesystem by:

-   Copying the image file from your local computer with basic file
    transfer tools - please refer to our documentation on [Moving files
    to/from the
    cluster](../../Getting_Started/Next_Steps/Moving_files_to_and_from_the_cluster)
    and [Data Transfer using
    Globus](https://support.nesi.org.nz/hc/en-gb/articles/360000576776)
    (if you have a very large container) for details
-   Downloading the container from an online repository

To download a container, use commands such as

``` bash
module load Singularity
singularity pull library://sylabsed/linux/alpine
```

Please refer to the [Singularity documentation](https://sylabs.io/docs/)
for further details.

## Using a Docker container

Singularity can transparently use Docker containers, without the need to
be root or to have Docker installed.

To download and convert a Docker container as a Singularity image, use
the `pull` command with a `docker://` prefix. The following example
downloads the latest version of the Ubuntu docker container and save it
in the `ubuntu.sif` Singularity image file:

``` sl
singularity pull ubuntu.sif docker://ubuntu
```

Access to private containers that needs registration is also supported,
as detailed in the [Singularity
documentation](https://sylabs.io/guides/master/user-guide/singularity_and_docker.html).

If you are building your own containers, you can also use Docker
containers as basis for a Singularity image, by specifying it in the
definition file as follows:

``` sl
Bootstrap: docker
From: ubuntu:latest

%post
    # intallation instructions go here
```

## Running a container on Mahuika or Māui Ancil

Singularity is not currently available on the Māui XC50 supercomputer.

Singularity containers can easily be run on Mahuika or Māui Ancil once
they are uploaded to a NeSI filesystem. Load the Singularity module
first by running the command

``` bash
module load Singularity
```

You can now execute a command inside the container using

``` bash
singularity exec my_container.sif <command>
```

If your container has a "%runscript" section, you can execute it using

``` bash
singularity run my_container.sif
```

To have a look at the contents of your container, you can "shell" into
it using

``` bash
singularity shell my_container.sif
```

Note the prompt is now prefixed with "Singularity",

``` bash
Singularity>
```

Exit the container by running the command

``` bash
Singularity> exit
```

which will bring you back to the host system.

### Accessing directories outside the container

Singularity containers are immutable by default to support
reproducibility of science results. Singularity will automatically bind
your home directory if possible, giving you access to all files in your
home directory tree.

If the work directory from which you spin up the container is outside
your home directory (e.g., in the "nobackup" or "project" file spaces)
and you need to access its contents, you will need to bind this
directory using, e.g., the command

``` sl
singularity run --bind $PWD my_container.sif
```

Note that older releases of Singularity bind the work directory
automatically.

You can easily bind extra directories and optionally change their
locations to a new path inside the container using, e.g.,

``` sl
singularity run --bind "/nesi/project/<your project ID>/inputdata:/var/inputdata,\
/nesi/nobackup/<your project ID>/outputdata:/var/outputdata" my_container.sif
```

Directories `inputdata` and `outputdata` can now be accessed inside your
container under `/var/inputdata` and `/var/outputdata`. Alternatively,
you can set environment variable `SINGULARITY_BIND` before running your
container,

``` bash
export SINGULARITY_BIND="/nesi/project/<your project ID>/inputdata:/var/inputdata,\
/nesi/nobackup/<your project ID>/outputdata:/var/outputdata"
```

### Accessing a GPU

If your Slurm job has requested access to an NVIDIA GPU (see [GPU use on
NeSI](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/GPU_use_on_NeSI)
to learn how to request a GPU), a singularity container can
transparently access it using the `--nv` flag:

``` bash
singularity run --nv my_container.sif
```
!!! prerequisite Note
     Make sure that your container contains the CUDA toolkit and additional
     libraries needed by your application (e.g. cuDNN). The `--nv` option
     only ensures that the basic CUDA libraries from the host are bound
     into the container and that the GPU device is accessible in the
     container.

### Network isolation

Singularity bridges the host network into the container by default. If
you want to isolate the network, add flags `--net --network=none` when
you run the container, e.g.,

``` bash
singularity run --net --network=none my_container.sif
```

### Slurm example

It is easy to run Singularity containers inside Slurm jobs. Here is an
example setup to run a container that uses 4 CPUs:

``` sl
#!/bin/bash -e
#SBATCH --job-name=singularity
#SBATCH --time=01:00:00
#SBATCH --mem=1024MB
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4

module load Singularity

# Bind directories and append SLURM job ID to output directory
export SINGULARITY_BIND="/nesi/project/<your project ID>/inputdata:/var/inputdata,\
/nesi/nobackup/<your project ID>/outputdata_${SLURM_JOB_ID:-0}:/var/outputdata"

# Run container %runscript
srun singularity run my_container.sif
```

Note that the output directory "outputdata" in the HPC file system is
automatically suffixed with the Slurm job ID in the above example, but
it is always available under the same path "/var/outputdata" from within
the container. This makes it easy to run multiple containers in separate
Slurm jobs. Please refer to our [SLURM: Reference
Sheet](../../Getting_Started/Cheat_Sheets/Slurm-Reference_Sheet) for
further details on using Slurm.

## Tips & Tricks

-   Make sure that your container runs before uploading it - you will
    not be able to rebuild it from a new definition file directly on the
    HPC
-   Try to configure all software to run in user space without requiring
    privilege escalation via "sudo" or other privileged capabilities
    such as reserved network ports - although Singularity supports some
    of these features inside a container on some systems, they may not
    always be available on the HPC or other platforms, therefore relying
    on features such as Linux user namespaces could limit the
    portability of your container
-   If your container runs an MPI application, make sure that the MPI
    distribution that is installed inside the container is compatible
    with Intel MPI
-   Write output data and log files to the HPC file system using a
    directory that is bound into the container - this helps
    reproducibility of results by keeping the container image immutable,
    it makes sure that you have all logs available for debugging if a
    job crashes, and it avoids inflating the container image file