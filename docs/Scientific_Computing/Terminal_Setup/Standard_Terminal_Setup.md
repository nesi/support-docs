---
created_at: '2018-11-30T00:34:14Z'
hidden: false
label_names:
- ssh
- howto
position: 0
title: Standard Terminal Setup
vote_count: 7
vote_sum: 7
zendesk_article_id: 360000625535
zendesk_section_id: 360000189696
---

> ### Requirements
>
> -   Have an [active account and
>     project.](https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects)
> -   Set up your [Linux
>     Password.](https://support.nesi.org.nz/hc/en-gb/articles/360000335995)
> -   Set up Second [Factor
>     Authentication.](https://support.nesi.org.nz/hc/en-gb/articles/360000203075)
> -   Using standard Linux/Mac terminal *or* [Windows Subsystem for
>     Linux](https://support.nesi.org.nz/hc/en-gb/articles/360001075575)
>     with [Ubuntu
>     terminal](https://support.nesi.org.nz/hc/en-gb/articles/360001050575).

## First time setup

The login process can be simplified significantly with a few easy
configurations.

1.  In a new local terminal run; `mkdir -p ~/.ssh/sockets` this will
    create a hidden file in your home directory to store socket
    configurations.
2.  Open your ssh config file with  `nano ~/.ssh/config` and add the
    following (replacing **`username`** with your username):

        Host mahuika
           User username
           Hostname login.mahuika.nesi.org.nz
           ProxyCommand ssh -W %h:%p lander
           ForwardX11 yes
           ForwardX11Trusted yes
           ServerAliveInterval 300
           ServerAliveCountMax 2

        Host maui
           User username
           Hostname login.maui.nesi.org.nz
           ProxyCommand ssh -W %h:%p lander
           ForwardX11 yes
           ForwardX11Trusted yes
           ServerAliveInterval 300
           ServerAliveCountMax 2

        Host lander
           User username
           HostName lander.nesi.org.nz
           ForwardX11 yes
           ForwardX11Trusted yes
           ServerAliveInterval 300
           ServerAliveCountMax 2

        Host *
            ControlMaster auto
            ControlPath ~/.ssh/sockets/ssh_mux_%h_%p_%r
            ControlPersist 1

    Close and save with <kbd>ctrl x</kbd>, <kbd>y</kbd>,
    <kbd>Enter</kbd>

3.  Ensure the permissions are correct by
    running `chmod 600 ~/.ssh/config`.

## Usage

Assuming you have followed the setup above you will be able to connect
to the clusters directly using;

    ssh mahuika

or

    ssh maui

Subsequent local terminals opened will be able to scp files without
having to re-enter authentication e.g.

    scp <path/filename> mahuika:~/

(For more info visit [data
transfer](https://support.nesi.org.nz/hc/en-gb/articles/360000578455-File-Transfer-with-SCP)).

> ### What Next?
>
> -   [Moving files to/from a
>     cluster.](https://support.nesi.org.nz/hc/en-gb/articles/360000578455)
> -   Setting up a
>     [X-Server](https://support.nesi.org.nz/hc/en-gb/articles/360001075975) (optional).
