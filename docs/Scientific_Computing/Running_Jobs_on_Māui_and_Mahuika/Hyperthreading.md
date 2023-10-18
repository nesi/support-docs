---
created_at: '2018-11-15T22:10:10Z'
hidden: false
label_names: []
position: 16
title: Hyperthreading
vote_count: 6
vote_sum: -4
zendesk_article_id: 360000568236
zendesk_section_id: 360000030876
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
 !!! Info
     This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
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

Hyperthreading is enabled by default on NeSI machines, meaning, by
default, Slurm will allocate two threads to each physical core. 

# Hyperthreading with slurm

When Slurm request a CPU, it is **requesting logical cores,** which, as
mentioned above, there are two of per physical core. If you use
`--ntasks=n` to request CPUs, Slurm will start `n` MPI tasks which are
each assigned to one physical core. Since Slurm "sees" logical cores,
once your job starts you will have twice the number of CPUs as `ntasks`.

If you set `--cpus-per-task=n`, Slurm will request `n` logical CPUs per
task, i.e., will set `n` threads for the job. Your code must be capable
of running Hyperthreaded (for example using
[OpenMP](https://support.nesi.org.nz/hc/en-gb/articles/360001070496)) if
`--cpus-per-task > 1`.

 

Setting `--hint=nomultithread` with srun or sbatch "causes Slurm to
allocate only one thread from each core to this job". This will allocate
CPUs according to the following image:

<table style="height: 132px;" data-border="1" width="591"
data-cellspacing="0" data-cellpadding="3">
<tbody>
<tr class="odd" style="height: 22px;">
<td style="height: 22px; width: 164.389px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>Node
name</strong></font></p></td>
<td colspan="16" style="height: 22px; width: 403.878px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>wbn009</strong></font></p></td>
</tr>
<tr class="even" style="height: 22px;">
<td style="height: 22px; width: 164.389px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>Physical Core
id</strong></font></p></td>
<td colspan="2" style="height: 22px; width: 37.2727px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>0</strong></font></p></td>
<td colspan="2" style="height: 22px; width: 37.2727px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>1</strong></font></p></td>
<td colspan="2" style="height: 22px; width: 37.2727px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>2</strong></font></p></td>
<td colspan="2" style="height: 22px; width: 37.2727px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>3</strong></font></p></td>
<td colspan="2" style="height: 22px; width: 37.2727px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>0</strong></font></p></td>
<td colspan="2" style="height: 22px; width: 47.358px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>1</strong></font></p></td>
<td colspan="2" style="height: 22px; width: 47.358px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>2</strong></font></p></td>
<td colspan="2" style="height: 22px; width: 46.4347px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>3</strong></font></p></td>
</tr>
<tr class="odd" style="height: 22px;">
<td style="height: 22px; width: 164.389px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>Logical CPU
id</strong></font></p></td>
<td style="height: 22px; width: 13.1818px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>0</strong></font></p></td>
<td style="height: 22px; width: 13.1818px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>1</strong></font></p></td>
<td style="height: 22px; width: 13.1818px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>2</strong></font></p></td>
<td style="height: 22px; width: 13.1818px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>3</strong></font></p></td>
<td style="height: 22px; width: 13.1818px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>4</strong></font></p></td>
<td style="height: 22px; width: 13.1818px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>5</strong></font></p></td>
<td style="height: 22px; width: 13.1818px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>6</strong></font></p></td>
<td style="height: 22px; width: 13.1818px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>7</strong></font></p></td>
<td style="height: 22px; width: 13.1818px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>8</strong></font></p></td>
<td style="height: 22px; width: 13.1818px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>9</strong></font></p></td>
<td style="height: 22px; width: 18.2244px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>10</strong></font></p></td>
<td style="height: 22px; width: 18.2244px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>11</strong></font></p></td>
<td style="height: 22px; width: 18.2244px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>12</strong></font></p></td>
<td style="height: 22px; width: 18.2244px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>13</strong></font></p></td>
<td style="height: 22px; width: 18.2244px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>14</strong></font></p></td>
<td style="height: 22px; width: 17.3011px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>15</strong></font></p></td>
</tr>
<tr class="even" style="height: 22px;">
<td style="height: 22px; width: 164.389px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>Number of Allocated
CPUs</strong></font></p></td>
<td colspan="8"
style="height: 22px; width: 181.818px"><p><font size="1">4</font></p></td>
<td colspan="8"
style="height: 22px; width: 211.151px"><p><font size="1">4</font></p></td>
</tr>
<tr class="odd" style="height: 22px;">
<td style="height: 22px; width: 164.389px"
data-bgcolor="#e0e0e0"><p><font size="1"><strong>Allocated CPU
ids</strong></font></p></td>
<td colspan="8"
style="height: 22px; width: 181.818px"><p><font size="1">0 2 4
6</font></p></td>
<td colspan="8"
style="height: 22px; width: 211.151px"><p><font size="1">8 10 12
14</font></p></td>
</tr>
</tbody>
</table>

Image adapted from [Slurm's documentation
page](https://slurm.schedmd.com/cpu_management.html).

# When to use Hyperthreading

Hyperthreading increases the efficiency of some jobs, but the fact that
Slurm is counting in logical CPUs makes aspects of running
non-Hyperthreaded jobs confusing, even when Hyperthreading is turned off
in the job with `--hint=nomultithread`. To determine if the code you are
running is capable of running Hyperthreaded, visit the manual pages for
the software.

Alternatively, it is possible to perform an ad-hoc test to determine if
your code is capable of making use of Hyperthreading. First run a job
that has requested 2 threads per physical core as described above. Then,
use the `nn_seff` command to check the jobs CPU efficiency. If CPU
efficiency is greater than 100%, then your code is making use of
Hyperthreading, and gaining performance from it. If your job gives an
error or stays at 100% efficiency, it is likely you can not run your
code Hyperthreaded. 200% CPU efficiency would be the maximally efficient
job, however, this is rarely observed and anything over 100% should be
considered a bonus.

# How to use Hyperthreading

-   Non-hyperthreaded jobs which use  `--mem-per-cpu` requests should
    halve their memory requests as those are based on memory per logical
    CPU, not per the number of threads or tasks.  For non-MPI jobs, or
    for MPI jobs that request the same number of tasks on every node, we
    recommend to specify `--mem` (i.e. memory per node) instead. See
    [How to request memory
    (RAM)](https://support.nesi.org.nz/hc/en-gb/articles/360001108756)
    for more information.
-   Non-MPI jobs which specify `--cpus-per-task` and use **srun** should
    also set `--ntasks=1`, otherwise the program will be run twice in
    parallel, halving the efficiency of the job.

The precise rules about when Hyperthreading applies are as follows:

<table style="width: 697px;">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="header">
<th style="width: 109px"> </th>
<th class="wysiwyg-text-align-center" style="width: 205px">Mahuika</th>
<th class="wysiwyg-text-align-center" style="width: 376px">Māui</th>
</tr>
&#10;<tr class="odd">
<td style="width: 109px">Jobs</td>
<td colspan="2" class="wysiwyg-text-align-center"
style="width: 581px">Never share physical cores</td>
</tr>
<tr class="even">
<td style="width: 109px">MPI tasks within the same job</td>
<td class="wysiwyg-text-align-center" style="width: 205px">Never share
physical cores</td>
<td class="wysiwyg-text-align-center" style="width: 376px">Share
physical cores by default. You can override this behaviour by using
<code>--hint=nomultithread</code> in your job submission script.</td>
</tr>
<tr class="odd">
<td style="width: 109px">Threads within the same task</td>
<td colspan="2" class="wysiwyg-text-align-center"
style="width: 581px">Share physical cores by default. You can override
this behaviour by using<br />
<code>--hint=nomultithread</code> in your job submission script.</td>
</tr>
</tbody>
</table>

 

## How many logical CPUs will my job use or be charged for?

The possible job configurations and their results are shown in the
following table. We have also included some recommendations to help you
make the best choices, depending on the needs of your workflow.

<table style="width: 697px;">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="header">
<th class="wysiwyg-text-align-center" style="width: 221px">Job
configuration</th>
<th class="wysiwyg-text-align-center" style="width: 237px">Mahuika</th>
<th class="wysiwyg-text-align-center" style="width: 232px">Māui</th>
</tr>
&#10;<tr class="odd">
<td style="width: 221px"><ul>
<li>Only one task</li>
<li><code>--cpus-per-task</code> is not used</li>
</ul></td>
<td class="wysiwyg-text-align-center" style="width: 237px">The job gets,
and is charged for, two logical CPUs. <code>--hint=nomultithread</code>
is irrelevant.</td>
<td class="wysiwyg-text-align-center" style="width: 232px"><p>The job
gets one logical CPU, but is charged for 80.<br />
<code>--hint=nomultithread</code> is irrelevant.</p>
<p><span><strong>This configuration is extremely uneconomical on Māui.
Consider using Mahuika or the Māui ancillary nodes
instead.</strong></span></p></td>
</tr>
<tr class="even">
<td style="width: 221px"><ul>
<li>Only one task</li>
<li><code>--cpus-per-task=</code><em>N</em></li>
<li><code>--hint=nomultithread</code> is not used</li>
</ul></td>
<td class="wysiwyg-text-align-center" style="width: 237px"><p>The job
gets, and is charged for, <em>N</em> logical CPUs, rounded up to the
nearest even number.</p>
<p><strong>Set <em>N</em> to an even number if
possible.</strong></p></td>
<td class="wysiwyg-text-align-center" style="width: 232px"><p>The job
gets <em>N</em> logical CPUs, but is charged for 80.</p>
<p><strong>Set <em>N</em> to 80 if possible.</strong></p></td>
</tr>
<tr class="odd">
<td style="width: 221px"><ul>
<li>Only one task</li>
<li><code>--cpus-per-task=</code><em>N</em></li>
<li><code>--hint=nomultithread</code> is used</li>
</ul></td>
<td class="wysiwyg-text-align-center" style="width: 237px">The job gets,
and is charged for, 2<em>N</em> logical CPUs.</td>
<td class="wysiwyg-text-align-center" style="width: 232px"><p>The job
gets 2<em>N</em> logical CPUs, but is charged for 80.</p>
<p><strong>Set <em>N</em> to 40 if possible.</strong></p></td>
</tr>
<tr class="even">
<td style="width: 221px"><ul>
<li>More than one task on one or more nodes</li>
<li><code>--cpus-per-task</code> is not used</li>
<li><code>--hint=nomultithread</code> is not used</li>
</ul></td>
<td rowspan="2" class="wysiwyg-text-align-center"
style="width: 237px"><p>Each task gets two logical CPUs. The job is
charged for two logical CPUs per task. <code>--hint=nomultithread</code>
is irrelevant.</p>
<p> </p></td>
<td class="wysiwyg-text-align-center" style="width: 232px"><p>Each task
gets one logical CPU. The job is charged for 80 logical CPUs per
allocated node.</p>
<p><strong>If possible, set the number of tasks per node to
80.</strong></p></td>
</tr>
<tr class="odd">
<td style="width: 221px"><ul>
<li>More than one task on one or more nodes</li>
<li><code>--cpus-per-task</code> is not used</li>
<li><code>--hint=nomultithread</code> is used</li>
</ul></td>
<td class="wysiwyg-text-align-center" style="width: 232px"><p>Each task
gets two logical CPUs. The job is charged for 80 logical CPUs per
allocated node.</p>
<p><strong>If possible, set the number of tasks per node to
40.</strong> </p></td>
</tr>
<tr class="even">
<td style="width: 221px"><ul>
<li>More than one task on one or more nodes</li>
<li><code>--cpus-per-task=</code><em>N</em></li>
<li><code>--hint=nomultithread</code> is not used</li>
</ul></td>
<td class="wysiwyg-text-align-center" style="width: 237px"><p>Each task
gets <em>N</em> logical CPUs, rounded up to the nearest even number. The
job is charged for that number of logical CPUs per task.</p>
<p><strong>Set <em>N</em> to an even number if
possible.</strong></p></td>
<td class="wysiwyg-text-align-center" style="width: 232px"><p>Each task
gets <em>N</em> logical CPUs. The job is charged for 80 logical CPUs per
allocated node.</p>
<p><strong>If possible, set <em>N</em> and the number of tasks per node
such that <em>N</em> × (tasks per node) = 80.</strong></p></td>
</tr>
<tr class="odd">
<td style="width: 221px"><ul>
<li>More than one task on one or more nodes</li>
<li><code>--cpus-per-task=</code><em>N</em></li>
<li><code>--hint=nomultithread</code> is used</li>
</ul></td>
<td class="wysiwyg-text-align-center" style="width: 237px">Each task
gets 2<em>N</em> logical CPUs. The job is charged for 2<em>N</em>
logical CPUs per task.</td>
<td class="wysiwyg-text-align-center" style="width: 232px"><p>Each task
gets 2<em>N</em> logical CPUs. The job is charged for 80 logical CPUs
per allocated node.</p>
<p><strong>If possible, set <em>N</em> and the number of tasks per node
such that <em>N</em> × (tasks per node) = 40.</strong></p></td>
</tr>
</tbody>
</table>

 
