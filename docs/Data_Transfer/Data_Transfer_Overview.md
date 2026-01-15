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

* [RClone](./RClone.md)
* [FileSender](./FileSender.md) <WHY USE THIS OVER RClone??>
* [Globus](./Globus/Overview.md) <WHY USE THIS OVER FILESENDER??>

For transferring data using specific tools, see:

* [File transfer using MobaXterm (Windows)](./Data_Transfer_Using_MobaXterm.md)
* [File transfer using WinSCP (Windows)](./Data_Transfer_Using_WinSCP.md)
* [Connecting with the default file manager (Ubuntu)](./File_Managers.md)
* [Moving data using VSCode](./VSCode.md)

!!! info
    Find more information on [our filesystem](../Storage/File_Systems_and_Quotas/Filesystems_and_Quotas.md).

## Data Transfer Best Practices

### Avoid Transferring Temporary Files

Temporary files are files that are created by a program while it is running. This may be to hold information that may be needed later, to hold memory that is too big to hold in memory (RAM), or are used for checkpointing. Temporary files are only needed by a program while it is running. Once a program has finished successfully, they can be removed. These may have file names ending with `.tmp` or `.temp`.

It is best to avoid transferring temporary files. This is because temporary files:

1. Can take up a large amount of space and contain a huge number of files.
2. Are only used *temporarily* by the program that created it and then not used again, so are not needed ever again.

It is recommended that before you transfer files that you either **delete all temporary files** or **avoid transferring temporary files**, as it will take longer for your files to transfer and take up unnecessary space on your host drive.

* Transferring lots of files using Globus in particular can also have detrimental effects on this service. Avoid transferring temporary files when using Globus.

### Avoid Transferring lots of Small Files

Whenever you transfer a file, a small amount of time is required to prepare the file for transfer. This is fine if you are only transferring a small number of files, or are transferring large data files where most of the time will be spent actually transferring the file. However, **if you transfer a large number of small files**, this preparation time grows significantly, **hindering the speed of your transfer**.

If you need to transfer lots of small files, it is best practice to **first tarball or zip your files before transferring them**. This will collect all your files into one file that is easier for file transfer.

To do this:

1. Tarball the folder containing your files to transfer (you can compress the tarball or leave it uncompressed):

    ```sh
    tar -cvf tarball_file.tar folder_to_tarball # Uncompressed Mode
    # or
    tar -czvf tarball_file.tar folder_to_tarball # Compressed Mode
    ```

2. Transfer the tarball file using a file transfer method.

3. Untarball the tarball containing your files:

    ```sh
    tar -xvf tarball_file.tar # Uncompressed Mode
    # or
    tar -xzvf tarball_file.tar # Compressed Mode
    ```

!!! tip
    To prevent running out of space on your `project` directory, create your tarballs in your `nobackup` directory.

    If you are running out of space in your `project` and `nobackup` directories, feel free to [get in touch with us](mailto:support@nesi.org.nz) and we can work with you to help transfer your files.

### Compress Large Files

Large files can take a long time to transfer. In some cases these large files can be compressed, minimising the amount of data needed to be transferred.

To compress one or more large files:

1. Tarball the folder containing your files to transfer (you can compress the tarball or leave it uncompressed):

    ```sh
    tar -czvf tarball_file.tar folder_to_tarball # Compressed Mode
    ```

2. Transfer the tarball file using a file transfer method.

3. Untarball the tarball containing your files:

    ```sh
    tar -xzvf tarball_file.tar # Compressed Mode
    ```

!!! tip
    To prevent running out of space on your `project` directory, create your tarballs in your `nobackup` directory.

    If you are running out of space in your `project` and `nobackup` directories, feel free to [get in touch with us](mailto:support@nesi.org.nz) and we can work with you to help transfer your files.

### Use either `cp`, `mv`, `RClone`, or `Rsync` to transfer files within Mahuika

It is recommended that if you are wanting to transfer files within or between your `home`, `project`, and `nobackup` directories that you use either copy (`cp`), move (`mv`), [RClone](./RClone.md) or [Rsync](./Rsync.md) to achieve this. 

### Only use Globus to transfer data onto and off of Mahuika from an outside source

**Do not use Globus for transferring files from place to place within Mahuika**. 

### Use Checksums

A checksum is a way to verify if a file you have copied has fully and successfully copied from one place to another. See the [Checksums](Checksums.md) page for more information about how checksums work and how to use them to verify your file transfers.
