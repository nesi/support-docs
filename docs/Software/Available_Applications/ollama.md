---
created_at: 2026-05-04
description: How to run ollama on the REANNZ GPUs
tags: 
    - llm
---


{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}

{{ app.description }}


## Starting ollama in a Slurm job

! warn
    We don't reccomend running ollama like this except for small test jobs.
    It is a very inefficient use of GPUs.


```sl
#!/bin/bash -e

#SBATCH --account nesi99991
#SBATCH --job-name ollama test
#SBATCH --time 01:00:00
#SBATCH --mem 10G
#SBATCH --gpus-per-node l4:1

PORT=16000 # please choose your own port number between 1024 and 49151

module load ollama
export OLLAMA_HOST=${HOSTNAME}:${PORT}
ssh -NfR ${PORT}:${HOSTNAME}:${PORT} ${SLURM_SUBMIT_HOST}

ollama serve
```

Then on the login node run,

```sh
module  load ollama
export OLLAMA_HOST=<nodename>:<port>
ollama
```

Where `<nodename>` is the host name of the node running your job (you can find this with `sacct` or `squeue --me`),
and `<port>` is your selected port.

!!! tip
    For debugging set

    ```sh
    GIN_MODE=debug
    ``` 

    before starting `ollama`.
