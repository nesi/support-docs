---
created_at: '2017-12-11T07:58:07Z'
hidden: false
position: 46
tags:
- mahuika
- biology
title: RAxML
vote_count: 1
vote_sum: 1
zendesk_article_id: 115001854444
zendesk_section_id: 360000040076
---


[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->

## Description

RAxML search algorithm for maximum likelihood based inference of
phylogenetic trees. The RAxML home page is at
<https://github.com/stamatak/standard-RAxML>.

 

## Licensing requirements

RAxML is licensed under the terms of the GNU General Public License
("the GPL"), version 2 or (at your option) any later version. A copy of
version 3 of the GPL as included with the RAxML software is available
[here](https://github.com/stamatak/standard-RAxML/blob/master/gpl-3.0.txt).

## Example scripts

### Example script for the Mahuika cluster

``` bash
#!/bin/bash -e

#SBATCH --job-name      RAxML_job
#SBATCH --time          01:00:00
#SBATCH --ntasks        1
#SBATCH --cpus-per-task 4
#SBATCH --mem           2G

module load RAxML/8.2.12-gimkl-2020a

srun raxmlHPC-PTHREADS-AVX -T $SLURM_CPUS_PER_TASK -m GTRCAT -s aln.fasta -n tree.out
```

## Documentation

`raxmlHPC-AVX -help` and the [RAxML
manual](https://github.com/stamatak/standard-RAxML/tree/master/manual).

## Parallel Versions

Each of our RAxML environment modules contains multiple RAxML
executables:

-   `raxmlHPC-AVX`
-   `raxmlHPC-SSE3`
-   `raxmlHPC-PTHREADS-AVX`
-   `raxmlHPC-PTHREADS-SSE3`
-   `raxmlHPC-MPI-AVX`
-   `raxmlHPC-MPI-SSE3`
-   `raxmlHPC-HYBRID-AVX`
-   `raxmlHPC-HYBRID-SSE3`

The combinations of Slurm settings and RAxML types which make sense are:

-   `raxmlHPC-AVX` or `raxmlHPC-SSE3` with one task on only one CPU.
-   `raxmlHPC-PTHREADS-AVX` or `raxmlHPC-PTHREADS-SSE3` with one task
    running on multiple CPUs.
-   `raxmlHPC-MPI-AVX` or `raxmlHPC-MPI-SSE3` with multiple tasks, each
    running on one CPU.
-   `raxmlHPC-HYBRID-AVX` or `raxmlHPC-HYBRID-SSE3` with multiple tasks,
    each of which runs on multiple CPUs.

MPI and HYBRID are only useful for bootstrapped trees.

For the multi-threaded cases (PTHREADS and HYBRID) you should tell RAxML
how many threads to use with the RAxML option `-T $SLURM_CPUS_PER_TASK`.

The "AVX" executables use the AVX SIMD instructions, while the "SSE3"
executables use the older and slower Intel SIMD (Single Instruction
Multiple Data) instructions, which can be anywhere from 10% to 30%
slower. There should be no need to use an SSE3 executable, unless you
find that an AVX executable doesn't work for any reason.