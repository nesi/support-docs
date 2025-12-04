---
created_at: 2025-11-10
tags: 
  - workflow
---

!!! note "Alternatives"
    See [Nextflow](Nextflow.md) and [Cylc](Cylc.md) for other possible choices of workflow engine.

[//]:snakemake.md> (APPS PAGE BOILERPLATE START)
{% set app_name = "snakemake" %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]:snakemake.md> (APPS PAGE BOILERPLATE END)

## Job groups

Please use [Snakemake's job grouping](https://snakemake.readthedocs.io/en/stable/executing/grouping.html)
functionality to avoid Snakemake submitting many short jobs to the queue.
Each job submitted to Slurm should take at least 30 minutes.

## Running in an interactive Slurm session

Request an interactive Slurm session with the resources required to run all sub-jobs labeled as `localrules`:

```sl
srun --account nesi12345
```

Once the interactive session has launched, load the Snakemake module (see above) and you should be able to launch your workflow.

## Submitting a workflow as a Slurm job

As with an interactive session, the main batch job should request the resources needed to run any sub-jobs marked as `localrules`.

```sl
#!/bin/bash -e

#SBATCH --job-name        my job
#SBATCH --account         nesi12345
#SBATCH --time            01:00:00
#SBATCH --mem             2G

# load snakemake
module load snakemake/{{app.default}}

# launch snakemake workflow
snakemake -pr --keep-going -j $SLURM_CPUS_PER_TASK all
```

## Slurm plugin

Snakemake maintains a [plugin](https://snakemake.github.io/snakemake-plugin-catalog/plugins/executor/slurm.html) to assist with running Snakemake with Slurm as the executor.
This plugin supports the use of MPI jobs.

## Community resources

There are two main repositories for reusable Snakemake rules and workflows.
[Snakemake Wrappers](https://snakemake-wrappers.readthedocs.io/en/stable/)
provide version controlled rules to conduct common steps in workflows.
[Snakemake Workflows](https://snakemake.github.io/snakemake-workflow-catalog/index.html)
are entire Snakemake workflows for common pipelines.

!!! note "Other Resources"
    - [Snakemake Docs](https://snakemake.readthedocs.io/en/stable/)
    - [Snakemake Wrappers Repository](https://snakemake-wrappers.readthedocs.io/en/stable/)
    - [Snakemake Workflows Catalog](https://snakemake.github.io/snakemake-workflow-catalog/index.html)
