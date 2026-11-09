#!/bin/bash -e

module purge
module load R/4.6.0-foss-2026
Rscript sum_matrix.r
echo "Done!"
