Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline
Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline
Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline
Nearline Nearline Nearline Nearline Nearline Nearline Nearline Nearline
Nearline Nearline Nearline Nearline

::: {.confluence-information-macro-body}
> ### Service Status {#nearline-service-status}
>
> Before deleting any data from your project or nobackup directory that
> has been uploaded to Nearline, please consider whether you require
> [verification of the
> transfer](https://support.nesi.org.nz/hc/en-gb/articles/360001482516).
> We recommend that you do at least a basic verification of all
> transfers.
>
> **Please note:** Best practice in research data management and data
> archiving is to use multiple storage technologies. In particular, any
> data that is irreplaceable and/or has regulatory retention
> requirements, should not rely solely on NeSI's Nearline service as the
> only copy.
>
> Please **send feedback** about your user experience at
> <https://support.nesi.org.nz/hc/requests/new>, which may include
> functionality issues, intuitive or counter-intuitive behaviours,
> behaviours or features that you like, suggestions for improvements,
> transfers taking too long, etc.

NeSI\'s Long-Term Storage aka Nearline service allows you to store your
data on our hierarchical system, which consists of a staging area (disk)
connected to a tape library. Users of this service gain access to more
persistent storage space for their research data, in return for slower
access to those files that are stored on tape. We recommend that you use
this service for larger datasets that you will only need to access
occasionally and will not need to change in situ. The retrieval of data
may be delayed, due to tape handling.

Due to the tape storage backend Nearline is intended for use with
relatively large files and should not be used for a large number of
small files. [Files smaller than 64 MB will not be accepted for upload
and should be combined into archive files using `nn_archive_files`,
`tar` or a similar tool. Likewise, Nearline write semantics are
different from a normal filesystem - overwriting existing files (e.g.
when the source data has been updated) is not supported, these must
first be removed (purged from Nearline) before being written (put to
Nearline) again.]{style="color: #1d1c1d;"}

> ### Note {#directory-mapping}
>
> The existing directory structure starting after
> `/nesi/project/<projectID>/` or `/nesi/nobackup/<projectID>/` will be
> mapped onto `/nesi/nearline/<projectID>/`. While retrieving data, the
> whole directory structure after `/nesi/nearline/<projectID>` will be
> mapped into the target directory. See [details](#directory_mapping)
> below for details.

A Nearline project gets locked when writing to or deleting from it.
Until this process is finished no other write or delete operation can be
performed on the same project and the user will see a status message
\"**project locked by none**\".

# What you can do

The client allows you to carry out the following operations:

-   View files: View a list of files stored in a Nearline directory.
-   Traverse a directory: View a list of files stored in a Nearline
    directory, including files stored in all its subdirectories.
-   Put: Copy files from your project or nobackup folder into Nearline.
-   Get: Retrieve files from Nearline into your project or nobackup
    folder, without deleting them from Nearline.
-   Compare the contents of a local directory with the contents of a
    Nearline directory.
-   Purge: Delete files stored in Nearline.
-   View job status: View a list of jobs (put/get/purge) you have run,
    along with their status.
-   View quota: View your Nearline quota and usage.

# Getting started

Nearline has a common tool for access, with a set of `nl` commands,
which are accessible by loading the following module:

    module load nearline
:::

> ### Note {#module-version}
>
> You may notice that in the above command no specific version of the
> Nearline software is chosen. This is deliberate, and is designed to
> ensure that you get the latest and greatest release, since Nearline is
> under active development. It\'s an exception to our normal practice of
> strongly advising you to load a specific version of a software module.

 

# View files

With the following command, you can print the list of files and
directories within the specified Nearline directory:

    nlls /nesi/nearline/<projectID>

OR e.g.

    nlls /nesi/nearline/<projectID>/path/to/results/

Furthermore, you can use the additional option `-l` to get the detailed
list including `mode`, `owner`, `group`, `filesize`, and `timestamp`.
The option `-s`, an alternative to `-l`, will additionally show each
file\'s migration status. Note that, due to technical limitations, `-s`
does not work on single files and so `nlls -s` requires a directory as
its argument.

    $ nlls -s /nesi/nearline/<projectID>/results/
    mode        s  owner               group      filesize    timestamp    filename
    ___________________________________________________________________________________________________________________________
    -rw-rw----+ r  userName        nesi12345      33.93 MB       Jun 17    file1.tar.gz
    -rw-rw----+ r  userName        nesi12345      33.93 MB       Jun 17    file2.tar.gz
    -rw-rw----+ r  userName        nesi12345      34.03 MB       Jun 17    file3.tar.gz

Status (\"s\" column of the `-s` output) legend:

-   migrated (**m**) - data of a specific Nearline file is on tape (does
    not necessarily mean that the file is replicated across sites)
-   pre-migrated (**p**) - data of a specific Nearline file is on both
    the staging filesystem and the tape.
-   resident (**r**) - data of a specific Nearline file is only on the
    staging filesystem.

# Traverse

If you want to see all the files within a Nearline directory and its
subdirectories, you can run `nltraverse`.

    nltraverse /nesi/nearline/<projectID>

Optionally, you can run `nltraverse` with the `-s` command-line switch,
which, as with `nlls`, will display the migration status of each file
found.

# Compare

If you want to compare a local (online storage) directory to a directory
on Nearline, you can use the `nlcompare` command. The syntax of this
command is:

    nlcompare <local_directory> <nearline_directory>

This command will print out the lists of files giving their last
modified times, sizes and file paths.

`nlcompare` is particularly useful if you want to compare a directory on
Nearline to a corresponding directory in `/nesi/project` or
`/nesi/nobackup`. See [Verifying uploads to Nearline
storage](https://support.nesi.org.nz/hc/en-gb/articles/360001482516) for
more information on how to do a comparison and verification.

If the contents of the Nearline directory and the corresponding local
directory differ, the lists will be kept, and can be compared using any
text file comparison program, such as `diff` or `vimdiff`.

# Put {#Nearlineearlyaccessuserguide-Put}

Data can be copied to Nearline using the `nlput` command. The syntax is:

    nlput [ --nowait ] <projectID> { <src_dir> | <file_list> }

The source directory or file list needs to be located under
`/nesi/project/` or `/nesi/nobackup/`and specified as such. 

> ### Note {#nlput-relative-paths}
>
> The following will not work:
>
>     cd /nesi/project/nesi12345
>     nlput nesi12345 some_directory
>
> It is necessary to do this instead:
>
>     nlput nesi12345 /nesi/project/nesi12345/some_directory

The data will be mapped into the same directory structure under
`/nesi/nearline/` (see below).

The recommended file size to archive is between 1 GB and 1 TB. The
client will not accept any directory or file list containing any file
smaller than 64 MB or larger than 1 TB.

The Nearline client also checks file and directory permissions.
Specifically, before uploading a directory or the contents of a file
list, `nlput` will check the following, and will reject any directory or
file list that does not satisfy all these criteria:

-   Every file must be readable by you, the operator.
-   Every file must be readable and writable by its owner.
-   Every file must be readable and writable by its group.
-   The POSIX group of every file must be the project selected for
    upload.

If you are uploading a directory rather than the contents of a file
list, the following additional permission restrictions apply:

-   Every subdirectory must be readable and executable by you, the
    operator.
-   Every subdirectory must be readable, writable and executable by its
    owner.
-   Every subdirectory must be readable, writable and executable by its
    group.
-   The POSIX group of every subdirectory must be the project selected
    for upload.

> ### Warning {#nlput-input}
>
> Files and directories are checked for existence and only new files are
> transferred to Nearline. **Files already on Nearline will not be
> updated to reflect newer source files**. Thus, files that already
> exist on Nearline (either tape or staging disk) will be skipped in the
> migration process, though you should receive a notification of this
>
> If you wish to replace an existing file at a specific file path
> (instead of creating a copy at a different file path) then the
> original copy on Nearline must be purged.

`nlput` takes only a directory or a file list. **A single file is
treated as a file list** and read line by line, searching for valid file
names. Single files can only be migrated using a file list containing
the full path of the file to be transferred.

## Put - directory {#Nearlineearlyaccessuserguide-Put-directory}

> ### Warning {#directories-with-spaces}
>
> If you try to upload to Nearline a path containing spaces, especially
> multiple consecutive spaces, you will get some very unexpected
> results, such as the job being dropped. We are aware of the issue and
> may introduce a fix in a future release. In the meantime, we suggest
> avoiding supplying such arguments to `nlput`. You can work around it
> by renaming the directory and all its ancestors to avoid spaces, or by
> putting the directory (or its ancestor whose name contains a space)
> into an archive file.
>
> This problem does not affect when your directory to upload happens to
> have contents (files or directories) with spaces in their names, i.e.
> to cause a problem the space must be in the name of the directory to
> be uploaded or one of its ancestor directories.

All files and subdirectories within a specified directory will be
transferred into Nearline. The target location maps with the source
location. As an example:

    nlput nesi12345 /nesi/nobackup/nesi12345/To/Archive/Results/

will copy all data within the `Results` directory into
`/nesi/nearline/nesi12345/To/Archive/Results/`.

> ### Warning {#directory-merging}
>
> If you put `/nesi/project/nesi12345/To/Archive/Results/` on Nearline
> as well as `/nesi/nobackup/nesi12345/To/Archive/Results/`, the
> contents of both source locations (`project` and `nobackup`) will be
> merged into `/nesi/nearline/nesi12345/To/Archive/Results/`. Within
> `/nesi/nearline/nesi12345/`, files with the same name and path will be
> skipped.

## Put - file list {#Nearlineearlyaccessuserguide-Put-file-list}

> ### Warning {#nlput-file-list}
>
> The file list must be located within `/nesi/project` or
> `/nesi/nobackup`. Any other location will cause obscure errors and
> failures.

The `file_list` is a file containing a list of files to be transferred.
It can specify **only one file per line** and **directories are
ignored**.

The target location will again map with the source location, see above.

## Update {#Nearlineearlyaccessuserguide-Update}

As a good practice:

-   migrate only large files (SquashFS archives, tarballs, or files that
    are individually large), or directories containing exclusively large
    files.
-   Do not try to modify a file in the source (nobackup or project)
    directory once there is a copy of it on Nearline.

If you need to update data on the Nearline file system with a newer
version of data from nobackup or project:

1.  Compare the contents of the source directory
    (on `/nesi/project` or `/nesi/nobackup`) and the target directory
    (on `/nesi/nearline`). To look at one directory
    on `/nesi/nearline` at a time, use `nlls`; if you need to compare a
    large number of files across a range of directories, or for more
    thorough verification (e.g. checksums), read [this
    article](https://support.nesi.org.nz/hc/en-gb/articles/360001482516)
    or [contact our support
    team](https://support.nesi.org.nz/hc/requests/new).
2.  Once you know which files you need to update (i.e. only files whose
    Nearline version is out of date), remove the old files on Nearline
    using `nlpurge`.
3.  Copy the updated files to the Nearline file system using `nlput`.

> ### Warning {#immutable-files}
>
> For technical reasons, files (data and metadata) and directory
> structures on Nearline cannot be safely changed once present, even by
> the system administrators, except by deletion and recreation. If you
> wish to rename your files or restructure your directories, you must
> follow the process below.

If you need to edit data, rename files, or restructure directories that
exist on Nearline but are no longer on project or nobackup:

1.  Retrieve the files and directories you wish to change using the
    `nlget` command (see below).
2.  Make the changes you wish to make.
3.  Follow the instructions above for updating data on Nearline with a
    new version of the data from project or nobackup.

# Get {#Nearlineearlyaccessuserguide-Get}

Data can be retrieved from Nearline using then `nlget` command. The
syntax is:

    nlget [ --nowait ] <projectID> { <src_dir> | <file_list> } <dest_dir>

Similar to `nlput` (see above), nlget accepts a Nearline** directory**
`src_dir` **(no single files on Nearline accepted)** or a **local file
list** `file_list`, defining the source of the data to be retrieved from
Nearline.

> ### Warnings {#nlget-file-list}
>
> -   The local file list must be located within `/nesi/project` or
>     `/nesi/nobackup`. Any other location will be rejected.
> -   Paths to files or directories to be retrieved must be absolute and
>     start with `/nesi/nearline`, whether supplied on the command line
>     (as a directory) or as entries in a file list.
> -   Directories whose names contain spaces, especially multiple
>     consecutive spaces, cannot be retrieved from Nearline directly
>     using `nlget`. You must retrieve the contents of such a directory
>     using a filelist, or retrieve one of its ancestors that doesn\'t
>     have a space in the name or path. That is, instead of retrieving
>     `/nesi/project/nesi12345/ab/c  d` directly, retrieve
>     `/nesi/project/nesi12345/ab`. We are aware of the problem and may
>     address it in a later Nearline release.

The destination `dest_dir` needs to be defined. The whole directory
structure after `/nesi/nearline/` will be created at the destination and
the specified data written into it. For example,

    nlget nesi00000 /nesi/nearline/nesi00000/dir/to/results/ /nesi/nobackup/

will create the directory structure
`/nesi/nobackup/nesi00000/dir/to/results/` if that directory structure
does not already exist, and copy the data within the `Results` directory
into it.

> ### Warning {#prerequisites}
>
> Any given file **will not be retrieved** if a file of the same name
> already exists in the destination directory. If you wish to retrieve a
> new copy of a file that already exists at the destination directory
> then you must either change the destination directory, or delete the
> existing copy of the file in the that directory.

`nlget` takes only one directory or one file list. **Single files, if
local, are treated as a file list** and read line by line, searching for
valid file names. A single Nearline file can only be retrieved using a
local file list specifying the full path of the file to be retrieved.

# Purge {#Nearlineearlyaccessuserguide-Purge}

The `nlpurge` command deletes specified data on the Nearline file system
permanently. The syntax is

    nlpurge [--nowait] <src_dir>
    nlpurge [ --nowait ] <projectID> { <src_dir> | <file_list> }

A **directory** `src_dir` already on Nearline **(no single files
accepted)** or a file list `file_list` needs to be specified (see
`nlput` above).

If the thing to be deleted is a directory, the project code is optional.
If you are instead deleting the entries of a file list, the project code
is compulsory, and moreover all entries in the file list must denote
files within (or supposed to be within) the chosen project\'s Nearline
directory.

> ### Warnings {#nlpurge-file-list}
>
> -   If a file list is used, it must be located within `/nesi/project`
>     or `/nesi/nobackup` and referred to by its full path starting with
>     one of those places (symlinks in the path are OK).
> -   Paths to files or directories to be purged must be absolute and
>     start with `/nesi/nearline`, whether supplied on the command line
>     (as a directory) or as entries in a file list.
> -   Purging the entire Nearline directory for a project, e.g.
>     `nlpurge /nesi/nearline/nesi12345`, is not permitted. To empty a
>     project\'s Nearline directory, you must purge its contents one by
>     one (if directories), or by means of a filelist (if files).

# View job status {#Nearlineearlyaccessuserguide-Viewjobstatus}

The tool `nljobstatus` provides current status of submitted (queued,
running and completed) tasks. The syntax is:

    nljobstatus [ <jobid> ]

If no job ID is specified the full list of your successfully submitted
and accepted jobs is returned. In this list, each job looks like the
following:

    $ nljobstatus
    +----------+------------+----------------------------+-----------+-------------+
    |  Jobid   | Project ID |         Job Status         | Job Host  |  Job User   |
    +----------+------------+----------------------------+-----------+-------------+
    | 4e23f517 |     13     |   job done successfully    | librarian | userName    |
    | -dfef-40 |            |                            |           |             |
    | e9-a83c- |            |                            |           |             |
    | 3da78b06 |            |                            |           |             |
    |   0310   |            |                            |           |             |
    +----------+------------+----------------------------+-----------+-------------+

With a job identifier `jobid`, information for a specific job can be
listed:

    $ nljobstatus 4e23f517-dfef-40e9-a83c-3da78b060310
    +--------------------------------------+
    |                Jobid                 |
    +--------------------------------------+
    | 4e23f517-dfef-40e9-a83c-3da78b060310 |
    +--------------------------------------+
    +------------+-----------------------+-----------+-------------+
    | Project ID |      Job Status       | Job Host  |  Job User   |
    +------------+-----------------------+-----------+-------------+
    |     13     | job done successfully | librarian | userName    |
    +------------+-----------------------+-----------+-------------+
    +---------------------+---------------------+---------------------+
    |   Job Start Time    |   Job Update Time   |    Job End Time     |
    +---------------------+---------------------+---------------------+
    | 2019-09-13T03:11:22 | 2019-09-13T03:11:44 | 2019-09-13T03:11:45 |
    +---------------------+---------------------+---------------------+

If an `nlput` or `nlpurge` is running in that project, the project is
locked until the task is finished.

**If a job stays in one state for an unexpectedly long time, please
[contact NeSI Support](https://support.nesi.org.nz/hc/request/new)**.

# View quota {#Nearlineearlyaccessuserguide-Viewquota}

With the command `nlquotalist`, the usage and limits of a Nearline
project quota can be listed:

::: {.confluence-information-macro-body}
    nlquotalist <projectID>
:::

The output looks like:

    $ nlquotalist nesi12345
    Projectname                                       Available           Used                Inodes         IUsed
    ___________________________________________________________________________________________________________________________
    nesi12345                                         30.00 TB            27.16 TB            1000000        412

This quota is different from the project quota on GPFS
(`/nesi/project/<projectID>`).

[]{#directory_mapping}

# Data management {#Nearlineearlyaccessuserguide-Datamanagement}

In case you have the same directory structure on your project and
nobackup directories, be careful when archiving data from both. They
will be merged in the Nearline file system. Further, when retrieving
data from Nearline, keep in mind that the directory structure up to your
projectID will be retrieved:

![librarian\_get\_put.jpeg](https://support.nesi.org.nz/hc/article_attachments/360002703556/librarian_get_put.jpeg)

# Underlying mechanism {#Nearlineearlyaccessuserguide-Underlyingmechanism}

The Nearline file system consists of two parts: Disk, mainly for
buffering data, and the tape library. It consists of a client running on
the login/compute node and the backend on the Nearline file system. It
is important to know that **even if you cancel a client process, the
corresponding backend process remains scheduled or running** until
finished.

[The process of what data goes into tape and when is
automated]{.inline-comment-marker
data-ref="78239edd-ceab-49eb-a747-0140db19a948"}, and is not something
you will have control over. The service is designed to optimise
interaction with the Nearline filesystem and avoid problem workloads for
the benefit of all users.

If your files are on tape, it will take time to retrieve them. Access to
tape readers is on a first come first served basis, and the amount of
wait time will vary dramatically depending on overall usage. We cannot
guarantee access to your files within any particular timeframe, and
indeed wait times could be hours or even in some cases more than a day.

# Known issues

> ### Retrievals {#retrieval}
>
> Some users of Nearline have reported that attempts to retrieve files
> from tape using `nlget` (see below) will not retrieve all files.
> Instead, only some files will come back, and the job will finish with
> the following output:
>
>     recall failed some syncs might still run (042)
>
> We are aware of this problem, which is caused by the Nearline job
> timing out while waiting for a tape drive to become available. This
> problem may also occur if you attempt to retrieve multiple files,
> together adding to a large amount of data, from Nearline.
>
> Unfortunately, a proper fix requires a fundamental redesign and
> rebuild of the Nearline server architecture, work that is on hold
> pending decisions regarding the direction in which we take NeSI\'s
> data services. We appreciate your patience as we work through these
> decisions.
>
> In the meantime, if you encounter this problem, the recommended
> workaround is to wait a couple of hours (or overnight, if at the end
> of a day) and try again once a tape drive is more likely to be free.
> You may have to try several times, waiting between each attempt. We
> apologise for any inconvenience caused to you by tape drive
> contention.

 

# Support contact {#Nearlineearlyaccessuserguide-Supportcontact}

Please [contact our support
team](https://support.nesi.org.nz/hc/requests/new) with any queries or
concerns you may have regarding this service. We welcome feedback from
our users.
