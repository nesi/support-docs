---
created_at: '2021-08-30T03:19:42Z'
hidden: false
label_names:
- releasenote
- nearline
position: 0
title: Long Term Storage - Nearline release notes v1.1.0.22
vote_count: 0
vote_sum: 0
zendesk_article_id: 4405757918095
zendesk_section_id: 360000502675
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p><em>Released Friday 27 August 2021.</em></p>
<p>This is a minor release incorporating bug fixes and improvements.</p>
<ul>
<li>A bug causing the programs <code>nlls</code>, <code>nltraverse</code> and <code>nlcompare</code> to misbehave when dealing with invisible files and directories (whose names start with <code>.</code>), and other files and directories whose names contain unorthodox characters such as spaces or other characters having special meaning to the shell, has been fixed.</li>
<li>A bug causing <code>nlls</code> to return <code>Internal Server Error</code> when the operator specifies a subdirectory of a project directory that doesn't exist on Nearline has been fixed. The error <code>no such file or directory</code> is now returned instead.</li>
<li>Some small improvements have been made to server configuration parsing and detection of inappropriate or missing configuration values.</li>
</ul>
<p>During testing of this release, we found that attempts to run <code>nlput</code> or <code>nlget</code> using arguments containing spaces, especially multiple consecutive spaces, fail at the Nearline datamover stage while running <code>rsync</code>. This issue has been recorded and documented. For now, the recommended workaround is to rename such files or directories before uploading them to Nearline, or, alternatively, to store them in an archive that does not contain spaces in its name. </p>