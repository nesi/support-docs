
[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

See [Snakemake](https://snakemake-on-nesi.sschmeier.com/) and [Cylc](https://cylc.github.io/) for other possible choices.

## Methods for running Nextflow with REANNZ

There are three suggested methods for running Nextflow pipelines on our system:

1. [Running Nextflow in an interactive Slurm session](#running-nextflow-in-an-interactive-slurm-session)
    - This method is best for setting up or debugging pipeline executions as the pipeline will end as soon as the interactive session ends.
2. [Submitting a Nextflow workflow as a batch job](#submitting-a-nextflow-workflow-as-a-batch-job)
    - This method will run all sub-processes in the same Slurm job. This is best if your workflow would spawn a large number of short jobs.
3. [Submitting a Nextflow workflow via a head job](#submitting-a-nextflow-workflow-via-a-head-job)
    - This method requires submitting a low resource but long running batch job which will control the Nextflow workflow and all processes will be submitted by Nextflow as separate jobs to Slurm. This method is useful for workflows with lots of variation in their computational needs and which comprise mostly long running processes.

The differences in these methods is largely controlled by configuration/profile settings. The examples below use the REANNZ configuration file provided in the [Configurations section](#configurations).

### Running Nextflow in an interactive Slurm session

Running Nextflow in an interactive session can be especially helpful when setting up or debugging a pipeline. To do so, request an interactive session with appropriate resources for the pipeline:

```bash
srun --account nesi12345 --job-name "InteractiveJob" --cpus-per-task 16 --mem-per-cpu 24000 --time 24:00:00 --pty bash
```

Once your interactive session has launched, load the Nextflow module with `module load Nextflow/25.10.1` (or your required version) and proceed. Parallelization of Nextflow processes will occur within this job.

There are several environmental variables that can be helpful to avoid loading containers and plugins into your persistent project space:

```bash
export NXF_APPTAINER_CACHEDIR=/nesi/nobackup/nesi12345/apptainer_cache
export NXF_PLUGINS_DIR=/nesi/project/nesi12345/.nextflow/plugins
```

You can confirm that Nextflow is loaded and ready using the `nextflow run hello` command to test Nextflow's Hello World pipeline.

### Submitting a Nextflow workflow as a batch job

The following `sbatch` will submit a Nextflow workflow as a Slurm job. All of the Nextflow processes will run on the same compute node, so request enough resources to run the most intensive process in the workflow and enough time for the entire workflow to complete.

```sl
#!/bin/bash -e

#SBATCH --job-name        nextflow-workflow
#SBATCH --account         nesi12345
#SBATCH --time            12:00:00
#SBATCH --mem             24G
#SBATCH --cpus-per-task   16

# load Nextflow and set environmental variables
module load Nextflow/25.10.0
export NXF_APPTAINER_CACHEDIR=/nesi/nobackup/nesi12345/apptainer_cache
export NXF_OFFLINE='true'
export NXF_PLUGINS_DIR=/nesi/project/nesi12345/.nextflow/plugins

# run nextflow
nextflow run NEXTFLOW_WORKFLOW \
    -profile local,apptainer \
    --outdir /nesi/project/nesi12345/NEXTFLOW_WORKFLOW/out \
    -w /nesi/nobackup/nesi12345/NEXTFLOW_WORKFLOW/work
```

### Submitting a Nextflow workflow via a head job

The following `sbatch` script will request the resources to run a Nextflow head job which will then submit processes to Slurm as separate tasks. Beyond the resources requested for this job, the only difference between this script and the previous one is the change in the `-profile` tag from `local,apptainer` to `slurm,apptainer`.

```sl
#!/bin/bash -e

#SBATCH --job-name        nextflow-head
#SBATCH --account         nesi12345
#SBATCH --time            12:00:00
#SBATCH --mem             4G
#SBATCH --cpus-per-task   4


# load Nextflow and set environmental variables
module load Nextflow/25.10.0
export NXF_APPTAINER_CACHEDIR=/nesi/nobackup/nesi12345/apptainer_cache
export NXF_OFFLINE='true'
export NXF_PLUGINS_DIR=/nesi/project/nesi12345/.nextflow/plugins

# run nextflow
nextflow run NEXTFLOW_WORKFLOW \
    -profile slurm,apptainer \
    --outdir /nesi/project/nesi12345/NEXTFLOW_WORKFLOW/out \
    -w /nesi/nobackup/nesi12345/NEXTFLOW_WORKFLOW/work
```

!!! warning "Avoid many short jobs"
    This will put a major burden on the Slurm scheduler for no improvement in your computational speed. Do not use the Nextflow `slurm` executor for jobs which take less than 30 minutes to complete.

<!-- ## Running with MPI

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
``` -->

## Configurations

For reproducibility and clarity, we recommend using the ability to [stack Nextflow configurations](https://nf-co.re/docs/usage/getting_started/configuration#different-config-locations) and use three distinct `.config` files.

1. Pipeline-level config: This configuration is system and data agnostic, but should be untouched for any runs of the given pipeline.
2. System-level config: This configuration is pipeline agnostic but provides settings for running on a given computer system. We provide a REANNZ-specific config below.
3. Run-level config: This configuration is where changes are made to fine-tune for the specifics of a given run/system/pipeline combination. For clarity, we will refer to this file as `custom.config`

Below is an example `nextflow.config` file with some configuration settings that will help when running Nextflow via REANNZ systems.

```json
// REANNZ nf-core configuration profile
// Global default params, used in configs
params {
    config_profile_description = 'REANNZ HPC profile provided by nf-core/configs'
    config_profile_contact     = 'Jennifer Reeve (@jen-reeve)'
    config_profile_url         = 'https://docs.nesi.org.nz'
    max_cpus                   = 64
    max_memory                 = 1024.GB
}

// Default settings for all profiles
process {
    stageInMode = 'symlink'
    cache       = 'lenient'
}

// Specific profiles to use in different contexts
profiles {
    debug {
        // This profile will not remove intermediate files from the work directory
        cleanup = false
    }
    local {
        // This profile should be used workflows submitted from interactive Slurm sessions or when a workflow will generate many short (<30 minutes) tasks
        process.executor = 'local'
    }
    slurm {
        // This profile should be used for workflows which need to submit processes as Slurm jobs
        process.executor = 'slurm'
        process.array    = 100
    }
}

// Settings for the Slurm executor
executor {
    '$slurm' {
        queueSize         = 500
        submitRateLimit   = '20 min'
        // 20 per minute
        pollInterval      = '30 sec'
        queueStatInterval = '30 sec'
        jobName           = { "${task.process}-${task.hash}" }
        queue             = 'genoa,milan'
    }
}

// Apptainer specific settings
apptainer {
    apptainer.pullTimeout = '2h'
}

cleanup = true
```

### Run-level configuration options

As mentioned above, the pipeline and system specific configuration files should generally be left untouched. This means any adjustments for your workflow will occur in final run level configuration file.

There are many options you may wish to use to fine-tune your Nextflow runs. For more information, we recommend starting with the [overview on configuration files](https://www.nextflow.io/docs/latest/config.html) and if needed digging into the [configuration reference](https://www.nextflow.io/docs/latest/reference/config.html) available in the Nextflow documentation.

One option of particular note is the ability to flag certain processes to use a different executor than the main workflow. This can allow you to either flag certain processes to be submitted as separate jobs despite generally [running a workflow in a single Slurm job](#submitting-a-nextflow-workflow-as-a-batch-job) or to flag processes to run in the [head job while most processes are submitted as separate jobs](#submitting-a-nextflow-workflow-via-a-head-job).

For example, if you submit a workflow as a batch job, but know that several of your individual processes regularly take longer than 30 minutes, you can flag them to be submitted as additional Slurm jobs separate from the head job. To do this, give these processes a [label](https://www.nextflow.io/docs/latest/reference/process.html#label) such as `'slurm_array'` and add the following to your `custom.config` file:

```json
process {
        withLabel: slurm_array {
            executor            = 'slurm'
        }
}
```

You could additionally provide [details about the specific resources required](https://nf-co.re/docs/usage/getting_started/configuration#tuning-workflow-resources), although this may already be provided by the pipeline level configuration via additional process labels or explicit definitions [using `withName`](https://www.nextflow.io/docs/latest/config.html#process-selectors). Please note that there is an [additional ranking of priority for process configuration settings](https://www.nextflow.io/docs/latest/config.html#selector-priority) beyond that of the layered configuration files.

## Monitoring and reporting

Nextflow provides tools that can assist you in making efficient use of the HPC resources. We strongly recommend testing your pipeline with a small subset of data to determine optimal settings before running full datasets.

The most human-readable, but least configurable option is the execution report which is [an HTML execution report containing CPU and memory utilization information](https://www.nextflow.io/docs/latest/reports.html#execution-report) for each individual process as well as each process type. This information can be used to ensure processes are only getting the resources they need.

For a more configurable option, [the trace file](https://www.nextflow.io/docs/latest/reports.html#trace-file) provides many potential fields of interest which can be requested. A full list of fields is available at the previous documentation link, but several of note for optimization and debugging:

- `native_id` will provide the job ID for any jobs submitted to Slurm
- `duration` will show the time from *submission* of the process to completion of the process
- `realtime` will show the time from the *start* of the process to completion of the process (job run time)
- `%cpu` will show the percentage of CPU used by the process
- `%mem` will sow the percentage of memory used by the process
- `peak_rss` will show the peak of real memory used
- `workdir` will provide the path to the working directory of the process

Adding the following to your `custom.config` will produce both an execution report and trace file for each run, named with the timestamp, and put these files in a separate `runInfo` directory rather than within the Nextflow output directory.

```json
// Name the reports according to when they were run
params.timestamp = new java.util.Date().format('yyyy-MM-dd_HH-mm-ss')

// Generate report-timestamp.html execution report 
report {
    enabled = true
    overwrite = false
    file = "./runInfo/report-${params.timestamp}.html"
}

// Generate trace-timestamp.txt trace file
trace {
    enabled = true 
    overwrite = false 
    file = "./runInfo/trace-${params.timestamp}.txt"
    fields = 'name,status,exit,duration,realtime,cpus,%cpu,memory,%mem,rss,peak_rss,workdir,native_id'
}
```

## Community pipelines - nf-core

[nf-core](https://nf-co.re/) is a global community collaborating to build open-source Nextflow components and pipelines. Many standard pipelines and tools have nf-core pipelines or modules which allow you to skip straight to running the pipeline.

!!! warning "Nextflow plugins"
    nf-core pipelines expect to use nf-plugins in their base configuration. If you want to use these plugins, you will need to manually download them and store them in a plugin cache directory that you can specify with the `NXF_PLUGINS_DIR` environmental variable (as in the example `.sl` above)

## Comparison of submission methods

The [nf-core rnaseq pipeline (v3.21.0)](https://nf-co.re/rnaseq/3.21.0) was run using the `test_full` dataset (v3.10) with three methods: a batch job, a head job, and a batch job with specific processes flagged for submission to Slurm.

| Type of run           | Number of cores / grid specification     | Run time (hrs:mins:secs)     | Total CPU     |
|-----------------------|------------------------------------------|------------------------------|--------------------------------|
| [Batch job](#batch-job) |                                  |                      |                             |
| [Head job](#head-job) |        |                      |                             |
| [Labeled processes](#labeled-processes) |        |                      |                          |

### Batch job

Using the [batch job method](#submitting-a-nextflow-workflow-as-a-batch-job).

Requested 1 task, 200GB memory, 16 CPUs per task, 12 hours

Duration    : 11h 16m 47s

CPU hours   : 319.6

```bash
> nn_seff <job-id>
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

### Head job

Using the [head job method](#submitting-a-nextflow-workflow-via-a-head-job)


### Labeled processes

Using the [batch job method](#submitting-a-nextflow-workflow-as-a-batch-job) with specific processes flagged for submission to the Slurm queue as described in the [run-level configuration options section](#run-level-configuration-options)

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
<!-- 
### MPI

```bash
#SBATCH --time=48:00:00
#SBATCH --ntasks=3
#SBATCH --cpus-per-task=12
#SBATCH --tasks-per-node=1
#SBATCH --mem=200GB
```


Duration    : 1d 3h 24m 12s
CPU hours   : 323.3

```bash
Cluster: hpc
Job ID: 3144335
State: ['COMPLETED']
Cores: 36
Tasks: 3
Nodes: 3
Job Wall-time:   57.1%  1-03:24:26 of 2-00:00:00 time limit
CPU Efficiency:  34.8%  14-07:51:02 of 41-02:39:36 core-walltime
Mem Efficiency:  28.4%  170.59 GB (55.79 GB to 58.00 GB / task) of 600.00 GB (200.00 GB/task)
``` -->
