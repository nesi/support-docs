---
created_at: '2023-07-21T04:10:04Z'
tags: 
  - storage
  - tmpdir
  - tmp
  - temp
  - localscratch
description: How temporary files are utilised on the REANNZ cluster.
---

Temporary files are those which get created during a job and are not needed after the
job has completed. Keeping such files (particularly small ones) in a fast local
filesystem can improve performance and guarantee their deletion at the end of the job.

For information about the other Mahuika filesystems,
see [Filesystems and Quotas](../Storage/Filesystems_and_Quotas.md)

## TMPDIR

Most programs which create temporary files will put those files in the
directory specified by the environment variable `$TMPDIR` if that is set,
or `/tmp` otherwise.

Where `$TMPDIR` is located can be modified to suit your requirements.

!!! warning
    Some programs ignore `$TMPDIR`,
    and may need to be told via their command lines or their own custom environment variables.

### In memory

Each Slurm job gets is own private `/tmp` directory which is removed when the job ends.

By default Slurm will set `$TMPDIR` to point here.

This job-specific directory is in a “tmpfs” filesystem and so actually sits in
ordinary RAM. As a consequence, your job’s memory request should include enough to
cover the size of any files it puts there.

### On SSD

If you need more space for temporary files then you have the option
of getting a slower but very much larger temporary directory by
specifying `#SBATCH --gres=ssd` in your job script, which
will create a directory for the job on a 1.5 TB NVMe SSD(Solid State Drive) attached to the
compute node and set the environment variables `$JOB_SCRATCH_DIR` and `$TMPDIR` to its path.

As that is not in RAM your job’s memory request *does not* need to cover
the size of the files your job puts there. Each node's SSD is allocated
exclusively to one job at a time, so there can only be one such job per node.
This gives the job all the available bandwidth of the SSD device
but does limit the number of such jobs.

### In WEKA scratch

You can ignore the provided `/tmp` directory and use a location
within `/nesi/nobackup`. This will generally be the slowest option,
particularly if there are thousands of small files involved. Also the
files will remain after the job finishes and will need to be manually deleted,
so be weary of how much space they take and how many of them there are.

For example;

``` sh
export TMPDIR=/nesi/nobackup/$SLURM_ACCOUNT/tmp/$SLURM_JOB_ID
```

## Scope and multi-node jobs

The `/tmp` and `$JOB_SCRATCH_DIR` directories are local to each node, shared by the
tasks of a the job on that node, but not not shared across the nodes of a multi-node job.

## Example of copying input data into $TMPDIR

A per job temporary directory can also be used to store data that
needs to be accessed repeatedly as the job runs. For example you may wish to read
the standard database of Kraken2 from the local SSDs instead
of the WEKA filesystem mounted at `/opt/nesi`. To do this, request the NVMe SSD as described
above. Then, after loading the Kraken2 module in your Slurm script, copy
the database onto the SSD and tell Kraken2 to use that copy,

``` sh
module load Kraken2
cp -pr $KRAKEN2_DEFAULT_DB/* $TMPDIR
export KRAKEN2_DEFAULT_DB=$TMPDIR
```

## On the login node

`$TMPDIR` will not automatically be set to anything if you are running work on the login node.
If your workflow explicitly requires a temporary directory to run you could include some logic to make sure.

```sh
TMPDIR=${TMPDIR:="/tmp"}
```
