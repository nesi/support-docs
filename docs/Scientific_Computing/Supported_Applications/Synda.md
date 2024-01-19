---
created_at: '2019-10-14T21:25:00Z'
tags: []
title: Synda
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001208256
zendesk_section_id: 360000040076
---

## What is synda?

Synda is a command line tool to search and download files from the Earth
System Grid Federation ([ESGF](http://pcmdi.llnl.gov/)) archive. Synda
is a useful tool if you need to download Climate Model Intercomparison
Project Phase 6 (CMIP6) data in particular. Synda supports different
download protocols (e.g. HTTPS) and can download files in parallel.

We'll describe the steps to install and use synda on Mahuika or
Maui\_ancil.

## How to install synda

1\. Load Anaconda3

``` sh
module load Anaconda3
```

2\. Create a conda environment and activate the environment

``` sh
conda create --prefix=<SYNDA_ENV>
```

where &lt;SYNDA\_ENV&gt; is a directory of your choice. Activate your
new environment

``` sh
conda activate <SYNDA_ENV>
```

3\. Install synda (currently version 3.10)

``` sh
conda install -c IPSL synda
```

4\. Configure synda

Set the ST\_HOME environment variable and populate `$ST_HOME`, for
instance

``` sh
export ST_HOME=/nesi/nobackup/<YOUR PROJECT>/synda_home
```

Note: you may want to add the above "export ST\_HOME=&lt;...&gt;"
somewhere near the bottom of your ~/.bashrc file.

To search and download climate model data you will in addition need to
create an account on one or more of the ESGF nodes,
e.g. <https://esgf-node.llnl.gov/projects/esgf-llnl/>. This will require
you to provide a user name (USER\_NAME) and a password - you will
receive an openID in return. Copy your openID string as you will need
later.

To configure and store your ESGF credentials, type

``` sh
synda -h
synda check-env
```

Paste in the openID you received when creating your ESGF account. If you
created an account on esgf-node.llnl.gov then your openID will be:

``` sh
openID url: https://esgf-node.llnl.gov/esgf-idp/openid/USER_NAME
```

(USER\_NAME is the user name you chose when creating the account). You
can change your default configuration by editing
$ST\_HOME/conf/sdt.conf. I have

``` sh
indexes = esgf-node.llnl.gov
default_index = esgf-node.llnl.gov
```

## Example

Find all the datasets for given ocean surface temperature ("tos"),
variant label ("r1i1p1f1") produced by institution "NOAA-GFDL" for
historical data and table Id "Omon":

``` sh
synda search project=CMIP6 realm=ocean variable=tos variant_label=r1i1p1f1 institution_id=NOAA-GFDL table_id=Omon experiment_id=historical
```

This will return

``` sh
new  CMIP6.CMIP.NOAA-GFDL.GFDL-CM4.historical.r1i1p1f1.Omon.tos.gn.v20180701
new  CMIP6.CMIP.NOAA-GFDL.GFDL-CM4.historical.r1i1p1f1.Omon.tos.gr.v20180701
new  CMIP6.CMIP.NOAA-GFDL.GFDL-ESM4.historical.r1i1p1f1.Omon.tos.gn.v20190726
new  CMIP6.CMIP.NOAA-GFDL.GFDL-ESM4.historical.r1i1p1f1.Omon.tos.gr.v20190726
```

Choose one of the datasets. To find out how big the dataset is, type: 

``` sh
synda stat CMIP6.CMIP.NOAA-GFDL.GFDL-ESM4.historical.r1i1p1f1.Omon.tos.gr.v20190726
```

which returns

``` sh
Total files count: 9
New files count: 9
Total size: 262.8 MB
New files size: 262.8 MB
```

To download the dataset, type

``` sh
synda get CMIP6.CMIP.NOAA-GFDL.GFDL-CM4.historical.r1i1p1f1.Omon.tos.gn.v2018070
```

The datasets (NetCDF files) will be downloaded locally in your
directory.
