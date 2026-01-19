---
created_at: '2019-09-22T20:20:07Z'
tags:
 - sinfo
 - busy
title: How busy is the cluster?
---

You can get information about all nodes on Mahuika using the command `sinfo`. Type the following into Mahuika

```bash
sinfo -N --Format=nodelist:10,StateLong:15,cpusState:20,Memory:15,FreeMem:15,Gres:30,GresUsed:30
```

where:

* `NODELIST`: The name of the node
* `STATE`: The state of the node
* `CPUS`: The amount of CPUs that each machine has and the number of CPUs available. A: Allocated (in use), I: Idle (not in use), O: Other, T: Total.
* `MEMORY`: The total amount of memory on the node (in MBs)
* `FREE_MEM`: The amount of memory free on the node (in MBs)
* `GRES`: The total amount of resources available on each node
* `GRES_USED`: The amount of resources that are currently being used on each node

This will give the following information:

```bash
username@login03:~$ sinfo -N --Format=nodelist:10,StateLong:15,cpusState:20,Memory:15,FreeMem:15,Gres:30,GresUsed:30,
NODELIST  STATE          CPUS(A/I/O/T)       MEMORY         FREE_MEM       GRES                          GRES_USED                     
c001      mixed          270/66/0/336        366694         83097          ssd:1                         ssd:0                         
c001      mixed          270/66/0/336        366694         83097          ssd:1                         ssd:0                         
c002      mixed          284/52/0/336        366694         79030          ssd:1                         ssd:0                         
c002      mixed          284/52/0/336        366694         79030          ssd:1                         ssd:0                         
c003      allocated      332/4/0/336         366694         176942         ssd:1                         ssd:0                         
c003      allocated      332/4/0/336         366694         176942         ssd:1                         ssd:0                         
c004      mixed          272/64/0/336        366694         75632          ssd:1                         ssd:0                         
c004      mixed          272/64/0/336        366694         75632          ssd:1                         ssd:0                         
g01       mixed          248/88/0/336        734401         289413         gpu:a100:2(S:1),ssd:1         gpu:a100:2(IDX:0-1),ssd:0     
g01       mixed          248/88/0/336        734401         289413         gpu:a100:2(S:1),ssd:1         gpu:a100:2(IDX:0-1),ssd:0     
g02       mixed          12/324/0/336        734401         223072         gpu:a100:2(S:1),ssd:1         gpu:a100:2(IDX:0-1),ssd:0     
g02       mixed          12/324/0/336        734401         223072         gpu:a100:2(S:1),ssd:1         gpu:a100:2(IDX:0-1),ssd:0     
g03       mixed          240/96/0/336        734401         259001         gpu:a100:2(S:1),ssd:1         gpu:a100:2(IDX:0-1),ssd:0     
g03       mixed          240/96/0/336        734401         259001         gpu:a100:2(S:1),ssd:1         gpu:a100:2(IDX:0-1),ssd:0     
g04       mixed          224/112/0/336       734401         233893         gpu:a100:2(S:1),ssd:1         gpu:a100:2(IDX:0-1),ssd:0     
g04       mixed          224/112/0/336       734401         233893         gpu:a100:2(S:1),ssd:1         gpu:a100:2(IDX:0-1),ssd:0     
g05       mixed-         292/44/0/336        1469837        395533         gpu:h100:2(S:1),ssd:1         gpu:h100:2(IDX:0-1),ssd:1     
g05       mixed-         292/44/0/336        1469837        395533         gpu:h100:2(S:1),ssd:1         gpu:h100:2(IDX:0-1),ssd:1     
g06       mixed-         300/36/0/336        1469837        602928         gpu:h100:2(S:1),ssd:1         gpu:h100:2(IDX:0-1),ssd:0     
g06       mixed-         300/36/0/336        1469837        602928         gpu:h100:2(S:1),ssd:1         gpu:h100:2(IDX:0-1),ssd:0     
g07       mixed-         268/68/0/336        1469837        373625         gpu:h100:2(S:1),ssd:1         gpu:h100:1(IDX:0),ssd:0       
g07       mixed-         268/68/0/336        1469837        373625         gpu:h100:2(S:1),ssd:1         gpu:h100:1(IDX:0),ssd:0       
g08       mixed-         284/52/0/336        1469837        32788          gpu:h100:2(S:1),ssd:1         gpu:h100:2(IDX:0-1),ssd:0     
g08       mixed-         284/52/0/336        1469837        32788          gpu:h100:2(S:1),ssd:1         gpu:h100:2(IDX:0-1),ssd:0     
g09       mixed-         308/28/0/336        1469837        124360         gpu:l4:4(S:0-1),ssd:1         gpu:l4:3(IDX:0-2),ssd:0       
g09       mixed-         308/28/0/336        1469837        124360         gpu:l4:4(S:0-1),ssd:1         gpu:l4:3(IDX:0-2),ssd:0       
g10       mixed-         300/36/0/336        1469837        107368         gpu:l4:4(S:0-1),ssd:1         gpu:l4:1(IDX:0),ssd:0         
g10       mixed-         300/36/0/336        1469837        107368         gpu:l4:4(S:0-1),ssd:1         gpu:l4:1(IDX:0),ssd:0         
g11       mixed-         306/30/0/336        1469837        21118          gpu:l4:4(S:0-1),ssd:1         gpu:l4:3(IDX:0-2),ssd:0       
g11       mixed-         306/30/0/336        1469837        21118          gpu:l4:4(S:0-1),ssd:1         gpu:l4:3(IDX:0-2),ssd:0       
g12       mixed-         308/28/0/336        1469837        548433         gpu:l4:4(S:1,3,5,7),ssd:1     gpu:l4:4(IDX:0-3),ssd:0       
g12       mixed-         308/28/0/336        1469837        548433         gpu:l4:4(S:1,3,5,7),ssd:1     gpu:l4:4(IDX:0-3),ssd:0    
```

