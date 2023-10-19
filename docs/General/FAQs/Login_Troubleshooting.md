---
created_at: '2018-11-16T01:13:47Z'
hidden: false
label_names: []
position: 13
title: Login Troubleshooting
vote_count: 4
vote_sum: 0
zendesk_article_id: 360000570215
zendesk_section_id: 360000039036
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<blockquote class="blockquote-prereq">
<h3 id="prerequisites">Requirements</h3>
<p>Please make sure you have followed the recommended setup. See <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001016335" target="_self">Choosing and Configuring Software for Connecting to the Clusters</a> for more information.</p>
</blockquote>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">New Command Line Users</h3>
<ul>
<li>Most terminals do not give an indication of how many characters have been typed when entering a password.</li>
<li>Paste is not usually bound to <code>ctrl</code> + <code>V</code> and will vary based on your method of access.</li>
</ul>
</blockquote>
<h1>Repeatedly asking for First and Second Factor.</h1>
<p>In addition to using an incorrect First/Second factor there are several other issues that will cause a similar looking failure to log in. </p>
<pre><span style="background-color: #bfe6ff;">Login Password:<br>Login Password:<br>Login Password:</span></pre>
<p>OR</p>
<pre><code>Login Password (First Factor): 
Authenticator Code (Second Factor):
Login Password (First Factor): 
Authenticator Code (Second Factor):
Login Password (First Factor): 
Authenticator Code (Second Factor):</code></pre>
<h3>1. Try logging in to <code>lander</code> directly.</h3>
<p>You can test what part of your connection has failed by first running:</p>
<pre class="highlight"><code class="hljs nginx">ssh &lt;user&gt;@lander.nesi.org.nz</code></pre>
<p><strong>If this succeeds</strong>: Run the following:</p>
<pre class="highlight"><code class="hljs nginx">ssh login.&lt;mahuika/maui&gt;.nesi.org.nz</code></pre>
<p><strong>If this fails:</strong> Are you logging in to the correct cluster? Mahuika/Maui have separate access control, also Maui requires your password input in a different format, see <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001244876-Mahuika-M%C4%81ui-Differences">here</a>.</p>
<p><strong>If this succeeds</strong>: If you are using a bash terminal, confirm your .ssh config is <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000161315#recLinux">set up correctly</a>.</p>
<p class="wysiwyg-indent13">If you are using a ssh client like <em>MobaXterm</em> or <em>WinSCP</em> make sure your session is <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000161315#recMoba">set up correctly</a>.</p>
<h3>2. Check you are a member of an active project</h3>
<p>If you are not a member of an active project, or your project has no active allocation, you will not be able to log in. You should be able to find whether you have any active projects with active allocations <a href="https://my.nesi.org.nz/html/view_projects">here</a>. </p>
<h3>3. Confirm you are using the correct username and password</h3>
<p>The most common cause of login failure is using incorrect login details. Make sure you are using your NeSI Username and the password you set when first logging into the Lander node. See <a href="https://my.nesi.org.nz/" target="_blank" rel="noopener">my.nesi.org.nz</a>.</p>
<h3>4. Check the time on your device</h3>
<p>If the device you are using as authentication token is not using NZST/NZDT, or is not keeping the correct time, the second factor code generated will be invalid. Even an error of a few seconds can be enough to invalidate the second factor code.</p>
<p>If your device can't keep time properly for whatever reason, please contact the person or team responsible for supporting it.</p>
<h3>5. Ensure you're not reusing the same <span>6-digit code </span>from your token.</h3>
<p>Login will fail if the same <span>6-digit code</span><dfn class="dictionary-of-numbers"> is </dfn>used to access the Māui or Mahuika login node after it has been used to access the lander node, or for consecutive login attempts to any node. If in doubt, wait <dfn class="dictionary-of-numbers dictionary-of-numbers-quantity-30s dictionary-of-numbers-processed">30 seconds</dfn> for a new token to be generated.</p>
<h3>6. Ensure the correct Second Factor token is being used</h3>
<p>Two-factor authentication is becoming a common security measure. Many people have multiple tokens and occasionally mix them up.</p>
<h3>7. Wait <dfn class="dictionary-of-numbers dictionary-of-numbers-quantity-14400s dictionary-of-numbers-processed">four hours</dfn>
</h3>
<p><dfn class="dictionary-of-numbers">Six failed login attempts </dfn>within <dfn class="dictionary-of-numbers dictionary-of-numbers-quantity-300s dictionary-of-numbers-processed">five minutes</dfn> will trigger a four-hour lockout. Users experiencing login issues can inadvertently trigger the lockout, making diagnosing the original issue much more difficult.  </p>
<h1 id="mobaPassPassPass">Connection closed by .... (MobaXterm)</h1>
<h3>1. Skip password prompts.</h3>
<p>There is a known MobaXterm bug in which a user who has set a second factor and is trying to log in to the lander node will be prompted multiple times for 'Password' before being prompted for 'First Factor'. (On the lander node, you should only be prompted for a 'password' if you have no Second Factor set up.)</p>
<p>These initial prompts can be skipped through by pressing 'Enter'. Any input before pressing Enter will cause the login to fail.</p>
<p>The expected processes is as follows:</p>
<pre class="highlight"><code class="hljs nginx">ssh &lt;user&gt;@lander.nesi.org.nz 
&lt;user&gt;@lander.nesi.org.nz's password: &lt;Enter&gt;
&lt;user&gt;@lander.nesi.org.nz's password: &lt;Enter&gt;
&lt;user&gt;@lander.nesi.org.nz's password: &lt;Enter&gt;
Login Password (First Factor): 
Authenticator Code (Second Factor):</code></pre>
<p><em>Note: Sometimes MobaXterm will prompt with a dialogue box.</em></p>
<h3>2. Update your MobaXTerm client.</h3>
<p>Occasionally an outdated client can cause errors.<br>MobaXterm can be updated through: 'help&gt;check for updates'</p>
<h3>3. Reinstall your MobaXTerm client.</h3>
<h1>Asked for 'Password' instead of 'First Factor'</h1>
<h3>1. Check the status using <a href="https://my.nesi.org.nz/" target="_blank" rel="noopener">my.nesi.org.nz</a> and confirm you have an authentication token registered.</h3>
<h3>2. See <a href="#mobaPassPassPass" target="_self">above</a>.</h3>
<h1>Authentication token manipulation error</h1>
<p>This occurs when your authentication token is out of sync. You will have to reset your token though <a href="https://my.nesi.org.nz/" target="_blank" rel="noopener">my.nesi.org.nz</a>.</p>
<h1 id="contactNesi">Nothing here has helped?</h1>
<p><a href="https://support.nesi.org.nz/hc/requests/new" target="_self">Contact NeSI support</a>.</p>
<p>Helpful things to include:</p>
<ul>
<li>The client you are using (WSL, MobaXterm, Mac terminal, Linux, etc.).</li>
<li>The nature of the problem, including the precise text of any error message you have been receiving.
<ul>
<li>Did you start out having <dfn class="dictionary-of-numbers">one login problem and </dfn>are now getting a different one? If so, when did the change happen, and were you doing anything in particular related to logging in at the time things changed?</li>
</ul>
</li>
<li>Have you successfully logged in in the past? if so when was the last time you successfully logged in, and to what NeSI cluster?</li>
<li>Has anything administrative and relevant to NeSI access changed since you last logged in? For example:
<ul>
<li>Have you opened or joined any new NeSI projects, or have any of your existing NeSI projects closed?</li>
<li>Have any of your NeSI projects been granted new allocations, had a previously granted new allocation actually start, or had an existing allocation modified?</li>
<li>Have any of your NeSI projects' existing allocations ended?</li>
<li>Have any of your NeSI projects had a disk space quota change?</li>
<li>Have you changed your institutional username and password, moved to a different institution, or started a new job at an institution while also keeping your position at your old institution? Might NeSI know about any of these changes?</li>
</ul>
</li>
<li>What have you tried so far?</li>
<li>Are you on the NIWA network, the NIWA VPN, or neither?</li>
</ul>
<div id="collapseExample" class="collapse">
<div class="card card-body"> </div>
</div>