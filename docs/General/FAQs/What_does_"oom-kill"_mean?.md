---
created_at: '2018-10-25T02:22:02Z'
hidden: false
label_names:
- faq
position: 0
title: What does "oom-kill" mean?
vote_count: 2
vote_sum: 2
zendesk_article_id: 360000532595
zendesk_section_id: 360000039036
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p>OOM stands for "Out Of Memory", and so an error such as this:</p>
<pre>slurmstepd: error: Detected 1 oom-kill event(s) in step 370626.batch cgroup</pre>
<p>indicates that your job attempted to use more memory (RAM) than Slurm reserved for it.  </p>
<p>OOM events can happen even without Slurm's <code>sacct</code> command reporting such a high memory usage, for two reasons:</p>
<ul>
<li>Unlike the enforcement via cgroups, Slurm's accounting system only records usage every 30 seconds, so sudden spikes in memory usage may not be recorded, but can still trigger the OOM killer;</li>
<li>Slurm's accounting system also does not include any temporary files the job may have put in the memory-based <code>/tmp</code> or <code>$TMPDIR</code> filesystems.</li>
</ul>
<p>If you see an OOM event, you have two options. The easier option is to request more memory by increasing the value of the <code>--mem</code> argument in your job submission script. The more difficult, but potentially more useful where it is feasible, is to make your job less memory-intensive.</p>