---
created_at: '2021-03-02T03:32:48Z'
hidden: false
position: 0
tags:
- releasenote
title: Long-term Storage - Nearline release notes v1.1.0.19
vote_count: 0
vote_sum: 0
zendesk_article_id: 360003551116
zendesk_section_id: 360000502675
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

*Released Thursday 4 March 2021.*

This release includes a number of significant changes and new features:

-   The `nltraverse` command is now supported by an `nlcompare` command.
    With `nlcompare`, you can compare a directory within `/nesi/project`
    or `/nesi/nobackup` with a corresponding directory on
    `/nesi/nearline`, and it will show any differences in file names,
    sizes, ownerships, permissions and last modified timestamps. Please
    note that `nlcompare` does not compare file contents.
-   File size limits are now in place when running `nlput` (not
    applicable to `nlget` or `nlpurge`):
    -   a minimum per-file size limit of 64 MB;
    -   a maximum per-file size limit of 1 TB.
-   Permission restrictions are now in place when running `nlput` (not
    applicable to `nlget` or `nlpurge`):
    -   You, as the operator, must be able to read every file selected
        for upload.
    -   The group of every file must match the project code you choose.
        If there is a mismatch, it may be that the project code has been
        mistyped.
    -   The permissions of every file must be set so that both the
        file's owner and the file's group are allowed to read and write
        the file.
    -   Where a directory (as opposed to a filelist) is specified for
        upload, that directory and every subdirectory therein must also
        be readable and executable by the operator, belong to the
        specified group, and be readable, writable and executable by the
        file owner and group.
-   Attempts to run `nlget` and `nlpurge` on files or directories not
    present on nearline will now fail before the job is submitted to the
    server, with a clear error message, instead of failing on the server
    side, after a delay and with an obscure error message.
-   Certain server errors that previously caused `KeyError` in the
    client will now be reported as
    `RuntimeError: Internal Server Error`.
-   Server-side logging and tracking with state files have been
    improved.
