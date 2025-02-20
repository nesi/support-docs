---
created_at: '2019-05-03T04:15:24Z'
description: How to set up cluster access using 'git bash'
tags:
   - git
   - bash
   - ssh
title: Git Bash (Windows)
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000929935
zendesk_section_id: 360000189696

---

!!! prerequisite
     -   Have a [NeSI account.](Creating_a_NeSI_Account_Profile.md))
     -   Be a member of an [active project.](Applying_to_join_an_existing_NeSI_project.md)

## First time setup

1. [Download Git Bash](https://git-scm.com/download/win) as part of Git.

   The login process can be simplified with a few configurations.

2. Open Git Bash and run `nano ~/.ssh/config` to open your ssh config
    file and add the following (replacing `<username>` with your
    username):

    ```ssh
    Host mahuika
       User <username>
       Hostname login.mahuika.nesi.org.nz
       ProxyCommand ssh -W %h:%p lander
       ForwardX11 yes
       ForwardX11Trusted yes
       ServerAliveInterval 300
       ServerAliveCountMax 2

    Host maui
       User <username>
       Hostname login.maui.nesi.org.nz
       ProxyCommand ssh -W %h:%p lander
       ForwardX11 yes
       ForwardX11Trusted yes
       ServerAliveInterval 300
       ServerAliveCountMax 2

    Host lander
       User <username>
       HostName lander.nesi.org.nz
       ForwardX11 yes
       ForwardX11Trusted yes
       ServerAliveInterval 300
       ServerAliveCountMax 2

    Host *
       ControlMaster auto
       ControlPersist 1
    ```

    Close and save with ctrl <kbd>x</kbd>, <kbd>y</kbd>, <kbd>enter</kbd>

3. Ensure the permissions are correct by
    running `chmod 600 ~/.ssh/config`.

## Usage

Assuming you have followed the setup above you will be able to connect
to the clusters directly using;

``` sl
ssh mahuika
```

or

``` sl
ssh maui
```

As multiplexing is not configured *you will have to enter your login
credentials every time you open a new terminal or try to move a file.*

``` sl
scp <path/filename> mahuika:~/
```

(For more info visit [data transfer](Moving_files_to_and_from_the_cluster.md).
