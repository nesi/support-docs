---
created_at: '2018-11-15T22:10:10Z'
tags:
  - hyperthreading
  - hyper-threading
  - smp
  - symmetric multiprocessing
  - simultaneous multithreading
  - shared-memory multiprocessing
description: How to use simultaneous multithreading (hyper-threading) on NeSI.
---

!!! note
    'Hyperthreading' is the name of the Intel proprietory implimentation of [Simultaneous Multithreading](https://en.wikipedia.org/wiki/Simultaneous_multithreading) (SMP).
    For consistancy, and because it is better recognised we use the 

!!! warning
    The presence of hyperthreading on the HPC results in Slurm falsely detecting twice the number of 
    CPUs being assigned to all jobs than is actually assigned, even when hyperthreading is disabled,
    this can seen in the outputs of commands such as `sacct`. However, your jobs are still only being
    charged for the acutal number of assigned CPUs.

As CPU technology advanced engineers realised that adapting CPU
architecture to include *logical* *processors* within the physical core
(conventionally, a CPU) allows some computation to occur simultaneously.
The name for this technology is *simultaneous multithreading*, and
Intel's implementation of it is called
[Hyperthreading](https://en.wikipedia.org/wiki/Hyper-threading).

CPUs capable of Hyperthreading consists of two logical processors per
physical core. The logical processors can operate on data/instruction
*threads* simultaneously, meaning the physical core can perform two
operations concurrently. In other words, the difference between logical
and physical cores is that logical cores are not full stand-alone CPUs,
and share some hardware with nearby logical cores. Physical cores are
made up of two logical cores.

Hyperthreading is disabled by default on REANNZ HPC, meaning, by
default, Slurm will allocate one thread to each physical core.
However, it can be enabled by adding `--threads-per-core=2` to your 
Slurm script, which will result in Slurm allocating two threads to 
each physical core.

## Hyperthreading with Slurm

When Slurm requests a CPU, it is **requesting logical cores,** which, as
mentioned above, there are two of per physical core. If you use
`--ntasks=n` to request CPUs, Slurm will start `n` MPI tasks which are
each assigned to one physical core. Since Slurm "sees" logical cores,
once your job starts you will have twice the number of cores as `ntasks`,
even when hyperthreading is disabled. If hyperthreading is disabled only
one thread of work will be allocated physical core, meaning one logical core
on each physical core will remain idle.

With hyperthreading disabled, if you set `--cpus-per-task=n`, Slurm will 
request `n` physical core per task, but because each physical core consists
of two logical cores you will be allocated 2n logical cores but only one
thread of work will be allocated physical core, meaning one logical core
on each physical core will remain idle.

If you set `--cpus-per-task=n`while hyperthreading is enabled, Slurm will
request `n` logical cores per task, i.e., will set `n` threads for the job.
Your code must be capable of running Hyperthreaded (for example using
[OpenMP](OpenMP_settings.md))
if `--cpus-per-task > 1`.

Below you can find a table of a hypothetical node. Regardless of whether you have
hyperthreading enabled or disabled your jobs will always be assigned full physical
cores and the corresponding logical cores. If hyperthreading is disabled your jobs
will only use one of the available logical core on each physical core.
<table style="height: 132px;" border="1" width="591" cellspacing="0" cellpadding="3">
<tbody>
<tr style="height: 22px;">
<td style="height: 22px; width: 164.389px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>Node name</strong></font></p>
</td>
<td style="height: 22px; width: 403.878px;" colspan="16" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>wbn009</strong></font></p>
</td>
</tr>
<tr style="height: 22px;">
<td style="height: 22px; width: 164.389px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>Physical Core id</strong></font></p>
</td>
<td style="height: 22px; width: 37.2727px;" colspan="2" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>0</strong></font></p>
</td>
<td style="height: 22px; width: 37.2727px;" colspan="2" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>1</strong></font></p>
</td>
<td style="height: 22px; width: 37.2727px;" colspan="2" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>2</strong></font></p>
</td>
<td style="height: 22px; width: 37.2727px;" colspan="2" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>3</strong></font></p>
</td>
<td style="height: 22px; width: 37.2727px;" colspan="2" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>0</strong></font></p>
</td>
<td style="height: 22px; width: 47.358px;" colspan="2" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>1</strong></font></p>
</td>
<td style="height: 22px; width: 47.358px;" colspan="2" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>2</strong></font></p>
</td>
<td style="height: 22px; width: 46.4347px;" colspan="2" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>3</strong></font></p>
</td>
</tr>
<tr style="height: 22px;">
<td style="height: 22px; width: 164.389px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>Logical CPU id</strong></font></p>
</td>
<td style="height: 22px; width: 13.1818px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>0</strong></font></p>
</td>
<td style="height: 22px; width: 13.1818px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>1</strong></font></p>
</td>
<td style="height: 22px; width: 13.1818px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>2</strong></font></p>
</td>
<td style="height: 22px; width: 13.1818px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>3</strong></font></p>
</td>
<td style="height: 22px; width: 13.1818px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>4</strong></font></p>
</td>
<td style="height: 22px; width: 13.1818px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>5</strong></font></p>
</td>
<td style="height: 22px; width: 13.1818px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>6</strong></font></p>
</td>
<td style="height: 22px; width: 13.1818px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>7</strong></font></p>
</td>
<td style="height: 22px; width: 13.1818px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>8</strong></font></p>
</td>
<td style="height: 22px; width: 13.1818px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>9</strong></font></p>
</td>
<td style="height: 22px; width: 18.2244px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>10</strong></font></p>
</td>
<td style="height: 22px; width: 18.2244px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>11</strong></font></p>
</td>
<td style="height: 22px; width: 18.2244px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>12</strong></font></p>
</td>
<td style="height: 22px; width: 18.2244px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>13</strong></font></p>
</td>
<td style="height: 22px; width: 18.2244px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>14</strong></font></p>
</td>
<td style="height: 22px; width: 17.3011px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>15</strong></font></p>
</td>
</tr>
<tr style="height: 22px;">
<td style="height: 22px; width: 164.389px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>Number of Allocated CPUs</strong></font></p>
</td>
<td style="height: 22px; width: 181.818px;" colspan="8">
<p align="CENTER"><font size="1">4</font></p>
</td>
<td style="height: 22px; width: 211.151px;" colspan="8">
<p align="CENTER"><font size="1">4</font></p>
</td>
</tr>
<tr style="height: 22px;">
<td style="height: 22px; width: 164.389px;" bgcolor="#e0e0e0">
<p align="CENTER"><font size="1"><strong>Allocated CPU ids</strong></font></p>
</td>
<td style="height: 22px; width: 181.818px;" colspan="8">
<p align="CENTER"><font size="1">0 2 4 6</font></p>
</td>
<td style="height: 22px; width: 211.151px;" colspan="8">
<p align="CENTER"><font size="1">8 10 12 14</font></p>
</td>
</tr>
</tbody>
</table>

Image adapted from [Slurm's documentation page](https://slurm.schedmd.com/archive/{{config.extra.slurm}}/cpu_management.html).

## When to use Hyperthreading

Hyperthreading increases the efficiency of some jobs, but the fact that
Slurm is counting in logical CPUs makes aspects of running
non-Hyperthreaded jobs confusing, even when Hyperthreading is turned off
in the job. To determine if the code you are
running is capable of running Hyperthreaded, visit the manual pages for
the software.

Alternatively, it is possible to perform an ad-hoc test to determine if
your code is capable of making use of Hyperthreading. First run a job
that has requested `--cpus-per-task=2` and `--threads-per-core=2`. Then,
use the `nn_seff` command to check the jobs CPU efficiency. If CPU
efficiency is greater than 100%, then your code is making use of
Hyperthreading, and may be gaining performance from it. If your job gives an
error or stays at 100% efficiency, it is likely you can not run your
code Hyperthreaded. 200% CPU efficiency would be the maximally efficient
job, however, this is rarely observed and anything over 100% should be
considered a bonus. Additioanlly, a job may appear to be getting a
performance boost from hyperthreading, but to confirm this boost you will 
need to compare the runtime of this job to another job with the same number
of physical cores but without having hyperthreading enabled.

## How to use Hyperthreading

- In non-hyperthreaded jobs `cpu` as in `--mem-per-cpu` or `cpus-per-task` requests should
    refers to the physical core. However, if hyperthreading is enabled `cpu` now refers to
    the logical core.  For non-MPI jobs, or for MPI jobs that request the same number of
    tasks on every node, we recommend to specify `--mem` (i.e. memory per node) instead.
    See [How to request memory
    (RAM)](../../Getting_Started/FAQs/How_do_I_request_memory.md) for more
    information.
- Non-MPI jobs which specify `--cpus-per-task` and use **srun** should
    also set `--ntasks=1`, otherwise the program will be run twice in
    parallel, halving the efficiency of the job.

The precise rules about when Hyperthreading applies are as follows:
<table style="width: 697px;">
<tbody>
<tr>
<th style="width: 109px;">&nbsp;</th>
<th class="wysiwyg-text-align-center" style="width: 205px;">Mahuika</th>
<th class="wysiwyg-text-align-center" style="width: 376px;">Māui</th>
</tr>
<tr>
<td style="width: 109px;">Jobs</td>
<td class="wysiwyg-text-align-center" style="width: 581px;" colspan="2">Never share physical cores</td>
</tr>
<tr>
<td style="width: 109px;">MPI tasks within the same job</td>
<td class="wysiwyg-text-align-center" style="width: 205px;">Never share physical cores</td>
<td class="wysiwyg-text-align-center" style="width: 376px;">Share physical cores by default. You can override this behaviour by using <code>--hint=nomultithread</code> in your job submission script.</td>
</tr>
<tr>
<td style="width: 109px;">Threads within the same task</td>
<td class="wysiwyg-text-align-center" style="width: 581px;" colspan="2">Share physical cores by default. You can override this behaviour by using<br><code>--hint=nomultithread</code> in your job submission script.</td>
</tr>
</tbody>
</table>

### How many logical CPUs will my job use or be charged for?

The possible job configurations and their results are shown in the
following table. We have also included some recommendations to help you
make the best choices, depending on the needs of your workflow.

<table>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<tbody>
<tr class="header">
<th>Job
configuration</th>
<th>Mahuika</th>
<th>Māui</th>
</tr>
<tr>
<td><ul>
<li>Only one task</li>
<li><code class="sl">--cpus-per-task</code> is not used</li>
</ul></td>
<td>The job gets,
and is charged for, two logical CPUs. <code class="sl">--threads-per-core=2</code> is irrelevant.</td>
<td>The job
gets one logical CPU, but is charged for 80.<br />
<code class="sl">--hint=nomultithread</code> is irrelevant.
<span>This configuration is extremely uneconomical on Māui.
Consider using Mahuika or the Māui ancillary nodes
instead.</span></td>
</tr>
<tr>
<td><ul>
<li>Only one task</li>
<li><code class="sl">--cpus-per-task=</code><em>N</em></li>
<li><code class="sl">--threads-per-cpu=2</code> is used</li>
</ul></td>
<td>The job
gets, and is charged for, <em>N</em> logical CPUs, rounded up to the
nearest even number.
Set <em>N</em> to an even number if
possible.</td>
<td>The job gets <em>N</em> logical CPUs, but is charged for 80.
Set <em>N</em> to 80 if possible.</td>
</tr>
<tr>
<td><ul>
<li>Only one task</li>
<li><code class="sl">--cpus-per-task=</code><em>N</em></li>
<li><code class="sl">--threads-per-cpu=2</code> is not used</li>
</ul></td>
<td>The job gets,
and is charged for, 2<em>N</em> logical CPUs.</td>
<td>The job
gets 2<em>N</em> logical CPUs, but is charged for 80.
Set <em>N</em> to 40 if possible.</td>
</tr>
<tr>
<td><ul>
<li>More than one task on one or more nodes</li>
<li><code class="sl">--cpus-per-task</code> is not used</li>
<li><code class="sl">--threads-per-cpu=2</code> is used</li>
</ul></td>
<td rowspan="2">Each task gets two logical CPUs. The job is
charged for two logical CPUs per task. <code class="sl">--threads-per-cpu=2</code> is irrelevant.</td>
<td>Each task
gets one logical CPU. The job is charged for 80 logical CPUs per
allocated node. If possible, set the number of tasks per node to 80.</td>
</tr>
<tr>
<td><ul>
<li>More than one task on one or more nodes</li>
<li><code class="sl">--cpus-per-task</code> is not used</li>
<li><code class="sl">--threads-per-cpu=2</code> is not used</li>
</ul></td>
<td>Each task
gets two logical CPUs. The job is charged for 80 logical CPUs per
allocated node.
If possible, set the number of tasks per node to
40.</td>
</tr>
<tr>
<td><ul>
<li>More than one task on one or more nodes</li>
<li><code class="sl">--cpus-per-task=</code><em>N</em></li>
<li><code class="sl">--threads-per-cpu=2</code> is used</li>
</ul></td>
<td>Each task
gets <em>N</em> logical CPUs, rounded up to the nearest even number. The
job is charged for that number of logical CPUs per task.
<strong>Set <em>N</em> to an even number if
possible.</strong></td>
<td>Each task
gets <em>N</em> logical CPUs. The job is charged for 80 logical CPUs per
allocated node.
If possible, set <em>N</em> and the number of tasks per node
such that <em>N</em> × (tasks per node) = 80.</td>
</tr>
<tr>
<td><ul>
<li>More than one task on one or more nodes</li>
<li><code class="sl">--cpus-per-task=</code><em>N</em></li>
<li><code class="sl">--threads-per-cpu=2</code> is not used</li>
</ul></td>
<td>Each task
gets 2<em>N</em> logical CPUs. The job is charged for 2<em>N</em>
logical CPUs per task.</td>
<td>Each task
gets 2<em>N</em> logical CPUs. The job is charged for 80 logical CPUs
per allocated node.
If possible, set <em>N</em> and the number of tasks per node
such that <em>N</em> × (tasks per node) = 40.</td>
</tr>
</tbody>
</table>
