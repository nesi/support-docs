> ### Requirements {#prerequisites}
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

::: {container=""}
WinSCP can be downloaded [here](https://winscp.net/eng/download.php).

Upon startup:

![WinSCP1.png](https://support.nesi.org.nz/hc/article_attachments/360001342295/WinSCP1.png)

1. Add a *New Site* and set:

-   Enter in *Host Name: *[login.mahuika.nesi.org.nz]{.kbd} or
    [login.maui.nesi.org.nz]{.kbd}
-   Enter your NeSI account username into *User name:* (Password
    optional)

> ### Tip {#llama-tip}
>
> For \"file protocol\" (the topmost drop-down menu), either SCP or SFTP
> is acceptable. If you are trying to move many small files or have a
> slow or flaky Internet connection, you may find that SFTP performs
> better than SCP. Feel free to try both and see which works best for
> you.

\
![WinSCP2.png](https://support.nesi.org.nz/hc/article_attachments/360001342315/WinSCP2.png)

5\. Open Advanced Settings.

![WinSCP3.png](https://support.nesi.org.nz/hc/article_attachments/360002834335/WinSCP3.png)

6\. Navigate to *Connection \> Tunnel *and set:

-   Enable \"Connect through SSH tunnel\".
-   Under \"Host name:\" enter [lander.nesi.org.nz]{.kbd}
-   Under \"User name:\" enter your username.
-   Optionally, enter your password in the \"Password:\" box.

10\. *OK \> Save*

Setup for PuTTY Terminal
------------------------

The default WinSCP terminal lacks much functionality. We highly
recommend you use the PuTTY terminal instead.

1\. Download PuTTY [here](https://www.putty.org/) and install.

2.In WinSCP open \'Tools \> Preferences\'

![WinSCP2-5.png](https://support.nesi.org.nz/hc/article_attachments/360001342495/WinSCP2-5.png)

3\. Under *Integration \> Applications* enable *Remember session
password and pass it to PuTTY*

![WinSCP4.png](https://support.nesi.org.nz/hc/article_attachments/360001344315/WinSCP4.png)

 

Setup for Xming (Optional) {#x_ming}
--------------------------

Xming is an X server for Windows allowing graphical interface with the
HPC and can be downloaded
[here](https://sourceforge.net/projects/xming/).

1\. Install Xming following the prompts. (Make sure \'Normal PuTTY Link
SSH Client\' is selected).

2\. Under *Integration \> Applications* and add -X after PuTTY/Terminal
client path.

*![WinSCP6.png](https://support.nesi.org.nz/hc/article_attachments/360001596916/WinSCP6.png)*

3\. Restart your session.

> ### Important {#prerequisites}
>
> In order for X11 forwarding to work you must have an Xming server
> running before connecting to the HPC.

Usage
=====

Files can be dragged, dropped and modified in the WinSCP GUI just like
in any windows file system.

![WinSCP5.png](https://support.nesi.org.nz/hc/article_attachments/360001494615/WinSCP5.png)

![putTerm.png](https://support.nesi.org.nz/hc/article_attachments/360001597336/putTerm.png) Will
open a **PuTTY terminal**. Assuming you followed the steps setting up
PuTTY, this should automatically enter in your details.

![winTerm.png](https://support.nesi.org.nz/hc/article_attachments/360001597316/winTerm.png) Will
open the default **WinSCP terminal**. While the functionality is
identical to any other terminal the interface is slightly abstracted,
with a separate window for input and command history drop-down.

![winAdd.png](https://support.nesi.org.nz/hc/article_attachments/360001494635/winAdd.png) Type
here to **change directory**.** **The GUI doesn\'t follow your current
terminal directory like MobaXterm so must be changed
manually. (Recommend making this larger as the default is very hard to
type in).

![winBook.png](https://support.nesi.org.nz/hc/article_attachments/360001599556/winBook.png) **Bookmark**
current directory.

> ### Important {#prerequisites}
>
> As WinSCP uses multiple tunnels for file transfer you will be required
> to authenticate again on your first file operation of the session. The
> second prompt for your second-factor token can be skipped, just as
> with login authentication.

> ### What Next? {#prerequisites}
>
> -   [Moving files to/from a
>     cluster.](https://support.nesi.org.nz/hc/en-gb/articles/360000578455)
> -   Setting up
>     an [X-Server](https://support.nesi.org.nz/hc/en-gb/articles/360001075975)
>     (optional).
:::
