---
created_at: '2018-11-15T22:10:10Z'
hidden: false
label_names: []
position: 16
title: Hyperthreading
vote_count: 4
vote_sum: -2
zendesk_article_id: 360000568236
zendesk_section_id: 360000030876
---

[Hyperthreading](https://en.wikipedia.org/wiki/Hyper-threading) is
enabled on the NeSI machines, so for each physical CPU core, there are
two logical CPUs. This increases the efficiency of some multithreaded
jobs, but the fact that Slurm is counting in logical CPUs makes aspects
of running non-hyperthreaded jobs confusing, even when hyperthreading is
turned off in the job with **--hint=nomultithread.**

-   Non-hyperthreaded jobs which use  **--mem-per-cpu** requests should
    halve their memory requests as those are based on memory per logical
    CPU, not per the number of threads or tasks.  For non-MPI jobs, or
    for MPI jobs that request the same number of tasks on every node, we
    recommend to specify **--mem** (i.e. memory per node) instead. See
    [How to request memory
    (RAM)](https://support.nesi.org.nz/hc/en-gb/articles/360001108756)
    for more information.
-   Non-MPI jobs which specify **--cpus-per-task** and use **srun**
    should also set **--ntasks=1**, otherwise the program will be run
    twice in parallel, halving the efficiency of the job.

The precise rules about when hyperthreading applies are as follows:

<table style="width: 697px;">
<tbody>
<tr>
<th style="width: 109px;">

 

</th>
<th class="wysiwyg-text-align-center" style="width: 205px;">

Mahuika

</th>
<th class="wysiwyg-text-align-center" style="width: 376px;">

Māui

</th>
</tr>
<tr>
<td style="width: 109px;">

Jobs

</td>
<td class="wysiwyg-text-align-center" style="width: 581px;" colspan="2">

Never share physical cores

</td>
</tr>
<tr>
<td style="width: 109px;">

MPI tasks within the same job

</td>
<td class="wysiwyg-text-align-center" style="width: 205px;">

Never share physical cores

</td>
<td class="wysiwyg-text-align-center" style="width: 376px;">

Share physical cores by default. You can override this behaviour by
using `--hint=nomultithread` in your job submission script.

</td>
</tr>
<tr>
<td style="width: 109px;">

Threads within the same task

</td>
<td class="wysiwyg-text-align-center" style="width: 581px;" colspan="2">

Share physical cores by default. You can override this behaviour by
using  
`--hint=nomultithread` in your job submission script.

</td>
</tr>
</tbody>
</table>

## How many logical CPUs will my job use or be charged for?

The possible job configurations and their results are shown in the
following table. We have also included some recommendations to help you
make the best choices, depending on the needs of your workflow.

<table style="width: 697px;">
<tbody>
<tr>
<th class="wysiwyg-text-align-center" style="width: 221px;">

Job configuration

</th>
<th class="wysiwyg-text-align-center" style="width: 237px;">

Mahuika

</th>
<th class="wysiwyg-text-align-center" style="width: 232px;">

Māui

</th>
</tr>
<tr>
<td style="width: 221px;">

-   Only one task
-   `--cpus-per-task` is not used

</td>
<td class="wysiwyg-text-align-center" style="width: 237px;">

The job gets, and is charged for, two logical
CPUs. `--hint=nomultithread` is irrelevant.

</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">

The job gets one logical CPU, but is charged for 80.  
`--hint=nomultithread` is irrelevant.

<span class="wysiwyg-color-red">**This configuration is extremely
uneconomical on Māui. Consider using Mahuika or the Māui ancillary nodes
instead.**</span>

</td>
</tr>
<tr>
<td style="width: 221px;">

-   Only one task
-   `--cpus-per-task=`*N*
-   `--hint=nomultithread` is not used

</td>
<td class="wysiwyg-text-align-center" style="width: 237px;">

The job gets, and is charged for, *N* logical CPUs, rounded up to the
nearest even number.

**Set *N* to an even number if possible.**

</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">

The job gets *N* logical CPUs, but is charged for 80.

**Set *N* to 80 if possible.**

</td>
</tr>
<tr>
<td style="width: 221px;">

-   Only one task
-   `--cpus-per-task=`*N*
-   `--hint=nomultithread` is used

</td>
<td class="wysiwyg-text-align-center" style="width: 237px;">

The job gets, and is charged for, 2*N* logical CPUs.

</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">

The job gets 2*N* logical CPUs, but is charged for 80.

**Set *N* to 40 if possible.**

</td>
</tr>
<tr>
<td style="width: 221px;">

-   More than one task on one or more nodes
-   `--cpus-per-task` is not used
-   `--hint=nomultithread` is not used

</td>
<td class="wysiwyg-text-align-center" style="width: 237px;" rowspan="2">

Each task gets two logical CPUs. The job is charged for two logical CPUs
per task. `--hint=nomultithread` is irrelevant.

 

</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">

Each task gets one logical CPU. The job is charged for 80 logical CPUs
per allocated node.

**If possible, set the number of tasks per node to 80.**

</td>
</tr>
<tr>
<td style="width: 221px;">

-   More than one task on one or more nodes
-   `--cpus-per-task` is not used
-   `--hint=nomultithread` is used

</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">

Each task gets two logical CPUs. The job is charged for 80 logical CPUs
per allocated node.

**If possible, set the number of tasks per node to 40.** 

</td>
</tr>
<tr>
<td style="width: 221px;">

-   More than one task on one or more nodes
-   `--cpus-per-task=`*N*
-   `--hint=nomultithread` is not used

</td>
<td class="wysiwyg-text-align-center" style="width: 237px;">

Each task gets *N* logical CPUs, rounded up to the nearest even number.
The job is charged for that number of logical CPUs per task.

**Set *N* to an even number if possible.**

</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">

Each task gets *N* logical CPUs. The job is charged for 80 logical CPUs
per allocated node.

**If possible, set *N* and the number of tasks per node such that *N* ×
(tasks per node) = 80.**

</td>
</tr>
<tr>
<td style="width: 221px;">

-   More than one task on one or more nodes
-   `--cpus-per-task=`*N*
-   `--hint=nomultithread` is used

</td>
<td class="wysiwyg-text-align-center" style="width: 237px;">

Each task gets 2*N* logical CPUs. The job is charged for 2*N* logical
CPUs per task.

</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">

Each task gets 2*N* logical CPUs. The job is charged for 80 logical CPUs
per allocated node.

**If possible, set *N* and the number of tasks per node such that *N* ×
(tasks per node) = 40.**

</td>
</tr>
</tbody>
</table>

 
