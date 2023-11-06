---
created_at: '2022-03-22T02:16:17Z'
hidden: false
label_names:
- general
position: 0
title: Slurm upgrade to version 21.8
vote_count: 0
vote_sum: 0
zendesk_article_id: 4544913401231
zendesk_section_id: 200732737
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<div class="p-rich_text_section">Slurm, the scheduler that controls Maui and Mahuika, has been upgraded to version 21.8 on machines.  Below are the highlights of the changes expected in the new version. The full list of bugfixes, improvements and changes is available on Schemd  website: <a href="https://slurm.schedmd.com/news.html" target="_blank" rel="noopener">Slurm news</a>
</div>
<div class="p-rich_text_section"><span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span></div>
<div class="p-rich_text_section"><span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span></div>
<div class="p-rich_text_section">
<span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span><strong data-stringify-type="bold"><em data-stringify-type="italic">squeue</em></strong>
</div>
<ul>
<li class="c-mrkdwn__quote" data-stringify-type="quote">Added<span> </span><code class="c-mrkdwn__code" data-stringify-type="code">--me</code><span> </span>option, equivalent to<code class="c-mrkdwn__code" data-stringify-type="code"> --user=$USER</code>.</li>
<li class="c-mrkdwn__quote" data-stringify-type="quote">Added "pendingtime" as a option for --Format.</li>
<li class="c-mrkdwn__quote" data-stringify-type="quote">Put sorted start times of "N/A" or 0 at the end of the list.</li>
</ul>
<div class="p-rich_text_section">
<span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span><strong data-stringify-type="bold"><em data-stringify-type="italic">sacct</em></strong>
</div>
<ul>
<li class="p-rich_text_section">Add time specification: "now-" (i.e. subtract from the present)</li>
<li class="p-rich_text_section">AllocGres and ReqGres were removed. Alloc/ReqTres should be used instead. </li>
</ul>
<div class="p-rich_text_section">
<span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span><strong data-stringify-type="bold"><em data-stringify-type="italic">scontrol</em></strong>
</div>
<ul>
<li class="p-rich_text_section">MAGNETIC flag on reservations. Reservations the user doesn't have to even request.</li>
<li class="p-rich_text_section">The LicensesUsed line has been removed from<span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span><code class="c-mrkdwn__code" style="font-size: 15px;" data-stringify-type="code">scontrol show config</code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">. Please use updated</span><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span><code class="c-mrkdwn__code" style="font-size: 15px;" data-stringify-type="code">scontrol show licenses</code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">command as an alternative.</span>
</li>
</ul>
<div class="p-rich_text_section">
<span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span><strong data-stringify-type="bold"><em data-stringify-type="italic">sbatch</em></strong><br><span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span>
</div>
<ul>
<li> <code class="c-mrkdwn__code" data-stringify-type="code">--threads-per-core</code><span> </span>now influences task layout/binding, not just allocation.</li>
<li>
<code class="c-mrkdwn__code" style="font-size: 15px;" data-stringify-type="code">--gpus-per-node</code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">can be used instead of</span><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span><code class="c-mrkdwn__code" style="font-size: 15px;" data-stringify-type="code">--gres=GPU</code>
</li>
<li>
<code class="c-mrkdwn__code" style="font-size: 15px;" data-stringify-type="code">--hint=nomultithread</code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> can now be replaced </span><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">with</span><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span><code class="c-mrkdwn__code" style="font-size: 15px;" data-stringify-type="code">--threads-per-core=1</code>
</li>
<li>The inconsistent terminology and environment variable naming for Heterogeneous Job ("HetJob") support has been tidied up.</li>
<li>The correct term for these jobs are "HetJobs", references to "PackJob"   have been corrected.</li>
<li>The correct term for the separate constituent jobs are "components",   references to "packs" have been corrected.</li>
</ul>
<div class="p-rich_text_section">
<span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span><strong data-stringify-type="bold">salloc</strong>
</div>
<ul>
<li>Added support for an "Interactive Step", designed to be used with salloc to launch a terminal on an allocated compute node automatically. Enable by setting "use_interactive_step" as part of LaunchParameters.</li>
</ul>
<div class="p-rich_text_section">
<span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span><strong data-stringify-type="bold"><em data-stringify-type="italic">srun</em></strong>
</div>
<ul>
<li> By default, a step started with srun will be granted exclusive (or non- overlapping) access to the resources assigned to that step. No other parallel step will be allowed to run on the same resources at the same time. This replaces one facet of the '--exclusive' option's behavior, but does not imply the '--exact' option described below. To get the previous default behavior - which allowed parallel steps to share all resources - use the new srun '--overlap' option.</li>
<li>In conjunction to this non-overlapping step allocation behavior being the new default, there is an additional new option for step management '--exact', which will allow a step access to only those resources requested by the step. This is the second half of the '--exclusive' behavior. Otherwise, by default all non-gres resources on each node in the allocation will be used by the step, making it so no other parallel step will have access to those resources unless both steps have specified '--overlap'.</li>
</ul>
<div class="p-rich_text_section">
<span class="c-mrkdwn__br" data-stringify-type="paragraph-break"></span><strong data-stringify-type="bold"><em data-stringify-type="italic">scrontab</em></strong>
</div>
<ul>
<li>New command which permits crontab-compatible job scripts to be defined. These scripts will recur automatically (at most) on the intervals described.</li>
</ul>