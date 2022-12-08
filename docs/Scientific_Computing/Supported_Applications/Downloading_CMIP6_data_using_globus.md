[This article targets researchers who need to download Climate Model
Intercomparison Project Phase 6 (CMIP6) datasets from any of the Earth
System Grid Federation ([ESGF](http://pcmdi.llnl.gov/){.reference
.external}) archives. See
[synda](https://support.nesi.org.nz/hc/en-gb/articles/360001208256-SYNDA)
if you need to search any ESGF archive for a specific dataset. You can
also download data with \"synda\"; however, using globus will be many
times faster than over https. (It is also possible to build a synda
version from source which can handle globus data transfers, see
instructions
[here](http://prodiguer.github.io/synda/sdt/globustransfer.html).)]{style="font-weight: 400;"}

 

## [Initial setup]{style="font-weight: 400;"}

[To get started you will need:]{style="font-weight: 400;"}

1.  [An account on one of the ESGF portals, e.g.
    ]{style="font-weight: 400;"}[[https://esgf-node.llnl.gov/projects/cmip6/]{style="font-weight: 400;"}](https://esgf-node.llnl.gov/projects/cmip6/)
2.  [An Open ID string, e.g.
    ]{style="font-weight: 400;"}[<https://esgf-node.llnl.gov/esgf-idp/openid/pletzer>]{style="font-weight: 400;"}
3.  [An account on globus.org. Write down your
    username.]{style="font-weight: 400;"}

You\'ll also need to install the globus cli tools. On mahuika:

    module load Python/2.7.16-gimkl-2018b && pip install globus-cli --user

 

## Choosing your dataset

First you will need to select some dataset by visiting the [CMIP6 search
interface](https://esgf-node.llnl.gov/search/cmip6/). You can keep most
default values. In this example we select only:

  --------------- ---------------------------------------------
  Experiment ID   historical
  Frequency       mon
  Realm           ocean
  Variable        tos
  Data Node       [aims3.llnl.gov]{style="font-weight: 400;"}
  --------------- ---------------------------------------------

 

[Then press "Search", which will list some datasets.  Feel free to add
any dataset to your Data cart,
eg **CMIP6.CMIP.CNRM-CERFACS.CNRM-CM6-1.historical.r1i1p1f2.Omon.tos.gr1.**
]{style="font-weight: 400;"}[Adding to the cart will make it possible to
download the data at a later time. Next, for the dataset of your
interest,]{style="font-weight: 400;"}

1.  [Click on
    ]{style="font-weight: 400;"}[ ]{style="font-weight: 400;"}[\[
    ]{style="font-weight: 400;"}**Globus Download**[
    \] ]{style="font-weight: 400;"}
2.  [Click on Start Script Download]{style="font-weight: 400;"}
3.  [Copy the script, globus\_download\_DATE\_TIME.py, over to
    mahuika]{style="font-weight: 400;"}

[where DATE has the format YYYMMDD and TIME is a number, eg
134525. ]{style="font-weight: 400;"}

## [Downloading the dataset]{style="font-weight: 400;"}

[This involves several steps]{style="font-weight: 400;"}

### [1. Login to globus]{style="font-weight: 400;"}

[On mahuika, ]{style="font-weight: 400;"}

    module load Python/2.7.16-gimkl-2018b

Next, you\'ll need to login to globus

    globus login

This will print an URL, something like

[https://auth.globus.org/v2/oauth2/authorize?prompt=login&access\_type=offline&state=\_default&redirect\_uri=https%3A%2F%2Fauth.globus.org%2Fv2%2Fweb%2Fauth-code&response\_type=code&client\_id=aba933b6-848b-4032-8d47-f41d0d2796ce&scope=openid+profile+email+urn%3Aglobus%3Aauth%3Ascope%3Aauth.globus.org%3Aview\_identity\_set+urn%3Aglobus%3Aauth%3Ascope%3Atransfer.api.globus.org%3Aall]{.s1}

[Point your web browser to the above URL (which will be different for
you). ]{.s1}

[![globus1.png](https://support.nesi.org.nz/hc/article_attachments/360002925856/globus1.png)]{.s1}

 

[Select Globus Id and say \"Allow\". ]{.s1}

[![globus2.png](https://support.nesi.org.nz/hc/article_attachments/360002925876/globus2.png)]{.s1}

[You will then get a code, ]{.s1}

[![globus3.png](https://support.nesi.org.nz/hc/article_attachments/360002925896/globus3.png)]{.s1}

[which you can paste into your terminal, eg]{.s1}

[Enter the resulting Authorization Code, here:
4KGskqiZXHW36llJWUvDEUZArfQlNz]{.s1}

### 2. Find the endpoint UUID for NeSI

[Globus connects different endpoints using a universally unique
identifier (UUID). This UUID can be retrieved from globus.org. For
\"NeSI Wellington DTN\" the UUID is:]{style="font-weight: 400;"}

::: {.row}
::: {.col-md-6 .mb-3 .mb-md-2 .col-lg-7 .col-xl-8 .d-flex .align-items-center}
3064bb28-e940-11e8-8caa-0a1d4c5c824a
:::
:::

::: {.row}
 
:::

### 3. Initiate the download {#initiate-the-download .row}

::: {.row}
    python globus_download_20191111_134525.py -e 3064bb28-e940-11e8-8caa-0a1d4c5c824a -u pletzera
:::

::: {.row}
If the above fails then you will likely need to activate the globus
endpoint. If so then go to step 4 and repeat 3.
:::

::: {.row}
 
:::

::: {.row}
If successful, you should see something like
:::

::: {.row}
::: {.row}
[Message: The transfer has been accepted and a task has been created and
queued for execution]{.s1}

[Task ID: ed4ce06c-04f6-11ea-be98-02fcc9cdd752]{.s1}
:::

[You can then check progress of the download by visiting globus.org and
clicking on \"Activity\". ]{style="font-weight: 400;"}
:::

::: {.row}
### 4. Activate the globus endpoint (may be required if 3 failed) {#activate-the-globus-endpoint-may-be-required-if-3-failed .row}

 This step is required if you got a message such as:

[The endpoint could not be auto-activated and must be activated before
it can be used.]{.s1}

[This endpoint supports the following activation methods: web, delegate
proxy, myproxy]{.s1}

 

[\'globus endpoint activate \--myproxy
415a6320-e49c-11e5-9798-22000b9da45e\']{.s1}

 

The error message should give you the proxy string. 

::: {.row}
    globus endpoint activate --myproxy 415a6320-e49c-11e5-9798-22000b9da45e
:::

Enter your globus username and password:

    Myproxy username: pletzer 
    Myproxy password: 

###   {#section .row}

[ ]{style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"}
:::

 
