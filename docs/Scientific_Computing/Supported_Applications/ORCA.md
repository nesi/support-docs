---
created_at: '2015-11-09T21:20:24Z'
hidden: false
position: 41
tags:
- mahuika
- chemistry
title: ORCA
vote_count: 3
vote_sum: 3
zendesk_article_id: 213718027
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->

ORCA is a flexible, efficient and easy-to-use general purpose tool for
quantum chemistry with specific emphasis on spectroscopic properties of
open-shell molecules. It features a wide variety of standard quantum
chemical methods ranging from semiempirical methods to DFT to single-
and multireference correlated *ab initio* methods. It can also treat
environmental and relativistic effects.

The ORCA home page is
at [https://orcaforum.kofo.mpg.de](https://orcaforum.kofo.mpg.de)

## Licensing requirements

ORCA is released as precompiled binaries at no cost, pursuant to a
closed-source licence.  Users are advised that the terms of [the ORCA
licence](https://orcaforum.kofo.mpg.de/app.php/dlext/?view=detail&df_id=41)
allow its use in the course of academic research only, and that each
research group is expected to register with the ORCA developers. If you
have any questions regarding your eligibility to access ORCA or any
particular version of it, please contact [our support
desk](mailto:support@nesi.org.nz).

## Example script

``` bash
#!/bin/bash -e
#SBATCH --job-name      ORCA_job
#SBATCH --time          01:00:00
#SBATCH --ntasks        16  # ORCA can be inefficient with ntasks > 16
#SBATCH --mem-per-cpu   1G

module load ORCA/5.0.4-OpenMPI-4.1.5

# ORCA under MPI requires that it be called via its full absolute path
orca_exe=$(which orca)

# Don't use "srun" as ORCA does that itself when launching its MPI process.
${orca_exe} MyInput.inp
```

## Further notes

### Requesting a parallel run

ORCA requires a parallel run to be requested in its input as well as
from the batch scheduler. To request a parallel run, you need to add a
line to the input file like the following:

``` sl
%pal nprocs <np> end
```

where `<np>` represents the total number of processors (cores) you have
requested from the scheduler.

### Checkpointing and restarting

ORCA provides for saving of checkpoint data, especially molecular
orbital information, in a file with extension ".gbw" (short for
Geometry-Basis-Wavefunction). Given an input file name of "foo.inp" or
some equivalent, the GBW file will be named "foo.gbw". The GBW file,
like temporary and other output files, will be written in the same
directory from which the ORCA executable is invoked.

To restart from an existing GBW file, you should do the following:

1.  Ensure that the GBW file you want to start from is renamed so that
    it does not have the same base name as your intended input file.
    Otherwise, it will be overwritten and destroyed as soon as ORCA
    starts running.
2.  In your input file, specify the following lines, replacing
    "checkpoint.gbw" with the name of the GBW file you intend to read
    from:

``` sl
! moread
% moinp "checkpoint.gbw"
```

1.  Run the calculation.

For more information about restarting from an older GBW file, including
how to restart from GBW files produced using earlier versions of ORCA,
please consult the ORCA manual.