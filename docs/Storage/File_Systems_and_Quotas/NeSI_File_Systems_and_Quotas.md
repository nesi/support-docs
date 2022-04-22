[Māui](https://support.nesi.org.nz/hc/articles/360000163695) and
[Mahuika](https://support.nesi.org.nz/hc/articles/360000163575), along
with all the ancillary nodes, share access to the same Spectrum Scale
file systems. (Spectrum Scale was previously known as GPFS, or General
Parallel File System.)

You may query your actual usage and disk allocations using the following
command: 

`$ nn_storage_quota`

The values for \'nn\_storage\_quota\' are updated approximately every
hour and cached between updates.

![neSI\_filetree.svg](https://support.nesi.org.nz/hc/article_attachments/360003251796/neSI_filetree.svg){width="629" height="578"}
----------------------------------------------------------------------------------------------------------------------------------

File System Specifications
==========================

**Filesystem**

**/home**

**/nesi/project**

**/nesi/nobackup**

**/nesi/nearline** (in Early Access phase)

**Default disk space\
**

 

 

 

No default; allocations are based on eligibility and technical
requirements\
  

**    - soft quota**

20 GB

100 GB\

10 TB

**    - hard quota**

 

110 GB

12 TB

**Default file count (inode)\
**

 

 

 

No default; allocations are based on eligibility and technical
requirements\
  

**    - soft quota**

1,000,000 files

100,000 files

1,000,000 files

**    - hard quota**

1,100,000 files

110,000 files

1,100,000 files

**Intended use**

User-specific files such as configuration files, environment setup,
source code, etc.

Persistent project-related data, project-related software, etc.

Data created or used by compute jobs that is intended to be temporary

Medium- to long-term storage of research data associated with past,
present or planned compute projects

**Total capacity**

175 TB

1,590 TB

4,400 TB

Will grow as tapes are purchased

**Data retention time**

180 days after the user ceases to be a member of any active project

90 days after the end of the project\'s last HPC Compute & Analytics
allocation

With certain exceptions, individual files will be deleted after being
untouched for 120 days. See [Automatic cleaning of nobackup file
system](https://support.nesi.org.nz/hc/en-gb/articles/360001162856) for
more information. 90 days after the end of the project\'s last HPC
Compute & Analytics allocation, all remaining data is subject to
deletion.

180 days after the end of the project\'s last nearline storage
allocation

**Data backup schedule\
(Excluding snapsots)**

Daily, last 10 versions of any given file retained for up to 90 days.

Daily, last 10 versions of any given file retained for up to 90 days.

None

Replication  between Wellington and Auckland tape libraries (under
development)

**Snapshots**

Daily (retention period 7 days)

Daily (retention period 7 days)

None

None

**Access speed**

Moderate

Moderate

Fast

Slow

**Access interfaces**

-   Native Spectrum Scale mounts
-   SCP
-   Globus data transfer

```{=html}
<!-- -->
```
-   Native Spectrum Scale mounts
-   SCP

```{=html}
<!-- -->
```
-   Native Spectrum Scale mounts
-   SCP
-   Globus data transfer

Nearline commands

### **Soft versus hard quotas**

We use Spectrum Scale soft and hard quotas for both disk space and
inodes.

-   Once you exceed a fileset\'s soft quota, a one-week countdown timer
    starts. When that timer runs out, you will no longer be able to
    create new files or write more data in that fileset. You can reset
    the countdown timer by dropping down to under the soft quota limit.
-   You will not be permitted to exceed a fileset\'s hard quota at all.
    Any attempt to try will produce an error; the precise error will
    depend on how your software responds to running out of disk space.

When quotas are first applied to a fileset, or are reduced, it is
possible to end up with more data or files in the fileset than the quota
allows for. This outcome does not trigger deletion of any existing data,
but will prevent creation of new data or files.

### **Notes:**

-   If you need to compile or install a software package that is large
    or is intended for use by a project team, please build it
    in `/nesi/project/<project_code>` rather than `/home/<username>`.
-   As the `/nesi/nobackup` file system provides the highest
    performance, input files should be moved or copied to this file
    system before starting any job that makes use of them. Likewise, job
    scripts should be written so as to write output files to the
    `/nesi/nobackup` file system. If you wish to keep your data for the
    long term, you can include as a final part of your job script an
    operation to copy or move the output data to the `/nesi/project`
    file system.
-   Keep in mind that data on `/nesi/nobackup` is not backed up,
    therefore users are advised to move valuable data
    to `/nesi/project/<project_code>`, or, if the data is seldom used,
    to other storage such as an institutional storage facility, as soon
    as batch jobs are completed. Please do **not** use the `touch`
    command to prevent the cleaning policy from removing files, because
    this behaviour would deprive the community of a shared resource.

/home
-----

This file system is accessible from login, compute and ancillary nodes.
Users should **not** run jobs from this filesystem. All home directories
are backed up daily, both via the Spectrum Protect backup system, which
retains the last 10 versions of all files for up to 90 days, and via
[Spectrum Scale
snapshots](https://support.nesi.org.nz/hc/articles/360000207315). No
cleaning policy will be applied to your home directory as long as your
My NeSI account is active and you are a member of at least one active
project.

/nesi/project
-------------

This filesystem is accessible from all login, compute and ancillary
nodes. Contents are backed up daily, via the Spectrum Protect backup
system, which retains the last 10 versions of all files for 90 days. No
cleaning policy is applied.

It provides storage space for datasets, shared code or configuration
scripts that need to be accessed by users within a project, and
[potentially by other
projects](https://support.nesi.org.nz/hc/articles/360000205435). Read
and write performance increases using larger files, therefore you should
consider archiving small files with the `nn_archive_files` utility, or a
similar archiving package such as `tar` .

Each NeSI project receives quota allocations for
`/nesi/project/<project_code>`, based on the requirements you tell us
about in your [application for a new NeSI
project](https://my.nesi.org.nz/html/request_project), and separately
covering disk space and number of files.

/nesi/nobackup
--------------

The `/nesi/nobackup` file system has the highest performance of all NeSI
file systems, with greater than 140 GB/s bandwidth from compute nodes to
disk. It provides access to a very large (4.4 PB) resource for
short-term project usage.

To prevent project teams from inadvertently bringing the file system
down for everyone by writing unexpectedly large amounts of data, we
apply per-project quotas to both disk space and number of files on this
file system. The default per-project quotas are as described in the
above table; if you require more temporary (scratch) space for your
project than the default quota allows for, you can discuss your
requirements with us during [the project application
process](https://support.nesi.org.nz/hc/en-gb/articles/360000202136), or
[contact our support team](https://support.nesi.org.nz/hc/requests/new)
at any time.

[To ensure this file system remains fit-for-purpose, we are rolling out
a regular cleaning policy as described in [Automatic cleaning of
nobackup
filesystem](https://support.nesi.org.nz/hc/en-gb/articles/360001162856).]{.wysiwyg-color-black}

Do not use the `touch` command or an equivalent to prevent the cleaning
policy from removing unused files, because this behaviour would deprive
the community of a shared resource.

The purpose of this policy is to ensure that any user will be able to
analyse datasets up to 1 PB in size.

/nesi/nearline
--------------

> ### Note {#nearline-not-available}
>
> The nearline service, including its associated file systems, is in an
> Early Access phase, and allocations are by invitation. We appreciate
> your patience as we develop, test and deploy this service. If you
> would like to participate in the Early Access Programme, please
> [contact our support
> team](https://support.nesi.org.nz/hc/requests/new).

The `/nesi/nearline` filesystem is a data cache for the Hierarchical
Storage Management System, which automatically manages the movement of
files between high performance disk storage and magnetic tape storage in
an Automatic Tape Library (ATL). Files will remain on `/nesi/nearline`
temporarily, typically for hours to days, before being moved to tape. A
catalogue of files on tape will remain on the disk for quick access.

See [this
page](https://support.nesi.org.nz/hc/en-gb/articles/360001169956) for
more information about the nearline service.

Snapshots
=========

If you have accidentally deleted data you can recover it from
a [snapshot](https://support.nesi.org.nz/knowledge/articles/360000207315/en-gb?brand_id=30406).
Snapshots are taken daily of `home/` and `project` directories If you
cannot find it in a snapshot, please ask us to recover it for you by
emailing [NeSI
Support](mailto:support@nesi.org.nz?subject=Please%20Recover%20a%20File).

Contributions of Small Files Towards Quotas
===========================================

The Spectrum Scale file system makes use of a feature called
*data-in-inode*. This feature will ensure that, once all of a
(non-encrypted) file\'s required metadata has been written to our
metadata storage, if all the file\'s data is able to fit within the
file\'s remaining inode space (4 KiB minus metadata), it will be written
there instead of to the data storage.

For files larger than 4 KiB (minus the space needed to store the file\'s
metadata), the data written to disk will be stored in one or more
sub-blocks of 256 KiB each (which are 1/32 of the filesystem Block
Size), and the \"size\" allocated on disk will be rounded up to the
nearest 256 KiB. Users or projects requiring many small files may find
themselves using large amounts of disk space. Use of *data-in-inode*
mitigates the effect of a large block size on such people and project
teams.

However, very small files, as well as zero-size entities such as
directories and symbolic links, still count towards the relevant
fileset\'s inode quota. If therefore you expect you will need to store
large numbers of very small files in your home directory or in a
project\'s persistent storage, please [contact our support
team](https://support.nesi.org.nz/hc/en-gb/requests/new) to discuss your
storage needs.
