---
created_at: '2020-11-04T04:39:50Z'
hidden: false
label_names:
- releasenote
position: 0
title: Long-Term Storage - Nearline release notes  v1.1.0.14
vote_count: 0
vote_sum: 0
zendesk_article_id: 360002113295
zendesk_section_id: 360000502675
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <h1>Version 1.1.0.14</h1>
<p><em>Released 5 November 2020.</em></p>
<p>This release includes the following changes:</p>
<ul>
<li>
<code>nlls</code>, <code>nlget</code>, <code>nlpurge</code>, <code>nlput</code> and <code>nljobstatus</code> now come with a debug mode, accessible via the <code>--debug</code> command line switch.</li>
<li>Help documentation, as well as the usage message when a nearline command is run with incorrect arguments, has been improved.</li>
<li>
<code>nljobstatus</code> now includes more comprehensive job status information. In particular, the job status message now includes a brief description of the stage the job is up to, and whether the job is at that moment pending (waiting in a queue to start the next operation), running, or complete.</li>
<li>The <code>nlls</code> command's <code>-ls</code> switch has been replaced with <code>-s</code>, though <code>-ls</code> still works, being interpreted as equivalent to <code>-l -s</code>. <code>nlls</code> also now comes with a <code>-b</code> switch, for reporting individual sizes in bytes instead of in human-readable sizes.</li>
<li>
<code>nltraverse</code> has been improved, and now reports file sizes, and sums of file sizes, in bytes, for greater accuracy and ease of comparison with the output of <code>ls</code>.</li>
<li>There have been numerous other bug fixes to improve performance and reduce the risk of unexpected failures and errors.</li>
</ul>