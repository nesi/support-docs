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

While we might be able to dig in and figure out a bit more, right now we don't know when we switch between these steps during our job, so we can't tell which processes need more memory or can't use all the CPUs available.

### Splitting up your job (without adding to your workload)

Ideally we want to know the performance of each step in our workflow, but no one likes watching for one job to finish so they can submit another.
Luckily, there are ways to make SLURM do all the work for you!

#### Job steps

SLURM provides ways to submit a single batch job that has multiple steps.
Within a SLURM script separate job steps are indicated by using `srun` before the command.
`srun` can be used to run multiple processes simultaneously with portions of the resources allocated to the entire job script.
To get a quick sense for the resources used in our job, we've modified `01_script.sl` to make `02_script.sl` which wraps different sections in `srun`.
There are 4 calls of `srun` within the script, which SLURM will label sequentially as steps 0 through 3.
We can look at the results of this job the same way as our previous job:

```bash
sacct {{ intermediate_hpc_job_id_02 }}
```

```output
JobID           JobName          Alloc     Elapsed     TotalCPU  ReqMem   MaxRSS State      
--------------- ---------------- ----- ----------- ------------ ------- -------- ---------- 
9310633         intermed-hpc-02      8    00:16:43    27:40.806      5G          COMPLETED  
9310633.batch   batch                8    00:16:43    00:22.645            6908K COMPLETED  
9310633.extern  extern               8    00:16:43     00:00:00                  COMPLETED  
9310633.0       bash                 8    00:01:52    01:51.996          593880K COMPLETED  
9310633.1       bash                 8    00:03:54    10:19.651         2263436K COMPLETED  
9310633.2       bash                 8    00:00:03    00:01.645                0 COMPLETED  
9310633.3       bash                 8    00:10:29    15:04.867         1299004K COMPLETED
```

`sacct` now gives us information for the entire job as well as for each individual job step.

```bash
seff {{ intermediate_hpc_job_id_02 }}
```

```output
Job ID: 9310633
State: COMPLETED
Steps: batch + 4
Tasks: 1
Cores: 4
Job Wall-time:         28%  00:16:43 of 01:00:00 time limit
Avg CPU Utilisation:   41%  00:27:41 of 01:06:52 core-walltime
Peak Mem Utilisation:  43%  2.17 GB of 5.00 GB (6.75 MB to 2.16 GB in each of 2 tasks from 2 job steps)
```

`seff` still summarises across the entire job, but we can see the range of peak memory utilisations across the different job steps.

```bash
profile_plot {{ intermediate_hpc_job_id_02 }}
```

![Profile plot for job ID `{{ intermediate_hpc_job_id_02 }}`](../../assets/images/intermediate_hpc_profile_plot_02.png)

The profile plot now shows each step in a different line/color.

#### Dependent jobs

SLURM also allows us to submit a job with a dependency specified.
In this case, we can indicate that we only want the job to run after a previous job has finished successfully.
To use this method, we've split `01_script.sl` into three separate job scripts: `03a_script.sl`, `03b_script.sl`, and `03c_script.sl`.
These jobs were then submitted as three commands:

```bash
sbatch 03a_script.sl
```

```output
Submitted batch job {{ intermediate_hpc_job_id_03a }}
```

```bash
sbatch --dependency=afterok:{{ intermediate_hpc_job_id_03a }} 03b_script.sl
```

```output
Submitted batch job {{ intermediate_hpc_job_id_03b }}
```

```bash
sbatch --dependency=afterok:{{ intermediate_hpc_job_id_03b }} 03c_script.sl
```

```output
Submitted batch job {{ intermediate_hpc_job_id_03c }}
```

!!! tip "Submitting dependent jobs via scripts"
    bash script use variables
    <!-- TODO -->

When you've submitted dependent jobs, they will appear in your queue as pending with the reason being 'Dependency'. For example:

```bash
squeue --me
```

```output
JOBID         USER     ACCOUNT   NAME        CPUS MIN_MEM PARTITI START_TIME     TIME_LEFT STATE    NODELIST(REASON)    
9311120       <user> <project> intermed-hpc   8      5G genoa   Sep 25 15:17       55:35 RUNNING  c005                
9311121       <user> <project> intermed-hpc   4      5G milan,g N/A              1:00:00 PENDING  (Dependency)        
9311125       <user> <project> intermed-hpc   4      5G milan,g N/A              1:00:00 PENDING  (Dependency) 
```

And again the same options for reviewing our jobs are available, but now we have 3 separate job IDs we need to query.

```bash
sacct -j {{ intermediate_hpc_job_id_03a }},{{ intermediate_hpc_job_id_03b }},{{ intermediate_hpc_job_id_03c }}
```

```output
JobID           JobName          Alloc     Elapsed     TotalCPU  ReqMem   MaxRSS State      
--------------- ---------------- ----- ----------- ------------ ------- -------- ---------- 
9311120         intermed-hpc-03a     8    00:04:47    10:35.512      5G          COMPLETED  
9311120.batch   batch                8    00:04:47    10:35.512         2199560K COMPLETED  
9311120.extern  extern               8    00:04:47     00:00:00                  COMPLETED  
9311121         intermed-hpc-03b     8    00:00:26    00:22.655      5G          COMPLETED  
9311121.batch   batch                8    00:00:26    00:22.655                0 COMPLETED  
9311121.extern  extern               8    00:00:26     00:00:00                  COMPLETED  
9311125         intermed-hpc-03c     8    00:11:17    15:45.592      5G          COMPLETED  
9311125.batch   batch                8    00:11:17    15:45.592         1632720K COMPLETED  
9311125.extern  extern               8    00:11:17     00:00:00                  COMPLETED  
```

```bash
seff {{ intermediate_hpc_job_id_03a }} {{ intermediate_hpc_job_id_03b }} {{ intermediate_hpc_job_id_03c }}
```

```output
Job ID: 9311120
State: COMPLETED
Cores: 4
Job Wall-time:          8%  00:04:47 of 01:00:00 time limit
Avg CPU Utilisation:   55%  00:10:35 of 00:19:08 core-walltime
Peak Mem Utilisation:  42%  2.10 GB of 5.00 GB

Job ID: 9311121
State: COMPLETED
Cores: 4
Job Wall-time:          1%  00:00:26 of 01:00:00 time limit
Avg CPU Utilisation:   22%  00:00:22 of 00:01:44 core-walltime
Peak Mem Utilisation:   0%  0.00 MB of 5.00 GB

Job ID: 9311125
State: COMPLETED
Cores: 4
Job Wall-time:         19%  00:11:17 of 01:00:00 time limit
Avg CPU Utilisation:   35%  00:15:45 of 00:45:08 core-walltime
Peak Mem Utilisation:  31%  1.56 GB of 5.00 GB
```

And for profile plot we will need to run the command separately for each job ID to get our plots.

`{{ intermediate_hpc_job_id_03a }}`

![Profile plot for job ID `{{ intermediate_hpc_job_id_03a }}`](../../assets/images/intermediate_hpc_profile_plot_03a.png)

`{{ intermediate_hpc_job_id_03b }}`

![Profile plot for job ID `{{ intermediate_hpc_job_id_03b }}`](../../assets/images/intermediate_hpc_profile_plot_03b.png)

`{{ intermediate_hpc_job_id_03c }}`

![Profile plot for job ID `{{ intermediate_hpc_job_id_03c }}`](../../assets/images/intermediate_hpc_profile_plot_03c.png)
