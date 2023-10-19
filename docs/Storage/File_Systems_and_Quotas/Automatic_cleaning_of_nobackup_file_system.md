---
created_at: '2019-09-15T23:36:59Z'
hidden: false
label_names: []
position: 1
title: Automatic cleaning of nobackup file system
vote_count: 4
vote_sum: 2
zendesk_article_id: 360001162856
zendesk_section_id: 360000033936
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p><a name="criteria"></a>The automatic cleaning feature is a programme of regular deletion of selected files from project directories in our nobackup file system. We do this to optimise the availability of this file system for active research computing workloads and to ensure NeSI can reliably support large-scale compute and analytics workflows.</p>
<p>Files are deleted if they meet <strong>all</strong> of the following criteria:</p>
<ul>
<li>The file was first created more than 120 days ago, and has not been accessed, and neither its data nor its metadata has been modified, for at least 120 days.</li>
<li>The file was identified as a candidate for deletion two weeks previously, and as such is listed in a the project's nobackup <code>.policy</code> directory.</li>
</ul>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tip</h3>
<p>You can get a list of files marked for deletion with the command <code>nn_doomed_list</code>.</p>
<p>Usage: nn_doomed_list [-h] [--project [PROJECTS]] [--unlimited] [--limit LENGTHLIMIT]</p>
<p><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">optional arguments:</span></p>
<p>-h, --help show this help message and exit<br>--project [PROJECTS], -p [PROJECTS]<br>Comma-separated list of projects to process. If not given, process all projects of which the user is a member<br>--unlimited, -u Do not limit the length of the output file<br>--limit LENGTHLIMIT, -l LENGTHLIMIT<br>Maximum length of the output file (lines)</p>
<p>If no arguments are given, nn_doomed_list checks and displays all project directories the user is a member of. </p>
<p>Default limit of the output file is 40 lines. </p>
</blockquote>
<p>The general process will follow a schedule as follows:</p>
<ul>
<li>
<strong>Notify</strong><span style="font-weight: 400;"> (at 106 days), then two weeks later </span><strong>Delete</strong><span style="font-weight: 400;"> (at 120 days)</span>.</li>
<li>
<span style="font-weight: 400;">Every fortnight on Tuesday morning, we will be reviewing files stored in the nobackup filesystem and identifying candidates for expiry</span>.</li>
<li>Project teams will be notified by email if they have file candidates for deletion. Emails will be sent two weeks in advance of any deletion taking place.
<blockquote class="blockquote-warning">
<h3 id="email">Warning</h3>
<p>Due to the nature of email, we cannot guarantee that any particular email message will be successfully delivered and received, for instance our emails could be blocked by your mail server or your inbox could be too full. We suggest that you check <code>/nesi/nobackup/&lt;project_code&gt;/.policy</code> (see below) for a list of deletion candidates, for each of your projects, whether you received an email from us or not.</p>
</blockquote>
</li>
<li>
<span style="font-weight: 400;">Immediately after deletion is complete, a new set of candidate files will be identified for expiry during the next automated cleanup</span>. These candidate files are all files within the project's nobackup that have not been created, accessed or modified within the last 106 days.</li>
</ul>
<p>A file containing the list of candidates for deletion during the next cleanup, along with the date of the next cleanup, will be created in a directory called <code>.policy/to_delete</code> inside the project's nobackup directory. For example, the candidates for future deletion from the directory <code>/nesi/nobackup/nesi12345</code> are recorded in <code>/nesi/nobackup/nesi12345/.policy/to_delete/&lt;date&gt;.filelist.gz</code>. Project team members are able to view the contents of <code>.policy</code> (but not delete or modify those contents). The gzip compressed filelist can be viewed and searched with the <code>zless</code> and <code>zgrep</code> commands respectively, e.g., <code>zless /nesi/nobackup/nesi12345/.policy/to_delete/&lt;date&gt;.filelist.gz</code>.</p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Warning</h3>
<p>Objects other than files, such as directories and symbolic links, are not deleted under this policy, even if at deletion time they are empty, broken, or otherwise redundant. These entities typically take up no disk space apart from a small amount of metadata, but still count towards the project's inode (file count) quota.</p>
</blockquote>
<h2>What should I do with expiring data on the nobackup filesystem?</h2>
<p>If the data is transient and no longer required for continued processing on NeSI then we would appreciate if you deleted it yourself, but you can also let the automated process do this.</p>
<p>If you have files identified as candidates for deletion that you need to keep beyond the scheduled expiry date, you have four options:</p>
<ul>
<li>Move the file to your persistent project directory, e.g., <code>/nesi/project/nesi12345</code>. You may need to request more disk space, more inodes, or both, in your persistent project directory before you can do this. <a href="https://support.nesi.org.nz/hc/en-gb/requests/new" target="_blank" rel="noopener">Submit a Support request</a>. We assess such requests on a case-by-case basis.  Note:  You can save space by compressing data.  Standard tools such as `gzip` `bzip2` etc are available.</li>
<li>Move or copy the file to a storage system outside NeSI, for example a research storage device at your institution. We expect most projects to do this for finalised output data and appreciate prompt egress of data once it is no longer used for processing.</li>
<li>
<strong>Modify</strong> the file before the deletion date, in which case the file will not be deleted even though it is listed in <code>.policy</code>. This must only be done in cases where you expect to begin active use of the data again within the next month.</li>
<li>Note: Accessing (Open/Close and Open/Save) or Moving (`mv`) does not update the timestamp of the file. Copying (`cp`) does create a new timestamped file.<br>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Warning</h3>
<p>Doing this for large numbers of files, or for files that together take up a large amount of disk space, in your project's nobackup directory, without regard for your project's computational activity, constitutes a breach of <a href="https://www.nesi.org.nz/services/high-performance-computing/guidelines/acceptable-use-policy">NeSI's acceptable use policy</a>.</p>
</blockquote>
</li>
</ul>
<p><a name="advice"></a></p>
<h2>Where should I put my data?</h2>
<table>
<tbody>
<tr>
<td><strong>How often will my team's HPC jobs be accessing the data?</strong></td>
<td><strong>How often will my team's HPC jobs be modifying the data? </strong></td>
<td><strong>Recommended option </strong></td>
</tr>
<tr>
<td>Often</td>
<td>Often (at least once every two months)</td>
<td>Leave in the nobackup directory (but ensure key result data is copied to the persistent project directory)</td>
</tr>
<tr>
<td>Often</td>
<td>Seldom</td>
<td>Put in the persistent project directory</td>
</tr>
<tr>
<td>Seldom</td>
<td>Seldom</td>
<td>
<p>Store the data elsewhere (e.g. at your institution)</p>
</td>
</tr>
</tbody>
</table>
<p>In general, the persistent project directory should be used for reference data, tools, and job submission and management scripts. The nobackup directory should be used for holding large reference working datasets (e.g., an extraction of compressed input data) and as a destination for writing and modifying temporary data. It can also be used to build and edit code, provided that the code is under version control and changes are regularly checked into upstream revision control systems.</p>
<h2>If I need a file that was deleted from nobackup, what should I do?</h2>
<p>Please <a href="https://support.nesi.org.nz/hc/en-gb/requests/new" target="_self">contact our support team</a> as soon as possible after you find that the file is missing. To reduce the risk of this outcome again in future, please <a href="https://support.nesi.org.nz/hc/en-gb/requests/new" target="_self">contact us in advance</a> so that we can discuss your data storage options with you.</p>
<h2>I have research data on nobackup that I can't store in my project directory or at my institution right now. What should I do?</h2>
<p>Please <a href="https://support.nesi.org.nz/hc/en-gb/requests/new" target="_self">contact our support team</a> without delay so we can discuss your short- and medium-term data storage needs. Our intention is to work with you to move your valuable data to an appropriate combination of:</p>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">persistent project storage on NeSI,</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">high performance /nobackup storage (temporary scratch space) on NeSI,</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">slow nearline storage (not released yet, on our roadmap), and </span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">institutional storage infrastructure.</span></li>
</ul>
<h2>User Webinars</h2>
<p>On 14 and 26 November 2019, we hosted webinars to explain these upcoming changes and answer user questions. If you missed these sessions, the archived materials are available at the links below:</p>
<ul>
<li>
<em><strong>Video recordings: </strong></em><br>14 November 2019 - <a href="https://youtu.be/KPNNSwDJU7A">https://youtu.be/KPNNSwDJU7A</a> <br>26 November 2019 <em>(repeat of 14 Nov session)</em> - <a href="https://youtu.be/iVTdlsiBTB4">https://youtu.be/iVTdlsiBTB4</a>
</li>
<li>
<em><strong>Slides: </strong></em><br><em>(same slides were used for both presentations)</em><br><a href="https://drive.google.com/file/d/1kLwghsj9es8oMqdWj-VhUvaklW6JkrwO/view?usp=sharing">https://drive.google.com/file/d/1kLwghsj9es8oMqdWj-VhUvaklW6JkrwO/view?usp=sharing</a>  </li>
<li>
<em><strong>Q&amp;A transcriptions: </strong></em><br>14 November 2019 - <a href="https://drive.google.com/file/d/1tImzibZ3DcN7QOttZEZoYsR43mEiS5KJ/view?usp=sharing" target="_blank" rel="noopener">https://drive.google.com/file/d/1tImzibZ3DcN7QOttZEZoYsR43mEiS5KJ/view?usp=sharing</a> <br>26 November 2019 - <a href="https://drive.google.com/file/d/1OSb71hhZnjnU9xsRALcpYM485va7aUxK/view?usp=sharing">https://drive.google.com/file/d/1OSb71hhZnjnU9xsRALcpYM485va7aUxK/view?usp=sharing</a>
</li>
</ul>
<h2> </h2>