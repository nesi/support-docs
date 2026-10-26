#!/bin/bash -e

#SBATCH --job-name      intermed-hpc-01
#SBATCH --account       nesi99991
#SBATCH --time          04:00:00
#SBATCH --mem           5G
#SBATCH --cpus-per-task 4
#SBATCH --profile       task

module purge
module load FastQC/0.12.1
module load Trimmomatic/0.39-Java-1.8.0_144
module load bwa-mem2/2.3-GCC-12.3.0
module load SAMtools/1.22-GCC-12.3.0
module load BCFtools/1.22-GCC-12.3.0

# Limit Java's memory, or Trimmomatic sizes it from the whole node.
export JAVA_TOOL_OPTIONS="-Xmx1g"

# Quality control
cd untrimmed_fastq
fastqc *.fastq*

mkdir -p ../trimmed
cd ../trimmed
for infile in ../untrimmed_fastq/*_1.fastq.gz
do
    base=$(basename ${infile} _1.fastq.gz)
    trimmomatic PE ${infile} ../untrimmed_fastq/${base}_2.fastq.gz \
        ${base}_1.trim.fastq.gz ${base}_1un.trim.fastq.gz \
        ${base}_2.trim.fastq.gz ${base}_2un.trim.fastq.gz \
        SLIDINGWINDOW:4:20 MINLEN:25 \
        ILLUMINACLIP:${EBROOTTRIMMOMATIC}/adapters/NexteraPE-PE.fa:2:40:15
done

cd ..
mkdir -p results/sam results/bam results/bcf results/vcf
gunzip trimmed/*.fastq.gz

# Reference genome indexing
gunzip -kf ref_genome/ecoli_rel606.fasta.gz
bwa-mem2 index ref_genome/ecoli_rel606.fasta

# Alignment and variant calling
for infile in trimmed/*_1.trim.fastq
do
    base=$(basename ${infile} _1.trim.fastq)
    bwa-mem2 mem -t 4 ref_genome/ecoli_rel606.fasta \
        ${infile} trimmed/${base}_2.trim.fastq > results/sam/${base}.aligned.sam
    samtools view -S -b results/sam/${base}.aligned.sam \
        > results/bam/${base}.aligned.bam
    samtools sort results/bam/${base}.aligned.bam \
        -o results/bam/${base}.aligned.sorted.bam
    bcftools mpileup -O b -o results/bcf/${base}.bcf \
        -f ref_genome/ecoli_rel606.fasta results/bam/${base}.aligned.sorted.bam
    bcftools call --ploidy 1 -m -v \
        -o results/vcf/${base}.vcf results/bcf/${base}.bcf
    vcfutils.pl varFilter results/vcf/${base}.vcf > results/vcf/${base}.var.vcf
done
