---
created_at: '2019-07-30T01:58:26Z'
hidden: false
label_names: []
position: 4
title: X11 on NeSI
vote_count: 2
vote_sum: 2
zendesk_article_id: 360001075975
zendesk_section_id: 360000189696
---

> ### Requirements
>
> -   Have working
>     [terminal](https://support.nesi.org.nz/hc/en-gb/sections/360000189696)set
>     up.

X<dfn class="dictionary-of-numbers">-11 is a protocol </dfn>for
rendering graphical user interfaces (GUIs) that can be sent along an SSH
tunnel. If you plan on using a GUI on a NeSI cluster you will need to
have an X-Server and X-Forwarding set up.

# X-Servers

You must have a X-server running on your local machine in order for a
GUI to be rendered.

Download links for X-servers can be found below.

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
</tbody>
</table>

Make sure you have launched the server and it is running in the
background, look for
this ![mceclip0.png](../../includes/images/mceclip0_8.png) symbol in
your taskbar 

> ### Note
>
> MobaXterm has a build in X server, no setup required. By default the
> server is started alongside MobaXterm. You can check it's status in
> the top left hand corner
> (![xon.png](../../includes/images/xon.png)=on, ![off.png](../../includes/images/off.png)=off). 

# X-Forwarding

Finally your ssh tunnel must be set up to 'forward' along
X<dfn class="dictionary-of-numbers">-11 connections</dfn>. 

## OpenSSH (terminal)

Make sure the `-Y` or `-X` flag is included

    ssh -Y user@lander.nesi.org.nz

    ssh -Y login.nesi.org.nz

## MobaXterm

 Under 'session settings' for your connection make sure the
X<dfn class="dictionary-of-numbers">-11 forwarding box is </dfn>checked.

<img src="../../includes/images/x11moba.png" alt="x11moba.png" width="451" height="303" />

If the ![mceclip0.png](../../includes/images/mceclip0_9.png) button in
the top right corner of your window is coloured, the X-server should be
running.

# X-Forwarding with *tmux*

In order to connect X11 into a tmux session you make the following
change to your config file.

    tmux show -g | sed 's/DISPLAY //' > ~/.tmux.conf

# Interactive Slurm jobs

In order to make use of X11 in an interactive Slurm job:

## srun

Add the flag `--x11`

    srun --ntasks 36 --mem-per-cpu 1500 --time 01:00:00 --x11 --pty bash

## salloc

add the flag -Y when sshing to the node.

    ssh -Y wbn001

# XVFB

If your application requires X11 in order to run, but does not need to
be interactive you can use X11 Virtual Frame Buffer. This may be
required to in order to run visual applications on the compute nodes.
Prepending any command with `xfvb-run` will provide a dummy X11 server
for the application to render to.  
e.g.

    xvfb-run xterm
