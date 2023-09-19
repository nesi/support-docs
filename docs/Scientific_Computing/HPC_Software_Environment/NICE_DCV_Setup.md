---
created_at: '2019-01-24T20:30:30Z'
hidden: false
label_names:
- support
- application
- visualisation
position: 12
title: NICE DCV Setup
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000719156
zendesk_section_id: 360000040056
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p>NICE DCV is a virtual desktop solution that enables users to run graphics-intensive OpenGL applications, such as 3D visualisation, remotely on the HPC. You get full access to your data on the high-performance file systems, as well as the advanced CPU and GPU capabilities of the Cray CS clusters Mahuika and Māui Ancil.</p>
<p>NICE DCV sessions can persist for as long as your SLURM resource allocation is valid - you could launch a session in the morning, start a complex visualisation job with ParaView or VisIt, disconnect while the machine is still rendering the graphics, and reconnect in the afternoon to check how your job is coming along.</p>
<p>Follow the instructions below to set up a new session and connect to it.</p>
<h1>Internet Connection</h1>
<p>NICE DCV uses image compression mechanisms to reduce the amount of data that needs to be transmitted from the HPC to your laptop or desktop computer. However, data volumes can still become significant for longer sessions. Please keep this in mind if your internet provider charges by data volume.</p>
<p>While NICE DCV works reasonably well over a WiFi connection, for best performance we suggest you use a wired (Ethernet) connection if possible.</p>
<h1>Creating a new NICE DCV server session</h1>
<ol>
<li>Log in to the appropriate host.
<h3>On Māui</h3>
<ol>
<li>Connect to the lander node following the instructions <a href="https://support.nesi.org.nz/hc/en-gb/sections/360000034315-Accessing-the-HPCs" target="_self">here</a>. For example:
<pre><code>ssh lander</code></pre>
</li>
<li>Connect from the lander node to one of the NICE DCV server nodes:
<pre><code>ssh w-ndcv01</code></pre>
</li>
</ol>
<h3>On Mahuika</h3>
<ol>
<li>Connect to the Mahuika login node:
<pre><code>ssh mahuika</code></pre>
</li>
<li>Connect to the NICE DCV server node (not yet available):
<pre><code>ssh vgpuwbg005</code></pre>
</li>
</ol>
</li>
<li>Create a new NICE DCV session, replacing <code>&lt;session name&gt;</code> with a session name of your choice:
<pre><code>dcv create-session &lt;session name&gt;</code></pre>
</li>
</ol>
<h1>Establishing an SSH tunnel</h1>
<p>For security reasons, the NICE DCV nodes are not on the public internet and so are not directly accessible from your workstation. Therefore, we must create an SSH tunnel through the NeSI lander node.</p>
<h2>Linux, Mac, or Windows Subsystem for Linux</h2>
<blockquote class="blockquote-warning">
<h3 id="hang">Warning</h3>
<p>If successful, commands to open SSH tunnels will look like they are doing nothing (hanging) but it is important to leave them running. Once you kill a relevant SSH tunnel connection (e.g. <code>Ctrl-c</code>) you will no longer be able to connect to your NICE DCV session.</p>
</blockquote>
<ol>
<li>
<p>On your machine run the following command in your Linux terminal emulator (assuming you added the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535-Recommended-Terminal-Setup" target="_self">recommended</a> sections to your <code>~/.ssh/config</code> file). This command opens an SSH tunnel through the NeSI lander node to the SSH port on w-ndcv01.</p>
<h3>To connect to Māui</h3>
<pre><code># The first port number (22222 in this example) can be anything you like &gt; 1024,
# so long as it's not in use by another service.
# We have picked 22222 because it's easy to remember, the SSH port being 22.
ssh -L 22222:w-ndcv01.maui.niwa.co.nz:22 -o ExitOnForwardFailure=yes -N lander</code></pre>
<p>If you don't already have another open connection to or through the NeSI lander node, you will at this point be prompted for your password and your second factor. Enter them in the usual manner.</p>
<h3>To connect to Mahuika</h3>
<ol>
<li>Open an SSH tunnel through the lander node to the Mahuika login node.
<pre><code># The tunnel port numbers (10022 in this example) can be anything you like &gt; 1024,
# so long as neither of them is in use by another service.
# We have picked 10022 because it's easy to remember, the SSH port being 22.
ssh -L 10022:login.mahuika.nesi.org.nz:22 -o ExitOnForwardFailure=yes -N lander</code></pre>
<p>If you don't already have another open connection to or through the NeSI lander node to the Mahuika login node, you will at this point be prompted for your password and your second factor. Enter them in the usual manner.</p>
</li>
<li>In a new terminal, open an SSH tunnel through this existing tunnel to Mahuika's NICE DCV node.
<pre><code># The tunnel port numbers (22222 in this example) can be anything you like &gt; 1024,
# so long as neither of them is in use by another service.
# We have picked 22222 because it's easy to remember, the SSH port being 22.
ssh -L 22222:vgpuwbg005:22 -o ExitOnForwardFailure=yes -N -p 10022 -l &lt;nesi_linux_username&gt; localhost</code></pre>
<p>If prompted for a first factor, enter it in the usual manner. The second factor is optional (you can just press Enter), but if you provide a second factor it must be correct.</p>
</li>
</ol>
</li>
<li>
<p>Open a second terminal session, and run the following command in it.</p>
<pre><code># The first port number (28443 in this example) can be anything you like &gt; 1024,
# so long as it's not in use by another service.
# We have picked 28443 because it's easy to remember, the NICE DCV port being 8443.
ssh -L 28443:localhost:8443 -o ExitOnForwardFailure=yes -N -p 22222 -l &lt;nesi_linux_username&gt; localhost</code></pre>
<p>You will probably be prompted for a first factor and an optional second factor.</p>
Like the above command, this command will apparently hang if successful. Do not interrupt it as it is necessary to hold the port open for the server.</li>
</ol>
<h2>MobaXTerm on Windows</h2>
<p>If using MobaXTerm on Windows, set up and then start port forwarding connections to look like this:</p>
<h3>To connect to Māui</h3>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360003569596/2020-02-11_NICE_DCV_tunnels_in_MobaXTerm.png" alt="2020-02-11_NICE_DCV_tunnels_in_MobaXTerm.png"><br>When setting up and using the connections, note the following:</p>
<h3>To connect to Mahuika</h3>
<p>A picture is still to come.</p>
<ul>
<li>The numbers of the forward ports (fourth column) are arbitrary so long as you set them to be greater than 1024, but the SSH server port for the second connection must be the same as the forward port for the first connection.</li>
<li>The destination port for the first tunnel must be <code>22</code> and that for the second tunnel must be <code>8443</code>.</li>
<li>The server port for the first tunnel must be <code>22</code>.</li>
<li>The tunnel through the lander node must be started before the tunnel through localhost can be started.</li>
<li>The destination server for the tunnel through the lander node must be the NeSI login node where your NICE DCV server is running.</li>
</ul>
<h1>Connecting to a session</h1>
<p>NICE DCV comes with a client for Windows and Linux systems, which can be downloaded from the <a href="http://www.nice-software.com/download/dcv" target="_blank" rel="noopener">NICE web pages</a>. If you use MacOS, or if you do not want to install the client, you can also connect to your NICE DCV session with a modern browser.</p>
<p>Before you proceed, make sure that you have a valid SLURM allocation on the HPC and that a session has been created.</p>
<h2>Connecting with a Client</h2>
<p>To connect with the NICE DCV client software:</p>
<ol>
<li>Launch the client on your laptop or desktop computer.</li>
<li>Enter the server and session name in the login screen using the format <code>localhost:28443#&lt;session_name&gt;</code>, or whatever port number you used for the second SSH tunnel as an alternative to 28443.</li>
<li>Click on "Connect".</li>
<li>Enter your NeSI Linux username and password.</li>
<li>Click on "Login".</li>
</ol>
<h2>Connecting with a Browser</h2>
<p>To connect with a browser:</p>
<ol>
<li>Launch the browser or open a new tab</li>
<li>Enter "https://localhost:28443/#&lt;session name&gt;" in the URL bar. If you used a port other than 28443 when creating the second SSH tunnel, make the necessary modifications to this URL.</li>
<li>You may need to accept the insecure certificate in your browser before you can proceed</li>
<li>Enter your HPC account credentials (first factor)</li>
<li>Click on "Login"</li>
</ol>
<h1>Using the Desktop Environment</h1>
<p>You should be presented with a Linux desktop environment after successful login with the client or browser. You can then use the application launcher to start an application. You can also launch the terminal application by right-clicking on the desktop and selecting "Konsole". This will give you access to the NeSI software stack that includes various <a href="https://support.nesi.org.nz/knowledge/articles/360000700295/en-gb?brand_id=30406&amp;return_to=%2Fhc%2Fen-gb%2Farticles%2F360000700295">visualisation software solutions</a>.</p>
<h1>Disconnecting and Stopping a Session</h1>
<p>Sessions can persist on the HPC for as long as the SLURM resource allocation is valid. You can disconnect and reconnect to the session as often as you like.</p>
<h2>Disconnecting from a session without stopping it</h2>
<ol>
<li>Click on the machine URL in the top-right corner of the NICE DCV window</li>
<li>Select "Disconnect"</li>
<li>Close the NICE DCV client or browser window</li>
</ol>
<h2>Disconnecting and stopping a session</h2>
<ol>
<li>Click on the application launcher icon in the top-left corner of the virtual desktop</li>
<li>Click on "Leave"</li>
<li>Click on "Log out"</li>
<li>Confirm the logout in the dialog box that appears</li>
<li>Close the NICE DCV client or browser window</li>
</ol>
<p>A running session will automatically stop if your SLURM resource allocation finishes.</p>