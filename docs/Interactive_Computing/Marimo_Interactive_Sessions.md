---
created_at: '2020-01-05T21:43:18Z'
tags: 
  - interactive
  - Marino
description: How to run a Marino interactive session on the NeSI cluster.
---

# Running Python+Marino in Interactive Mode

!!! warning
     If you are using a windows computer, this method has currently 
     been tested in VSCode, WSL powershell, and WSL Ubuntu. We have not 
     tested it yet in Putty or Mobaxterm

To run Python+Marino in interactive mode, first we need to load 
your interactive session:

```sh
srun --account nesi12345 --job-name "InteractiveJob" --cpus-per-task 2 --mem 8G --time 24:00:00 --pty bash
```

Then, we need to start up Python, install Marino if you dont have it 
yet, and obtain the hostname and the port:

```sh
# Load Python
module load Python

# Install and activate a python virtual environment (or activate your
# current virtual environment). 
python3 -m venv venv
source venv/bin/activate

# Install Marino
pip3 install marimo

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
# Start Marino. This might take a minute
jupyter lab --no-browser --ip=0.0.0.0 --port=$PORT
marimo edit --no-token --headless --port $PORT
```

Make a note of the second URL given by JupyterLab once it launches. 
For instance: 

```sh
Create or edit notebooks in your browser 📝

➜  URL: http://0.0.0.0:9153/node/0.0.0.0/9153
➜  Network: http://10.232.1.65:9153/node/0.0.0.0/9153
```

The `http://0.0.0.0:9153/node/0.0.0.0/9153`
address in this case will be our url that we will use to launch JupyterLabs

In a second terminal on your local machine (or a second screen in tmux or screen),
type the following:

```sh
ssh -L PORT:HOSTNAME:PORT mahuika

#For example:
#ssh -L 9153:c003:9153 mahuika
```

Then, in your browser, type in the URL from before

```sh
http://127.0.0.1:PORT/lab?token=TOKEN

# For example:
# http://127.0.0.1:9339/lab?token=e6ff816a27867d88311bcc9f04141402590af48c2fd5f117
```

You will now be able to see and work wih Python+JupyterLab in your web browser.
