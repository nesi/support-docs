---
created_at: '2015-09-02T20:55:32Z'
hidden: true
position: 25
tags:
- mahuika
- tier1
- biology
title: BEAST
vote_count: 0
vote_sum: 0
zendesk_article_id: 208367078
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->

The BEAST home page is at <http://beast2.org>.

# Example scripts

## Example script for the Pan cluster

``` bash
#!/bin/bash -e

#SBATCH --job-name      MyBEASTJob
#SBATCH --account       nesi99999
#SBATCH --time          01:00:00
#SBATCH --cpus-per-task 16
#SBATCH --mem-per-cpu   4G
#SBATCH --output        MyBEASTJob.%j.out   # Include the job ID in the names
#SBATCH --error         MyBEASTJob.%j.err   # of the output and error files

module load BEAST/2.2.1

# Here Java is told it can use ( cpus-per-task * mem-per-cpu - 2GB ) = 62GB
export _JAVA_OPTS="-Xms62g -Xmx62g" 

srun beast -beagle -beagle_SSE -threads $SLURM_CPUS_PER_TASK input.xml
```

## Memory

Please note the Java options in the above script. BEAST is a Java
program, and Java will not automatically use all the memory which Slurm
has allocated for it unless told to do so.

## Long BEAST runs

If your Slurm job ends too early you can continue its calculation in a
second job by way of the `-resume` option of BEAST2. For very long BEAST
runs it may even make sense to deliberately break it into 1-week
segments to get around our limits on maximum job duration.
