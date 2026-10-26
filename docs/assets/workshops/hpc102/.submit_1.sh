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

common="--account nesi99991 --output log/%x_%j.out --error log/%x_%j.err"

# Index the reference genome once.
index=$(sbatch --parsable --job-name index --time 00:05:00 --mem 1G \
    --cpus-per-task 1 ${common} index.sh)

# For each sample: quality control, then alignment once QC and indexing succeed.
while read -r sample; do
    qc=$(sbatch --parsable --job-name qc --time 00:15:00 --mem 2G \
        --cpus-per-task 2 ${common} qc.sh ${sample})
    align=$(sbatch --parsable --job-name align --time 00:15:00 --mem 1500M \
        --cpus-per-task 4 ${common} --dependency afterok:${qc}:${index} \
        align.sh ${sample})
    echo "${sample}: qc ${qc}, align ${align}"
done < samples.txt

echo "index: ${index}"
