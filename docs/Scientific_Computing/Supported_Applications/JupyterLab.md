---
created_at: '2019-08-09T00:46:44Z'
hidden: false
label_names: []
position: 33
title: JupyterLab
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001093315
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<blockquote class="blockquote-warning">
<h3 id="prerequisites">Note</h3>
This documentation contains our legacy instructions for running JupyterLab by tunnelling through the lander node.<br><span class="wysiwyg-font-size-large"><a href="https://support.nesi.org.nz/hc/en-gb/articles/360001555615" target="_blank" rel="noopener">If you are a Mahuika cluster user, we recommend using jupyter via  jupyter.nesi.org.nz. Follow this link for more information </a></span>
</blockquote>
<p>NeSI provides a service for working on Jupyter Notebooks. As a first step JupyterLab can be used on Mahuika nodes. JupyterLab is a single-user web-based Notebook server, running in the user space. JupyterLab servers should be started preferably on a compute node, especially for compute intensive or memory intensive workloads. For less demanding work the JupyterLab server can be started on a login or virtual lab node. After starting the server your local browser can be connected. Therefore port forwarding needs to be enabled properly. The procedure will be simplified in future, but now require the following steps, which are then described in more details:</p>
<ul>
<li>
<a href="#h_a0e4107a-358d-4db6-a7a4-c2c3273c74ed" target="_self">Launch JupyterLab</a>
<ul>
<li>
<a href="#h_22b17d98-8054-4898-871e-38a42a2e3849" target="_self">Connect to the NeSI system to establish SSH port forwarding </a>
<ul>
<li>
<a href="#h_892370eb-662a-4480-9ae4-b56fd64eb7d0" target="_self">SSH Command Line</a> OR</li>
<li><a href="#h_cc633523-5df0-4f24-a460-391ced9a0316" target="_self">MobaXterm GUI</a></li>
</ul>
</li>
<li>open another session to the NeSI system</li>
<li>
<a href="#h_a46369a1-5f2c-4ed8-82c2-f06c0c1d58b4" target="_self">Launch the JupyterLab server</a>
<ul>
<li>
<a href="#h_fca84ce8-3167-4c14-a128-23049417a5dd" target="_self">on login nodes / virtual labs</a> OR</li>
<li><a href="#h_6cb2d7b4-f63c-49ed-ba73-f58fd903d86d" target="_self">on compute nodes</a></li>
</ul>
</li>
<li><a href="#h_22b17d98-8054-4898-871e-38a42a2e3849" target="_self">Launch JupyterLab in your local browser</a></li>
</ul>
</li>
<li><a href="#h_e7f80560-91c0-420a-bccb-17bbf8c2e916" target="_self">Kernels</a></li>
<li><a href="#h_04f2f4e2-8e7a-486d-aea5-e020eb9df66e" target="_self">Packages</a></li>
</ul>
<h1 id="h_a0e4107a-358d-4db6-a7a4-c2c3273c74ed">Launch JupyterLab</h1>
<p>Since JupyterLab is a web based application, and at NeSI launched behind the firewall, a <strong>port</strong> needs to be forwarded to your local machine, where your browser should connected. This ports are numbers between 2000 and 65000, which needs to be unique on the present machine. The default port for JupyterLab is 8888, but only one user can use this at a time.</p>
<p>To avoid the need for modifying the following procedure again and again, we suggest to (once) select a unique number (between 2000 and 65000). This number needs to be used while establishing the port forwarding and while launching JupyterLab. In the following we use the port number 15051 (<strong>please select another number</strong>).</p>
<h2 id="h_22b17d98-8054-4898-871e-38a42a2e3849">Setup SSH port forwarding </h2>
<blockquote class="blockquote-prereq">
<h3 id="prerequisites">Requirements</h3>
<ul>
<li>In the following we assume you already configured your<code>.ssh/config</code> to use two hop method as described in the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535" target="_self">Standard Terminal Setup</a>.</li>
</ul>
</blockquote>
<p>First, the port forwarding needs to be enabled between your local machine and the NeSI system. Therewith a local port will be connected to the remote port on the NeSI system. For simplicity, we kept both numbers the same (here 15051). This can be specified on the<a href="#h_892370eb-662a-4480-9ae4-b56fd64eb7d0" target="_self"> command line in the terminal</a> or using the <a href="#h_cc633523-5df0-4f24-a460-391ced9a0316" target="_self">MobaXterm GUI</a>.</p>
<h3 id="h_892370eb-662a-4480-9ae4-b56fd64eb7d0">SSH Command Line</h3>
<p>The ssh command need to be called with following arguments, e.g. for Mahuika:</p>
<pre><code>ssh -N -L 15051:localhost:15051 mahuika</code></pre>
<p>Here -N means "Do not execute a remote command" and -L means "Forward Local Port".</p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tips</h3>
<ul>
<li>For Maui_Ancil, e.g. w-mauivlab01 you may want to add the following to your <code>.ssh/config</code> to avoid establishing the additional hop manually.
<pre><code>Host maui_vlab
   User &lt;username&gt;
   Hostname w-mauivlab01.maui.niwa.co.nz
   ProxyCommand ssh -W %h:%p maui
   ForwardX11 <span class="hljs-literal">yes</span>
   ForwardX11Trusted <span class="hljs-literal">yes</span>
   ServerAliveInterval <span class="hljs-number">300</span>
   ServerAliveCountMax <span class="hljs-number">2</span></code></pre>
