---
created_at: 2026-01-16
---

!!! time "30 Minutes"

!!! objectives
    - "Understand how to look up job statistics and profile code."
    - "Understand job size implications."
    - "Understand problems and limitations involved in using multiple CPUs."

## What Resources?

Last time we submitted a job, we did not specify a number of CPUs, and therefore
we were provided the default of `2` (1 _core_).

As a reminder, our Slurm script `example_job.sl` currently looks like this.

```sl
#!/bin/bash -e

#SBATCH --job-name      example_job
#SBATCH --account       nesi99991
#SBATCH --mem           300M
#SBATCH --time          00:15:00

module purge
module load R/4.3.1-gimkl-2022a
Rscript sum_matrix.r
echo "Done!"```
```

We will now submit the same job again with more CPUs.
We ask for more CPUs using by adding `#SBATCH --cpus-per-task 4` to our script.
Your script should now look like this:

```sl
#!/bin/bash -e

#SBATCH --job-name      example_job
#SBATCH --account       nesi99991
#SBATCH --mem           300M
#SBATCH --time          00:15:00
#SBATCH --cpus-per-task 4

module purge
module load R/4.3.1-gimkl-2022a
Rscript sum_matrix.r
echo "Done!"
```

And then submit using `sbatch` as we did before.

```sh
 sbatch example_job.sl
```

```out
Submitted batch job 23137702
```

!!! tip Watch
    We can prepend any command with `watch` in order to periodically (default 2 seconds) run a command. e.g. `watch
    squeue --me` will give us up to date information on our running jobs.
    Care should be used when using `watch` as repeatedly running a command can have adverse effects.
    Exit `watch` with <kbd>ctrl</kbd> + <kbd>c</kbd>.

Note in squeue, the number under cpus, should be '4'.

Checking on our job with `sacct`.

Oh no!

```out
JobID           JobName  Partition    Account  AllocCPUS      State ExitCode 
------------ ---------- ---------- ---------- ---------- ---------- -------- 
27323464         my_job      large  {{ config.extra.project_code }}          4 OUT_OF_ME+    0:125 
27323464.ba+      batch             {{ config.extra.project_code }}          4 OUT_OF_ME+    0:125 
27323464.ex+     extern             {{ config.extra.project_code }}          4  COMPLETED      0:0 
```

To understand why our job failed, we need to talk about the resources involved.

Understanding the resources you have available and how to use them most efficiently is a vital skill in high performance computing.

Below is a table of common resources and issues you may face if you do not request the correct amount.

<table>
    <thead>
        <tr>
            <th>  </th>
            <th>Not enough</th>
            <th>Too Much</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>   CPU   </b></td>
            <td>The job will run more slowly than expected, and so may run out of time and get killed for exceeding its time limit.</td>
            <td>The job will wait in the queue for longer. <br>
             You will be charged for CPUs regardless of whether they are used or not.<br>
            Your fair share score will fall more.
           </td>
        </tr>
        <tr>
            <td><b>   Memory   </b></td>
            <td>Your job will fail, probably with an 'OUT OF MEMORY' error, segmentation fault or bus error (may not happen immediately).</td>
            <td>The job will wait in the queue for longer.<br>
             You will be charged for memory regardless of whether it is used or not.<br>
             Your fair share score will fall more.</td>
        </tr>
        <tr>
            <td><b>   Walltime   </b></td>
            <td>The job will run out of time and be terminated by the scheduler.</td>
            <td>The job will wait in the queue for longer.</td>
        </tr>
    </tbody>
</table>

## Measuring Resource Usage of a Finished Job

Since we have already run a job (successful or otherwise), this is the best source of info we currently have.
If we check the status of our finished job using the `sacct` command we learned earlier.

```sh
 sacct
```

```sh
JobID           JobName          Alloc     Elapsed     TotalCPU  ReqMem   MaxRSS State
--------------- ---------------- ----- ----------- ------------ ------- -------- ----------
31060451        example_job.sl       2    00:00:48    00:33.548      1G          CANCELLED
31060451.batch  batch                2    00:00:48    00:33.547          102048K CANCELLED
31060451.extern extern               2    00:00:48     00:00:00                0 CANCELLED
```

With this information, we may determine a couple of things.

Memory efficiency can be determined by comparing _ReqMem_ (requested memory) with _MaxRSS_ (maximum used memory), MaxRSS is  given in KB, so a unit conversion is usually required.

<br>

$$ {Efficiency_{mem} = { MaxRSS \over ReqMem}} $$

<br>

So for the above example we see that _0.1GB_ (102048K) of our requested _1GB_ meaning the memory efficincy was about _10%_.

