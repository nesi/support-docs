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
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p><span style="font-weight: 400;">This article targets researchers who need to download Climate Model Intercomparison Project Phase 6 (CMIP6) datasets from any of the Earth System Grid Federation (<a class="reference external" href="http://pcmdi.llnl.gov/">ESGF</a>) archives. See <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001208256-SYNDA" target="_self">synda</a> if you need to search any ESGF archive for a specific dataset. You can also download data with "synda"; however, using globus will be many times faster than over https. (It is also possible to build a synda version from source which can handle globus data transfers, see instructions <a href="http://prodiguer.github.io/synda/sdt/globustransfer.html" target="_self">here</a>.)</span></p>
<p> </p>
<h2><span style="font-weight: 400;">Initial setup</span></h2>
<p><span style="font-weight: 400;">To get started you will need:</span></p>
<ol>
<li style="font-weight: 400;">
<span style="font-weight: 400;">An account on one of the ESGF portals, e.g. </span><a href="https://esgf-node.llnl.gov/projects/cmip6/"><span style="font-weight: 400;">https://esgf-node.llnl.gov/projects/cmip6/</span></a>
</li>
<li style="font-weight: 400;">
<span style="font-weight: 400;">An Open ID string, e.g. </span><span style="font-weight: 400;"><a href="https://esgf-node.llnl.gov/esgf-idp/openid/pletzer">https://esgf-node.llnl.gov/esgf-idp/openid/pletzer</a></span>
</li>
<li><span style="font-weight: 400;">An account on globus.org. Write down your username.</span></li>
</ol>
<p>You'll also need to install the globus cli tools. On mahuika:</p>
<pre><span style="font-weight: 400;">module load Python/2.7.16-gimkl-2018b &amp;&amp; pip install globus-cli --user</span></pre>
<p> </p>
<h2>Choosing your dataset</h2>
<p>First you will need to select some dataset by visiting the <a href="https://esgf-node.llnl.gov/search/cmip6/" target="_self">CMIP6 search interface</a>. You can keep most default values. In this example we select only:</p>
<table style="height: 149px;" width="471">
<tbody>
<tr>
<td style="width: 243px;">Experiment ID</td>
<td style="width: 221px;">historical</td>
</tr>
<tr>
<td style="width: 243px;">Frequency</td>
<td style="width: 221px;">mon</td>
</tr>
<tr>
<td style="width: 243px;">Realm</td>
<td style="width: 221px;">ocean</td>
</tr>
<tr>
<td style="width: 243px;">Variable</td>
<td style="width: 221px;">tos</td>
</tr>
<tr>
<td style="width: 243px;">Data Node</td>
<td style="width: 221px;"><span style="font-weight: 400;">aims3.llnl.gov</span></td>
</tr>
</tbody>
</table>
<p> </p>
<p><span style="font-weight: 400;">Then press “Search”, which will list some datasets.  Feel free to add any dataset to your Data cart, eg <strong>CMIP6.CMIP.CNRM-CERFACS.CNRM-CM6-1.historical.r1i1p1f2.Omon.tos.gr1. </strong></span><span style="font-weight: 400;">Adding to the cart will make it possible to download the data at a later time. Next, for the dataset of your interest,</span></p>
<ol>
<li>
<span style="font-weight: 400;">Click on </span><span style="font-weight: 400;"> </span><span style="font-weight: 400;">[ </span><strong>Globus Download</strong><span style="font-weight: 400;"> ] </span>
</li>
<li><span style="font-weight: 400;">Click on Start Script Download</span></li>
<li><span style="font-weight: 400;">Copy the script, globus_download_DATE_TIME.py, over to mahuika</span></li>
</ol>
<p><span style="font-weight: 400;">where DATE has the format YYYMMDD and TIME is a number, eg 134525. </span></p>
<h2><span style="font-weight: 400;">Downloading the dataset</span></h2>
<p><span style="font-weight: 400;">This involves several steps</span></p>
<h3><span style="font-weight: 400;">1. Login to globus</span></h3>
<p><span style="font-weight: 400;">On mahuika, </span></p>
<pre><span style="font-weight: 400;">module load Python/2.7.16-gimkl-2018b<br></span></pre>
<p>Next, you'll need to login to globus</p>
<pre>globus login</pre>
<p>This will print an URL, something like</p>
<p class="p1"><span class="s1">https://auth.globus.org/v2/oauth2/authorize?prompt=login&amp;access_type=offline&amp;state=_default&amp;redirect_uri=https%3A%2F%2Fauth.globus.org%2Fv2%2Fweb%2Fauth-code&amp;response_type=code&amp;client_id=aba933b6-848b-4032-8d47-f41d0d2796ce&amp;scope=openid+profile+email+urn%3Aglobus%3Aauth%3Ascope%3Aauth.globus.org%3Aview_identity_set+urn%3Aglobus%3Aauth%3Ascope%3Atransfer.api.globus.org%3Aall</span></p>
<p class="p1"><span class="s1">Point your web browser to the above URL (which will be different for you). </span></p>
<p class="p1"><span class="s1"><img src="https://support.nesi.org.nz/hc/article_attachments/360002925856/globus1.png" alt="globus1.png"></span></p>
<p class="p1"> </p>
<p class="p1"><span class="s1">Select Globus Id and say "Allow". </span></p>
<p class="p1"><span class="s1"><img src="https://support.nesi.org.nz/hc/article_attachments/360002925876/globus2.png" alt="globus2.png"></span></p>
<p class="p1"><span class="s1">You will then get a code, </span></p>
<p class="p1"><span class="s1"><img src="https://support.nesi.org.nz/hc/article_attachments/360002925896/globus3.png" alt="globus3.png"></span></p>
<p class="p1"><span class="s1">which you can paste into your terminal, eg</span></p>
<p class="p1"><span class="s1">Enter the resulting Authorization Code, here: 4KGskqiZXHW36llJWUvDEUZArfQlNz</span></p>
<h3>2. Find the endpoint UUID for NeSI</h3>
<p><span style="font-weight: 400;">Globus connects different endpoints using a universally unique identifier (UUID). This UUID can be retrieved from globus.org. For "NeSI Wellington DTN" the UUID is:</span></p>
<div class="row">
<div class="col-md-6 mb-3 mb-md-2 col-lg-7 col-xl-8 d-flex align-items-center">3064bb28-e940-11e8-8caa-0a1d4c5c824a</div>
</div>
<div class="row"> </div>
<h3 class="row">3. Initiate the download</h3>
<div class="row">
<pre class="p1"><span class="s1">python globus_download_20191111_134525.py -e 3064bb28-e940-11e8-8caa-0a1d4c5c824a -u pletzera</span></pre>
</div>
<div class="row">If the above fails then you will likely need to activate the globus endpoint. If so then go to step 4 and repeat 3.</div>
<div class="row"> </div>
<div class="row">If successful, you should see something like</div>
<div class="row">
<div class="row">
<p class="p1"><span class="s1">Message: The transfer has been accepted and a task has been created and queued for execution</span></p>
<p class="p1"><span class="s1">Task ID: ed4ce06c-04f6-11ea-be98-02fcc9cdd752</span></p>
</div>
<p><span style="font-weight: 400;">You can then check progress of the download by visiting globus.org and clicking on "Activity". </span></p>
</div>
<div class="row">
<h3 class="row">4. Activate the globus endpoint (may be required if 3 failed)</h3>
<p> This step is required if you got a message such as:</p>
<p class="p1"><span class="s1">The endpoint could not be auto-activated and must be activated before it can be used.</span></p>
<p class="p1"><span class="s1">This endpoint supports the following activation methods: web, delegate proxy, myproxy</span></p>
<p class="p1"> </p>
<p class="p1"><span class="s1">'globus endpoint activate --myproxy 415a6320-e49c-11e5-9798-22000b9da45e'</span></p>
<p class="p1"> </p>
<p>The error message should give you the proxy string. </p>
<div class="row">
<pre class="p1"><span class="s1">globus endpoint activate --myproxy 415a6320-e49c-11e5-9798-22000b9da45e</span></pre>
</div>
<p class="row">Enter your globus username and password:</p>
<pre class="p1"><span class="s1">Myproxy username: pletzer </span><br><span class="s1">Myproxy password: </span></pre>
<h3 class="row"> </h3>
<p><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;"> </span></p>
</div>
<p> </p>