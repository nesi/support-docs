---
created_at: '2019-07-30T04:11:05Z'
hidden: true
label_names: []
position: 1
title: Jumping Lander node.
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001076675
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
<li>Have your <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535-Standard-Terminal-Setup" target="_self">connection to the NeSI cluster</a> configured.</li>
</ul>
</blockquote>
<p>For the purposes of connecting to the cluster as specified in (connecting to cluster) this is <strong>included in the setup</strong>. This page is meant to show how an equivalent arrangement can be set up for applications that <strong>cannot make use of your existing tunnel</strong>.</p>
<p>For applications that require a connection to the cluster, but cannot make multiple hops, or have no way to enter a password it may be necessary to forward a local connection across to the cluster.</p>
<p><strong>Local Port:</strong> Any process connecting to <code>127.0. 0.1:&lt;local port&gt;</code> on your local will be forwarded to the remote (in this case, the NeSI cluster).</p>
<p><strong>Host Alias:</strong> An alias for the socket of your main connection to the cluster, <code>mahuika</code> or <code>maui</code> if you have set up your ssh config file as described <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535" target="_self">here</a>.</p>
<p><strong>Remote Port:</strong> Any process connecting to <code>127.0. 0.1:&lt;remote port&gt;</code> on your remote will be forwarded to your local.</p>
<blockquote class="blockquote-warning">
<ul>
<li>
<pre><code></code></pre>
</li>
</ul>
</blockquote>
<h1>MobaXterm</h1>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tips</h3>
<ul>
<li>MobaXterm has an internal terminal which acts like a linux terminal and can be configured as described in the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535" target="_self">Standard Terminal Setup</a>. </li>
</ul>
</blockquote>
<p>MobaXterm has a GUI to setup and launch sessions with port forwarding, click 'Tools &gt; MobaSSH Tunnel (port forwarding)':</p>
<ul>
<li>specify the lander.nesi.org.nz as SSH server address (right, lower box, first line)</li>
<li>specify your user name (right, lower box, second line)</li>
<li>specify the remote server address, e.g. login.mahuika.nesi.org.nz  (right, upper box first line)</li>
<li> and at the remote server (right upper box, second line)</li>
<li>Specify the local port number on the local side (left)</li>
<li>Save</li>
</ul>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/8295479596175" alt="sshTunnel.PNG"></p>
<h1>PuTTY</h1>
<p><em>Coming soon..</em></p>
<p> </p>
<p> </p>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What Next?</h3>
<ul>
<li>Using <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001093315" target="_self">JupyterLab </a>on the cluster.</li>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360000719156" target="_self">NiceDCV </a></li>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360001002956-ParaView" target="_self">Paraview</a></li>
</ul>
</blockquote>