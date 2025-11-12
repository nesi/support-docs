---
created_at: '2018-10-25T02:22:02Z'
tags:
- faq
description: Explanation of the "oom-kill" error
---

OOM stands for "Out Of Memory", and so an error such as this:

```bash
slurmstepd: error: Detected 1 oom-kill event(s) in step 370626.batch cgroup
```

indicates that your job attempted to use more memory (RAM) than Slurm
reserved for it.  

OOM events can happen even without Slurm's `sacct` command reporting
such a high memory usage, for two reasons:

- Unlike the enforcement via cgroups, Slurm's accounting system only
    records usage every 30 seconds, so sudden spikes in memory usage may
    not be recorded, but can still trigger the OOM killer;
- Slurm's accounting system also does not include any temporary files
    the job may have put in the memory-based `/tmp` or `$TMPDIR`
    filesystems.

If you see an OOM event, you have two options. The easier option is to
request more memory by increasing the value of the `--mem` argument in
your job submission script. The more difficult, but potentially more
useful where it is feasible, is to make your job less memory-intensive.
