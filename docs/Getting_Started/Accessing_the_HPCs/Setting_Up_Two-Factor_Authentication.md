---
created_at: '2018-05-18T03:56:37Z'
hidden: false
label_names:
- 2fa
- access
- mfa
- token
position: 1
title: Setting Up Two-Factor Authentication
vote_count: 6
vote_sum: -6
zendesk_article_id: 360000203075
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
You must:
<ul>
<li>Have a <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000159715" target="_self">NeSI account</a>.</li>
<li>Be a member of an <a href="https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects" target="_self">active project</a>.</li>
<li>Have <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000335995-Setting-Up-and-Resetting-Your-Password" target="_blank" rel="noopener">set up your NeSI account password</a>.</li>
<li>Have a device with an authentication app.</li>
</ul>
</blockquote>
<h2> Authentication App</h2>
<p>In order to generate your second factor, which you will require in order to access to any NeSI cluster, you will need a device with an authentication app, such as Authy or Google Authenticator installed (generally the device is a smartphone, but there are also authentication apps which work through the browser like Authy).</p>
<p>If you some reason you can't do this, please contact NeSI support.</p>
<p> </p>
<h2>Linking a device to your account</h2>
<ol>
<li>
<p>Log in to <a href="https://my.nesi.org.nz" target="_blank" rel="noopener">My NeSI</a> via your browser.</p>
</li>
<li>
<p>Click <strong>My HPC Account</strong> on left hand panel  and then <strong>Setup Two-Factor Authentication device</strong></p>
<img src="https://support.nesi.org.nz/hc/article_attachments/4414700806543" alt="authentication_factor_setup.png" width="560" height="210">
</li>
<li>Click the "<strong>Setup Two-Factor Authentication device</strong>" link.<br><img style="max-width: 480px;" src="https://support.nesi.org.nz/hc/article_attachments/360001267755">
</li>
<li>After clicking on "Continue" you will retrieve the QR code.</li>
<li>Open your Authy or Google Authenticator app and click on the add button and select "<strong>Scan a barcode</strong>". Alternatively, if you are not able to scan the barcode from your device you can manually enter the provided authentication code into your authentication app.</li>
</ol>
<h2>The second-factor token</h2>
<p>The <span class="wysiwyg-underline">6 digit code</span> displayed on your app can now be used as the second factor in the authentication process.<br>This code rotates every 30 seconds, and it <strong>can only be used once</strong>. This means that you can only try logging in to the lander node once every 30 seconds.</p>
<blockquote class="blockquote-postreq">
<h3 id="prerequisites">What next?</h3>
<ul>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360001016335" target="_self">Getting access to the cluster</a></li>
</ul>
</blockquote>