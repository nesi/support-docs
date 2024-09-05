---
created_at: '2024-09-05T06:38:01Z'
tags:
- storage
- freezer
- tape
title: Freezer Long-Term Storage Service
vote_count: 3
vote_sum: 3
---

NeSI's Freezer service allows you to store your data on our hierarchical system, which consists of a staging area (disk) connected to a tape library. Users of this service gain access to more persistent storage space for their research data, in return for slower access to those files that are stored on tape. 

We recommend that you use this service for larger datasets that you will only need to access occasionally and will not need to change in situ. The retrieval of data may be delayed, due to tape handling, queuing of the nearline backend service and size of the data to be ingested or retrieved.

Due to the tape storage backend Freezer is intended for use with relatively large files and should not be used for a large number of small files. Files smaller than 64 MB will not be accepted for upload and should be combined into archive files using `tar` or a similar tool.

!!! warning
    A Freezer project gets locked when writing to or deleting from it. Until this process is finished no other write or delete operation can be performed on the same project and the user will see a status message "**project locked by none**".

## What you can do

- View files: View a list of files stored in a Freezer directory.
- Traverse a directory: View a list of files stored in a Freezer directory, including files stored in all its subdirectories.
- Copy files from your project or nobackup folder into Freezer.
- Retrieve files from Freezer into your project or nobackup folder, without deleting them from Freezer.
- Compare the contents of a local directory with the contents of a Freezer directory.
- Delete files stored in Freezer.

## Getting started

Before getting started, your account will must be 'activated' to use the Freezer service.

## Viewing files in Freezer

View files and directories within the specified Freezer directory using the shell command `ls` you can list subdirectories as well:

``` sh
ls /nesi/freezer/<projectID>/
```

Furthermore, you can use the additional option `-l` to get the detailed list including `mode`, `owner`, `group`, `filesize`, and `timestamp`. 


## Data management

In case you have the same directory structure on your project and nobackup directories, be careful when archiving data from both. They will be merged in the Nearline file system. Further, when retrieving data from Freezer, keep in mind that the directory structure up to your projectID will be retrieved:

## Underlying mechanism

The Freezer file system consists of two parts: Disk, mainly for buffering data, and the tape library.

The process of what data goes into tape and when is automated, and is not something you will have control over. The service is designed to optimise interaction with the Nearline filesystem and avoid problem workloads for the benefit of all users.

If your files are on tape, it will take time to retrieve them. Access to tape readers is on a first come first served basis, and the amount of wait time will vary dramatically depending on overall usage. We cannot guarantee access to your files within any particular timeframe, and indeed wait times could be hours or even in some cases more than a day.

## Known issues



## Support contact

Please {% include "partials/support_request.html" %} about your user experience which may include
functionality issues, intuitive or counter-intuitive behaviours, behaviours or features that you like, suggestions for improvements, transfers taking too long, etc.

We welcome feedback from our users.
