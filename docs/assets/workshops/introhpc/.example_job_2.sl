#!/bin/bash -e

#SBATCH --job-name      example_job
#SBATCH --account       nesi99991
#SBATCH --time          00:15:00
#SBATCH --mem           300M

module purge
module load R/4.6.0-foss-2026
Rscript sum_matrix.r
echo "Done!"
