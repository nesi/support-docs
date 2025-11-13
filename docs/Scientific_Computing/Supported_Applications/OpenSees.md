---
created_at: '2019-08-15T05:48:41Z'
tags:
- geo
- earthquake
description: Supported applications page for OpenSees
---

[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

There are three commands with which a OpenSees job can be launched.

- `OpenSees`: For running a job in serial (single CPU).
- `OpenSeesSP`: Intended for the single analysis of large models.
- `OpenSeesMP`: For advanced parametric studies.

[See the OpenSees documentation for more details on running in parallel](http://opensees.berkeley.edu/OpenSees/parallel/TNParallelProcessing.pdf).

=== "SerialJob"

Single *process* with a single *thread*.
Usually submitted as part of an array, as in the case of parameter
sweeps.

    ```sl
    #!/bin/bash -e
    
    #SBATCH --job-name      OpenSees-Serial
    #SBATCH --account       nesi12345
    #SBATCH --time          00:05:00          # Walltime</span></span>
    #SBATCH --cpus-per-task 1                 # Double if hyperthreading enabled.
    #SBATCH --mem           512MB             # total mem
    #SBATCH --hint          nomultithread     # Hyperthreading disabled
    
    module load OpenSees/{{app.default}}
    OpenSees "frame.tcl"

## Input from Shell

Information can be passed from the bash shell to a Tcl script by use of
environment variables.

Set in Slurm script:

```bash
export MY_VARIABLE="Hello World!"
```

Retrieved in Tcl script:

```tcl
puts $::env(MY_VARIABLE)
```