Some notes:

* Note that 2 cpus from above are unavailable (one for slurm, and one for WEKA).
* `STATE`: most of the time you can ignore this. But if this message is `down` or `draining`, this indicates the node is unavailable for use.
* `GRES` and `GRES_USED`: Compare these to see how many internal SSDs and GPUs are available for use. For example, `g10` `GRES` indicates this node contains 4 L4 GPUs in total, while `g10` `GRES_USED` indicates that only 1 L4 GPU is being used for `g10`. This means there are 3 L4 GPUs available on `g10`. In the example above, as long as your job requires less than 18 cores (36 divided by 2) and 107368 MBs (104 GBs) RAM, your job should go on (however, this will still be based on your priority)
* Each node appears twice in this command. This is because each node is apart of the `genoa`/`milan` partition as well as being apart of the `maintanance` partition. 

## What Jobs are Running on a Particular Node

If you would like to know more about what jobs are running on a node and what resources they are using, type into Mahuika:

```bash
squeue -w <NODE_NAME> -O "JobID,UserName,State,NumCPUs,MinMemory,GRES,TimeLeft"
```

where `<NODE_NAME>` is the name of the node, and where:

* `JOBID`: The job id for the slurm job
* `USER`: The username of the slurm job
* `STATE`: The state of this job
* `CPUS`: The number of CPUs this job is using (this will be 2 times the number of CPUs requested, i.e. if a job requests 4 CPUs, it will show here as 8)
* `MIN_MEMORY`: The amount of RAM that the job is using
* `TRES_PER_NODE`: The resources that the job is using, such as the numbver of GPUs and internal SSDs that are being used.
* `TIME_LEFT`: The time left on the job before it timesout

An example of what this looks like is shown below

```bash
username@login03:~$ squeue -w g09 -O "JobID,UserName,State,NumCPUs,MinMemory,GRES,TimeLeft"
JOBID               USER                STATE               CPUS                MIN_MEMORY          TRES_PER_NODE       TIME_LEFT           
4153353             user1              RUNNING             2                   8G                  N/A                 1-17:13:53          
4120303             user2              RUNNING             2                   5G                  N/A                 2-21:32:52          
4134913             user3              RUNNING             2                   5G                  N/A                 20:20:29            
4181740             user4              RUNNING             8                   32G                 N/A                 5-21:08:11          
4184516             user5              RUNNING             2                   216G                gres/gpu:1          1-15:15:44          
4187996             user6              RUNNING             2                   6G                  N/A                 2:13:49             
4188252             user7              RUNNING             8                   25G                 gres/gpu:1          1-02:42:15          
4197896             user8              RUNNING             2                   5G                  N/A                 6-19:20:09          
4198360             user9              RUNNING             4                   2G                  gres/gpu:l4:1       22:53:42    
```
