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
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p><span style="font-weight: 400;">As CPU technology advanced </span>engineers realised that adapting CPU architecture to include <em>logical </em><span style="font-weight: 400;"><span><em>processors </em>within the physical core (conventionally, a CPU) allows </span></span>some computation to occur simultaneously<span style="font-weight: 400;"><span>.</span></span> The name for this technology is <span style="font-weight: 400;"><em style="font-weight: 400;">simultaneous multithreading</em>, and </span><span style="font-weight: 400;">Intel's implementation of it is called <a style="font-weight: 400;" href="https://en.wikipedia.org/wiki/Hyper-threading" target="_self">Hyperthreading</a>.</span></p>
<p><span style="font-weight: 400;">CPUs capable of Hyperthreading consists of two logical <span>processors per </span>physical core. The logical processors can operate on data/instruction <em>threads</em> simultaneously, meaning the physical core can perform two operations concurrently. </span><span style="font-weight: 400;">In other words, t<span>he difference between logical and physical cores is that logical cores are not full stand-alone CPUs, and share some hardware with nearby logical cores. Physical cores are made up of two logical cores.</span></span></p>
<p><span style="font-weight: 400;">Hyperthreading is enabled by default on NeSI machines, meaning, by default, Slurm will allocate two threads to each physical core. </span></p>
<h1 id="h_01HBYNN7M3G9GVHJPZ0C8VX4JW">
<span style="font-weight: 400;">Hyperthreading</span> with slurm</h1>
<p><span style="font-weight: 400;"><span>When Slurm request a CPU, it is <strong>requesting logical cores,</strong> which, as mentioned above, there are two of per physical core.</span></span><span style="font-weight: 400;"><span> If you use </span><code>--ntasks=n</code> to request CPUs, Slurm will start <code>n</code> MPI tasks which are each assigned to one physical core. Since Slurm "sees" logical cores, once your job starts you will have twice the number of CPUs as <code>ntasks</code>.</span></p>
<p><span style="font-weight: 400;">If you set <code>--cpus-per-task=n</code>, Slurm will request <code>n</code> logical CPUs per task, i.e., will set <code>n</code> threads for the job. Your code must be capable of running Hyperthreaded (for example using <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001070496">OpenMP</a>) if <code>--cpus-per-task &gt; 1</code>.</span><span></span><span style="font-weight: 400;"></span></p>
<p> </p>
<p><span style="font-weight: 400;"><span>Setting <code>--hint=nomultithread</code> with srun or sbatch "causes Slurm to allocate only one thread from each core to this job". This will allocate CPUs according to the following image:</span></span></p>
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
<p><span style="font-weight: 400;"><span>Image adapted from <a href="https://slurm.schedmd.com/cpu_management.html">Slurm's documentation page</a>.</span></span></p>
<h1 id="h_01HBYVY0FAQ45YVR8GM4YFDTCY">When to use Hyperthreading</h1>
<p><span><span>Hyperthreading</span> increases the efficiency of some jobs, but the fact that Slurm is counting in logical CPUs makes aspects of running non-Hyperthreaded jobs confusing, even when Hyperthreading is turned off in the job with <code>--hint=nomultithread</code>.</span> To determine if the code you are running is capable of running <span>Hyperthreaded</span>, visit the manual pages for the software.</p>
<p><span></span>Alternatively, it is possible to perform an ad-hoc test to determine if your code is capable of making use of <span>Hyperthreading</span>. First run a job that has requested 2 threads per physical core as described above. Then, use the <span style="font-weight: 400;"><code>nn_seff</code> </span>command to check the jobs CPU <span>efficiency. If CPU efficiency</span> is greater than 100%, then your code is making use of <span>Hyperthreading, and gaining performance from it. If your job gives an error or stays at 100% efficiency, it is likely you can not run your code Hyperthreaded. 200% CPU efficiency would be the maximally efficient job, however, this is rarely observed and anything over 100% should be considered a bonus.</span></p>
<h1 id="01HBYXJXEQTAXC2C2RM97N7VWK">How to use Hyperthreading</h1>
<ul>
<li style="font-weight: 400;">
<span style="font-weight: 400;">Non-hyperthreaded jobs which use  </span><code>--mem-per-cpu</code><span style="font-weight: 400;"> requests should halve their memory requests as those are based on memory per logical CPU, not per the number of threads or tasks.  For non-MPI jobs, or for MPI jobs that request the same number of tasks on every node, we recommend to specify <code>--mem</code> (i.e. memory per node) instead. See <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001108756" target="_self">How to request memory (RAM)</a> for more information.</span>
</li>
<li style="font-weight: 400;">
<span style="font-weight: 400;">Non-MPI jobs which specify </span><code>--cpus-per-task</code><span style="font-weight: 400;"> and use </span><strong>srun </strong><span style="font-weight: 400;">should also set </span><code>--ntasks=1</code><span style="font-weight: 400;">, otherwise the program will be run twice in parallel, halving the efficiency of the job.</span>
</li>
</ul>
<p><span style="font-weight: 400;">The precise rules about when Hyperthreading applies are as follows:</span></p>
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
<td class="wysiwyg-text-align-center" style="width: 581px;" colspan="2">Share physical cores by default. You can override this behaviour by using<br><code>--hint=nomultithread</code> in your job submission script.</td>
</tr>
</tbody>
</table>
<p> </p>
<h2 id="h_01HBYM07C3A28VEE90FQRBEM53">How many logical CPUs will my job use or be charged for?</h2>
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
<p>The job gets one logical CPU, but is charged for 80.<br><code>--hint=nomultithread</code> is irrelevant.</p>
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