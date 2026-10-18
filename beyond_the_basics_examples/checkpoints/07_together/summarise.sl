#!/bin/bash -e

# Checkpoint: end of lesson 7 (Putting it Together).
# Runs after every sample has finished: counts the variants found in each sample.

#SBATCH --job-name      summarise
#SBATCH --account       nesi99991
#SBATCH --time          00:05:00
#SBATCH --mem           512M
#SBATCH --cpus-per-task 1
#SBATCH --output        log/%x_%j.out
#SBATCH --error         log/%x_%j.err

set -u

summary="results/variant_counts.txt"

echo -e "sample\tvariants" > "${summary}"
while read -r sample; do
    count=$(grep -vc '^#' "results/vcf/${sample}.var.vcf")
    echo -e "${sample}\t${count}" >> "${summary}"
done < samples.txt

cat "${summary}"
