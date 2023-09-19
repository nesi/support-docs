---
created_at: '2018-11-26T03:03:23Z'
hidden: false
label_names: []
position: 3
title: WinSCP/PuTTY Setup (Windows)
vote_count: 3
vote_sum: 1
zendesk_article_id: 360000584256
zendesk_section_id: 360000189696
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    !!!
>
> -   Have an [active account and
>     project.](https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects)
> -   Set up your [NeSI account
>     password.](https://support.nesi.org.nz/hc/en-gb/articles/360000335995)
> -   Set up Second [Factor
>     Authentication.](https://support.nesi.org.nz/hc/en-gb/articles/360000203075)
> -   Be using the Windows operating system.

 

WinSCP is an SCP client for windows implementing the SSH protocol from
PuTTY.

WinSCP can be downloaded [here](https://winscp.net/eng/download.php).

Upon startup:

![WinSCP1.png](assets/images/WinSCP1_1.png)

1. Add a *New Site* and set:

-   Enter in *Host Name: *login.mahuika.nesi.org.nz or
    login.maui.nesi.org.nz
-   Enter your NeSI account username into *User name:* (Password
    optional)
!!!
>
> For "file protocol" (the topmost drop-down menu), either SCP or SFTP
> is acceptable. If you are trying to move many small files or have a
> slow or flaky Internet connection, you may find that SFTP performs
> better than SCP. Feel free to try both and see which works best for
> you.

  
![WinSCP2.png](assets/images/WinSCP2_1.png)

5\. Open Advanced Settings.

![WinSCP3.png](assets/images/WinSCP3_1.png)

6\. Navigate to *Connection &gt; Tunnel *and set:

-   Enable "Connect through SSH tunnel".
-   Under "Host name:" enter lander.nesi.org.nz
-   Under "User name:" enter your username.
-   Optionally, enter your password in the "Password:" box.

10\. *OK &gt; Save*

## Setup for PuTTY Terminal

The default WinSCP terminal lacks much functionality. We highly
recommend you use the PuTTY terminal instead.

1\. Download PuTTY [here](https://www.putty.org/) and install.

2.In WinSCP open 'Tools &gt; Preferences'

![WinSCP2-5.png](assets/images/WinSCP2-5_1.png)

3\. Under *Integration &gt; Applications* enable *Remember session
password and pass it to PuTTY*

![WinSCP4.png](assets/images/WinSCP4_1.png)

 

## Setup for Xming (Optional)

Xming is an X server for Windows allowing graphical interface with the
HPC and can be downloaded
[here](https://sourceforge.net/projects/xming/).

1\. Install Xming following the prompts. (Make sure 'Normal PuTTY Link
SSH Client' is selected).

2\. Under *Integration &gt; Applications* and add -X after
PuTTY/Terminal client path.

*![WinSCP6.png](assets/images/WinSCP6_1.png)*

3\. Restart your session.
!!!
>
> In order for X11 forwarding to work you must have an Xming server
> running before connecting to the HPC.

# Usage

Files can be dragged, dropped and modified in the WinSCP GUI just like
in any windows file system.

![WinSCP5.png](assets/images/WinSCP5_1.png)

![putTerm.png](assets/images/putTerm_1.png) Will open a **PuTTY
terminal**. Assuming you followed the steps setting up PuTTY, this
should automatically enter in your details.

![winTerm.png](assets/images/winTerm_1.png) Will open the default
**WinSCP terminal**. While the functionality is identical to any other
terminal the interface is slightly abstracted, with a separate window
for input and command history drop-down.

![winAdd.png](assets/images/winAdd_1.png) Type here to **change
directory**.** **The GUI doesn't follow your current terminal directory
like MobaXterm so must be changed manually. (Recommend making this
larger as the default is very hard to type in).

![winBook.png](assets/images/winBook_1.png) **Bookmark** current
directory.
!!!
>
> As WinSCP uses multiple tunnels for file transfer you will be required
> to authenticate again on your first file operation of the session. The
> second prompt for your second-factor token can be skipped, just as
> with login authentication.
!!!
>
> -   [Moving files to/from a
>     cluster.](https://support.nesi.org.nz/hc/en-gb/articles/360000578455)
> -   Setting up
>     an [X-Server](https://support.nesi.org.nz/hc/en-gb/articles/360001075975)
>     (optional).
