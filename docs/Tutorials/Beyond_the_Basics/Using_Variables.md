---
description: 
status: tutorial
tags:
- tutorial
---

!!! time "wibbly wobbly timey wimey" <!--TODO-->

!!! objectives
    - Use variables to improve script reusability
    - Use variables to improve script robustness
    - Use variables to improve script readability

!!! info "Prerequisites"
    This tutorial assumes familiarity with Mahuika and the use of HPCs. You should be able to:
    
    - use the terminal to navigate a filesystem
    - find and load software
    - write a SLURM batch script
    - submit batch jobs to SLURM
    - check on the status of queued and completed SLURM jobs

    These tasks are covered in the [Introduction to HPC tutorials](../Introduction_To_HPC/What_Is_an_HPC.md).

## Summary and Setup

This tutorial aims to give you hands on experience using variables in SLURM job scripts. To do that, we are going to work with an example script from genomics, but no genomics knowledge is needed for the tutorial. The example used here is based on materials from the [Data Carpentry Data Wrangling and Processing for Genomics](https://datacarpentry.github.io/wrangling-genomics/02-quality-control.html#bioinformatic-workflows) if you want more information.

You don't need to have completed the [Evaluating Job Efficiency tutorial](../Beyond_the_Basics/Evaluating_Job_Efficiency.md) but we will be working with one of the scripts set up at the end of that tutorial. If you haven't already, please follow the setup instructions in the box below to get all the files needed to run the scripts in this tutorial.

??? note "Setup instructions"
    We will be working with some example scripts that can be found in `/opt/nesi/examples/intermediate_hpc`.
    You will want to have these files in your `nobackup` directory.
    Let's make a directory to work from and copy the files in.

    ```bash
    cd /nesi/nobackup/<project_id>/
    mkdir -p tutorial_<username>
    cd tutorial_<username>
    cp -r /opt/nesi/examples/tutorials/job_scripting .
    ```

The script we will be working from is called `02_script.sl` and should be in the `tutorial_<username>` directory you already created. The contents are also below:

```bash
#!/bin/bash -e

#SBATCH --job-name=intermed-hpc-01c
#SBATCH --output=log/%x_%j.out
#SBATCH --error=log/%x_%j.err
#SBATCH --time=00:30:00
#SBATCH --mem=1G
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --profile=task
    
mkdir -p results/sam results/bam results/bcf results/vcf
gunzip trimmed/*.fastq.gz

module load bwa-mem2/2.3-GCC-12.3.0
module load SAMtools/1.22-GCC-12.3.0
module load BCFtools/1.22-GCC-12.3.0
# Alignment and variant calling
for infile in trimmed/*_1.trim.fastq
do
    base=$(basename ${infile} _1.trim.fastq)
    bwa-mem2 mem -t 4 ref_genome/ecoli_rel606.fasta ${infile} trimmed/${base}_2.trim.fastq > results/sam/${base}.aligned.sam
    samtools view -S -b results/sam/${base}.aligned.sam > results/bam/${base}.aligned.bam
    samtools sort results/bam/${base}.aligned.bam -o results/bam/${base}.aligned.sorted.bam
    bcftools mpileup -O b -o results/bcf/${base}.bcf -f ref_genome/ecoli_rel606.fasta results/bam/${base}.aligned.sorted.bam
    bcftools call --ploidy 1 -m -v -o results/vcf/${base}.vcf results/bcf/${base}.bcf
    vcfutils.pl varFilter results/vcf/${base}.vcf > results/vcf/${base}.var.vcf
done
```

This script already uses variables in the for loop with `infile` and `base`.
But how can they help us improve our script further?

Using variables helps with several aspects of writing and using code.
Variables can help with ensuring our script is readable, reusable and robust.

## Variables in file paths

For example, the for loop is quite the block of code and not the easiest to read, but most of that is just listing file names.
Let's define our file names once, and then use variables to call the files where they are needed.

For each loop we have the following files, almost all of which are used multiple times:

- `$infile`: `trimmed/${base}_1.trim.fastq` and its partner `trimmed/${base}_2.trim.fastq`
- the reference genome: `ref_genome/ecoli_rel606.fasta`
- the aligned `.sam`
- the aligned `.bam`
- the sorted `.bam`
- the `.bcf`
- the `.vcf`
- the `.var.vcf`

Let's give each of these a simple but unique name, and see how the for loop looks.

```bash
for infile in trimmed/*_1.trim.fastq
do
    base=$(basename ${infile} _1.trim.fastq)

    # setting the variables
    ref_genome=ref_genome/ecoli_rel606.fasta
    fq1=trimmed_reads/${base}_1.trim.fastq
    fq2=trimmed_reads/${base}_2.trim.fastq
    sam=results/sam/${base}.aligned.sam
    bam=results/bam/${base}.aligned.bam
    sorted_bam=results/bam/${base}.aligned.sorted.bam
    bcf=results/bcf/${base}.bcf
    vcf=results/vcf/${base}.vcf
    final_variants=results/vcf/${base}.var.vcf

    bwa-mem2 mem -t 4 ${ref_genome} ${fq1} ${fq2} > ${sam}
    samtools view -S -b ${sam} > ${bam}
    samtools sort ${bam} -o ${sorted_bam}
    bcftools mpileup -O b -o ${bcf} -f ${ref_genome} ${sorted_bam}$
    bcftools call --ploidy 1 -m -v -o ${vcf} ${bcf}
    vcfutils.pl varFilter ${vcf} > ${final_variants}
done
```

Our for loop is definitely longer, but the commands are easier to read because we don't need to sift through the file paths to know what file is being used where.
Beyond readability, this also helps reduce errors and make any errors that do occur easier to fix.

Let's compare the impact of a simple typo in each version of this loop:

<!-- TODO: just make a typo in the sam file path, either once in the OG script or just in the variable setting in the second script -->

## SLURM environment variables

<!-- TODO: bwa-mem2 takes the threads as an argument, switch to use SLURM TASKS or whatever  -->

<!-- TODO: table of other useful SLURM vars? -->
