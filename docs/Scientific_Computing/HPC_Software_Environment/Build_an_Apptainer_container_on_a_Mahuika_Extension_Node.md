---
created_at: '2022-12-08T00:55:40Z'
hidden: true
label_names: []
position: 0
title: Build an Apptainer container on a Mahuika Extension Node
vote_count: 0
vote_sum: 0
zendesk_article_id: 6008779241999
zendesk_section_id: 360000040056
---

> ### Service Status
>
> Mahuika's new nodes are in an **Early Access Programme (EAP) phase**
> and not fully in production.
>
> See [Mahuika Extension
> Onboarding](https://support.nesi.org.nz/hc/en-gb/articles/5002335382543)
> for more information about it.

This article describes a technique to build
[Apptainer](https://apptainer.org/) containers using Mahuika Extension
nodes, via a Slurm job. You can also build
[Singularity](https://support.nesi.org.nz/hc/en-gb/articles/360001107916)
container using this technique.

# Build Environment Variables

To build containers, you need to ensure that Apptainer has enough
storage space to create intermediate files. It also requires a cache
folder to save images pulled from a different location (e.g. DockerHub).
By default both of these locations are set to `/tmp` which has limited
space, large builds may exceed this limitation causing the builder to
crash.

The environment variables `APPTAINER_TMPDIR` and `APPTAINER_CACHEDIR`
environment can be used to overwrite the default location of these
directories.

    export APPTAINER_CACHEDIR=/nesi/nobackup/PROJECTID/apptainer_cache
    export APPTAINER_TMPDIR=/nesi/nobackup/PROJECTID/apptainer_tmpdir
    mkdir -p $APPTAINER_CACHEDIR $APPTAINER_TMPDIR
    setfacl -b $APPTAINER_TMPDIR

where `PROJECTID` is your NeSI project ID.

# Building container via Slurm

The new Mahuika Extension nodes can be used to build Apptainer
containers using the [fakeroot
feature](https://apptainer.org/docs/user/main/fakeroot.html).

Assuming a container definition file called `my_container.def`, from a
Mahuika login node, you can build it using the `srun` command as
follows:

    module load Apptainer
    module unload XALT
    srun -p milan --time 0-00:30:00 --mem 4GB --cpus-per-task 2 apptainer build --fakeroot my_container.sif my_container.def

This command will start an interactive Slurm job for 30 minutes using 2
cores and 4 GB of memory to build the image. Make sure to set these
resources correctly, some containers can take hours to build and require
tens of GB of memory.

If you need more resources to build your container, please consider
submitting your job using a Slurm submission script, for example:

    #!/bin/bash -e
    #SBATCH --job-name=apptainer_build
    #SBATCH --partition=milan
    #SBATCH --time=0-00:30:00
    #SBATCH --mem=4GB
    #SBATCH --cpus-per-task=2

    module load Apptainer
    module unload XALT

    apptainer build --fakeroot my_container.sif my_container.def

More information about how to submit a Slurm job is available in the
[Submitting your first
job](https://support.nesi.org.nz/hc/en-gb/articles/360000684396) support
page.

# Known limitations

If your container uses RPM to install packages, i.e. is based on CentOS
or Rocky Linux, you need to disable the `APPTAINER_TMPDIR` environment
variable (use `unset APPTAINER_TMPDIR`) and request more memory for your
Slurm job. Otherwise, rpm will crash due to an incompatibility with the
`nobackup` filesystem.

> ### Other limitations
>
> This method, using fakeroot, is known to **not** work for types of
> Apptainer/Singularity containers.
>
> If you encounter an issue, please contact us at <support@nesi.org.nz>.
