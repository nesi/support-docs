#!/bin/bash -e

set -u

module purge
module load FastQC/0.12.1
module load Trimmomatic/0.39-Java-1.8.0_144
module load bwa-mem2/2.3-GCC-12.3.0
module load SAMtools/1.22-GCC-12.3.0
module load BCFtools/1.22-GCC-12.3.0

# Limit Java's memory, or Trimmomatic sizes it from the whole node.
export JAVA_TOOL_OPTIONS="-Xmx1g"

# sbatch passes the modules loaded here on to each job,
# and each step script's #SBATCH header sets its resources.
# Index the reference genome once, then queue each sample's steps.
index=$(sbatch --parsable index.sh)

while read -r sample; do
    qc=$(sbatch --parsable qc.sh ${sample})
    # Alignment waits for this sample's quality control, and for indexing.
    align=$(sbatch --parsable --dependency afterok:${qc}:${index} \
        align.sh ${sample})
    echo "${sample}: qc ${qc}, align ${align}"
done < samples.txt

echo "index: ${index}"
