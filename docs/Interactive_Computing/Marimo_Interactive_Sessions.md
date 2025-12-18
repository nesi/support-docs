---
created_at: '2020-01-05T21:43:18Z'
tags: 
  - interactive
  - Marino
description: How to run a Marino interactive session on the NeSI cluster.
---

# Marimo interactive sessions

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
and `echo $PORT` commands. Then, we need to start up Marino:

```sh
# Start Marino. This might take a minute
marimo edit --headless --host 0.0.0.0 --port $PORT
```

Make a note of the second URL given by Marino once it launches.
For instance:

```sh
Create or edit notebooks in your browser 📝

➜  URL: http://0.0.0.0:9929?access_token=Q2QwZyLs8kJP8eHLcNv13A
➜  Network: http://10.232.1.62:9929?access_token=Q2QwZyLs8kJP8eHLcNv13A
```

The `http://0.0.0.0:9929?access_token=Q2QwZyLs8kJP8eHLcNv13A`
address in this case will be our url that we will use to launch Marino

In a second terminal on your local machine (or a second screen in tmux or screen),
type the following:

```sh
ssh -L PORT:HOSTNAME:PORT mahuika

#For example:
#ssh -L 9929:c010:9929 mahuika
```

Then, in your browser, type in the URL from before

```sh
http://0.0.0.0:PORT?access_token=TOKEN

# For example:
# http://0.0.0.0:9929?access_token=Q2QwZyLs8kJP8eHLcNv13A
```

You will now be able to see and work wih Python+Marino in your web browser.
