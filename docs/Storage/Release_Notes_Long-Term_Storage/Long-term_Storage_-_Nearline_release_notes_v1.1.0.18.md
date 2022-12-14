---
created_at: '2021-01-12T07:20:01Z'
hidden: false
label_names:
- releasenote
position: 0
title: Long-term Storage - Nearline release notes v1.1.0.18
vote_count: 0
vote_sum: 0
zendesk_article_id: 360002655596
zendesk_section_id: 360000502675
---

This release incorporates several minor but significant bug fixes and
new features.

In particular:

-   To run `nljobstatus` with a particular job ID, you no longer need
    the `-j` switch before the job ID. `nljobstatus <jobID>` will
    suffice.
-   The `nlput` program will now check to see whether any of the files
    requested for upload already exist on nearline. If it finds any of
    them, it will ask you if you want to continue anyway, warning you
    that the already existing files will not be altered or updated by
    the nlput process.
-   The `nlput` program will also offer to create a filelist of already
    existing files, in order to help you more conveniently delete them
    from nearline if you wish to replace them with an updated version.
    Users taking advantage of this feature are encouraged to review the
    filelist after it has been generated, in case there are any files
    included that you do not wish to delete.
-   `nlput`, `nlget` and `nlpurge` now verify that files and filelists
    are in allowed locations, and (in the case of filelists) that the
    individual filelist entries are in allowed locations:
    -   For `nlput`, all files to be uploaded must be within either
        `/nesi/project` or `/nesi/nobackup`, whether they come from a
        directory or are specified in a filelist
    -   For `nlget`, all files to be retrieved must be within
        `/nesi/nearline`, and the destination must be within
        `/nesi/project` or `/nesi/nobackup`
    -   For `nlpurge`, all files to be deleted must be within
        `/nesi/nearline`
    -   For `nlput`, `nlget` and `nlpurge` with filelists, the filelist
        must be within `/nesi/project` or `/nesi/nobackup`
-   A bug causing projects to be locked indefinitely when `nlput` is
    given a filelist as an argument has been fixed.
-   An attempt to remove a nonexistent directory from nearline using
    `nlpurge` will no longer lock the project.
-   Various bugs causing locks to persist on nearline projects even once
    the locking process has ended have been fixed. Previously, many
    error conditions causing nearline server tasks to end prematurely
    would have left orphaned locks on involved projects.
