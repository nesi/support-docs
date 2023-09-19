---
created_at: '2018-05-02T04:06:16Z'
hidden: false
label_names:
- info
- mahuika
- storage
- maui
- quota
position: 0
title: NeSI File Systems and Quotas
vote_count: 3
vote_sum: 3
zendesk_article_id: 360000177256
zendesk_section_id: 360000033936
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <blockquote class="blockquote-prereq">
<h3 id="compression-note">New Feature</h3>
<p><a href="#h_01GZ2Q7PG53YQEKFDDWTWHHDVT" target="_self" rel="undefined">Transparent File Compression</a> - we have recently started rolling out compression of inactive data on the NeSI Project filesystem. Please see the <a href="#h_01GZ2Q22EAZYMA7E9XG9F5FC1Z" target="_self">documentation below</a> to learn more about how this works and what data will be compressed.</p>
</blockquote>
<p> </p>
<p><a href="https://support.nesi.org.nz/hc/articles/360000163695">Māui</a> and <a href="https://support.nesi.org.nz/hc/articles/360000163575">Mahuika</a>, along with all the ancillary nodes, share access to the same IBM Storage Scale file systems. Storage Scale was previously known as Spectrum Scale, and before that as GPFS, or General Parallel File System - we'll generally refer to it as "Scale" where the context is clear.</p>
<p>You may query your actual usage and disk allocations using the following command: </p>
<p><code>$ nn_storage_quota</code></p>
<p>The values for 'nn_storage_quota' are updated approximately every hour and cached between updates.</p>
<h2><img src="https://support.nesi.org.nz/hc/article_attachments/360003251796" alt="neSI_filetree.svg" width="629" height="578"></h2>
<h1>File System Specifications</h1>
<table class="table table-bordered" style="tr td: first-child {    white-space:nowrap;">
<tbody>
<tr>
<td style="width: 84.1875px;"><span><strong>Filesystem</strong></span></td>
<td style="width: 119px;"><span><strong>/home</strong></span></td>
<td style="width: 135px;"><span><strong>/nesi/project</strong></span></td>
<td style="width: 188px;"><span><strong>/nesi/nobackup</strong></span></td>
<td style="width: 116.09375px;"><span><strong>/nesi/nearline</strong> </span></td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>Default disk space <br></strong></span></td>
<td style="width: 119px;"> </td>
<td style="width: 135px;"> </td>
<td style="width: 188px;"> </td>
<td style="width: 116.09375px;" rowspan="3">
<span>No default; allocations are based on eligibility and technical requirements</span><br><span> </span><span> </span>
</td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>    - soft quota</strong></span></td>
<td style="width: 119px;"><span>20 GB</span></td>
<td style="width: 135px;"><span>100 GB<br></span></td>
<td style="width: 188px;">10 TB</td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>    - hard quota</strong></span></td>
<td style="width: 119px;"> </td>
<td style="width: 135px;"><span>110 GB</span></td>
<td style="width: 188px;">12 TB</td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>Default file count (inode) <br></strong></span></td>
<td style="width: 119px;"> </td>
<td style="width: 135px;"> </td>
<td style="width: 188px;"> </td>
<td style="width: 116.09375px;" rowspan="3">
<span>No default; allocations are based on eligibility and technical requirements</span><br><span> </span><span> </span>
</td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>    - soft quota</strong></span></td>
<td style="width: 119px;"><span>1,000,000 files</span></td>
<td style="width: 135px;"><span>100,000 files</span></td>
<td style="width: 188px;"><span>1,000,000 files</span></td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>    - hard quota</strong></span></td>
<td style="width: 119px;"><span>1,100,000 files</span></td>
<td style="width: 135px;"><span>110,000 files</span></td>
<td style="width: 188px;"><span>1,100,000 files</span></td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>Intended use</strong></span></td>
<td style="width: 119px;"><span>User-specific files such as configuration files, environment setup, source code, etc.</span></td>
<td style="width: 135px;"><span>Persistent project-related data, project-related software, etc.</span></td>
<td style="width: 188px;"><span>Data created or used by compute jobs that is intended to be temporary</span></td>
<td style="width: 116.09375px;"><span>Medium- to long-term storage of research data associated with past, present or planned compute projects</span></td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>Total capacity</strong></span></td>
<td style="width: 119px;"><span>175 TB</span></td>
<td style="width: 135px;"><span>1,590 TB</span></td>
<td style="width: 188px;"><span>4,400 TB</span></td>
<td style="width: 116.09375px;"><span>Will grow as tapes are purchased</span></td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>Data retention time</strong></span></td>
<td style="width: 119px;"><span>180 days after the user ceases to be a member of any active project</span></td>
<td style="width: 135px;"><span>90 days after the end of the project's last HPC Compute &amp; Analytics allocation. See also Transparent File Data Compression.</span></td>
<td style="width: 188px;">
<span>With certain exceptions, individual files will be deleted after being untouched for 120 days. See <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001162856" target="_self">Automatic cleaning of nobackup file system</a> for more information. </span><span>90 days after the end of the project's last HPC Compute &amp; Analytics allocation, all remaining data is subject to deletion.</span>
</td>
<td style="width: 116.09375px;"><span>180 days after the end of the project's last nearline storage allocation</span></td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>Data backup schedule<br>(Excluding snapsots)</strong></span></td>
<td style="width: 119px;"><span>Daily, last 10 versions of any given file retained for up to 90 days.</span></td>
<td style="width: 135px;"><span>Daily, last 10 versions of any given file retained for up to 90 days.</span></td>
<td style="width: 188px;"><span>None</span></td>
<td style="width: 116.09375px;"><span>Replication  between Wellington and Auckland tape libraries (under development)</span></td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>Snapshots</strong></span></td>
<td style="width: 119px;"><span>Daily (retention period 7 days)</span></td>
<td style="width: 135px;"><span>Daily (retention period 7 days)</span></td>
<td style="width: 188px;"><span>None</span></td>
<td style="width: 116.09375px;"><span>None</span></td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>Access speed</strong></span></td>
<td style="width: 119px;"><span>Moderate</span></td>
<td style="width: 135px;"><span>Moderate</span></td>
<td style="width: 188px;"><span>Fast</span></td>
<td style="width: 116.09375px;"><span>Slow</span></td>
</tr>
<tr>
<td style="width: 84.1875px;"><span><strong>Access interfaces</strong></span></td>
<td style="width: 119px;">
<ul>
<li><span>Native Scale mounts</span></li>
<li><span>SCP</span></li>
<li><span>Globus data transfer</span></li>
</ul>
</td>
<td style="width: 135px;">
<ul>
<li><span>Native Scale mounts</span></li>
<li><span>SCP</span></li>
</ul>
</td>
<td style="width: 188px;">
<ul>
<li><span>Native Scale mounts</span></li>
<li><span>SCP</span></li>
<li><span>Globus data transfer</span></li>
</ul>
</td>
<td style="width: 116.09375px;"><span>Nearline commands</span></td>
</tr>
</tbody>
</table>
<h3><strong>Soft versus hard quotas</strong></h3>
<p>We use Scale soft and hard quotas for both disk space and inodes.</p>
<ul>
<li>Once you exceed a fileset's soft quota, a one-week countdown timer starts. When that timer runs out, you will no longer be able to create new files or write more data in that fileset. You can reset the countdown timer by dropping down to under the soft quota limit.</li>
<li>You will not be permitted to exceed a fileset's hard quota at all. Any attempt to try will produce an error; the precise error will depend on how your software responds to running out of disk space.</li>
</ul>
<p>When quotas are first applied to a fileset, or are reduced, it is possible to end up with more data or files in the fileset than the quota allows for. This outcome does not trigger deletion of any existing data, but will prevent creation of new data or files.</p>
<h3><strong>Notes:</strong></h3>
<ul>
<li>You may request an increase in storage and inode quota if needed by a project. This may in turn be reduced as part of managing overall risk, where large amounts of quota aren't used for a long period (~6 Months).</li>
<li>If you need to compile or install a software package that is large or is intended for use by a project team, please build it in <code>/nesi/project/&lt;project_code&gt;</code> rather than <code>/home/&lt;username&gt;</code>.</li>
<li>As the <code>/nesi/nobackup</code> file system provides the highest performance, input files should be moved or copied to this file system before starting any job that makes use of them. Likewise, job scripts should be written so as to write output files to the <code>/nesi/nobackup</code> file system. If you wish to keep your data for the long term, you can include as a final part of your job script an operation to copy or move the output data to the <code>/nesi/project</code> file system.</li>
<li>Keep in mind that data on <code>/nesi/nobackup</code> is not backed up, therefore users are advised to move valuable data to <code>/nesi/project/&lt;project_code&gt;</code>, or, if the data is seldom used, to other storage such as an institutional storage facility, as soon as batch jobs are completed. Please do <strong>not</strong> use the <code>touch</code> command to prevent the cleaning policy from removing files, because this behaviour would deprive the community of a shared resource.</li>
</ul>
<h2>/home</h2>
<p>This file system is accessible from login, compute and ancillary nodes. Users should <strong>not</strong> run jobs from this filesystem. All home directories are backed up daily, both via the Spectrum Protect backup system, which retains the last 10 versions of all files for up to 90 days, and via <a href="https://support.nesi.org.nz/hc/articles/360000207315" target="_self" rel="undefined">Scale snapshots</a>. No cleaning policy will be applied to your home directory as long as your My NeSI account is active and you are a member of at least one active project.</p>
<h2>/nesi/project</h2>
<p>This filesystem is accessible from all login, compute and ancillary nodes. Contents are backed up daily, via the Spectrum Protect backup system, which retains the last 10 versions of all files for 90 days. No cleaning policy is applied.</p>
<p>It provides storage space for datasets, shared code or configuration scripts that need to be accessed by users within a project, and <a href="https://support.nesi.org.nz/hc/articles/360000205435">potentially by other projects</a>. Read and write performance increases using larger files, therefore you should consider archiving small files with the <code>nn_archive_files</code> utility, or a similar archiving package such as <code>tar</code> .</p>
<p>Each NeSI project receives quota allocations for <code>/nesi/project/&lt;project_code&gt;</code>, based on the requirements you tell us about in your <a href="https://my.nesi.org.nz/html/request_project" target="_self">application for a new NeSI project</a>, and separately covering disk space and number of files.</p>
<h2>/nesi/nobackup</h2>
<p>The <code>/nesi/nobackup</code> file system has the highest performance of all NeSI file systems, with greater than 140 GB/s bandwidth from compute nodes to disk. It provides access to a very large (4.4 PB) resource for short-term project usage.</p>
<p>To prevent project teams from inadvertently bringing the file system down for everyone by writing unexpectedly large amounts of data, we apply per-project quotas to both disk space and number of files on this file system. The default per-project quotas are as described in the above table; if you require more temporary (scratch) space for your project than the default quota allows for, you can discuss your requirements with us during <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000202136" target="_self">the project application process</a>, or <a href="https://support.nesi.org.nz/hc/requests/new" target="_self">contact our support team</a> at any time.</p>
<p><span class="wysiwyg-color-black">To ensure this file system remains fit-for-purpose, we are rolling out a regular cleaning policy as described in <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001162856" target="_self">Automatic cleaning of nobackup filesystem</a>.</span></p>
<p>Do not use the <code>touch</code> command or an equivalent to prevent the cleaning policy from removing unused files, because this behaviour would deprive the community of a shared resource.</p>
<p>The purpose of this policy is to ensure that any user will be able to analyse datasets up to 1 PB in size.</p>
<h2>/nesi/nearline</h2>
<blockquote class="blockquote-tip">
<h3 id="nearline-not-available">Note</h3>
<p>The nearline service, including its associated file systems, is in an Early Access phase, and allocations are by invitation. We appreciate your patience as we develop, test and deploy this service. If you would like to participate in the Early Access Programme, please <a href="https://support.nesi.org.nz/hc/requests/new" target="_self">contact our support team</a>.</p>
</blockquote>
<p>The <code>/nesi/nearline</code> filesystem is a data cache for the Hierarchical Storage Management System, which automatically manages the movement of files between high performance disk storage and magnetic tape storage in an Automatic Tape Library (ATL). Files will remain on <code>/nesi/nearline</code> temporarily, typically for hours to days, before being moved to tape. A catalogue of files on tape will remain on the disk for quick access.</p>
<p>See <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001169956" target="_self">this page</a> for more information about the nearline service.</p>
<h1>Snapshots</h1>
<p>If you have accidentally deleted data you can recover it from a <a href="https://support.nesi.org.nz/knowledge/articles/360000207315/en-gb?brand_id=30406">snapshot</a>. Snapshots are taken daily of <code>home/</code> and <code>project</code> directories If you cannot find it in a snapshot, please ask us to recover it for you by emailing <a href="mailto:support@nesi.org.nz?subject=Please%20Recover%20a%20File">NeSI Support</a>.</p>
<h1>Contributions of Small Files Towards Quotas</h1>
<p>The Scale file system makes use of a feature called <em>data-in-inode</em>. This feature will ensure that, once all of a (non-encrypted) file's required metadata has been written to our metadata storage, if all the file's data is able to fit within the file's remaining inode space (4 KiB minus metadata), it will be written there instead of to the data storage.</p>
<p>For files larger than 4 KiB (minus the space needed to store the file's metadata), the data written to disk will be stored in one or more sub-blocks of 256 KiB each (which are 1/32 of the filesystem Block Size), and the "size" allocated on disk will be rounded up to the nearest 256 KiB. Users or projects requiring many small files may find themselves using large amounts of disk space. Use of <em>data-in-inode</em> mitigates the effect of a large block size on such people and project teams.</p>
<p>However, very small files, as well as zero-size entities such as directories and symbolic links, still count towards the relevant fileset's inode quota. If therefore you expect you will need to store large numbers of very small files in your home directory or in a project's persistent storage, please <a href="https://support.nesi.org.nz/hc/en-gb/requests/new">contact our support team</a> to discuss your storage needs.</p>
<h1 id="h_01GZ2Q7PG53YQEKFDDWTWHHDVT">Transparent File Data Compression</h1>
<p>The Scale file system has the ability to transparently compress file data. That is, file contents/data can be compressed behind the scenes, taking up less space on disk, while appearing uncompressed to applications reading or altering the file. Scale automatically handles decompression before passing data to user-space applications. This in-line decompression may have a small IO performance/latency impact, though this is mitigated by space and bandwidth savings.</p>
<p>Transparent file data compression can be controlled and applied by users via file attributes, you can find out more about using this method on our <a href="https://support.nesi.org.nz/hc/en-gb/articles/6359601973135" target="_self">Data Compression support page</a>. File data compression can also be automatically applied by administrators through the Scale policy engine. We leverage this latter feature to regularly identify and compress inactive data on the <code>/nesi/project</code> file system.</p>
<h2 id="h_01GZ2Q22EAZYMA7E9XG9F5FC1Z">What Project data is automatically compressed?</h2>
<p>Our current policy compresses files that have not been accessed (either read from or written to) within the last 365 days, i.e., very inactive cold data. We may decrease this in future.</p>
<p>Additionally, we only automatically compress files in the range of 4kB - 10GB in size. Files larger than this can be compressed by user interaction - see the instructions for the<span> <code>mmchattr</code> command on the <a href="https://support.nesi.org.nz/hc/en-gb/articles/6359601973135" target="_self">Data Compression support page</a>. Also note that the Scale filesystem will only store compressed blocks when the compression space saving is &gt;=10%.</span></p>