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
operating system\'s kernel, relying heavily on [Linux
namespaces](https://en.wikipedia.org/wiki/Linux_namespaces) (kernel
partitioning and isolation features for previously global Linux system
resources). Resources and data outside of the container can be mapped
into the container to achieve integration, for example, Singularity
makes it simple to expose GPUs to the container and to access
input/output files & directories mounted on the host (such as those on
[shared
filesystems](https://support.nesi.org.nz/hc/en-gb/articles/360000177256)).

Contrary to other containerisation tools such as Docker, Singularity
removes the need for elevated privileges (\"root access\", e.g., via the
\"sudo\" command) at container runtime. This feature is essential for
enabling containers to run on shared platforms like an HPC, where users
cannot be allowed to elevate privileges for security reasons.
Singularity container images are also read-only by default at runtime,
to help reproducibility of results, and they integrate easily with
scheduling systems like Slurm and with MPI parallelisation.

Containerisation technologies, both the fundamental underlying Linux
kernel features, the various runtime support tools, and associated
cloud-services (such as container libraries, remote builders, and image
signing services), are a broad and fast moving landscape. The
information here is provided as an overview and may not be necessarily
be completely up-to-date with the latest available features, however we
will endeavour to ensure it accurately reflects NeSI\'s currently
supported Singularity version.

Building a new container
========================

Please note that **building a new container from a container definition
file is not currently possible on any NeSI machines **as it requires
either elevated privileges (\"root access\") or use of *user namespaces*
(which we do not yet support). If you see error messages of the kind

    FATAL: Unable to build from my_new_container.def: you must be the root user to build from a definition file

during the build process, you will need to build the container on a
local Linux system or in the cloud using the [Singularity Image Format
(SIF)](https://github.com/sylabs/sif). The SIF format produces a single
compressed container image that can be easily moved to the HPC
afterwards.

Note that the build process from definition files can be quite demanding
in terms of privilege requirements - even if you have root access to
your system, further Linux security features such as restrictive
partition mount options can inhibit a successful build. Please refer to
the [Singularity documentation](https://sylabs.io/docs/) for further
details.

 

Moving a container to NeSI
==========================

A container in Singularity\'s SIF format can be easily moved to the HPC
filesystem by:

-   Copying the image file from your local computer with basic file
    transfer tools - please refer to our documentation on [Moving files
    to/from the
    cluster](https://support.nesi.org.nz/hc/en-gb/articles/360000578455)
    and [Data Transfer using
    Globus](https://support.nesi.org.nz/hc/en-gb/articles/360000576776)
    (if you have a very large container) for details
-   Downloading the container from an online repository

To download a container, use commands such as

    module load Singularity
    singularity pull library://sylabsed/linux/alpine

Please refer to the [Singularity documentation](https://sylabs.io/docs/)
for further details.

Running a container on Mahuika or Māui Ancil
============================================

Singularity is not currently available on the Māui XC50 supercomputer.

Singularity containers can easily be run on Mahuika or Māui Ancil once
they are uploaded to a NeSI filesystem. Load the Singularity module
first by running the command

    module load Singularity

You can now execute a command inside the container using

    singularity exec my_container.sif <command>

If your container has a \"%runscript\" section, you can execute it using

    singularity run my_container.sif

To have a look at the contents of your container, you can \"shell\" into
it using

    singularity shell my_container.sif

Note the prompt is now prefixed with \"Singularity\",

    Singularity my_container.sif:~>

Exit the container by running the command

    Singularity my_container.sif:~> exit

which will bring you back to the host system.

Accessing directories outside the container
-------------------------------------------

Singularity containers are immutable by default to support
reproducibility of science results. Singularity will automatically bind
your home directory if possible, giving you access to all files in your
home directory tree.

If the work directory from which you spin up the container is outside
your home directory (e.g., in the \"nobackup\" or \"project\" file
spaces) and you need to access its contents, you will need to bind this
directory using, e.g., the command

    singularity run --bind $PWD my_container.sif

Note that older releases of Singularity bind the work directory
automatically.

You can easily bind extra directories and optionally change their
locations to a new path inside the container using, e.g.,

    singularity run --bind "/nesi/project/<your project ID>/inputdata:/var/inputdata,\
    /nesi/nobackup/<your project ID>/outputdata:/var/outputdata" my_container.sif

Directories \"inputdata\" and \"outputdata\" can now be accessed inside
your container under \"/var/inputdata\" and \"/var/outputdata\".
Alternatively, you can set environment variable \"SINGULARITY\_BIND\"
before running your container,

    export SINGULARITY_BIND="/nesi/project/<your project ID>/inputdata:/var/inputdata,\
    /nesi/nobackup/<your project ID>/outputdata:/var/outputdata"

Network isolation
-----------------

Singularity bridges the host network into the container by default. If
you want to isolate the network, add flags \"\--net \--network=none\"
when you run the container, e.g.,

    singularity run --net --network=none my_container.sif

Slurm example
-------------

It is easy to run Singularity containers inside Slurm jobs. Here is an
example setup to run a container that uses 4 CPUs:

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

Note that the output directory \"outputdata\" in the HPC file system is
automatically suffixed with the Slurm job ID in the above example, but
it is always available under the same path \"/var/outputdata\" from
within the container. This makes it easy to run multiple containers in
separate Slurm jobs. Please refer to our [SLURM: Reference
Sheet](https://support.nesi.org.nz/hc/en-gb/articles/360000691716) for
further details on using Slurm.

Tips & Tricks
=============

-   Make sure that your container runs before uploading it - you will
    not be able to rebuild it from a new definition file directly on the
    HPC
-   Try to configure all software to run in user space without requiring
    privilege escalation via \"sudo\" or other privileged capabilities
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
