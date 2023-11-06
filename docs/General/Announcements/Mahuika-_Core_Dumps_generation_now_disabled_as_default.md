---
created_at: '2022-07-11T23:23:04Z'
hidden: false
label_names:
- mahuika
- .core
- corefile
- coredump
position: 0
status: new
title: 'Mahuika: Core Dumps generation now disabled as default'
vote_count: 0
vote_sum: 0
zendesk_article_id: 5126681349903
zendesk_section_id: 200732737
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>A Slurm configuration change has been made on Mahuika so that the  maximum size of<span> </span><a class="c-link" href="https://support.nesi.org.nz/hc/en-gb/articles/360001584875-What-is-a-core-file-" target="_blank" rel="noopener noreferrer" data-stringify-link="https://support.nesi.org.nz/hc/en-gb/articles/360001584875-What-is-a-core-file-" data-sk="tooltip_parent">core file</a><span> </span>that can be generated inside a job now defaults to<span> </span><code class="c-mrkdwn__code" data-stringify-type="code">0</code><span> </span>bytes rather than<span> </span><code class="c-mrkdwn__code" data-stringify-type="code">unlimited</code>. </p>
<p>You can reenable core dumps with<span> </span><code class="c-mrkdwn__code" data-stringify-type="code">ulimit -c unlimited</code><span> </span>.</p>