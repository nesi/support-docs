---
created_at: '2021-08-30T03:19:42Z'
hidden: false
tags:
- releasenote
- nearline
title: Long Term Storage - Nearline release notes v1.1.0.22
vote_count: 0
vote_sum: 0
zendesk_article_id: 4405757918095
zendesk_section_id: 360000502675
---

*Released Friday 27 August 2021.*

This is a minor release incorporating bug fixes and improvements.

-   A bug causing the programs `nlls`, `nltraverse` and `nlcompare` to
    misbehave when dealing with invisible files and directories (whose
    names start with `.`), and other files and directories whose names
    contain unorthodox characters such as spaces or other characters
    having special meaning to the shell, has been fixed.
-   A bug causing `nlls` to return `Internal Server Error` when the
    operator specifies a subdirectory of a project directory that
    doesn't exist on Nearline has been fixed. The error
    `no such file or directory` is now returned instead.
-   Some small improvements have been made to server configuration
    parsing and detection of inappropriate or missing configuration
    values.

During testing of this release, we found that attempts to run `nlput` or
`nlget` using arguments containing spaces, especially multiple
consecutive spaces, fail at the Nearline datamover stage while running
`rsync`. This issue has been recorded and documented. For now, the
recommended workaround is to rename such files or directories before
uploading them to Nearline, or, alternatively, to store them in an
archive that does not contain spaces in its name. 