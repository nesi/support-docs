---
created_at: '2018-05-22T01:49:31Z'
hidden: false
label_names: []
position: 0
title: File Recovery
vote_count: 8
vote_sum: 6
zendesk_article_id: 360000207315
zendesk_section_id: 360000042215
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<h2>Snapshots</h2>
<p>Snapshots are read only copies of the file system taken every day at 12:15, and retained for seven days.<br><br>Files from you project directory can be found in <code class="nohighlight">/nesi/project/.snapshots/</code> followed by the weekday (capitalised) and project code, e.g;</p>
<pre class="nohighlight"><code>/nesi/project/.snapshots/Sunday/nesi99999/
</code></pre>
<p> And for home directory;</p>
<pre class="nohighlight"><code>/home/username/.snapshots/Sunday/</code></pre>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Warning</h3>
<p>Files in <code class="nohighlight">/nesi/nobackup/</code> are not snapshotted.</p>
</blockquote>
<p> </p>
<p>Recovering a file or a directory from the snapshot is as simple as copying it over, e.g.</p>
<pre class="nohighlight"><code>cp /nesi/project/.snapshots/Sunday/nesi99999/file.txt /nesi/project/nesi99999/file.txt
</code></pre>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tip</h3>
<p>For copying directories use the flag <kbd>-ir</kbd> or just <kbd>-r</kbd> if you don't want to be prompted before overwriting.</p>
</blockquote>