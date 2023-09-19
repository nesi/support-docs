---
created_at: '2018-11-30T00:32:25Z'
hidden: false
label_names: []
position: 2
title: MobaXterm Setup (Windows)
vote_count: 5
vote_sum: 5
zendesk_article_id: 360000624696
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
<li>Have an <a href="https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects" target="_self">active account and project.</a>
</li>
<li>Set up your <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000335995" target="_self">Linux Password.</a>
</li>
<li>Set up Second <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000203075" target="_self">Factor Authentication.</a>
</li>
<li>Windows operating system.</li>
</ul>
</blockquote>
<p>Setting up MobaXterm as shown below will allow you to connect to the Cluster with less keyboard inputs as well as allow use of the file transfer GUI.</p>
<ol>
<li>Download MobaXTerm <a href="https://mobaxterm.mobatek.net/download-home-edition.html" target="_self">here</a>
<ul>
<li>Use the Portable Edition if you don't have administrator rights on your machine. This is the recommended way for NIWA researchers.</li>
<li>Otherwise, choose freely the Portable or Installer Edition.</li>
</ul>
</li>
<!--
  <li>
    <p>
      Enable the "Use two-factor authentication for SSH gateways" option. First,
      open the MobaXTerm settings dialog (in the button bar at the top of the
      MobaXTerm window):
    </p>
    <p>
      <img src="https://support.nesi.org.nz/hc/article_attachments/360002872536/moba4.png" alt="moba4.png">
    </p>
    <p>
      Then, go to the SSH tab and enable the option, "Use 2-factor authentication
      for SSH gateways" (You can also enable SSH keepalive here to stop inactive
      sessions closing).
    </p>
    <p>
      <img src="https://support.nesi.org.nz/hc/article_attachments/360003057975/moba3_update.png" alt="moba3_update.png">
    </p>
    <p>
      Click OK to exit the Settings dialog, and&nbsp;<strong>quit and restart MobaXTerm before continuing</strong>.
    </p>
    Note: Make sure that "Remote-monitoring (experimental)" is disabled as this
    setting appears to cause MobaXterm crashes.
  </li>-->
<li>To set up a session, Click 'Session' in the top left corner:</li>
<li>In "SSH",
<ul>
<li>Set the remote host to <code>login.mahuika.nesi.org.nz</code> for Mahuika users or <code>login.maui.nesi.org.nz</code> for Maui users.</li>
<li>Enable the "Specify username" option and put your Username in the corresponding box.</li>
</ul>
</li>
<li>In the "Advanced SSH settings"
<ul>
<li>Set SSH-browser type to '<strong>SCP (enhanced speed)</strong>'.</li>
<li>Optionally, tick the 'Follow SSH path' button.</li>
</ul>
</li>
</ol>
<ol start="6">
<li>In the “Network settings” tab:
<ul>
<li>Select "SSH gateway (jump host)" to open a popup window</li>
<li>In this window enter <code class="highlighter-rouge">lander.nesi.org.nz</code> in the “Gateway host” field, as well as your NeSI username in the Username field for the gateway SSH server then select OK to close the window.</li>
</ul>
</li>
</ol>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/4411672582031/mceclip4.png" alt="mceclip4.png"></p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/4411672594191/mceclip5.png" alt="mceclip5.png"></p>
<ol start="7">
<li>Click 'OK' on the open window, usually this will start a new session immediately. <em>See usage below.</em>
</li>
</ol>
<blockquote class="blockquote-warning">
<h3 id="moba-bug">WARNING</h3>
<p>There is a bug which causes some users to be repeatedly prompted <samp>&lt;username&gt;@lander.nesi.org.nz's password:</samp><br>This can be resolved by clicking "OK" each time you are prompted then logging in as normal once you are prompted for your <samp>First Factor:</samp> or <samp>Password:</samp>.<br>See <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000570215" target="_self">Login Troubleshooting</a> for more details</p>
</blockquote>
<h2>Usage</h2>
<p>You will see your saved session in the left hand panel under 'Sessions'. Double click to start.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/4411680807951/mceclip6.png" alt="mceclip6.png"></p>
<p>You will be prompted by dialogue box.</p>
<pre><code>Login Password (First Factor):<br></code></pre>
<p>Enter your password.</p>
<pre><code>Authenticator Code (Second Factor):</code></pre>
<p>Enter your second factor six digit number (no space).</p>
<p>Then Mahuika users may be prompted again:</p>
<pre><code>Login Password:</code></pre>
<p>Enter your password again</p>
<p>Maui users will instead be prompted with:</p>
<pre><code>Password:</code></pre>
<p>Maui users must enter their password combined with their second factor. For example, if your password is "Password" and your current second factor is "123456" then you must enter "Password123456".</p>
<blockquote class="blockquote-tip">
<h3 id="warn">Tip</h3>
<p>If you choose to save your password, the process will be the same minus the prompts for First Factor.</p>
</blockquote>
<h2>Credential Manager</h2>
<p>If you are using the built in credential manager you will have to make sure to delete old entries when changing your password.</p>
<h2>Login Issues</h2>
<p>If you are experiencing login issues after resetting your password, it is likely due to an issue with MobaXterm saved sessions and Password management system for saved session.</p>
<p>Two steps to try:</p>
<ul dir="auto">
<li>Remove any previously saved sessions either related to <code>lander</code> OR <code>mahuika</code> from sessions panel on the left</li>
<li>Access MobaXterm password management system as below and remove saved credentials
<ul dir="auto">
<li>Go to <strong>Settings</strong>-&gt;<strong>Configuration</strong> and go to the <strong>General</strong> tab and click on <strong>MobaXterm password management</strong>
</li>
<li>You will see the saved sessions for <code>lander</code> (and perhaps <code>mahuika</code> as well). I recommend removing all of it and restart MobaXterm before the next login attempt</li>
</ul>
</li>
</ul>
<p>Then setup a new session <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000624696-MobaXterm-Setup-Windows-" rel="noopener noreferrer">according to the support doc instructions</a> as before.</p>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What Next?</h3>
<ul>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360000578455" target="_self">Moving files to/from a cluster.</a></li>
</ul>
</blockquote>