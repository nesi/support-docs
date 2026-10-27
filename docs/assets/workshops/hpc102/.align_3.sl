#!/bin/bash -e

#SBATCH --job-name      align
#SBATCH --account       nesi99991
#SBATCH --time          00:15:00
#SBATCH --mem           1500M
#SBATCH --cpus-per-task 4
#SBATCH --output        log/%x_%A_%a.out

set -u

# Alignment and variant calling for one sample.
# The first argument if given, otherwise this array task's line of samples.txt.
base=${1:-$(sed -n "${SLURM_ARRAY_TASK_ID}p" samples.txt)}

ref_genome=ref_genome/ecoli_rel606.fasta
fq1=trimmed/${base}_1.trim.fastq
fq2=trimmed/${base}_2.trim.fastq
sam=results/sam/${base}.aligned.sam
bam=results/bam/${base}.aligned.bam
sorted_bam=results/bam/${base}.aligned.sorted.bam
bcf=results/bcf/${base}.bcf
vcf=results/vcf/${base}.vcf
final_variants=results/vcf/${base}.var.vcf

mkdir -p results/sam results/bam results/bcf results/vcf
gunzip -kf ${fq1}.gz ${fq2}.gz

bwa-mem2 mem -t ${SLURM_CPUS_PER_TASK} ${ref_genome} ${fq1} ${fq2} > ${sam}
samtools view -S -b ${sam} > ${bam}
samtools sort ${bam} -o ${sorted_bam}
bcftools mpileup -O b -o ${bcf} -f ${ref_genome} ${sorted_bam}
bcftools call --ploidy 1 -m -v -o ${vcf} ${bcf}
vcfutils.pl varFilter ${vcf} > ${final_variants}
