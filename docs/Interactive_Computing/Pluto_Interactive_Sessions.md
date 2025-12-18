---
created_at: '2020-01-05T21:43:18Z'
tags: 
  - interactive
  - Pluto
description: How to run a Pluto interactive session on the NeSI cluster.
---

# Pluto.ji interactive sessions

!!! warning
     If you are using a windows computer, this method has currently
     been tested in VSCode, WSL powershell, and WSL Ubuntu. We have not
     tested it yet in Putty or Mobaxterm

To run Julia+Pluto.ji in interactive mode, first we need to load
your interactive session:

```sh
srun --account nesi12345 --job-name "InteractiveJob" --cpus-per-task 2 --mem 8G --time 24:00:00 --pty bash
```

Then, we need to start up Julia and obtain the hostname and the port:

```sh
# Load Julia
module load Julia 

# Select a random port
PORT=$(shuf -i8000-9999 -n1)

# Check the hostname and port - we will need this later, you can also 
# see it at the start of your prompt
hostname | cut -d'.' -f1 # <-- This is the hostname
echo $PORT               # <-- This is the port

# Export port to a variable name
export pluto_port=${PORT}
```

Make a note of the hostname and the port, given by the `hostname | cut -d'.' -f1`
and `echo $PORT` commands. Then, we need to start up Julia, install and
run Pluto.ji:

```sh
#Start Julia
julia

# Install Pluto.ji. This might take a minute
import Pkg; Pkg.add("Pluto")

# Start Pluto. This might take a minute
using Pluto
Pluto.run(host="0.0.0.0",port=parse(Int, ENV["pluto_port"]),launch_browser=false)
```

Take a note of the information given for the URL

```sh
[ Info: Loading...
┌ Info: 
│ Go to http://0.0.0.0:9627/?secret=mXmq6659 in your browser to start writing ~ have fun!
└ 
```

Here, we will be using `http://0.0.0.0:9627/?secret=mXmq6659` to access
Pluto.

Next, open up a second terminal on your local machine (or a second screen
in tmux or screen), and type the following:

```sh
ssh -L PORT:HOSTNAME:PORT mahuika

#For example:
#ssh -L 9627:mc081:9627 mahuika
```

Then, in your browser, type in the URL from before

```sh
http://0.0.0.0:PORT/?secret=SECRET

# For example:
# http://0.0.0.0:9627/?secret=mXmq6659
```

You will now be able to see and work wih Julia+Pluto in your web browser.
