---
created_at: '2022-12-08T00:55:40Z'
tags: []
title: Build an Apptainer container on a Milan compute node
vote_count: 0
vote_sum: 0
zendesk_article_id: 6008779241999
zendesk_section_id: 360000040056
---

This article describes a technique to build
[Apptainer](https://apptainer.org/) containers using [Milan compute
nodes](../../Scientific_Computing/Running_Jobs_on_Maui_and_Mahuika/Milan_Compute_Nodes.md),
via a Slurm job. You can also build
[Singularity](../../Scientific_Computing/Supported_Applications/Singularity.md)
container using this technique.

## Building container via Slurm

The new Milan compute nodes can be used to build Apptainer containers
using the [fakeroot
feature](https://apptainer.org/docs/user/main/fakeroot.html). This
functionality is only available on these nodes at the moment due to
their operating system version.

To illustrate this functionality, create an example container definition
file `my_container.def` from a shell session on NeSI as follows:

```sh
cat << EOF > my_container.def
BootStrap: docker
From: ubuntu:20.04
%post
    apt-get -y update
    apt-get install -y wget
EOF
```

Then submit the following Slurm job submission script to build the
container:

```sl
#!/bin/bash -e
#SBATCH --job-name=apptainer_build
#SBATCH --partition=milan
#SBATCH --time=0-00:30:00
#SBATCH --mem=4GB
#SBATCH --cpus-per-task=2

# load environment module
module purge
module load Apptainer/1.2.2

# recent Apptainer modules set APPTAINER_BIND, which typically breaks
# container builds, so unset it here
unset APPTAINER_BIND

# create a build and cache directory on nobackup storage
export APPTAINER_CACHEDIR="/nesi/nobackup/$SLURM_JOB_ACCOUNT/$USER/apptainer_cache"
export APPTAINER_TMPDIR="/nesi/nobackup/$SLURM_JOB_ACCOUNT/$USER/apptainer_tmpdir"
mkdir -p $APPTAINER_CACHEDIR $APPTAINER_TMPDIR
setfacl -b $APPTAINER_TMPDIR

# build the container
apptainer build --force --fakeroot my_container.sif my_container.def
```

Note this script will start an Slurm job for 30 minutes using 2 cores
and 4 GB of memory to build the image. Make sure to set these resources
correctly, some containers can take hours to build and require tens of
GB of memory.

Option `--force` will rebuild *my_container.sif* even if it already is in
the directory.

More information about how to submit a Slurm job is available in the
[Submitting your first../../Getting_Started/Submitting_A_Job/Submitting_your_first_job.md
job](../../Getting_Started/Next_Steps/Submitting_your_first_job.md)
support page.

!!! info "Build environment variables"
     To build containers, you need to ensure that Apptainer has enough
     storage space to create intermediate files. It also requires a cache
     folder to save images pulled from a different location (e.g.
     DockerHub). By default both of these locations are set to `/tmp` which
     has limited space, large builds may exceed this limitation causing the
     builder to crash. The environment variables `APPTAINER_TMPDIR` and
     `APPTAINER_CACHEDIR` are used to overwrite the default location of
     these directories.
     In this example, the Slurm job submission script creates these folders
     using your project `nobackup` folder.

## Known limitations

If your container uses RPM to install packages, i.e. is based on CentOS
or Rocky Linux, you need to disable the `APPTAINER_TMPDIR` environment
variable (use `unset APPTAINER_TMPDIR`) and request more memory for your
Slurm job. Otherwise, RPM will crash due to an incompatibility with the
`nobackup` filesystem.

If you encounter the following error when using a base Docker image in
your Apptainer definition file

```stderr
While making image from oci registry: error fetching image to cache: while building SIF from layers: conveyor failed to get: unsupported image-specific operation on artifact with type "application/vnd.docker.container.image.v1+json"
```

it is likely due to an upstream issue (e.g. bad image on Dockerhub). In
this case, try an older image version or a different base image.

!!! warning "Other limitations"
     This method, using fakeroot, is known to **not** work for all types of
     Apptainer/Singularity containers.
     If you encounter an issue, please {% include "partials/support_request.html" %}
