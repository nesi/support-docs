---
created_at: '2018-05-02T04:06:16Z'
description: Overview of the REANNZ HPC filesystems.
tags:
- data storage
---

The HPC compute nodes, login nodes and OnDemand all share access to the same filesystems.
You may query your actual usage and disk allocations using the following
command:

```sh
 nn_storage_quota
```

The values for `nn_storage_quota` are updated approximately every hour
and cached between updates.

![neSI\_filetree.svg](../assets/images/NeSI_File_Systems_and_Quotas.png)

## filesystem Specifications

| Filesystem     | `/home`                                                                               | `/nesi/project`                                                                                                 | `/nesi/nobackup`                                                                                                                                                                                          | `Freezer`                                                                          |
| -------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Disk Quota     | 20 GB                                                                                 | 100 [110] GB                                                                                                    | 10 [12] TB                                                                                                                                                                                                | -                                                                                  |
| Usage          | User-specific files such as configuration files, environment setup, source code, etc. | Persistent project-related data, software, etc.                                                                 | Data created or used by compute jobs that is intended to be temporary                                                                                                                                     | Medium- to long-term storage of research data, (past, present or planned projects) |
| Data retention | 180 days after the user ceases to be a member of any active project                   | 90 days after the end of the project's last HPC compute allocation. See also Transparent File Data Compression. | Untouched for 90 days, or 90 days after the end of the project's last HPC Compute allocation. See [Automatic cleaning of nobackup filesystem](./Automatic_cleaning_of_nobackup.md ) for more information. | 180 days after the end of the project's Freezer storage allocation                 |
| Snapshots      | Daily<br>7 days                                                                       | Daily<br>7 days                                                                                                 | -                                                                                                                                                                                                         | -                                                                                  |
| Speed          | Fast                                                                                  | Fast                                                                                                            | Fast                                                                                                                                                                                                      | Slow                                                                               |
| Interfaces     | <ul><li>Native Mounts</li><li>SCP</li><li>Globus</li><ul>                             | <ul><li>Native mounts</li><li>SCP</li></ul>                                                                     | <ul><li>Native Mounts</li><li>SCP</li><li>Globus</li>                                                                                                                                                     | <ul><li>s3cmd commands</li></ul>                                                   |

### Soft and hard quotas

We use Scale soft and hard quotas for both disk space and inodes.

- Once you exceed a fileset's soft quota, a one-week countdown timer
    starts. When that timer runs out, you will no longer be able to
    create new files or write more data in that fileset. You can reset
    the countdown timer by dropping down to under the soft quota limit.
- You will not be permitted to exceed a fileset's hard quota at all.
    Any attempt to try will produce an error; the precise error will
    depend on how your software responds to running out of disk space.

When quotas are first applied to a fileset, or are reduced, it is
possible to end up with more data or files in the fileset than the quota
allows for. This outcome does not trigger deletion of any existing data,
but will prevent creation of new data or files.

!!! note
    - You may request an increase in storage quota if needed by
        a project. This may in turn be reduced as part of managing overall
        risk, where large amounts of quota aren't used for a long period (~6
        Months).
    - If you need to compile or install a software package that is large
        or is intended for use by a project team, please build it
        in `/nesi/project/<project_code>` rather than `/home/<username>`.
    - Keep in mind that data on `/nesi/nobackup` is not backed up,
        therefore users are advised to move valuable data
        to `/nesi/project/<project_code>` or Freezer, or, if the data is seldom used,
        to other storage such as an institutional storage facility, as soon
        as batch jobs are completed. Please do **not** use the `touch`
        command to prevent the cleaning policy from removing files, because
        this behaviour would deprive the community of a shared resource.

### `/home`

For storing files that are central for performing your simulations and calculations on Mahuika. This includes program installations, conda environments and other virtual environments. Home directories (folders) are available in the `/home` volume.

This filesystem is accessible from login, compute and ancillary nodes.
Users should **not** run jobs from this filesystem. [Snapshots](Data_Recovery.md) are taken of all home directories
daily.
No cleaning policy will be applied to your home directory as long as
your user account is active and you are a member of at least one
active project.

### `/nesi/project`

For storing files that you want to keep for long periods of time that you access regularly. This includes important research files you do not want deleted and you access regularly, and can include conda environments and other virtual environments that are too large for `home`. Project space is available as the `/nesi/project` storage volume.

This filesystem is accessible from all login, compute and ancillary
nodes. [Snapshots](Data_Recovery.md) are taken daily. No
cleaning policy is applied.

It provides storage space for datasets, shared code or configuration
scripts that need to be accessed by users within a project, and
[potentially by other projects](./File_permissions_and_groups.md).
Read and write performance increases using larger files, therefore you should
consider archiving small files with an archiving package such as `tar` .

