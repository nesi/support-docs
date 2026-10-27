#!/bin/bash -e

# align.sl uses the software loaded here.
module purge
module load FastQC/0.12.1
module load Trimmomatic/0.39-Java-1.8.0_144
module load bwa-mem2/2.3-GCC-12.3.0
module load SAMtools/1.22-GCC-12.3.0
module load BCFtools/1.22-GCC-12.3.0

# Limit Java's memory, or Trimmomatic sizes it from the whole node.
export JAVA_TOOL_OPTIONS="-Xmx1g"

# Find the failed tasks of the job array with ID $1, as a list like "1,3".
failed=$(sacct --jobs "$1" --array --allocations --noheader \
    --parsable2 --format JobID,State |
    grep -E 'FAILED|OUT_OF_MEMORY|TIMEOUT' |
    cut -d '|' -f 1 | cut -d '_' -f 2 | paste -sd ,)

# Resubmit only those tasks, with more memory.
if [ -n "${failed}" ]; then
    sbatch --array "${failed}" --mem 3G \
        align.sl
fi
