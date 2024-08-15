---
created_at: 2024-08-05
description: How to set up Visual Studio Code to access the NeSI cluster
tags: [vscode, ide]
---

'Visual Studio Code' (not to be confused with 'Visual Studio') or 'VSCode', is a popular editor/IDE that with many useful extensions. The 'Remote' extension allows you to connect to a remote computer (like NeSI).

## Setup

=== "Linux / MacOS"
    - Make sure you have set up an `~/.ssh/config` file as described in
    [Terminal Setup](../Terminal_Setup).
    - Open the 'Extensions' Tab, search `remote` and make sure you have 'Remote - SSH' and 'Remote Explorer' by Microsoft, installed.
    ![vscode remote extension](../../../assets/images/vscode-remote.png)
=== "Windows"
    - Set up WSL as described in
    [Windows Subsystem for Linux (WSL)](Windows_Subsystem_for_Linux_WSL.md).
    - Open the 'Extensions' Tab, search `remote` and make sure you have 'Remote - SSH', 'Remote Explorer' and  by Microsoft, installed
    ![vscode remote extension](../../../assets/images/vscode-remote.png)
    - Make sure you have set up an `~/.ssh/confisg` file as described in
    [Terminal Setup](../Terminal_Setup), in your subsystem install.

<!-- ```json
"remote.SSH.configFile": "\\\\wsl$\\Ubuntu-20.04\\home\\cwal219\\.ssh\\config",
"remote.SSH.path": "C:\\Users\\cwal219\\ssh.bat",
"security.allowedUNCHosts": ["wsl$", "wsl.localhost"],
``` -->

## Connecting

Under the 'Remote Explorer' Tab on the left, you should now see the NeSI machines (as well as any other machines configured in your `~/.ssh/config` file)

![vscode explorer](../../../assets/images/vscode-explorer.png)

You will then be prompted for your password and second factor, as per usual.

!!! warning
    As VSCode will continue attempting to reconnect after a failure,
    take care that you do-not get locked out for too many failed login attempts.

## Features

## Changing Software Versions

You may find that VSCode is not utilising your preferred versions of software (e.g. when debugging or linting).

As the NeSI cluster utilises [Environment Modules](../../Getting_Started/Next_Steps/Submitting_your_first_job.md#environment-modules), changing the executable used is not just a matter of changing the path in VSCode configuration, as the libraries required will not be loaded. 

The only way to make sure that VSCode has access to a suitable environment, is to load the required modules in your `~/.bashrc`

For example,
