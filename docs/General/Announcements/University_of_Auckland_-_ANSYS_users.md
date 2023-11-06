---
created_at: '2021-04-03T22:28:54Z'
hidden: false
label_names: []
position: 7
title: University of Auckland - ANSYS users
vote_count: 0
vote_sum: 0
zendesk_article_id: 360003984776
zendesk_section_id: 200732737
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>On 01/04/2021 afternoon, there was a change to the University ANSYS licences; you may find that your jobs fail with a licence error.</p>
<p>The following command should resolve the issue (where <code>-revn 202</code> is replaced with the version you use).</p>
<pre>module load ANSYS/2020R2<br>ansysli_util -revn 202 -deleteuserprefs</pre>
<p>The effect this will have on all of the ANSYS products is yet to be determined, so please open a <a href="mailto:support.nesi.org.nz" target="_self">support ticket</a> if you encounter problems.</p>