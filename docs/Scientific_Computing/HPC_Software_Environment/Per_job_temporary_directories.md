---
created_at: '2023-07-21T04:10:04Z'
hidden: false
position: 0
tags: []
title: Per job temporary directories
vote_count: 0
vote_sum: 0
zendesk_article_id: 7463891150863
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

Most programs which create temporary files will put those files in the
directory specified by the environment variable `TMPDIR` if that is set,
or `/tmp` otherwise. This is also true in Slurm, such that whenever a
job starts, a temporary directory is created for that job and `TMPDIR`
set. When the job ends our Slurm epilog ensures that the directory is
deleted.

By default, this job-specific temporary directory is placed in
`/dev/shm`, which is a “tmpfs” filesystem and so actually sits in
ordinary RAM.  As a consequence, your job’s memory request should
include enough to cover the size of any temporary files.

On the `milan` and `hgx` partitions, however, you have the option of
specifying `#SBATCH --gres=ssd` in your job script which will place
`TMPDIR` on a 1.5 TB NVMe SSD attached to the node rather than in RAM.
When `--gres=ssd` is set your job’s memory request *does not* need to
include enough to cover the size of any temporary files (as this is a
separate resource). These SSDs give the job a slower but very much
larger temporary directory. They are allocated exclusively to jobs, so
there can only be one such job per node at a time. This gives the job
all the available bandwidth of the SSD device but does limit the number
of such jobs.

Alternatively you can ignore the provided directory and set `TMPDIR`
yourself, typically to a location in `/nesi/nobackup`.  This will be the
slowest option with the largest capacity. Also if set to `nobackup` the
files will remain after the job finishes, so be weary of how much space
your jobs temporary files use. An example of how `TMPDIR` may be set
yourself is shown below,

`export TMPDIR=/nesi/nobackup/$SLURM_ACCOUNT/tmp/$SLURM_JOB_ID`

 

## Example of copying data into the per job temporary directories for use mid-job

The per job temporary directory can also be used to store data that
needs to be accessed as the job runs. For example you may wish to read
the standard database of Kraken2 (located in
`/opt/nesi/db/Kraken2/standard-2018-09`) from the `milan` SSDs instead
of `/opt`. To do this, request the NVMe SSD on `milan` as described
above. Then, after loading the Kraken2 module in your Slurm script, copy
the database onto the SSD,

``` sl
cp -r /opt/nesi/db/Kraken2/standard-2018-09/* $TMPDIR
```

To get Kraken2 to read the DB from the SSDs (and not from `/opt`),
change the `KRAKEN2_DEFAULT_DB` variable,

``` bash
export KRAKEN2_DEFAULT_DB=$TMPDIR
```

The variable `KRAKEN2_DEFAULT_DB` simply points to the database and is
found by `module show Kraken2`.