---
created_at: '2019-11-11T21:32:46Z'
hidden: true
label_names: []
position: 15
title: Downloading CMIP6 data using globus
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001244856
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

This article targets researchers who need to download Climate Model
Intercomparison Project Phase 6 (CMIP6) datasets from any of the Earth
System Grid Federation ([ESGF](http://pcmdi.llnl.gov/)) archives. See
[synda](https://support.nesi.org.nz/hc/en-gb/articles/360001208256-SYNDA)
if you need to search any ESGF archive for a specific dataset. You can
also download data with "synda"; however, using globus will be many
times faster than over https. (It is also possible to build a synda
version from source which can handle globus data transfers, see
instructions
[here](http://prodiguer.github.io/synda/sdt/globustransfer.html).)

 

## Initial setup

To get started you will need:

1.  An account on one of the ESGF portals, e.g.
    [https://esgf-node.llnl.gov/projects/cmip6/](https://esgf-node.llnl.gov/projects/cmip6/)
2.  An Open ID string, e.g.
    <https://esgf-node.llnl.gov/esgf-idp/openid/pletzer>
3.  An account on globus.org. Write down your username.

You'll also need to install the globus cli tools. On mahuika:

    module load Python/2.7.16-gimkl-2018b && pip install globus-cli --user

 

## Choosing your dataset

First you will need to select some dataset by visiting the [CMIP6 search
interface](https://esgf-node.llnl.gov/search/cmip6/). You can keep most
default values. In this example we select only:

|               |                |
|---------------|----------------|
| Experiment ID | historical     |
| Frequency     | mon            |
| Realm         | ocean          |
| Variable      | tos            |
| Data Node     | aims3.llnl.gov |

 

Then press “Search”, which will list some datasets.  Feel free to add
any dataset to your Data cart,
eg **CMIP6.CMIP.CNRM-CERFACS.CNRM-CM6-1.historical.r1i1p1f2.Omon.tos.gr1.**
Adding to the cart will make it possible to download the data at a later
time. Next, for the dataset of your interest,

1.  Click on  \[ **Globus Download** \] 
2.  Click on Start Script Download
3.  Copy the script, globus\_download\_DATE\_TIME.py, over to mahuika

where DATE has the format YYYMMDD and TIME is a number, eg 134525. 

## Downloading the dataset

This involves several steps

### 1. Login to globus

On mahuika, 

    module load Python/2.7.16-gimkl-2018b

Next, you'll need to login to globus

    globus login

This will print an URL, something like

https://auth.globus.org/v2/oauth2/authorize?prompt=login&access\_type=offline&state=\_default&redirect\_uri=https%3A%2F%2Fauth.globus.org%2Fv2%2Fweb%2Fauth-code&response\_type=code&client\_id=aba933b6-848b-4032-8d47-f41d0d2796ce&scope=openid+profile+email+urn%3Aglobus%3Aauth%3Ascope%3Aauth.globus.org%3Aview\_identity\_set+urn%3Aglobus%3Aauth%3Ascope%3Atransfer.api.globus.org%3Aall

Point your web browser to the above URL (which will be different for
you).

There should be an image here but it couldn't be loaded.

 

Select Globus Id and say "Allow".

There should be an image here but it couldn't be loaded.

You will then get a code,

There should be an image here but it couldn't be loaded.

which you can paste into your terminal, eg

Enter the resulting Authorization Code, here:
4KGskqiZXHW36llJWUvDEUZArfQlNz

### 2. Find the endpoint UUID for NeSI

Globus connects different endpoints using a universally unique
identifier (UUID). This UUID can be retrieved from globus.org. For "NeSI
Wellington DTN" the UUID is:

### 3. Initiate the download

 
