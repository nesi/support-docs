
[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

## Configurations

Below is an example `nextflow.config` file with some configuration settings that will help when running Nextflow via NeSI.

```json
// enable use of apptainer to run containers
apptainer {
    apptainer.pullTimeout       = '1h'
}

// Default settings for all profiles
process {
    stageInMode                 = 'symlink'
    cache                       = 'lenient'
}

// Specific profiles to use in different contexts
profiles {
    debug {
        cleanup                 = false
    }
    local {
        executor                = 'local'
    }
}

cleanup                         = true
```

## Running Nextflow in an interactive Slurm session

Running Nextflow in an interactive session can be especially helpful when setting up or debugging a pipeline. To do so, request an interactive session with appropriate resources for the pipeline:

```bash
srun --account nesi12345 --job-name "InteractiveJob" --cpus-per-task 8 --mem-per-cpu 1500 --time 24:00:00 --pty bash
```

Once your interactive session has launched, load the Nextflow module with `module load Nextflow/25.10.1` (or your required version) and proceed. Parallelization of Nextflow processes will occur within this job.

There are several environmental variables that can be helpful to avoid loading containers and plugins into your persistent project space:

```bash
export NXF_APPTAINER_CACHEDIR=/nesi/nobackup/nesi12345/apptainer_cache
export NXF_PLUGINS_DIR=/nesi/project/nesi12345/user/PROJECT_DIR/.nextflow/plugins
```

You can confirm that Nextflow is loaded and ready using the `nextflow run hello` command to test Nextflow's Hello World pipeline.

## Submitting a Nextflow workflow as a batch job

The following `sbatch` will submit a Nextflow workflow as a Slurm job. All of the Nextflow processes will run on the same compute node, so request enough resources to run the most intensive process in the workflow and enough time for the entire workflow to complete.

```sl
#!/bin/bash -e

#SBATCH --job-name        my job
#SBATCH --account         nesi12345
#SBATCH --time            01:00:00
#SBATCH --mem             2G

# load Nextflow and set environmental variables
module load Nextflow/25.10.0
export NXF_APPTAINER_CACHEDIR=/nesi/nobackup/nesi12345/apptainer_cache
export NXF_OFFLINE='true'
export NXF_PLUGINS_DIR=/nesi/project/nesi12345/user/PROJECT_DIR/.nextflow/plugins

# run nextflow
nextflow run NEXTFLOW_WORKFLOW \
    -profile local,apptainer \
    --outdir /nesi/project/nesi12345/user/PROJECT_DIR/NEXTFLOW_WORKFLOW/out \
    -w /nesi/nobackup/nesi12345/user/PROJECT_DIR/NEXTFLOW_WORKFLOW/work \
    -with-trace \
    -with-report \
    -with-dag
```

## Time/compute intensive processes

If any of your individual processes regularly take longer than 30 minutes, you can flag them to be submitted as additional Slurm jobs separate from the head job. To do this, give these processes a [label](https://www.nextflow.io/docs/latest/reference/process.html#label) such as `'slurm_array'` and add the following to your `nextflow.config` file:

```json
process {
        withLabel: slurm_array {
            executor            = 'slurm'
            queue               = 'genoa,milan'
            queueSize           = 10
            jobName             = { "$task.name - $task.hash" }
            slurm_array         = 100
        }
}
```

This will allow the main Nextflow Slurm job to submit this process to Slurm as separate tasks. `queueSize` limits the number of these additional Slurm jobs that can be queued simultaneously, while `array` tells Nextflow to group up to 100 processes with label and submit them as a job array. You can provide more specific labels and set up the configuration to request different resources for different processes.

!!! warning "Avoid many short jobs"
    This will put a major burden on the Slurm scheduler for no improvement in your computational speed. Do not use the Nextflow `slurm` executor for jobs which take less than 30 minutes to complete.

## Running with MPI

In addition to being able to use Nextflow to submit job arrays, you can also [run Nextflow across several nodes using MPI (Message-Passing Interface)](https://github.com/nextflow-io/nf-ignite?tab=readme-ov-file#slurm).

```sl
#!/bin/bash -e

#SBATCH --job-name=nextflow-mpi
#SBATCH --time=24:00:00
#SBATCH --ntasks=3
#SBATCH --cpus-per-task=12
#SBATCH --tasks-per-node=1
#SBATCH --mem=200GB
#SBATCH --account=nesi12345
#SBATCH --output="%x-%j.out"

# load nextflow
module load Nextflow/25.10.0
export NXF_CLUSTER_SEED=$(shuf -i 0-16777216 -n 1)

# run nextflow
srun nextflow run <workflow> \
    -with-mpi
```

## Improving efficiency

Nextflow provides tools that can assist you in making efficient use of the HPC resources. Running a pipeline with the CLI option `-with-report` will produce [a HTML execution report containing CPU and memory utilization information](https://www.nextflow.io/docs/latest/reports.html#execution-report) for each individual process as well as each process type. This information can be used to ensure processes are only getting the resources they need.

## Community pipelines - nf-core

[nf-core](https://nf-co.re/) is a global community collaborating to build open-source Nextflow components and pipelines. Many standard pipelines and tools have nf-core pipelines or modules which allow you to skip straight to running the pipeline.

!!! warning "Nextflow plugins"
    nf-core pipelines expect to use nf-plugins in their base configuration. If you want to use these plugins, you will need to manually download them and store them in a plugin cache directory that you can specify with the `NXF_PLUGINS_DIR` environmental variable (as in the example `.sl` above)

## Comparison of submission methods

The [nf-core rnaseq pipeline (v3.21.0)](https://nf-co.re/rnaseq/3.21.0) was run using the `test_full` dataset (v3.10) with three methods: a single Slurm job, a Slurm job capable of launching additional jobs, and a Slurm job split 4 ways by MPI.

| Type of run           | Number of cores / grid specification     | Run time (hrs:mins:secs)     | Total CPU     |
|-----------------------|------------------------------------------|------------------------------|--------------------------------|
| Single Slurm job | 4 cores                                 | 00:05:37                     | 16:42.462                            |
| Slurm job with additional | max\_nodes=1; cmds\_per\_node=4       | 00:06:13                     | 17:16.920                            |
| Slurm job with MPI | max\_nodes=3; cmds\_per\_node=4       | 00:09:41                     | 42:18.727                            |

### Local only

Requested 1 task, 200GB memory, 16 CPUs per task, 12 hours
Duration    : 11h 16m 47s
CPU hours   : 319.6

```bash
nn_seff <job-id>
Cluster: hpc
Job ID: 3034402
State: ['COMPLETED']
Cores: 16
Tasks: 1
Nodes: 1
Job Wall-time:   94.0%  11:17:04 of 12:00:00 time limit
CPU Efficiency:  76.6%  5-18:19:39 of 7-12:33:04 core-walltime
Mem Efficiency:  53.8%  107.69 GB of 200.00 GB
```

### MPI

Requested 3 tasks, 200GB memory, 12 CPUs per task, 24 hours.

### Labeled processes

Requested 1 task, 72GB memory, 12 CPUs per task, 12 hours.
Duration    : 5h 19m 46s
CPU hours   : 381.9 (1.4% failed)

Labeled processes (list below) could submit via slurm array requesting 12 CPUs, 72GB memory with a max queue size of 10.

- `TRIMMGALORE`
- `STAR_ALIGN_IGENOMES`
- `PICARD_MARKDUPLICATES`
- `QUALIMAP_RNASEQ`

```bash
nn_seff <job-id>
Cluster: hpc
Job ID: 3059728
State: ['OUT_OF_MEMORY']
Cores: 12
Tasks: 1
Nodes: 1
Job Wall-time:   44.4%  05:20:01 of 12:00:00 time limit
CPU Efficiency:  79.4%  2-02:47:46 of 2-16:00:12 core-walltime
Mem Efficiency:  61.9%  44.55 GB of 72.00 GB
```
