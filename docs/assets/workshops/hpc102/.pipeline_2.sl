#!/bin/bash -e

#SBATCH --job-name      intermed-hpc-01
#SBATCH --account       nesi99991
#SBATCH --time          04:00:00
#SBATCH --mem           5G
#SBATCH --cpus-per-task 4

module purge
module load FastQC/0.12.1
module load Trimmomatic/0.39-Java-1.8.0_144
module load bwa-mem2/2.3-GCC-12.3.0
module load SAMtools/1.22-GCC-12.3.0
module load BCFtools/1.22-GCC-12.3.0

# Limit Java's memory, or Trimmomatic sizes it from the whole node.
export JAVA_TOOL_OPTIONS="-Xmx1g"

adapters=${EBROOTTRIMMOMATIC}/adapters/NexteraPE-PE.fa

# Quality control
mkdir -p results/fastqc trimmed
for infile in untrimmed_fastq/*_1.fastq.gz
do
    base=$(basename ${infile} _1.fastq.gz)
    raw_2=untrimmed_fastq/${base}_2.fastq.gz
    fastqc --outdir results/fastqc ${infile} ${raw_2}
    trimmomatic PE ${infile} ${raw_2} \
        trimmed/${base}_1.trim.fastq.gz trimmed/${base}_1un.trim.fastq.gz \
        trimmed/${base}_2.trim.fastq.gz trimmed/${base}_2un.trim.fastq.gz \
        SLIDINGWINDOW:4:20 MINLEN:25 ILLUMINACLIP:${adapters}:2:40:15
done

mkdir -p results/sam results/bam results/bcf results/vcf
gunzip -kf trimmed/*.fastq.gz

# Reference genome indexing
gunzip -kf ref_genome/ecoli_rel606.fasta.gz
bwa-mem2 index ref_genome/ecoli_rel606.fasta

# Alignment and variant calling
for infile in trimmed/*_1.trim.fastq
do
    base=$(basename ${infile} _1.trim.fastq)

    # setting the variables
    ref_genome=ref_genome/ecoli_rel606.fasta
    fq1=trimmed/${base}_1.trim.fastq
    fq2=trimmed/${base}_2.trim.fastq
    sam=results/sam/${base}.aligned.sam
    bam=results/bam/${base}.aligned.bam
    sorted_bam=results/bam/${base}.aligned.sorted.bam
    bcf=results/bcf/${base}.bcf
    vcf=results/vcf/${base}.vcf
    final_variants=results/vcf/${base}.var.vcf

    bwa-mem2 mem -t 4 ${ref_genome} ${fq1} ${fq2} > ${sam}
    samtools view -S -b ${sam} > ${bam}
    samtools sort ${bam} -o ${sorted_bam}
    bcftools mpileup -O b -o ${bcf} -f ${ref_genome} ${sorted_bam}
    bcftools call --ploidy 1 -m -v -o ${vcf} ${bcf}
    vcfutils.pl varFilter ${vcf} > ${final_variants}
done
