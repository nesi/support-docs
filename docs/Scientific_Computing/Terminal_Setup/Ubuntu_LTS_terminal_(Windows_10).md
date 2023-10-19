---
created_at: '2019-07-15T04:12:01Z'
hidden: false
label_names: []
position: 1
title: Ubuntu LTS terminal (Windows 10)
vote_count: 3
vote_sum: 3
zendesk_article_id: 360001050575
zendesk_section_id: 360000189696
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
<li>Be a <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000693896-Applying-to-join-a-NeSI-project" target="_self">member of an active project.</a>
</li>
<li>Windows 10 with <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001075575" target="_self">WSL enabled.</a>
</li>
</ul>
</blockquote>
<p>Currently the native Windows command prompt (even with WSL enabled) does not support certain features, until this is fixed we recommend using the Ubuntu LTS Terminal.</p>
<ol>
<li>Open the Microsoft store, search for 'Ubuntu', find and install 'Ubuntu 18.04 LTS' or  'Ubuntu 20.04 LTS' <br><br> <img src="https://support.nesi.org.nz/hc/article_attachments/360002495316/ubuntu5.png" alt="ubuntu5.png"><img src="https://support.nesi.org.nz/hc/article_attachments/360002495256/ubuntu6.png" alt="ubuntu6.png"><br> <br><br>
</li>
<li>Close the “Add your Microsoft account.. dialogue box as you do not need an account for the installation.You may have to click “Install” for a second time (If the above dialogue box reappears, close as before and download/install will begin.<br><br> <img src="https://support.nesi.org.nz/hc/article_attachments/360002495336/ubuntu3.png" alt="ubuntu3.png">    <img src="https://support.nesi.org.nz/hc/article_attachments/360002495356/ubuntu4.png" alt="ubuntu4.png"><br><br>
</li>
<li>Launch “Ubuntu 18.04 LTS” from start menu and wait for the first time installation to complete.</li>
<li>As you are running Ubuntu on Windows for the first time, it will require to be configured. Once the installation was complete, you will be prompted to “Enter new UNIX username” and press &lt;Enter&gt;. This username can be anything you want.<br><br> <img src="https://support.nesi.org.nz/hc/article_attachments/360002495216/ubuntu1.png" alt="ubuntu1.png"><br><br>
</li>
<li>Now, type in a new password for the username you picked and press &lt;Enter&gt;. (Again this password is anything you want). Then retype the password to confirm and press &lt;Enter&gt;<br><br> <img src="https://support.nesi.org.nz/hc/article_attachments/360002389595/ubuntu2.png" alt="ubuntu2.png">
</li>
<li>To create a symbolic link to your Windows filesystems in your home directory run the following command replacing c with the name of your Windows filesystems found in /mnt/. 
<pre>ln -s /mnt/c/Users/YourWindowsUsername/ WinFS</pre>
</li>
</ol>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What Next?</h3>
<ul>
<li>Set up your <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535" target="_self">SSH config file</a>.</li>
</ul>
</blockquote>