&lt;username&gt; needs to be changed. Hostnames can be adapted for other nodes, e.g. <code>w-clim01</code>
</li>
</ul>
</blockquote>
<h3 id="h_cc633523-5df0-4f24-a460-391ced9a0316">MobaXterm GUI</h3>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tips</h3>
<ul>
<li>MobaXterm has an internal terminal which acts like a linux terminal and can be configured as described in the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535" target="_self">Standard Terminal Setup</a>. Therewith the <a href="#h_892370eb-662a-4480-9ae4-b56fd64eb7d0" target="_self">SSH command line</a> approach above can be used.</li>
</ul>
</blockquote>
<p> </p>
<p>MobaXterm has a GUI to setup and launch sessions with port forwarding, click 'Tools &gt; MobaSSH Thunnel (port forwarding)':</p>
<ul>
<li>specify the lander.nesi.org.nz as SSH server address (right, lower box, first line)</li>
<li>specify your user name (right, lower box, second line)</li>
<li>specify the remote server address, e.g. login.mahuika.nesi.org.nz  (right, upper box first line)</li>
<li>specify the JupyterLab port number on the local side (left) and at the remote server (right upper box, second line)</li>
<li>Save</li>
</ul>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360002834175/sshTunnel.PNG" alt="sshTunnel.PNG"></p>
<h2 id="h_a46369a1-5f2c-4ed8-82c2-f06c0c1d58b4">Launch the JupyterLab server </h2>
<p>After successfully establishing the port forwarding, we need open another terminal and login to the NeSI system in the usual way, e.g. opening a new terminal and start another ssh session:</p>
<pre><code>ssh mahuika<br></code></pre>
<p>On the Mahuika login node, load the environment module which provides JupyterLab:</p>
<pre>module load JupyterLab</pre>
<p>Or alternatively, and particularly if you are using a Māui ancillary node instead of Mahuika, you can use the Anaconda version of JupyterLab instead:</p>
<pre><code>module load Anaconda3<br>module load IRkernel  # optional</code></pre>
<p>The JupyterLab server then can be started on the present node (login or virtual lab) or offloaded to a compute node. Please launch compute or memory intensive tasks <a href="#h_6cb2d7b4-f63c-49ed-ba73-f58fd903d86d" target="_self">on a compute node</a>.</p>
<h3 id="h_fca84ce8-3167-4c14-a128-23049417a5dd">On login nodes / virtual labs</h3>
<p>For very small (computational cheap and small memory) the JupyterLab can be started on the login or virtual lab using: </p>
<pre><code>jupyter lab --port 15051 --no-browser</code></pre>
<p>Where, <code>--port 15051</code> specifies the above selected port number and <code>--no-browser</code> option prevents JupyterLab from trying to open a browser on the compute/login node side. Jupyter will present output as described in the <a href="#h_6cb2d7b4-f63c-49ed-ba73-f58fd903d86d" target="_self">next section</a> including the URL and a unique key, which needs to be copied in your local browser.</p>
<h3 id="h_6cb2d7b4-f63c-49ed-ba73-f58fd903d86d">On compute node</h3>
<p>Especially notebooks with computational and memory intensive tasks should run on compute nodes. Therefore, a script is provided, taking care of port forwarding to the compute node and launching JupyterLab. A session with 60 min on 1 core can be launched using:</p>
<pre><code>srun --ntasks 1 -t 60  jupyter-compute 15051  # please change port number</code></pre>
<p>After general output, JupyterLab prints a URL with a unique key and the network port number where the web-server is listening, this should look similar to:</p>
<pre><code>...
[C 14:03:19.911 LabApp]
  To access the notebook, open this file in a browser:
      file:///scale_wlg_persistent/filesets/project/nesi99996/.local/share/jupyter/runtime/nbserver-503-open.html
  Or copy and paste one of these URLs:
      <strong>http://localhost:<span class="wysiwyg-color-red">15051</span>/?token=d122855ebf4d029f2bfabb0da03ae01263972d7d830d79c4</strong></code></pre>
