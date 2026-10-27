#!/bin/bash -e

set -u

# Alignment and variant calling for every sample.
ref_genome=ref_genome/ecoli_rel606.fasta
mkdir -p results/sam results/bam results/bcf results/vcf

for infile in trimmed/*_1.trim.fastq.gz
do
    base=$(basename ${infile} _1.trim.fastq.gz)

    fq1=trimmed/${base}_1.trim.fastq
    fq2=trimed/${base}_2.trim.fastq
    sam=results/sam/${base}.aligned.sam
    bam=results/bam/${base}.aligned.bam
    sorted_bam=results/bam/${base}.aligned.sorted.bam
    bcf=results/bcf/${base}.bcf
    vcf=results/vcf/${base}.vcf
    final_variants=results/vcf/${base}.var.vcf

    gunzip -kf ${fq1}.gz ${fq2}.gz
    bwa-mem2 mem -t ${SLURM_CPUS_PER_TASK} ${ref_genome} ${fq1} ${fq2} > ${sam}
    samtools view -S -b ${sam} > ${bam}
    samtools sort ${bam} -o ${sorted_bam}
    bcftools mpileup -O b -o ${bcf} -f ${ref_genome} ${sorted_bam}
    bcftools call --ploidy 1 -m -v -o ${vcf} ${bcf}
    vcfutils.pl varFilter ${vcf} > ${final_variants}
done
