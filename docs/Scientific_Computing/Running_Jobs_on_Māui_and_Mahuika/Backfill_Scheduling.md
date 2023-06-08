---
created_at: '2017-12-06T04:48:11Z'
hidden: true
label_names:
- mahuika
position: 15
title: Backfill Scheduling
vote_count: 0
vote_sum: 0
zendesk_article_id: 115001826590
zendesk_section_id: 360000030876
---

 

Backfill is a scheduling strategy that allows small, short jobs to run
immediately if by doing so they will not delay the expected start time
of any higher-priority jobs. Since the expected star time of pending
jobs depends upon the expected completion time of running jobs, for
backfill to work well, it is important that users set reasonably
accurate job time limits 

While the kinds of jobs that can be backfilled will also get a low job
size score, it is our general experience that an ability to be
backfilled is on the whole more useful when it comes to getting work
done on the HPCs.

More information about backfill can be found
[here](https://slurm.schedmd.com/sched_config.html).
