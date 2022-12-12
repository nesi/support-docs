##  

The [Coupled Model Intercomparison
Project](https://www.wcrp-climate.org/wgcm-cmip), which began in 1995
under the auspices of the [World Climate Research Programme
(WCRP)](https://www.wcrp-climate.org/about-wcrp/wcrp-overview), is now
in its sixth phase (CMIP6). CMIP6 orchestrates somewhat independent
model intercomparison activities and their experiments, which have
adopted a common infrastructure for collecting, organising, and
distributing output from models performing common sets of experiments.

This document shows how to explore which CMIP6 data are available and
how to download the data once you have figured out what you need. The
data will be downloaded asynchronously<span
style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> -
no need to st</span><span
style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">are
at a screen for hours.  The downloaded data will reside in a shared
directory and hence will also be accessible to your
collaborators.</span>

The instructions are geared towards members of the niwa02916 group -
send a message to <support@nesi.org.nz> if you are a NIWA employee and
want to become part of this group. Other NeSI users may want to
read [this](https://support.nesi.org.nz/hc/en-gb/articles/360001208256-Synda),
which explains how to install the synda tool. Once installed, you can
then type similar commands to the ones below to test your configuration.

## Setup

On mahuika or <span class="s1">w-mauivlab01.maui.nesi.org.nz</span>:

    source /nesi/project/niwa02916/synda_env.sh

This will load the Anaconda3 environment and set the ST\_HOME variable.
You should also now be able to invoke
[synda](https://support.nesi.org.nz/hc/en-gb/articles/360001208256-Synda)
commands, a tool that can be used to synchronise CMIP data with Earth
System Grid Federation archives. A full list of options can be obtained
with

    synda -h

Below we demonstrate how synda might be used.

## Find some datasets 

CMIP6 datasets are organised by institution\_id, experiment\_id,
variable etc. A full list can be glanced
from <https://esgf-node.llnl.gov/search/cmip6/>. A possible search might
involve

    synda search institution_id=NCAR experiment_id=1pctCO2 variable=ta

<span class="s1">which returns</span>

<span class="s1">new<span class="Apple-converted-space"> 
</span>CMIP6.CMIP.NCAR.CESM2-WACCM.1pctCO2.r1i1p1f1.day.ta.gn.v20190425</span>

<span class="s1">new<span class="Apple-converted-space"> 
</span>CMIP6.CMIP.NCAR.CESM2-WACCM.1pctCO2.r1i1p1f1.Amon.ta.gn.v20190425</span>

<span class="s1">...</span>

<span class="s1">as well as some other datasets. </span>

 

## Find out how big the datasets are

Once you know what you want to download, it's a good idea to check the
size of the dataset:

    synda stat CMIP6.CMIP.NCAR.CESM2-WACCM.1pctCO2.r1i1p1f1.day.ta.gn.v20190425

This prints "<span class="s1">Total files count: 16, </span><span
class="s1">New files count: 16, </span><span class="s1">Total size: 48.7
GB, </span><span class="s1">New files size: 48.7 GB". The "New"
indicates that the files have not yet been downloaded. You can see that
there are 16 files to download, taking nearly 50GB of disk space.</span>

## Download/install the dataset 

    synda install CMIP6.CMIP.NCAR.CESM2-WACCM.1pctCO2.r1i1p1f1.day.ta.gn.v20190425

The first time you may get a message requesting you to start a daemon,
if so do

    synda daemon start

This will put your request in a queue. The transfer will take place as a
background process so you can close your terminal if you want and come
back later to check progress.

The data will end up under <span
class="s1">$ST\_HOME/data/CMIP6/CMIP/NCAR/CESM2-WACCM/1pctCO2/r1i1p1f1/day/ta/gn/v20190425
in this case. </span>

You can type

    synda queue

to see progress.

Note that if another researcher (or you) decide execute the same synda
install command then synda will recognise the files to be already
installed and will print the message

<span class="s1">INFO: Nothing to install (matching files are already
installed or waiting in the download queue)</span>