Each project receives quota allocations for
`/nesi/project/<project_code>`, based on the requirements you tell us
about in your [application for a new NeSI
project](https://my.nesi.org.nz/html/request_project), and separately
covering disk space and number of files.

### `/nesi/nobackup` (scratch)

For storing raw data and larger files that are temporary. In this case, temporary may be for short (seconds) to long (90 days) amounts of time. Examples include `temp` files, files that you only need for less than 3 months at a time. Scratch space is available as the `/nesi/nobackup` storage volume.

This filesystem is accessible from all login, compute and ancillary
nodes. No snapshots or backups of this filesystem are guaranteed.

To prevent project teams from inadvertently bringing the filesystem
down for everyone by writing unexpectedly large amounts of data, we
apply per-project disk space quotas to projects on this
filesystem. The default per-project quotas are as described in the
above table; if you require more temporary (scratch) space for your
project than the default quota allows for, you can discuss your
requirements with us during
[the project application process](../Policy/How_we_review_applications.md),
or {% include "partials/support_request.html" %} at any time.

To ensure this filesystem remains fit-for-purpose, we have a regular
cleaning policy as described in
[Automatic cleaning of nobackup filesystem](./Automatic_cleaning_of_nobackup.md).

Do not use the `touch` command or an equivalent to prevent the cleaning
policy from removing unused files, because this behaviour would deprive
the community of a shared resource.

The purpose of this policy is to ensure that any user will be able to
analyse datasets up to 1 PB in size.

### Freezer

Freezer is a tape storage system that employs the S3 protocol and is designed to hold large amounts of data that are accessed infrequently. Freezer is a great solution to prevent data being lost by our fortnightly auto-deletion policy or to run those quarterly, semi-annual or annual workflows. See [Freezer long term storage](Long_Term_Storage/Freezer_long_term_storage.md) for more information.

The Freezer filesystem is a data cache for the Hierarchical
Storage Management System, which automatically manages the movement of
files between high performance disk storage and magnetic tape storage in
an Automatic Tape Library (ATL). Files will remain on Freezer
temporarily, typically for hours to days, before being moved to tape. A
catalogue of files on tape will remain on the disk for quick access.

See more information about the long term storage see our
[documentation about the Freezer storage service](../Long_Term_Storage/Freezer_long_term_storage.md).

## Snapshots

If you have accidentally deleted data you can recover it from
a [snapshot](../Data_Recovery.md).
Snapshots are taken daily of `home/` and `project` directories If you
cannot find it in a snapshot, please ask us to recover it for you by
{% include "partials/support_request.html" %}

This page will guide you through best practices for storing your data on Mahuika.

## What are temporary files and do I need them?

Many programs create temporary files that are created by a program *temporarily* (as the name implies). Programs create temporary files because they would take up too much space in RAM or provide a way to checkpoint so that if the program crashes or times out it can be resumed.

Temporary files can be a problem to store long term because they can take up a large amount of space and create many files (use a lot of inodes). This second point can be problematic as many of the services running behind the scenes in Mahuika are affected by the number of files on our systems.

It is recommended that if your program creates temporary files that you guide that program to write those temporary files to the ``nobackup`` directory.

Temporary files are not needed once the program has finished. Once your program has finished successfully, **you can delete all temporary files**. This is recommended as it will minimise the amount of space that you use ``nobackup``

## Best Practices

### The 3,2,1 Rule

It is vital that files that are important to your work are backed up after you have processed them and want to move them off Mahuika. The 3,2,1 rule is best practise for storing and backing up files to minimise lose of mission critical data. The rule is:

- **3 Copies**: Keep your original data plus two backups.
- **2 Media Types**: Store backups on different media (e.g., internal hard drive, external hard drives, cloud, network attached storage device, high capacity storage, freezer).
- **1 Offsite**: Keep one copy physically separate (e.g., cloud, freezer, high capacity storage, offsite drive) to survive local disasters.

### Where to run jobs

It is best practice to perform your calculations/simulations in the following order:

1. Perform your calculations/simulations in `scratch`. `scratch` is a large storage space that gives you space to perform your calculations/simulations.
2. After analysis, any data you want to keep for further analysis and that you will access regularly should be kept in `project`.
3. If you have gigabytes or terabytes of data that you need to keep on Mahuika but don't have enough space on `project` and do not access regularly, you should consider moving this data onto Freezer. Freezer is designed to keep mass amounts of data on that you will only need to access every few months.
See [Freezer long term storage](Long_Term_Storage/Freezer_long_term_storage.md) for more information.
4. `project` is limited in space, so any data you can move off Mahuika should be when you are either done with the data, or you can do analysis of the data on your own computer. See
[I would like to move data off Mahuika. What are my options?](Offsite_Storage_Options.md).
