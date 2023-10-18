---
created_at: '2022-08-03T21:35:50Z'
hidden: false
label_names: []
position: 4
title: Cylc
vote_count: 0
vote_sum: 0
zendesk_article_id: 5254610390415
zendesk_section_id: 360000040076
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<h2 id="01G9X8TM54HGX95GWY5CR3E4CS">What is Cylc</h2>
<p><span><a href="https://cylc.github.io/" target="_self">Cylc</a> is a </span><strong>general purpose workflow engine</strong><span> that can also orchestrate </span><strong>cycling systems</strong><span> very efficiently. It is used in production weather, climate, and environmental forecasting on HPC, but is not specialised to those domains.</span><span></span></p>
<p>Using a workflow engine may enable you to run large parametric or sensitivity studies while ensuring scalability, reproducibility and flexibility. If you have embarrassingly parallel jobs then Cylc might be a good solution for you. The workflow engine will allow for the concurrent execution of parallel jobs, depending on the task graph and available resources on the platform. One advantage of this approach over running a monolithic, parallel executable is that each task will require less resources that the complete problem, it is thus easier for each task to slip into the queue and start running.</p>
<p>See the NeSI  <a href="https://snakemake-on-nesi.sschmeier.com/" target="_self">Snakemake</a> page for another, possible choice.</p>
<p>In this article, we show how you can create a simple workflow and run it on NeSI's platform. Consult the <a href="https://cylc.github.io/documentation/" target="_self">Cylc documentation</a> for more elaborate examples, including some with a cycling (repeated) graph pattern. One of the strengths of Cylc is that simple workflows can be executed simply while allowing for very complex workflows, with thousands of tasks, which may be repeated ad infinitum. </p>
<p> </p>
<h2 id="01H8JX6Z1X199ZG99REHBGTKAN">SSH configuration</h2>
<p>Cylc uses ssh <span> </span>to automatically start schedulers on configured "run hosts" and to submit jobs to remote platforms, so if you haven't already done so you need to allow ssh to connect to other hosts on the HPC cluster without prompting for a passphrase (all HPC nodes see the same filesystem, so this is easy):</p>
<ul>
<li>run<span> </span><strong><code>ssh-keygen</code></strong><span> </span>to generate a public/private key pair with<span> </span><strong>no passphrase</strong><span> </span>(when it asks for a passphrase, just hit enter)</li>
<li>add your own public key to your authorized keys file:<span> </span><strong><code>cat .ssh/id_rsa.pub &gt;&gt; .ssh/authorized_keys</code></strong> </li>
<li>check that your<span> </span><strong>keys, authorized_keys file, ssh directory,<span> </span></strong>and<strong><span> </span>home directory</strong><span> </span>all have sufficiently secure file permissions. If not,<span> </span><code>ssh</code><span> </span>will silently revert to requiring password entry. See for example<span> </span><a class="external-link" href="https://www.frankindev.com/2020/11/26/permissions-for-.ssh-folder-and-key-files/" rel="nofollow">https://www.frankindev.com/2020/11/26/permissions-for-.ssh-folder-and-key-files/</a>
</li>
<li>make sure your<span> </span><strong>home directory</strong><span> </span>has a maximum of<span> </span><strong>750</strong><span> </span>permissions</li>
</ul>
<p>Now you should be able to run<span> </span><strong><code>ssh mahuika02</code></strong>(for example) without being asked for a passphrase.</p>
<h2 id="01G9X8TM55D8QFZK1483S2X5HX"><span>How to select the Cylc version</span></h2>
<p><span>Cylc has been installed on Māui and Mahuika, there is no need to load any module,</span></p>
<pre><span>$ which cylc<br>/opt/nesi/share/bin/cylc<br></span></pre>
<p><span>(Access if via the NeSI module, which is loaded by default.) </span></p>
<p><span>Be aware that the default version</span></p>
<pre><span>$ cylc version<br>7.9.1</span></pre>
<p>is not the latest, and that configuration file and Cylc commands have changed significantly at version 8.</p>
<p><strong>New Cylc users should use version 8 or later</strong>,</p>
<pre>$ cylc list-versions<br><br>7.9.1 <br>...<br>8.0.1 <br>cylc -&gt; 7.9.1</pre>
<p>You can select your Cylc version by setting the environment variable CYLC_VERSION, for instance,</p>
<pre><code class="bash plain">$ export CYLC_VERSION=8.0.1<br>$ cylc version<br>8.0.1</code></pre>
<p>At the time of writing, the latest version is 8.0.1.</p>
<h2 id="01G9X8TM552SXXBMFG41TGRKBP">A simple example of a Cylc workflow</h2>
<p>To demonstrate Cylc, let's start with a workflow, which we call "simple",</p>
<pre>$ mkdir -p ~/cylc-src/simple<br>$ cd ~/cylc-src/simple</pre>
<p>Create/edit the following <strong>flow.cylc</strong> file containing</p>
<pre>[scheduling] # Define the tasks and when they should run<br>  [[graph]]<br>    <span class="wysiwyg-color-blue">R1 = """ # R1 means run this graph once</span><br><span class="wysiwyg-color-blue">      taskA &amp; taskB =&gt; taskC # Defines the task graph</span><br>    """<br>[runtime] # Define what each task should run<br>  [[root]] # Default settings inherited by all tasks<br>    <span class="wysiwyg-color-red">platform = mahuika-slurm</span> # Run "cylc conf" to see platforms. <br>    [[[directives]]] # Default SLURM options for the tasks below<br>       <span class="wysiwyg-color-red">--account = nesi99999 # CHANGE</span><br>  [[taskA]]<br>    script = echo "running task A"<br>      [[[directives]]] # specific SLURM option for this task<br>        <span class="wysiwyg-color-red">--ntasks = 2</span><br>  [[taskB]]<br>    script = echo "running task B"<br>  [[taskC]]<br>    script = echo "running task C"</pre>
<p id="01G9X8TM55MJRN2SPQX792TS6E">In the above example, we have three tasks (taskA, taskB and taskC), which run under SLURM (hence platform = mahuika-slurm). Type</p>
<pre class="p1"><span class="s1">cylc config --platform-names</span></pre>
<p class="p1"><span class="s1">to see a list of platforms. The SLURM settings for taskA are in the [[[directives]]] section.</span></p>
<h2 id="01GFPTSN3XAE8EXPK03B6W99N7">How to interact with Cylc</h2>
<p>Cylc takes command lines. Type </p>
<pre>$ cylc help all</pre>
<p>to see the available commands. Type </p>
<pre>$ cylc help install # or cylc install --help</pre>
<p>to find out how to use a specific command (in this case "install").</p>
<h2 id="01G9X8TM55ZW1DWYMSEYTRQBYZ">Installing a workflow</h2>
<p>Prior to running a workflow, <strong>it must be installed</strong> to a run directory. Due to limited disk space in home directories on NeSI, Cylc has been configured to symlink the <span>standard run directories to project directories, if $PROJECT is defined</span>. Hence, you need to set</p>
<pre>$ export PROJECT=nesi99999 # CHANGE</pre>
<p>Then install the workflow with</p>
<pre>cylc install simple</pre>
<h2 id="01G9X8TM55X80D5CPV6ATFYJHM">Validating the workflow</h2>
<p>It's a good idea to check that there are no syntax errors in flow.cylc,</p>
<pre class="p1"><span class="s1">$</span><span class="s2"> cylc validate simple<br>Valid for cylc-8.0.1</span></pre>
<h2 id="01G9X8TM55X4AHY2WEE1ENZF34">Looking at the workflow graph</h2>
<p>A useful command is </p>
<pre>$ cylc graph simple</pre>
<p>which will generate a png file, generally in the /tmp directory with a name like <span class="s1">/tmp/tmpzq3bjktw.PNG. Take note of the name of the png file. To visualise the file you can type </span></p>
<pre>$ display  <span class="s1">/tmp/tmpzq3bjktw.PNG # ADJUST the file name</span></pre>
<p>Here, we see that our workflow "simple" has a "taskC", which waits for "taskA" and "taskB" to complete,</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/5255042984079" alt="simple.png"></p>
<p>The "1" indicates that this workflow graph is executed only once.</p>
<h2 id="01G9X8TM56VMG4J8KRW0NNZWSZ">Different ways to interact with Cylc</h2>
<p>Every Cylc action can be executed via the command line. Alternatively, you can invoke each action through a <strong>terminal user interface</strong> (tui), </p>
<pre>$ cylc tui simple</pre>
<p>Another alternative, is to use the <strong>graphical user interface</strong></p>
<pre>$ cylc gui</pre>
<p>Read below on how access the web interface running on NeSI using your local browser.</p>
<h3 id="01GSRRYEYECWFWBZFSK8ERZAXS">Connecting via Jupyter</h3>
<p>If you're connecting through <a href="https://jupyter.nesi.org.nz">https://jupyter.nesi.org.nz</a> you'll need to replace anything before the ":" with <a href="https://jupyter.nesi.org.nz/user/USERNAME/proxy/">https://jupyter.nesi.org.nz/user/USERNAME/proxy/</a> to get access to the web graphical user interface (where USERNAME is your NeSI user name). Hence the URL becomes <a href="https://jupyter.nesi.org.nz/user/USERNAME/proxy/">https://jupyter.nesi.org.nz/user/USERNAME/proxy/</a><a href="http://wbn003:8888/cylc?token=30d9e2b3dfe097318539cff02f69a24217f2967e8809f0a9">8888/cylc?token=TOKEN</a></p>
<h3 id="01GSRS0FDDK8VJZ61SM3H3S0AH">Connecting via SSH</h3>
<p class="x_MsoNormal"><span>First open ssh tunnelling, so that a given port on your local machine (e.g. your laptop) maps to the Cylc UI Server’s port on the HPC. On your local machine, type</span></p>
<pre class="x_MsoNormal">$ ssh -N -L PORT:localhost:PORT HOST</pre>
<p class="x_MsoNormal">where <strong>PORT</strong> is a valid port number and <strong>HOST</strong> can be maui or mahuika. See the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001523916-Port-Forwarding">NeSI page</a> for the range of allowed ports (currently 1024-49151). Choose any number in this range but make sure your port number is fairly unique to avoid clashing with other users. Option <span>-N is optional: it opens the connection without logging you into the shell.</span></p>
<p class="x_MsoNormal"><span>Then ssh to the host (e.g. mahuika)</span></p>
<pre class="x_MsoNormal"><span>$ ssh HOST</span></pre>
<p class="x_MsoNormal"><span>and add the following to <strong>$HOME/.cylc/uiserver/jupyter_config.py </strong>on the <strong>HOST</strong>.</span></p>
<pre class="x_MsoNormal">c.ServerApp.open_browser=False<br>c.ServerApp.port=PORT<br><span></span></pre>
<p class="x_MsoNormal">where PORT and HOST match the values you selected when opening the ssh tunnel.</p>
<p class="x_MsoNormal">You're now ready to fire up the web graphical interface</p>
<pre class="x_MsoNormal">$ cylc gui</pre>
<p class="x_MsoNormal">Just copy the URL that looks like</p>
<pre class="p1"><span class="s1">http://127.0.0.1:PORT/cylc?token=TOKEN</span></pre>
<p class="x_MsoNormal">into your web browser.<span> (Again substitute HOST and PORT with the values chosen above.)</span></p>
<h2 id="01G9X8TM56RRFMK8Y0H56RKEMQ">How to execute a workflow</h2>
<p>To execute the workflow type</p>
<pre>$ cylc play --no-detach simple</pre>
<p><span>The "--no-detach" option makes scheduler run in the foreground so you can see its output in your terminal. Without this option it will "daemonize" so it can keep running even if you log out.</span></p>
<p>Command</p>
<pre>$ cylc scan</pre>
<p>will list all running and installed workflows.<span class="s1"></span></p>
<h2 id="01G9X8TM5665B7RHWWTQEZBG2E">Checking the output</h2>
<pre>$ cylc cat-log simple//1/taskA  # note // between workflow and task ID</pre>
<p>of the first cycle of taskA. The "1" refers to the task iteration, or cycle point. <span>Our simple workflow only has one iteration (as dictated by the R1 graph above). </span></p>
<h2 id="01G9X8TM56H3QSGFM28FRGAD83">How to clean or remove a workflow</h2>
<pre>$ cylc clean simple</pre>
<p>will remove the file structure associated with workflow "simple".</p>
<h2 id="01G9X8TM560YEF30SXD3V2BFBG">Where jobs, results and log files are stored</h2>
<p>Cylc will create a directory under $HOME/cylc-run. On NeSI, the output of the runs will be stored in the project directory, with a symbolic link pointing from the user home directory to the project directory</p>
<pre class="p1"><span class="s1">$</span><span class="s2"> ls -l $HOME/cylc-run/simple/run1</span><br><span class="s3">lrwxrwxrwx 1 pletzera pletzera 54 Aug<span class="Apple-converted-space">  </span>5 03:19 </span><span class="s4">/home/pletzera/cylc-run/simple/run1</span><span class="s3"> -&gt; </span><span class="s2">/nesi/nobackup/nesi99999/pletzera/cylc-run/simple/run1</span></pre>
<h2 id="01G9X8TM56RGGS0RY0F1VJFD1C">About Cylc</h2>
<p>More can be found about Cylc <a href="https://cylc.github.io/cylc-doc/nightly/html/tutorial/index.html" target="_blank" rel="noopener">here</a>, including what Cylc is and how you can leverage Cylc to submit parallel jobs.</p>