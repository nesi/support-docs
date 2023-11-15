---
created_at: '2022-07-11T23:23:04Z'
hidden: false
position: 0
status: new
tags:
- mahuika
- .core
- corefile
- coredump
title: 'Mahuika: Core Dumps generation now disabled as default'
vote_count: 0
vote_sum: 0
zendesk_article_id: 5126681349903
zendesk_section_id: 200732737
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

A Slurm configuration change has been made on Mahuika so that the 
maximum size of [core
file](https://support.nesi.org.nz/hc/en-gb/articles/360001584875-What-is-a-core-file-) that
can be generated inside a job now defaults to `0` bytes rather
than `unlimited`. 

You can reenable core dumps with `ulimit -c unlimited` .
