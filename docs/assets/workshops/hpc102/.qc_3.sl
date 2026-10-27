#!/bin/bash -e

#SBATCH --job-name      qc
#SBATCH --account       nesi99991
#SBATCH --time          00:15:00
#SBATCH --mem           2G
#SBATCH --cpus-per-task 2
#SBATCH --output        log/%x_%A_%a.out

set -u

# Quality control for one sample.
# The first argument if given, otherwise this array task's line of samples.txt.
base=${1:-$(sed -n "${SLURM_ARRAY_TASK_ID}p" samples.txt)}

raw_1=untrimmed_fastq/${base}_1.fastq.gz
raw_2=untrimmed_fastq/${base}_2.fastq.gz
adapters=${EBROOTTRIMMOMATIC}/adapters/NexteraPE-PE.fa
mkdir -p results/fastqc trimmed

fastqc --outdir results/fastqc ${raw_1} ${raw_2}
trimmomatic PE ${raw_1} ${raw_2} \
    trimmed/${base}_1.trim.fastq.gz trimmed/${base}_1un.trim.fastq.gz \
    trimmed/${base}_2.trim.fastq.gz trimmed/${base}_2un.trim.fastq.gz \
    SLIDINGWINDOW:4:20 MINLEN:25 ILLUMINACLIP:${adapters}:2:40:15
