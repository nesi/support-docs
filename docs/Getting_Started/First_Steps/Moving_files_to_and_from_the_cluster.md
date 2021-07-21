> ### Requirements {#prerequisites}
>
> -   Have an [active account and
>     project.](https://support.nesi.org.nz/hc/en-gb/sections/360000196195-Accounts-Projects)
> -   Have a [SSH connection to a NeSI
>     cluster](https://support.nesi.org.nz/hc/en-gb/articles/360001016335),
>     and [set up as
>     recommended.](https://support.nesi.org.nz/hc/en-gb/sections/360000189696)

Find more information on the different types of directories
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000177256).

Standard Terminal
=================

In a local terminal the following commands can be used to:

Move a file from your local machine to Mahuika.

    scp <path/filename> mahuika:<path/filename>

Move a file from Mahuika to your local machine.

    scp mahuika:<path/filename> <path/filename>

> ### Note
>
> -   This will only work if you have set up aliases as described in
>     [Terminal
>     Setup](https://support.nesi.org.nz/hc/en-gb/articles/360000625535-Terminal-Setup-MacOS-Linux-).
> -   As the terms \'maui\' and \'mahuika\' are defined locally, the
>     above commands *only works when using a local terminal* (i.e. not
>     on Mahuika).
> -   If you are using Windows subsystem, the root paths are different
>     as shown by Windows. e.g. `C:` is located at `/mnt/c/`

`scp` stands for Secure CoPy and operates in a similar way to regular cp
with the source file as the left term and destination on the right.

These commands make use of *multiplexing, *this means that if you
already have a connection to the cluster you will not be prompted for
your password.

File Managers 
--------------

Most file managers can be used to connect to a remote directory simply
by typing in the address bar (provided your have an active connection to
the cluster and your ssh config file is set up as described
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000625535)).

For Nautilus (Ubuntu default) just prepend the path you want to connect
to with `sftp://mahuika`. (ctrl + L opens address bar)

This does not work for File Explorer (Windows default)

This does not work for Finder (Mac default)

![mceclip0.png](https://support.nesi.org.nz/hc/article_attachments/360003129656/mceclip0.png)

If your default file manager does not support mounting over sftp, see
our documentation
on [SSHFS](https://support.nesi.org.nz/hc/en-gb/articles/360000621135).

MobaXterm
=========

Clicking the \"*Scp*\" tab (located on the left-hand side of the
MobaXTerm window) opens up a graphical user interface that can be used
for basic file operations. You can drag and drop files in the file
explorer or use the up and down arrows on the toolbar to upload and
download files.

![2019-01-07\_SCP\_in\_MobaXTerm.png](https://support.nesi.org.nz/hc/article_attachments/360001503115/2019-01-07_SCP_in_MobaXTerm.png)

You may also transfer files as described under \'Standard Terminal\'
(provided
[WSL](https://support.nesi.org.nz/hc/en-gb/articles/360001075575) is
enabled).

WinSCP
======

As WinSCP uses multiple tunnels for file transfer you will be required
to authenticate again on your first file operation of the session. The
second prompt for your 2FA can be skipped, just the same as with login
authentication.

 

 

 

 
