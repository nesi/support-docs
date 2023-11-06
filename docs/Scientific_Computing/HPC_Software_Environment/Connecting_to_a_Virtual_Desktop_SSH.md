---
created_at: '2021-03-29T01:57:32Z'
hidden: true
label_names: []
position: 0
title: Connecting to a Virtual Desktop (SSH)
vote_count: 0
vote_sum: 0
zendesk_article_id: 360004050315
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>A virtual desktop provides a graphical interface to using the cluster. Desktops are hosted within Singularity containers, so not all of the NeSI software stack is supported. If you would like to build your own desktop containers with the code <a href="https://github.com/nesi/nesi-singularity-recipes" target="_self">here</a>.</p>
<p>Rendering is d<dfn class="dictionary-of-numbers">one cluster-side</dfn>, and compressed before being sent to your local machine. This means any rendering should be significantly more responsive than when using X<dfn class="dictionary-of-numbers">11 on it</dfn>s own (approximately <dfn class="dictionary-of-numbers">40 times faster)</dfn>.</p>
<h1>Connecting Through SSH</h1>
<blockquote class="blockquote-prereq">
<h3 id="prerequisites">Requirements</h3>
<p>You must be able to <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001523916" target="_self">forward a port</a>.</p>
</blockquote>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Note</h3>
<p>The Virtual desktops are still in development, please report any issues to NeSI support, or open an issue <a href="https://github.com/nesi/nesi-virtual-desktops/issues" target="_self">here</a>.</p>
</blockquote>
<h1>Setup</h1>
<h2>Port Forwarding</h2>
<p>A port on your local machine must be forwarded to Mahuika.</p>
<p><a href="https://support.nesi.org.nz/hc/en-gb/articles/360001523916" target="_self">Learn about setting up port forwarding</a>. </p>
<p>For example:</p>
<pre><code>ssh -L 1234:localhost:1234 mahuika</code></pre>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tip</h3>
<p>Port numbers should be between <strong>1025-49151</strong>. It's OK to use the same number for local and remote ports (makes it easier to remember too!)</p>
</blockquote>
<h2>Add VDT to path</h2>
<p>Run the command.</p>
<pre><code>echo "export PATH="/opt/nesi/vdt/:\$PATH""&gt;&gt;~/.bash_profile;. ~/.bash_profile</code></pre>
<p>to add the VDT command to your path, if you don't do this step you can still use the <code>vdt</code> command as <code>/opt/nesi/vdt/vdt</code></p>
<h1 style="display: flex;">Commands</h1>
<p><code>vdt -h</code> for general help or <code>vdt [command] -h</code> for help relating to that command.</p>
<table style="height: 190px; width: 774px;">
<tbody>
<tr style="height: 22px;">
<td style="width: 232px; height: 63px;">vdt start [port]</td>
<td style="width: 248px; height: 63px;"><code>vdt start 4321</code></td>
<td style="width: 260px; height: 63px;">Starts a desktop session on the login node. It will last until the shell is closed.</td>
</tr>
<tr>
<td style="width: 232px;"> </td>
<td style="width: 248px;"><code>vdt start 4321 &amp;</code></td>
<td style="width: 260px;">Starts a desktop session on the login node. It will continue running after you disconnect.</td>
</tr>
<tr>
<td style="width: 232px;"> </td>
<td style="width: 248px;"><code>vdt start -r wbg005 4321 &amp;</code></td>
<td style="width: 260px;">Starts a desktop session on another  node. It will continue running after you disconnect.</td>
</tr>
<tr>
<td style="width: 232px;"> </td>
<td style="width: 248px;"><code>salloc [slurm flags] vdt start 4321 &amp;</code></td>
<td style="width: 260px;">Starts a desktop session in a Slurm job. It will continue running after you disconnect.</td>
</tr>
<tr style="height: 22px;">
<td style="width: 232px; height: 61px;">vdt list</td>
<td style="width: 248px; height: 21px;"><code>vdt list</code></td>
<td style="width: 260px; height: 21px;">Lists all your sessions.</td>
</tr>
<tr style="height: 22px;">
<td style="width: 232px; height: 66px;">vdt kill [name]</td>
<td style="width: 248px; height: 22px;"><code>vdt kill my_desktop</code></td>
<td style="width: 260px; height: 22px;">Kills desktop [name].</td>
</tr>
</tbody>
</table>
<h1> </h1>
<h1>Settings</h1>
<p>Recommend setting scaling to 'remote'</p>
<div style="display: flex;">
<img src="https://support.nesi.org.nz/hc/article_attachments/8279624032015" width="426" height="362"><img src="https://support.nesi.org.nz/hc/article_attachments/8279534876303">
</div>
<h1>Examples</h1>
<p>The conditions for running a desktop on the login node are similar to when using a shell. There are no time limits, but should not be used for large or long running jobs. Any serious amount of computation should be launched with SLURM, this can be d<dfn class="dictionary-of-numbers">one using the terminal </dfn>or GUI. <br><br></p>
<p>In the case where your work needs to be run interactively, and cannot be managed from a different node, you can launch the desktop on a compute node </p>
<h2>On the login node</h2>
<p>You may run desktops on the login node, provided you are not doing any serious computation there.</p>
<p>Once on Mahuika, enter in the path to the desktop followed by your forwarded port (<code>--help</code> for more options).</p>
<pre><code>vdt start -N my_desktop [port]</code></pre>
<!--
<p>
  And select <code>n) New desktop.</code>&nbsp;
