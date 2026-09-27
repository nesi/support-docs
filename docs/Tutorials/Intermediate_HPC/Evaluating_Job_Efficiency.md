---
description: 
status: tutorial
tags:
- tutorial
- perf
- profiling
---


!!! time "wibbly wobbly timey wimey" <!--TODO-->

!!! objectives
    - review the resource utilisation of a previous job
    - identify areas for improvement in job efficiency

!!! info "Prerequisites"
    This tutorial assumes familiarity with Mahuika and the use of HPCs. You should be able to:
    
    - use the terminal to navigate a filesystem
    - find and load software
    - write a SLURM batch script
    - submit batch jobs to SLURM
    - check on the status of queued and completed SLURM jobs

    These tasks are covered in the [Introduction to HPC tutorials](../Introduction_To_HPC/What_Is_an_HPC.md).

## Summary and Setup

This tutorial aims to give you hands on experience evaluating and improving job efficiency.
To do that, we are going to work with an example workflow from genomics, but no genomics knowledge is needed for the tutorial.
The example used here is based on materials from the [Data Carpentry Data Wrangling and Processing for Genomics](https://datacarpentry.github.io/wrangling-genomics/02-quality-control.html#bioinformatic-workflows) if you want more information.
There are 3 broad steps that need to run in this workflow:

1. Quality control
2. Indexing the reference genome
3. Alignment and variant calling

To begin, we will be working with some example scripts that can be found in `/opt/nesi/examples/intermediate_hpc`.
You will want to have these files in your `nobackup` directory.
Let's make a directory to work from and copy the files in.

```bash
cd /nesi/nobackup/<project_id>/
mkdir -p intermed_hpc_<username>
cd intermed_hpc_<username>
cp -r /opt/nesi/examples/intermediate_hpc .
```

## Looking at a previous job and its efficiency

### `sacct`

??? note "`01_script.sl`"

    ```bash

    #!/bin/bash -e

    #SBATCH --job-name=intermed-hpc-01
    #SBATCH --output=log/%x_%j.out
    #SBATCH --error=log/%x_%j.err
    #SBATCH --time=1:00:00
    #SBATCH --mem=5G
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=4
    #SBATCH --profile=task

    module purge

    # Quality control
    module load FastQC/0.12.1

    cd untrimmed_fastq
    fastqc *.fastq* # fastqc can take multiple files as input, so we can run it on all fastq files in the current directory

    mkdir -p ../trimmed
    cd ../trimmed
    module load Trimmomatic/0.39-Java-1.8.0_144

    for infile in ../untrimmed_fastq/*_1.fastq.gz
    do
        base=$(basename ${infile} _1.fastq.gz)
        trimmomatic PE ${infile} ../untrimmed_fastq/${base}_2.fastq.gz \
                        ${base}_1.trim.fastq.gz ${base}_1un.trim.fastq.gz \
                        ${base}_2.trim.fastq.gz ${base}_2un.trim.fastq.gz \
                        SLIDINGWINDOW:4:20 MINLEN:25 ILLUMINACLIP:/opt/nesi/CS400_centos7_bdw/Trimmomatic/0.39-Java-1.8.0_144/adapters/NexteraPE-PE.fa:2:40:15 
    done


    cd ..
    mkdir -p results/sam results/bam results/bcf results/vcf
    gunzip trimmed/*.fastq.gz

    module load bwa-mem2/2.3-GCC-12.3.0
    module load SAMtools/1.22-GCC-12.3.0
    module load BCFtools/1.22-GCC-12.3.0
    # Reference genome indexing
    gunzip -k ref_genome/ecoli_rel606.fasta.gz
    bwa-mem2 index ref_genome/ecoli_rel606.fasta
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

The example script `01_script.sl` has already been run as a batch job and has the job ID `{{ intermediate_hpc_job_id_01 }}`.
Let's take a look at the status of that job before we even start looking at the script and see what we can learn.

```bash
sacct -j {{ intermediate_hpc_job_id_01 }}
```

```output
JobID           JobName    Elapsed     AveCPU     MinCPU   TotalCPU Al NT     MaxRSS      State 
------------ ---------- ---------- ---------- ---------- ---------- -- -- ---------- ---------- 
9296168      intermed-+   00:29:10                        29:56.822  8                COMPLETED 
9296168.bat+      batch   00:29:10   00:29:57   00:29:57  29:56.822  8  1   1439444K  COMPLETED 
9296168.ext+     extern   00:29:10                         00:00:00  8  1             COMPLETED
```

!!! tip "Changing what `sacct` shows you by default"
    format flags that might be helpful
    
    stick this in bash profile
    <!-- TODO -->

### `seff`

The basic `sacct` tells us a little about the job: the runtime, how many CPUs were allocated, the final job state.
But this information doesn't really help us evaluate how well the job ran.
To look at the efficiency of our job, we can use the command `seff` (short for **s**lurm **eff**iciency):

```bash
seff {{ intermediate_hpc_job_id_01 }}
```

```output
Job ID: 9296168
State: COMPLETED
Cores: 4
Job Wall-time:         12%  00:29:10 of 04:00:00 time limit
Avg CPU Utilisation:   26%  00:29:57 of 01:56:40 core-walltime
Peak Mem Utilisation:  27%  1.37 GB of 5.00 GB
```

`seff` gives us a lot of the same information but with a bit more context.

!!! exercise "What resources would you request if resubmitting the job based only on this information?"
    You aren't working with a lot of information yet, but we can take a first stab at how to improve our job efficiency just by adjusting our requested resources.
    

??? solution "Resources for next time"
    We can probably lower the memory and CPUs requested, but if we are doing so, it might be best to leave the job time alone so if the job runs a little slower it doesn't timeout.

This is a good first step, we noticed that we are requesting more resources than we need and can make some quick adjustments.
But this assumes that the resources being used are fairly stable over the script.
The CPU utilisation is just an average, so we don't know if there was a portion of the job that did use all the CPUs we allocated to the job.

### Job profiling

SLURM has the ability to conduct 'profiling' on jobs being submitted.
This stores extra data about the resources the job uses at various times throughout the job and can let you assess your efficiency in more detail.
To enable profiling in a batch job, you need to add the following to your SLURM header:

```sl
#SBATCH --profile=task
```

Luckily for us, this was included in our script when it was run previously, so we can access this data about our job.
We can run `profile_plot {{ intermediate_hpc_job_id_01 }}` to produce a PNG with plots of the CPU, memory and I/O utilisation over the course of our job.

![Profile plot for job ID `{{ intermediate_hpc_job_id_01 }}`](../../assets/images/intermediate_hpc_profile_plot_01.png)

Now we can see things in a bit more detail.

!!! exercise "What stands out?"
    What more can we learn from these plots? Does this change your thoughts on how to adjust the requested resources?

## Reviewing our job script

Now let's actually take a look at what this job was running.
Let's open `01_script.sl` and poke around.

!!! tip "Looking at the script based on the job ID"
    If we add the flag `-B` to our `sacct` command, `sacct` will return the script that was called for the job we are interested in.

    ```bash
    sacct -B -j {{ intermediate_hpc_job_id_01 }}
    ```

    Ideally you remember what script was run, but this can be helpful if you aren't sure what you changed since you last ran a job or if you aren't sure which script was actually used.

As mentioned above, this script is doing 3 major steps which are indicated with comments in the script:

1. Quality control
2. Indexing the reference genome
3. Alignment and variant calling

!!! exercise "Splitting tasks by resource needs"
    Let's identify different sections of the script (`01_script.sl`) that have significantly different resource needs and split them into separate jobs with appropriate resource requests for each.

??? solution "Updated scripts"
    There is no one correct answer here! But here is one option.
    Looking at the profile plot, we can try to identify the steps of the job.

    ![Annotated profile plot for `{{ intermediate_hpc_job_id_01 }}`](../../assets/images/intermediate_hpc_job_id_01_markup.png)

    There are two major sections in the profile plot, and one little blip in the middle that we can guess is the reference genome indexing occurring between the quality control and alignment/variant calling steps.

    So we can create three scripts to better assign resources:

    `01_script_a.sl`
    
    ```bash

    #!/bin/bash -e

    #SBATCH --job-name=intermed-hpc-01a
    #SBATCH --output=log/%x_%j.out
    #SBATCH --error=log/%x_%j.err
    #SBATCH --time=00:30:00
    #SBATCH --mem=5G
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --profile=task

    module purge
    # Quality control
    module load FastQC/0.12.1
    cd untrimmed_fastq
    fastqc *.fastq* # fastqc can take multiple files as input, so we can run it on all fastq files in the current directory

    mkdir -p ../trimmed
    cd ../trimmed
    module load Trimmomatic/0.39-Java-1.8.0_144

    for infile in ../untrimmed_fastq/*_1.fastq.gz
    do
        base=$(basename ${infile} _1.fastq.gz)
        trimmomatic PE ${infile} ../untrimmed_fastq/${base}_2.fastq.gz \
                        ${base}_1.trim.fastq.gz ${base}_1un.trim.fastq.gz \
                        ${base}_2.trim.fastq.gz ${base}_2un.trim.fastq.gz \
                        SLIDINGWINDOW:4:20 MINLEN:25 ILLUMINACLIP:/opt/nesi/CS400_centos7_bdw/Trimmomatic/0.39-Java-1.8.0_144/adapters/NexteraPE-PE.fa:2:40:15 
    done
    ```
    
    `01_script_b.sl`
    
    ```bash

    #!/bin/bash -e

    #SBATCH --job-name=intermed-hpc-01b
    #SBATCH --output=log/%x_%j.out
    #SBATCH --error=log/%x_%j.err
    #SBATCH --time=00:30:00
    #SBATCH --mem=1G
    #SBATCH --ntasks=1
    #SBATCH --cpus-per-task=1
    #SBATCH --profile=task

    module load bwa-mem2/2.3-GCC-12.3.0
    # Reference genome indexing
    gunzip -k ref_genome/ecoli_rel606.fasta.gz
    bwa-mem2 index ref_genome/ecoli_rel606.fasta
    ```

    `01_script_c.sl`
    
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

