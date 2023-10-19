---
created_at: '2021-08-27T03:30:10Z'
hidden: false
label_names: []
position: 3
title: Globus V5 Paths, Permissions, Storage Allocation
vote_count: 0
vote_sum: 0
zendesk_article_id: 4405623499791
zendesk_section_id: 360000040596
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<h2>Globus default directory</h2>
<p>If you point Globus File Manager to an endpoint collection where you have an account/access, it will open a single panel pointing to the root path directory, displayed as '<code>/home/&lt;username&gt;</code>'.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/4408734639887" alt="mceclip0.png"></p>
<h3> On NeSI's Māui/Mahuika clusters this means:</h3>
<table style="height: 160px; width: 728px;">
<thead>
<tr style="height: 44px;">
<th style="width: 178.783px; height: 44px;">Globus path</th>
<th style="width: 101.033px; height: 44px;">Visible to Globus</th>
<th style="width: 181.817px; height: 44px;">HPC Filesystem</th>
<th style="width: 130.15px; height: 44px;">Globus usage</th>
<th style="width: 120.217px; height: 44px;">Permissions</th>
</tr>
</thead>
<tbody>
<tr style="height: 44px;">
<td style="width: 170.783px; height: 44px;"><code>/home/&lt;username&gt;</code></td>
<td style="width: 93.0333px; height: 44px;">yes (default)</td>
<td style="width: 173.817px; height: 44px;"><code>/home/&lt;username&gt;</code></td>
<td style="width: 122.15px; height: 44px;">possible, not recommended</td>
<td style="width: 112.217px; height: 44px;">read and write access</td>
</tr>
<tr>
<td style="width: 170.783px; height: 36px;"><code>/nesi/nobackup/&lt;project_code&gt;</code></td>
<td style="width: 93.0333px; height: 36px;">yes</td>
<td style="width: 173.817px; height: 36px;"><code>/nesi/nobackup/&lt;project_code&gt;</code></td>
<td style="width: 122.15px; height: 36px;">yes</td>
<td style="width: 112.217px; height: 36px;">read and write access</td>
</tr>
<tr>
<td style="width: 170.783px; height: 36px;"><code>/nesi/project/&lt;project_code&gt;</code></td>
<td style="width: 93.0333px; height: 36px;">yes</td>
<td style="width: 173.817px; height: 36px;"><code>/nesi/project/&lt;project_code&gt;</code></td>
<td style="width: 122.15px; height: 36px;">yes</td>
<td style="width: 112.217px; height: 36px;">
<strong>read only</strong> access</td>
</tr>
</tbody>
</table>
<p> </p>
<p>For more information about NeSI filesystem, check <a style="background-color: #ffffff;" href="https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas" target="_self" rel="undefined">here</a>.</p>
<h2>Performing Globus transfers to/from Māui/Mahuika</h2>
<ul>
<li>If transferring files off the cluster, move/copy files onto <code>/nesi/project</code> or <code>/nesi/nobackup</code> first, via your HPC access</li>
<li>Sign in to Globus and navigate the file manager to the path associated with your project (viz. <code>/nesi/project/&lt;project_code&gt;</code> or <code style="font-size: 15px;">/nesi/nobackup/&lt;project_code&gt;</code>)</li>
<li>Click the "two-panels" area in the file manager and select the other endpoint</li>
<li>Select source of transfer</li>
<li>Transfer data (from), using the appropriate "start" button</li>
<li>If transferring files onto the cluster, the fastest location will be <code>/nesi/nobackup/&lt;project_code&gt;</code>
</li>
</ul>
<h3>Tips</h3>
<p>1.  Globus bookmarks can be created for <code>/nesi/project</code> or <code>/nesi/nobackup</code> paths and these bookmarks pinned.</p>
<p>2.  Symbolic links can be created in your <em>project</em> directories and <em>nobackup</em> directories to enable easy moving of files to and from.<br>To create a symbolic link from a first to a second directory and vice-versa (using <em>full</em> paths for &lt;first&gt; and &lt;second&gt;):</p>
<pre>$ cd &lt;first&gt;<br>$ ln -s &lt;full_path_to_second&gt; &lt;alias_to_second&gt;<br> <br>$ cd &lt;second&gt;<br>$ ln -s &lt;full_path_to_first&gt;  &lt;alias_to_first&gt;<br><br></pre>
<p>Alias can be any value which is convenient to you. .i.e. easy to identify <br>After you do this, there will be an alias listed in each directory that points to the other directory. You can see this with the <strong>ls</strong> command, and <strong>cd</strong> from each to the other using its alias.</p>
<p> </p>