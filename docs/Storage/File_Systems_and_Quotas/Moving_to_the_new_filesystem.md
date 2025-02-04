---
created_at: 2024-11-27
description: 
tags: [refresh]
status: new
search:
  boost: 2
---

Migration of your data from GPFS to WEKA will be ongoing for several weeks.
All data from your `home` and `project` directories will be copied, however **by default nothing will be migrated from `nobackup` directories**, you can override this by specifying nobackup content which should be preserved.

## Controlling which data gets migrated

You can place a file named `.RSYNC_FILTER` in your directory (`home`, `project`, or `nobackup`) telling rsync to include or exclude particular file paths from the migration to WEKA.  Note that the file is a hidden one, as its name starts with `.`.

Full documentation can be found [online](https://www.man7.org/linux/man-pages/man1/rsync.1.html#FILTER_RULES) or via `man rsync`.

### Examples

#### Nobackup directories

For nobackup directories the default filter rule excludes everything:

```rsync
# Default to excluding everything
- *
```

Below are some example `.RSYNC_FILTER` patterns.

<table><tbody>
  <tr>
    <td><code># Keep only the "Important" directory and its contents<br>+ /Important/***</code></td>
    <td><code> ── projects/<br>   ├── file.md<br>   ├── folder/<br>   │   ├── another_file.md<br>   │   └── 29421094.core<br>   └── secrets/<br></code></td>
  </tr></tbody>
</table>


=== "Keep One"
    ```rsync
    # Keep only the "Important" directory and its contents
    + /Important/***
    ```
=== "Keep All Except"
    ```rsync
    # Keep everything other than the "JobTmpDir" directory
    +! /JobTmpDir
    ```
=== "Keep All"
    ```rsync
    # Keep everything.
    + *
    ```
    !!! warning
        Unless you have a small amount of `nobackup` data, please give it more thought that that!  
        There is no point in copying across data which will be obsolete by the time you get login access to the new system.

#### Home and Project directories

We are running rsync with these filtering rules:

```rsync
# System generated directories which we don't want to copy
- /.snapshots
- /.policy
# Caches and corefiles don't need to be preserved
- /.cache
- core.[0-9]*
# Your additional rules from any .RSYNC_FILTER file are inserted here
: .RSYNC_FILTER
```

It is unlikely that you will want to add additional rules via an `.RSYNC_FILTER` file in these directories, but if you do then it is most likely to be a fairly simple exclusion such as

```rsync
# Leave behind this nearly obsolete directory
- /NotNeededAfter2024
```

### Rules

Each line of the file (other than comment lines and blank lines) specifies a rule.  The paths to the various files and sub-directories are tested against these rules in turn, with the first rule to match the path taking effect.  Each rule consists of an operator (`+` or `-`), an optional modifier (`!`), a single space, and then a pattern:

- `- pattern` excludes paths which match the pattern.

- `-! pattern` excludes paths which don't match the pattern.

- `+ pattern` includes paths which match the pattern.

- `+! pattern` includes paths which don't match the pattern.

### Patterns

A pattern can be as simple as the name of a subdirectory, but can also include wildcards:

- `*` matches anything other than a slash `/`, i.e: any component of a path.

- `**` matches anything, so `keep**` would include all of the contents of a directory named `~/keepthis`.

- A trailing `dir_name/***` matches both `dir_name/` and `dir_name/**`, i.e: the directory and all its contents.

- A leading `/` anchors the pattern in the top directory (`project`, `home`, or `nobackup`), so  `/tmp` matches `~/tmp` but not `~/other/tmp`.

- A trailing `/` indicates that the pattern should only match directories.

- `[` introduces a character class, such as `[0-9]` or `[[:alpha:]]`.

## Checking on progress

Logs can be found in `/opt/nesi/migration/syncs` which record each successful synchronisation.  
