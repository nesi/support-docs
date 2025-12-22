---
created_at: '2025-12-23T07:00:00Z'
tags: 
    - globus
    - file transfer
title: Globus CLI
---

This page will describe the various step to how to use the Globus Command Line Interface (CLI).
This is a useful way to use globus directly from your terminal.

## Loading Globus CLI and logging in

Whenever you need to use Globus CLI, you must first load the module:

```sh
module load Globus-CLI/3.16.0-foss-2023a
```

Then, you need to login to Globus by typing into the terminal

```sh
globus login
```

This will show you a website that will require you to authenticate yourself, as well as to allow
Globus CLI to have access to your Globus files. You will be given an authorization codethat you
want to enter into the terminal.

![Globus_CLI_1.png](../../assets/images/Globus_CLI_1.png)
![Globus_CLI_2.png](../../assets/images/Globus_CLI_2.png)
![Globus_CLI_3.png](../../assets/images/Globus_CLI_3.png)
![Globus_CLI_4.png](../../assets/images/Globus_CLI_4.png)
![Globus_CLI_5.png](../../assets/images/Globus_CLI_5.png)
![Globus_CLI_6.png](../../assets/images/Globus_CLI_6.png)

## Transfer files/folders using Globus CLI

To transfer a files/folders using
