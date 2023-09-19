---
created_at: '2023-01-12T02:42:17Z'
hidden: false
label_names: []
position: 9
title: Data transfer between NeSI and a PC without NeSI two-factor authentication
vote_count: 0
vote_sum: 0
zendesk_article_id: 6198499650703
zendesk_section_id: 360000040596
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p>This article shows how to transfer potentially large amounts of data between NeSI and your personal computer, without requiring 2FA (two-factor authentication) each time you initiate the transfer.  This is particularly useful in the context of automated, or <a href="https://support.nesi.org.nz/hc/en-gb/articles/6202743496591" target="_blank" rel="noopener">scripted data transfers</a>.</p>
<p>The approach is based on using <a href="https://support.nesi.org.nz/hc/en-gb/articles/4405623380751-Data-Transfer-using-Globus-V5" target="_blank" rel="noopener">Globus</a> and a guest collection on the source side. <strong>Globus</strong> allows you to copy and synchronise files between NeSI's platforms and other computers, including your personal computer.</p>
<p>A <strong><em>collection</em></strong> is a directory whose content can be shared. A <strong><em>guest collection</em></strong> allows you to share data without having to type in your credentials each time your transfer files.</p>
<p>See this <a href="https://support.nesi.org.nz/hc/en-gb/articles/4405623380751" target="_blank" rel="noopener">support page</a> on how to set up Globus. Here, we assume you have an account on NeSI and have registered and created an account on Globus.</p>
<h2>Step 1: Create a guest collection on NeSI</h2>
<ul>
<li>Go to <a href="https://app.globus.org/file-manager" target="_self">https://app.globus.org/file-manager</a>
</li>
<li>In the "Collection" search box type <strong>NeSI Wellington DTN V5 </strong>and select this collection</li>
<li><em>You may then need to log onto NeSI DTN to see the files</em></li>
<li>Find the root folder of your guest collection, the directory you would like to share, and
<ul>
<li>click on the “Share” button,</li>
<li>click on “Add Guest Collection”</li>
<li>provide a "Display Name"</li>
<li>press on "Create Collection"</li>
</ul>
</li>
<li>You should now see your new guest collection at <a href="https://app.globus.org/collections?scope=administered-by-me" target="_self">https://app.globus.org/collections?scope=administered-by-me</a>
</li>
</ul>
<p><img style="max-width: 800px;" src="https://support.nesi.org.nz/hc/article_attachments/6202960141583" alt="mceclip0.png"></p>
<h2>Step 2: Download and install Globus Connect Personal</h2>
<p>On your personal computer, download "Globus Connect Personal" from <a href="https://app.globus.org/file-manager/gcp">https://app.globus.org/file-manager/gcp</a>. Versions exist for Mac, Windows and Linux. Follow the instructions to install and set up the software. Also see our support page about <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000217915" target="_blank" rel="noopener">Personal Globus Endpoint Configuration</a>.</p>
<h2>Step 3: Share a directory on your personal computer</h2>
<ul>
<li>Launch "Globus Connect Personal" and go to "Preferences". </li>
<li>Select "Access"
<ul>
<li>click on the "+" sign to share a new directory</li>
<li>navigate your directory and press "Open"</li>
<li>make the directory writable</li>
</ul>
</li>
</ul>
<p>Note: By default your entire home directory will be exposed. It is good practice to only share specific directories. You can remove your home directory by highlighting it and clicking on the "-" sign.</p>
<p><img style="max-width: 800px;" src="https://support.nesi.org.nz/hc/article_attachments/6202963231503" alt="mceclip1.png"></p>
<h2>Step 4: Test a file transfer</h2>
<ul>
<li>Go to <a href="https://app.globus.org/collections">https://app.globus.org</a>
</li>
<li>Log in</li>
<li>In the "FILE MANAGER" tab, type the source and destination collections. The source path should be relative to the guest collection root. However, the destination path is absolute, as can be seen in the picture below.</li>
<li>Click on the files you want to transfer and press "Start"</li>
</ul>
<p><img style="max-width: 800px;" src="https://support.nesi.org.nz/hc/article_attachments/6203141379215" alt="mceclip3.png"></p>