---
created_at: '2021-08-27T03:18:13Z'
hidden: false
label_names: []
position: 1
title: Data Transfer using Globus V5
vote_count: 5
vote_sum: 3
zendesk_article_id: 4405623380751
zendesk_section_id: 360000040596
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<h2>Globus</h2>
<p>Globus is a third-party service for transferring large amounts of data between Globus Data Transfer Nodes (DTNs). For example you can transfer data between the NeSI Wellington DTN V5 and your personal workstation endpoint, or an endpoint from your institution. With Globus, very high data transfer rates are achievable. This service allows data to be accessible to any person who has a Globus account. The newest implementation (v5) provides extra features and some key differences from the previous setup that you can find <a href="https://docs.globus.org/globus-connect-server/" target="_self">here</a>. </p>
<p>To use Globus on NeSI platforms, you need:</p>
<ol id="nesi_globus_access">
<li>A Globus account (see <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000817476" target="_blank" rel="noopener">Initial Globus Sign-Up and Globus ID</a>)</li>
<li>An active NeSI account (see <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000159715" target="_blank" rel="noopener">Creating a NeSI Account</a>)</li>
<li>Access privileges on the non-NeSI Globus endpoint/collection you plan on transferring data from or to. This other endpoint/collection could be a personal one on your workstation, or it could be managed by your institution or a third party.</li>
</ol>
<ul>
<li><em>Note that a NeSI user account does not create a Globus account, and similarly a Globus account does not create a NeSI user account. Nor can you, as the end user, link the two through any website.</em></li>
</ul>
<p>Both your accounts (NeSI and Globus) must exist before you try to use our DTN.</p>
<p>The NeSI Wellington DTN endpoint is protected by a second factor authentication (2FA).  Also note, your NeSI username and password are case-sensitive.</p>
<h2><span class="wysiwyg-color-black">The NeSI Data Transfer Node</span></h2>
<p>The NeSI Data Transfer Node (DTN) acts as an interface between our HPC facility storage and a worldwide network of Globus endpoints. This is achieved using Globus.org, a web-based service that solves many of the challenges encountered moving large volumes of data between systems. While NeSI supports use of other data transfer tools and protocols such as <code class="bash">scp</code>, Globus provides the most comprehensive, efficient, and easy to use service for NeSI users who need to move large data sets (more than a few gigabytes at a time).</p>
<h2>Types of Globus endpoints or Data Transfer Nodes</h2>
<p>Globus data transfers take place between <em>endpoints</em>. An endpoint is nothing more than an operating system (Windows, Linux, etc) that has the Globus endpoint software installed on it. Endpoints come in two kinds: personal and server. Within a endpoint users can access data via collections, with specific permissions and the ability to shared with others.</p>
<p>The NeSI DTN is an example of a <em>server endpoint</em>. These type of endpoints are usually configured to access large capacity and high-performance parallel filesystems. Endpoints can be unmanaged or managed by a subscription. NeSI DTN is a server type, managed endpoint (by NeSI subscription) which allows authorised users to provide data transfer and data sharing services on behalf of their Globus accounts.</p>
<p>Your institution may have its own managed server endpoint, and if so we encourage you to use that endpoint for your data transfers between your institution and NeSI. You may need to apply to the person or group administering the managed server endpoint, most likely your IT team, to get access to the endpoint. Your institution may even have several endpoints, in which case we recommend that you consider which one would be best suited for your data transfer requirements. If you need any help in regards to this, get in touch with us via <a href="mailto:support@nesi.org.nz">support@nesi.org.nz</a>, or consult your institution's IT team.</p>
<p>If your institution doesn't have a managed server endpoint, you can set up a personal endpoint using software provided by Globus (see below). Please be aware that even if you set up a personal endpoint, you may still need to consult your IT team in order to make it usable, especially if your institution has an aggressive firewall.</p>
<h2>Transferring data using a managed endpoint</h2>
<p>As an example, to move files between the NeSI HPC Storage (accessible from Māui and Mahuika) and the Otago University high-capacity central file storage (another managed server endpoint):</p>
<div class="callout callout--info">
<p>Log in to the <a class="external-link" href="https://transfer.nesi.org.nz/file-manager" target="_self" rel="nofollow">NeSI File Manager</a> where you are able to search for DTNs in the <em>Collection</em> field.<br><a href="https://support.nesi.org.nz/hc/en-gb/articles/360000931775" target="_self">Here</a> is a listing of available endpoints on the New Zealand Data Transfer Platform.</p>
</div>
<p>Find the NeSI endpoint by typing in "NeSI Wellington DTN V5". Select the endpoint "NeSI Wellington DTN V5" from the list, and you will be asked to authenticate your access to the endpoint. Click Continue to the next step.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/4405622947215" alt="mceclip0.png" width="700" height="431"></p>
<p> </p>
<p>You can choose either of <strong>&lt;username&gt;@wlg-dtn-oidc.nesi.org.nz</strong> or NeSI Wellington OIDC Server (wlg-dtn-oidc.nesi.org.nz), they are all linked to the same website. If this is your first time login, you may ask to <em>bind</em> your primary <span>identity to the OIDC login, you need to allow that.</span></p>
<p> </p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/4405622955791" alt="mceclip1.png" width="700" height="226"></p>
<p>The NeSI Wellington DTN V5 endpoint is protected by a second factor authentication (2FA-same as accessing NeSI clusters).  In the '<strong>Username'</strong> field, enter your Māui/Mahuika username. In the '<strong>Password'</strong> field, your <code class="c-mrkdwn__code" data-stringify-type="code">Password</code> will be equal to <code class="c-mrkdwn__code" data-stringify-type="code"><span>Login Password (First Factor)</span></code> + <code class="c-mrkdwn__code" data-stringify-type="code"><span>Authenticator Code (Second Factor)</span></code> e.g. <code class="c-mrkdwn__code" data-stringify-type="code">password123456</code>. (<em><strong>Do not</strong></em> use any additional characters or spaces between your password and the token number.)</p>
<p>                            <img src="https://support.nesi.org.nz/hc/article_attachments/4408962414351" alt="mceclip0.png" width="451" height="561"></p>
<p>After the login, you will navigate to the default root(display as "/") path, then you could change the path to</p>
<p>(1) your<em><strong> /home/&lt;username&gt;</strong></em> directory,</p>
<p>(2) project directory (read-only) <em><strong>/nesi</strong><strong>/project/&lt;project_code&gt;</strong></em> </p>
<p>(3) project sub-directories of <em><strong>/nesi</strong><strong>/nobackup/&lt;project_code&gt;</strong></em>  - see <a href="https://support.nesi.org.nz/hc/en-gb/articles/4405623499791-Globus-V5-Paths-Permissions-Storage-Allocation" target="_self">Globus Paths, Permissions,  Storage Allocation</a>.<br><br>Navigate to your selected directory. e.g. the <em>nobackup</em> filesystem <em>/nesi/nobackup/&lt;project_code&gt;</em> and select the two-endpoint panel for transfer.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/4405623113615" alt="mceclip3.png" width="851" height="298"></p>
<p>Select the target endpoint and authenticate.</p>
<p>When you have activated endpoints in both transfer windows, you can start transferring files between them.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/4405623130383" alt="mceclip4.png" width="850" height="249"></p>
<p>Select files you wish to transfer and select the corresponding "Start" button:<br><br><img src="https://support.nesi.org.nz/hc/article_attachments/4405623291791" alt="mceclip5.png" width="850" height="250"></p>
<p> </p>
<p>To find other NeSI endpoints, type in "nesi#":</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/4940171187343" alt="filemanage_nesi.png"></p>
<h2>In brief:</h2>
<ul>
<li>Sign in to the NeSI Globus Web App <a href="https://transfer.nesi.org.nz/">https://transfer.nesi.org.nz/</a>. You will be taken to the <em>File Manager</em> page <a href="https://transfer.nesi.org.nz/file-manager" target="_self">https://transfer.nesi.org.nz/file-manager</a>
</li>
<li>If this is your first time, you will need to create a Globus account.</li>
<li>Open the two-endpoint panel <img src="https://support.nesi.org.nz/hc/article_attachments/5622407243151" alt="two_endpoint.png" width="109" height="34">located on the top-right of the <em>File Manager</em> page.</li>
<li>Select the Endpoints you wish to move files between (start typing "nesi#" to see the list of NeSI DTNs to select from). <a href="https://support.nesi.org.nz/hc/en-gb/articles/4405630948495" target="_self" rel="undefined">Authenticate</a> at both endpoints.</li>
<li>At Globus.org the<strong> </strong>endpoint<strong> <span class="wysiwyg-underline">defaults</span> to "/home/&lt;username&gt;" path </strong>(represented by "/~/") on Mahuika or Māui. We do not recommend uploading data to your home directory, as home directories are very small. Instead, navigate to an appropriate project directory under /nobackup (see <a href="https://support.nesi.org.nz/hc/en-gb/articles/4405623499791-Globus-V5-Paths-Permissions-Storage-Allocation" target="_self" rel="undefined">Globus Paths, Permissions, Storage Allocation</a>).</li>
<li>Transfer the files by clicking the appropriate <img src="https://support.nesi.org.nz/hc/article_attachments/5622408199183" alt="start.png">button depending on the direction of the transfer.</li>
<li>Check your email for confirmation about the job completion report.</li>
</ul>
<h2>Transferring data using a personal endpoint</h2>
<p>To transfer files into/out of your laptop, desktop computer or any other system you control, configure it as a <a href="https://www.globus.org/globus-connect-personal">Globus Personal Endpoint</a> (see <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000217915-Personal-Globus-Endpoint-Configuration" target="_self">Personal Globus Endpoint Configuration</a> for transfers between personal endpoints).</p>
<h2>File sharing</h2>
<p>To share files with others outside your filesystem, see <a href="https://docs.globus.org/how-to/share-files/">https://docs.globus.org/how-to/share-files/</a></p>
<p> </p>
<h2>Using Globus to transfer data to or from the cloud</h2>
<p>Globus connectors enable a uniform interface for accessing, moving, and sharing across a variety of cloud providers. We do not currently have a connector subscription (note a subscription is required per cloud provider) so we can’t use globus to transfer to/from cloud storage. If you see this as key for you, please let us know (support@nesi.org.nz).</p>
<p><span style="font-weight: 400;">Our current advice for moving data to or from the cloud is to use tools such as Rclone  (</span><a href="https://rclone.org/"><span style="font-weight: 400;">https://rclone.org/</span></a><span style="font-weight: 400;">) or the cloud CLI's such as aswcli for S3 (https://aws.amazon.com/cli/) or gcloud CLI (</span><a href="https://cloud.google.com/sdk/gcloud"><span style="font-weight: 400;">https://cloud.google.com/sdk/gcloud</span></a><span style="font-weight: 400;">). If you have any trouble or would like further advice, please get in touch (</span><a href="mailto:support@nesi.org.nz"><span style="font-weight: 400;">support@nesi.org.nz</span></a><span style="font-weight: 400;">).</span></p>