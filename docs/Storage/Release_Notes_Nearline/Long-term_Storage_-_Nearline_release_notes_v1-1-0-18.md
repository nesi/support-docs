---
created_at: '2021-01-12T07:20:01Z'
hidden: false
label_names:
- releasenote
position: 0
title: Long-term Storage - Nearline release notes v1.1.0.18
vote_count: 0
vote_sum: 0
zendesk_article_id: 360002655596
zendesk_section_id: 360000502675
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>This release incorporates several minor but significant bug fixes and new features.</p>
<p>In particular:</p>
<ul>
<li>To run <code>nljobstatus</code> with a particular job ID, you no longer need the <code>-j</code> switch before the job ID. <code>nljobstatus &lt;jobID&gt;</code> will suffice.</li>
<li>The <code>nlput</code> program will now check to see whether any of the files requested for upload already exist on nearline. If it finds any of them, it will ask you if you want to continue anyway, warning you that the already existing files will not be altered or updated by the nlput process.</li>
<li>The <code>nlput</code> program will also offer to create a filelist of already existing files, in order to help you more conveniently delete them from nearline if you wish to replace them with an updated version. Users taking advantage of this feature are encouraged to review the filelist after it has been generated, in case there are any files included that you do not wish to delete.</li>
<li>
<code>nlput</code>, <code>nlget</code> and <code>nlpurge</code> now verify that files and filelists are in allowed locations, and (in the case of filelists) that the individual filelist entries are in allowed locations:
<ul>
<li>For <code>nlput</code>, all files to be uploaded must be within either <code>/nesi/project</code> or <code>/nesi/nobackup</code>, whether they come from a directory or are specified in a filelist</li>
<li>For <code>nlget</code>, all files to be retrieved must be within <code>/nesi/nearline</code>, and the destination must be within <code>/nesi/project</code> or <code>/nesi/nobackup</code>
</li>
<li>For <code>nlpurge</code>, all files to be deleted must be within <code>/nesi/nearline</code>
</li>
<li>For <code>nlput</code>, <code>nlget</code> and <code>nlpurge</code> with filelists, the filelist must be within <code>/nesi/project</code> or <code>/nesi/nobackup</code>
</li>
</ul>
</li>
<li>A bug causing projects to be locked indefinitely when <code>nlput</code> is given a filelist as an argument has been fixed.</li>
<li>An attempt to remove a nonexistent directory from nearline using <code>nlpurge</code> will no longer lock the project.</li>
<li>Various bugs causing locks to persist on nearline projects even once the locking process has ended have been fixed. Previously, many error conditions causing nearline server tasks to end prematurely would have left orphaned locks on involved projects.</li>
</ul>