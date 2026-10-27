#!/bin/bash -e

#SBATCH --job-name      qc
#SBATCH --account       nesi99991
#SBATCH --time          00:15:00
#SBATCH --mem           2G
#SBATCH --cpus-per-task 2
#SBATCH --output        log/%x_%j.out

set -u

# Quality control for every sample.
adapters=${EBROOTTRIMMOMATIC}/adapters/NexteraPE-PE.fa
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
