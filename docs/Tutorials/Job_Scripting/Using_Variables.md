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

This tutorial aims to give you hands-on experience using variables in SLURM job scripts. To do that, we are going to work with an example script from genomics, but no genomics knowledge is needed for the tutorial. The example used here is based on materials from the [Data Carpentry Data Wrangling and Processing for Genomics](https://datacarpentry.github.io/wrangling-genomics/02-quality-control.html#bioinformatic-workflows) if you want more information.

You don't need to have completed the [Evaluating Job Efficiency tutorial](./Evaluating_Job_Efficiency.md) but we will be working with one of the scripts set up at the end of that tutorial. If you haven't already, please follow the setup instructions in the box below to get all the files needed to run the scripts in this tutorial.

??? note "Setup instructions"
    We will be working with some example scripts that can be found in `/opt/nesi/examples/tutorials/job_scripting`.
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

This script already uses variables in the for loop with `$infile` and `$base`.
But how can they help us improve our script further?

Using variables helps with several aspects of writing and using code.
Variables can help with ensuring our script is readable, reusable and robust.

## Formatting variables

You will likely see variables called several different ways: `$var`, `${var}` and `"${var}"` are all common options.
All of these are technically correct, and in some situations you can use whatever option you want.
BUT, in some situations how you format your variable calls makes a difference.

In some cases, it can be unclear where your variable ends and where any adjacent string begins.
To help with that, we can wrap the variable name in curly braces: `${var}`.

```bash
ls
```

```output
01sample.txt  02sample.txt
```

```bash
number=01
wc $numbersample.txt
```

```output
wc: .txt: No such file or directory
```

Instead of combining our variable (`01`) with the rest of the filename (`sample`), bash has instead used what it has stored in the variable `$numbersample` which is currently nothing.

```bash
wc ${number}sample.txt
```

```output
0 0 0 01sample.txt
```

Using quotations around a call of a variable name can help avoid issues caused by spaces or other special characters in the variable.
For example, if we try to use a variable to create a directory with a space in the name, we run into issues that don't immediately raise any errors.

```bash
dir="Folder Name"
mkdir $dir
ls
```

```output
Folder  Name
```

Instead of creating a directory called 'Folder Name', bash instead interpretted the command as `mkdir Folder Name` and created two directories: `Folder` and `Name`.

```bash
mkdir "$dir"
ls
```

```output
'Folder Name'
```

## Variables in file paths

Let's use variables to help make the for loop more readable.
We will define our filenames once, and then use variables to call the files where they are needed.

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
    bcftools mpileup -O b -o ${bcf} -f ${ref_genome} ${sorted_bam}
    bcftools call --ploidy 1 -m -v -o ${vcf} ${bcf}
    vcfutils.pl varFilter ${vcf} > ${final_variants}
done
```

Our for loop is definitely longer, but the commands are easier to read because we don't need to sift through the file paths to know what file is being used where.
Beyond readability, this also helps reduce errors and make any errors that do occur easier to fix.

Let's compare the impact of a simple typo in each version of this loop. For example, what if I miss a letter when typing in the path for the `.sam` file?

Without variables this returns:

```bash
[E::hts_open_format] Failed to open file "results/sam/SRR2584863.aligned.sam" : No such file or directory
samtools view: failed to open "results/sam/SRR2584863.aligned.sam" for reading: No such file or directory
```

!!! question "Exercise"
    In the original script, the path for `.sam` is written out twice.
    Which call of the `.sam` file had the typo that created that error?

??? question "Answer"
    The typo was made in the `bwa-mem2` call where the `.sam` file was created, which means the `samtools view` call requests a file that doesn't exist.

When we use variables the script actually succeeds even though we have made a small mistake in the `.sam` variable (`sam=results/sam/${base}.aliged.sam`).
And instead of needing to search for which call of the `.sam` path is incorrect, there is only one place that the path is defined.

## Environmental variables

In addition to defining variables ourselves, there are also variables that are defined by the operating system and software.
We can use these to make scripts flexible for use by other users or in other contexts.
Rather than having to update your script to run in a new environment etc, we can have the script adapt to the new environment automatically.

In this case, we are going to make sure that the software we are running knows how many CPUs are available to it.
Currently, we pass the argument `-t 4` to the command `bwa-mem2 mem`.
This argument tells `bwa-mem2` how many threads it can use, and we want it to be able to use as many threads as are available to it.
Currently, if we change the number of CPUs we are requesting, we need to change this argument to see any difference in the behaviour of `bwa-mem2`.
But SLURM has an environmental variable called `$SLURM_CPUS_PER_TASK` that can be used to pass this information programmatically.
We can update our for loop to use this variable:

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

    bwa-mem2 mem -t ${SLURM_CPUS_PER_TASK} ${ref_genome} ${fq1} ${fq2} > ${sam}
    samtools view -S -b ${sam} > ${bam}
    samtools sort ${bam} -o ${sorted_bam}
    bcftools mpileup -O b -o ${bcf} -f ${ref_genome} ${sorted_bam}
    bcftools call --ploidy 1 -m -v -o ${vcf} ${bcf}
    vcfutils.pl varFilter ${vcf} > ${final_variants}
done
```

Now if we request more CPUs for this job, `bwa-mem2` will have access to all the CPUs allocated.

There are lots of environmental variables that can be useful in scripts:

|    Variable name      | Meaning |          Potential use          |
| ------------------------ | ------------------------------------------------ |
| `$USER`        | The username of the current user |  |
| `$HOME`      | The path to the user's home directory |                                |
| `$PWD` | Present Working Directory |        |
| `$SHELL` | The path to the current shell interpreter | |
| `$PATH`        | Directories searched for executable commands |           |
| `$HOSTNAME`    | The network name of the machine (within a job this will be the compute node being used)  |        |


SLURM has some specific environmental variables that it sets when running a job as well.

|    Variable name      | Meaning |          Potential use          |
| ------------------------ | ------------------------------------------------ |
| `$SLURM_JOB_ID`        | ID for the current job | Useful for naming output files that won't clash. |
| `$SLURM_JOB_NAME`      | Name of the job | Could be used for creating files/directories with useful names |
| `$SLURM_ARRAY_TASK_ID` | The current index of your job array | Helpful when writing job arrays |
| `$SLURM_CPUS_PER_TASK` | Number of CPUs  | Useful as an input for multithreaded functions. |
| `$SLURM_NTASKS`        | Number of tasks | Useful as an input for MPI functions.            |
| `$SLURM_SUBMIT_DIR`    | Directory where `sbatch` was called. | Helpful for being able to use relative paths |

!!! tip "Finding out about more useful environmental variables"
    You can't use environmental variables that you don't know about!
    So how can we learn about new environmental variables that might help us?

    One option is the classic advice to RTFM (read the frickin manual).
    Lots of documentation includes information about environmental variables that are set or used by the software/tool.
    For example, the samtools documentation includes a section called ['Environmental variables'](https://www.htslib.org/doc/samtools.html#ENVIRONMENT_VARIABLES) which includes paths to reference files and plugins that can be used.

    Another option is to look at what environmental variables exist in your current environment.
    Running the command `env` will print out the details of your environment, and can be a little overwhelming.
    You can combine `env` with the command `grep` to search and narrow things down.
    For example, after loading the SAMtools module, we can use `env | grep SAM` to only get results that include the string `SAM`.


!!! keypoints
    - Using variables can help make code more readable and robust to errors
    - Using environmental variables can help make your code more portable

