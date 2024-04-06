---
created_at: '2021-04-03T22:28:54Z'
tags: []
title: University of Auckland - ANSYS users
vote_count: 0
vote_sum: 0
zendesk_article_id: 360003984776
zendesk_section_id: 200732737
---


On 01/04/2021 afternoon, there was a change to the University ANSYS
licences; you may find that your jobs fail with a licence error.

The following command should resolve the issue (where `-revn 202` is
replaced with the version you use).

``` sl
module load ANSYS/2020R2
ansysli_util -revn 202 -deleteuserprefs
```

The effect this will have on all of the ANSYS products is yet to be
determined, so please open a [support
ticket](mailto:support.nesi.org.nz) if you encounter problems.
