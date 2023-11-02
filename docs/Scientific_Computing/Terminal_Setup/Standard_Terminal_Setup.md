---
created_at: '2018-11-30T00:34:14Z'
hidden: false
label_names:
- ssh
- howto
position: 0
title: Standard Terminal Setup
vote_count: 8
vote_sum: 6
zendesk_article_id: 360000625535
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
<li>Set up your <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000335995" target="_self">Linux Password.</a>
</li>
<li>Set up Second <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000203075" target="_self">Factor Authentication.</a>
</li>
<li>Using standard Linux/Mac terminal <em>or</em> <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001075575" target="_self">Windows Subsystem for Linux</a> with <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001050575" target="_self">Ubuntu terminal</a>.</li>
</ul>
</blockquote>
<h2 id="recLinux">First time setup</h2>
<p>The login process can be simplified significantly with a few easy configurations.</p>
<ol>
<li>In a new local terminal run; <code class="nohighlight">mkdir -p ~/.ssh/sockets</code> this will create a hidden file in your home directory to store socket configurations.</li>
<li>
<p>Open your ssh config file with  <code class="nohighlight">nano ~/.ssh/config</code> and add the following (replacing <strong><code class="nohighlight">username</code></strong> with your username):</p>
<pre><code class="nohighlight">Host mahuika
   User <strong>username</strong>
   Hostname login.mahuika.nesi.org.nz
   ProxyCommand ssh -W %h:%p lander
   ForwardX11 <span class="hljs-literal">yes</span>
   ForwardX11Trusted <span class="hljs-literal">yes</span>
   ServerAliveInterval <span class="hljs-number">300</span>
   ServerAliveCountMax <span class="hljs-number">2</span>

Host maui
   User <strong>username</strong>
   Hostname login.maui.nesi.org.nz
   ProxyCommand ssh -W %h:%p lander
   ForwardX11 <span class="hljs-literal">yes</span>
   ForwardX11Trusted <span class="hljs-literal">yes</span>
   ServerAliveInterval <span class="hljs-number">300</span>
   ServerAliveCountMax <span class="hljs-number">2</span>

Host lander
   User <strong>username</strong>
   HostName lander.nesi.org.nz
   ForwardX11 <span class="hljs-literal">yes</span>
   ForwardX11Trusted <span class="hljs-literal">yes</span>
   ServerAliveInterval <span class="hljs-number">300</span>
   ServerAliveCountMax <span class="hljs-number">2</span>

Host *
    ControlMaster auto
    ControlPath ~/.ssh/sockets/ssh_mux_%h_%p_%r
    ControlPersist 1</code></pre>
<p>Close and save with <kbd>ctrl x</kbd>, <kbd>y</kbd>, <kbd>Enter</kbd></p>
</li>
<li>Ensure the permissions are correct by running <code>chmod 600 ~/.ssh/config</code>.</li>
</ol>
<h2>Usage</h2>
<p>Assuming you have followed the setup above you will be able to connect to the clusters directly using;</p>
<pre><code>ssh mahuika</code></pre>
<p>or</p>
<pre><code>ssh maui</code></pre>
<p>Subsequent local terminals opened will be able to scp files without having to re-enter authentication e.g.</p>
<pre><code>scp &lt;path/filename&gt; mahuika:~/</code></pre>
<p>(For more info visit <a style="background-color: #ffffff;" href="https://support.nesi.org.nz/hc/en-gb/articles/360000578455-File-Transfer-with-SCP">data transfer</a>).</p>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What Next?</h3>
<ul>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360000578455" target="_self">Moving files to/from a cluster.</a></li>
<li>Setting up a <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001075975" target="_self">X-Server</a> (optional).</li>
</ul>
</blockquote>