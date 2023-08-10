---
created_at: '2020-05-12T01:43:30Z'
hidden: false
label_names: []
position: 3
title: Port Forwarding
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001523916
zendesk_section_id: 360000034315
---

> ### Requirements
>
> -   Have your [connection to the NeSI
>     cluster](https://support.nesi.org.nz/hc/en-gb/articles/360000625535-Standard-Terminal-Setup)
>     configured.

Some applications only accept connections from internal ports (i.e a
port on the same local network), if you are running one such application
on the cluster and want to connect to it you will need to set up [port
forwarding](https://en.wikipedia.org/wiki/Port_forwarding).

Three values must be known, the *local port*, the *host alias*, and the
*remote port*. Chosen port numbers should be between **1024** and
**49151** and not be in use by another process.

**Localhost: **The self address of a host (computer), equivalent
to `127.0.0.1`. The alias `localhost` can also be used in most cases.

**Local Port:** The port number you will use on your local machine. 

**Host Alias:** An alias for the socket of your main connection to the
cluster, `mahuika` or `maui` if you have set up your ssh config file as
described
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000625535).

**Remote Port:** The port number you will use on the remote machine (in
this case the NeSI cluster)

> ### Note
>
> The following examples use aliases as set up in [standard terminal
> setup](https://support.nesi.org.nz/hc/en-gb/articles/360000625535).
> This allows the forwarding from your local machine to the NeSI
> cluster, without having to re-tunnel through the lander node.

# Command line (OpenSSH)

*Works for any Linux terminal, Mac terminal, or Windows with WSL
enabled.*

The command for forwarding a port is

    ssh -L <local_port>:<destination_host>:<remote_port> <ssh_host>

## Example:

A client program on my local machine uses the port 5555 to communicate.
I want to connect to a server running on mahuika that is listening on
port 6666. In a new terminal on my local machine I enter the command:

    ssh -L 5555:localhost:6666 mahuika 

Your terminal will now function like a normal connection to mahuika.
However if you close this terminal session the port forwarding will end.

If there is no existing session on mahuika, you will be prompted for
your first and second factor, same as during the regular log in
procedure. 

> ### Note
>
> Your local port and remote port do not have to be different numbers.
> It is generally easier to use the same number for both.

# SSH Config (OpenSSH)

If you are using port forwarding on a regular basis, and don't want the
hassle of opening a new tunnel every time, you can include a port
forwarding line in your ssh config file ~/.ssh/config on your local
machine.

Under the alias for the cluster you want to connect to add the following
lines.

    LocalForward <local_port> <host_alias>:<remote_port>
    ExitOnForwardFailure yes

ExitOnForwardFailure is optional, but it is useful to kill the session
if the port fails. 

e.g.

      Host mahuika
          User cwal219
          Hostname login.mahuika.nesi.org.nz
          ProxyCommand ssh -W %h:%p lander
          ForwardX11 yes
          ForwardX11Trusted yes
          ServerAliveInterval 300
          ServerAliveCountMax 2
          LocalForward 6676 mahuika:6676
          ExitOnForwardFailure yes

In the above example, the local and remote ports are the same. This
isn't a requirement, but it makes things easier to remember.

Now so long as you have a connection to the cluster, your chosen port
will be forwarded.

> ### Note
>
> -   If you get a error message
>
>         bind: No such file or directory
>         unix_listener: cannot bind to path: 
>
>     try to create the following directory:
>
>         mkdir -P ~/.ssh/sockets

# MobaXterm

If you have Windows Subsystem for Linux installed, you can use the
method described above. This is the recommended method.

You can tell if MobaXterm is using WSL as it will appear in the banner
when starting a new terminal session. 

![mceclip0.png](../../includes/images/360004708596)

You can also set up port forwarding using the MobaXterm tunnelling
interface.

![mceclip1.png](../../includes/images/360004708616)

You will need to create **two** tunnels. One from lander to mahuika. And
another from mahuika to itself. (This is what using an alias in the
first two examples allows us to avoid).

The two tunnels should look like this.

![mobakey.png](../../includes/images/360004580035)

<span class="wysiwyg-color-green110">■</span> local port  
<span class="wysiwyg-color-orange90">■</span> remote port  
<span class="wysiwyg-color-red90">■</span> must match  
<span class="wysiwyg-color-pink80">■</span> doesn't matter

 

# sshuttle 

[sshuttle](https://sshuttle.readthedocs.io/en/stable/) is a transparent
proxy implementing VPN like traffic forwarding. It is based on Linux or
MacOS platforms (unfortunately Windows is not supported). `sshuttle`
allows users to create a VPN connection from a local machine to any
remote server that they can connect to via `ssh`.There is no need to
create a separate tunnel for every port to be forwarded, the package
routes all traffic, going to the specified subnet, through the tunnel.

The command line for `sshuttle` has the following form:

    sshuttle [-l [ip:]port] -r <host_alias>[:port] <subnets...>

More information about specific keys and modifiers for sshuttle commands
is available in the online documentation.

As an example, this is how to establish a tunnel through Mahuika login
node over to a specific virtual machine with IP address `192.168.90.5`:

    sshuttle -r mahuika 192.168.0.0/16

which uses remote SSH host Mahuika to forward all traffic coming to
`192.16.XXX.XXX` subnet through the port forwarder.

# Forwarding to Compute Nodes

Ports can also be forwarded from the login node to a compute node.

The best way to do this is by creating a reverse tunnel **from your
slurm job** (that way the tunnel doesn't depend on a separate shell, and
the tunnel will not outlive the job). 

The syntax for opening a reverse tunnel is similar the regular tunnel
command, `-N` to not execute a command after connecting, `-f` to run the
connection in the background and `-R` for a reverse tunnel ( as opposed
to `-L` ).

    ssh -Nf -R <remote_port>:localhost:<local_port> ${SLURM_SUBMIT_HOST}

An example Slurm script:

    #!/bin/bash

    #SBATCH --time 00:15:00
    #SBATCH --mem  1G

    ssh -Nf -R 6676:localhost:6676 ${SLURM_SUBMIT_HOST}

    <some process using port 6676>

> ### What Next?
>
> -   Using
>     [JupyterLab ](https://support.nesi.org.nz/hc/en-gb/articles/360001093315)on
>     the cluster.
> -   [NiceDCV ](https://support.nesi.org.nz/hc/en-gb/articles/360000719156)
> -   [Paraview](https://support.nesi.org.nz/hc/en-gb/articles/360001002956-ParaView)
