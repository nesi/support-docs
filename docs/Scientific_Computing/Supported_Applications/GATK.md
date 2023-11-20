---
created_at: '2023-02-21T21:21:50Z'
hidden: false
position: 1
tags: []
title: GATK
vote_count: 0
vote_sum: 0
zendesk_article_id: 6443618773519
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

The Genome Analysis Toolkit (GATK), developed at the [Broad
Institute](http://www.broadinstitute.org/), provides a wide variety of
tools focusing primarily on variant discovery and genotyping. It is
regarded as the industry standard for identifying SNPS and indels in
germline DNA and RNAseq data.

General documentation for running GATK can be found at their website
[here.](https://gatk.broadinstitute.org/hc/en-us)



## Running GATK

GATK uses requires the Java Runtime Environment. The appropriate version
of Java is already included as part of the GATK module, you will not
need to load a Java module separately.



**Note**  :

-   `--time` and `--mem` defined in the following example are just place
holders.
-   Please load the GATK version of your choice

``` sl
#!/bin/bash -e
#SBATCH --job-name=MarkDuplicates
#SBATCH --output=%x_%j.out     # log file
#SBATCH --error=%x_%j.err      # error log file
#SBATCH --account=nesi12345    # your NeSI project code
#SBATCH --time=2:00:00         # maximum run time hh:mm:ss
#SBATCH --mem=30G              # maximum memory available to GATK

# create temporary directory for Java so it does not fill up /tmp
TMPDIR=/nesi/nobackup/<project_ID>/GATK_tmp/
mkdir -p ${TMPDIR}

# remove other modules that may be loaded
# load specific GATK version
module purge
module load GATK/4.3.0.0-gimkl-2022a

# tell Java to use ${TMPDIR} as the temporary directory
export _JAVA_OPTIONS=-Djava.io.tmpdir=${TMPDIR}

# run GATK command
gatk MarkDuplicates I=input.bam O=marked_duplicates.bam M=marked_dup_metrics.txt
```



### GATK-Picard

GATK versions 4.0 or higher all contains a copy of the Picard toolkit,
you will not need to separately load the Picard module. To run
GATK-picard commands, use:

``` sl
gatk <picard function> <options>
```

This is different what what is currently written on the GATK
documentation, you do not need to call "java -jar picard.jar
&lt;Picard-function&gt;". Simply replace the Java parts with "gatk" and
the function of interest.

Please also note that there are some inconsistencies between Picard and
GATK flag naming conventions, so it is best to double check them.



## Common Issues

### Out of Memory or Insufficient Space for Shared Memory File

This is related to temporary files being created by Java in `/tmp`, and
then running out of space. If you see the error message
`IOException: No space left on device`, this is not necessarily
referring to your nobackup or projects directory, but is likely to be
Java applications pointing to the small temporary filesystem available
in a compute node.

To work around this, create another directory to use for temporrary
files.

``` sl
# create a new temporary directory
TMPDIR="/nesi/nobackup/<project_directory>/GATK_tmp/"
mkdir -p ${TMPDIR}

# put this line in AFTER you load GATK but BEFORE running GATK
export _JAVA_OPTIONS=-Djava.io.tmpdir=${TMPDIR}
```



### File is not a supported reference file type

The error message "File is not a supported reference file type" comes in
one of the log files. It appears that sometimes GATK requires the file
extension of "fasta" or "fa", for fasta files. Please make sure your
file extensions correctly reflect the file type.





