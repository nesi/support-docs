---
created_at: '2022-03-24T22:11:13Z'
hidden: false
position: 0
tags: []
title: 'tmux: Reference sheet'
vote_count: 1
vote_sum: 1
zendesk_article_id: 4563511601679
zendesk_section_id: 360000278975
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

*tmux* is a terminal multiplexer.  A multiplexer enables the creation
and control of multiple terminals from a single screen.  It also allows
the detachment of a screen to run in the background with the ability to
re-attach and start where you left off.

Here is an example of starting  a *tmux* session:

``` sl
$ tmux new -s data_transfer
$ cd /nesi/nobackup/nesi99999/myproject
$ rsync -av someserver:/projectdata.tgz projectdata.tgz
CTRL-b d
```

The **CTRL-b** **d** keyboard shortcut "detaches" the screen which
allows you to logoff .  When you are ready to reattach to the session
you login and run the following:

``` sl
$ tmux attach -t data_transfer
```

Once reattached your session will be where you left it.   You can name
the session whatever is most appropriate, such as the task you are
performing.  You can run as many sessions as you like and they will
remain until you terminate the tmux session or the node is rebooted. 
Also of note, your session will be available even if your laptop/desktop
crashes or the network goes down.

 

More information can be found on the web, here are some good references:

Shortcut keys and cheat sheet: <https://tmuxcheatsheet.com>

Getting started Guide:
<https://linuxize.com/post/getting-started-with-tmux/>

 