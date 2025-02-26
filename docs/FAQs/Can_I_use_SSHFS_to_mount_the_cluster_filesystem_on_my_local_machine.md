---
created_at: '2018-11-27T23:55:26Z'
tags: []
title: Can I use SSHFS to mount the cluster filesystem on my local machine?
vote_count: 5
vote_sum: 3
zendesk_article_id: 360000621135
zendesk_section_id: 360000039036
---

[SSHFS](https://github.com/libfuse/sshfs) allows you to mount a remote
filesystem on your local machine. SSHFS relies on SSH underneath, so you
should follow the "Recommended logon procedure" instructions
[here](Choosing_and_Configuring_Software_for_Connecting_to_the_Clusters.md) to configure SSH
first.

## Linux

Use the following commands to mount your home directory from Mahuika on
your local machine:

```sh
# create a mount point and connect
mkdir -p ~/mahuika-home
sshfs -oauto_cache,follow_symlinks mahuika: ~/mahuika-home
```

Now you should be able to navigate to "~/mahuika-home" on your local
machine to access your home directory on Mahuika. To unmount the
directory run:

```sh
fusermount -u ~/mahuika-home
```

To mount a project directory, you could run:

```sh
# create a mount point and connect
mkdir -p ~/mahuika-project
sshfs -oauto_cache,follow_symlinks mahuika:/nesi/project/nesiXXXXX ~/mahuika-project
```

## MacOS

We recommend using some extra options with MacOS. The following commands
will mount your home directory, make it show up under devices in Finder
and give the volume a sensible name:

```sh
# create a mount point and connect
mkdir -p ~/mahuika-home
sshfs mahuika: ~/mahuika-home \
    -oauto_cache,follow_symlinks \
    -ovolname=MahuikaHome,defer_permissions,noappledouble,local 
```

To unmount the directory on MacOS, either eject from Finder or run:

```sh
umount ~/mahuika-home
```

!!! note
     Newer MacOS does not come with SSHFS pre installed. You will have to
     install FUSE as SSHFS from [here](https://osxfuse.github.io/).
