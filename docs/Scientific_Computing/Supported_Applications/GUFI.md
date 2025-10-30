---
created_at: '2025-10-30T17:00:00Z'
tags: []
title: GUFI
vote_count: 0
vote_sum: 0
---

GUFI (Grand Unified File Index) is a file system metadata indexing tool designed for large-scale data centers to enable fast, secure, and comprehensive searches of files and directories. It works by creating a hierarchical index that preserves file access permissions, allowing users to efficiently find and characterize data across multiple, potentially disparate file systems. This results in significantly faster search times compared to traditional methods.

There are two commands that GUFI provides:

* `gufi_find`: For finding files and subfolders in a directory
* `gufi_du`: For obtaining the size of files and folders

!!! warning
    This method uses a database that is updated on a weekly basis. It may not find or measure the size of files that were created or moved about mahuika within a week of them being created or moved. 

## Finding Files and Folders using GUFI

The usual method for searching for a file using the terminal is:

```sh
find path/to/folder/to/search -name "*NameOfFileToSearchFor*"
```

In GUFI, you provide the same arguments to `gufi_find` as you do with `find`:

```sh
module load .gufi
gufi_find path/to/folder/to/search -name "*NameOfFileToSearchFor*"
```

If you want to find the largest file in your folder:

```sh
gufi_find home/johndoe -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -n 1
gufi_find project/nesi12345 -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -n 1
gufi_find nobackup/nesi12345 -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -n 1
```

!!! warning
    You must give the path name beginning from `project` or `nobackup`. Local addresses starting with `.` will also not work. For example:

    * `nobackup/nesi12345/a_folder` is acceptible, but 
    * `/nesi/nobackup/nesi12345/a_folder`, `nesi12345/a_folder`, or `./nesi12345/a_folder` will not work. 


## Obtaining the Size of Files and Folders using GUFI

The usual method for obtaining the size of a file or folder using the terminal is:

```sh
du -s path/to/file/or/folder
```

In GUFI, you provide the same arguments to `gufi_du` as you do with `du`:

```sh
module load .gufi
gufi_du -s path/to/file/or/folder
```

If you want to obtain the number of files in a folder, such as `nobackup/nesi12345/a_folder`, you would do the following:

```sh
gufi_du --inodes -s nobackup/nesi12345/a_folder
```

For more options, see `gufi_du --help`

!!! warning
    You must give the path name beginning from `project` or `nobackup`. Local addresses starting with `.` will also not work. For example:

    * `nobackup/nesi12345/a_folder` is acceptible, but 
    * `/nesi/nobackup/nesi12345/a_folder`, `nesi12345/a_folder`, or `./nesi12345/a_folder` will not work. 

