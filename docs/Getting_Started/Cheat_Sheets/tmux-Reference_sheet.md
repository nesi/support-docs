---
created_at: '2022-03-24T22:11:13Z'
tags: 
    - tmux
    - screen
    - zellij
    - multiplexer
title: 'tmux: Reference sheet'
vote_count: 1
vote_sum: 1
zendesk_article_id: 4563511601679
zendesk_section_id: 360000278975
---

## tmux

*tmux* is a terminal multiplexer.  A multiplexer enables the creation
and control of multiple terminals from a single screen.  `tmux` also allows
you to detach your screen to run in the background with the ability to
re-attach and start where you left off.  This is useful for long running processes 
such as data transfers, or if you want to keep a perpetual session. 

A `tmux` session will continue to run until you exit (with `exit` or `ctrl-d`) or the 
host is rebooted.

Here is an example of starting  a *tmux* session to run a `rsync` data transfer:

``` sh
tmux new -s data_transfer
cd /nesi/nobackup/nesi99999/myproject
rsync -av someserver:/projectdata.tgz projectdata.tgz
```

then

<kbd>ctrl</kbd> + <kbd>b</kbd>, <kbd>d</kbd>

The <kbd>ctrl</kbd> + <kbd>b</kbd>, <kbd>d</kbd>keyboard shortcut "detaches" the screen which
allows you to logoff.  You can also simply close your terminal or laptop.  Running `ctrl-b-d` is 
not required to save the session.  


When you are ready to reattach to the session
you login and run the following:

``` sh
tmux attach -t data_transfer
```

Once reattached your session will be where you left it.   You can name
the session whatever is most appropriate, such as the task you are
performing.  You can run as many sessions as you like and they will
remain until you terminate the tmux session or the node is rebooted.
Also of note, your session will be available even if your laptop/desktop
crashes or the network goes down.

More information can be found on the web, here are some good references:

[Detailed `tmux` cheat sheet](https://tmuxcheatsheet.com)  and a 
[Getting started Guide](https://linuxize.com/post/getting-started-with-tmux/)

## screen and zellij

`screen` and `zellij` (pronounced like zellidge) are alternatives to `tmux`  

`screen` is one of the original terminal multiplexers and works well but many users have switched to the more fully functional 
`tmux` or `zellij`.

`zellij` is available as a module `module load zellij` and is advertised as a multiplexer with _batteries included_.  It is recommended for 
new users as it comes with a useful reference footer.  `zellij` shares many of the same keybindings as `tmux`, for instance `ctrl-b-d` will detach
 a session.

More details on using `zellij`  can be found at the 
[zellij.dev](https://zellij.dev/documentation/) site.  

