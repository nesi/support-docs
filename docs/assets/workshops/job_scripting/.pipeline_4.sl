#!/bin/bash -e

#SBATCH --job-name      pipeline
#SBATCH --account       nesi99991
#SBATCH --time          04:00:00
#SBATCH --mem           5G
#SBATCH --cpus-per-task 4
#SBATCH --profile       task
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
bash index.sh
bash qc.sh
bash align.sh
