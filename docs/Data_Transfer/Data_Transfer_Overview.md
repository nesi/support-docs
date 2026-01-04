---
created_at: '2018-11-20T22:41:32Z'
title: Introduction to Data Transferring
---

!!! prerequisite
    Have an [active account and project.](../Getting_Started/Creating_an_Account.md)

There are several ways to transfer your data between the Mahuika Supercomputer and your computer or server.

!!! tip
    **Read [data transfer best practises](./Data_Transfer_Best_Practices.md) before moving data to and from Mahuika.**

For simple, graphical user interface options, see:

* [Moving data with OnDemand](./Data_Transfer_Using_OnDemand.md)
* [Moving data using VSCode](./VSCode.md)

For file transfer methods that use the terminal, see:

* [scp (Secure Copy)](./SCP.md)
* [rsync](./Rsync.md)
* [RClone](./RClone.md)

If you are transferring large files or a large amount of files, see:

* [FileSender](./FileSender.md)
* [Globus](./Globus/Overview.md)

For transferring data using specific tools, see:

* [File transferring using MobaXterm (Windows)](./Data_Transfer_Using_MobaXterm.md)
* [File transferring using WinSCP (Windows)](./Data_Transfer_Using_WinSCP.md)
* [Setting up a File Manager on your computer (Ubuntu)](./File_Managers.md)

Find more information on [our filesystem](../Storage/File_Systems_and_Quotas/Filesystems_and_Quotas.md).

## Best Practice
### Avoid Transferring Temporary Files

It is best to avoid transferring temporary files. This is because temporary files:

1. Can take up a large amount of space and contain a huge number of files.
2. Are only used *temporarily* by the program that creates it and then not used again, so are not needed.

It is recommended that before you transfer files that you either **delete all temporary files** or **avoid transferring temporary files**, it will take longer for your files to transfer and take up unnecessary space on your host drive.

Transferring lots of files using Globus can also have detrimental effects on this service. Avoid transferring temporary files when using Globus.

### Compress Large Files

Write something here

### Use Checksums

[checksums](Checksums.md)