CPU efficiency can be determined by comparing _TotalCPU_ (CPU time), with the maximum possible CPU time. The maximum possible CPU time equal to _Alloc_ (number of allocated CPUs) multiplied by _Elapsed_ (Walltime, actual time passed).

$$ {Efficiency_{cpu} = { TotalCPU \over {Elapsed \times Alloc}}} $$

For the above example _33 seconds_ of computation was done,

where the maximum possible computation time was **96 seconds** (_2 CPUs_ multiplied by _48 seconds_), meaning the CPU efficiency was about _35%_.

Time Efficiency is simply the _Elapsed Time_ divided by _Time Requested_.

$$ {Efficiency_{time} = { Elapsed \over Requested }} $$

_48 seconcds_ out of _15 minutes_ requested give a time efficiency of about _5%_

!!! question "Efficiency Exercise"
  Calculate for the job shown below,

  ```out
  JobID           JobName          Alloc     Elapsed     TotalCPU  ReqMem   MaxRSS State
  --------------- ---------------- ----- ----------- ------------ ------- -------- ----------
  37171050        Example-job          8    00:06:03     00:23:04     32G           FAILED
  37171050.batch  batch                8    00:06:03    23:03.999         14082672k FAILED
  37171050.extern extern               8    00:06:03    00:00.001                0  COMPLETED
  ```

  a. CPU efficiency.
  b. Memory efficiency.

  ??? question Solution
    a. CPU efficiency is `( 23 / ( 8 * 6 ) ) x 100` or around **48%**.
    b. Memory efficiency is `( 14 / 32 ) x 100` or around **43%**.

For convenience, NeSI has provided the command `nn_seff <jobid>` to calculate **S**lurm **Eff**iciency (all NeSI commands start with `nn_`, for **N**eSI **N**IWA).

```sh
 nn_seff <jobid>
```

```out
Job ID: 27323570
Cluster: mahuika
User/Group: username/username
State: COMPLETED (exit code 0)
Cores: 1
Tasks: 1
Nodes: 1
Job Wall-time:  5.11%  00:00:46 of 00:15:00 time limit
CPU Efficiency: 141.30%  00:01:05 of 00:00:46 core-walltime
Mem Efficiency: 93.31%  233.29 MB of 250.00 MB
```

Knowing what we do now about job efficiency, lets submit the previous job again but with more appropriate resources.

```sl
#!/bin/bash -e

#SBATCH --job-name      example_job
#SBATCH --account       nesi99991
#SBATCH --mem           300M
#SBATCH --time          00:15:00
#SBATCH --cpus-per-task 4

module purge
module load R/4.3.1-gimkl-2022a
Rscript sum_matrix.r
echo "Done!"
```

```sh
sbatch example_job.sl
```

Hopefully we will have better luck with this one!

### Simultaneous Multithreading (SMT)

Modern CPU cores have 2 threads of operation that can execute independently of one
another. SMT is the technology that allows the 2 threads within one physical core to present
as multiple logical cores, sometimes referred to as virtual CPUS (vCPUS).

For more details please see our
[documentation on SMT](../../Software/Parallel_Computing/Simultaneous_Multithreading.md)

## Measuring the System Load From Currently Running Tasks

On Mahuika, we allow users to connect directly to compute nodes from the
login node. This is useful to check on a running job and see how it's doing, however, we
only allow you to connect to nodes on which you have running jobs.

The most reliable way to check current system stats is with `htop`.
`htop` is an interactive process viewer that can be launched from command line.

### Finding job node

Before we can check on our job, we need to find out where it is running.
We can do this with the command `squeue --me`, and looking under the 'NODELIST' column.

```sh
squeue --me
```

```out
JOBID         USER     ACCOUNT   NAME        CPUS MIN_MEM PARTITI START_TIME     TIME_LEFT STATE    NODELIST(REASON)    
26763045      cwal219  {{config.extra.project_code}} test           2    512M large   May 11 11:35       14:46 RUNNING  wbn144 
```

Now that we know the location of the job (wbn189) we can use `ssh` to run `htop` _on that node_.

```sh
 ssh wbn189 -t htop -u $USER
```

You may get a message:

```sh
ECDSA key fingerprint is SHA256:############################################
ECDSA key fingerprint is MD5:9d:############################################
Are you sure you want to continue connecting (yes/no)?
```

If so, type `yes` and <kbd>Enter</kbd>

You may also need to enter your cluster password.

If you cannot connect, it may be that the job has finished and you have lost permission to `ssh` to that node.

### Reading Htop

You may see something like this,

