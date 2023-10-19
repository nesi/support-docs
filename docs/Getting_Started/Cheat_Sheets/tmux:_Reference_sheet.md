---
created_at: '2022-03-24T22:11:13Z'
hidden: false
label_names: []
position: 0
title: 'tmux: Reference sheet'
vote_count: 1
vote_sum: 1
zendesk_article_id: 4563511601679
zendesk_section_id: 360000278975
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p><em>tmux</em> is a terminal multiplexer.  A multiplexer enables the creation and control of multiple terminals from a single screen.  It also allows the detachment of a screen to run in the background with the ability to re-attach and start where you left off.</p>
<p>Here is an example of starting  a <em>tmux</em> session:</p>
<pre>$ tmux new -s data_transfer<br>$ cd /nesi/nobackup/nesi99999/myproject<br>$ rsync -av someserver:/projectdata.tgz projectdata.tgz<br>CTRL-b d</pre>
<p>The<strong> CTRL-b</strong> <strong>d</strong> keyboard shortcut "detaches" the screen which allows you to logoff .  When you are ready to reattach to the session you login and run the following:</p>
<pre>$ tmux attach -t data_transfer</pre>
<p>Once reattached your session will be where you left it.   You can name the session whatever is most appropriate, such as the task you are performing.  You can run as many sessions as you like and they will remain until you terminate the tmux session or the node is rebooted.  Also of note, your session will be available even if your laptop/desktop crashes or the network goes down.</p>
<p> </p>
<p>More information can be found on the web, here are some good references:</p>
<p>Shortcut keys and cheat sheet: <a href="https://tmuxcheatsheet.com" target="_self" rel="undefined">https://tmuxcheatsheet.com</a></p>
<p>Getting started Guide: <a href="https://linuxize.com/post/getting-started-with-tmux/" target="_self" rel="undefined">https://linuxize.com/post/getting-started-with-tmux/</a></p>
<p> </p>