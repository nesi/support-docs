---
created_at: '2019-09-23T00:08:13Z'
hidden: false
position: 47
tags:
- no_toc
- no_lic
- no_desc
- no_ver
title: Relion
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001174055
zendesk_section_id: 360000040076
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/appHeader.md" %}
[//]: <> (APPS PAGE BOILERPLATE END)


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

Getting started with Relion is most easily done via its X11 GUI, which
is launched with the command "relion".  

``` sl
$ module load Relion
$ relion
```

After the desired options have been selected press the "Check command"
button to see the command it constructs in your terminal window. That
command line can then be pasted into a Slurm batch script.

If you leave "Number of MPI procs" at 1 then the Relion GUI will produce
a command like

``` sl
which relion_run_ctffind ...
```

That will work but can be simplified to

``` sl
relion_run_ctffind ...
```

If MPI is used then Relion will correctly recommend the MPI version of
the tool, eg:

``` sl
which relion_run_ctffind_mpi ...
```

but MPI programs need to be launched via srun, so that should be:

``` sl
srun relion_run_ctffind_mpi ...
```

We have made some effort to integrate the Relion GUI directly with Slurm
so that it can submit Slurm jobs directly, however this might not
entirely work yet. 

Some of the Relion tools benefit tremendously from using a GPU.

For licensing reasons we ask that you install the GPU
accelerated *MotionCorr2* yourself if you find Relion's own CPU-only
version of the same algorithm insufficient.

 

 