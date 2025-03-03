---
created_at: '2018-11-20T22:41:32Z'
tags:
- scp
- transfer
- copying
- download
- upload
- mv
- cp
- move
- moving
vote_count: 11
vote_sum: 3
---

!!! prerequisite
    Have an [active account and project.](../Mahuika_Cluster/Next_Steps/Creating_a_NeSI_Account_Profile.md)

Find more information on [the NeSI Filesystem](../Mahuika_Cluster/Next_Steps/NeSI_File_Systems_and_Quotas.md).

## Using the Jupyter interface

The [Jupyter interface](../Mahuika_Cluster/Next_Steps/Jupyter_on_NeSI.md)
useful for running code on NeSI requiring only a web browser; the instructions are same whether your are
connecting from a Windows, Mac or a Linux computer.

To upload a file, click on the

![up arrow](../Mahuika_Cluster/Next_Steps/Moving_files_to_and_from_the_cluster.png)

button, near the top left and generally under the Run button.

To download a file, navigate the file browser on the left and
right-click on the file to see the menu below,

![right click menu](../Mahuika_Cluster/Next_Steps/Moving_files_to_and_from_the_cluster_0.png)

The Download button is at the bottom.

## Standard Terminal

!!! prerequisite
    Have SSH setup as described in [Standard Terminal Setup](../Mahuika_Cluster/Next_Steps/Standard_Terminal_Setup.md)

In a local terminal the following commands can be used to:

Move a file from your local machine to Mahuika.

```bash
scp <path/filename> mahuika:<path/filename>
```

Move a file from Mahuika to your local machine.

```bash
scp mahuika:<path/filename> <path/filename>
```

!!! note
    - This will only work if you have set up aliases as described in
      [Terminal Setup](../Mahuika_Cluster/Next_Steps/Standard_Terminal_Setup.md).
    - As the terms 'maui' and 'mahuika' are defined locally, the above
      commands *only works when using a local terminal* (i.e. not on Mahuika).
    - If you are using Windows subsystem, the root paths are different
      as shown by Windows. e.g. `C:` is located at `/mnt/c/`

`scp` stands for Secure CoPy and operates in a similar way to regular cp
with the source file as the left term and destination on the right.

These commands make use of *multiplexing*, this means that if you
already have a connection to the cluster you will not be prompted for
your password.

## File Managers

!!! prerequisite
    Have SSH setup as described in [Standard Terminal Setup](Standard_Terminal_Setup.md)

Most file managers can be used to connect to a remote directory simply
by typing in the address bar provided your have an active connection to
the cluster.

For Nautilus (Ubuntu default) just prepend the path you want to connect
to with `sftp://mahuika`. (ctrl + L opens address bar)

This **does not** work for File Explorer (Windows default)

This **does not** work for Finder (Mac default)

![files](../Mahuika_Cluster/Next_Steps/Moving_files_to_and_from_the_cluster_1.png)

If your default file manager does not support mounting over SFTP, see
[Can I use SSHFS to mount the cluster filesystem on my local machine?](../Mahuika_Cluster/Next_Steps/Can_I_use_SSHFS_to_mount_the_cluster_filesystem_on_my_local_machine.md).

## MobaXterm

!!! prerequisite
    [MobaXterm Setup Windows](../Mahuika_Cluster/Next_Steps/MobaXterm_Setup_Windows.md)

Clicking the "*Scp*" tab (located on the left-hand side of the  
window) opens up a graphical user interface that can be used for basic
file operations. You can drag and drop files in the file explorer or use
the up and down arrows on the toolbar to upload and download files.

![moba terminal](../Mahuika_Cluster/Next_Steps/Moving_files_to_and_from_the_cluster_2.png)

You may also transfer files as described under 'Standard Terminal'
(provided
[Windows_Subsystem_for_Linux](../Mahuika_Cluster/Next_Steps/Windows_Subsystem_for_Linux_WSL.md)
is enabled).

## WinSCP

!!! prerequisite
    [WinSCP-PuTTY Setup Windows](../Mahuika_Cluster/Next_Steps/WinSCP-PuTTY_Setup_Windows.md)

As WinSCP uses multiple tunnels for file transfer you will be required
to authenticate again on your first file operation of the session. The
second prompt for your 2FA can be skipped, just the same as with login
authentication.

## Globus

Globus is available for those with large amounts of data, security
concerns, or connection consistency issues.
You can find more details in
[Data_Transfer_using_Globus_V5](../Mahuika_Cluster/Next_Steps/Data_Transfer_using_Globus_V5.md).

## Rclone

Rclone is available for those that need to transfer data from cloud
storage services like Google drive or OneDrive.

The basic command syntax of Rclone:

```bash
rclone subcommand options source:path dest:path
```

The most frequently used Rclone subcommands:

- `rclone copy` - Copy files from the source to the destination, skipping what has already been copied.
- `rclone sync` - Make the source and destination identical, modifying only the destination.
- `rclone move` - Move files from the source to the destination.
- `rclone delete` - Remove the contents of a path.

A more extensive list can be found in the [Rclone documentation](https://rclone.org/docs).

## Rsync

Rsync is an utility that provides fast incremental file transfer and
efficient file synchronization between a computer and a storage disk.
The basic command syntax of:

```bash
rsync -options source target
```

If the data source or target location is a remote site, it is defined
with syntax:

```txt
userame@server:/path/in/server
```

The most frequently used Rsync options:

- `-r` - Recurse into directories.
- `-a` - Use archive mode: copy files and directories recursively and preserve access permissions and time stamps.
- `-z` - Compress.
- `-e ssh` - Specify the remote shell to use.
- `-n` - Show what files would be transferred.

A more extensive list can be found in the [Rsync documentation](https://download.samba.org/pub/rsync/rsync.1).
