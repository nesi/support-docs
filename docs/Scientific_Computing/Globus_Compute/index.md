# Globus Compute

!!! warning

    Our Globus Compute offering is in early-access mode and may change. Please let us know if you have any feedback or suggestions for improvements.

## Overview

[Globus Compute](https://www.globus.org/compute) provides a secure, scalable way to run Python functions remotely on compute resources.
On Mahuika, we host a Globus Compute multi-user endpoint, allowing users to submit and manage compute tasks through
Globus or compatible clients without needing to connect to the HPC via SSH or OnDemand.
Globus Compute has [comprehensive documentation](https://globus-compute.readthedocs.io/en/latest/quickstart.html) and here we will just
highlight the specifics of working with the Mahuika endpoints.

## Key concepts

`Endpoint`

:   A Globus Compute service running on the HPC system that executes user functions

`Single-user mode`

:   Each user runs and manages their own endpoint on a login node, which can execute their functions (this approach will not be discussed
    here but is documented on the Globus Compute site)

`Multi-user mode`

:   A centrally managed endpoint that all REANNZ HPC users can send tasks to; a user identity mapping process
    maps the user's Globus identity to their account on Mahuika

`Executors`

:   Manage job submissions to Slurm or execute jobs directly on login nodes

`Authentication`

:   Handled via Globus Auth - users must have a Globus account, which they can sign into with institutional or Globus IDs, and they
    must add a linked identity with the "NeSI Keycloak" to their Globus account

## Requirements

You must have a NeSI account, Globus account and have linked an identity from your Globus account to the NeSI Keycloak. This can be achieved by
navigating to the [NeSI HPC Storage](https://app.globus.org/file-manager?origin_id=763d50ee-e814-4080-878b-6a8be5cf7570) in the Globus
web app and ensuring you can see your NeSI files.

## Endpoints

| Name       | Endpoint ID                            | Purpose                                                      |
|------------|----------------------------------------|--------------------------------------------------------------|
| nesi-login | `63c0b682-43d1-4b97-bf23-6a676dfdd8bd` | Lighweight tasks that are suitable to be run on a login node, such as submitting Slurm jobs, checking job status, etc. |
| nesi-slurm | `abf152c8-ad9b-453f-bcc8-3424284344f3` | Resource intensive tasks; work sent to this endpoint will run in a Slurm job |

## `nesi-slurm` endpoint

This endpoint submits work in Slurm jobs. The following configuration options are available via [`user_endpoint_config`](https://globus-compute.readthedocs.io/en/v2.20.1/reference/executor.html#globus_compute_sdk.Executor.user_endpoint_config):

- `ACCOUNT_ID` (required): your NeSI project code
- `WALL_TIME` (optional, defaults to `00:05:00`): the wall time for the Slurm job that gets submitted (must be enough time for your function to complete)
- `MEM_PER_CPU` (optional, defaults to `2G`): amount of memory to be requested in the Slurm job
- `GPUS_PER_NODE` (optional, defaults to no GPU): request GPUs for the Slurm job

## Limitation and known problems

Limitations and known problems related to our current implementation are listed here.
If these are impacting your ability to use this service, please [let us know](mailto:support@nesi.org.nz).

- Currently limited to a single CPU
- You must use Python 3.11 (we are exploring options to execute functions in containers, which will enable use of different Python versions)
- You can only import Python packages that are available in the `Python/3.11.6-foss-2023a` environment module (containerisation will help here too)
- Globus Compute version 3.x

## Other notes

- Globus Compute uses token based auth after the initial setup (along with guest collections things can be fully automated)
- standard access and usage policies, quotas and accounting rules apply (active project, no compute intensive work on login endpoint, etc)
