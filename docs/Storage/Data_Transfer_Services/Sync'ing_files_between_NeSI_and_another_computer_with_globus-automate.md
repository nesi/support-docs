---
created_at: '2023-01-12T20:45:15Z'
hidden: false
label_names: []
position: 10
title: Sync'ing files between NeSI and another computer with globus-automate
vote_count: 0
vote_sum: 0
zendesk_article_id: 6202743496591
zendesk_section_id: 360000040596
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p>It is common to generate large amounts of simulation data on NeSI and then having to migrate the files to another computer for storage or post-processing.</p>
<p>Here we show how to transfer data from NeSI to another computer <strong><em>programmatically</em></strong>, that is without using a web graphical user interface and <em><strong>without typing your credentials each time you initiate the transfer</strong></em>.</p>
<p>You can also use this approach to synchronise your files, that is to copy only the files that don't yet exist at the destination point, or refresh the files that have changed since you last triggered a transfer.</p>
<p>We'll assume that you have a NeSI account, you have registered at <a href="https://globus.org" target="_blank" rel="noopener">https://globus.org</a>, and have created a guest collections on NeSI and and a private mapped collection on the destination computer (follow the instructions <a href="https://support.nesi.org.nz/hc/en-gb/articles/6198499650703" target="_blank" rel="noopener">our corresponding support page</a>). A guest collection is directory whose content is shared via Globus.</p>
<h2>Step 1: Write a JSON file describing the transfer</h2>
<p>On NeSI, create a file named <code>transfer_input.json</code> with the following content:</p>
<pre>{<br>  "source_endpoint_id": "ENDPOINT1",<br>  "destination_endpoint_id": "ENDPOINT2",<br>  "transfer_items": [<br>    {<br>      "source_path": "SOURCE_FOLDER",<br>      "destination_path": "DESTINATION_FOLDER",<br>      "recursive": true<br>    }<br>  ],<br>  "sync_level": SYNC_LEVEL, <br>  "notify_on_succeeded": true,<br>  "notify_on_failed": true,<br>  "notify_on_inactive": true,<br>  "verify_checksum": true<br>}</pre>
<p>where</p>
<ul>
<li>
<code>ENDPOINT1</code> is the source endpoint UUID, which you can get <a href="https://app.globus.org/collections" target="_self" rel="undefined">https://app.globus.org/collections</a> by clicking on the collection of your choice. Using a guest collection will allow you to transfer the data without two-factor authentication</li>
<li>
<code>ENDPOINT2</code> is the destination UUID, e.g. your personal endpoint UUID, which may be for your private mapped collection if you're transferring to your personal computer</li>
<li>
<code>SOURCE_FOLDER</code> is the <strong>relative</strong> path of the source folder in the source endpoint. This is a directory, it cannot be a file. Use "/" if you do not intend to transfer the data from sub-directories</li>
<li>
<code>DESTINATION_FOLDER</code> is the <strong>absolute</strong> path of the destination folder in the destination endpoint when the destination is a private mapped collection</li>
<li>
<code>SYNC_LEVEL</code> specifies the synchronisation level in the range 0-3. <code>SYNC_LEVEL=0</code> will transfer new files that do not exist on destination. Leaving this setting out will overwrite all the files on destination. Click <a href="https://docs.globus.org/api/transfer/task_submit/#transfer_specific_fields" target="_blank" rel="noopener">here</a> to see how other sync_level settings can be used to update data in the destination directory based on modification time and checksums.</li>
</ul>
<h2>Step 2: Initiate the transfer</h2>
<p>Load the <code>globus-automate-client</code> environment module</p>
<pre>module purge &amp;&amp; module load globus-automate-client/0.16.1.post1-gimkl-2022</pre>
<p>then start the transfer using</p>
<pre>globus-automate action run --action-url https://actions.globus.org/transfer/transfer \<br>    --body transfer_input.json</pre>
<p>The first printed line will display the <code>ACTION_ID</code>. You can monitor progress with</p>
<pre>globus-automate action status --action-url \<br>    https://actions.globus.org/transfer/transfer ACTION_ID</pre>
<p>or on the web at <a href="https://app.globus.org/activity" target="_blank" rel="noopener">https://app.globus.org/activity</a>.</p>