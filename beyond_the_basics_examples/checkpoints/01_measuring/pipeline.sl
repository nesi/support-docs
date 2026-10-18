#!/bin/bash -e

# Checkpoint: end of lesson 1 (Measuring Job Efficiency).
# Each command runs as a job step (srun), so sacct and profile_plot show each one separately.

#SBATCH --job-name      pipeline
#SBATCH --account       nesi99991
#SBATCH --time          01:00:00
#SBATCH --mem           5G
#SBATCH --cpus-per-task 4
#SBATCH --output        log/%x_%j.out
#SBATCH --error         log/%x_%j.err
#SBATCH --profile       task

module purge
module load FastQC/0.12.1 Trimmomatic/0.39-Java-1.8.0_144
module load bwa-mem2/2.3-GCC-12.3.0 SAMtools/1.22-GCC-12.3.0 BCFtools/1.22-GCC-12.3.0

# Quality control
cd untrimmed_fastq
srun fastqc *.fastq*

mkdir -p ../trimmed
cd ../trimmed
for infile in ../untrimmed_fastq/*_1.fastq.gz
do
    base=$(basename ${infile} _1.fastq.gz)
    srun trimmomatic PE ${infile} ../untrimmed_fastq/${base}_2.fastq.gz \
        ${base}_1.trim.fastq.gz ${base}_1un.trim.fastq.gz \
        ${base}_2.trim.fastq.gz ${base}_2un.trim.fastq.gz \
        SLIDINGWINDOW:4:20 MINLEN:25 \
        ILLUMINACLIP:${EBROOTTRIMMOMATIC}/adapters/NexteraPE-PE.fa:2:40:15
done

cd ..
mkdir -p results/sam results/bam results/bcf results/vcf
srun gunzip trimmed/*.fastq.gz

# Reference genome indexing
srun gunzip -kf ref_genome/ecoli_rel606.fasta.gz
srun bwa-mem2 index ref_genome/ecoli_rel606.fasta

# Alignment and variant calling
for infile in trimmed/*_1.trim.fastq
do
    base=$(basename ${infile} _1.trim.fastq)
    srun bwa-mem2 mem -t 4 ref_genome/ecoli_rel606.fasta ${infile} trimmed/${base}_2.trim.fastq \
        > results/sam/${base}.aligned.sam
    srun samtools view -S -b results/sam/${base}.aligned.sam > results/bam/${base}.aligned.bam
    srun samtools sort results/bam/${base}.aligned.bam -o results/bam/${base}.aligned.sorted.bam
    srun bcftools mpileup -O b -o results/bcf/${base}.bcf -f ref_genome/ecoli_rel606.fasta \
        results/bam/${base}.aligned.sorted.bam
    srun bcftools call --ploidy 1 -m -v -o results/vcf/${base}.vcf results/bcf/${base}.bcf
    srun vcfutils.pl varFilter results/vcf/${base}.vcf > results/vcf/${base}.var.vcf
done
