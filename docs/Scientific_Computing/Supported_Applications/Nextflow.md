
[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

[Nextflow](https://www.nextflow.io/) is a workflow system for creating scalable, portable, and reproducible workflows. It uses a dataflow programming model that simplifies writing parallel and distributed pipelines by allowing you to focus on data flow and computation. Nextflow can deploy workflows on a variety of execution platforms, including your local machine, HPC schedulers, and cloud. Additionally, Nextflow supports a range of compute environments, software container runtimes, and package managers, allowing workflows to be executed in reproducible and isolated environments.

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
    slurm {
        executor                = 'slurm'
        executor.queue          = 'genoa,milan'
        executor.queueSize      = 100
    }
}

cleanup                         = true
```

## Community pipelines - nf-core

[nf-core](https://nf-co.re/) is a global community collaborating to build open-source Nextflow components and pipelines. Many standard pipelines and tools have nf-core pipelines or modules which allow you to skip straight to running the pipeline.
