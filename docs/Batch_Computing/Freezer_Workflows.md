---
created_at: 2026-04-02
description: Freezer Workflow Examples
tags:
    - freezer
    - autodelete
    - s3cmd
---

## Intro

The following page will present examples of how you can use our Freezer service as part of your workflows.  If you 
want to restore and retrieve data manually 



## Manual restore example

If running manually, we recommend starting a terminal multiplexer such as `tmux` to allow you to close your laptop or otherwise disconnect from the cluster while the data retrieval continues, for example:

```
    tmux new -s freezer
    cd /nesi/nobackup/nesi99999/project1
    s3cmd restore s3://nesi99999-10551/project1/data.tar
    s3cmd get s3://nesi99999-10551/project1/data.tar
```

You can reconnect to your session by running:  `tmux a -t freezer`   We have more information about 
`tmux` on this page: [tmux reference](../Getting_Started/Cheat_Sheets/tmux-Reference_sheet.md)

We also have more examples of running the Freezer utility, `s3cmd`, on our main Freezer documentation 
page: [Freezer long term storage](../Storage/Long_Term_Storage/Freezer_long_term_storage.md).  


## Slurm dependency examples

The Mahuika job scheduler, Slurm, has the ability to run jobs that depend on the outcome of another job.  
This is called a job dependency.  Running any large filesystem tasks such as retrieving data from Freezer, 
allows you to optimize your resource request.  Instead of retrieving data as part of a multi-CPU/large 
memory job, you can run a data retrievel job with minimal resources which is depended upon by your main 
compute job.  

### Singleton Dependency

The easiest example of a job dependency is the _singleton_ type.  A singleton job will start after all your
previous jobs of the same name successfuly complete.

##### Data staging job
```
    #!/bin/bash -e
    #SBATCH --job-name=bigjob
    #SBATCH --cpus-per-task=1
    #SBATCH --mem=2G
    #SBATCH --time=1-00:00 #1 day

    cd /nesi/nobackup/nesi99999/project1
    s3cmd restore s3://nesi99999-10551/project1/data.tar
    s3cmd get s3://nesi99999-10551/project1/data.tar
    
    tar xvf data.tar

    echo "done with Freezer staging and extraction"
```

##### Main job
```
    #!/bin/bash -e
    #SBATCH --job-name=bigjob  #name must match job dependency
    #SBATCH --cpus-per-task=32
    #SBATCH --mem=64G
    #SBATCH --time=6:00:00 # 6 hours
    #SBATCH --dependency=singleton

    compute data.in
```
    
You will then run the data staging job followed by your main job.  As soon as the data staging job completes 
your main job will be queued to run.

#### Snakemake example


#### NextFlow example




