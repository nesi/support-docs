---
created_at: '2019-08-15T05:48:41Z'
hidden: false
tags:
- geo
- earthquake
title: OpenSees
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001111156
zendesk_section_id: 360000040076
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

There are three commands with which a OpenSees job can be launched.

- `OpenSees`: For running a job in serial (single CPU).
- `OpenSeesSP`: Intended for the single analysis of very large models.
- `OpenSeesMP`: For advanced parametric studies.

More info can be found about running OpenSees in parallel
[here](http://opensees.berkeley.edu/OpenSees/parallel/TNParallelProcessing.pdf).

=== "SerialJob"

Single *process* with a single *thread*.
Usually submitted as part of an array, as in the case of parameter
sweeps.

    ```sl
    #!/bin/bash -e
    
    #SBATCH --job-name      OpenSees-Serial
    #SBATCH --time          00:05:00          # Walltime</span></span>
    #SBATCH --cpus-per-task 1                 # Double if hyperthreading enabled.
    #SBATCH --mem           512MB             # total mem
    #SBATCH --hint          nomultithread     # Hyperthreading disabled
    
    module load OpenSees/{{app.machines.mahuika.versions | last}}
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
