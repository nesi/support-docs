---
created_at: '2019-09-15T23:36:59Z'
hidden: false
weight: 1
description: Description of NeSI's automatic deletion of old data.
tags:
- nobackup
- cleaning
vote_count: 4
vote_sum: 2
zendesk_article_id: 360001162856
zendesk_section_id: 360000033936
---

The automatic cleaning feature is a programme of regular deletion of
selected files from project directories in our nobackup file system.
We do this to optimise the availability of this file system for active
research computing workloads and to ensure NeSI can reliably support
large-scale compute and analytics workflows.

Files are deleted if they meet **all** of the following criteria:

- The file was first created more than 120 days ago, and has not been
    accessed, and neither its data nor its metadata has been modified,
    for at least 120 days.
- The file was identified as a candidate for deletion two weeks
    previously, and as such is listed in a the project's
    nobackup `.policy` directory.

!!! tip
     You can get a list of files marked for deletion with the command
     `nn_doomed_list`.

    Maximum length of the output file (lines)
    If no arguments are given, `nn_doomed_list` checks and displays all
    project directories the user is a member of. 
    Default limit of the output file is 40 lines. 

The general process will follow a schedule as follows:

- **Notify** (at 106 days), then two weeks later **Delete** (at 120
    days).

- Every fortnight on Tuesday morning, we will be reviewing files
    stored in the nobackup filesystem and identifying candidates for
    expiry.

- Project teams will be notified by email if they have file candidates
    for deletion. Emails will be sent two weeks in advance of any
    deletion taking place.

!!! warning
     Due to the nature of email, we cannot guarantee that any
     particular email message will be successfully delivered and
     received, for instance our emails could be blocked by your mail
     server or your inbox could be too full. We suggest that you check
     `/nesi/nobackup/<project_code>/.policy` (see below) for a list of
     deletion candidates, for each of your projects, whether you
     received an email from us or not.

- Immediately after deletion is complete, a new set of candidate files
  will be identified for expiry during the next automated cleanup.
  These candidate files are all files within the project's nobackup
  that have not been created, accessed or modified within the last 106
  days.

A file containing the list of candidates for deletion during the next
cleanup, along with the date of the next cleanup, will be created in a
directory called `.policy/to_delete` inside the project's nobackup
directory. For example, the candidates for future deletion  from the
directory `/nesi/nobackup/nesi12345` are recorded in
`/nesi/nobackup/nesi12345/.policy/to_delete/<date>.filelist.gz`. Project
team members are able to view the contents of `.policy` (but not delete
or modify those contents). The `gzip` compressed file-list can be viewed
and searched with the `zless` and `zgrep` commands respectively, e.g.,
`zless /nesi/nobackup/nesi12345/.policy/to_delete/<date>.filelist.gz`.

!!! warning
     Objects other than files, such as directories and symbolic links, are
     not deleted under this policy, even if at deletion time they are
     empty, broken, or otherwise redundant. These entities typically take
     up no disk space apart from a small amount of metadata, but still
     count towards the project's inode (file count) quota.

## What should I do with expiring data on the nobackup filesystem?

If the data is transient and no longer required for continued processing
on NeSI then we would appreciate if you deleted it yourself, but you can
also let the automated process do this.

If you have files identified as candidates for deletion that you need to
keep beyond the scheduled expiry date, you have four options:

- Move the file to your persistent project directory,
    e.g., `/nesi/project/nesi12345`. You may need to request more disk
    space, more inodes, or both, in your persistent project directory
    before you can do this. {% include "partials/support_request.html" %}. We
    assess such requests on a case-by-case basis.  Note:  You can save
    space by compressing data.  Standard tools such as `gzip`
    `bzip2` etc are available.

- Move or copy the file to a storage system outside NeSI, for example
    a research storage device at your institution. We expect most
    projects to do this for finalised output data and appreciate prompt
    egress of data once it is no longer used for processing.

- **Modify** the file before the deletion date, in which case the file
    will not be deleted even though it is listed in `.policy`. This must
    only be done in cases where you expect to begin active use of the
    data again within the next month.

- Note: Accessing (Open/Close and Open/Save) or Moving (`mv`) does
    not update the timestamp of the file. Copying (`cp`) does create a
    new timestamped file.

!!! warning
     Doing this for large numbers of files, or for files that together
     take up a large amount of disk space, in your project's nobackup
     directory, without regard for your project's computational
     activity, constitutes a breach of
     [NeSI's acceptable use policy](https://www.nesi.org.nz/services/high-performance-computing/guidelines/acceptable-use-policy).

## Where should I put my data?

| How often will my team's HPC jobs be accessing the data? | How often will my team's HPC jobs be modifying the data? | Recommended option                                                                                         |
| -------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Often                                                    | Often (at least once every two months)                   | Leave in the nobackup directory (but ensure key result data is copied to the persistent project directory) |
| Often                                                    | Seldom                                                   | Put in the persistent project directory                                                                    |
| Seldom                                                   | Seldom                                                   | Store the data elsewhere (e.g. at your institution)                                                        |

In general, the persistent project directory should be used for
reference data, tools, and job submission and management scripts. The
nobackup directory should be used for holding large reference working
datasets (e.g., an extraction of compressed input data) and as a
destination for writing and modifying temporary data. It can also be
used to build and edit code, provided that the code is under version
control and changes are regularly checked into upstream revision control
systems.

## If I need a file that was deleted from nobackup, what should I do?

Please {% include "partials/support_request.html" %} as soon as
possible after you find that the file is missing.
To reduce the risk of this outcome again in future,
please {% include "partials/support_request.html" %} so that we
can discuss your data storage options with you.

## I have research data on nobackup that I can't store in my project directory or at my institution right now. What should I do?

Please {% include "partials/support_request.html" %} without delay
so we can discuss your short- and medium-term data storage needs. Our
intention is to work with you to move your valuable data to an
appropriate combination of:

- Persistent project storage on NeSI,
- High performance /nobackup storage (temporary scratch space) on NeSI,
- Slow nearline storage (not released yet, on our road-map).
- Institutional storage infrastructure.

## User Webinars

On 14 and 26 November 2019, we hosted webinars to explain these upcoming
changes and answer user questions. If you missed these sessions, the
archived materials are available at the links below:

- Video recordings:  
    - [14 November 2019](https://youtu.be/KPNNSwDJU7A)
    - [26 November 2019 repeat of 14 Nov session](https://youtu.be/iVTdlsiBTB4)
- Slides:  
    - [same slides were used for both presentations](https://drive.google.com/file/d/1kLwghsj9es8oMqdWj-VhUvaklW6JkrwO/view?usp=sharing)
- Q&A transcriptions:  
    - [14 November 2019](https://drive.google.com/file/d/1tImzibZ3DcN7QOttZEZoYsR43mEiS5KJ/view?usp=sharing)
    - [26 November 2019](https://drive.google.com/file/d/1OSb71hhZnjnU9xsRALcpYM485va7aUxK/view?usp=sharing)
