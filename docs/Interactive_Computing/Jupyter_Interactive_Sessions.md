---
created_at: '2020-01-05T21:43:18Z'
tags: 
  - interactive
  - JupyterLab
description: How to run an JupyterLab interactive session on the NeSI cluster.
---

# JupyterLab interactive sessions

!!! warning
     If you are using a windows computer, this method has currently 
     been tested in VSCode, WSL powershell, and WSL Ubuntu. We have not 
     tested it yet in Putty or Mobaxterm

To run Python+JupyterLab in interactive mode, first we need to load 
your interactive session:

```sh
srun --account nesi12345 --job-name "InteractiveJob" --cpus-per-task 2 --mem 8G --time 24:00:00 --pty bash
```

Then, we need to start up Python, install JupyterLab if you dont have it 
yet, and obtain the hostname and the port:

```sh
# Load Python
module load Python

# Install and activate a python virtual environment (or activate your
# current virtual environment). 
python3 -m venv venv
source venv/bin/activate

# Install JupyterLab
pip3 install JupyterLab

# Select a random port
PORT=$(shuf -i8000-9999 -n1)

# Check the hostname and port - we will need this later, you can also 
# see it at the start of your prompt
hostname | cut -d'.' -f1 # <-- This is the hostname
echo $PORT               # <-- This is the port
```

Make a note of the hostname and the port, given by the `hostname | cut -d'.' -f1`
and `echo $PORT` commands. Then, we need to start up JupyterLab:

```sh
# Start Jupyter. This might take a minute
jupyter lab --no-browser --ip=0.0.0.0 --port=$PORT
```

Make a note of the second URL given by JupyterLab once it launches. 
For instance: 

```sh
[C 2025-11-03 14:34:31.797 ServerApp] 
    
    To access the server, open this file in a browser:
        file:///home/john.doe/.local/share/jupyter/runtime/jpserver-2965439-open.html
    Or copy and paste one of these URLs:
        http://c003.hpc.nesi.org.nz:9339/lab?token=e6ff816a27867d88311bcc9f04141402590af48c2fd5f117
        http://127.0.0.1:9339/lab?token=e6ff816a27867d88311bcc9f04141402590af48c2fd5f117
```

The `http://127.0.0.1:9339/lab?token=e6ff816a27867d88311bcc9f04141402590af48c2fd5f117`
address in this case will be our url that we will use to launch JupyterLabs

In a second terminal on your local machine (or a second screen in tmux or screen),
type the following:

```sh
ssh -L PORT:HOSTNAME:PORT mahuika

#For example:
#ssh -L 9339:c003:9339 mahuika
```

Then, in your browser, type in the URL from before

```sh
http://127.0.0.1:PORT/lab?token=TOKEN

# For example:
# http://127.0.0.1:9339/lab?token=e6ff816a27867d88311bcc9f04141402590af48c2fd5f117
```

You will now be able to see and work wih Python+JupyterLab in your web browser.
