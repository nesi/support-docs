> ### Requirements {#prerequisites}
>
> -   Have working
>     [terminal](https://support.nesi.org.nz/hc/en-gb/sections/360000189696)
>     set up.

X-11 is a protocol for rendering graphical user interfaces (GUIs) that
can be sent along an SSH tunnel. If you plan on using a GUI on a NeSI
cluster you will need to have an X-Server and X-Forwarding set up.

X-Servers
=========

You must have a X-server running on your local machine in order for a
GUI to be rendered.

Download links for X-servers can be found below.

  --------- ---------------------------------------------------
  MacOS     [Xquartz](https://www.xquartz.org/)
  Linux     [Xorg](https://www.x.org/wiki/Releases/Download/)
  Windows   [Xming](https://sourceforge.net/projects/xming/)
  --------- ---------------------------------------------------

Make sure you have launched the server and it is running in the
background, look for
this ![mceclip0.png](https://support.nesi.org.nz/hc/article_attachments/360002963236/mceclip0.png) symbol
in your taskbar 

> ### Note {#prerequisites}
>
> MobaXterm has a build in X server, no setup required. By default the
> server is started alongside MobaXterm. You can check it\'s status in
> the top left hand corner
> (![xon.png](https://support.nesi.org.nz/hc/article_attachments/360002939175/xon.png)=on, ![off.png](https://support.nesi.org.nz/hc/article_attachments/360002939155/off.png)=off). 

X-Forwarding
============

Finally your ssh tunnel must be set up to \'forward\' along X-11
connections. 

OpenSSH (terminal)
------------------

Make sure the `-Y` or `-X` flag is included

    ssh -Y user@lander.nesi.org.nz

    ssh -Y login.nesi.org.nz

MobaXterm
---------

 Under \'session settings\' for your connection make sure the X-11
forwarding box is checked.

![x11moba.png](https://support.nesi.org.nz/hc/article_attachments/360002871175/x11moba.png){width="451"
height="303"}

If the
![mceclip0.png](https://support.nesi.org.nz/hc/article_attachments/360005129276/mceclip0.png)
button in the top right corner of your window is coloured, the X-server
should be running.

X-Forwarding with *tmux*
========================

In order to connect X11 into a tmux session you make the following
change to your config file.

    tmux show -g | sed 's/DISPLAY //' > ~/.tmux.conf

Interactive Slurm jobs
======================

In order to make use of X11 in an interactive Slurm job:

srun
----

Add the flag `--x11`

    srun --ntasks 36 --mem-per-cpu 1500 --time 01:00:00 --x11 --pty bash

salloc
------

add the flag -Y when sshing to the node.

    ssh -Y wbn001

XVFB
====

If your application requires X11 in order to run, but does not need to
be interactive you can use X11 Virtual Frame Buffer. This may be
required to in order to run visual applications on the compute nodes.
Prepending any command with `xfvb-run` will provide a dummy X11 server
for the application to render to.\
e.g.

    xvfb-run xterm
