---
created_at: 2026-06-24
description: Summary of available workflow managers
tags:
    - software
---

!!! tip "Webinar"
    Check out the recording of our webinar entitled [Introduction to Containers and Workflows](https://www.youtube.com/watch?v=Dn0xIdPfPQ4).

Workflow managers help make research more reproducible and coordinate tasks that are interdependent.
These tools can range from the simple, running the same process on a large number of inputs, to the complex, managing a series of analyses with filtering logic.

## What are workflow managers?

Workflow managers automate multi-step analysis pipelines so that you don't need to run each step or script independently.
They are commonly used in modeling and bioinformatics workflows, but can be applicable in a large range of settings.
Rather than manually checking the results of one task before starting the next, workflow managers can confirm that the first task completed successfully before starting the second task.
Instead of submitting one Slurm job, or job array, for the first task and checking to see when it is finished before starting the second task, a workflow manager allows you to start one task which will monitor the progress of the subtasks and start them when appropriate.

## What are the options?

On Mahuika we have several workflow managers installed:

- [Cylc](./Available_Applications/Cylc.md)
    - Cylc (pronounced silk) is a general purpose workflow engine that also manages cycling systems very efficiently. It is used in production weather, climate, and environmental forecasting on HPC, but is not specialized to those domains.
- [Nextflow](./Available_Applications/Nextflow.md)
    - Nextflow is a workflow system for creating scalable, portable, and reproducible workflows. It is based on the dataflow programming model, which greatly simplifies the writing of parallel and distributed pipelines, allowing you to focus on the flow of data and computation. Nextflow can deploy workflows on a variety of execution platforms, including your local machine, HPC schedulers, AWS Batch, Azure Batch, Google Cloud Batch, and Kubernetes. Additionally, it supports many ways to manage your software dependencies, including Conda, Spack, Docker, Podman, Singularity, and more.
- [Snakemake](./Available_Applications/snakemake.md)
    - The Snakemake workflow management system is a tool to create reproducible and scalable data analyses. Snakemake is highly popular, with on average more than 7 new citations per week in 2021, and almost 400k downloads. Workflows are described via a human readable, Python based language. They can be seamlessly scaled to server, cluster, grid and cloud environments without the need to modify the workflow definition. Finally, Snakemake workflows can entail a description of required software, which will be automatically deployed to any execution environment.

There are reasons for each workflow manager, but a first step for identifying the tool you want to use is to see if anyone in your research group or field is already using a tool and has a workflow you can adapt for your needs.

| Workflow manager                                   | Workflow language | Script language | Slurm integration | Use GPU | Dynamic resource allocation | Failed job retry |
| -------------------------------------------------- | ----------------- | --------------- | ----------------- | -- | -- | -- |
| [Cylc](./Available_Applications/Cylc.md)           | Python            | bash            | Built in           |  |  |  |
| [Nextflow](./Available_Applications/Nextflow.md)   | Groovy DSL        | Any             | Built in          | Yes | Yes | Yes |
| [snakemake](./Available_Applications/snakemake.md) | Python            | Any             | Plugin installed             |  |  |  |

As always, feel free to {% include "partials/support_request.html" %} with any questions or for help implementing a workflow manager in your research.
