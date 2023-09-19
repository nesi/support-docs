---
created_at: '2018-05-21T05:14:00Z'
hidden: false
label_names: []
position: 2
title: File permissions and groups
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000205435
zendesk_section_id: 360000033936
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <blockquote class="blockquote-prereq">
<h3 id="see-also">See also</h3>
<ul>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360001237915" target="_self">How can I let my fellow project team members read or write my files?</a></li>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/4401821809679" target="_self">How can I give read-only team members access to my files?</a></li>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360000177256" target="_self">NeSI file systems and quotas</a></li>
</ul>
</blockquote>
<p>Access to data (i.e. files and directories) on NeSI is controlled by POSIX permissions, supplemented with Access Control Lists (ACLs). Default permissions differ from file system to file system.</p>
<h2>Group membership</h2>
<p>Each user has a private user group, of which that user is by default the only member. Each user is also a member of various other groups, such as:</p>
<ul>
<li>A group for each active NeSI project of which that user is a member</li>
<li>Groups for all active users, all active Mahuika users, all active Māui users, etc. as appropriate</li>
<li>A group representing all active NeSI users who are affiliated with the user's institution</li>
<li>Groups for specific licensed software to which that user has been granted access</li>
</ul>
<p>You can see which groups you are a member of at any time by running the following command on a Mahuika, Māui or Māui ancillary login node:</p>
<pre><code>groups</code></pre>
<h2>Files in home directories</h2>
<p>Your home directory is owned by you, and its group is usually your personal group. (For historical reasons, some NIWA users' home directories have <code>niwa_nesi_users</code> or <code>niwa_unix_users</code> as the group.) By default, files and directories that are created in your home directory, or copied to your home directory from another network or file system, inherit this ownership scheme. You can override these defaults depending on how you use the <code>cp</code>, <code>scp</code>, <code>rsync</code>, etc. commands. Please consult the documentation for your copying program.</p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Warning</h3>
<p>If you choose to preserve the original owner and group, but that owner and group (name or numeric ID) don't both exist at the destination, your files may end up with odd permissions that you can't fix, for example if you're copying from your workstation to NeSI.</p>
</blockquote>
<p>The default permissions mode for new home directories is as follows:</p>
<ul>
<li>The owner has full privileges: read, write, and (where appropriate) execute.</li>
<li>The group and world have no privileges.</li>
</ul>
<p>Some home directories have the "setgid" bit set. This has the effect that files and subdirectories created within the home directory will inherit the owner and group of their parent directory, rather than of the person doing the creating.</p>
<p>Home directories and their contents do not have any ACLs by default.</p>
<h2>Files in project directories</h2>
<p>Every new project almost always gets two directories, namely a persistent directory in <code>/nesi/project</code> and a scratch directory in <code>/nesi/nobackup</code>. Both these directories are group directories. Both top level project directories are owned by root (i.e. the super-user) and their group is the project group. Files and directories that are created in either place are also in the project group, but the owner is the creating user; or, if the entity doing the creating was an automatic process, the user in whose name the process ran.</p>
<p>Your project directory and nobackup directory should both have the "setgid" bit set, so that files created in either directory inherit the project group.</p>
<blockquote class="blockquote-warning">
<h3 id="proj-setgid">Warning</h3>
<p>The setgid bit only applies the directory's group to files that are newly created in that directory, or copied to the directory over the internet. If a file or directory is moved or copied from elsewhere on the cluster, using for example the <code>mv</code> or <code>cp</code> command, that file or directory will keep its original owner and group. Moreover, a directory moved from elsewhere will probably not have its setgid bit set, meaning that files and subdirectories later created within that directory will inherit neither the group nor the setgid bit.</p>
<p>You probably don't want this to happen. For instructions on how to prevent it, please see our article: <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001237915" target="_self">How can I let my fellow project team members read or write my files?</a></p>
</blockquote>
<p>By default, the world, i.e. people not in the project team, have no privileges in respect of a project directory, with certain exceptions.</p>
<p>Unlike home directories, project directories are set up with ACLs. The default ACL for a project directory is as follows:</p>
<ul>
<li>The owner of a file or directory is allowed to read, write, execute and modify the ACL of that file or directory</li>
<li>Every member of the file or directory's group is allowed to read, write and execute the file or directory, but not modify its ACL</li>
<li>Members of NeSI's support team are allowed to read and execute the file or directory, but not change it or modify its ACL</li>
</ul>
<p>Some projects also have read and execute privileges granted to a group "apache-web02-access".</p>
<p>Each directory has two ACLs: One is for the directory itself, and the other is for files and directories that are created in future within that directory. We have set up both of these ACLs to be the same as each other for the two top level project directories.</p>
<blockquote class="blockquote-tip">
<h3 id="read-only-group">Tip</h3>
<p>Some project teams, especially those with broader memberships, benefit from read-only groups. A read-only group gets added to a project's ACL once, and then individual members can be added to or removed from that group as required. This approach involves much less editing of file metadata than adding and removing individuals from the ACLs directly. If you would like a read-only group created for your project, please <a href="https://support.nesi.org.nz/hc/requests/new" target="_self">contact us</a>.</p>
</blockquote>
<p>The owner of a file or directory may create, edit or revoke that file or directory's ACL and, in the case of a directory, also the directory's default (heritable) ACL.</p>
<blockquote class="blockquote-warning">
<h3 id="edit-acl">Warning</h3>
<p>Every time you edit an ACL of a file in the home or persistent project directory, the file's metadata changes and triggers a backup of that file. Doing so recursively on a large number of files and directories, especially if they together amount to a lot of disk space, can strain our backup system. Please consider carefully before doing a recursive ACL change, and if possible make the change early on in the life of the project on NeSI, so that only a few files are affected.</p>
</blockquote>
<h2>Other directories</h2>
<p>We may from time to time create and maintain other directories, for example for users of a particular piece of software or database. If you believe you have data storage requirements that don't neatly fit within the home and project scheme described above, please <a href="https://support.nesi.org.nz/hc/requests/new" target="_self">contact our support team</a>. If we agree to set up a special-purpose directory for you, we will discuss and agree upon a suitable permissions model.</p>