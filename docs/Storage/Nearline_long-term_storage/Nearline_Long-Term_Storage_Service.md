---
created_at: '2019-09-18T22:28:01Z'
hidden: false
label_names:
- storage
- nearline
- tape
position: 0
title: Nearline Long-Term Storage Service
vote_count: 2
vote_sum: 2
zendesk_article_id: 360001169956
zendesk_section_id: 360000042255
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p style="display: none;">Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline</p>
<div class="confluence-information-macro-body">
<p> </p>
<p>NeSI's Nearline service allows you to store your data on our hierarchical system, which consists of a staging area (disk) connected to a tape library. Users of this service gain access to more persistent storage space for their research data, in return for slower access to those files that are stored on tape. We recommend that you use this service for larger datasets that you will only need to access occasionally and will not need to change in situ. The retrieval of data may be delayed, due to tape handling, queuing of the nearline backend service and size of the data to be ingested or retrieved..</p>
<p>Due to the tape storage backend Nearline is intended for use with relatively large files and should not be used for a large number of small files. <span style="color: #1d1c1d;">Files smaller than 64 MB will not be accepted for upload and should be combined into archive files using <code>nn_archive_files</code>, <code>tar</code> or a similar tool. Likewise, Nearline write semantics are different from a normal filesystem - overwriting existing files (e.g. when the source data has been updated) is not supported, these must first be removed (purged from Nearline) before being written (put to Nearline) again.</span></p>
<p><strong>IMPORTANT</strong>: A Nearline project gets locked when writing to or deleting from it. Until this process is finished no other write or delete operation can be performed on the same project and the user will see a status message "<strong>project locked by none</strong>".</p>
<h1>What you can do</h1>
<p>The client allows you to carry out the following operations:</p>
<ul>
<li>View files: View a list of files stored in a Nearline directory.</li>
<li>Traverse a directory: View a list of files stored in a Nearline directory, including files stored in all its subdirectories.</li>
<li>Put: Copy files from your project or nobackup folder into Nearline.</li>
<li>Get: Retrieve files from Nearline into your project or nobackup folder, without deleting them from Nearline.</li>
<li>Compare the contents of a local directory with the contents of a Nearline directory.</li>
<li>Purge: Delete files stored in Nearline.</li>
<li>View job status: View a list of jobs (put/get/purge) you have run, along with their status.</li>
<li>View quota: View your Nearline quota and usage.</li>
</ul>
<h1>Getting started</h1>
<p>Nearline has a common tool for access, with a set of <code>nl*</code> commands, which are accessible by loading the following module:</p>
<pre><code>module load nearline</code></pre>
</div>
<p> </p>
<h1>Viewing files in nearline</h1>
<p>With the following command, you can print the list of files and directories within the specified Nearline directory:</p>
<pre><code>nlls /nesi/nearline/&lt;projectID&gt;</code></pre>
<p>Similar to the shell command <code>ls</code> you can list subdirectories as well:</p>
<pre><code>nlls /nesi/nearline/&lt;projectID&gt;/results/</code></pre>
<p>Furthermore, you can use the additional option <code>-l</code> to get the detailed list including <code>mode</code>, <code>owner</code>, <code>group</code>, <code>filesize</code>, and <code>timestamp</code>. The option <code>-s</code>, an alternative to <code>-l</code>, will additionally show each file's migration status. Note that, due to technical limitations, <code>-s</code> does not work on single files and so <code>nlls -s</code> requires a directory as its argument.</p>
<pre><code>$ nlls -s /nesi/nearline/nesi12345/results/
mode        s  owner               group      filesize    timestamp    filename
___________________________________________________________________________________________________________________________
-rw-rw----+ r  userName        nesi12345      33.93 MB       Jun 17    file1.tar.gz
-rw-rw----+ r  userName        nesi12345      33.93 MB       Jun 17    file2.tar.gz
-rw-rw----+ r  userName        nesi12345      34.03 MB       Jun 17    file3.tar.gz
</code></pre>
<p class="auto-cursor-target">Status ("s" column of the <code>-s</code> output) legend:</p>
<ul>
<li class="auto-cursor-target">migrated (<strong>m</strong>) - data of a specific Nearline file is on tape (does not necessarily mean that the file is replicated across sites)</li>
<li class="auto-cursor-target">pre-migrated (<strong>p</strong>) - data of a specific Nearline file is on both the staging filesystem and the tape.</li>
<li class="auto-cursor-target">resident (<strong>r</strong>) - data of a specific Nearline file is only on the staging filesystem.</li>
</ul>
<p><strong>BUG WARNING: </strong> The <code>-l</code> and  <code>-s</code>flags may fail if the nearline directory has a large amount of files.  You will receive a long Python stack trace if this occurs.</p>
<h1>Traversing files within nearline</h1>
<p>If you want to see all the files within a Nearline directory and its subdirectories, you can run <code>nltraverse</code>.</p>
<pre><code>nltraverse /nesi/nearline/&lt;projectID&gt;</code></pre>
<p>Optionally, you can run <code>nltraverse</code> with the <code>-s</code> command-line switch, which, as with <code>nlls</code>, will display the migration status of each file found.</p>
<p> </p>
<p><strong>BUG WARNING: </strong> The<code>-s</code>flag may fail if a nearline directory has a large amount of files.  You will receive a long Python stack trace if this occurs.</p>
<h1>Comparing files in nearline to those on disk</h1>
<p>If you want to compare a local (online storage) directory to a directory on Nearline, you can use the <code>nlcompare</code> command. The syntax of this command is:</p>
<pre><code>nlcompare &lt;local_directory&gt; &lt;nearline_directory&gt;</code></pre>
<p>This command will print out the lists of files giving their last modified times, sizes and file paths.</p>
<p><code>nlcompare</code> is particularly useful if you want to compare a directory on Nearline to a corresponding directory in <code>/nesi/project</code> or <code>/nesi/nobackup</code>. See <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001482516" target="_self">Verifying uploads to Nearline storage</a> for more information on how to do a comparison and verification.</p>
<p>If the contents of the Nearline directory and the corresponding local directory differ, the lists will be kept, and can be compared using any text file comparison program, such as <code>diff</code> or <code>vimdiff</code>.</p>
<h1 id="Nearlineearlyaccessuserguide-Put">Putting/Ingesting files into nearline</h1>
<p>Data can be copied to Nearline using the <code>nlput</code> command. The syntax is:</p>
<pre><code>nlput [ --nowait ] &lt;projectID&gt; { &lt;src_dir&gt; | &lt;file_list&gt; }</code></pre>
<p>The source directory or file list needs to be located under <code>/nesi/<strong>project</strong>/</code> or <code>/nesi/<strong>nobackup</strong>/</code>and specified as such. </p>
<blockquote class="blockquote-tip">
<h3 id="nlput-relative-paths">Note</h3>
<p>The following will not work:</p>
<pre><code>cd /nesi/project/nesi12345
nlput nesi12345 some_directory</code></pre>
<p>It is necessary to do this instead:</p>
<pre><code>nlput nesi12345 /nesi/project/nesi12345/some_directory</code></pre>
</blockquote>
<p>The data will be mapped into the same directory structure under <code>/nesi/<strong>nearline</strong>/</code> (see below).</p>
<blockquote class="blockquote-prereq">
<h3 id="nlput-file-list">Warning</h3>
<p>Please ensure your file or directory names do not contain spaces, non-standard characters or symbols. This may cause issues when uploading or downloading files.</p>
</blockquote>
<p>The recommended file size to archive is between 1 GB and 1 TB. The client <strong>will not</strong> accept any directory or file list containing any file smaller than 64 MB or larger than 1 TB.</p>
<p>The Nearline client also checks file and directory permissions. Specifically, before uploading a directory or the contents of a file list, <code>nlput</code> will check the following, and will reject any directory or file list that does not satisfy all these criteria:</p>
<ul>
<li>Every file must be readable by you, the operator.</li>
<li>Every file must be readable and writable by its owner.</li>
<li>Every file must be readable and writable by its group.</li>
<li>The POSIX group of every file must be the project selected for upload.</li>
</ul>
<p>If you are uploading a directory rather than the contents of a file list, the following additional permission restrictions apply:</p>
<ul>
<li>Every subdirectory must be readable, writable and executable by its owner.</li>
<li>Every subdirectory must be readable, writable and executable by its group.</li>
<li>The POSIX group of every subdirectory must be the project selected for upload.</li>
</ul>
<p>The existing directory structure starting after <code>/nesi/project/&lt;projectID&gt;/</code> or <code>/nesi/nobackup/&lt;projectID&gt;/</code> will be mapped onto <code>/nesi/nearline/&lt;projectID&gt;/</code></p>
<blockquote class="blockquote-prereq">
<h3 id="nlput-input">Warning</h3>
<p>Files and directories are checked for existence and only new files are transferred to Nearline. <strong>Files already on Nearline will not be updated to reflect newer source files</strong>. Thus, files that already exist on Nearline (either tape or staging disk) will be skipped in the migration process, though you should receive a notification of this</p>
<p>If you wish to replace an existing file at a specific file path (instead of creating a copy at a different file path) then the original copy on Nearline must be purged.</p>
</blockquote>
<p><code>nlput</code> takes only a directory or a file list. <strong>A single file is treated as a file list</strong> and read line by line, searching for valid file names. Single files can only be migrated using a file list containing the full path of the file to be transferred.</p>
<h2 id="Nearlineearlyaccessuserguide-Put-directory">Put - directory</h2>
<blockquote class="blockquote-prereq">
<h3 id="directories-with-spaces">Warning</h3>
<p>If you try to upload to Nearline a path containing spaces, especially multiple consecutive spaces, you will get some very unexpected results, such as the job being dropped. We are aware of the issue and may introduce a fix in a future release. In the meantime, we suggest avoiding supplying such arguments to <code>nlput</code>. You can work around it by renaming the directory and all its ancestors to avoid spaces, or by putting the directory (or its ancestor whose name contains a space) into an archive file.</p>
<p>This problem does not affect when your directory to upload happens to have contents (files or directories) with spaces in their names, i.e. to cause a problem the space must be in the name of the directory to be uploaded or one of its ancestor directories.</p>
</blockquote>
<p>All files and subdirectories within a specified directory will be transferred into Nearline. The target location maps with the source location. As an example:</p>
<pre><code>nlput nesi12345 /nesi/nobackup/nesi12345/To/Archive/Results/</code></pre>
<p>will copy all data within the <code>Results</code> directory into</p>
<p><code>/nesi/nearline/nesi12345/<strong>To/Archive/Results/</strong></code>.</p>
<blockquote class="blockquote-prereq">
<h3 id="directory-merging">Warning</h3>
<p>If you put <code>/nesi/<strong>project</strong>/nesi12345/To/Archive/Results/</code> on Nearline as well as <code>/nesi/<strong>nobackup</strong>/nesi12345/To/Archive/Results/</code>, the contents of both source locations (<code>project</code> and <code>nobackup</code>) will be merged into <code>/nesi/nearline/nesi12345/To/Archive/Results/</code>. Within <code>/nesi/nearline/nesi12345/</code>, files with the same name and path will be skipped.</p>
</blockquote>
<h2 id="Nearlineearlyaccessuserguide-Put-file-list">Put - file list</h2>
<blockquote class="blockquote-prereq">
<h3 id="nlput-file-list">Warning</h3>
<p>The file list must be located within <code>/nesi/project</code> or <code>/nesi/nobackup</code>. Any other location will cause obscure errors and failures.</p>
</blockquote>
<p>The <code>file_list</code> is a file containing a list of files to be transferred. It can specify <strong>only one file per line</strong> and <strong>directories are ignored</strong>.</p>
<p>The target location will again map with the source location, see above.</p>
<h2 id="Nearlineearlyaccessuserguide-Update">Update</h2>
<p>As a good practice:</p>
<ul>
<li>migrate only large files (SquashFS archives, tarballs, or files that are individually large), or directories containing exclusively large files.</li>
<li>Do not try to modify a file in the source (nobackup or project) directory once there is a copy of it on Nearline.</li>
<li>Before deleting any data from your project or nobackup directory that has been uploaded to Nearline, please consider whether you require <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001482516" target="_self">verification of the transfer</a>. We recommend that you do at least a basic verification of all transfers.</li>
</ul>
<p>If you need to update data on the Nearline file system with a newer version of data from nobackup or project:</p>
<ol>
<li>Compare the contents of the source directory (on <code>/nesi/project</code> or <code>/nesi/nobackup</code>) and the target directory (on <code>/nesi/nearline</code>). To look at one directory on <code>/nesi/nearline</code> at a time, use <code>nlls</code>; if you need to compare a large number of files across a range of directories, or for more thorough verification (e.g. checksums), read <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001482516" target="_self">this article</a> or <a href="https://support.nesi.org.nz/hc/requests/new" target="_self">contact our support team</a>.</li>
<li>Once you know which files you need to update (i.e. only files whose Nearline version is out of date), remove the old files on Nearline using <code>nlpurge</code>.</li>
<li>Copy the updated files to the Nearline file system using <code>nlput</code>.</li>
</ol>
<blockquote class="blockquote-prereq">
<h3 id="immutable-files">Warning</h3>
<p>For technical reasons, files (data and metadata) and directory structures on Nearline cannot be safely changed once present, even by the system administrators, except by deletion and recreation. If you wish to rename your files or restructure your directories, you must follow the process below.</p>
</blockquote>
<p>If you need to edit data, rename files, or restructure directories that exist on Nearline but are no longer on project or nobackup:</p>
<ol>
<li>Retrieve the files and directories you wish to change using the <code>nlget</code> command (see below).</li>
<li>Make the changes you wish to make.</li>
<li>Follow the instructions above for updating data on Nearline with a new version of the data from project or nobackup.</li>
</ol>
<h1 id="Nearlineearlyaccessuserguide-Get">Getting/Retrieving files from nearline</h1>
<p>Data can be retrieved from Nearline using then <code>nlget</code> command. The syntax is:</p>
<pre><code>nlget [ --nowait ] &lt;projectID&gt; { &lt;src_dir&gt; | &lt;file_list&gt; } &lt;dest_dir&gt;</code></pre>
<p>Similar to <code>nlput</code> (see above), nlget accepts a Nearline<strong> directory</strong> <code>src_dir</code> <strong>(no single files on Nearline accepted)</strong> or a <strong>local file list</strong> <code>file_list</code>, defining the source of the data to be retrieved from Nearline.</p>
<blockquote class="blockquote-prereq">
<h3 id="nlget-file-list">Warnings</h3>
<ul>
<li>The local file list must be located within <code>/nesi/project</code> or <code>/nesi/nobackup</code>. Any other location will be rejected.</li>
<li>Paths to files or directories to be retrieved must be absolute and start with <code>/nesi/nearline</code>, whether supplied on the command line (as a directory) or as entries in a file list.</li>
<li>Directories whose names contain spaces, especially multiple consecutive spaces, cannot be retrieved from Nearline directly using <code>nlget</code>. You must retrieve the contents of such a directory using a filelist, or retrieve one of its ancestors that doesn't have a space in the name or path. That is, instead of retrieving <code>/nesi/project/nesi12345/ab/c  d</code> directly, retrieve <code>/nesi/project/nesi12345/ab</code>. We are aware of the problem and may address it in a later Nearline release.</li>
</ul>
</blockquote>
<p>The destination <code>dest_dir</code> needs to be defined. The whole directory structure after <code>/nesi/nearline/</code> will be created at the destination and the specified data written into it. For example,</p>
<pre><code>nlget nesi00000 /nesi/nearline/nesi00000/dir/to/results/ /nesi/nobackup/nesi00000</code></pre>
<p>will create the directory structure <code>/nesi/nobackup/nesi00000/nesi00000/<strong>dir/to/results/</strong></code> if that directory structure does not already exist, and copy the data within the <code>Results</code> directory into it.  Note that the output pathe will include the project root in the path.</p>
<blockquote class="blockquote-prereq">
<h3 id="prerequisites">Warning</h3>
<p>Any given file <strong>will not be retrieved</strong> if a file of the same name already exists in the destination directory. If you wish to retrieve a new copy of a file that already exists at the destination directory then you must either change the destination directory, or delete the existing copy of the file in the that directory.</p>
</blockquote>
<p><code>nlget</code> takes only one directory or one file list. <strong>Single files, if local, are treated as a file list</strong> and read line by line, searching for valid file names. A single Nearline file can only be retrieved using a local file list specifying the full path of the file to be retrieved.</p>
<h1 id="Nearlineearlyaccessuserguide-Purge">Purging/Removing files from nearline</h1>
<p>The <code>nlpurge</code> command deletes specified data on the Nearline file system permanently. The syntax is</p>
<pre><code>nlpurge [--nowait] &lt;src_dir&gt;<br>nlpurge [ --nowait ] &lt;projectID&gt; { &lt;src_dir&gt; | &lt;file_list&gt; }</code></pre>
<p>A <strong>directory</strong> <code>src_dir</code> already on Nearline <strong>(no single files accepted)</strong> or a file list <code>file_list</code> needs to be specified (see <code>nlput</code> above).</p>
<p>If the thing to be deleted is a directory, the project code is optional. If you are instead deleting the entries of a file list, the project code is compulsory, and moreover all entries in the file list must denote files within (or supposed to be within) the chosen project's Nearline directory.</p>
<blockquote class="blockquote-prereq">
<h3 id="nlpurge-file-list">Warnings</h3>
<ul>
<li>If a file list is used, it must be located within <code>/nesi/project</code> or <code>/nesi/nobackup</code> and referred to by its full path starting with one of those places (symlinks in the path are OK).</li>
<li>Paths to files or directories to be purged must be absolute and start with <code>/nesi/nearline</code>, whether supplied on the command line (as a directory) or as entries in a file list.</li>
<li>Purging the entire Nearline directory for a project, e.g. <code>nlpurge /nesi/nearline/nesi12345</code>, is not permitted. To empty a project's Nearline directory, you must purge its contents one by one (if directories), or by means of a filelist (if files).</li>
</ul>
</blockquote>
<h1 id="Nearlineearlyaccessuserguide-Viewjobstatus">View nearline  job status</h1>
<p>The tool <code>nljobstatus</code> provides current status of submitted (queued, running and completed) tasks. The syntax is:</p>
<pre><code>nljobstatus [ &lt;jobid&gt; ]</code></pre>
<p>If no job ID is specified the full list of your successfully submitted and accepted jobs is returned. In this list, each job looks like the following:</p>
<pre><code>$ nljobstatus
+----------+------------+----------------------------+-----------+-------------+
|  Jobid   | Project ID |         Job Status         | Job Host  |  Job User   |
+----------+------------+----------------------------+-----------+-------------+
| 4e23f517 |     13     |   job done successfully    | librarian | userName    |
| -dfef-40 |            |                            |           |             |
| e9-a83c- |            |                            |           |             |
| 3da78b06 |            |                            |           |             |
|   0310   |            |                            |           |             |
+----------+------------+----------------------------+-----------+-------------+
</code></pre>
<p>With a job identifier <code>jobid</code>, information for a specific job can be listed:</p>
<pre><code>$ nljobstatus 4e23f517-dfef-40e9-a83c-3da78b060310
+--------------------------------------+
|                Jobid                 |
+--------------------------------------+
| 4e23f517-dfef-40e9-a83c-3da78b060310 |
+--------------------------------------+
+------------+-----------------------+-----------+-------------+
| Project ID |      Job Status       | Job Host  |  Job User   |
+------------+-----------------------+-----------+-------------+
|     13     | job done successfully | librarian | userName    |
+------------+-----------------------+-----------+-------------+
+---------------------+---------------------+---------------------+
|   Job Start Time    |   Job Update Time   |    Job End Time     |
+---------------------+---------------------+---------------------+
| 2019-09-13T03:11:22 | 2019-09-13T03:11:44 | 2019-09-13T03:11:45 |
+---------------------+---------------------+---------------------+
</code></pre>
<p>If an <code>nlput</code> or <code>nlpurge</code> is running in that project, the project is locked until the task is finished.</p>
<p><strong>If a job stays in one state for an unexpectedly long time, please <a href="https://support.nesi.org.nz/hc/request/new">contact NeSI Support</a></strong>.</p>
<h1 id="Nearlineearlyaccessuserguide-Viewquota">View nearline quota</h1>
<p>With the command <code>nlquotalist</code>, the usage and limits of a Nearline project quota can be listed:</p>
<div class="confluence-information-macro-body">
<pre><code>nlquotalist &lt;projectID&gt;</code></pre>
</div>
<p>The output looks like:</p>
<pre><code>$ nlquotalist nesi12345
Projectname                                       Available           Used                Inodes         IUsed
___________________________________________________________________________________________________________________________
nesi12345                                         30.00 TB            27.16 TB            1000000        412
</code></pre>
<p>This quota is different from the project quota on GPFS (<code>/nesi/project/&lt;projectID&gt;</code>).</p>
<p><a name="directory_mapping"></a></p>
<h1 id="Nearlineearlyaccessuserguide-Datamanagement">Data management</h1>
<p>In case you have the same directory structure on your project and nobackup directories, be careful when archiving data from both. They will be merged in the Nearline file system. Further, when retrieving data from Nearline, keep in mind that the directory structure up to your projectID will be retrieved:</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360002703556" alt="librarian_get_put.jpeg"></p>
<h1 id="Nearlineearlyaccessuserguide-Underlyingmechanism">Underlying mechanism</h1>
<p>The Nearline file system consists of two parts: Disk, mainly for buffering data, and the tape library. It consists of a client running on the login/compute node and the backend on the Nearline file system. It is important to know that <strong>even if you cancel a client process, the corresponding backend process remains scheduled or running</strong> until finished.</p>
<p><span class="inline-comment-marker" data-ref="78239edd-ceab-49eb-a747-0140db19a948">The process of what data goes into tape and when is automated</span>, and is not something you will have control over. The service is designed to optimise interaction with the Nearline filesystem and avoid problem workloads for the benefit of all users.</p>
<p>If your files are on tape, it will take time to retrieve them. Access to tape readers is on a first come first served basis, and the amount of wait time will vary dramatically depending on overall usage. We cannot guarantee access to your files within any particular timeframe, and indeed wait times could be hours or even in some cases more than a day.</p>
<h1>Known issues</h1>
<blockquote class="blockquote-prereq">
<h3 id="retrieval">Retrievals</h3>
<p>Some users of Nearline have reported that attempts to retrieve files from tape using <code>nlget</code> (see below) will not retrieve all files. Instead, only some files will come back, and the job will finish with the following output:</p>
<pre><code>recall failed some syncs might still run (042)</code></pre>
<p>We are aware of this problem, which is caused by the Nearline job timing out while waiting for a tape drive to become available. This problem may also occur if you attempt to retrieve multiple files, together adding to a large amount of data, from Nearline.</p>
<p>Unfortunately, a proper fix requires a fundamental redesign and rebuild of the Nearline server architecture, work that is on hold pending decisions regarding the direction in which we take NeSI's data services. We appreciate your patience as we work through these decisions.</p>
<p>In the meantime, if you encounter this problem, the recommended workaround is to wait a couple of hours (or overnight, if at the end of a day) and try again once a tape drive is more likely to be free. You may have to try several times, waiting between each attempt. We apologise for any inconvenience caused to you by tape drive contention.</p>
</blockquote>
<p> </p>
<h1 id="Nearlineearlyaccessuserguide-Supportcontact">Support contact</h1>
<p>Please <strong>send feedback</strong> about your user experience at <a class="external-link" href="https://support.nesi.org.nz/hc/requests/new" rel="nofollow">https://support.nesi.org.nz/hc/requests/new</a>, which may include functionality issues, intuitive or counter-intuitive behaviours, behaviours or features that you like, suggestions for improvements, transfers taking too long, etc.</p>
<p>We welcome feedback from our users.</p>