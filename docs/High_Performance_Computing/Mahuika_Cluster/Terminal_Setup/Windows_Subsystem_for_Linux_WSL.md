---
created_at: '2019-07-30T00:31:40Z'
tags: [wsl, windows, terminal]
title: Windows Subsystem for Linux (WSL)
description: Enabling WSL allows utilising Linux tools on Windows.
vote_count: 4
vote_sum: 4
---

!!! prerequisite
     -   Windows 10 (version 1903) or later.

Windows Subsystem for Linux is a feature that allows you to utilise some
Linux commands and command line tools.

WSL is enabled by default on later versions of Windows 10.

!!! tip
     WSL1 has been superseded by WSL2, which is an
     [improvement in several areas](https://learn.microsoft.com/en-us/windows/wsl/compare-versions).
  
     You can what version is installed by opening 'Windows PowerShell'
     and typing `wsl --version`.
  
     If you are still using WSL1, see
     [Upgrade version from WSL1 to WSL2](https://learn.microsoft.com/en-us/windows/wsl/install#upgrade-version-from-wsl-1-to-wsl-2)

## Enabling WSL

1. Open 'Turn Windows features on or off'  
    ![WSL1.png](Windows_Subsystem_for_Linux_WSL.png)
2. Scroll down and tick the 'Windows Subsystem for Linux' option.  
    ![WSL2.png](Windows_Subsystem_for_Linux_WSL_0.png)
  
    And click OK

3. Wait for the installation to finish then restart your computer.

## Installing a Distribution

In order to make use of WSL features, you will also need to install a Linux distribution.

Distributions can be obtained through the Microsoft Store, or using command line.

=== "Using The Microsoft Store"
     - Open the Microsoft store, search for 'Ubuntu', find and install the
     latest version of the Ubuntu LTS it should look something like
     'Ubuntu 20.04 LTS' , though you may find a later version.

     ![MS store](Ubuntu_LTS_terminal_Windows.png)
     ![MS store](Ubuntu_LTS_terminal_Windows_0.png)  
          
     - Close the “Add your Microsoft account.. dialogue box as you do not
     need an account for the installation.You may have to click “Install”
     for a second time (If the above dialogue box reappears, close as
     before and download/install will begin).
     
     ![MS store](Ubuntu_LTS_terminal_Windows_1.png)
     ![MS store](Ubuntu_LTS_terminal_Windows_2.png)
=== "Using Command Line"
     - Open 'Windows Power Shell' and type

     ```ps
     wsl --install -d Ubuntu-20.04
     ```
  
- When it has finished downloading, the Ubuntu Terminal will appear and prompt you to “Enter new UNIX username”
    and press <kbd>Enter</kbd>.
  
    This can be anything you want, although we reccomend using the same as your Windows username.
    ![ubuntu1.png](Ubuntu_LTS_terminal_Windows_3.png)
  
- Now, type in a new password for the username you picked and press
    <kbd>Enter</kbd> (this password can be anything you want, although you shouldn't need to enter it again).
    Then retype the password to confirm and press <kbd>Enter</kbd>.
    ![ubuntu2.png](Ubuntu_LTS_terminal_Windows_4.png)

## Creating a Symlink (optional)

You may find having a symbolic link to your Windows filesystems useful.

Within Ubuntu terminal run the following command replacing c with the name of
your Windows filesystems found in /mnt/.

```sh
ln -s /mnt/c/Users/YourWindowsUsername/ WinFS
```

!!! prerequisite What "Next?"
     -   Set up your [SSH config file](Standard_Terminal_Setup.md).
