---
created_at: '2021-06-04T00:42:20Z'
hidden: false
label_names: []
position: 0
title: How can I give read-only team members access to my files?
vote_count: 0
vote_sum: 0
zendesk_article_id: 4401821809679
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
<p dir="auto">Not all projects have read-only groups created by default. If your project has a read-only group created after the project itself was created, you will need to add appropriate access control lists (ACLs) to each of your files and directories within the project or nobackup directory.</p>
<p dir="auto">To do this, you can use the script <code>nn_add_to_acls_recursively</code>. The following commands explain how to do this;  when running the commands, replace <code>nesi12345</code> and <code>nesi12345r</code> with your project code and read-only project code respectively.</p>
<blockquote class="blockquote-warning">
<h3 id="tmux-warning">Warning</h3>
<p>If this process is interrupted part-way through, for example due to your computer going to sleep and losing its connection to your NeSI terminal session, your files can end up in a bad way. For this reason please <strong>run all the following commands in a <code>screen</code> or <code>tmux</code> session.</strong></p>
</blockquote>
<ol>
<li>Prepare a file containing the ACL to add. Ensure you include the <code>mask</code> line. Note that the script will not remove any of the existing ACL, except for overwriting existing lines that are the same, up to the second colon, as one of the new lines you ask to add.
<pre dir="ltr"><code>echo "mask::rwxc" &gt; acl_to_add.txt
echo "group:nesi12345r:r-x-" &gt;&gt; acl_to_add.txt</code></pre>
</li>
<li>Check that the contents of the file are correct.
<pre dir="ltr"><code>cat acl_to_add.txt</code></pre>
</li>
<li>Carry out the ACL change. You can specify a subdirectory instead if, as may well be the case, you don't want to trawl through the entirety of <code>/nesi/project/nesi12345</code> or <code>/nesi/nobackup/nesi12345</code>.
<pre dir="ltr"><code>nn_add_to_acls_recursively -f acl_to_add.txt /nesi/project/nesi12345</code></pre>
</li>
<li>Check the resulting ACLs, for example:
<pre dir="ltr"><code>/usr/lpp/mmfs/bin/mmgetacl /nesi/project/nesi12345/some_dir
/usr/lpp/mmfs/bin/mmgetacl -d /nesi/project/nesi12345/some_dir</code></pre>
We suggest to check at least one subdirectory, at least one executable file (if there is one) and at least one non-executable file.</li>
<li>Repeat steps 3 and 4 for other directories within <code>/nesi/project/nesi12345</code> and <code>/nesi/nobackup/nesi12345</code>, with the necessary modifications.</li>
<li>Optionally, remove your ACL file.
<pre dir="ltr"><code>rm acl_to_add.txt</code></pre>
</li>
<li>Optionally, exit the <code>screen</code> or <code>tmux</code> session when you are finished.</li>
</ol>