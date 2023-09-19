---
created_at: '2021-04-16T01:18:51Z'
hidden: false
label_names:
- releasenote
position: 0
title: Long-term Storage - Nearline release notes v1.1.0.20
vote_count: 0
vote_sum: 0
zendesk_article_id: 360004089016
zendesk_section_id: 360000502675
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p><em>Released Thursday 15 April 2021.</em></p>
<p>This is a minor release incorporating bug fixes and improvements.</p>
<ul>
<li>The <code>nlcompare</code> command will no longer call attention to differences between files and directories that are solely due to the expected difference at the start of the absolute path, i.e. the textual difference between <code>/nesi/nearline/&lt;project_code&gt;</code> and <code>/nesi/project/&lt;project_code&gt;</code> (or <code>/nesi/nobackup/&lt;project_code&gt;</code>) at the start of the path is ignored as irrelevant. <code>nlcompare</code> continues to highlight the differences that might actually matter: files present on nearline but missing from the project or nobackup directory (or vice versa), files that have been renamed, and files with different sizes or last modified times.</li>
<li>The <code>nlget</code> command now gives a prompt and informative error message if you attempt to retrieve a single file from Nearline, instead of, as previously, submitting the job to the server, which would, after a wait that might well be lengthy depending on demand for the service, respond with <code>pol_failed</code> or some other uninformative error.</li>
<li>The <code>nlls</code> command now gives a prompt and meaningful error message if run on a single file with the <code>-s</code> command-line switch, instead of, as previously, returning no results.</li>
<li>The in-program usage message for the <code>nlpurge</code> command, which is printed when the wrong number or type of arguments is supplied, has been improved.</li>
<li>For ease of scripting, client or server errors that occur while the client program is running and you are requesting a nearline operation will, in almost all cases, cause the nearline client program to exit with a non-zero exit code. Note that this is not, and can not be, the case where the error first occurs after the job has been accepted by the server for processing.</li>
</ul>