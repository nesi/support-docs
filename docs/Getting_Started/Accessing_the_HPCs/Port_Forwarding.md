---
created_at: '2020-05-12T01:43:30Z'
hidden: false
label_names: []
position: 3
title: Port Forwarding
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001523916
zendesk_section_id: 360000034315
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
<li>Have your <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535-Standard-Terminal-Setup" target="_self">connection to the NeSI cluster</a> configured.</li>
</ul>
</blockquote>
<p>Some applications only accept connections from internal ports (i.e a port on the same local network), if you are running one such application on the cluster and want to connect to it you will need to set up <a href="https://en.wikipedia.org/wiki/Port_forwarding" target="_self">port forwarding</a>.</p>
<p>Three values must be known, the <em>local port</em>, the <em>host alias</em>, and the <em>remote port</em>. Chosen port numbers should be between <strong>1024</strong> and <strong>49151 </strong>and not be in use by another process.</p>
<p><strong>Localhost: </strong>The self address of a host (computer), equivalent to <code>127.0.0.1</code>. The alias <code>localhost</code> can also be used in most cases.</p>
<p><strong>Local Port:</strong> The port number you will use on your local machine. </p>
<p><strong>Host Alias:</strong> An alias for the socket of your main connection to the cluster, <code>mahuika</code> or <code>maui</code> if you have set up your ssh config file as described <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535" target="_self">here</a>.</p>
<p><strong>Remote Port:</strong> The port number you will use on the remote machine (in this case the NeSI cluster)</p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>The following examples use aliases as set up in <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535" target="_self">standard terminal setup</a>. This allows the forwarding from your local machine to the NeSI cluster, without having to re-tunnel through the lander node.</p>
</blockquote>
<h1>Command line (OpenSSH)</h1>
<p><em>Works for any Linux terminal, Mac terminal, or Windows with WSL enabled.</em></p>
<p>The command for forwarding a port is</p>
<pre><code>ssh -L &lt;local_port&gt;:&lt;destination_host&gt;:&lt;remote_port&gt; &lt;ssh_host&gt;</code></pre>
<h2>Example:</h2>
<p>A client program on my local machine uses the port 5555 to communicate. I want to connect to a server running on mahuika that is listening on port 6666. In a new terminal on my local machine I enter the command:</p>
<pre><code>ssh -L 5555:localhost:6666 mahuika</code> </pre>
<p>Your terminal will now function like a normal connection to mahuika. However if you close this terminal session the port forwarding will end.</p>
<p>If there is no existing session on mahuika, you will be prompted for your first and second factor, same as during the regular log in procedure. </p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>Your local port and remote port do not have to be different numbers. It is generally easier to use the same number for both.</p>
</blockquote>
<h1>SSH Config (OpenSSH)</h1>
<p>If you are using port forwarding on a regular basis, and don't want the hassle of opening a new tunnel every time, you can include a port forwarding line in your ssh config file ~/.ssh/config on your local machine.</p>
<p>Under the alias for the cluster you want to connect to add the following lines.</p>
<pre><code>LocalForward &lt;local_port&gt; &lt;host_alias&gt;:&lt;remote_port&gt;<br>ExitOnForwardFailure yes
</code></pre>
<p>ExitOnForwardFailure is optional, but it is useful to kill the session if the port fails. </p>
<p>e.g.</p>
<pre><code>  Host mahuika
      User cwal219
      Hostname login.mahuika.nesi.org.nz
      ProxyCommand ssh -W %h:%p lander
      ForwardX11 yes
      ForwardX11Trusted yes
      ServerAliveInterval 300
      ServerAliveCountMax 2
      LocalForward 6676 mahuika:6676<br>      ExitOnForwardFailure yes
</code></pre>
<p>In the above example, the local and remote ports are the same. This isn't a requirement, but it makes things easier to remember.</p>
<p>Now so long as you have a connection to the cluster, your chosen port will be forwarded.</p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Note</h3>
<ul>
<li>If you get a error message
<pre><code>bind: No such file or directory
unix_listener: cannot bind to path: </code></pre>
try to create the following directory:
<pre><code>mkdir -P ~/.ssh/sockets</code></pre>
</li>
</ul>
</blockquote>
<h1>MobaXterm</h1>
<p>If you have Windows Subsystem for Linux installed, you can use the method described above. This is the recommended method.</p>
<p>You can tell if MobaXterm is using WSL as it will appear in the banner when starting a new terminal session. </p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360004708596" alt="mceclip0.png"></p>
<p>You can also set up port forwarding using the MobaXterm tunnelling interface.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360004708616" alt="mceclip1.png"></p>
<p>You will need to create <strong>two</strong> tunnels. One from lander to mahuika. And another from mahuika to itself. (This is what using an alias in the first two examples allows us to avoid).</p>
<p>The two tunnels should look like this.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360004580035" alt="mobakey.png"></p>
<p><span class="wysiwyg-color-green110">■</span> local port<br><span class="wysiwyg-color-orange90">■</span> remote port<br><span class="wysiwyg-color-red90">■</span> must match<br><span class="wysiwyg-color-pink80">■</span> doesn't matter</p>
<p> </p>
<h1>sshuttle </h1>
<p><a href="https://sshuttle.readthedocs.io/en/stable/" target="_self">sshuttle</a> is a transparent proxy implementing VPN like traffic forwarding. It is based on Linux or MacOS platforms (unfortunately Windows is not supported). <code>sshuttle</code> allows users to create a VPN connection from a local machine to any remote server that they can connect to via <code>ssh</code>.There is no need to create a separate tunnel for every port to be forwarded, the package routes all traffic, going to the specified subnet, through the tunnel.</p>
<p>The command line for <code>sshuttle</code> has the following form:</p>
<pre><code>sshuttle [-l [ip:]port] -r &lt;host_alias&gt;[:port] &lt;subnets...&gt;</code></pre>
<p>More information about specific keys and modifiers for sshuttle commands is available in the online documentation.</p>
<p>As an example, this is how to establish a tunnel through Mahuika login node over to a specific virtual machine with IP address <code>192.168.90.5</code>:</p>
<pre><span>sshuttle -r mahuika 192.168.0.0/16</span></pre>
<p>which uses remote SSH host Mahuika to forward all traffic coming to <code>192.16.XXX.XXX</code> subnet through the port forwarder.</p>
<h1>Forwarding to Compute Nodes</h1>
<p>Ports can also be forwarded from the login node to a compute node.</p>
<p>The best way to do this is by creating a reverse tunnel<strong> from your slurm job</strong> (that way the tunnel doesn't depend on a separate shell, and the tunnel will not outlive the job). </p>
<p>The syntax for opening a reverse tunnel is similar the regular tunnel command, <code>-N</code> to not execute a command after connecting, <code>-f</code> to run the connection in the background and <code>-R</code> for a reverse tunnel ( as opposed to <code>-L</code> ).</p>
<pre><code>ssh -Nf -R &lt;remote_port&gt;:localhost:&lt;local_port&gt; ${SLURM_SUBMIT_HOST}</code></pre>
<p>An example Slurm script:</p>
<pre><code>#!/bin/bash<br><br>#SBATCH --time 00:15:00<br>#SBATCH --mem  1G<br><br>ssh -Nf -R 6676:localhost:6676 ${SLURM_SUBMIT_HOST}<br><br>&lt;some process using port 6676&gt;</code></pre>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What Next?</h3>
<ul>
<li>Using <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001093315" target="_self">JupyterLab </a>on the cluster.</li>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360000719156" target="_self">NiceDCV </a></li>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360001002956-ParaView" target="_self">Paraview</a></li>
</ul>
</blockquote>