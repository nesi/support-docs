---
created_at: '2024-03-05T23:28:34Z'
tags: []
vote_count: 0
vote_sum: 0
zendesk_article_id: 9170849009551
zendesk_section_id: 360000164635
---

When you ask the support team for help, there are a few things we will
almost always want to know, you can save us (and yourself) time by
including this information in your support request.

General Troubleshooting

- What command(s) you ran
- The error message.
    - You may have to look in the slurm output. If you didn't
        explicitly set on, it will be in the directory you submitted
        from and look something like `slurm-44240633.out`
- Environment (modules loaded, conda, venv, etc).
    - You can use the command `module list` to get a list of loaded
        modules.
    - env will give a complete print out of your environment (it will
        be long).
- What things you have tried so far.

If your problem involves a SLURM job, please include:

- The job ID
    - sacct will show a list of all your recently run jobs and their
        status.
- The Slurm Script used.
    - Including `cat $0` in your slurm script will print the script
        into your output. This is useful as you will always have the
        script recorded as it was when you submitted.
- directory/pathway to files.
- When you last had a job succeed (and slurm jobid if applicable) 

[FurtherReading](https://hpc-uit.readthedocs.io/en/latest/help/writing-support-requests.html)
