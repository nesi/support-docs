---
created_at: '2022-07-11T23:23:04Z'
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
search:
  boost: 0.1
---

A Slurm configuration change has been made on Mahuika so that the 
maximum size of [core file](../FAQs/What_is_a_core_file.md) that
can be generated inside a job now defaults to `0` bytes rather
than `unlimited`.

You can reenable core dumps with `ulimit -c unlimited` .
