---
created_at: '2018-11-20T22:41:32Z'
---

!!! prerequisite
    Have an [active account and project.](../Getting_Started/Creating_an_Account.md)

There are several ways to transfer your data between the Mahuika Supercomputer and your computer or server.

For simple, graphical user interface options without requiring additional setup, see:

* [Moving data with OnDemand](./Data_Transfer_Using_OnDemand.md)

!!! warning
    OnDemand interface is not suitable for large data transfers or automated workflows.

For file transfer methods that use the terminal, see:

* [SCP (Secure Copy)](./SCP.md), the default method, SCP is pre-installed on all versions of Mac, Linux and WSL.
* [Rsync](./Rsync.md), for larger and more complex data moving operations providing additional features over SCP.

For transferring files from other remote endpoints (i.e. not your local computer), see:

* [RClone](./RClone.md),
* [FileSender](./FileSender.md) <WHY USE THIS OVER RClone??>
* [Globus](./Globus/Overview.md) <WHY USE THIS OVER FILESENDER??>

For transferring data using specific tools, see:

* [File transfer using MobaXterm (Windows)](./Data_Transfer_Using_MobaXterm.md)
* [File transfer using WinSCP (Windows)](./Data_Transfer_Using_WinSCP.md)
* [Connecting with the default file manager (Ubuntu)](./File_Managers.md)
* [Moving data using VSCode](./VSCode.md)

!!! info
    Find more information on [our filesystem](../Storage/File_Systems_and_Quotas/Filesystems_and_Quotas.md).

## Best Practice

### Avoid Transferring Temporary Files

<ELABORATE ON WHAT ARE TEMPORARY FILES>

It is best to avoid transferring temporary files. This is because temporary files:

1. Can take up a large amount of space and contain a huge number of files.
2. Are only used *temporarily* by the program that creates it and then not used again, so are not needed.

It is recommended that before you transfer files that you either **delete all temporary files** or **avoid transferring temporary files**, it will take longer for your files to transfer and take up unnecessary space on your host drive.

Transferring lots of files using Globus can also have detrimental effects on this service. Avoid transferring temporary files when using Globus.

### Compress Large Files

Write something here

### Use Checksums

Write something here

[checksums](Checksums.md)
