A virtual desktop provides a graphical interface to using the cluster.
Desktops are hosted within Singularity containers, so not all of the
NeSI software stack is supported. If you would like to build your own
desktop containers with the code
[here](https://github.com/nesi/nesi-singularity-recipes).

Rendering is d[one cluster-side]{.dfn .dictionary-of-numbers}, and
compressed before being sent to your local machine. This means any
rendering should be significantly more responsive than when using X[11
on its own ]{.dfn .dictionary-of-numbers}(approximately [40 times
faster)]{.dfn .dictionary-of-numbers}.

The quickest and easiest way to get started with a desktop is through
Jupyter on NeSI,[ ]{style="font-size: 15px;"}[connect
here](https://jupyter.nesi.org.nz/)[.]{style="font-size: 15px;"}

Connecting
----------

Click the icon labelled \'VirtualDesktop\', The desktop instance will
last as long as your Jupyter session.

Setup Scripts
-------------

Several scripts are available that will help you get started by setting
up desktop shortcuts and loading module in the base environment. These
can be found at `$VDT_ROOT/setup_scripts`

Settings
========

Environment {#modules}
-----------

You may manage modules inside a terminal as usual using the `module`
command, however these changes won\'t propagate to the desktop
environment. Modules to be loaded in the desktop can be set by modifying
the file at `~/.vdt/vdtrc.sh`. This file is sourced before launching the
desktop.

 
-

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
