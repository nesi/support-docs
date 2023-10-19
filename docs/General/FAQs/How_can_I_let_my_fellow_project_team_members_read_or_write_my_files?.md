---
created_at: '2019-11-07T04:11:03Z'
hidden: false
label_names: []
position: 0
title: How can I let my fellow project team members read or write my files?
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001237915
zendesk_section_id: 360000039036
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<blockquote class="blockquote-prereq">
<h3 id="see-also">See also</h3>
<p><a href="https://support.nesi.org.nz/hc/en-gb/articles/360000205435" target="_self">File permissions and groups</a></p>
</blockquote>
<p dir="auto">If you move or copy a file or directory from one project directory to another, or from somewhere within your home directory to somewhere within a project directory, generally the file, or the directory together with its contents, as the case may be, will keep its original ownership, group and permissions.</p>
<p dir="auto">So, supposing Joe Bloggs moves a file from his home directory to the project directory <code>/nesi/project/nesi99999</code>, his fellow team members won't be able to write to it:</p>
<pre dir="ltr"><code>$ ls -l README
-rw-r--r-- 1 bloggsj bloggsj 235 Mar 14  2014 README
$ mv README /nesi/project/nesi99999/bloggsj/README
$ ls -l /nesi/project/nesi99999/bloggsj/README
-rw-r--r-- 1 bloggsj bloggsj 235 Mar 14  2014 /nesi/project/nesi99999/bloggsj/README
</code></pre>
<p dir="auto">As you can see, the file stays in the group <code>bloggsj</code>, that is Joe Bloggs' personal group, even though it is now inside the project directory.</p>
<p dir="auto">There is, however, a solution involving the <code>rsync</code> command, a more advanced version of <code>scp</code>. <code>rsync</code> is typically used to copy files between two or more machines, but can also be used within the same machine.</p>
<blockquote class="blockquote-warning">
<h3 id="perms-group-warning">Warning</h3>
<p>In both these commands, the <code>--no-perms</code> and <code>--no-group</code> options must both come after <code>-a</code>. <code>-a</code> implicitly asserts <code>--perms</code> and <code>--group</code>, and will therefore override whichever of <code>--no-perms</code> and <code>--no-group</code> come before it.</p>
</blockquote>
<h2 dir="auto">To copy a file (or directory and its contents), updating its group and setting its permissions</h2>
<pre dir="ltr"><code>rsync -a --no-perms --no-group --chmod=ugo=rwX,Dg+s /path/to/source /path/to/destination
</code></pre>
<h2 dir="auto">To move a file (or directory and its contents), updating its group and setting its permissions</h2>
<blockquote class="blockquote-warning">
<h3 id="remove-source-warning">Warning</h3>
<p>The <code>--remove-source-files</code> option is safe only if every source file is otherwise left intact during the moving process.</p>
</blockquote>
<pre dir="ltr"><code>rsync --remove-source-files -a --no-perms --no-group --chmod=ugo=rwX,Dg+s /path/to/source /path/to/destination
</code></pre>
<p dir="auto">If you want to set files to executable in all cases, replace <code>...ugo=rwX...</code> with <code>...ugo=rwx...</code>. The capital <code>X</code> means, "Preserve whatever executable permissions existed on the source file and aren't masked at the destination." A lower case <code>x</code> on the other hand means, "Make this entity executable, even if it wasn't so previously, though this may be masked at the destination."</p>
<h2 dir="auto">To fix the permissions of a file or directory that is already in its intended place</h2>
<p dir="auto">Change to the parent directory, which could be a project or nobackup directory, that you want to fix, and find and fix your files. You can do this by means of the following commands.</p>
<pre dir="ltr"><code># Replace nesi12345 with your desired project code
group=nesi12345
startdir=$(pwd)
# Replace /nesi/project with /nesi/nobackup if needed
cd /nesi/project/${group}
# Move all files, directories, etc. owned by yourself into the project group
# The --no-dereference option updates the group of symbolic links (where permitted)
find . -user $(whoami) -print0 | xargs -0 -I {} chgrp --no-dereference ${group} {}<br># Make all files owned by yourself readable and writable by the group<br>find . -user $(whoami) -and -type f -print0 | xargs -0 -I {} chmod g+rw {}
# Make all directories owned by yourself readable, writable and executable by the group,
# and set the setgid bit
find . -user $(whoami) -and -type d -print0 | xargs -0 -I {} chmod g+rwxs {}
# Go back to the starting location
cd ${startdir}
</code></pre>