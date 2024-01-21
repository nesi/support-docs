---
created_at: '2018-11-30T00:34:14Z'
tags:
- ssh
- howto
vote_count: 8
vote_sum: 6
zendesk_article_id: 360000625535
zendesk_section_id: 360000189696
---

!!! prerequisite
     -   Have an [active account and project.](https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects)
     -   Set up your [Linux Password.](../../Getting_Started/Accessing_the_HPCs/Setting_Up_and_Resetting_Your_Password.md)
     -   Set up Second [Factor Authentication.](../../Getting_Started/Accessing_the_HPCs/Setting_Up_Two_Factor_Authentication.md)
     -   Using standard Linux/Mac terminal *or* [Windows Subsystem for Linux](../../Scientific_Computing/Terminal_Setup/Windows_Subsystem_for_Linux_WSL.md)
         with [Ubuntu terminal](../../Scientific_Computing/Terminal_Setup/Ubuntu_LTS_terminal_Windows.md).

## First time setup

The login process can be simplified significantly with a few easy
configurations.

1. In a new local terminal run; `mkdir -p ~/.ssh/sockets` this will
    create a hidden file in your home directory to store socket
    configurations.

2. Open your ssh config file with  `nano ~/.ssh/config` and add the
    following (replacing **`username`** with your username):

    ``` sh
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
    ```

    Close and save with ctrl x, y, Enter

3. Ensure the permissions are correct by
    running `chmod 600 ~/.ssh/config`.

## Usage

Assuming you have followed the setup above you will be able to connect
to the clusters directly using;

``` sh
ssh mahuika
```

or

``` sh
ssh maui
```

Subsequent local terminals opened will be able to `scp` files without
having to re-enter authentication e.g.

``` sh
scp <path/filename> mahuika:~/
```

(For more info visit [data transfer](https://support.nesi.org.nz/hc/en-gb/articles/360000578455-File-Transfer-with-SCP)).

!!! prerequisite "What Next?"
     -   [Moving files to/from a cluster.](../../Getting_Started/Next_Steps/Moving_files_to_and_from_the_cluster.md)
     -   Setting up an [X-Server](../../Scientific_Computing/Terminal_Setup/X11_on_NeSI.md) (optional).
