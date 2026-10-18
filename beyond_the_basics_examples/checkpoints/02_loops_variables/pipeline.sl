#!/bin/bash -e

# Checkpoint: end of lesson 2 (Loops and Variables).
# Same steps as lesson 1, with paths in variables, braces and quotes, and set -u.

#SBATCH --job-name      pipeline
#SBATCH --account       nesi99991
#SBATCH --time          01:00:00
#SBATCH --mem           5G
#SBATCH --cpus-per-task 4
#SBATCH --output        log/%x_%j.out
#SBATCH --error         log/%x_%j.err
#SBATCH --profile       task

# Stop if a variable is used before it is set (for example, a misspelt name).
set -u

module purge
module load FastQC/0.12.1 Trimmomatic/0.39-Java-1.8.0_144
module load bwa-mem2/2.3-GCC-12.3.0 SAMtools/1.22-GCC-12.3.0 BCFtools/1.22-GCC-12.3.0

raw_dir="untrimmed_fastq"
trim_dir="trimmed"
results="results"
ref_genome="ref_genome/ecoli_rel606.fasta"
adapters="${EBROOTTRIMMOMATIC}/adapters/NexteraPE-PE.fa"

mkdir -p "${trim_dir}" "${results}"/{sam,bam,bcf,vcf}

# Quality control
srun fastqc "${raw_dir}"/*.fastq*

for raw_1 in "${raw_dir}"/*_1.fastq.gz
do
    base=$(basename "${raw_1}" _1.fastq.gz)
    srun trimmomatic PE "${raw_1}" "${raw_dir}/${base}_2.fastq.gz" \
        "${trim_dir}/${base}_1.trim.fastq.gz" "${trim_dir}/${base}_1un.trim.fastq.gz" \
        "${trim_dir}/${base}_2.trim.fastq.gz" "${trim_dir}/${base}_2un.trim.fastq.gz" \
        SLIDINGWINDOW:4:20 MINLEN:25 ILLUMINACLIP:"${adapters}":2:40:15
done

srun gunzip "${trim_dir}"/*.fastq.gz

# Reference genome indexing
srun gunzip -kf "${ref_genome}.gz"
srun bwa-mem2 index "${ref_genome}"

# Alignment and variant calling
for fq1 in "${trim_dir}"/*_1.trim.fastq
do
    base=$(basename "${fq1}" _1.trim.fastq)
    fq2="${trim_dir}/${base}_2.trim.fastq"
    sam="${results}/sam/${base}.aligned.sam"
    bam="${results}/bam/${base}.aligned.bam"
    sorted_bam="${results}/bam/${base}.aligned.sorted.bam"
    bcf="${results}/bcf/${base}.bcf"
    vcf="${results}/vcf/${base}.vcf"
    final_variants="${results}/vcf/${base}.var.vcf"

    srun bwa-mem2 mem -t 4 "${ref_genome}" "${fq1}" "${fq2}" > "${sam}"
    srun samtools view -S -b "${sam}" > "${bam}"
    srun samtools sort "${bam}" -o "${sorted_bam}"
    srun bcftools mpileup -O b -o "${bcf}" -f "${ref_genome}" "${sorted_bam}"
    srun bcftools call --ploidy 1 -m -v -o "${vcf}" "${bcf}"
    srun vcfutils.pl varFilter "${vcf}" > "${final_variants}"
done
