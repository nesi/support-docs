---
created_at: 2026-05-04
description: How to run ollama on the REANNZ GPUs
tags: 
    - llm
---


{% set app = applications["ollama"] %}

{{ app.description }}

For a list of available models, see [AI Models](../../Storage/Models.md).

## Interactive Run

!!! warning
    We don't recommend running ollama like this except for small test jobs.
    It is a very inefficient use of GPUs.

```sl
#!/bin/bash -e

#SBATCH --account nesi99991
#SBATCH --job-name ollama-test
#SBATCH --time 01:00:00
#SBATCH --mem 10G
#SBATCH --gpus-per-node l4:1

PORT=16000 # please choose your own port number between 1024 and 49151

module purge
module load ollama/{{ app.default }}
export OLLAMA_HOST=${HOSTNAME}:${PORT}
ssh -NfR ${PORT}:${HOSTNAME}:${PORT} ${SLURM_SUBMIT_HOST}

unset CUDA_VISIBLE_DEVICES # Slurm sets this to 0

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

## Batch Job

Start `ollama serve` in the background, wait for it to be ready, run your prompt, then exit.
The job ending kills the server automatically.

```sl
#!/bin/bash -e

#SBATCH --account        nesi99991
#SBATCH --job-name       ollama-batch
#SBATCH --time           00:30:00
#SBATCH --mem            10G
#SBATCH --gpus-per-node  l4:1

module load ollama
unset CUDA_VISIBLE_DEVICES  # Slurm sets this to 0; ollama manages the GPU itself

# pipe server output to `/dev/null` to avoid noise.
ollama serve &>/dev/null & 

until ollama list &>/dev/null; do sleep 1; done

echo "What is the capital of France" | ollama run llama3.1:8b
```

!!! tip "Random Port"

    ```
    PORT=$(python3 -c "import socket; s=socket.socket(); s.bind(('', 0)); print(s.getsockname()[1]); s.close()")
    ```
    Will assign a random free port number to `PORT`

!!! tip Debugging
    For verbose server logs, set `OLLAMA_DEBUG=1` before `ollama serve`.
