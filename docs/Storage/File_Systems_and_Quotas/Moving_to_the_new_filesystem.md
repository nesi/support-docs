---
created_at: 2024-11-27
description: Migration of your data from GPFS to WEKA will be ongoing for several weeks.
tags: 
  - hpc3
  - refresh
status: new
search:
  boost: 2
---

!!! note
    GPFS is the filesystem on Mahuika. WEKA is the filesystem on the new HPC. When we refer to a path in GPFS, we are referring to a path on Mahuika. Similarily, a WEKA path is on the new HPC.

!!! WARNING WARNING  
    Before running substantial/production jobs on the new HPC, you ***MUST*** stop the synchronisation of your data from GPFS to WEKA, otherwise you will lose any new work you do on the new HPC. See the section on [halting the synchronisation from GPFS entirely](#halting-the-synchronisation-from-gpfs-entirely) below.  

Migration of your data from GPFS (Mahuika) to WEKA (new platforms) will be ongoing for several weeks.
We will be copying across a few project directories in parallel at a time, using _rsync_.
As each project directory is completed, the home directories of that project’s members will also be copied.
To keep the WEKA copy of your data as fresh as possible on the new platform, we will continue cycling through the projects that way, repeatedly syncing your directories from GPFS to WEKA until you ask us to stop.

On the second and successive rounds of these synchronisations, the nobackup directories will also be examined.
However **by default nothing will be migrated from nobackup directories**, as they often contain large amounts of data which is too transient to be worth preserving. You can override that, specifying nobackup content which should be preserved, as described below.

## Controlling which data gets migrated

You can place a file named `.RSYNC_FILTER` in your **Mahuika directory** (home, project, or nobackup) telling rsync to include or exclude particular file paths from the migration to WEKA on the new platform. Note that the file is a hidden one, as its name starts with `.`. Full documentation can be found [online](https://www.man7.org/linux/man-pages/man1/rsync.1.html#FILTER_RULES) or via `man rsync`, but in brief:

### Rules

Each line of the file (other than comment lines and blank lines) specifies a rule. The paths to the various files and sub-directories are tested against these rules in turn, with the first rule to match the path taking effect. Each rule consists of an operator (`+` or `-`), an optional modifier (`!`), a single space, and then a pattern:

- `+ pattern` includes paths which match the pattern.

- `- pattern` excludes paths which match the pattern.

- `+! pattern` includes paths which don't match the pattern.

- `-! pattern` excludes paths which don't match the pattern.

### Patterns

A pattern can be as simple as the name of a subdirectory, but can also include wildcards:

- `*` matches anything other than a slash `/`, i.e: any component of a path.

- `**` matches anything, so `keep**` would include all of the contents of a directory named `~/keepthis`.

- A trailing `dir_name/***` matches both `dir_name/` and `dir_name/**`, i.e: the directory and all its contents.

- A leading `/` anchors the pattern in the top directory, so  `/tmp` matches `~/tmp` but not `~/other/tmp`.

- A trailing `/` indicates that the pattern should only match directories.

- `[` introduces a character class, such as `[0-9]` or `[[:alpha:]]`.

### Home and Project directories

We are running rsync with these filtering rules:

```rsync
# System generated directories which we don't want to copy
- /.snapshots
- /.policy
# Caches and corefiles don't need to be preserved
- /.cache
- /*/.lmod.d
- core.[0-9]*
# Your additional rules from any .RSYNC_FILTER file are inserted here
: .RSYNC_FILTER
```

!!! note
    Despite beginning with "/" the RSYC_FILTER file uses relatives paths from the location of the file.

It is unlikely that you will want to add additional rules via an `.RSYNC_FILTER` file in these directories, but if you do then it is most likely to be a fairly simple exclusion such as

```rsync
# Leave behind this nearly obsolete directory
- /NotNeededAfter2024`.
```

### Nobackup directories

For nobackup directories we use the same filter rules as above with one additional rule at the end which excludes everything:

```rsync
# Default to excluding everything
- *
```

so you will have to override that if you want anything from your nobackup directory migrated into WEKA.
e.g:

```sh
echo '+ *' > /nesi/nobackup/nesi99999/.RSYNC_FILTER
```

However unless you have a small amount of nobackup data, please give it more thought that that! There is no point in copying across data which will be obsolete by the time you get login access to the new system, and the smaller the amount of data that is copied the more frequently it will be updated in the new WEKA filesystems, and so the more flexibility you will have about when you start working on the new system.

A more selective example of a simple .RSYNC_FILTER file would be:

```rsync
# Keep everything other than the "JobTmpDir" directory
+! /JobTmpDir
```

or

```rsync
# Keep only the "Important" directory and its contents
+ /Important/***
```

or equivalently:

```rsync
# Keep only the "Important" directory and its contents
+ /Important
+ /Important/**
```

Note that `+ /Important` by itself would only keep the (now empty) directory, and `+ /Important/**` by itself would never be tested against the important file names because the directory would be excluded and so never looked at by rsync.  `+ /Important**` would work but would also match a filename like, for example, `ImportantButNotReally.2023.tgz`.

If combining exclusions and inclusions, remember that the order matters, as the first rule to match each file path is the effective one:

```rsync
# Specific match appears before the generic wildcard, since "Temporary" would also match "***"
- /MyData/Temporary
+ /MyData/***
```

### Large multi-user projects

`.RSYNC_FILTER` files can be put in any directory on Mahuika, not just the top one, so responsibility for sub-directories can be delegated, which may be useful if you have a project or nobackup directory containing several per-user sub directories.  Users can then manage their own `.RSYNC_FILTER` files, just so long as the project's top level rules don’t completely exclude their directory in advance.  In such cases the `.RSYNC_FILTER` in the nobackup directory might look like:

```rsync
# Include all top-level directories (but not their contents), sub directories can specify their own inclusions. 
+ /*/
```

or

```rsync
# Keep everything except any stray non-directory top level content, sub directories can specify their own exclusions.
+ /*/***
```

## Using the new WEKA copy of your data

### Checking on progress

To check on how often or how recently your data was synced, the command `nn_data_migration_rsyncs` (on Mahuika) displays the five most recent rsync runs. You can give a project code to it as a command line argument, or else it will default to showing records for your home directory and the project and nobackup directories for each of your projects.  

Once you can log in to the new cluster and see the WEKA filsystems for yourself, please check that your important files have arrived there, particularly if you used a complex `.RSYNC_FILTER` file. You can use the command `df -h /nesi/project/<code>/` to compare the total amount of data at each end, though there could be differences in size due to [differences between the ways GPFS and WEKA work](../../General/FAQs/Mahuika_HPC3_Differences.md#disk).

### Protecting your new work from the ongoing data synchronisation

All home, project, and nobackup directories are still being rsynced from Mahuika's GPFS system every couple of days, and that rsync is configured to mirror rather than just update, because that makes sense before you start using the WEKA copy. So **any changes you make on the new platform / WEKA will get overwritten when the mirror synchronisation runs**. There are two ways to protect yourself from that:

#### Protecting specific file paths in WEKA

An `.RSYNC_FILTER` file in the WEKA copy on the new platform can protect new files there from deletion. For example, an `.RSYNC_FILTER` file containing the line `P /example` will protect the (sibling) directory named "example", so preventing rsync from modifying its contents. This is a distinct file from the one of the same name at the GPFS end, which will not be copied across to WEKA.

#### Halting the synchronisation from GPFS entirely

Once you are happy that all your data has been successfully copied to the new platforms / WEKA system, and you are ready to move to working entirely on the new platform, please place a file named `.GOODBYE_GPFS` in the top directory of each of your three GPFS filesets (home, project, and nobackup) **on Mahuika**.

  - `touch $HOME/.GOODBYE_GPFS`
  - `touch /nesi/project/your_project/.GOODBYE_GPFS`
  - `touch /nesi/nobackup/your_project/.GOODBYE_GPFS`
  
That signals to our rsyncing script to skip that directory entirely.

Once a home directory or both the filesets of a project have indicated ".GOODBYE_GPFS" **on Mahuika** we will stop even checking them, forever, so it will not be possible restart their rsyncing without asking NeSI Support to do it.

This will not only save your new workspace from regularly resetting back to the state it was on GPFS, it will also let the remaining directories of other users get updated more quickly.

#### Recovering deleted files

If you accidentally remove an important file from WEKA, you might be able to find an older copy of it from a filesystem snapshot, eg: in `/nesi/nobackup/.snapshots/`.

## Video tutorial

[Watch a demo of the instructions on this page](https://www.youtube.com/watch?v=BDuyeE3bIsc). 

If you have questions or need help adding the `.RSYNC_FILTER` or `.GOODBYE_GPFS` files to your directories, please contact [support@nesi.org.nz](mailto:support@nesi.org.nz).
