---
created_at: '2018-05-02T04:06:16Z'
tags:
- storage
- quota
title: NeSI filesystems and Quotas
---

The HPC compute nodes, login nodes and OnDemand all share access to the same filesystems.
You may query your actual usage and disk allocations using the following
command:

```sh
 nn_storage_quota
```

The values for `nn_storage_quota` are updated approximately every hour
and cached between updates.

![neSI\_filetree.svg](../../assets/images/NeSI_File_Systems_and_Quotas.png)

## filesystem Specifications

| Filesystem     | `/home`                                                                                | `/nesi/project`                                                                                                  | `/nesi/nobackup` | `Freezer`        |
| -------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Disk Quota     | 20 GB                                                                                 | 100 [110] GB                                                                                                    | 10 [12] TB | -                                                                                                       |
| Usage  | User-specific files such as configuration files, environment setup, source code, etc. | Persistent project-related data, software, etc. | Data created or used by compute jobs that is intended to be temporary | Medium- to long-term storage of research data, (past, present or planned projects) |
| Data retention | 180 days after the user ceases to be a member of any active project                   | 90 days after the end of the project's last HPC compute allocation. See also Transparent File Data Compression. | Untouched for 90 days, or 90 days after the end of the project's last HPC Compute allocation. See Automatic cleaning of nobackup filesystem for more information.  | 180 days after the end of the project's last nearline storage allocation |
| Snapshots      | Daily<br>7 days                                                               | Daily<br>7 days                                                                                        | - | - |
| Speed          | Fast | Fast | Fast | Slow |
| Interfaces     | <ul><li>Native Mounts</li><li>SCP</li><li>Globus</li><ul> | <ul><li>Native mounts</li><li>SCP</li></ul> | <ul><li>Native Mounts</li><li>SCP</li><li>Globus</li> |<ul><li>s3cmd commands</li></ul> |

### **Soft versus hard quotas**

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

#### Notes

- You may request an increase in storage quota if needed by
    a project. This may in turn be reduced as part of managing overall
    risk, where large amounts of quota aren't used for a long period (~6
    Months).
- If you need to compile or install a software package that is large
    or is intended for use by a project team, please build it
    in `/nesi/project/<project_code>` rather than `/home/<username>`.
- Keep in mind that data on `/nesi/nobackup` is not backed up,
    therefore users are advised to move valuable data
    to `/nesi/project/<project_code>` or Freezer, or, if the data is seldom used,
    to other storage such as an institutional storage facility, as soon
    as batch jobs are completed. Please do **not** use the `touch`
    command to prevent the cleaning policy from removing files, because
    this behaviour would deprive the community of a shared resource.

### /home

This filesystem is accessible from login, compute and ancillary nodes.
Users should **not** run jobs from this filesystem. [Snapshots](../Data_Recovery/File_Recovery.md) are taken of all home directories
daily.
No cleaning policy will be applied to your home directory as long as
your user account is active and you are a member of at least one
active project.

### /nesi/project

This filesystem is accessible from all login, compute and ancillary
nodes. [Snapshots](../Data_Recovery/File_Recovery.md) are taken daily. No
cleaning policy is applied.

It provides storage space for datasets, shared code or configuration
scripts that need to be accessed by users within a project, and
[potentially by other projects](../File_Systems_and_Quotas/File_permissions_and_groups.md).
Read and write performance increases using larger files, therefore you should
consider archiving small files with an archiving package such as `tar` .

Each project receives quota allocations for
`/nesi/project/<project_code>`, based on the requirements you tell us
about in your [application for a new NeSI
project](https://my.nesi.org.nz/html/request_project), and separately
covering disk space and number of files.

### /nesi/nobackup

This filesystem is accessible from all login, compute and ancillary
nodes. No snapshots or backups of this filesystem are guaranteed.

To prevent project teams from inadvertently bringing the filesystem
down for everyone by writing unexpectedly large amounts of data, we
apply per-project disk space quotas to projects on this
filesystem. The default per-project quotas are as described in the
above table; if you require more temporary (scratch) space for your
project than the default quota allows for, you can discuss your
requirements with us during [the project application process](../../General/NeSI_Policies/How_we_review_applications.md),
or {% include "partials/support_request.html" %} at any time.

To ensure this filesystem remains fit-for-purpose, we have a regular
cleaning policy as described in
[Automatic cleaning of nobackup filesystem](../../Storage/File_Systems_and_Quotas/Automatic_cleaning_of_nobackup_file_system.md).

Do not use the `touch` command or an equivalent to prevent the cleaning
policy from removing unused files, because this behaviour would deprive
the community of a shared resource.

The purpose of this policy is to ensure that any user will be able to
analyse datasets up to 1 PB in size.

### Freezer

The Freezer filesystem is a data cache for the Hierarchical
Storage Management System, which automatically manages the movement of
files between high performance disk storage and magnetic tape storage in
an Automatic Tape Library (ATL). Files will remain on Freezer
temporarily, typically for hours to days, before being moved to tape. A
catalogue of files on tape will remain on the disk for quick access.

See more information about the long term storage see our [documentation about the Freezer storage service](../../Storage/Long_Term_Storage/Freezer_long_term_storage.md).

## Snapshots

If you have accidentally deleted data you can recover it from
a [snapshot](../Data_Recovery/File_Recovery.md).
Snapshots are taken daily of `home/` and `project` directories If you
cannot find it in a snapshot, please ask us to recover it for you by
{% include "partials/support_request.html" %}
