---
created_at: '2020-06-08T04:21:37Z'
hidden: false
label_names:
- jupyter
- hub
- home
- lab
- notebook
position: 0
title: Jupyter on NeSI
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001555615
zendesk_section_id: 360001189255
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<blockquote class="blockquote-prereq">
<h3 id="prerequisites">Note</h3>
This service is available for users with a current allocation on Mahuika only.<br><a href="https://support.nesi.org.nz/hc/en-gb/requests/new" target="_blank" rel="noopener">Please contact us to request a suitable allocation.</a>
</blockquote>
<h1 id="h_01HAJKZVAGKVMQDJNQBGH4CWJJ">Introduction</h1>
<p>NeSI supports the use of <a href="https://jupyter.org/" target="_blank" rel="noopener">Jupyter</a> for <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001316356" target="_blank" rel="noopener">interactive computing</a>. Jupyter allows you to create notebooks that contain live code, equations, visualisations and explanatory text. There are many uses for Jupyter, including data cleaning, analytics and visualisation, machine learning, numerical simulation, managing <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000684396" target="_self">Slurm job submissions</a> and workflows and much more.</p>
<blockquote class="blockquote-tip">
<h3 id="llama-tip">See also</h3>
<ul>
<li>See the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360004337836" target="_blank" rel="noopener">RStudio via Jupyter on NeSI</a> page for launching an RStudio instance.</li>
<li>See the <a href="https://support.nesi.org.nz/hc/en-gb/articles/4614893064591" target="_blank" rel="noopener">MATLAB via Jupyter on NeSI</a> page for launching MATLAB via Jupyter</li>
<li>See the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001600235" target="_blank" rel="noopener">Virtual Desktop via Jupyter on NeSI</a> page for launching a virtual desktop via Jupyter.</li>
<li>See the <a href="https://support.nesi.org.nz/hc/en-gb/articles/4414958674831" target="_blank" rel="noopener">Jupyter kernels - Tool-assisted management</a> (recommended) and <a href="https://support.nesi.org.nz/hc/en-gb/articles/4414951820559" target="_blank" rel="noopener">Jupyter kernels - Manual management</a> pages for adding kernels.</li>
</ul>
</blockquote>
<h1 id="h_01HAJKZVAGYANF9V95MFYWEA55">Accessing Jupyter on NeSI</h1>
<p>Jupyter at NeSI is powered by <a style="background-color: #ffffff; font-size: 15px;" href="https://jupyter.org/hub" target="_blank" rel="noopener">JupyterHub</a><span style="font-size: 15px;">, a multi-user hub that spawns, manages and proxies multiple instances of the single-user Jupyter server.</span></p>
<h4 id="h_01HAJKZVAG4HN2H5GBF3ERBK8A">Access NeSI's JupyterHub here:</h4>
<p><a href="https://jupyter.nesi.org.nz" target="_blank" rel="noopener">https://jupyter.nesi.org.nz</a></p>
<p>When you log in with your <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000335995" target="_self">NeSI credentials</a> you will be taken to the "Server Options" page, where typical job configuration options can be selected to allocate the resources that will be used to run Jupyter. Typical jobs, not requesting a GPU, should be up and running within one to two minutes. Requesting a GPU can increase this time significantly as there are only a small number of GPUs available at NeSI.</p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tip</h3>
If your server appears to not have started within 3 minutes please reload the browser window and check again, otherwise contact <a href="mailto:support@nesi.org.nz?subject=Jupyter%20on%20NeSI" target="_blank" rel="noopener">support@nesi.org.nz</a>.</blockquote>
<h1 id="h_01HAJKZVAGEM741F5VPFDTJA6S">Known issues</h1>
<ul>
<li>When using <em>srun</em> in a Jupyter terminal you may see messages like those shown below. The "error" messages are actually just warnings and can be ignored; the <em>srun</em> command should still work. Alternatively, you could run <em>unset TMPDIR</em> in the terminal before running <em>srun</em> to avoid these warnings.
<pre>$ srun --pty bash<br>srun: job 28560743 queued and waiting for resources<br>srun: job 28560743 has been allocated resources<br>slurmstepd: error: Unable to create TMPDIR [/dev/shm/jobs/28560712]: Permission denied<br>slurmstepd: error: Setting TMPDIR to /tmp</pre>
</li>
</ul>
<h1 id="h_01HAJKZVAGZQBY0T8EV31TS8TK">Jupyter user interface</h1>
<h2 id="h_01HAJKZVAHP8QQ70ZGW2FYPV6V">JupyterLab</h2>
<p>Once your server has started you will be redirected to <a href="https://jupyterlab.readthedocs.io/en/stable/" target="_blank" rel="noopener">JupyterLab</a>. JupyterLab is the next generation of the Jupyter user interface and provides a way to use notebooks, text editor, terminals and custom components together. If you would prefer to use the classic Notebook interface, then select "Launch Classic Notebook" from the JupyterLab Help menu, or change the URL from <em>/lab</em> to <em>/tree</em> once the server is running.</p>
<h2 id="h_01HAJKZVAH43QY6P6M7JPA2C15">File systems</h2>
<p>Your Jupyter server will start in a new directory created within your home directory for that specific Jupyter job. Within that directory, you will find symbolic links to your home directory and to the project and nobackup directories of your active projects. We do not recommend that you store files in this initial directory because next time you launch Jupyter you will be starting in a different directory, instead switch to one of your home, project or nobackup directories first.</p>
<h2 id="jupyter-term">Jupyter terminal</h2>
<p>JupyterLab provides a terminal that can be an alternative means of gaining command line access to NeSI systems instead of using an SSH client. Some things to note are:</p>
<ul>
<li>when you launch the terminal application some environment modules are already loaded, so you may want to run <code>module purge</code> </li>
<li>processes launched directly in the JupyterLab terminal will probably be killed when you Jupyter session times out</li>
</ul>
<h1 id="h_01HAJKZVAHJWQ9AEJWTWD1ZJYE">Ending your interactive session and logging out</h1>
<p>To end a JupyterLab session, please select "Hub Control Panel" under the File menu then "Stop My Server". Finally, click on "Log Out".</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/6551812176911" width="208" height="394"> <img src="https://support.nesi.org.nz/hc/article_attachments/6551880407439" width="408" height="67"></p>
<p>If you click "Log Out" without stopping your server, the server will continue to run until the Slurm job reaches its maximum wall time.</p>
<p>This means that if you wish to have a session lasting, say, 4 hours (which is not offered in the "Select walltime" drop-down) then you can start a 8 hour session and end the job as described above when you are finished. Alternatively, you can cancel your Jupyter job by running <code>scancel 'job_id'</code> from within the Jupyter terminal when you are done. Note this will make the page unresponsive as it now has no compute powering it.</p>
<h1 id="h_01HAJKZVAH5STW963K76QCN03E">Installing JupyterLab extensions</h1>
<p>JupyterLab supports many extensions that enhance its functionality. At NeSI we package some extensions into the default JupyterLab environment. Keep reading if you need to install extensions yourself.</p>
<p>Note, there were some changes related to extensions in JupyterLab 3.0 and there are now multiple methods to install extensions. More details about JupyterLab extensions can be found <a href="https://jupyterlab.readthedocs.io/en/stable/user/extensions.html" target="_blank" rel="noopener">here</a>. Check the extension's documentation to find out the supported installation method for that particular extension.</p>
<h2 id="h_01HAJKZVAHHWDWXM4X5164JCWJ">Installing prebuilt extensions </h2>
<p>If the extension is packaged as a prebuilt extension (e.g. as a pip package), then you can install it from the JupyterLab terminal by running:</p>
<pre>$ pip install --user &lt;packagename&gt;</pre>
<p>For example, the <a href="https://github.com/dask/dask-labextension#jupyterlab-30-or-greater" target="_blank" rel="noopener">Dask extension</a> can be installed with the following:</p>
<pre>$ pip install --user dask-labextension</pre>
<h2 id="h_01HAJKZVAHP88ER3WC5HX66MJZ">Installing source extensions</h2>
<p>Installing source extensions requires a rebuild of the JupyterLab web application. Since this requires write permissions, you will need to set the JupyterLab <a href="https://jupyterlab.readthedocs.io/en/stable/user/extensions.html#advanced-usage" target="_blank" rel="noopener">application directory</a> to a location that you can write to. To do this you need to create a file named <em>~/.jupyterlab3_dir</em> in your home directory with the full path to your desired JupyterLab application directory and then run some commands to initialise the JupyterLab application directory.</p>
<p>Running the following commands will create the JupyterLab application directory in your home directory:</p>
<pre>$ module load JupyterLab<br>$ echo $HOME/.local/share/jupyter/lab &gt; ~/.jupyterlab3_dir<br>$ export JUPYTERLAB_DIR=$HOME/.local/share/jupyter/lab<br>$ jupyter lab build</pre>
<p>These changes will only take effect after relaunching your Jupyter server and then you should be able to install JupyterLab extensions as you please.</p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
The above commands will put the JupyterLab application directory in your home directory. The application directory often requires at least 1-2GB of disk space and 30,000 inodes (file count), so make sure you have space available in your home directory first (see <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000177256-NeSI-File-Systems-and-Quotas" target="_blank" rel="noopener">NeSI File Systems and Quotas</a>) or request a larger quota.</blockquote>
<p>You could change the path to point to a location in your project directory, especially if multiple people on your project will share the same JupyterLab application directory, e.g.:</p>
<pre>$ module load JupyterLab<br>$ echo /nesi/project/&lt;project_code&gt;/$USER/jupyter/lab &gt; ~/.jupyterlab_dir<br>$ export JUPYTERLAB_DIR=/nesi/project/&lt;project_code&gt;/$USER/jupyter/lab<br>$ jupyter lab build</pre>
<h1 id="h_01HAJKZVAHZCWFBRNEXR9RMWAK">Log files</h1>
<p>The log file of a Jupyter server session is saved either in the project directory of the project you selected on the "Server Options" JupyterHub page, or in your home directory, and is named <code>.jupyterhub_&lt;username&gt;_&lt;job_id&gt;.log</code> (note the leading <code>.</code> which means the log file is hidden). If you encounter problems with your Jupyter session, the contents of this file can be a good first clue to debug the issue.</p>
<h1 id="h_01HAJKZVAHM9Z7448R6SJ5ABXB">External documentation</h1>
<ul>
<li><a href="https://jupyter.readthedocs.io/en/latest/" target="_blank" rel="noopener">Jupyter</a></li>
<li><a href="https://jupyterhub.readthedocs.io/en/stable/" target="_blank" rel="noopener">JupyterHub</a></li>
<li><a href="https://jupyterlab.readthedocs.io/en/stable/" target="_blank" rel="noopener">JupyterLab</a></li>
</ul>