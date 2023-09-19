---
created_at: '2021-03-02T03:32:48Z'
hidden: false
label_names:
- releasenote
position: 0
title: Long-term Storage - Nearline release notes v1.1.0.19
vote_count: 0
vote_sum: 0
zendesk_article_id: 360003551116
zendesk_section_id: 360000502675
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p><em>Released Thursday 4 March 2021.</em></p>
<p>This release includes a number of significant changes and new features:</p>
<ul>
<li>The <code>nltraverse</code> command is now supported by an <code>nlcompare</code> command. With <code>nlcompare</code>, you can compare a directory within <code>/nesi/project</code> or <code>/nesi/nobackup</code> with a corresponding directory on <code>/nesi/nearline</code>, and it will show any differences in file names, sizes, ownerships, permissions and last modified timestamps. Please note that <code>nlcompare</code> does not compare file contents.</li>
<li>File size limits are now in place when running <code>nlput</code> (not applicable to <code>nlget</code> or <code>nlpurge</code>):
<ul>
<li>a minimum per-file size limit of 64 MB;</li>
<li>a maximum per-file size limit of 1 TB.</li>
</ul>
</li>
<li>Permission restrictions are now in place when running <code>nlput</code> (not applicable to <code>nlget</code> or <code>nlpurge</code>):
<ul>
<li>You, as the operator, must be able to read every file selected for upload.</li>
<li>The group of every file must match the project code you choose. If there is a mismatch, it may be that the project code has been mistyped.</li>
<li>The permissions of every file must be set so that both the file's owner and the file's group are allowed to read and write the file.</li>
<li>Where a directory (as opposed to a filelist) is specified for upload, that directory and every subdirectory therein must also be readable and executable by the operator, belong to the specified group, and be readable, writable and executable by the file owner and group.</li>
</ul>
</li>
<li>Attempts to run <code>nlget</code> and <code>nlpurge</code> on files or directories not present on nearline will now fail before the job is submitted to the server, with a clear error message, instead of failing on the server side, after a delay and with an obscure error message.</li>
<li>Certain server errors that previously caused <code>KeyError</code> in the client will now be reported as <code>RuntimeError: Internal Server Error</code>.</li>
<li>Server-side logging and tracking with state files have been improved.</li>
</ul>