<p>The last line will be needed in the browser later.</p>
<p>Therewith the Notebook and its containing tasks are performed on a compute node. You can double check e.g. using</p>
<pre><code>import os<br>os.open('hostname').read()</code></pre>
<p>More resources can be requested, e.g. by using:</p>
<pre><code>srun --ntasks 1 -t 60 --cpus-per-task 5 --mem 512MB jupyter-compute 15051 </code></pre>
<p>Where 5 cores are requested for threading and a total memory of 3GB. Please do not use <code>multiprocessing.cpu_count()</code> since this is returning the total amount of cores on the node. Furthermore, if you use libraries, which implement threading align the numbers of threads (often called jobs) to the selected number of cores (otherwise the performance will be affected).</p>
<h2 id="h_6cb2d7b4-f63c-49ed-ba73-f58fd903d86d">JupyterLab in your local browser </h2>
<p>Finally, you need to open your local web browser and copy and paste the URL specified by the JupyterLab server into the address bar. After initializing Jupyter Lab you should see a page similar to:</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360002463475/Jupyter.PNG" alt="Jupyter.PNG"></p>
<h1 id="h_e7f80560-91c0-420a-bccb-17bbf8c2e916">Kernels</h1>
<p>The following JupyterLab kernel are installed:</p>
<ul>
<li>Python3</li>
<li>R </li>
<li>Spark</li>
</ul>
<h2>R</h2>
<p>verify that the module IRkernel is loaded</p>
<pre><code>module load IRkernel</code></pre>
<h1 id="h_04f2f4e2-8e7a-486d-aea5-e020eb9df66e">Spark</h1>
<p>pySpark and SparkR is supported in NeSI Jupyter notebooks. Therefore, the module Spark needs to be loaded before starting Jupyter. Please run Spark workflows on compute nodes.</p>
<pre><code>module load Spark</code></pre>
<h1 id="h_04f2f4e2-8e7a-486d-aea5-e020eb9df66e">Packages</h1>
<p>There are a long list of default packages provided by the JupyterLab environment module (list all using <code>!pip list</code>) and R (list using <code>installed.packages(.Library)</code>, note the list is shortened). </p>
<p>Furthermore, you can install additional packages as described on the <a href="https://support.nesi.org.nz/hc/en-gb/articles/207782537" target="_self">Python</a> and <a href="https://support.nesi.org.nz/hc/en-gb/articles/209338087" target="_self">R</a> support page.</p>