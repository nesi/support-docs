---
created_at: '2024-02-15T03:27:38Z'
hidden: false
position: 0
tags: []
title: FlexiBLAS
vote_count: 0
vote_sum: 0
zendesk_article_id: 9027967596303
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

[FlexiBLAS](https://www.mpi-magdeburg.mpg.de/projects/flexiblas) is a
lightweight wrapper around the BLAS and LAPACK APIs.  It allows you to
choose an implementation at run-time.  Our *foss/2023a* toolchain
specifies FlexiBLAS as its BLAS/LAPACK library, with OpenBLAS as the
default real implementation.  So for any software built with that
toolchain, you can substitute OpenBLAS with BLIS or with Intel's MKL by
setting the environment variable FLEXIBLAS:

``` sl
module load Python/3.11.3-foss-2023a
# using OpenBLAS

# switch to Intel MKL
module load imkl/2022.0.2
export FLEXIBLAS=IMKL

# switch to BLIS
module load BLIS/0.9.0-GCC-12.3.0
export FLEXIBLAS=BLIS

# explicitly switch back to OpenBLAS
export FLEXIBLAS=OPENBLAS

# switch to our default (currently OpenBLAS)
unset FLEXIBLAS
```

For workloads which spend a considerable amount of CPU time doing linear
algebra via BLAS or LAPACK, it may be worth benchmarking these options
to see which performs the best.  Their relative performance can differ
between different CPU types.