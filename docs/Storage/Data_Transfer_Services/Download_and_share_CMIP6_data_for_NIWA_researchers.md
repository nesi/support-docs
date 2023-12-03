---
created_at: '2019-12-05T22:46:53Z'
hidden: false
position: 8
tags: []
title: Download and share CMIP6 data (for NIWA researchers)
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001287235
zendesk_section_id: 360000040596
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)



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
data will be downloaded asynchronously - no need to stare at a screen
for hours.  The downloaded data will reside in a shared directory and
hence will also be accessible to your collaborators.

The instructions are geared towards members of the niwa02916 group -
send a message to <support@nesi.org.nz> if you are a NIWA employee and
want to become part of this group. Other NeSI users may want to
read [this](../../Scientific_Computing/Supported_Applications/Synda),
which explains how to install the synda tool. Once installed, you can
then type similar commands to the ones below to test your configuration.

## Setup

On mahuika or w-mauivlab01.maui.nesi.org.nz:

``` sl
source /nesi/project/niwa02916/synda_env.sh
```

This will load the Anaconda3 environment and set the ST\_HOME variable.
You should also now be able to invoke
[synda](../../Scientific_Computing/Supported_Applications/Synda)
commands, a tool that can be used to synchronise CMIP data with Earth
System Grid Federation archives. A full list of options can be obtained
with

``` sl
synda -h
```

Below we demonstrate how synda might be used.

## Find some datasets 

CMIP6 datasets are organised by institution\_id, experiment\_id,
variable etc. A full list can be glanced
from <https://esgf-node.llnl.gov/search/cmip6/>. A possible search might
involve

``` sl
synda search institution_id=NCAR experiment_id=1pctCO2 variable=ta
```

which returns

new  CMIP6.CMIP.NCAR.CESM2-WACCM.1pctCO2.r1i1p1f1.day.ta.gn.v20190425

new  CMIP6.CMIP.NCAR.CESM2-WACCM.1pctCO2.r1i1p1f1.Amon.ta.gn.v20190425

...

as well as some other datasets. 

 

## Find out how big the datasets are

Once you know what you want to download, it's a good idea to check the
size of the dataset:

``` sl
synda stat CMIP6.CMIP.NCAR.CESM2-WACCM.1pctCO2.r1i1p1f1.day.ta.gn.v20190425
```

This prints "Total files count: 16, New files count: 16, Total size:
48.7 GB, New files size: 48.7 GB". The "New" indicates that the files
have not yet been downloaded. You can see that there are 16 files to
download, taking nearly 50GB of disk space.

## Download/install the dataset 

``` sl
synda install CMIP6.CMIP.NCAR.CESM2-WACCM.1pctCO2.r1i1p1f1.day.ta.gn.v20190425
```

The first time you may get a message requesting you to start a daemon,
if so do

``` sl
synda daemon start
```

This will put your request in a queue. The transfer will take place as a
background process so you can close your terminal if you want and come
back later to check progress.

The data will end up
under $ST\_HOME/data/CMIP6/CMIP/NCAR/CESM2-WACCM/1pctCO2/r1i1p1f1/day/ta/gn/v20190425
in this case. 

You can type

``` sl
synda queue
```

to see progress.

Note that if another researcher (or you) decide execute the same synda
install command then synda will recognise the files to be already
installed and will print the message

INFO: Nothing to install (matching files are already installed or
waiting in the download queue)