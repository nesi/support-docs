---
created_at: '2020-03-13T03:23:18Z'
tags: []
description: Supported applications page for MAKER
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

## Local Customisations

Since the MAKER control file *maker\_exe.ctl* is just an annoyance in an
environment module based system we have patched MAKER to make that
optional. If it is absent then the defaults will be used directly.

## Parallelism

MAKER can be used with MPI, though due to a complicated interaction
between Infiniband libraries and MAKER's use of forking it can't be used
across multiple nodes. So we recommend running large MAKER jobs with up
to 36 tasks on one node (ie: one full regular node), eg:

``` sl
#!/bin/bash -e

#SBATCH --account           nesi12345
#SBATCH --job-name          MAKER
#SBATCH --nodes             1
#SBATCH --ntasks-per-node   36
#SBATCH --mem-per-cpu       1500
#SBATCH --time              01:00:00

module load MAKER/2.31.9-gimkl-2020a
srun maker -q
```

## Resources

MAKER creates many files in its output, sometimes hundreds of thousands.
 There is a risk that you exhaust your quota of inodes, so:

- Don't run too many MAKER jobs simultaneously.
- Delete unneeded output files promptly after MAKER finishes.  You can
    use `nn_archive_files` or `tar` to archive them first.
