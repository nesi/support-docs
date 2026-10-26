#!/bin/bash -e

# Load the software here. sbatch passes this environment on to each job.
module purge
module load FastQC/0.12.1
module load Trimmomatic/0.39-Java-1.8.0_144
module load bwa-mem2/2.3-GCC-12.3.0
module load SAMtools/1.22-GCC-12.3.0
module load BCFtools/1.22-GCC-12.3.0

# Limit Java's memory, or Trimmomatic sizes it from the whole node.
export JAVA_TOOL_OPTIONS="-Xmx1g"

n_samples=$(wc -l < samples.txt)

# Quality control as a job array, one task per sample, and indexing alongside.
qc=$(sbatch --parsable --array 1-${n_samples} qc.sl)
index=$(sbatch --parsable --job-name index --account nesi99991 --time 00:05:00 \
    --mem 1G --cpus-per-task 1 --output log/%x_%j.out --error log/%x_%j.err \
    index.sh)

# Each alignment task waits for the QC task of the same sample, and for indexing.
align=$(sbatch --parsable --array 1-${n_samples} \
    --dependency aftercorr:${qc},afterok:${index} align.sl)

# Once every alignment task has succeeded, summarise the results.
summary=$(sbatch --parsable --dependency afterok:${align} summarise.sl)

# If any alignment task fails, resubmit only the failed tasks, with more memory.
resubmit=$(sbatch --parsable --dependency afternotok:${align} --job-name resubmit \
    --time 00:05:00 --mem 512M --output log/%x_%j.out \
    --wrap "bash resubmit_failed.sh ${align}")

echo "qc: ${qc}  index: ${index}  align: ${align}"
echo "summarise: ${summary}  resubmit: ${resubmit}"
