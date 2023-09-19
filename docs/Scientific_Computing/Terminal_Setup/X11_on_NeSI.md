---
created_at: '2019-07-30T01:58:26Z'
hidden: false
label_names: []
position: 4
title: X11 on NeSI
vote_count: 2
vote_sum: 2
zendesk_article_id: 360001075975
zendesk_section_id: 360000189696
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <blockquote class="blockquote-prereq">
<h3 id="prerequisites">Requirements</h3>
<ul>
<li>Have working <a href="https://support.nesi.org.nz/hc/en-gb/sections/360000189696" target="_self">terminal </a>set up.</li>
</ul>
</blockquote>
<p>X<dfn class="dictionary-of-numbers">-11 is a protocol </dfn>for rendering graphical user interfaces (GUIs) that can be sent along an SSH tunnel. If you plan on using a GUI on a NeSI cluster you will need to have an X-Server and X-Forwarding set up.</p>
<h1>X-Servers</h1>
<p>You must have a X-server running on your local machine in order for a GUI to be rendered.</p>
<p>Download links for X-servers can be found below.</p>
<table style="height: 23px;" width="633">
<tbody>
<tr>
<td style="width: 313px;">MacOS</td>
<td style="width: 313px;"><a href="https://www.xquartz.org/" target="_blank" rel="noopener">Xquartz</a></td>
</tr>
<tr>
<td style="width: 313px;">Linux</td>
<td style="width: 313px;"><a href="https://www.x.org/wiki/Releases/Download/" target="_self">Xorg</a></td>
</tr>
<tr>
<td style="width: 313px;">Windows</td>
<td style="width: 313px;"><a style="background-color: #ffffff; font-size: 15px;" href="https://sourceforge.net/projects/xming/" target="_blank" rel="noopener">Xming</a></td>
</tr>
</tbody>
</table>
<p>Make sure you have launched the server and it is running in the background, look for this <img src="https://support.nesi.org.nz/hc/article_attachments/360002963236/mceclip0.png" alt="mceclip0.png"> symbol in your taskbar </p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>MobaXterm has a build in X server, no setup required. By default the server is started alongside MobaXterm. You can check it's status in the top left hand corner (<img src="https://support.nesi.org.nz/hc/article_attachments/360002939175/xon.png" alt="xon.png">=on, <img src="https://support.nesi.org.nz/hc/article_attachments/360002939155/off.png" alt="off.png">=off). </p>
</blockquote>
<h1>X-Forwarding</h1>
<p>Finally your ssh tunnel must be set up to 'forward' along X<dfn class="dictionary-of-numbers">-11 connections</dfn>. </p>
<h2>OpenSSH (terminal)</h2>
<p>Make sure the <code>-Y</code> or <code>-X</code> flag is included</p>
<pre><code>ssh <span class="wysiwyg-color-red">-Y</span> user@lander.nesi.org.nz</code></pre>
<pre><code>ssh <span class="wysiwyg-color-red">-Y </span>login.nesi.org.nz</code></pre>
<h2>MobaXterm</h2>
<p> Under 'session settings' for your connection make sure the X<dfn class="dictionary-of-numbers">-11 forwarding box is </dfn>checked.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360002871175/x11moba.png" alt="x11moba.png" width="451" height="303"></p>
<p>If the <img src="https://support.nesi.org.nz/hc/article_attachments/360005129276/mceclip0.png" alt="mceclip0.png"> button in the top right corner of your window is coloured, the X-server should be running.</p>
<h1>X-Forwarding with <em>tmux</em>
</h1>
<p>In order to connect X11 into a tmux session you make the following change to your config file.</p>
<pre><code>tmux show -g | sed 's/DISPLAY //' &gt; ~/.tmux.conf
</code></pre>
<h1>Interactive Slurm jobs</h1>
<p>In order to make use of X11 in an interactive Slurm job:</p>
<h2>srun</h2>
<p>Add the flag <code>--x11</code></p>
<pre><code>srun --ntasks 36 --mem-per-cpu 1500 --time 01:00:00 <span class="wysiwyg-color-red">--x11</span> --pty bash</code></pre>
<h2>salloc</h2>
<p>add the flag -Y when sshing to the node.</p>
<pre><code>ssh <span class="wysiwyg-color-red">-Y</span> wbn001</code></pre>
<h1>XVFB</h1>
<p>If your application requires X11 in order to run, but does not need to be interactive you can use X11 Virtual Frame Buffer. This may be required to in order to run visual applications on the compute nodes. Prepending any command with <code>xfvb-run</code> will provide a dummy X11 server for the application to render to.<br>e.g.</p>
<pre>xvfb-run xterm</pre>