---
created_at: '2020-04-30T01:28:34Z'
hidden: false
position: 7
tags: []
title: NVIDIA GPU Containers
vote_count: 2
vote_sum: 2
zendesk_article_id: 360001500156
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

NVIDIA provides access to GPU accelerated software through their NGC
container
registry: <https://www.nvidia.com/en-us/gpu-cloud/containers/>.

*NGC offers a comprehensive catalog of GPU-accelerated software for deep
learning, machine learning, and HPC. NGC containers deliver powerful and
easy-to-deploy software proven to deliver the fastest results. By taking
care of the plumbing, NGC enables users to focus on building lean
models, producing optimal solutions and gathering faster insights.*

Many of these containers are able to run under Singularity, which is
supported on the NeSI platform. NVIDIA also specifies the GPU
requirements for each container, i.e. whether it will run on our Pascal
(sm60) GPUs.

There are instructions for converting their Docker images to Singularity
images on the NVIDIA site but some small changes are required to these
instructions on NeSI. As an example, here we show the steps required for
running the NAMD image on NeSI, based on the NVIDIA instructions
here: <https://ngc.nvidia.com/catalog/containers/hpc:namd>.

1.  Download the APOA1 benchmark data:
    -   ``` sl
        wget -O - https://gitlab.com/NVHPC/ngc-examples/raw/master/namd/3.0/get_apoa1.sh | bash
        cd apoa1
        ```
2.  Load the Singularity module:
    -   ``` sl
        module load Singularity
        ```
3.  Build the Singularity image. This step differs from the NVIDIA
    instructions because instead of using "build" we "pull" the image
    directly, which does not require root access:
    -   Please do refer  "[Build Environment
        Variables](../../Scientific_Computing/Supported_Applications/Singularity.md#build_environment_variables)"
        prior to running the following `pull` command

    -   ``` sl
        singularity pull namd-3.0-alpha9-singlenode.sif docker://nvcr.io/hpc/namd:3.0-alpha9-singlenode
        ```
4.  Copy the following into a Slurm script named *run.sl*:
    -   ``` sl
        #!/bin/bash -e

        #SBATCH --job-name=namdgpu
        #SBATCH --time=00:10:00
        #SBATCH --ntasks=1
        #SBATCH --cpus-per-task=8
        #SBATCH --gpus-per-node P100:1
        #SBATCH --mem=1G

        module purge
        module load Singularity

        # name of the NAMD input file, tag, etc
        NAMD_INPUT="apoa1_nve_cuda.namd"
        NAMD_SIF="namd-3.0-alpha9-singlenode.sif"
        NAMD_EXE=namd3

        # singularity command with required arguments
        SINGULARITY="singularity exec --nv -B $(pwd):/host_pwd --pwd /host_pwd ${NAMD_SIF}"

        # run NAMD
        ${SINGULARITY} ${NAMD_EXE} +ppn ${SLURM_CPUS_PER_TASK} +idlepoll ${NAMD_INPUT}
        ```
5.  Submit the job:
    -   ``` sl
        sbatch run.sl
        ```
6.  View the standard output from the simulation in the Slurm .out file.

 We expect similar steps to work for other NGC containers.