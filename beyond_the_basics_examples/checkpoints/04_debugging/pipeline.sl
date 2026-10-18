#!/bin/bash -e

# Checkpoint: end of lesson 4 (Debugging Failed Jobs). Unchanged from lesson 3.
# The per-sample steps have moved to sample.sl. Only the step that runs once is left here.

#SBATCH --job-name      pipeline
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
