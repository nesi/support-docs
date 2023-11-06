---
created_at: '2023-10-13T00:14:22Z'
hidden: false
label_names: []
position: 0
title: Globus Quick Start Guide
vote_count: 0
vote_sum: 0
zendesk_article_id: 8117557125391
zendesk_section_id: 360000040596
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>This is intended to be a quick-start guide, for more detailed information, please see our other Globus articles here: <a href="https://support.nesi.org.nz/hc/en-gb/sections/360000040596">Globus documentation</a></p>
<p>Globus is a third-party service for transferring large amounts of data between two Globus Data Transfer Nodes (DTNs). To use Globus to transfer data to or from NeSI, you need:</p>
<ol>
<li>A NeSI account</li>
<li>A Globus account</li>
<li>Access to Globus DTNs or endpoint<br>
<ul type="A">
<li value="a">Access to a DTN (e.g., at your home institution)</li>
<li value="b">Personal endpoint if no DTN is available</li>
</ul>
</li>
</ol>
<p> </p>
<h2 id="h_01HCXQY0D23KC9J88RT5XFRK39">Globus Account</h2>
<p class="wysiwyg-text-align-left">Please note that a Globus account is not the same as a NeSI account. You will need both Globus and NeSI accounts in order to transfer data to or from NeSI HPC facilities.</p>
<p class="wysiwyg-text-align-left">To get a Globus account, go to <a href="https://transfer.nesi.org.nz/">https://transfer.nesi.org.nz/</a> and sign up using one of the available options on the page. Please note that the "existing organizational login" is somewhat limited, if your organisation is not listed, please sign in (sign up) using any of the other methods.</p>
<p class="wysiwyg-indent2 wysiwyg-text-align-left"><img src="https://support.nesi.org.nz/hc/article_attachments/8149105856015" alt="Globus_login.png" width="398" height="436"></p>
<p class="wysiwyg-text-align-left">For more detailed instructions please see <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000817476"> Initial Globus Sign-Up, and your Globus Identities</a>.</p>
<p class="wysiwyg-text-align-left"> </p>
<h2 id="h_01HCXQYMCZP3S6K1Z0S8R0P6S2">Globus Endpoint Activation</h2>
<p>A NeSI account is required in addition to a Globus account to transfer data to or from NeSI facilities. <em><br></em></p>
<p>To transfer data, between two sites, you need to have access to a DTN or endpoint at each location. For example, one on NeSI (NeSI Wellington DTN V5), the other to University of Otago's central file storage. You will also need the appropriate read and write permissions from where you're copying to and from. Please note that the NeSI <code>project</code> directory is read only, and <code>nobackup</code> is read and write.</p>
<p>A list of some Institutional endpoints can be found here: <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000931775-National-Data-Transfer-Platform">National-Data-Transfer-Platform</a>. You can also set up your own <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000217915">personal endpoint</a> to transfer data to or from your personal computer, however, administrative access to your computer is required</p>
<p>To activate the NeSI endpoint click go to <a href="https://transfer.nesi.org.nz/">https://transfer.nesi.org.nz/</a>  and click "file manager" on the menu bar on the left.</p>
<ol>
<li>Next to "Collection", search for "NeSI Wellington DTN V5", select it, then click "Continue".</li>
<li>In the 'Username<strong>'</strong> field, enter your NeSI HPC username. In the 'Password<strong>'</strong> field, the password is <code class="c-mrkdwn__code" data-stringify-type="code"><span>Login Password (First Factor)</span></code> + <code class="c-mrkdwn__code" data-stringify-type="code"><span>Authenticator Code (Second Factor)</span></code> e.g. <code class="c-mrkdwn__code" data-stringify-type="code">password123456</code>. Please <strong>do not</strong> save your password on "<em>Browser settings</em>" as it will change every time due to the 2nd factor requirement.</li>
</ol>
<p class="wysiwyg-text-align-center"><img src="https://support.nesi.org.nz/hc/article_attachments/8149067986063" alt="NeSI_Globus_Authenticate.png" width="296" height="340"></p>
<p class="wysiwyg-text-align-left"> </p>
<p class="wysiwyg-text-align-left"> </p>
<h2 id="h_01HCXQZ3EYNQC08EMBEJ6BM1B6">Transferring Data</h2>
<p>To transfer data, activate your two endpoints and navigate to the appropriate folders, then select the files or folders of interest. To initiate the transfer, select one of the two directional arrows. In the image below, the 'config' folder is being transferred from the location on the right, to the location on the left.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/8149738412815" alt="Globus_transfer_data.png"></p>
<p>To see the progress of the transfer, please click 'Activity' on the left hand menu bar.</p>
<p> </p>
<p>If you have any questions or issues using Globus to transfer data to or from NeSI, email <a href="https://support@nesi.org.nz">support@nesi.org.nz</a>.</p>
<p> </p>
<p> </p>
<p> </p>