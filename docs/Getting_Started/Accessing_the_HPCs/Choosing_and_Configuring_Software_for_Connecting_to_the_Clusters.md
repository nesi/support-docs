---
created_at: '2019-06-25T22:40:46Z'
hidden: false
position: 2
tags:
- terminal
- mobaxterm
- gitbash
- login
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001016335
zendesk_section_id: 360000034315
---

!!! prerequisite
     -   Have an [active account and
         project](https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects).
     -   Set up your [NeSI Account
         Password](https://support.nesi.org.nz/hc/en-gb/articles/360000335995).
     -   Set up [Two-Factor
         Authentication](https://support.nesi.org.nz/hc/en-gb/articles/360000203075).

Before you can start submitting work you will need some way of
connecting to the NeSI clusters.

This is done by establishing an SSH (Secure SHell) connection, giving
you access to a command line interface (bash) on the cluster. In order
to set up such a connection, you will need a suitable Terminal (or
equivalent application). The correct option for you depends on your
operating system and level of experience.

## Web Browser

### JupyterHub

JupyterHub is a service providing access to Jupyter Notebooks on
NeSI. A terminal similar to the other setups describe below can be
accessed through the Jupyter Launcher.

!!! tip "What next?"
    More info on [Jupyter Terminal](https://support.nesi.org.nz/hc/en-gb/articles/360001555615#jupyter-term) Visit [jupyter.nesi.org.nz](https://jupyter.nesi.org.nz/hub/).

## Linux or Mac OS

### Terminal

    On MacOS or Linux you will already have a terminal emulator
    installed, usually called, "Terminal." To find it, simply search for
    "terminal".  
    Congratulations! You are ready to move to the next step.

!!! tip "What next?"
    - Setting up your [Default Terminal](https://support.nesi.org.nz/hc/en-gb/articles/360000625535)

## Windows

As Windows is not a "Unix-Like" operating system, getting access to a
functional terminal requires some additional steps. There are several
different options, listed in order of preference.

### Ubuntu Terminal (Windows 10)

The Ubuntu Terminal and Windows Subsystem for Linux require
administrative privileges to enable and install them. If your
institution has not given you such privileges, consider using
another option such as MobaXTerm Portable Edition (see below).

This is the most functional replication of a Unix terminal available
on Windows, and allows users to follow the same set of instructions
given to Mac/Linux users. It may be necessary to enable Windows
Subsystem for Linux (WSL) first.

!!! tip "What next?"
    - Enabling [WSL](https://support.nesi.org.nz/hc/en-gb/articles/360001075575).
    - Setting up the [UbuntuTerminal](https://support.nesi.org.nz/hc/en-gb/articles/360001050575).
    - Setting up [X-Forwarding](https://support.nesi.org.nz/hc/en-gb/articles/4407442866703).

### MobaXterm

    In addition to being a terminal emulator, MobaXterm also includes
    several useful features like multiplexing, X11 forwarding and a file
    transfer GUI.

    MobaXterm can be downloaded from
    [here](https://mobaxterm.mobatek.net/download-home-edition.html).
    The portable edition will allow you to use MobaXterm without needing
    administrator privileges, however it introduces several bugs so we
    *highly* recommend using the installer edition if you have
    administrator privileges on your workstation or if your
    institution's IT team supports MobaXTerm.

!!! tips "What next?"
    Setting up [MobaXterm](https://support.nesi.org.nz/hc/en-gb/articles/360000624696)

### Using a Virtual Machine

    In order to avoid the problems of using a Windows environment, it
    may be advisable to install a Linux Virtual machine. This may be
    advantageous in other ways as many elements of scientific computing
    require a Linux environment, also it can provide a more user
    friendly place to become familiar with command line use.

    There are multiple free options when it comes to VM software. We
    recommend [Oracle
    VirtualBox](https://www.virtualbox.org/wiki/Downloads).

    Further instructions on how to set up a virtual machine can be found
    [here](https://blog.storagecraft.com/the-dead-simple-guide-to-installing-a-linux-virtual-machine-on-windows/).

    Once you have a working VM you may continue following the
    instructions as given for
    [Linux/MacOS](#h_c1bbd761-1133-499b-a61a-57b9c4320a1a).

!!! tips "What next?"
    Setting up a [VirtualMachine](https://blog.storagecraft.com/the-dead-simple-guide-to-installing-a-linux-virtual-machine-on-windows/)

### WinSCP

    WinSCP has some advantages over MobaXterm (customisable, cleaner
    interface, open source), and some disadvantages (no built in
    X-server, additional authentication step). However, WinSCP setup is
    more involved than with MobaXterm, therefore we do not recommend it
    for new users.

!!! tips "What next?"
    Setting up [WinSCP](https://support.nesi.org.nz/hc/en-gb/articles/360000584256)

### Git Bash

    If you are using Git for version control you may already have Git
    Bash installed. If not it can be downloaded
    from [here](https://git-scm.com/downloads).

    Git Bash is perfectly adequate for testing your login or setting up
    your password, but lacks many of the features of MobaXterm or a
    native Unix-Like terminal. Therefore we do not recommend it as your
    primary terminal.

### Windows PowerShell

    All Windows computers have PowerShell installed, however it will
    only be useful to you if Windows Subsystem for Linux (WSL) is also
    enabled, instructions
    [here](https://support.nesi.org.nz/hc/en-gb/articles/360001075575).

    Like Git Bash, PowerShell is perfectly adequate for testing your
    login or setting up your password, but lacks many of the features of
    MobaXterm or a native Unix-Like terminal. Therefore we do not
    recommend it as your primary terminal.
