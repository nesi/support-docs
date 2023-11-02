---
created_at: '2018-11-26T03:03:23Z'
hidden: false
label_names: []
position: 3
title: WinSCP/PuTTY Setup (Windows)
vote_count: 4
vote_sum: 2
zendesk_article_id: 360000584256
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
<li>Have an <a href="https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects" target="_self">active account and project.</a>
</li>
<li>Set up your <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000335995" target="_blank" rel="noopener">NeSI account password.</a>
</li>
<li>Set up Second <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000203075" target="_self">Factor Authentication.</a>
</li>
<li>Be using the Windows operating system.</li>
</ul>
</blockquote>
<p> </p>
<p>WinSCP is an SCP client for windows implementing the SSH protocol from PuTTY.</p>
<div class="" data-container="">
<p>WinSCP can be downloaded <a href="https://winscp.net/eng/download.php" target="_self">here</a>.</p>
<p>Upon startup:</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360001342295" alt="WinSCP1.png"></p>
<p>1. Add a <em>New Site</em> and set:</p>
<ul>
<li>Enter in <em>Host Name: </em><kbd>login.mahuika.nesi.org.nz</kbd> or <kbd>login.maui.nesi.org.nz</kbd>
</li>
<li>Enter your NeSI account username into <em>User name:</em> (Password optional)</li>
</ul>
<blockquote class="blockquote-tip">
<h3 id="llama-tip">Tip</h3>
<p>For "file protocol" (the topmost drop-down menu), either SCP or SFTP is acceptable. If you are trying to move many small files or have a slow or flaky Internet connection, you may find that SFTP performs better than SCP. Feel free to try both and see which works best for you.</p>
</blockquote>
<p><br><img src="https://support.nesi.org.nz/hc/article_attachments/360001342315" alt="WinSCP2.png"></p>
<p>5. Open Advanced Settings.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360002834335" alt="WinSCP3.png"></p>
<p>6. Navigate to <em>Connection &gt; Tunnel </em>and set:</p>
<ul>
<li>Enable "Connect through SSH tunnel".</li>
<li>Under "Host name:" enter <kbd>lander.nesi.org.nz</kbd>
</li>
<li>Under "User name:" enter your username.</li>
<li>Optionally, enter your password in the "Password:" box.</li>
</ul>
<p>10. <em>OK &gt; Save</em></p>
<h2 id="h_01HBPX415JHKBC1VADVC9Y7VCH">Setup for PuTTY Terminal</h2>
<p>The default WinSCP terminal lacks much functionality. We highly recommend you use the PuTTY terminal instead.</p>
<p>1. Download PuTTY <a href="https://www.putty.org/" target="_self">here</a> and install.</p>
<p>2.In WinSCP open 'Tools &gt; Preferences'</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360001342495" alt="WinSCP2-5.png"></p>
<p>3. Under<em> Integration &gt; Applications</em> enable <em>Remember session password and pass it to PuTTY</em></p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360001344315" alt="WinSCP4.png"></p>
<p> </p>
<h2 id="x_ming">Setup for Xming (Optional)</h2>
<p>Xming is an X server for Windows allowing graphical interface with the HPC and can be downloaded <a href="https://sourceforge.net/projects/xming/">here</a>.</p>
<p>1. Install Xming following the prompts. (Make sure 'Normal PuTTY Link SSH Client' is selected).</p>
<p>2. Under<em> Integration &gt; Applications</em> and add -X after PuTTY/Terminal client path.</p>
<p><em><img src="https://support.nesi.org.nz/hc/article_attachments/360001596916" alt="WinSCP6.png"></em></p>
<p>3. Restart your session.</p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Important</h3>
<p>In order for X11 forwarding to work you must have an Xming server running before connecting to the HPC.</p>
</blockquote>
<h1 id="h_01HBPX415JDNZ5AVRJNMJK84EE">Usage</h1>
<p>Files can be dragged, dropped and modified in the WinSCP GUI just like in any windows file system.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360001494615" alt="WinSCP5.png"></p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360001597336" alt="putTerm.png"> Will open a <strong>PuTTY terminal</strong>. Assuming you followed the steps setting up PuTTY, this should automatically enter in your details.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360001597316" alt="winTerm.png"> Will open the default <strong>WinSCP terminal</strong>. While the functionality is identical to any other terminal the interface is slightly abstracted, with a separate window for input and command history drop-down.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360001494635" alt="winAdd.png"> Type here to <strong>change directory</strong>.<strong> </strong>The GUI doesn't follow your current terminal directory like MobaXterm so must be changed manually. (Recommend making this larger as the default is very hard to type in).</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360001599556" alt="winBook.png"> <strong>Bookmark</strong> current directory.</p>
<h2 id="h_01HBPX47JG1T9BE383KRTPGKHE">Troubleshooting</h2>
<h3>Repeated Authentication Prompts</h3>
<p>By default, WinSCP will create multiple tunnels for file transfers. Occasionally this can lead to an excessive number of prompts. Limiting number of tunnels will reduce the number of times you are prompted. </p>
<p>1. Open settings</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/8026405972111" alt="winscp_settings.png" width="513" height="93"></p>
<p>2. Under 'Transfer' -&gt; 'Background', set the 'Maximal number of transfers at the same time' to '1' and untick 'Use multiple connections for a single transfer'.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/8026392031247" alt="winscp_Settings2.png"> </p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Important</h3>
<p>As WinSCP uses multiple tunnels for file transfer you will be required to authenticate again on your first file operation of the session. The second prompt for your second-factor token can be skipped, just as with login authentication.</p>
</blockquote>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What Next?</h3>
<ul>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360000578455" target="_self">Moving files to/from a cluster.</a></li>
<li>Setting up an <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001075975" target="_self">X-Server</a> (optional).</li>
</ul>
</blockquote>
</div>