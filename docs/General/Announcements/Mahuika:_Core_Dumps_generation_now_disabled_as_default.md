---
created_at: '2022-07-11T23:23:04Z'
hidden: false
label_names:
- mahuika
- .core
- corefile
- coredump
position: 0
status: new
title: 'Mahuika: Core Dumps generation now disabled as default'
vote_count: 0
vote_sum: 0
zendesk_article_id: 5126681349903
zendesk_section_id: 200732737
---

A Slurm configuration change has been made on Mahuika so that the 
maximum size
of <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001584875-What-is-a-core-file-" class="c-link">core file</a> that
can be generated inside a job now defaults to `0` bytes rather
than `unlimited`. 

You can reenable core dumps with `ulimit -c unlimited` .
