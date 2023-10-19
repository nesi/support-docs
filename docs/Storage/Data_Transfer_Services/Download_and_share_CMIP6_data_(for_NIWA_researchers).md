---
created_at: '2019-12-05T22:46:53Z'
hidden: false
label_names: []
position: 8
title: Download and share CMIP6 data (for NIWA researchers)
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001287235
zendesk_section_id: 360000040596
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<h2> </h2>
<p>The <a href="https://www.wcrp-climate.org/wgcm-cmip">Coupled Model Intercomparison Project</a>, which began in 1995 under the auspices of the <a href="https://www.wcrp-climate.org/about-wcrp/wcrp-overview">World Climate Research Programme (WCRP)</a>, is now in its sixth phase (CMIP6). CMIP6 orchestrates somewhat independent model intercomparison activities and their experiments, which have adopted a common infrastructure for collecting, organising, and distributing output from models performing common sets of experiments.</p>
<p>This document shows how to explore which CMIP6 data are available and how to download the data once you have figured out what you need. The data will be downloaded asynchronously<span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> - no need to st</span><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">are at a screen for hours.  The downloaded data will reside in a shared directory and hence will also be accessible to your collaborators.</span></p>
<p>The instructions are geared towards members of the niwa02916 group - send a message to <a href="mailto:support@nesi.org.nz">support@nesi.org.nz</a> if you are a NIWA employee and want to become part of this group. Other NeSI users may want to read <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001208256-Synda" target="_self" rel="undefined">this</a>, which explains how to install the synda tool. Once installed, you can then type similar commands to the ones below to test your configuration.</p>
<h2>Setup</h2>
<p>On mahuika or <span class="s1">w-mauivlab01.maui.nesi.org.nz</span>:</p>
<pre class="p1"><span class="s1">source /nesi/project/niwa02916/synda_env.sh</span></pre>
<p>This will load the Anaconda3 environment and set the ST_HOME variable. You should also now be able to invoke <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001208256-Synda" target="_self">synda</a> commands, a tool that can be used to synchronise CMIP data with Earth System Grid Federation archives. A full list of options can be obtained with</p>
<pre>synda -h</pre>
<p>Below we demonstrate how synda might be used.</p>
<h2>Find some datasets </h2>
<p>CMIP6 datasets are organised by institution_id, experiment_id, variable etc. A full list can be glanced from <a href="https://esgf-node.llnl.gov/search/cmip6/">https://esgf-node.llnl.gov/search/cmip6/</a>. A possible search might involve</p>
<pre class="p1"><span class="s1">synda search institution_id=NCAR experiment_id=1pctCO2 variable=ta</span></pre>
<p class="p1"><span class="s1">which returns</span></p>
<p class="p1"><span class="s1">new<span class="Apple-converted-space">  </span>CMIP6.CMIP.NCAR.CESM2-WACCM.1pctCO2.r1i1p1f1.day.ta.gn.v20190425</span></p>
<p class="p1"><span class="s1">new<span class="Apple-converted-space">  </span>CMIP6.CMIP.NCAR.CESM2-WACCM.1pctCO2.r1i1p1f1.Amon.ta.gn.v20190425</span></p>
<p class="p1"><span class="s1">...</span></p>
<p class="p1"><span class="s1">as well as some other datasets. </span></p>
<p> </p>
<h2>Find out how big the datasets are</h2>
<p>Once you know what you want to download, it's a good idea to check the size of the dataset:</p>
<pre>synda stat <span class="s1">CMIP6.CMIP.NCAR.CESM2-WACCM.1pctCO2.r1i1p1f1.day.ta.gn.v20190425</span></pre>
<p>This prints "<span class="s1">Total files count: 16, </span><span class="s1">New files count: 16, </span><span class="s1">Total size: 48.7 GB, </span><span class="s1">New files size: 48.7 GB". The "New" indicates that the files have not yet been downloaded. You can see that there are 16 files to download, taking nearly 50GB of disk space.</span></p>
<h2>Download/install the dataset </h2>
<pre>synda install <span class="s1">CMIP6.CMIP.NCAR.CESM2-WACCM.1pctCO2.r1i1p1f1.day.ta.gn.v20190425</span></pre>
<p>The first time you may get a message requesting you to start a daemon, if so do</p>
<pre>synda daemon start</pre>
<p>This will put your request in a queue. The transfer will take place as a background process so you can close your terminal if you want and come back later to check progress.</p>
<p>The data will end up under <span class="s1">$ST_HOME/data/CMIP6/CMIP/NCAR/CESM2-WACCM/1pctCO2/r1i1p1f1/day/ta/gn/v20190425 in this case. </span></p>
<p>You can type</p>
<pre>synda queue</pre>
<p>to see progress.</p>
<p>Note that if another researcher (or you) decide execute the same synda install command then synda will recognise the files to be already installed and will print the message</p>
<p class="p1"><span class="s1">INFO: Nothing to install (matching files are already installed or waiting in the download queue)</span></p>