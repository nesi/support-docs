#!/bin/bash -e

set -u

# Load the software here. sbatch passes this environment on to each job.
module purge
module load FastQC/0.12.1
module load Trimmomatic/0.39-Java-1.8.0_144
module load bwa-mem2/2.3-GCC-12.3.0
module load SAMtools/1.22-GCC-12.3.0
module load BCFtools/1.22-GCC-12.3.0

# Limit Java's memory, or Trimmomatic sizes it from the whole node.
export JAVA_TOOL_OPTIONS="-Xmx1g"

# One array task per sample. Task indexes start at 0, so the last is one less
# than the number of files.
files=(untrimmed_fastq/*_1.fastq.gz)
last=$(( ${#files[@]} - 1 ))

# Quality control as a job array, and indexing alongside.
qc=$(sbatch --parsable --array 0-${last} qc.sl)
index=$(sbatch --parsable index.sh)

# Each alignment task waits for the QC task of the same sample, and for indexing.
align=$(sbatch --parsable --array 0-${last} \
    --dependency aftercorr:${qc},afterok:${index} align.sl)

# Once every alignment task has succeeded, summarise the results.
summary=$(sbatch --parsable --dependency afterok:${align} summarise.sl)

# If any alignment task fails, resubmit only the failed tasks, with more memory.
resubmit=$(sbatch --parsable --dependency afternotok:${align} --job-name resubmit \
    --time 00:05:00 --mem 512M --output log/%x_%j.out \
    --wrap "bash resubmit_failed.sh ${align}")

echo "qc: ${qc}  index: ${index}  align: ${align}"
echo "summarise: ${summary}  resubmit: ${resubmit}"
