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

<table style="height: 149px;" width="471">
<tbody>
<tr class="odd">
<td style="width: 243px">Experiment ID</td>
<td style="width: 221px">historical</td>
</tr>
<tr class="even">
<td style="width: 243px">Frequency</td>
<td style="width: 221px">mon</td>
</tr>
<tr class="odd">
<td style="width: 243px">Realm</td>
<td style="width: 221px">ocean</td>
</tr>
<tr class="even">
<td style="width: 243px">Variable</td>
<td style="width: 221px">tos</td>
</tr>
<tr class="odd">
<td style="width: 243px">Data Node</td>
<td style="width: 221px"><span>aims3.llnl.gov</span></td>
</tr>
</tbody>
</table>

 

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

![globus1.png](../../assets/images/globus1_0.png)

 

Select Globus Id and say "Allow".

![globus2.png](../../assets/images/globus2_0.png)

You will then get a code,

![globus3.png](../../assets/images/globus3_0.png)

which you can paste into your terminal, eg

Enter the resulting Authorization Code, here:
4KGskqiZXHW36llJWUvDEUZArfQlNz

### 2. Find the endpoint UUID for NeSI

Globus connects different endpoints using a universally unique
identifier (UUID). This UUID can be retrieved from globus.org. For "NeSI
Wellington DTN" the UUID is:

3064bb28-e940-11e8-8caa-0a1d4c5c824a

 

### 3. Initiate the download

    python globus_download_20191111_134525.py -e 3064bb28-e940-11e8-8caa-0a1d4c5c824a -u pletzera

If the above fails then you will likely need to activate the globus
endpoint. If so then go to step 4 and repeat 3.

 

If successful, you should see something like

Message: The transfer has been accepted and a task has been created and
queued for execution

Task ID: ed4ce06c-04f6-11ea-be98-02fcc9cdd752

You can then check progress of the download by visiting globus.org and
clicking on "Activity". 

### 4. Activate the globus endpoint (may be required if 3 failed)

 This step is required if you got a message such as:

The endpoint could not be auto-activated and must be activated before it
can be used.

This endpoint supports the following activation methods: web, delegate
proxy, myproxy

 

'globus endpoint activate --myproxy
415a6320-e49c-11e5-9798-22000b9da45e'

 

The error message should give you the proxy string. 

    globus endpoint activate --myproxy 415a6320-e49c-11e5-9798-22000b9da45e

Enter your globus username and password:

    Myproxy username: pletzer 
    Myproxy password: 

###  

 

 
