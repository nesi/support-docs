---
created_at: '2020-04-17T09:40:49Z'
hidden: false
label_names: []
position: 3
title: Verifying uploads to Nearline storage
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001482516
zendesk_section_id: 360000042255
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>Our <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001169956" target="_blank" rel="noopener">Long-Term Storage Service</a> is currently in an Early Access phase, and we encourage researchers using the service to verify their data before deleting it from the project directory (persistent storage) or nobackup directory (temporary storage).</p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Service Status</h3>
<p>The verification options outlined below are intended to support the Early Access phase of Nearline development. Verification options may change as the Early Access Programme continues and as the Nearline service moves into production. We will update our documentation to reflect all such changes.</p>
<p>Your feedback on which verification options you think are necessary will help us decide on future directions for the Nearline service. Please <a class="external-link" href="https://support.nesi.org.nz/hc/requests/new" rel="nofollow">contact our support team</a> to request verification or to offer suggestions regarding this or any other aspect of our Nearline service.</p>
</blockquote>
<p>There are several options for verification, depending on the level of assurance you require.</p>
<h1>Level 1: Transfer status report</h1>
<p>The most basic form of verification is to look at the results of <code>nljobstatus</code>. If all the Nearline job IDs associated with movement of data to Nearline (i.e. <code>nlput</code> commands) report <code>job done successfully</code>, that gives you a basic level of confidence that the files were in fact copied over to nearline.</p>
<blockquote class="blockquote-warning">
<h3 id="verification-level-1">Warning</h3>
<p>The above check is reliable only if <em>all</em> <code>nlput</code> commands were concerned solely with uploading new files to nearline. Because of the way <code>nlput</code> is designed, a command trying to update files that already existed on nearline will silently skip those files and still report success.</p>
</blockquote>
<h1>Level 2: File counts and sizes</h1>
<p>You can get a higher level of assurance by checking the number of files, and their sizes and last modified times, in a particular directory on nearline, and optionally to compare that number and size to the corresponding directory on <code>/nesi/project</code> or <code>/nesi/nobackup</code>. We can also enable comparisons of file permissions if requested, though differences in permissions or even modification times do not necessarily suggest a problem as long as the names and sizes are the same. If you are interested in verifying file permissions, please <a href="https://support.nesi.org.nz/hc/requests/new" target="_self">contact our support team</a>.</p>
<p>To get a list of file names, sizes and dates in a particular directory on nearline, run the following command with the necessary modifications. Note that the <code>nlcompare</code> command traverses all subdirectories within your chosen directory, and may therefore take some time if you verify a directory at the top of a complex directory tree.</p>
<pre><code>nlcompare &lt;local_directory&gt; &lt;nearline_directory&gt;</code></pre>
<p>This command will generate lists of files giving their last modified times, sizes and file paths. If there are any differences, the lists will be kept and you will be invited to compare the lists against each other, which you can do using a comparison program such as <code>diff</code> or <code>vimdiff</code>.</p>
<blockquote class="blockquote-warning">
<h3 id="verification-level-2">Warning</h3>
<p>The above check is useful only if the corresponding files in <code>/nesi/project</code> and/or <code>/nesi/nobackup</code> have not been modified or deleted, nor any new files added, since they were copied to nearline. For this reason, if you want to carry out this level of checking, you should do so as soon as possible after you have established that the <code>nlput</code> operation completed successfully.</p>
</blockquote>
<h1>Level 3: Checksums</h1>
<p>For especially important files, you can get a still higher level of assurance by retrieving those files individually or in small numbers from nearline and running checksums (e.g. SHA256 sums) on them, comparing the checksums to the corresponding original files in <code>/nesi/project</code> or <code>/nesi/nobackup</code>. If the checksums come out identical, it is virtually certain that the files contain the same data, even if their modification dates and times are reported differently.</p>
<blockquote class="blockquote-warning">
<h3 id="verification-level-3">Warning</h3>
<p>The above check is reliable only if the corresponding file in <code>/nesi/project</code> and/or <code>/nesi/nobackup</code> has not been modified since it was copied to nearline. For this reason, if you want to carry out this level of checking, you should do so as soon as possible after you have established that the <code>nlput</code> operation completed successfully and the file has been migrated to tape.</p>
<p>Also, this check is very expensive, so you should not perform it on large numbers of files or on files that collectively take up a lot of disk space. Instead, please reserve this level of verification for your most valuable research data.</p>
</blockquote>