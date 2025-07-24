---
created_at: '2019-05-03T04:15:24Z'
description: How to set up cluster access using 'git bash'
tags:
   - git
   - bash
   - ssh
title: Git Bash (Windows)
---

!!! prerequisite
     -   Have a [NeSI account.](../../Getting_Started/Accounts-Projects_and_Allocations/Creating_a_NeSI_Account_Profile.md).
     -   Be a member of an [active project.](../../Getting_Started/Accounts-Projects_and_Allocations/Applying_to_join_an_existing_NeSI_project.md)

## First time setup

1. [Download Git Bash](https://git-scm.com/download/win) as part of Git.

   The login process can be simplified with a few configurations.

2. Follow instructions [Standard Terminal Setup](Standard_Terminal_Setup.md).

## Usage

Assuming you have followed the setup above you will be able to connect
to the clusters directly using;

```sh
ssh nesi
```

You will be prompted twice for Authetication ![alt text](../../assets/images/gitbash_auth1.png)
Hit `ctrl` and click the link and then `enter` after the browser pop shows
![alt text](../../assets/images/gitbash_auth2.png)

As multiplexing is not configured *you will have to enter your login
credentials every time you open a new terminal or try to move a file.*

```sh
scp <path/filename> nesi:~/
```

For more info visit [data transfer](../../Getting_Started/Next_Steps/Moving_files_to_and_from_the_cluster.md).

!!! prerequisite "What Next?"
   - [Standard Terminal Setup](Standard_Terminal_Setup.md)
