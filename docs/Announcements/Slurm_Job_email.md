---
created_at: 2026-02-11
description: Email from Slurm Jobs now available
tags: 
    - hpc3
    - email
    - mahuika
---

Sending email from Slurm jobs is now available on Mahuika.  Here is an example of the Slurm parameters required to send email:

```
   #SBATCH --mail-type=ALL
   #SBATCH --mail-user=myemail@mydomain.com
```

`mail-type` can be _BEGIN_, _END_, _FAIL_, and others.  See the `sbatch` manpage for a full list.  Using _ALL_ will send an email for any of the event types. 
