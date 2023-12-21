---
created_at: '2020-04-17T09:40:49Z'
hidden: false
weight: 3
tags: []
title: Verifying uploads to Nearline storage
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001482516
zendesk_section_id: 360000042255
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

Our [Long-Term Storage
Service](../../Storage/Nearline_long_term_storage/Nearline_Long_Term_Storage_Service.md)
is currently in an Early Access phase, and we encourage researchers
using the service to verify their data before deleting it from the
project directory (persistent storage) or nobackup directory (temporary
storage).
!!! prerequisite Service Status
     The verification options outlined below are intended to support the
     Early Access phase of Nearline development. Verification options may
     change as the Early Access Programme continues and as the Nearline
     service moves into production. We will update our documentation to
     reflect all such changes.
     Your feedback on which verification options you think are necessary
     will help us decide on future directions for the Nearline service.
     Please {% include "partials/support_request.html" %} to request
     verification or to offer suggestions regarding this or any other
     aspect of our Nearline service.

There are several options for verification, depending on the level of
assurance you require.

## Level 1: Transfer status report

The most basic form of verification is to look at the results
of `nljobstatus`. If all the Nearline job IDs associated with movement
of data to Nearline (i.e. `nlput` commands)
report `job done successfully`, that gives you a basic level of
confidence that the files were in fact copied over to nearline.
!!! prerequisite Warning
     The above check is reliable only if *all* `nlput` commands were
     concerned solely with uploading new files to nearline. Because of the
     way `nlput` is designed, a command trying to update files that already
     existed on nearline will silently skip those files and still report
     success.

## Level 2: File counts and sizes

You can get a higher level of assurance by checking the number of files,
and their sizes and last modified times, in a particular directory on
nearline, and optionally to compare that number and size to the
corresponding directory on `/nesi/project` or `/nesi/nobackup`. We can
also enable comparisons of file permissions if requested, though
differences in permissions or even modification times do not necessarily
suggest a problem as long as the names and sizes are the same. If you
are interested in verifying file permissions, please [contact our
support team {% include "partials/support_request.html" %}.

To get a list of file names, sizes and dates in a particular directory
on nearline, run the following command with the necessary modifications.
Note that the `nlcompare` command traverses all subdirectories within
your chosen directory, and may therefore take some time if you verify a
directory at the top of a complex directory tree.

``` sl
nlcompare <local_directory> <nearline_directory>
```

This command will generate lists of files giving their last modified
times, sizes and file paths. If there are any differences, the lists
will be kept and you will be invited to compare the lists against each
other, which you can do using a comparison program such as `diff` or
`vimdiff`.
!!! prerequisite Warning
     The above check is useful only if the corresponding files in
     `/nesi/project` and/or `/nesi/nobackup` have not been modified or
     deleted, nor any new files added, since they were copied to nearline.
     For this reason, if you want to carry out this level of checking, you
     should do so as soon as possible after you have established that the
     `nlput` operation completed successfully.

## Level 3: Checksums

For especially important files, you can get a still higher level of
assurance by retrieving those files individually or in small numbers
from nearline and running checksums (e.g. SHA256 sums) on them,
comparing the checksums to the corresponding original files in
`/nesi/project` or `/nesi/nobackup`. If the checksums come out
identical, it is virtually certain that the files contain the same data,
even if their modification dates and times are reported differently.
!!! prerequisite Warning
     The above check is reliable only if the corresponding file in
     `/nesi/project` and/or `/nesi/nobackup` has not been modified since it
     was copied to nearline. For this reason, if you want to carry out this
     level of checking, you should do so as soon as possible after you have
     established that the `nlput` operation completed successfully and the
     file has been migrated to tape.
     Also, this check is very expensive, so you should not perform it on
     large numbers of files or on files that collectively take up a lot of
     disk space. Instead, please reserve this level of verification for
     your most valuable research data.