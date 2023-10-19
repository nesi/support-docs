---
created_at: '2018-11-27T23:55:26Z'
hidden: false
label_names: []
position: 0
title: Can I use SSHFS to mount the cluster filesystem on my local machine?
vote_count: 5
vote_sum: 3
zendesk_article_id: 360000621135
zendesk_section_id: 360000039036
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p><a href="https://github.com/libfuse/sshfs">SSHFS</a> allows you to mount a remote filesystem on your local machine. SSHFS relies on SSH underneath, so you should follow the "Recommended logon procedure" instructions <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000161315-Logging-in-to-the-HPCs">here</a> to configure SSH first.</p>
<h2 id="toc_1">Linux</h2>
<p>Use the following commands to mount your home directory from Mahuika on your local machine (the same command will work for Māui, just replace the names):</p>
<div>
<pre class="line-numbers language-none"><code class=" language-none"># create a mount point and connect
mkdir -p ~/mahuika-home
sshfs -oauto_cache,follow_symlinks mahuika: ~/mahuika-home</code></pre>
</div>
<p>Now you should be able to navigate to "~/mahuika-home" on your local machine to access your home directory on Mahuika. To unmount the directory run:</p>
<div>
<pre class="line-numbers language-none"><code class=" language-none">fusermount -u ~/mahuika-home</code></pre>
</div>
<p>To mount a project directory, you could run:</p>
<div>
<pre class="line-numbers language-none"><code class=" language-none"># create a mount point and connect
mkdir -p ~/mahuika-project
sshfs -oauto_cache,follow_symlinks mahuika:/nesi/project/nesiXXXXX ~/mahuika-project</code></pre>
</div>
<h2 id="toc_2">MacOS</h2>
<p>We recommend using some extra options with MacOS. The following commands will mount your home directory, make it show up under devices in Finder and give the volume a sensible name:</p>
<div>
<pre class="line-numbers language-none"><code class=" language-none"># create a mount point and connect
mkdir -p ~/mahuika-home
sshfs mahuika: ~/mahuika-home \<br>    -oauto_cache,follow_symlinks \<br>    -ovolname=MahuikaHome,defer_permissions,noappledouble,local </code></pre>
</div>
<p>To unmount the directory on MacOS, either eject from Finder or run:</p>
<div>
<pre class="line-numbers language-none"><code class=" language-none">umount ~/mahuika-home</code></pre>
</div>
<blockquote class="blockquote-warning">
<h3 id="fuse-warning">Note</h3>
<p>Newer MacOS does not come with SSHFS pre installed. You will have to install FUSE as SSHFS from <a href="https://osxfuse.github.io/">here</a>.</p>
</blockquote>