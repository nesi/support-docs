---
created_at: 2024-08-05
description: How to set up Visual Studio Code to access the NeSI cluster
tags: [ide, code]
---

'Visual Studio Code' (not to be confused with 'Visual Studio') or 'VSCode', is a popular editor/IDE with many useful extensions.
The 'Remote' extension allows you to connect to a remote computer (like NeSI).

## Setup

=== "Linux / MacOS"
    1. Make sure you have set up an `~/.ssh/config` file as described in
    [Terminal Setup](Standard_Terminal_Setup.md).
    2. In VSCode, open the 'Extensions' Tab, search `remote` and make sure you have 'Remote - SSH' and 'Remote Explorer' by Microsoft, installed.
    ![vscode remote extension](../../assets/images/vscode-remote.png)
=== "Windows"
    1. Set up WSL as described in
    [Windows Subsystem for Linux (WSL)](Windows_Subsystem_for_Linux_WSL.md).
    2. In VSCode, open the 'Extensions' Tab, search `remote` and make sure you have 'Remote - SSH' and 'Remote Explorer' by Microsoft installed.
    ![vscode remote extension](../../assets/images/vscode-remote.png)
    3. Still in the 'Extensions' Tab, search `wsl` and make sure you have 'WSL' by Microsoft installed.
    4. In `C:\Users\<username>` create a file named `ssh.bat` with the following contents.
      ```bat
      C:\Windows\system32\wsl.exe ssh %*
      ```
    Where `<username>` is your username.
    5. In VSCode, open your configuration file by pressing <kbd>ctrl</kbd> + <kbd>shift</kbd> + <kbd>P</kbd>, then typing `user settings json` and selecting "Preferences: Open User Settings (JSON)"
    6. Add the following to the config file opened
    ```json
    "remote.SSH.configFile": "\\\\wsl$\\<distro>\\home\\<username>\\.ssh\\config",
    "remote.SSH.path": "C:\\Users\\<username>\\ssh.bat",
    "security.allowedUNCHosts": ["wsl$", "wsl.localhost"],
    ```
    Where `<username>` is your username and `<distro>` is your installed WSL distribution (e.g. `Ubuntu-20.04`).
    7. Make sure the config file is valid JSON (e.g. each keypair is followed by a `,`
    and is in between the enclosing `{}`), then save.
    8. From inside a WSL terminal follow the steps to set up an `~/.ssh/config` file as described in
    [Terminal Setup](Standard_Terminal_Setup.md), in your subsystem install.

!!! tip
    You may want to set `"remote.SSH.showLoginTerminal": true` as VSCode does not always correclty identify when a login prompt is presented.

## Connecting

Under the 'Remote Explorer' Tab on the left, you should now see the NeSI machines (as well as any other machines configured in your `~/.ssh/config` file)

![vscode explorer](../../assets/images/vscode-explorer.png)

Clicking on these will open a connection to that machine, you will then be prompted for your password and second factor, as per usual.

!!! warning
    As VSCode will continue attempting to reconnect after a failure,
    take care that you do-not get locked out for too many failed login attempts.

## Changing Software Versions

### Environment Modules

You may find that VSCode is not utilising your preferred versions of software (e.g. when debugging or linting your Python code).

As the NeSI cluster utilises [Environment Modules](../../Getting_Started/Next_Steps/Submitting_your_first_job.md#environment-modules), changing the executable used is not just a matter of changing the path in VSCode configuration, as the libraries required will not be loaded.

The only way to make sure that VSCode has access to a suitable environment, is to load the required modules in your `~/.bashrc`

For example, if you use `Python/3.11.3-gimkl-2022a` in your SLURM scripts, and wish to use the VSCode plugins with this version of Python you will need to add `module load Python/3.11.3-gimkl-2022a` at the end of your `~/.bashrc`
then restart [VSCode](#killing-vscode).

!!! warning
    Commands in your `~/.bashrc` are run **whenever a new shell is opened**, meaning every Slurm job, every terminal session in Jupyter or via SSH will be affected. Make sure to have `module purge` in any Slurm scripts that may be affected by changes in loaded modules.

### Using Virtual Environments

Setting up virtual environments on remote machines [follows the same steps as for on your local machine](https://code.visualstudio.com/docs/python/environments), however you will still have to load your desired version of Python / Conda using the method described in [Changing Software Versions - Environment Modules](#environment-modules).

## Killing VSCode

As VSCode operates spawns a server running on the cluster, closing your local client will not necessarily lead to all processes being stopped on the cluster. This is not usually a problem, as the processes do not use much resources, however sometimes you may want a clean start (e.g. after changing modules in your `~/.bashrc`).

From the cluster, running the command

```sh
killall code
```

Will end all your VSCode related processes.

!!! warning
    This will end all tasks running in the integrated terminal, and your connection to the cluster will be lost.
