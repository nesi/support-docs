# File Managers

!!! prerequisite
    Have SSH setup as described in [Standard Terminal Setup](../Getting_Started/Accessing_the_HPCs/Standard_Terminal_Setup.md)

Most file managers can be used to connect to a remote directory simply
by typing in the address bar provided your have an active connection to
the cluster.

For Nautilus (Ubuntu default) just prepend the path you want to connect
to with `sftp://mahuika`. (ctrl + L opens address bar)

This **does not** work for File Explorer (Windows default)

This **does not** work for Finder (Mac default)

![files](../assets/images/Moving_files_to_and_from_the_cluster_1.png)

If your default file manager does not support mounting over SFTP, see
[Can I use SSHFS to mount the cluster filesystem on my local machine?](../Getting_Started/FAQs/Can_I_use_SSHFS_to_mount_the_cluster_filesystem_on_my_local_machine.md).
