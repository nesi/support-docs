A virtual desktop provides a graphical interface to using the cluster.
Desktops are hosted within Singularity containers, so not all of the
NeSI software stack is supported. If you would like to build your own
desktop containers with the code
[here](https://github.com/nesi/nesi-singularity-recipes).

Rendering is d<dfn class="dictionary-of-numbers">one cluster-side</dfn>,
and compressed before being sent to your local machine. This means any
rendering should be significantly more responsive than when using
X<dfn class="dictionary-of-numbers">11 on it</dfn>s own (approximately
<dfn class="dictionary-of-numbers">40 times faster)</dfn>.

# Connecting Through SSH

> ### Requirements {#prerequisites}
>
> You must be able to [forward a
> port](https://support.nesi.org.nz/hc/en-gb/articles/360001523916).

> ### Note {#prerequisites}
>
> The Virtual desktops are still in development, please report any
> issues to NeSI support, or open an issue
> [here](https://github.com/nesi/nesi-virtual-desktops/issues).

# Setup

## Port Forwarding

A port on your local machine must be forwarded to Mahuika.

[Learn about setting up port
forwarding](https://support.nesi.org.nz/hc/en-gb/articles/360001523916). 

For example:

    ssh -L 1234:localhost:1234 mahuika

> ### Tip {#prerequisites}
>
> Port numbers should be between **1025-49151**. It\'s OK to use the
> same number for local and remote ports (makes it easier to remember
> too!)

## Add VDT to path

Run the command.

    echo "export PATH="/opt/nesi/vdt/:\$PATH"">>~/.bash_profile;. ~/.bash_profile

to add the VDT command to your path, if you don\'t do this step you can
still use the `vdt` command as `/opt/nesi/vdt/vdt`

# Commands {#commands style="display: flex;"}

`vdt -h` for general help or `vdt [command] -h` for help relating to
that command.

  -------------------- ----------------------------------------- --------------------------------------------------------------------------------------------
  vdt start \[port\]   `vdt start 4321`                          Starts a desktop session on the login node. It will last until the shell is closed.
                       `vdt start 4321 &`                        Starts a desktop session on the login node. It will continue running after you disconnect.
                       `vdt start -r wbg005 4321 &`              Starts a desktop session on another  node. It will continue running after you disconnect.
                       `salloc [slurm flags] vdt start 4321 &`   Starts a desktop session in a Slurm job. It will continue running after you disconnect.
  vdt list             `vdt list`                                Lists all your sessions.
  vdt kill \[name\]    `vdt kill my_desktop`                     Kills desktop \[name\].
  -------------------- ----------------------------------------- --------------------------------------------------------------------------------------------

#  

# Settings

Recommend setting scaling to \'remote\'

::: {style="display: flex;"}
![](https://support.nesi.org.nz/hc/article_attachments/360004678036/fig1.svg){width="426"
height="362"}![](https://support.nesi.org.nz/hc/article_attachments/360005192376/VirtualScaling.png)
:::

# Examples

The conditions for running a desktop on the login node are similar to
when using a shell. There are no time limits, but should not be used for
large or long running jobs. Any serious amount of computation should be
launched with SLURM, this can be d<dfn class="dictionary-of-numbers">one
using the terminal </dfn>or GUI. \
\

In the case where your work needs to be run interactively, and cannot be
managed from a different node, you can launch the desktop on a compute
node 

## On the login node

You may run desktops on the login node, provided you are not doing any
serious computation there.

Once on Mahuika, enter in the path to the desktop followed by your
forwarded port (`--help` for more options).

    vdt start -N my_desktop [port]

<!--
<p>
  And select <code>n) New desktop.</code>&nbsp;
</p>
-->

Then in a web browser navigate to your forwarded address. e.g.

![mceclip0.png](https://support.nesi.org.nz/hc/article_attachments/360004789255/mceclip0.png)

## On a compute node {#compute}

<!--
<h2>On a compute node</h2>
<p>
  To start a desktop on a compute node you must already have an job running, this
  could be a regular job submitted with sbatch, or a dedicated allocation. Starting
  a desktop inside an allocation will automatically forward your connection to
  the appropriate node.
</p>
<p>Otherwise you can connect using the menu.</p>
<p>
  <code>a) Adopt a SLURM session.</code>
</p>
<p>
  Or by supplying a jobid or node name when giving the command.
</p>
<p>
  or <code>-j &lt;jobid&gt;</code>
</p>
<p>
  or <code>-n &lt;node&gt;</code>(must have an allocation on that node)
</p>
<p>&nbsp;for example</p>
<pre><code>/opt/nesi/vdt/run 1234&nbsp;-j 13864207</code></pre>
<blockquote class="blockquote-warning">
  <h3 id="prerequisites">Note</h3>
  <p>
    To <em>reconnect</em> to a desktop session running on a compute node you
    must be forwarded to that node. A desktop running on a compute node is not
    visible from the login node.
  </p>
</blockquote>
<h2>Reconnecting</h2>
<p>
  Desktops are persistent,&nbsp; you can reconnect to a desktop running on the
  cluster using&nbsp;<code>/opt/nesi/vdt/run</code>&nbsp;and then selecting
  <code>#) Connect.</code> under your chosen session.
</p>
<h2>Killing</h2>
<p>
  Closing your terminal or ctrl + C will not terminate the session, only the webserver
  connecting you. You can end a desktop by running
  <code>/opt/nesi/vdt/run</code>&nbsp;and then selecting <code>#) Kill.</code>
  under your chosen session.
</p>
<p>&nbsp;</p>
-->

If you plan on doing computation in the desktop instance, you should be
doing it on a compute node.

If you already have a Slurm job running, you can start a desktop on that
node using the `-r [hostname]` e.g.

    vdt start -N my_desktop -r [hostname] [port]

If you want to start a new Slurm session, you can do this using salloc ,
the hostname will be inferred from environment (unless explicitly set).

    salloc --job-name my_desktop --nodes 1 --cpus-per-task 8 --time 01:00:00 vdt start 1234

## Persistence

If you wish your desktop to stay around after you close your shell, add
`&` after the command. e.g.

    vdt start [port] &

# Troubleshooting

-   Add `-v` flag for extra information.
-   Try using `-c` to remove local files.
-   Close any extra `/usr/bin/ssh-agent` or `/usr/bin/gpg-agent`
    processes running in the background.

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
