---
created_at: '2025-10-30T17:00:00Z'
tags: []
title: GUFI
vote_count: 0
vote_sum: 0
---

GUFI (Grand Unified File Index) is a file system metadata indexing tool designed for large-scale data centers to enable fast, secure, and comprehensive searches of files and directories. It works by creating a hierarchical index that preserves file access permissions, allowing users to efficiently find and characterize data across multiple, potentially disparate file systems. This results in significantly faster search times and lessens impact/load on parallel filesystems compared to traditional methods.

There are two commands that GUFI provides:

* `gufi_find`: For finding files and subfolders in a directory
* `gufi_du`: For obtaining the size of files and folders

!!! warning
    This method uses a database that is updated on a weekly basis. It may not find or measure the size of files that were created or moved about mahuika within a week of them being created or moved. 

!!! note
    The filesystems that `gufi_find` and `gufi_du` work on are:
    
    * `\home`
    * `\projects`
    * `\nobackup`

    For `gufi_find` and `gufi_du` to work, you must give the path name beginning from `project` or `nobackup`. Local addresses starting with `.` will also not work. For example:

    * `nobackup/nesi12345/a_folder` and `/nobackup/nesi12345/a_folder` are acceptible, but 
    * `/nesi/nobackup/nesi12345/a_folder`, `nesi12345/a_folder`, or `./nesi12345/a_folder` will not work. 


## Prerequisite: Must Load `gufi` Module 

To use `gufi_find` and `gufi_du`, you must load them by entering in the following command in mahuika:

```sh
module load .gufi
```

Without this, `gufi_find` and `gufi_du` will not be loaded. 


## Finding Files and Folders using GUFI

The usual method for searching for a file using the terminal is:

```sh
find path/to/folder/to/search -name "*NameOfFileToSearchFor*"
```

In GUFI, you provide the same arguments to `gufi_find` as you do with `find` (but starting with either `home`, `projects`, or `nobackup`):

```sh
gufi_find path/to/folder/to/search -name "*NameOfFileToSearchFor*"
```

!!! example
    If you want to find `.bashrc` in your home directory:
    
    ```sh
    gufi_find home/USERNAME -name .bashrc
    ```

    If you want to find the largest file in your folder:

    ```sh
    gufi_find home/USERNAME -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -n 1
    gufi_find project/nesi12345 -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -n 1
    gufi_find nobackup/nesi12345 -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -n 1
    ```

## Obtaining the Size of Files and Folders using GUFI

The usual method for obtaining the size of a file or folder using the terminal is:

```sh
du -hs path/to/file/or/folder
```

In GUFI, you provide the same arguments to `gufi_du` as you do with `du` (but starting with either `home`, `projects`, or `nobackup`):

```sh
gufi_du -hs path/to/file/or/folder
```

For more options, see `gufi_du --help`

!!! example
    If you want to find the size of your in your home directory:
    
    ```sh
    gufi_du -hs home/USERNAME
    ```

    If you want to find the size of your `.bashrc` in your home directory:
    
    ```sh
    gufi_du -hs home/USERNAME/.bashrc
    ```

    If you want to find the size of your project folder in `projects` or `nobackup`:
    
    ```sh
    gufi_du -hs project/nesi12345
    gufi_du -hs nobackup/nesi12345
    ```

    If you want to obtain the number of files in a folder, such as `nobackup/nesi12345/a_folder`, you would do the following:

    ```sh
    gufi_du --inodes -s nobackup/nesi12345/a_folder
    ```
