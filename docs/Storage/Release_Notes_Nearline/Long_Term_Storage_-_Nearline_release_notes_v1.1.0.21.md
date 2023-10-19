---
created_at: '2021-07-28T00:05:31Z'
hidden: false
label_names:
- releasenote
- nearline
position: 0
title: Long Term Storage - Nearline release notes v1.1.0.21
vote_count: 0
vote_sum: 0
zendesk_article_id: 4404255007503
zendesk_section_id: 360000502675
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p><em>Released Wednesday 4 August 2021.</em></p>
<p>This is a minor release incorporating bug fixes and improvements.</p>
<ul>
<li>Certain server errors when a bad job is submitted now generate a more informative error message in the client program than, "Internal Server Error."</li>
<li>Nearline client programs now log to the <code>~/.librarian</code> directory, so you no longer need to explicitly decorate the Nearline command with complex strings in order to capture basic troubleshooting information.</li>
<li>A bug causing <code>nlput</code> with a file list to fail if any entries in the file list were missing from Nearline has been fixed. Now, <code>nlput</code> will work even though the file is not already present on Nearline.</li>
<li>
<code>nlput</code> no longer throws an exception if, when you are prompted for a y/n response, you hit Enter thereby submitting an empty string. Instead, it asks the same question again.</li>
<li>If a local directory into which files are to be retrieved does not exist, <code>nlget</code> will now carry out the retrieval. Previously, <code>nlget</code> would create the directory but then abandon the retrieval.</li>
<li>We have clarified in help messages that <code>nlpurge</code> does not accept a single file (on Nearline) as the file to be purged. The argument that is not the project code must be either a directory on Nearline, or a local file list.</li>
<li>A bug has been fixed in the Nearline server whereby the server would incorrectly calculate the changes to the project's disk space and file count usage if an <code>nlpurge</code> command were to fail (or skip some files) for any reason after it was accepted by the server.</li>
<li>
<code>nlpurge</code> can now be used to delete empty directories from Nearline, provided the directory is given directly as an argument and not included in a file list.</li>
<li>
<code>nlpurge</code> deals gracefully with the situation in which a directory to be purged is not a subdirectory somewhere within the specified project's Nearline directory, by printing an informative error message.</li>
<li>
<code>nlpurge</code> will no longer accept a file list argument if any of the entries in the file list point to files (on Nearline) that are outside the specified project's Nearline directory. Instead, an error message will be displayed, listing all affected lines in the file list.</li>
<li>A bug that required users to start <code>nlpurge</code> file list entries with <code>/scale_wlg_nearline/filesets/nearline/</code> has been fixed. Now, entries must start with the more intuitive <code>/nesi/nearline/</code>.</li>
<li>A bug causing <code>nlls</code> (and commands depending on it, like <code>nltraverse</code>) to fail if an empty directory is listed or included in the traverse operation has been fixed.</li>
</ul>