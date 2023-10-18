---
created_at: '2020-07-08T01:45:40Z'
hidden: false
label_names: []
position: 3
title: Virtual Desktop via Jupyter on NeSI
vote_count: 2
vote_sum: 2
zendesk_article_id: 360001600235
zendesk_section_id: 360001189255
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
 !!! Info
     This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
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

# Settings

## Environment

You may manage modules inside a terminal as usual using the `module`
command, however these changes won't propagate to the desktop
environment. Modules to be loaded in the desktop can be set by modifying
the file at `~/.vdt/vdtrc.sh`. This file is sourced before launching the
desktop.

## Setup Scripts

Several scripts are available that will help you get started by setting
up desktop shortcuts and loading module in the base environment. These
can be found at `$VDT_ROOT/setup_scripts`

<!--
<h2>noVNC</h2>
<p>Recommend setting scaling to 'remote'</p>
<div style="display: flex;">
  <img src="https://support.nesi.org.nz/hc/article_attachments/360004678036/fig1.svg" width="426" height="362"><img src="https://support.nesi.org.nz/hc/article_attachments/360005192376/VirtualScaling.png">
</div>
<blockquote class="blockquote-warning">
  <h3 id="prerequisites">Restore Defaults</h3>
  <p>
    All local settings can be restored by running the command
    <code>vdt clean</code> (or <code>/opt/nesi/vdt clean</code>). Note, this
    will probably break any running desktop sessions.
  </p>
</blockquote>
-->

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
