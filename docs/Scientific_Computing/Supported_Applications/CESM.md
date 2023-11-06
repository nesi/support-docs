---
created_at: '2020-11-02T03:07:06Z'
hidden: false
label_names: []
position: 10
title: CESM
vote_count: 0
vote_sum: 0
zendesk_article_id: 360002105076
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<h1>CESM</h1>
<p><span>The Community Earth System Model (CESM) is a coupled climate model for simulating Earth’s climate system. Composed of separate models simultaneously simulating the Earth’s atmosphere, ocean, land, river run-off, land-ice, and sea-ice, plus one central coupler/moderator component, CESM allows researchers to conduct fundamental research into the Earth’s past, present, and future climate states.</span></p>
<h1><span>Building CESM2 on Maui</span></h1>
<p><span>Here we provide a guide for downloading, building and running a CESM test case yourself on Maui. This guide is based on CESM 2.1.</span></p>
<h2><span>Prerequisites</span></h2>
<p><span>Git Large File Storage seems to be required to download some of the CESM components. Download the Git-LFS archive from <a href="https://git-lfs.github.com/" target="_blank" rel="noopener">here</a>, copy the <em>git-lfs</em> executable to the <em>bin</em> directory in your home, add that directory to <em>PATH</em> and run a git command to finish the Git-LFS installation. The following commands will achieve this:</span></p>
<pre><span>mkdir git-lfs<br>cd git-lfs<br>wget https://github.com/git-lfs/git-lfs/releases/download/v2.12.0/git-lfs-linux-amd64-v2.12.0.tar.gz<br>tar xf git-lfs-linux-amd64-v2.12.0.tar.gz<br>mkdir -p ~/bin<br>cp git-lfs ~/bin/<br>export PATH=$PATH:~/bin<br>echo export PATH=\$PATH:\$HOME/bin &gt;&gt; ~/.bashrc<br>git lfs install</span></pre>
<h2><span>Download CESM</span></h2>
<p>These instructions are based on the <a href="https://escomp.github.io/CESM/release-cesm2/downloading_cesm.html" target="_blank" rel="noopener">upstream documentation</a>. First switch to your project directory (or wherever else you would like the CESM source to live) and then run the commands to download CESM (replacing <em>&lt;your_project_code&gt;</em> with your project code):</p>
<pre><span class="go">cd /nesi/project/&lt;your_project_code&gt;<br>git clone -b release-cesm2.1.3 https://github.com/ESCOMP/CESM.git my_cesm_sandbox</span>
<span class="go">cd my_cesm_sandbox<br>./manage_externals/checkout_externals<br></span></pre>
<p><span>Make sure the above command is successful (see the upstream documentation linked above for how to check). You may need to rerun the command until it is successful, especially if it asks you to accept a certificate.</span></p>
<h2><span>NeSI specific CIME configuration</span></h2>
<p>Clone the repo containing NeSI specific CIME configuration (<a href="http://esmci.github.io/cime/versions/master/html/what_cime/index.html" target="_blank" rel="noopener">CIME</a> provides a case control system for configuring, building and executing Earth system models) and copy the config files to <em>~/.cime</em>. In the following, replace <em>&lt;your_project_code&gt;</em> with your project code (this will overwrite any current configuration your have in <em>~/.cime</em>):</p>
<pre>cd /nesi/project/&lt;your_project_code&gt;<br>git clone https://github.com/nesi/nesi-cesm-config.git<br>cd nesi-cesm-config<br>mkdir -p ~/.cime<br>sed <span class="pl-s"><span class="pl-pds">'</span>s/nesi99999/&lt;your_project_code&gt;/g<span class="pl-pds">'</span></span> config_machines.xml <span class="pl-k">&gt;</span> <span class="pl-k">~</span>/.cime/config_machines.xml<br>cp config_batch.xml <span class="pl-k">~</span>/.cime/config_batch.xml</pre>
<p>Check that you are happy with the paths specified in <em>~/.cime/config_machines.xml</em>, in particular, it is recommended that CESM users share the same input data locations as the input data can be large.</p>
<h2><span>Setting up and running a test case</span></h2>
<p>Here we will run the test described in the CESM <a href="https://escomp.github.io/CESM/release-cesm2/quickstart.html" target="_blank" rel="noopener">quick start guide</a>. The following are basic instructions to run create and run the case, see the above link for more information.</p>
<p>First, create the case:</p>
<pre>cd /nesi/project/&lt;your_project_code&gt;/my_cesm_sandbox/cime/scripts<br>./create_newcase --case /nesi/nobackup/&lt;your_project_code&gt;/$USER/cesm/output/b.e20.B1850.f19_g17.test --compset B1850 --res f19_g17 --machine maui --compiler intel<br>cd /nesi/nobackup/&lt;your_project_code&gt;/$USER/cesm/output/b.e20.B1850.f19_g17.test</pre>
<p><span>The <em>--machine maui --compiler intel</em> arguments to <em>./create_case</em> tell CESM to use the NeSI specific configuration we added to your home directory in the previous step.</span></p>
<p><span>Next, set up the case and preview the run:</span></p>
<pre><span>./case.setup<br>./preview_run</span></pre>
<p><span>Check that everything looks correct in the preview and then build the case:</span></p>
<pre><span>./case.build</span></pre>
<p><span>Update any settings if necessary, for example here we turn off short term archiving:</span></p>
<pre><span class="go">./xmlchange DOUT_S=FALSE</span><span></span></pre>
<p><span>Finally, run the job:</span></p>
<pre><span>./case.submit</span></pre>
<p><span>A job will be submitted to the Slurm queue, you can view the queue using <em>squeue</em> or <em>squeue -u $USER</em> for just your own jobs. Check the job succeeded as described on the upstream quick start guide.</span></p>
<h1><span>Performance tuning - optimising processor layout</span></h1>
<p><span>With CESM it can be important to tune the processor layout for best performance with respect to the different components (atmosphere, land, sea ice, etc.). Many different configurations are possible, although there are some hard coded constraints, and this is well documented in CIME (the case control system used by CESM):</span></p>
<p><a href="https://esmci.github.io/cime/versions/maint-5.6/html/users_guide/pes-threads.html" target="_blank" rel="noopener"><span>https://esmci.github.io/cime/versions/maint-5.6/html/users_guide/pes-threads.html</span></a></p>
<p><span>The above link lists some of the common configurations, such as fully sequential or fully sequential except the ocean running concurrently.</span></p>
<p>One approach to load balancing (i.e. optimising processor layout) is documented on the above page in the section "One approach to load balancing" <a href="https://esmci.github.io/cime/versions/maint-5.6/html/users_guide/pes-threads.html" target="_blank" rel="noopener">here</a>. It involves performing a number of short model runs to determine which components are most expensive and how the individual components scale. That information can then be used to determine an optimal load balance.</p>
<p> </p>