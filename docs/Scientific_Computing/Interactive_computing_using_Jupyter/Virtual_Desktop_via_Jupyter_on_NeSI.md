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
Jupyter on NeSI, [connect here](https://jupyter.nesi.org.nz/).

## Connecting

Click the icon labelled 'VirtualDesktop', The desktop instance will last
as long as your Jupyter session.

## Setup Scripts

Several scripts are available that will help you get started by setting
up desktop shortcuts and loading module in the base environment. These
can be found at `$VDT_ROOT/setup_scripts`

# Settings

## Environment

You may manage modules inside a terminal as usual using the `module`
command, however these changes won't propagate to the desktop
environment. Modules to be loaded in the desktop can be set by modifying
the file at `~/.vdt/vdtrc.sh`. This file is sourced before launching the
desktop.

##  

## noVNC

Recommend setting scaling to 'remote'

<img src="img/fig1.svg" width="426" height="362" />![](img/VirtualScaling.png)

> ### Restore Defaults
>
> All local settings can be restored by running the command `vdt clean`
> (or `/opt/nesi/vdt clean`). Note, this will probably break any running
> desktop sessions.

*You can help contribute to this
project [here](https://github.com/nesi/nesi-virtual-desktops/projects/1).*

<!--
<table style="height:190px;width:722px;display:none">
  <tbody>
    <tr>
      <td style="width:47px">&nbsp;Desktop</td>
      <td style="width:272.122px">&nbsp;command</td>
      <td style="width:143.878px">Working</td>
      <td style="width:138px">OS</td>
      <td style="width:62px">Desktop</td>
    </tr>
    <tr>
      <td style="width:47px">eng_dev</td>
      <td style="width:272.122px">
        <code>/opt/nesi/vdt/run&nbsp;eng_dev &lt;port&gt;</code>
      </td>
      <td style="width:143.878px">
        <p>
          ABAQUS<br>
          ANSYS<br>
          MATLAB<br>
          COMSOL
        </p>
      </td>
      <td style="width:138px">Centos7</td>
      <td style="width:62px">xfce</td>
    </tr>
    <tr>
      <td style="width:47px">default</td>
      <td style="width:272.122px">
        <code>/opt/nesi/vdt/run&nbsp;default &lt;port&gt;</code>
      </td>
      <td style="width:143.878px">
        <p>&nbsp;</p>
      </td>
      <td style="width:138px">Centos7</td>
      <td style="width:62px">xfce</td>
    </tr>
  </tbody>
</table>
-->
