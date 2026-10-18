#!/bin/bash -e

# Checkpoint: end of lesson 3 (Reusable Job Scripts).
# Processes one sample, given as the first argument:
#   sbatch sample.sl SRR2584863
# Run pipeline.sl first, so the reference genome is indexed.

#SBATCH --job-name      sample
#SBATCH --account       nesi99991
#SBATCH --time          00:30:00
#SBATCH --mem           2G
#SBATCH --cpus-per-task 4
#SBATCH --output        log/%x_%j.out
#SBATCH --error         log/%x_%j.err
#SBATCH --profile       task

set -u

module purge
module load FastQC/0.12.1 Trimmomatic/0.39-Java-1.8.0_144
module load bwa-mem2/2.3-GCC-12.3.0 SAMtools/1.22-GCC-12.3.0 BCFtools/1.22-GCC-12.3.0

sample="$1"
threads="${SLURM_CPUS_PER_TASK}"

raw_dir="untrimmed_fastq"
trim_dir="trimmed"
results="results"
ref_genome="ref_genome/ecoli_rel606.fasta"
adapters="${EBROOTTRIMMOMATIC}/adapters/NexteraPE-PE.fa"

raw_1="${raw_dir}/${sample}_1.fastq.gz"
raw_2="${raw_dir}/${sample}_2.fastq.gz"
fq1="${trim_dir}/${sample}_1.trim.fastq"
fq2="${trim_dir}/${sample}_2.trim.fastq"
sam="${results}/sam/${sample}.aligned.sam"
bam="${results}/bam/${sample}.aligned.bam"
sorted_bam="${results}/bam/${sample}.aligned.sorted.bam"
bcf="${results}/bcf/${sample}.bcf"
vcf="${results}/vcf/${sample}.vcf"
final_variants="${results}/vcf/${sample}.var.vcf"

mkdir -p "${trim_dir}" "${results}"/{fastqc,sam,bam,bcf,vcf}

# Quality control
srun fastqc --threads "${threads}" --outdir "${results}/fastqc" "${raw_1}" "${raw_2}"
srun trimmomatic PE -threads "${threads}" "${raw_1}" "${raw_2}" \
    "${fq1}.gz" "${trim_dir}/${sample}_1un.trim.fastq.gz" \
    "${fq2}.gz" "${trim_dir}/${sample}_2un.trim.fastq.gz" \
    SLIDINGWINDOW:4:20 MINLEN:25 ILLUMINACLIP:"${adapters}":2:40:15
srun gunzip -f "${fq1}.gz" "${fq2}.gz"

# Alignment and variant calling
srun bwa-mem2 mem -t "${threads}" "${ref_genome}" "${fq1}" "${fq2}" > "${sam}"
srun samtools view -S -b "${sam}" > "${bam}"
srun samtools sort "${bam}" -o "${sorted_bam}"
srun bcftools mpileup -O b -o "${bcf}" -f "${ref_genome}" "${sorted_bam}"
srun bcftools call --ploidy 1 -m -v -o "${vcf}" "${bcf}"
srun vcfutils.pl varFilter "${vcf}" > "${final_variants}"
