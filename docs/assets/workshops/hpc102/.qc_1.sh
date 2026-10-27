#!/bin/bash -e

set -u

# Quality control for one sample, given as the first argument.
base="$1"

raw_1=untrimmed_fastq/${base}_1.fastq.gz
raw_2=untrimmed_fastq/${base}_2.fastq.gz
adapters=${EBROOTTRIMMOMATIC}/adapters/NexteraPE-PE.fa
mkdir -p results/fastqc trimmed

fastqc --outdir results/fastqc ${raw_1} ${raw_2}
trimmomatic PE ${raw_1} ${raw_2} \
    trimmed/${base}_1.trim.fastq.gz trimmed/${base}_1un.trim.fastq.gz \
    trimmed/${base}_2.trim.fastq.gz trimmed/${base}_2un.trim.fastq.gz \
    SLIDINGWINDOW:4:20 MINLEN:25 ILLUMINACLIP:${adapters}:2:40:15
