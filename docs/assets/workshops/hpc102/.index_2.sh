#!/bin/bash -e

#SBATCH --job-name      index
#SBATCH --account       nesi99991
#SBATCH --time          00:15:00
#SBATCH --mem           1G
#SBATCH --cpus-per-task 1
#SBATCH --output        log/%x_%j.out
#SBATCH --error         log/%x_%j.err

set -u

# Reference genome indexing, once for all samples.
ref_genome=ref_genome/ecoli_rel606.fasta

gunzip -kf ${ref_genome}.gz
bwa-mem2 index ${ref_genome}
