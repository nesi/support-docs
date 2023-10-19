---
created_at: '2021-03-01T21:23:33Z'
hidden: false
label_names: []
position: 0
title: Logging in to my.nesi.org.nz
vote_count: 2
vote_sum: -2
zendesk_article_id: 360003584515
zendesk_section_id: 360001059296
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<h2 id="01F4GDKWCS77EHT9R115HFJC28"><span>Login credentials</span></h2>
<p><span>We allow students, academics, alumni and researchers to securely login and create a <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000159715" target="_blank" rel="noopener">NeSI account profile</a> using the credentials granted by their home organisation via Tuakiri.</span></p>
<h3 id="01F4GDKWCSKP2KFCJ51R49TCR6"><span>Tuakiri - federated identity and access management</span></h3>
<p><span>Most New Zealand universities and Crown Research Institutes are members of the </span><a href="https://www.reannz.co.nz/products-and-services/tuakiri/join/" target="_blank" rel="noopener">Tuakiri authentication federation</a><span>, but many other institutions, including private sector organisations and most central and local government agencies, are not. </span></p>
<p><span>See also <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000159715" target="_blank" rel="noopener">Creating a NeSI Account Profile</a></span></p>
<h3 id="01F4GDKWCS6WMDYNVKEYXWHKR6"><span>Support for users outside the Tuakiri federation</span></h3>
<p>In case your organisation is not part of the Tuakiri federated identity management service, a user can still <a class="btn-link" href="https://my.nesi.org.nz/html/request_nesi_account">request a NeSI Account profile.</a> NeSI will (if approved) provision a so-called "virtual home account" on Tuakiri. </p>
<p>See also <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000216035" target="_blank" rel="noopener">Account Requests for non-Tuakiri Members</a></p>
<h2 id="01F4GDN6XE5RWF610MZKG77EAS">Troubleshooting login issues</h2>
<p>Please use the <strong><a href="https://attributes.tuakiri.ac.nz/snapshots/latest">Tuakiri Attribute Validator</a> </strong>to verify the details of your account. Contact your identity provider (e.g. institution, university) in case there are details missing or wrong.</p>
<h3 id="01F4GDTS6RTDR30872X1FXFJDB">Tuakiri Attribute Validator</h3><p id="01F4GDTS6RM420P1H7P6NTP3TF">This Tuakiri service is a health check for your managed identity. It checks the attributes provided about you from your identity provider, seeing whether they are provided in a format that is suitable for consumption by Tuakiri connected services. It will report any problems that it finds with your identity record, so that you can talk with the IT department at your identity provider (normally your employer or university) and have the problems fixed.</p><p id="01F4H07V6S3Y55NV4KKV9MTEFV">Generally speaking, errors in your Tuakiri Core Attributes, such as empty values, will probably cause problems for you when you try to log in to a service using Tuakiri; while errors in your Tuakiri Optional Attributes are mostly harmless, and not worth bothering your IT department about unless you need a particular Optional Attribute to be correctly set for a specific purpose.</p><p id="01F4H0G40215NZM17GP66879W6">To access the Tuakiri Attribute Validator, browse to this page: <a id="01F4GZHYGZG2HPMGKX8DZFBGMB" href="https://attributes.tuakiri.ac.nz/snapshots/latest">https://attributes.tuakiri.ac.nz/snapshots/latest﻿</a></p><p id="01F4GDTS6RWV8VC1R2HFMR8GA2">The primary identifier NeSI consumes is the attribute <strong>auEduPersonSharedToken</strong>. This is a so-called, "Tuakiri Core Attribute," expected to exist for every account.</p><p id="01F4GZMEH0R8X6D9A91DTYK1DP">If your institution has issued you an empty or invalid auEduPersonSharedToken (rare), or if there is a difference between the value of your auEduPersonSharedToken as proffered by your institution's identity provision service and its value as recorded in the NeSI database (more common), you will not be able to log in to My NeSI. If you cannot log in, please raise a support ticket with your institutions IT support. <br>For troubleshooting the support team may ask you for a PDF of your Tuakiri attributes. Tuakiri does not include your password in the attribute printout and there is no security risk involved in providing a copy of that PDF.</p>