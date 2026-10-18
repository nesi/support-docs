#!/bin/bash -e

# Checkpoint: end of lesson 6 (Job Arrays). Unchanged from lesson 5.
# Renamed from pipeline.sl. Runs once, before any sample.

#SBATCH --job-name      prepare
#SBATCH --account       nesi99991
#SBATCH --time          00:15:00
#SBATCH --mem           1G
#SBATCH --cpus-per-task 1
#SBATCH --output        log/%x_%j.out
#SBATCH --error         log/%x_%j.err

set -u

module purge
module load bwa-mem2/2.3-GCC-12.3.0

ref_genome="ref_genome/ecoli_rel606.fasta"

# Reference genome indexing
gunzip -kf "${ref_genome}.gz"
bwa-mem2 index "${ref_genome}"
