A virtual desktop provides a graphical interface to using the cluster.
Desktops are hosted within Singularity containers, so not all of the
NeSI software stack is supported. If you would like to build your own
desktop containers with the code
[here](https://github.com/nesi/nesi-singularity-recipes).

Rendering is done cluster-side, and compressed before being sent to your
local machine. This means any rendering should be significantly more
responsive than when using X11 on its own (approximately 40 times
faster).

The quickest and easiest way to get started with a desktop is through
Jupyter on NeSI,[ ]{style="font-size: 15px;"}[connect
here](https://jupyter.nesi.org.nz/)[.]{style="font-size: 15px;"}

First Time Install
------------------

In a terminal, run the command:

    pip install --user git+https://github.com/nesi/nesi-virtual-desktops

Restart your JupyterLab instance and you should see a \'VirtualDesktop\'
icon.

Connecting
----------

Click the icon labelled \'VirtualDesktop\', The desktop instance will
last as long as your Jupyter session.

Settings
========

Modules
-------

You may manage modules inside a terminal as usual using the `module`
command, however these changes won\'t propagate to the desktop
environment. Modules to be loaded in the desktop can be set by modifying
the file at `~/.vnc/setup.config`

noVNC
-----

Recommend setting scaling to \'remote\'

::: {style="display: flex;"}
![](https://support.nesi.org.nz/hc/article_attachments/360004678036/fig1.svg){width="426"
height="362"}![](https://support.nesi.org.nz/hc/article_attachments/360005192376/VirtualScaling.png)
:::

> ### Restore Defaults {#prerequisites}
>
> All local settings can be restored by running the command `vdt clean`
> (or `/opt/nesi/vdt clean`). Note, this will probably break any running
> desktop sessions.

::: {style="display: flex;"}
*You can help contribute to this
project [here](https://github.com/nesi/nesi-virtual-desktops/projects/1).*
:::
