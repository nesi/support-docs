---
created_at: 2024-11-27
description: 
tags: [refresh]
---

Migration of your data from GPFS to WEKA will be ongoing for several weeks.
We will be copying across a few project directories in parallel at a time, using rsync.
As each project directory is completed, the home directories of that project’s members will also be copied.
To keep the WEKA copy of your data as fresh as possible, we will continue cycling through the projects, repeatedly syncing your directories from GPFS to WEKA until you ask us to stop.

On the second and successive rounds of synchronisation, the corresponding nobackup directories will also be copied across, however since they are larger and often contain data which is too transient to be worth preserving, we ask that you specify which files you want included from those, as described below.

## Controlling which data gets migrated

You can place a file named `.RSYNC_FILTER` in your directory (home, project, or nobackup) to control which files are included or excluded from migration to WEKA.  Note that the file is a hidden one, as its name starts with `.`. Full documentation can be found [online](https://www.man7.org/linux/man-pages/man1/rsync.1.html#FILTER_RULES) or via `man rsync`, but in brief:

### Rules

Each line of the file (other than comment lines and blank lines) specifies a rule.  The paths to the various files and sub-directories are tested against these rules in turn, with the first rule to match the path taking effect.  Each rule consists of an operator (`+` or `-`), an optional modifier (`!`), a single space, and then a pattern:

- `-` pattern excludes paths which match the pattern.

- `-!` pattern excludes paths which don't match the pattern.

- `+` pattern includes paths which match the pattern.

- `+!` pattern includes paths which don't match the pattern.

### Patterns

A pattern can be as simple as the same of a subdirectory, but can also include wildcards:

- `*` matches anything other than a slash `/`, ie: any component of a path.

- `**` matches anything, so `keep**` would include all of the contents of a directory named `~/keepthis`.

- A trailing `dir_name/***` matches both `dir_name/` and `dir_name/**`, ie: the directory and all its contents.

- A leading `/` anchors the pattern in the top directory, so  `/tmp` matches `~/tmp` but not `~/other/tmp`.

- A trailing `/` indicates that the pattern should only match directories.

- `[` introduces a character class, such as `[0-9]` or `[[:alpha:]]`.

### Home and Project directories

We are running rsync with these filtering rules:

```sh
# System generated directories which we don't want to copy
- /.snapshots
- /.policy
# Caches and corefiles don't need to be preserved
- /.cache
- core.[0-9]*
# Your additional rules from any .RSYNC_FILTER file are inserted here
: .RSYNC_FILTER
```

It is unlikely that you will want to add additional rules via an `.RSYNC_FILTER` file in these directories, but if you do then it is most likely to be a fairly simple exclusion such as `- /NotNeededAfter2024`.

### Nobackup directories

For nobackup directories we use the same filter rules as above with one additional rule at the end so that the default is to not migrate any of the contents of your nobackup directory:

```rsync
# Default to excluding everything
- *
```

so you will have to override that if you want anything migrated to WEKA. eg:

```sh
echo '+ *' > /nesi/nobackup/nesi99999/.RSYNC_FILTER
```

However unless you have a very small amount of nobackup data, please give it more thought that that!  There is no point in copying across data which will be obsolete by the time you get login access to the new system, and the smaller the amount of data that is copied the more frequently it will be updated in the new WEKA filesystems, and so the more flexibility you will have about when you start working on the new system.

A more selective example of a simple .RSYNC_FILTER file would be:

```sh
# Keep everything other than the "JobTmpDir" directory
+! JobTmpDir
```

or

```sh
# Keep only the "Important" directory and its contents
+ Important/***
```

or equivalently:

```sh
# Keep only the "Important" directory and its contents
+ /Important
+ /Important/**
```

Note that `+ /Important` by itself would only keep the (now empty) directory, and `+ /Important/**` by itself would never be tested against the important file names because the directory would be excluded and so never looked at by rsync.  `+ /Important**` would work but would also match a filename like, for example, `ImportantButNotReally.2023.tgz`.

## Checking on progress

Logs can be found in `/opt/nesi/migration/syncs` which record each successful synchronisation.  

## Overlapping use of the old and new systems

At some point after all of your needed data has been copied across we will be migrating your work to the new system. It will be simplest to avoid using the old and new systems at the same time, but for some users there may be an overlap period when you which to access both systems, and if so care will need to be taken, because rsync can not tell the difference between a file you created directly on WEKA versus one which was copied from GPFS and has since deleted there.  If you wish to protect a directory on WEKA while still syncing other changing data from GPFS then that can be done with the same filtering mechanism described above.  A rule such as `- TestingOnWEKA` in your `~/.RSYNC_FILER` file (on the old, GPFS end) should protect a corresponding `~/TestingOnWEKA` directory on WEKA from being deleted by rsync.
