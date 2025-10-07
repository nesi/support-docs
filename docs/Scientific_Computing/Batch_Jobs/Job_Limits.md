---
created_at: 2025-07-17
description: What limits are there on running jobs.
tags: 
    - Slurm
    - accounting
---

These are open for review if you find any of them unreasonable or inefficient.  

#### Per Job

- 10 nodes
- 21 node-days (so 1 node for 3 weeks, or 3 nodes for 1 week, or 10 nodes for 2 days)
- 21 days (but less on `milan` until more of those nodes arrive)

#### Per User

- 1344 CPU cores occupied (8 full Genoa nodes),
- 3528 core-days booked by running jobs (so 3 weeks of one full Genoa node).
- 6 TB of memory occupied (4 full 1.5 TB nodes)
- 30 TB-days booked by running jobs (so 3 weeks of one full 1.5 TB node).
- 6 GPUs occupied, 14 GPU-days booked by running jobs (so 2 GPUs for 1 week).
- No user can have more than 1,000 jobs in the queue at a time.
