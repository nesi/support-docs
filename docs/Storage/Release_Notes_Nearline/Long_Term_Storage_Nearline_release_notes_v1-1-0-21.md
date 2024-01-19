---
created_at: '2021-07-28T00:05:31Z'
tags:
- releasenote
- nearline
title: Long Term Storage - Nearline release notes v1.1.0.21
vote_count: 0
vote_sum: 0
zendesk_article_id: 4404255007503
zendesk_section_id: 360000502675
---

*Released Wednesday 4 August 2021.*

This is a minor release incorporating bug fixes and improvements.

-   Certain server errors when a bad job is submitted now generate a
    more informative error message in the client program than, "Internal
    Server Error."
-   Nearline client programs now log to the `~/.librarian` directory, so
    you no longer need to explicitly decorate the Nearline command with
    complex strings in order to capture basic troubleshooting
    information.
-   A bug causing `nlput` with a file list to fail if any entries in the
    file list were missing from Nearline has been fixed. Now, `nlput`
    will work even though the file is not already present on Nearline.
-   `nlput` no longer throws an exception if, when you are prompted for
    a y/n response, you hit Enter thereby submitting an empty string.
    Instead, it asks the same question again.
-   If a local directory into which files are to be retrieved does not
    exist, `nlget` will now carry out the retrieval. Previously, `nlget`
    would create the directory but then abandon the retrieval.
-   We have clarified in help messages that `nlpurge` does not accept a
    single file (on Nearline) as the file to be purged. The argument
    that is not the project code must be either a directory on Nearline,
    or a local file list.
-   A bug has been fixed in the Nearline server whereby the server would
    incorrectly calculate the changes to the project's disk space and
    file count usage if an `nlpurge` command were to fail (or skip some
    files) for any reason after it was accepted by the server.
-   `nlpurge` can now be used to delete empty directories from Nearline,
    provided the directory is given directly as an argument and not
    included in a file list.
-   `nlpurge` deals gracefully with the situation in which a directory
    to be purged is not a subdirectory somewhere within the specified
    project's Nearline directory, by printing an informative error
    message.
-   `nlpurge` will no longer accept a file list argument if any of the
    entries in the file list point to files (on Nearline) that are
    outside the specified project's Nearline directory. Instead, an
    error message will be displayed, listing all affected lines in the
    file list.
-   A bug that required users to start `nlpurge` file list entries with
    `/scale_wlg_nearline/filesets/nearline/` has been fixed. Now,
    entries must start with the more intuitive `/nesi/nearline/`.
-   A bug causing `nlls` (and commands depending on it, like
    `nltraverse`) to fail if an empty directory is listed or included in
    the traverse operation has been fixed.