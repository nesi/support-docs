---
created_at: '2018-11-15T22:10:10Z'
hidden: false
position: 16
tags: []
title: Hyperthreading
vote_count: 6
vote_sum: -4
zendesk_article_id: 360000568236
zendesk_section_id: 360000030876
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
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

## Hyperthreading with slurm

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

|                                                    |                                  |                             |                             |                             |                             |                             |                             |                             |                                  |                             |                              |                              |                              |                              |                              |                              |
|----------------------------------------------------|----------------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|----------------------------------|-----------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|
| <font size="1">**Node name**</font>                | <font size="1">**wbn009**</font> |                             |                             |                             |                             |                             |                             |                             |                                  |                             |                              |                              |                              |                              |                              |                              |
| <font size="1">**Physical Core id**</font>         | <font size="1">**0**</font>      |                             | <font size="1">**1**</font> |                             | <font size="1">**2**</font> |                             | <font size="1">**3**</font> |                             | <font size="1">**0**</font>      |                             | <font size="1">**1**</font>  |                              | <font size="1">**2**</font>  |                              | <font size="1">**3**</font>  |                              |
| <font size="1">**Logical CPU id**</font>           | <font size="1">**0**</font>      | <font size="1">**1**</font> | <font size="1">**2**</font> | <font size="1">**3**</font> | <font size="1">**4**</font> | <font size="1">**5**</font> | <font size="1">**6**</font> | <font size="1">**7**</font> | <font size="1">**8**</font>      | <font size="1">**9**</font> | <font size="1">**10**</font> | <font size="1">**11**</font> | <font size="1">**12**</font> | <font size="1">**13**</font> | <font size="1">**14**</font> | <font size="1">**15**</font> |
| <font size="1">**Number of Allocated CPUs**</font> | <font size="1">4</font>          |                             |                             |                             |                             |                             |                             |                             | <font size="1">4</font>          |                             |                              |                              |                              |                              |                              |                              |
| <font size="1">**Allocated CPU ids**</font>        | <font size="1">0 2 4 6</font>    |                             |                             |                             |                             |                             |                             |                             | <font size="1">8 10 12 14</font> |                             |                              |                              |                              |                              |                              |                              |

Image adapted from [Slurm's documentation
page](https://slurm.schedmd.com/cpu_management.html).

## When to use Hyperthreading

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

## How to use Hyperthreading

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

----------------------- ------------------------ ------------------------
Mahuika                  Māui

Jobs                    Never share physical
cores

MPI tasks within the    Never share physical     Share physical cores by
same job                cores                    default. You can
override this behaviour
by using
`--hint=nomultithread`
in your job submission
script.

Threads within the same Share physical cores by
task                    default. You can
override this behaviour
by using
`--hint=nomultithread`
in your job submission
script.
----------------------- ------------------------ ------------------------



### How many logical CPUs will my job use or be charged for?

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
<li><code class="sl">--cpus-per-task</code> is not used</li>
</ul></td>
<td class="wysiwyg-text-align-center" style="width: 237px">The job gets,
and is charged for, two logical CPUs. <code
class="sl">--hint=nomultithread</code> is irrelevant.</td>
<td class="wysiwyg-text-align-center" style="width: 232px"><p>The job
gets one logical CPU, but is charged for 80.<br />
<code class="sl">--hint=nomultithread</code> is irrelevant.</p>
<p><span><strong>This configuration is extremely uneconomical on Māui.
Consider using Mahuika or the Māui ancillary nodes
instead.</strong></span></p></td>
</tr>
<tr class="even">
<td style="width: 221px"><ul>
<li>Only one task</li>
<li><code class="sl">--cpus-per-task=</code><em>N</em></li>
<li><code class="sl">--hint=nomultithread</code> is not used</li>
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
<li><code class="sl">--cpus-per-task=</code><em>N</em></li>
<li><code class="sl">--hint=nomultithread</code> is used</li>
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
<li><code class="sl">--cpus-per-task</code> is not used</li>
<li><code class="sl">--hint=nomultithread</code> is not used</li>
</ul></td>
<td rowspan="2" class="wysiwyg-text-align-center"
style="width: 237px"><p>Each task gets two logical CPUs. The job is
charged for two logical CPUs per task. <code
class="sl">--hint=nomultithread</code> is irrelevant.</p>
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
<li><code class="sl">--cpus-per-task</code> is not used</li>
<li><code class="sl">--hint=nomultithread</code> is used</li>
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
<li><code class="sl">--cpus-per-task=</code><em>N</em></li>
<li><code class="sl">--hint=nomultithread</code> is not used</li>
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
<li><code class="sl">--cpus-per-task=</code><em>N</em></li>
<li><code class="sl">--hint=nomultithread</code> is used</li>
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

