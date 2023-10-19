---
created_at: '2022-02-15T01:13:51Z'
hidden: false
label_names: []
position: 1
title: Checking your project's usage using nn_corehour_usage
vote_count: 0
vote_sum: 0
zendesk_article_id: 4416692988047
zendesk_section_id: 360000030876
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p>To check your project's usage of Slurm-managed resources, you can use the command <code>nn_corehour_usage</code>. This command displays usage of cluster resources by a specific project, computed from the Slurm program <code>sreport</code>.</p>
<h1 id="h_01HC8WWMEVN2GWM123MH3QYSMK">Synopsis</h1>
<pre>nn_corehour_usage [OPTIONS...] PROJECT_CODE...
</pre>
<h1 id="h_01HC8WWMEV6YJ024FBNRD8C9FN">Description</h1>
<p><code>nn_corehour_usage</code> shows a month-by-month breakdown of how the specified project or projects have used Slurm resources. Some resources, like disk space, are not managed by Slurm and so are excluded. Included resources are CPU time, RAM time (also known as memory time) and GPU time.</p>
<h1 id="h_01HC8WWMEV57MXWE1KQ4PZ0HX8">Options</h1>
<p><code>-c</code>, <code>--calendar-months</code></p>
<p>Break usage down so that the time periods are the first and last days of the calendar months, instead<br>of working back a month at a time from today.</p>
<p><code>-n</code>, <code>--number-of-months=NUM</code></p>
<p>Show <code>NUM</code> months back from today. Used in conjunction with <code>-c</code>, will show <code>NUM</code> complete months plus the partial month up to when the command is run. Default is 12 months. The results will not go further back than when the cluster commenced operations.</p>
<p><code>-u</code>, <code>--user=USERNAME</code></p>
<p>Display results for the user <code>USERNAME</code>. The default user is the current user.</p>
<p> </p>
<p>Treat all subsequent entries on the command line, including those starting with a dash (<code>-</code>), as arguments instead of as options.</p>
<h1 id="h_01HC8WWMEV923NGDKPWFKZTDGX">Examples</h1>
<p>To print the last year of project nesi12345:</p>
<pre>nn_corehour_usage nesi12345</pre>
<p>To print the last six complete calendar months of project nesi12345:</p>
<pre>nn_corehour_usage -c -n 6 nesi12345</pre>