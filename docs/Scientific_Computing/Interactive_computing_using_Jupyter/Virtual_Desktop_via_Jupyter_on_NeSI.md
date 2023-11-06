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
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>A virtual desktop provides a graphical interface to using the cluster. Desktops are hosted within Singularity containers, so not all of the NeSI software stack is supported. If you would like to build your own desktop containers with the code <a href="https://github.com/nesi/nesi-singularity-recipes" target="_self">here</a>.</p>
<p>Rendering is done cluster-side, and compressed before being sent to your local machine. This means any rendering should be significantly more responsive than when using X11 on its own (approximately 40 times faster).</p>
<p>The quickest and easiest way to get started with a desktop is through Jupyter on NeSI,<span style="font-size: 15px;"> </span><a href="https://jupyter.nesi.org.nz/" target="_blank" rel="noopener">connect here</a><span style="font-size: 15px;">.</span></p>
<h2 id="h_01HDHQPY630C2APR4EK5Q5DE1X">Connecting</h2>
<p>Click the icon labelled 'VirtualDesktop', The desktop instance will last as long as your Jupyter session.</p>
<h2 id="h_01HDHQWZ570GN55N6RVT3BJC62">Customisation</h2>
<p>Most of the customisation of the desktop can be done from within,<br>panels, desktop, software preferences.</p>
<h3 id="h_01HDHR0AN8384HZCFFP4QVAKM0"><code>pre.bash</code></h3>
<p>Enviroment set in <code>singularity_wrapper.bash</code> can be changed by creating a file <code>$XDG_CONFIG_HOME/vdt/pre.bash</code> Anything you want to run *before* launching the container put in here.</p>
<pre><code>export VDT_BASE_IMAGE="~/my_custom_container.sif" # Use a different image file.
export VDT_RUNSCRIPT="~/my_custom_runscript" # Use a different runscript.

export OVERLAY="TRUE"
export BROWSER="chrome" # Desktop session will inherit this.

module load ANSYS/2021R2 # Any modules you want to be loaded in main instance go here.
</code></pre>
<h3 id="h_01HDHQZZXHWJT415NKB1SKABFG">`post.bash`</h3>
<p>Environment set in <code>runscript_wrapper.bash</code> can be changed by creating a file <code>$XDG_CONFIG_HOME/vdt/post.bash</code></p>
<p>Things you may wish to set here are:<br><code>VDT_WEBSOCKOPTS</code>, <code>VDT_VNCOPTS</code>, any changes to the wm environment, any changes to path, this include module files.</p>
<pre><code>export VDT_VNCOPTS="-depth 16" # This will start a 16bit desktop<br>export BROWSER="chrome" # Desktop session will inherit this.

module load ANSYS/2021R2 # Any modules you want to be loaded in main instance go here.
</code></pre>
<h2 id="h_01HDHQZM89ZCH66QV5QNNHAMNH">Custom container</h2>
<p>You can build your own container bootstrapping off <code>vdt_base.sif</code>/<code>rocky8vis.sif</code> and then overwrite the default by setting <code>VDT_BASE_IMAGE</code> in <code>pre.bash</code>.</p>
<p><!--
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
--></p>
<div style="display: flex;">
<p> </p>
<p><em>You can help contribute to this project <a href="https://github.com/nesi/nesi-virtual-desktops/projects/1" target="_self">here</a>.</em></p>
</div>
<p><!--
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
--></p>