```out
top - 21:00:19 up  3:07,  1 user,  load average: 1.06, 1.05, 0.96
Tasks: 311 total,   1 running, 222 sleeping,   0 stopped,   0 zombie
%Cpu(s):  7.2 us,  3.2 sy,  0.0 ni, 89.0 id,  0.0 wa,  0.2 hi,  0.2 si,  0.0 st
KiB Mem : 16303428 total,  8454704 free,  3194668 used,  4654056 buff/cache
KiB Swap:  8220668 total,  8220668 free,        0 used. 11628168 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 1693 jeff      20   0 4270580 346944 171372 S  29.8  2.1   9:31.89 gnome-shell
 3140 jeff      20   0 3142044 928972 389716 S  27.5  5.7  13:30.29 Web Content
 3057 jeff      20   0 3115900 521368 231288 S  18.9  3.2  10:27.71 firefox
 6007 jeff      20   0  813992 112336  75592 S   4.3  0.7   0:28.25 tilix
 1742 jeff      20   0  975080 164508 130624 S   2.0  1.0   3:29.83 Xwayland
    1 root      20   0  230484  11924   7544 S   0.3  0.1   0:06.08 systemd
   68 root      20   0       0      0      0 I   0.3  0.0   0:01.25 kworker/4:1
 2913 jeff      20   0  965620  47892  37432 S   0.3  0.3   0:11.76 code
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.02 kthreadd
```

Overview of the most important fields:

- `PID`: What is the numerical id of each process?
- `USER`: Who started the process?
- `RES`: What is the amount of memory currently being used by a process (in
  bytes)?
- `%CPU`: How much of a CPU is each process using? Values higher than 100
  percent indicate that a process is running in parallel.
- `%MEM`: What percent of system memory is a process using?
- `TIME+`: How much CPU time has a process used so far? Processes using 2 CPUs
  accumulate time at twice the normal rate.
- `COMMAND`: What command was used to launch a process?

To exit press <kbd>q</kbd>.

Running this command as is will show us information on tasks running on the login node (where we should not be running resource intensive jobs anyway).

## Running Test Jobs

As you may have to run several iterations before you get it right, you should choose your test job carefully.
A test job should not run for more than 15 minutes. This could involve using a smaller input, coarser parameters or using a subset of the calculations.
As well as being quick to run, you want your test job to be quick to start (e.g. get through queue quickly), the best way to ensure this is keep the resources requested (memory, CPUs, time) small.
Similar as possible to actual jobs e.g. same functions etc.
Use same workflow. (most issues are caused by small issues, typos, missing files etc, your test job is a good chance to sort out these issues.).
Make sure outputs are going somewhere you can see them.

!!! tip "Serial Test"
  Often a good first test to run, is to execute your job _serially_ e.g. using only 1 CPU.
  This not only saves you time by being fast to start, but serial jobs can often be easier to debug.
  If you confirm your job works in its most simple state you can identify problems caused by
  paralellistaion much more easily.

You generally should ask for 20% to 30% more time and memory than you think the job will use.
Testing allows you to become more more precise with your resource requests. We will cover a bit more on running tests in the last lesson.

## Efficient way to run tests jobs using debug QOS (Quality of Service)

Before submitting a large job, first submit one as a test to make
sure everything works as expected. Often, users discover typos in their submit
scripts, incorrect module names or possibly an incorrect path name after their job
has queued for many hours. Be aware that your job is not fully scanned for
correctness when you submit the job. While you may get an immediate error if your
`#SBATCH` directives are malformed, it is not until the job starts to run that the
interpreter starts to process the batch script.
NeSI has an easy way for you to test your job submission.  One can employ the debug
QOS to get a short, high priority test job. Debug jobs have to run within 15
minutes and cannot use more that 2 nodes. To use debug QOS, add or change the
following in your batch submit script

```sh
#SBATCH --qos=debug
#SBATCH --time=15:00
```

Adding these SBATCH directives will provide your job with the highest priority
possible, meaning it should start to run within a few minutes, provided
your resource request is not too large.

## Initial Resource Requirements

As we have just discussed, the best and most reliable method of determining resource requirements is from testing,
but before we run our first test there are a couple of things you can do to start yourself off in the right area.

### Read the Documentation

NeSI maintains documentation  that does have some guidance on using resources for some software
However, as you noticed in the Modules lessons, we have a lot of software.  So it is also advised to search
the web for others that may have written up guidance for getting the most out of your specific software.

### Ask Other Users

If you know someone who has used the software before, they may be able to give you a ballpark figure.

<!-- Now that you know the efficiency of your small test job what next? Throw 100 more CPUs at the problem for 100x speedup? -->

!!! postrequisite "Next Steps"
    You can use this knowledge to set up the
    next job with a closer estimate of its load on the system.
    A good general rule
    is to ask the scheduler for **30%** more time and memory than you expect the
    job to need.

!!! keypoints
    - As your task gets larger, so does the potential for inefficiencies.
    - The smaller your job (time, CPUs, memory, etc), the faster it will schedule.
