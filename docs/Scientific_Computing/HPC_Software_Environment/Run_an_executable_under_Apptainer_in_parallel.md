---
created_at: '2024-01-15T13:20:00Z'
hidden: false
weight: 0
tags: []
title: Run an executable under Apptainer in parallel
vote_count: 0
vote_sum: 0
zendesk_article_id: 
zendesk_section_id:
---

This article describes how to run an [MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface) program that was compiled in an [Apptainer](https://apptainer.org/) environment in parallel, using the host MPI library.

While an Apptainer environment encapsulates the dependencies of an application, including MPI, it is often beneficial, to delegate MPI calls within the container to the host. The advantages are:

 * You can let SLURM manage the resources for you
 * You can leverage the MPI library on the host, which has been configured for maximum performance

 Note that for this to work, the MPI version inside the container must be compatible with that on the host. We'll illustrate this approach 
 with an example.

## Build the containerised executable

 This will need to take place on a Milan node. Hence, we need to submit a SLURM script that calls `apptainer build`:  
```sh
git clone git@github.com:pletzer/fidibench.git
cd fidibench
sbatch fidibench_apptainer_build_intel.sl
```
When the job finishes (after 1+ hour), you will have a `fidibench_intel.sif` file in your directory.


## Run the containerised executable


You can check that the executable was built successfully by running a quick test, using the internal MPI
```sh
apptainer exec fidibench_intel.sif mpiexec -n 4 /software/fidibench/bin/upwindMpiCxx -numCells 128 -numSteps 10
Number of procs: 4
...
 times min/max/avg: 3.33281/3.34092/3.3355 [seconds]
Check sum: 1
```

To submit the job via SLURM, write the following job script `fidibench_intel_apptainer.sl`:
```sh
#!/bin/bash -e
#SBATCH --ntasks=64
#SBATCH --partition=milan
#SBATCH --job-name=fidibench_app

module load Apptainer
module load intel        # load the Intel MPI
export I_MPI_FABRICS=ofi # turn off shm to allow the code to run on multiple nodes

# -B /opt/slurm/lib64/ binds this directory to the image when running on mahuika, 
# it is required  for the image's MPI to find the libpmi2.so library. This path
# may be different on a different host.
srun apptainer exec -B /opt/slurm/lib64/ fidibench_intel.sif /software/fidibench/bin/upwindMpiCxx -numCells 512 -numSteps 10
```
and submit it
```sh
sbatch fidibench_intel_apptainer.sl
```
The above job can run on multiple nodes. 

Note that the host MPI is loaded with the `intel` module. The MPI libraries on the host and in the 
container need to be compatible. At the time of writing, the host MPI is `2021.5` and the MPI in the container is `2021.8`.

