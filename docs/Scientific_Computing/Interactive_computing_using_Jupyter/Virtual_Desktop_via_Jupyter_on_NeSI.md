---
created_at: '2020-07-08T01:45:40Z'
hidden: false
position: 3
tags: []
title: Virtual Desktop via Jupyter on NeSI
vote_count: 2
vote_sum: 2
zendesk_article_id: 360001600235
zendesk_section_id: 360001189255
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
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

## Customisation

Most of the customisation of the desktop can be done from within,  
panels, desktop, software preferences.

### `pre.bash`

Enviroment set in `singularity_wrapper.bash` can be changed by creating
a file `$XDG_CONFIG_HOME/vdt/pre.bash` Anything you want to run
\*before\* launching the container put in here.

``` sl
export VDT_BASE_IMAGE="~/my_custom_container.sif" # Use a different image file.
export VDT_RUNSCRIPT="~/my_custom_runscript" # Use a different runscript.

export OVERLAY="TRUE"
export BROWSER="chrome" # Desktop session will inherit this.

module load ANSYS/2021R2 # Any modules you want to be loaded in main instance go here.
```

### \`post.bash\`

Environment set in `runscript_wrapper.bash` can be changed by creating a
file `$XDG_CONFIG_HOME/vdt/post.bash`

Things you may wish to set here are:  
`VDT_WEBSOCKOPTS`, `VDT_VNCOPTS`, any changes to the wm environment, any
changes to path, this include module files.

``` sl
export VDT_VNCOPTS="-depth 16" # This will start a 16bit desktop
export BROWSER="chrome" # Desktop session will inherit this.

module load ANSYS/2021R2 # Any modules you want to be loaded in main instance go here.
```

## Custom container

You can build your own container bootstrapping off
`vdt_base.sif`/`rocky8vis.sif` and then overwrite the default by setting
`VDT_BASE_IMAGE` in `pre.bash`.

<!--
<h2 id="h_01HDHQPY636ARH8CE6RP0700VX">Setup Scripts</h2>
<p>
  Several scripts are available that will help you get started by setting up desktop
  shortcuts and loading module in the base environment. These can be found at
  <code>$VDT_ROOT/setup_scripts</code>
</p>
<h2>noVNC</h2>
<p>Recommend setting scaling to 'remote'</p>
<div style="display: flex;">
  <img src="https://support.nesi.org.nz/hc/article_attachments/360004678036" width="426" height="362"><img src="https://support.nesi.org.nz/hc/article_attachments/360005192376">
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
