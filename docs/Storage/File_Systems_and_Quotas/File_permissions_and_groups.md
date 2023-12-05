---
created_at: '2018-05-21T05:14:00Z'
hidden: false
position: 2
tags: []
title: File permissions and groups
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000205435
zendesk_section_id: 360000033936
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

!!! prerequisite See also
     -   [How can I let my fellow project team members read or write my
         files?](../../General/FAQs/How_can_I_let_my_fellow_project_team_members_read_or_write_my_files.md)
     -   [How can I give read-only team members access to my
         files?](../../General/FAQs/How_can_I_give_read_only_team_members_access_to_my_files.md)
     -   [NeSI file systems and
         quotas](../../Storage/File_Systems_and_Quotas/NeSI_File_Systems_and_Quotas.md)

Access to data (i.e. files and directories) on NeSI is controlled by
POSIX permissions, supplemented with Access Control Lists (ACLs).
Default permissions differ from file system to file system.

## Group membership

Each user has a private user group, of which that user is by default the
only member. Each user is also a member of various other groups, such
as:

-   A group for each active NeSI project of which that user is a member
-   Groups for all active users, all active Mahuika users, all active
    Māui users, etc. as appropriate
-   A group representing all active NeSI users who are affiliated with
    the user's institution
-   Groups for specific licensed software to which that user has been
    granted access

You can see which groups you are a member of at any time by running the
following command on a Mahuika, Māui or Māui ancillary login node:

``` sl
groups
```

## Files in home directories

Your home directory is owned by you, and its group is usually your
personal group. (For historical reasons, some NIWA users' home
directories have `niwa_nesi_users` or `niwa_unix_users` as the group.)
By default, files and directories that are created in your home
directory, or copied to your home directory from another network or file
system, inherit this ownership scheme. You can override these defaults
depending on how you use the `cp`, `scp`, `rsync`, etc. commands. Please
consult the documentation for your copying program.
!!! prerequisite Warning
     If you choose to preserve the original owner and group, but that owner
     and group (name or numeric ID) don't both exist at the destination,
     your files may end up with odd permissions that you can't fix, for
     example if you're copying from your workstation to NeSI.

The default permissions mode for new home directories is as follows:

-   The owner has full privileges: read, write, and (where appropriate)
    execute.
-   The group and world have no privileges.

Some home directories have the "setgid" bit set. This has the effect
that files and subdirectories created within the home directory will
inherit the owner and group of their parent directory, rather than of
the person doing the creating.

Home directories and their contents do not have any ACLs by default.

## Files in project directories

Every new project almost always gets two directories, namely a
persistent directory in `/nesi/project` and a scratch directory in
`/nesi/nobackup`. Both these directories are group directories. Both top
level project directories are owned by root (i.e. the super-user) and
their group is the project group. Files and directories that are created
in either place are also in the project group, but the owner is the
creating user; or, if the entity doing the creating was an automatic
process, the user in whose name the process ran.

Your project directory and nobackup directory should both have the
"setgid" bit set, so that files created in either directory inherit the
project group.
!!! prerequisite Warning
     The setgid bit only applies the directory's group to files that are
     newly created in that directory, or copied to the directory over the
     internet. If a file or directory is moved or copied from elsewhere on
     the cluster, using for example the `mv` or `cp` command, that file or
     directory will keep its original owner and group. Moreover, a
     directory moved from elsewhere will probably not have its setgid bit
     set, meaning that files and subdirectories later created within that
     directory will inherit neither the group nor the setgid bit.
     You probably don't want this to happen. For instructions on how to
     prevent it, please see our article: [How can I let my fellow project
     team members read or write my
     files?](../../General/FAQs/How_can_I_let_my_fellow_project_team_members_read_or_write_my_files.md)

By default, the world, i.e. people not in the project team, have no
privileges in respect of a project directory, with certain exceptions.

Unlike home directories, project directories are set up with ACLs. The
default ACL for a project directory is as follows:

-   The owner of a file or directory is allowed to read, write, execute
    and modify the ACL of that file or directory
-   Every member of the file or directory's group is allowed to read,
    write and execute the file or directory, but not modify its ACL
-   Members of NeSI's support team are allowed to read and execute the
    file or directory, but not change it or modify its ACL

Some projects also have read and execute privileges granted to a group
"apache-web02-access".

Each directory has two ACLs: One is for the directory itself, and the
other is for files and directories that are created in future within
that directory. We have set up both of these ACLs to be the same as each
other for the two top level project directories.
!!! prerequisite Tip
     Some project teams, especially those with broader memberships, benefit
     from read-only groups. A read-only group gets added to a project's ACL
     once, and then individual members can be added to or removed from that
     group as required. This approach involves much less editing of file
     metadata than adding and removing individuals from the ACLs directly.
     If you would like a read-only group created for your project, please
     [contact us](mailto:support@nesi.org.nz).

The owner of a file or directory may create, edit or revoke that file or
directory's ACL and, in the case of a directory, also the directory's
default (heritable) ACL.
!!! prerequisite Warning
     Every time you edit an ACL of a file in the home or persistent project
     directory, the file's metadata changes and triggers a backup of that
     file. Doing so recursively on a large number of files and directories,
     especially if they together amount to a lot of disk space, can strain
     our backup system. Please consider carefully before doing a recursive
     ACL change, and if possible make the change early on in the life of
     the project on NeSI, so that only a few files are affected.

## Other directories

We may from time to time create and maintain other directories, for
example for users of a particular piece of software or database. If you
believe you have data storage requirements that don't neatly fit within
the home and project scheme described above, please [contact our support
team](mailto:support@nesi.org.nz). If we agree to set
up a special-purpose directory for you, we will discuss and agree upon a
suitable permissions model.