</p>
-->
<p>Then in a web browser navigate to your forwarded address. e.g.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/8279624033039" alt="mceclip0.png"></p>
<h2 id="compute">On a compute node</h2>
<!--
<h2>On a compute node</h2>
<p>
  To start a desktop on a compute node you must already have an job running, this
  could be a regular job submitted with sbatch, or a dedicated allocation. Starting
  a desktop inside an allocation will automatically forward your connection to
  the appropriate node.
</p>
<p>Otherwise you can connect using the menu.</p>
<p>
  <code>a) Adopt a SLURM session.</code>
</p>
<p>
  Or by supplying a jobid or node name when giving the command.
</p>
<p>
  or <code>-j &lt;jobid&gt;</code>
</p>
<p>
  or <code>-n &lt;node&gt;</code>(must have an allocation on that node)
</p>
<p>&nbsp;for example</p>
<pre><code>/opt/nesi/vdt/run 1234&nbsp;-j 13864207</code></pre>
<blockquote class="blockquote-warning">
  <h3 id="prerequisites">Note</h3>
  <p>
    To <em>reconnect</em> to a desktop session running on a compute node you
    must be forwarded to that node. A desktop running on a compute node is not
    visible from the login node.
  </p>
</blockquote>
<h2>Reconnecting</h2>
<p>
  Desktops are persistent,&nbsp; you can reconnect to a desktop running on the
  cluster using&nbsp;<code>/opt/nesi/vdt/run</code>&nbsp;and then selecting
  <code>#) Connect.</code> under your chosen session.
</p>
<h2>Killing</h2>
<p>
  Closing your terminal or ctrl + C will not terminate the session, only the webserver
  connecting you. You can end a desktop by running
  <code>/opt/nesi/vdt/run</code>&nbsp;and then selecting <code>#) Kill.</code>
  under your chosen session.
</p>
<p>&nbsp;</p>
-->
<p>If you plan on doing computation in the desktop instance, you should be doing it on a compute node.</p>
<p>If you already have a Slurm job running, you can start a desktop on that node using the <code>-r [hostname]</code> e.g.</p>
<pre><code>vdt start -N my_desktop -r [hostname] [port]</code></pre>
<p>If you want to start a new Slurm session, you can do this using salloc , the hostname will be inferred from environment (unless explicitly set).</p>
<pre><code>salloc --job-name my_desktop --nodes 1 --cpus-per-task 8 --time 01:00:00 vdt start 1234</code></pre>
<h2>Persistence</h2>
<p>If you wish your desktop to stay around after you close your shell, add <code>&amp;</code> after the command. e.g.</p>
<pre><code>vdt start [port] &amp;</code></pre>
<h1>Troubleshooting</h1>
<ul>
<li>Add <code>-v</code> flag for extra information.</li>
<li>Try using <code>-c</code> to remove local files.</li>
<li>Close any extra <code>/usr/bin/ssh-agent</code> or <code>/usr/bin/gpg-agent</code> processes running in the background.</li>
</ul>
<!--
<table style="height:190px;width:722px;display:none">
  <tbody>
    <tr>
      <td style="width:47px">&nbsp;Desktop</td>
      <td style="width:272.122px">&nbsp;command</td>
      <td style="width:143.878px">Working</td>
      <td style="width:138px">OS</td>
      <td style="width:62px">Desktop</td>
    </tr>
    <tr>
      <td style="width:47px">eng_dev</td>
      <td style="width:272.122px">
        <code>/opt/nesi/vdt/run&nbsp;eng_dev &lt;port&gt;</code>
      </td>
      <td style="width:143.878px">
        <p>
          ABAQUS<br>
          ANSYS<br>
          MATLAB<br>
          COMSOL
        </p>
      </td>
      <td style="width:138px">Centos7</td>
      <td style="width:62px">xfce</td>
    </tr>
    <tr>
      <td style="width:47px">default</td>
      <td style="width:272.122px">
        <code>/opt/nesi/vdt/run&nbsp;default &lt;port&gt;</code>
      </td>
      <td style="width:143.878px">
        <p>&nbsp;</p>
      </td>
      <td style="width:138px">Centos7</td>
      <td style="width:62px">xfce</td>
    </tr>
  </tbody>
</table>
-->