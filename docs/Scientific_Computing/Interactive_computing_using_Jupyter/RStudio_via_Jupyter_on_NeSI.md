---
created_at: '2021-05-13T01:00:08Z'
hidden: false
label_names: []
position: 1
title: RStudio via Jupyter on NeSI
vote_count: 7
vote_sum: 3
zendesk_article_id: 360004337836
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
<p>This functionality is experimental and may introduce breaking changes in the future. These notes should be read in conjunction with NeSI's main <a href="https://support.nesi.org.nz/hc/en-gb/articles/209338087-R">R support page</a></p>
<p>Your feedback is welcome, please don't hesitate to contact us at <a href="mailto:support@nesi.org.nz">support@nesi.org.nz</a> to make suggestions.</p>
</blockquote>
<h1 id="01GHF19KZ5P8Z4TZ8XQNNJFE6N">Getting started</h1>
<p>RStudio can be accessed as a web application via <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001555615" target="_blank" rel="noopener">Jupyter on NeSI</a>.</p>
<p>In the JupyterLab interface, RStudio can be started using the corresponding entry in the launcher.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/4595373978255" alt="rstudio_launcher.png"></p>
<p>Clicking on this entry will open a separate tab in your web browser, where RStudio will be accessible.</p>
<p>Once RStudio is launched, you should briefly see a login screen. It will be auto-filled using a pre-generated password, unless you disabled javascript in your web browser.</p>
<h1 id="01GHF19KZ5RECSM2QSH0ZD9R0B">Changing R version</h1>
<p>You can configure a set of <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001113076-The-HPC-environment-" target="_blank" rel="noopener">environment modules</a> to preload before starting RStudio. This can be useful if you want to change the version of the R interpreter or use NeSI's <em>R-Geo</em> or <em>R-bundle-Bioconductor</em> modules.</p>
<p>The module needs to be entered in the configuration file <code>~/.config/rstudio_on_nesi/prelude.bash</code>.</p>
<p>In the following example, we use the module that is built for R/4.2.1</p>
<pre><code>$ echo "module load R/4.2.1-gimkl-2022a" &gt; ~/.config/rstudio_on_nesi/prelude.bash</code><code></code></pre>
<p>Once your configuration file is ready, make sure to restart your Jupyter session and re-launch RStudio for these changes to be taken into account. Check that the correct version of R has loaded and that the correct Library Paths are available. For R/4.2.1 the command <code>.libPaths()</code> will return the following:</p>
<pre id="rstudio_console_output" class="GAQXDSOBH1B" tabindex="0" aria-label="Console Output"><span class="GAQXDSOBI1B" tabindex="-1"><span class="GAQXDSOBO1B ace_keyword">&gt; </span><span class="GAQXDSOBN0B ace_keyword">.libPaths()
</span><span class="GAQXDSOBH1B">[1] "/home/<em>YOUR_USER_NAME</em>/R/gimkl-2022a/4.2"                            
[2] "/opt/nesi/CS400_centos7_bdw/R/4.2.1-gimkl-2022a/lib64/R/library"</span></span></pre>
<h1 id="01GHF19KZ5RNM1XGE76EWS5PXM">Package Installation</h1>
<p>To avoid read/write issues with a small temorary directory filling up, in a terminal run the following two lines of code. These will setup a larger directory that will allow for packages to be installed to your personal library. NOTE: this is not creating a library.</p>
<div>
<pre><span>$ mkdir </span><span>-</span><span>p </span><span>/</span><span>nesi/nobackup</span><span>/&lt;projectID&gt;</span><span>/</span><span>rstudio_tmp</span><br><span>$ echo </span><span>"TMP=/nesi/nobackup/&lt;projectID&gt;/rstudio_tmp</span><span>" </span><span></span><span>&gt;</span><span> .Renviron</span></pre>
</div>
<p>Within RStudio run the command `tempdir()` which should return the following (below), where `Rtmpjp2rm8` is a randomly generated folder name, and is emptied with each new session. So will not fill up your home directory.</p>
<pre id="rstudio_console_output" class="GND-IWGDH3B" tabindex="0" aria-label="Console Output"><span class="GND-IWGDI3B" tabindex="-1"><span class="GND-IWGDH3B"><span class="GAQXDSOBI1B" tabindex="-1"><span class="GAQXDSOBH1B">&gt;tempdir()<br>[1] "<span>/</span><span>nesi/nobackup</span><span>/&lt;projectID&gt;</span><span>/</span><span>rstudio_tmp/</span></span></span>Rtmpjp2rm8"</span></span></pre>
<p>The alternative is to install packages in a terminal session</p>
<h1 id="01GHF19KZ5ZHD0XK9M0QSSKDFX">Advanced usage</h1>
<p>RStudio runs in a <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001107916" target="_blank" rel="noopener">Singularity container</a> prepared by the NeSI team to run on <a href="https://jupyter.nesi.org.nz" target="_blank" rel="noopener">jupyter.nesi.org.nz</a>. The related code is hosted on GitHub, in the <a href="https://github.com/nesi/rstudio_on_nesi" target="_blank" rel="noopener">rstudio_on_nesi</a> repository.</p>
<p>To modify the content of the container, you need to adapt the <a href="https://github.com/nesi/rstudio_on_nesi/blob/main/conf/rstudio_server_on_centos7.def" target="_blank" rel="noopener">Singularity definition file</a>, found in the <code>conf</code> folder of the repository, and then rebuild the container.</p>
<p>Once your container is ready, upload it on NeSI and use the configuration file <code>~/.config/rstudio_on_nesi/singularity_image_path</code> to indicate the path of your container to the RStudio-on-NeSI plugin:</p>
<pre><code>$ echo PATH_TO_CONTAINER &gt; ~/.config/rstudio_on_nesi/singularity_image_path</code></pre>
<p>Then restart your Jupyter session and launch a new RStudio session to make use of your container.</p>
<p>If your RStudio session does not start, try to reload the page, in case the reported failure is just due to the container taking too much time to start.</p>
<p>If this does not work, you will need to investigate the errors. A good place to start is looking at the log file from jupyter, for the current session:</p>
<pre><code>$ cat ~/.jupyter/.jupyterhub_${USER}_${SLURM_JOB_ID}.log</code></pre>
<h1 id="01GHF19KZ6ZA8ZNDQDNFB8PWWP">Troubleshooting</h1>
<p>If you get an error 500 after clicking on the launcher icon, this could be due to RStudio taking too much time to start, which is interpreted as a failure by JupyterLab. Please try to start RStudio again from the launcher. If the problem persists, contact our support team at <a href="mailto:support@nesi.org.nz">support@nesi.org.nz</a>.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/4614666941455" alt="error_500.PNG"></p>
<p>If you have disabled javascript in your web browser, you will need to enter your password manually in the RStudio login screen. To retrieve the password, open a terminal in JupyterLab and enter the following to print the password:</p>
<pre><code>$ cat ~/.config/rstudio_on_nesi/server_password</code></pre>
<p> </p>