---
created_at: '2021-02-23T02:54:11Z'
hidden: false
position: 7
tags: []
title: VirSorter
vote_count: 1
template: app.html
vote_sum: -1
zendesk_article_id: 360003472036
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

We have customised VirSorter slightly for the cluster environment:

-   The number of jobs must be specified
-   We default to `--skip-deps-install`and `--use-conda-off`

We don't provide the VirSorter databases, so you will have to run
`virsorter setup` first

If you are doing many runs, it is good practice to use the
`--rm-tmpdir` option to delete all the temporary files which VirSorter
makes, and so reduce the risk of reaching your file quota.

VirSorter defaults its LOCAL\_SCRATCH configuration setting to "/tmp",
but we would prefer that Slurm jobs instead use the automatically
cleaned up per-job directory $TMPDIR. This is actually a Snakemake rule
configuration, so can be set at the end of the *virsorter* command line.

So an example which uses the SLURM\_CPUS\_PER\_TASK and TMPDIR values
provided to Slurm jobs would be:

``` sl
module load VirSorter/2.1-gimkl-2020a-Python-3.8.2
virsorter run \
    --seqfile test.fasta \
    --jobs ${SLURM_CPUS_PER_TASK:-2} \
    --rm-tmpdir \
    all \
    --config LOCAL_SCRATCH=${TMPDIR:-/tmp}
```

 