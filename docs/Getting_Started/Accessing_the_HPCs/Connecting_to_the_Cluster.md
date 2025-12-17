---
created_at: '2019-06-25T22:40:46Z'
tags:
- terminal
- mobaxterm
- gitbash
- login
---

!!! prerequisite
    -  Have an [active account and project](../Creating_an_Account.md).

Before you can start submitting work you will need to connect to the cluster. This is done by establishing a connection using a web browser (easy) or a command-line terminal and SSH (more advanced).

## Web Browser (Recommended)

### NeSI OnDemand

__OnDemand__ is a service providing access to Jupyter Notebooks, RStudio, VSCode, a Virtual Desktop, a terminal and other applications, allowing you to utilise cluster resources via the browser.

!!! tip "What next?"
    -  More info on
       [NeSI OnDemand](../../Interactive_Computing/OnDemand/how_to_guide.md)
    -  Visit [ondemand.nesi.org.nz](https://ondemand.nesi.org.nz/).

## Linux or MacOS

### Terminal

MacOS & Linux have a default terminal emulator installed. On both it is called: _Terminal_. Start the terminal and you are ready to move to the next step.

!!! prerequisite "What next?"
    Setting up your [Default Terminal](Standard_Terminal_Setup.md)

### VSCode 

The 'remotes' plugin allows connecting to remote hosts using SSH.
If you have set up your `~/.ssh/config` as described in [Standard_Terminal_Setup](Standard_Terminal_Setup.md),
VSCode will detect this and show configured hosts in the 'Remote Explorer' Tab.

## MS Windows

There are several options for connecting to the cluster using SSH from Windows. Below are our recommendations in order: 

### Windows Subsystem for Linux (WSL)

 The Windows Subsystem for Linux is our top recommendation since it will provide the most functionality.  WSL may require administrative privileges to enable and install.  If you are not allowed to enable and install, contact your local IT team. If your institution will not allow WSL to be installed, consider using another option see below.

!!! tip "What next?"
    Setting up [WSL](Windows_Subsystem_for_Linux_WSL.md) 

### VSCode 

The 'remotes' plugin allows connecting to remote hosts. A detailed description and options for VSCode Remote development can be found [on this website](https://code.visualstudio.com/docs/remote/ssh) 
VSCode can be used with WSL but WSL is not a requirement. 

### MobaXterm

 In addition to being a terminal emulator, MobaXterm also includes
 several useful features like multiplexing, X11 forwarding and a file
 transfer GUI.

 MobaXterm can be downloaded from
 [mobaxterm.mobatek.net](https://mobaxterm.mobatek.net/download-home-edition.html).
 The portable edition will allow you to use MobaXterm without needing
 administrator privileges, however it introduces several bugs so we
 *highly* recommend using the installer edition if you have
 administrator privileges on your workstation or if your
 institution's IT team supports MobaXTerm.
!!! tip "What next?"
    -  Setting up
       [MobaXterm](MobaXterm_Setup_Windows.md)

### Git Bash

If you are using Git for version control you may already have Git
Bash installed. If not it can be downloaded
from [git-scm.com](https://git-scm.com/downloads).

Git Bash is perfectly adequate for testing your login or setting up
your password, but lacks many of the features of MobaXterm or a
native Unix-Like terminal. Therefore we do not recommend it as your
primary terminal.

### WinSCP

WinSCP has some advantages over MobaXterm (customisable, cleaner
interface, open source), and some disadvantages (no built in
X-server, additional authentication step). However, WinSCP setup is
more involved than with MobaXterm, therefore we do not recommend it
for new users.

!!! tip "What next?"
    -  Setting up
       [WinSCP](WinSCP-PuTTY_Setup_Windows.md)

