---
created_at: '2018-11-20T22:41:32Z'
hidden: false
label_names:
- scp
- transfer
- copying
- download
- upload
- mv
- cp
- move
- moving
position: 2
title: Moving files to and from the cluster
vote_count: 11
vote_sum: 3
zendesk_article_id: 360000578455
zendesk_section_id: 360000189716
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<blockquote class="blockquote-prereq">
<h3 id="prerequisites">Requirements</h3>
<ul>
<li>Have an <a href="https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects" target="_self">active account and project.</a>
</li>
<li>Have a <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001016335" target="_self">SSH connection to a NeSI cluster</a>, and <a href="https://support.nesi.org.nz/hc/en-gb/sections/360000189696" target="_self">set up as recommended. </a>
</li>
</ul>
</blockquote>
<p>Find more information on the different types of directories <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000177256" target="_self">here</a>.</p>
<h1>Standard Terminal</h1>
<p>In a local terminal the following commands can be used to:</p>
<p>Move a file from your local machine to Mahuika.</p>
<pre><code><a title="Put actual path here (no &lt;&gt;)" data-toggle="tooltip">scp &lt;path/filename&gt; mahuika:&lt;path/filename&gt;</a></code></pre>
<p>Move a file from Mahuika to your local machine.</p>
<pre><code><a title="Put actual path here (no &lt;&gt;)" data-toggle="tooltip">scp mahuika:&lt;path/filename&gt; &lt;path/filename&gt;</a></code></pre>
<blockquote class="blockquote-warning">
<h3 id="">Note</h3>
<ul>
<li>This will only work if you have set up aliases as described in <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535-Terminal-Setup-MacOS-Linux-">Terminal Setup</a>.</li>
<li>As the terms 'maui' and 'mahuika' are defined locally, the above commands <em>only works when using a local terminal</em> (i.e. not on Mahuika).</li>
<li>If you are using Windows subsystem, the root paths are different as shown by Windows. e.g. <code>C:</code> is located at <code>/mnt/c/</code>
</li>
</ul>
</blockquote>
<p><code>scp</code> stands for Secure CoPy and operates in a similar way to regular cp with the source file as the left term and destination on the right.</p>
<p>These commands make use of <em>multiplexing, </em>this means that if you already have a connection to the cluster you will not be prompted for your password.</p>
<h2>File Managers </h2>
<p>Most file managers can be used to connect to a remote directory simply by typing in the address bar (provided your have an active connection to the cluster and your ssh config file is set up as described <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535" target="_self">here</a>).</p>
<p>For Nautilus (Ubuntu default) just prepend the path you want to connect to with <code>sftp://mahuika</code>. (<kbd>ctrl</kbd> + <kbd>L</kbd> opens address bar)</p>
<p>This does not work for File Explorer (Windows default)</p>
<p>This does not work for Finder (Mac default)</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360003129656/mceclip0.png" alt="mceclip0.png"></p>
<p>If your default file manager does not support mounting over sftp, see our documentation on <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000621135" target="_self">SSHFS</a>.</p>
<h1>MobaXterm</h1>
<p>Clicking the "<em>Scp</em>" tab (located on the left-hand side of the MobaXTerm window) opens up a graphical user interface that can be used for basic file operations. You can drag and drop files in the file explorer or use the up and down arrows on the toolbar to upload and download files.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360001503115/2019-01-07_SCP_in_MobaXTerm.png" alt="2019-01-07_SCP_in_MobaXTerm.png"></p>
<p>You may also transfer files as described under 'Standard Terminal' (provided <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001075575" target="_self">WSL</a> is enabled).</p>
<h1>WinSCP</h1>
<p>As WinSCP uses multiple tunnels for file transfer you will be required to authenticate again on your first file operation of the session. The second prompt for your 2FA can be skipped, just the same as with login authentication.</p>
<h1>Globus</h1>
<p>Globus is available for those with large amounts of data, security concerns, or connection consistency issues.<br>You can find more details on its use on our <a href="https://support.nesi.org.nz/hc/en-gb/articles/4405623380751-Data-Transfer-using-Globus-V5" target="_self">Globus support page</a>.</p>
<h1>Rclone</h1>
<p>Rclone is available for those that need to transfer data from cloud storage services like Google drive or OneDrive.</p>
<p>The basic command syntax of Rclone:</p>
<pre>rclone <em>subcommand options source:path dest:path</em></pre>
<p>The most frequently used Rclone subcommands:</p>
<ul>
<li>
<strong>rclone copy</strong> – Copy files from the source to the destination, skipping what has already been copied.</li>
<li>
<strong>rclone sync</strong> – Make the source and destination identical, modifying only the destination.</li>
<li>
<strong>rclone mov</strong>e – Move files from the source to the destination.</li>
<li>
<strong>rclone delete</strong> – Remove the contents of a path.</li>
<li>
<strong>rclone mkdir</strong> – Create the path if it does not already exist.</li>
<li>
<strong>rclone rmdir</strong> – Remove the path.</li>
<li>
<strong>rclone check</strong> – Check if the files in the source and destination match.</li>
<li>
<strong>rclone ls</strong> – List all objects in the path, including size and path.</li>
<li>
<strong>rclone lsd</strong> – List all directories/containers/buckets in the path.</li>
<li>
<strong>rclone lsl</strong> – List all objects in the path, including size, modification time and path.</li>
<li>
<strong>rclone lsf</strong> – List the objects using the virtual directory structure based on the object names.</li>
<li>
<strong>rclone cat</strong> – Concatenate files and send them to stdout.</li>
<li>
<strong>rclone copyto</strong> – Copy files from the source to the destination, skipping what has already been copied.</li>
<li>
<strong>rclone moveto</strong> – Move the file or directory from the source to the destination.</li>
<li>
<strong>rclone copyurl</strong> – Copy the URL's content to the destination without saving it in the tmp storage.</li>
</ul>
<p>A more extensive list can be found on the the<a href="https://rclone.org/docs" target="_self"> Rclone documentation</a>.</p>
<h1>Rsync</h1>
<p>Rsync <span>is an utility that provides fast incremental file transfer and efficient file synchronization between a computer and a storage disk.<br>The basic command syntax of:<br></span><span></span></p>
<pre><span>rsync -options source target</span></pre>
<p><span>If the data source or target location is a remote site, it is defined with syntax:<br></span></p>
<pre><span>userame@server:/path/in/server</span></pre>
<p>The most frequently used Rsync options:</p>
<ul>
<li>
<strong>-r</strong>                         Recurse into directories</li>
<li>
<strong>-a </strong>                       Use archive mode: copy files and directories recursively and preserve access permissions and time stamps.</li>
<li>
<strong>-v</strong>                        Verbose mode.</li>
<li>
<strong>-z</strong>                        Compress</li>
<li>
<strong>-e ssh</strong>                 Specify the remote shell to use.</li>
<li>
<strong>-n</strong>                       Show what files would be transferred.</li>
<li>
<strong>--partial</strong>             Keep partially transferred files.</li>
<li>
<strong>--progress</strong>         Show progress during transfer.</li>
</ul>
<p>A more extensive list can be found on the the <a style="background-color: #ffffff;" href="https://download.samba.org/pub/rsync/rsync.1" target="_self">Rsync documentation</a>.</p>
<p> </p>