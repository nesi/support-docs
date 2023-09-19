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
    <p><span style="font-weight: 400;"><a href="https://en.wikipedia.org/wiki/Hyper-threading" target="_self">Hyperthreading</a> is enabled on the NeSI machines, so for each physical CPU core, there are two logical CPUs. This increases the efficiency of some multithreaded jobs, but the fact that Slurm is counting in logical CPUs makes aspects of running non-hyperthreaded jobs confusing, even when hyperthreading is turned off in the job with </span><strong>--hint=nomultithread.</strong></p>
<ul>
<li style="font-weight: 400;">
<span style="font-weight: 400;">Non-hyperthreaded jobs which use  </span><strong>--mem-per-cpu</strong><span style="font-weight: 400;"> requests should halve their memory requests as those are based on memory per logical CPU, not per the number of threads or tasks.  For non-MPI jobs, or for MPI jobs that request the same number of tasks on every node, we recommend to specify <strong>--mem</strong> (i.e. memory per node) instead. See <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001108756" target="_self">How to request memory (RAM)</a> for more information.</span>
</li>
<li style="font-weight: 400;">
<span style="font-weight: 400;">Non-MPI jobs which specify </span><strong>--cpus-per-task</strong><span style="font-weight: 400;"> and use </span><strong>srun </strong><span style="font-weight: 400;">should also set </span><strong>--ntasks=1</strong><span style="font-weight: 400;">, otherwise the program will be run twice in parallel, halving the efficiency of the job.</span>
</li>
</ul>
<p><span style="font-weight: 400;">The precise rules about when hyperthreading applies are as follows:</span></p>
<table style="width: 697px;">
<tbody>
<tr>
<th style="width: 109px;"> </th>
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
<td class="wysiwyg-text-align-center" style="width: 581px;" colspan="2">Share physical cores by default. You can override this behaviour by using<br> <code>--hint=nomultithread</code> in your job submission script.</td>
</tr>
</tbody>
</table>
<h2>How many logical CPUs will my job use or be charged for?</h2>
<p>The possible job configurations and their results are shown in the following table. We have also included some recommendations to help you make the best choices, depending on the needs of your workflow.</p>
<table style="width: 697px;">
<tbody>
<tr>
<th class="wysiwyg-text-align-center" style="width: 221px;">Job configuration</th>
<th class="wysiwyg-text-align-center" style="width: 237px;">Mahuika</th>
<th class="wysiwyg-text-align-center" style="width: 232px;">Māui</th>
</tr>
<tr>
<td style="width: 221px;">
<ul>
<li>Only one task</li>
<li>
<code>--cpus-per-task</code> is not used</li>
</ul>
</td>
<td class="wysiwyg-text-align-center" style="width: 237px;">The job gets, and is charged for, two logical CPUs. <code>--hint=nomultithread</code> is irrelevant.</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">
<p>The job gets one logical CPU, but is charged for 80.<br> <code>--hint=nomultithread</code> is irrelevant.</p>
<p><span class="wysiwyg-color-red"><strong>This configuration is extremely uneconomical on Māui. Consider using Mahuika or the Māui ancillary nodes instead.</strong></span></p>
</td>
</tr>
<tr>
<td style="width: 221px;">
<ul>
<li>Only one task</li>
<li>
<code>--cpus-per-task=</code><em>N</em>
</li>
<li>
<code>--hint=nomultithread</code> is not used</li>
</ul>
</td>
<td class="wysiwyg-text-align-center" style="width: 237px;">
<p>The job gets, and is charged for, <em>N</em> logical CPUs, rounded up to the nearest even number.</p>
<p><strong>Set <em>N</em> to an even number if possible.</strong></p>
</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">
<p>The job gets <em>N</em> logical CPUs, but is charged for 80.</p>
<p><strong>Set <em>N</em> to 80 if possible.</strong></p>
</td>
</tr>
<tr>
<td style="width: 221px;">
<ul>
<li>Only one task</li>
<li>
<code>--cpus-per-task=</code><em>N</em>
</li>
<li>
<code>--hint=nomultithread</code> is used</li>
</ul>
</td>
<td class="wysiwyg-text-align-center" style="width: 237px;">The job gets, and is charged for, 2<em>N</em> logical CPUs.</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">
<p>The job gets 2<em>N</em> logical CPUs, but is charged for 80.</p>
<p><strong>Set <em>N</em> to 40 if possible.</strong></p>
</td>
</tr>
<tr>
<td style="width: 221px;">
<ul>
<li>More than one task on one or more nodes</li>
<li>
<code>--cpus-per-task</code> is not used</li>
<li>
<code>--hint=nomultithread</code> is not used</li>
</ul>
</td>
<td class="wysiwyg-text-align-center" style="width: 237px;" rowspan="2">
<p>Each task gets two logical CPUs. The job is charged for two logical CPUs per task. <code>--hint=nomultithread</code> is irrelevant.</p>
<p> </p>
</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">
<p>Each task gets one logical CPU. The job is charged for 80 logical CPUs per allocated node.</p>
<p><strong>If possible, set the number of tasks per node to 80.</strong></p>
</td>
</tr>
<tr>
<td style="width: 221px;">
<ul>
<li>More than one task on one or more nodes</li>
<li>
<code>--cpus-per-task</code> is not used</li>
<li>
<code>--hint=nomultithread</code> is used</li>
</ul>
</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">
<p>Each task gets two logical CPUs. The job is charged for 80 logical CPUs per allocated node.</p>
<p><strong>If possible, set the number of tasks per node to 40.</strong> </p>
</td>
</tr>
<tr>
<td style="width: 221px;">
<ul>
<li>More than one task on one or more nodes</li>
<li>
<code>--cpus-per-task=</code><em>N</em>
</li>
<li>
<code>--hint=nomultithread</code> is not used</li>
</ul>
</td>
<td class="wysiwyg-text-align-center" style="width: 237px;">
<p>Each task gets <em>N</em> logical CPUs, rounded up to the nearest even number. The job is charged for that number of logical CPUs per task.</p>
<p><strong>Set <em>N</em> to an even number if possible.</strong></p>
</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">
<p>Each task gets <em>N</em> logical CPUs. The job is charged for 80 logical CPUs per allocated node.</p>
<p><strong>If possible, set <em>N</em> and the number of tasks per node such that <em>N</em> × (tasks per node) = 80.</strong></p>
</td>
</tr>
<tr>
<td style="width: 221px;">
<ul>
<li>More than one task on one or more nodes</li>
<li>
<code>--cpus-per-task=</code><em>N</em>
</li>
<li>
<code>--hint=nomultithread</code> is used</li>
</ul>
</td>
<td class="wysiwyg-text-align-center" style="width: 237px;">Each task gets 2<em>N</em> logical CPUs. The job is charged for 2<em>N</em> logical CPUs per task.</td>
<td class="wysiwyg-text-align-center" style="width: 232px;">
<p>Each task gets 2<em>N</em> logical CPUs. The job is charged for 80 logical CPUs per allocated node.</p>
<p><strong>If possible, set <em>N</em> and the number of tasks per node such that <em>N</em> × (tasks per node) = 40.</strong></p>
</td>
</tr>
</tbody>
</table>
<p> </p>