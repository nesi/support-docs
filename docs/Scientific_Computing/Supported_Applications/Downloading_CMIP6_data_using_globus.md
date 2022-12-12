This article targets researchers who need to download Climate Model
Intercomparison Project Phase 6 (CMIP6) datasets from any of the Earth
System Grid Federation
(<a href="http://pcmdi.llnl.gov/" class="reference external">ESGF</a>)
archives. See
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

<table>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
</tr>
<tr class="even">
</tr>
<tr class="odd">
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

<span
class="s1">https://auth.globus.org/v2/oauth2/authorize?prompt=login&access\_type=offline&state=\_default&redirect\_uri=https%3A%2F%2Fauth.globus.org%2Fv2%2Fweb%2Fauth-code&response\_type=code&client\_id=aba933b6-848b-4032-8d47-f41d0d2796ce&scope=openid+profile+email+urn%3Aglobus%3Aauth%3Ascope%3Aauth.globus.org%3Aview\_identity\_set+urn%3Aglobus%3Aauth%3Ascope%3Atransfer.api.globus.org%3Aall</span>

<span class="s1">Point your web browser to the above URL (which will be
different for you). </span>

<span class="s1">![globus1.png](img/globus1.png)</span>

 

<span class="s1">Select Globus Id and say "Allow". </span>

<span class="s1">![globus2.png](img/globus2.png)</span>

<span class="s1">You will then get a code, </span>

<span class="s1">![globus3.png](img/globus3.png)</span>

<span class="s1">which you can paste into your terminal, eg</span>

<span class="s1">Enter the resulting Authorization Code, here:
4KGskqiZXHW36llJWUvDEUZArfQlNz</span>

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

<span class="s1">Message: The transfer has been accepted and a task has
been created and queued for execution</span>

<span class="s1">Task ID: ed4ce06c-04f6-11ea-be98-02fcc9cdd752</span>

You can then check progress of the download by visiting globus.org and
clicking on "Activity". 

### 4. Activate the globus endpoint (may be required if 3 failed)

 This step is required if you got a message such as:

<span class="s1">The endpoint could not be auto-activated and must be
activated before it can be used.</span>

<span class="s1">This endpoint supports the following activation
methods: web, delegate proxy, myproxy</span>

 

<span class="s1">'globus endpoint activate --myproxy
415a6320-e49c-11e5-9798-22000b9da45e'</span>

 

The error message should give you the proxy string. 

    globus endpoint activate --myproxy 415a6320-e49c-11e5-9798-22000b9da45e

Enter your globus username and password:

    Myproxy username: pletzer 
    Myproxy password: 

###  

 

 
