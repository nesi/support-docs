[SSHFS](https://github.com/libfuse/sshfs) allows you to mount a remote
filesystem on your local machine. SSHFS relies on SSH underneath, so you
should follow the \"Recommended logon procedure\" instructions
[here](https://support.nesi.org.nz/hc/en-gb/articles/360000161315-Logging-in-to-the-HPCs)
to configure SSH first.

Linux {#toc_1}
-----

Use the following commands to mount your home directory from Mahuika on
your local machine (the same command will work for Māui, just replace
the names):

<div>

    # create a mount point and connect
    mkdir -p ~/mahuika-home
    sshfs -oauto_cache,follow_symlinks mahuika: ~/mahuika-home

</div>

Now you should be able to navigate to \"\~/mahuika-home\" on your local
machine to access your home directory on Mahuika. To unmount the
directory run:

<div>

    fusermount -u ~/mahuika-home

</div>

To mount a project directory, you could run:

<div>

    # create a mount point and connect
    mkdir -p ~/mahuika-project
    sshfs -oauto_cache,follow_symlinks mahuika:/nesi/project/nesiXXXXX ~/mahuika-project

</div>

MacOS {#toc_2}
-----

We recommend using some extra options with MacOS. The following commands
will mount your home directory, make it show up under devices in Finder
and give the volume a sensible name:

<div>

    # create a mount point and connect
    mkdir -p ~/mahuika-home
    sshfs mahuika: ~/mahuika-home \
        -oauto_cache,follow_symlinks \
        -ovolname=MahuikaHome,defer_permissions,noappledouble,local 

</div>

To unmount the directory on MacOS, either eject from Finder or run:

<div>

    umount ~/mahuika-home

</div>
