---
created_at: '2019-05-03T04:15:24Z'
hidden: false
label_names: []
position: 6
title: Git Bash (Windows)
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000929935
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
<li>
<p>Have a <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000159715-Creating-a-NeSI-Account" target="_self">NeSI account.</a></p>
</li>
<li>
<p>Be a member of an<a href="https://support.nesi.org.nz/hc/en-gb/articles/360000693896-Applying-to-join-a-NeSI-project" target="_self"> active project.</a></p>
</li>
</ul>
</blockquote>
<h2 id="recLinux">First time setup</h2>
<p>Git Bash can be downloaded as part of Git <a href="https://git-scm.com/download/win" target="_self">here</a>.</p>
<p>The login process can be simplified with a few configurations.</p>
<ol>
<li>
<p>Open Git Bash and run <code class="nohighlight">nano ~/.ssh/config</code> to open your ssh config file and add the following (replacing <code class="nohighlight">&lt;username&gt;</code> with your username):</p>
<pre><code class="nohighlight">Host mahuika
   User &lt;username&gt;
   Hostname login.mahuika.nesi.org.nz
   ProxyCommand ssh -W %h:%p lander
   ForwardX11 <span class="hljs-literal">yes</span>
   ForwardX11Trusted <span class="hljs-literal">yes</span>
   ServerAliveInterval <span class="hljs-number">300</span>
   ServerAliveCountMax <span class="hljs-number">2</span>

Host maui
   User &lt;username&gt;
   Hostname login.maui.nesi.org.nz
   ProxyCommand ssh -W %h:%p lander
   ForwardX11 <span class="hljs-literal">yes</span>
   ForwardX11Trusted <span class="hljs-literal">yes</span>
   ServerAliveInterval <span class="hljs-number">300</span>
   ServerAliveCountMax <span class="hljs-number">2</span>

Host lander
   User &lt;username&gt;
   HostName lander.nesi.org.nz
   ForwardX11 <span class="hljs-literal">yes</span>
   ForwardX11Trusted <span class="hljs-literal">yes</span>
   ServerAliveInterval <span class="hljs-number">300</span>
   ServerAliveCountMax <span class="hljs-number">2</span>

Host *
   ControlMaster auto
   ControlPersist 1
</code></pre>
<p>Close and save with <kbd>ctrl x</kbd>, <kbd>y</kbd>, <kbd>Enter</kbd></p>
</li>
<li>Ensure the permissions are correct by running <code>chmod 600 ~/.ssh/config</code>.</li>
</ol>
<h2>Usage</h2>
<p>Assuming you have followed the setup above you will be able to connect to the clusters directly using;</p>
<pre><code>ssh mahuika</code></pre>
<p>or</p>
<pre><code>ssh maui</code></pre>
<p>As multiplexing is not configured<em> you will have to enter in your login credentials every time you open a new terminal or try to move a file.</em></p>
<pre><code>scp &lt;path/filename&gt; mahuika:~/</code></pre>
<p>(For more info visit <a style="background-color: #ffffff;" href="https://support.nesi.org.nz/hc/en-gb/articles/360000578455-File-Transfer-with-SCP">data transfer</a>).</p>