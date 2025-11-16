---
created_at: '2019-09-15T23:36:59Z'
description: Description of our automatic deletion of old data.
tags:
- nobackup
- cleaning
- storage
---

The automatic cleaning feature is a programme of regular deletion of selected files from project directories in our scratch filesystem (/nesi/nobackup).

We do this to optimise the availability of this filesystem for active research computing workloads and to ensure we can reliably support large-scale compute and analytics workflows.

## How it works

Files are deleted if they meet **all** of the following criteria:

- The file was first created more than 60 days ago
- The file has not been accessed, and neither its data nor its metadata has been modified, for at least 60 days
- The file was identified as a candidate for deletion two weeks previously (and as such is listed in the project's nobackup `.policy` directory)

The general process follows a schedule of:

- Every week, we review files stored in the scratch filesystem and identify candidates for expiry.
- Project teams will be notified by email if they have file candidates for deletion. Emails will be sent two weeks in advance of any deletion taking place.
- Immediately after deletion is complete, a new set of candidate files will be identified for expiry during the next automated cleanup. These candidate files are all files within the project's scratch filesystem that have not been created, accessed or modified within the last 46 days.

In summary, we **notify** at 46 days (2 weeks advance notice) and then **delete** at 60 days.
There will be ***no exclusions*** to this auto-deletion process. If you need to store data for longer than 60 days, [get in touch with our Support Team](mailto:support@nesi.org.nz).

!!! tip
     At any time you can check for and delete files older than 60 days (replace <project code> with the project code of interest, e.g. “nesi99999”):

    - To list all files (and their owners) not accessed within 60 days, run the following command (you may want to redirect the output to a file): 
    ```find /nesi/nobackup/<project code> -type f -atime +60 -ctime +60 -printf '%u : %p\n'```

    - To direct this to a file: 
    ```find /nesi/nobackup/<project code> -type f -atime +60 -ctime +60 -printf '%u : %p\n' > files_that_will_be_deleted.txt```

    - To delete those files, run this command:
    ```find /nesi/nobackup/<project code> -type f -atime +60 -ctime +60 -delete```

Objects other than files, such as directories and symbolic links, are not deleted under this policy, even if at deletion time they are empty, broken, or otherwise redundant. These entities typically take up no disk space apart from a small amount of metadata, but still count towards the project's inode (file count) quota.

## How will I be notified that my data is a candidate for deletion?

Prior to data being deleted, we’ll send you an email identifying what has been marked for deletion. These email notifications are optional so if you do not want to receive them, you can ‘unsubscribe’ through my.nesi.org.nz.

## How can I check which files have been already deleted or are scheduled for deletion?

You can manually check at any time if you have any data that's already been deleted or is scheduled for deletion. A file containing the list of candidates for deletion during the next cleanup, along with the date of the next cleanup, will be created in a directory called `.policy/to_delete` inside your project's scratch directory.

## What should I do with expiring data on the nobackup filesystem?

If you have files identified as candidates for deletion that you need to keep beyond the scheduled expiry date, you have two options:

- Move the file to your persistent project directory, e.g., /nesi/project/nesi12345. You may need to request more disk space in your persistent project directory before you can do this. Contact our Support Team. We assess such requests on a case-by-case basis.  Note:  You can save space by compressing data.  Standard tools such as gzipbzip2 etc are available.
- Move or copy the file to a storage system at your institution. We expect most projects to do this for finalised output data and appreciate prompt egress of data once it is no longer used for processing.

## Where should I store my data?

Generally:

- the project directory should be used for reference data, tools, and job submission and management scripts.
- the scratch filesystem should be used for holding large reference working datasets (e.g., an extraction of compressed input data) and as a destination for writing and modifying temporary data. It can also be used to build and edit code, provided that the code is under version control and changes are regularly checked into upstream revision control systems.
- Freezer, our long-term storage service should be used for larger datasets that you only access occasionally and do not need to change in situ.

| Frequency of data being read | Frequency of data being written | Recommended option                                                                                         |
| -------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Often                                                    | Often (at least once every two months)                   | Store in your /nobackup/<projectcode> directory (but ensure key result data is copied to the persistent project directory) |
| Often                                                    | Seldom                                                   | Store in your /project/<projectcode> directory                                                                    |
| Seldom                                                   | Seldom                                                   | Apply for an allocation to use Freezer or store the data elsewhere (e.g. at your institution)                                                        |

## If I need a file that was deleted from nobackup, what should I do?

Please [contact our Support Team](mailto:support@nesi.org.nz) as soon as possible after you find that the file is missing. We can’t guarantee that it can be recovered, but we will do our best to retrieve the data.

## I have research data on nobackup that I can't store in my project directory or at my institution right now. What should I do?

Please [contact our Support Team](mailto:support@nesi.org.nz) so we can discuss your short- and medium-term data storage needs.

## More information

If you have any questions or would like to discuss our storage facilities and policies in more detail, come to one of our [weekly Online Office Hours](https://docs.nesi.org.nz/Getting_Started/Getting_Help/Weekly_Online_Office_Hours/) or [email our Support Team](mailto:support@nesi.org.nz) .
