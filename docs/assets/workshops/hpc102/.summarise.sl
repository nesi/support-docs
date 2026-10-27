#!/bin/bash -e

#SBATCH --job-name      summarise
#SBATCH --account       nesi99991
#SBATCH --time          00:05:00
#SBATCH --mem           512M
#SBATCH --output        log/%x_%j.out

summary=results/variant_counts.txt

# Count the variants found in each sample.
echo -e "sample\tvariants" > ${summary}
while read -r sample; do
    count=$(grep -vc '^#' results/vcf/${sample}.var.vcf)
    echo -e "${sample}\t${count}" >> ${summary}
done < samples.txt

cat ${summary}
