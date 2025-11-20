---
created_at: 2025-11-10
title: snakemake
tags: []
---

[//]:snakemake.md> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]:snakemake.md> (APPS PAGE BOILERPLATE END)

## Snakemake job groups

Please use [Snakemake's job grouping](https://snakemake.readthedocs.io/en/stable/executing/grouping.html) functionality to avoid Snakemake submitting many short jobs to the queue. Each job submitted to Slurm should take at least 30 minutes.

## Running Snakemake in an interactive Slurm session

Request an interactive Slurm session with the resources required to run all subjobs labeled as `localrules`:

```
srun --account nesi12345
```

Once the interactive session has launched, load the Snakemake module (see above) and you should be able to launch your workflow.

## Submitting a Snakemake workflow as a Slurm job

As with an interactive session, the main batch job should request the resources needed to run any subjobs marked as `localrules`.

```sl
#!/bin/bash -e

#SBATCH --job-name        my job
#SBATCH --account         nesi12345
#SBATCH --time            01:00:00
#SBATCH --mem             2G

# load snakemake
module load snakemake/7.32.3-gimkl-2022a-Python-3.11.3

# launch snakemake workflow
snakemake -pr --keep-going -j $SLURM_CPUS_PER_TASK all
```

## Snakemake Slurm plugin

Snakemake maintains a [plugin](https://snakemake.github.io/snakemake-plugin-catalog/plugins/executor/slurm.html) to assist with running Snakemake with Slurm as the executor.
This plugin supports the use of MPI jobs.

## Snakemake community resources

There are two main repositories for reuseable Snakemake rules and workflows.
[Snakemake Wrappers](https://snakemake-wrappers.readthedocs.io/en/stable/) provide version controlled rules to conduct common steps in workflows.
[Snakemake Workflows](https://snakemake.github.io/snakemake-workflow-catalog/index.html) are entire Snakemake workflows for common pipelines.


## External references
- [Snakemake Docs](https://snakemake.readthedocs.io/en/stable/)
- [Snakemake Wrappers Repository](https://snakemake-wrappers.readthedocs.io/en/stable/)
- [Snakemake Workflows Catalog](https://snakemake.github.io/snakemake-workflow-catalog/index.html)
