#!/bin/bash -e

#SBATCH --job-name      intermed-hpc-01
#SBATCH --account       nesi99991
#SBATCH --time          04:00:00
#SBATCH --mem           5G
#SBATCH --cpus-per-task 4
#SBATCH --output        log/%x_%j.out

set -u

module purge
module load FastQC/0.12.1
module load Trimmomatic/0.39-Java-1.8.0_144
module load bwa-mem2/2.3-GCC-12.3.0
module load SAMtools/1.22-GCC-12.3.0
module load BCFtools/1.22-GCC-12.3.0

# Limit Java's memory, or Trimmomatic sizes it from the whole node.
export JAVA_TOOL_OPTIONS="-Xmx1g"

# The step scripts run with the modules loaded here.
# Index the reference genome once, then run each sample's steps in turn.
bash index.sh

while read -r sample; do
    bash qc.sh ${sample}
    bash align.sh ${sample}
done < samples.txt
