---
created_at: '2021-05-03T00:36:34Z'
hidden: true
label_names: []
position: 0
title: When does CPU efficiency matter more than speed?
vote_count: 0
vote_sum: 0
zendesk_article_id: 360004351115
zendesk_section_id: 360000039036
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
Often when running an [embarrassingly parallel
problem](https://support.nesi.org.nz/hc/en-gb/articles/360000690275), or
just lots of jobs at once, the limiting factor on your throughput (work
you can get done over a set period of time) will likely be the SLURM
queue rather than the jobs execution time. 

If this is the case, you will get more work done by optimising for
efficiency rather than speed, and running on a single CPU is almost
always more efficient than any form of parallelisation. 

<figure>
<img src="../../assets/images/4tasks_0.png" alt="4tasks.png" />
<figure>

</figure>
<figcaption><em>Four serial tasks run concurrently will finish faster
than for parallel 4cpu tasks CPUs one after another. </em></figcaption>
</figure>
