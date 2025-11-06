
[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

## Running Nextflow in an interactive Slurm session

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
    


## Improving efficiency

Nextflow provides tools that can assist you in making efficient use of the HPC resources. Running a pipeline with the CLI option `-with-report` will produce [a HTML execution report containing CPU and memory utilization information](https://www.nextflow.io/docs/latest/reports.html#execution-report) for each individual process as well as each process type. This information can be used to ensure processes are only getting the resources they need.

## Community pipelines - nf-core

[nf-core](https://nf-co.re/) is a global community collaborating to build open-source Nextflow components and pipelines. Many standard pipelines and tools have nf-core pipelines or modules which allow you to skip straight to running the pipeline.

!!! warning "Nextflow plugins"
    nf-core pipelines expect to use nf-plugins in their base configuration. If you want to use these plugins, you will need to manually download them and store them in a plugin cache directory that you can specify with the `NXF_PLUGINS_DIR` environmental variable (as in the example `.sl` above)
    