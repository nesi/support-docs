---
created_at: '2025-10-30T17:00:00Z'
tags: []
title: GUFI
vote_count: 0
vote_sum: 0
---

test

GUFI (Grand Unified File Index) is a file system metadata indexing tool designed for large-scale data centers to enable fast, secure, and comprehensive searches of files and directories. It works by creating a hierarchical index that preserves file access permissions, allowing users to efficiently find and characterize data across multiple, potentially disparate file systems. This results in significantly faster search times and lessens impact/load on parallel filesystems compared to traditional methods.

There are two commands that GUFI provides:

* `gufi_find`: For finding files and subfolders in a directory
* `gufi_du`: For obtaining the size of files and folders

!!! warning
    This method uses a database that is updated on a weekly basis. It may not find or measure the size of files that were created or moved around Mahuika within the last week. 
    
    * We do indexing of GUFI at the weekend. 

!!! note
    The filesystems that `gufi_find` and `gufi_du` work on are:
    
    * `/nesi/home`
    * `/nesi/projects`
    * `/nesi/nobackup`

    For `gufi_find` and `gufi_du` to work, you must give the path name beginning with `/nesi/home`, `/nesi/project` or `/nesi/nobackup`. Local addresses starting with `.` will also not work. For example:

    * `/nesi/home/$USER/a_folder`
    * `/nesi/nobackup/nesi12345/a_folder`
    * `/nesi/nobackup/nesi12345/a_folder`


## Prerequisite: Must Load `gufi` Module

To use `gufi_find` and `gufi_du`, you must load them by entering in the following command in Mahuika:

```sh
module load .gufi
```


## Finding Files and Folders using GUFI

The usual method for searching for a file using the terminal is:

```sh
find full/path/to/folder/to/search -name <your_file>
```

In GUFI, you provide the same arguments to `gufi_find` as you do with `find`:

```sh
gufi_find /nesi/full/path/to/folder/to/search -name <your_file>
```

!!! example
    If you want to find `.bashrc` in your home directory:
    
    ```sh
    gufi_find /nesi/home/$USER -name .bashrc
    ```

    If you want to find the largest file in your folder:

    ```sh
    gufi_find /nesi/home/$USER -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -n 1
    gufi_find /nesi/project/nesi12345 -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -n 1
    gufi_find /nesi/nobackup/nesi12345 -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -n 1
    ```

## Obtaining the Size of Files and Folders using GUFI

The usual method for obtaining the size of a file or folder using the terminal is:

```sh
du -s full/path/to/file/or/folder
```

In GUFI, you provide the same arguments to `gufi_du` as you do with `du` (but starting with either `home`, `projects`, or `nobackup`):

```sh
gufi_du -s /nesi/full/path/to/file/or/folder
```

For more options, see `gufi_du --help`

!!! example
    If you want to find the size of your in your home directory:
    
    ```sh
    gufi_du -s /nesi/home/$USER
    ```

    If you want to find the size of your `.bashrc` in your home directory:
    
    ```sh
    gufi_du -s /nesi/home/$USER/.bashrc
    ```

    If you want to find the size of your project folder in `projects` or `nobackup`:
    
    ```sh
    gufi_du -s /nesi/project/nesi12345
    gufi_du -s /nesi/nobackup/nesi12345
    ```

    If you want to obtain the number of files in a folder, such as `nobackup/nesi12345/a_folder`, you would do the following:

    ```sh
    gufi_du --inodes -s /nesi/nobackup/nesi12345/a_folder
    ```

## Troubleshooting

### My file or folder exists, but `GUFI` does not include it during its search

If your file or folder exists but `GUFI` does not find it, it is likely that your folder has not been indexed by `GUFI` yet. You will need to wait until the end of the week for those files and folders to be indexed by `GUFI`. 

* In the meantime, you can either use `find` or `du` instead of `gufi_find` or `gufi_du` as alternatives for these functions. 

!!! example

    ```sh
    john.doe@login03:~$ gufi_find /nesi/home/new_folder
    Could not get realpath of "/search/nesi/home/new_folder": No such file or directory (2)
    ```

### I get the message: `Does "XYZ" have treesummary data?`

If you get a message like this:

```sh
gufi_du --inodes -s /nesi/nobackup/nesi99991
Error: Skipping directory "/search/nesi/nobackup/nesi99991": Permission denied (13)
0 nesi/nobackup/nesi99991
Warning: Did not get any results from gufi_query.
Does "nesi/nobackup/nesi99991" have treesummary data?
```

This means that `gufi_find` or `gufi_du` was not able to find any information about the path you gave it to search. This could be because:

1. The folder you are search in doesn't exist, 
2. You don't have permissions to look at the files and folders that you were trying to search in, or 
3. Your files and folders were created before they were included in the `GUFI` database. 

If 3 applies to you, you will need to wait until the end of the weekend for those files and folders to be indexed by `GUFI`.

### I get the message: `Error: Skipping directory "nesi/nobackup/XYZ": Permission denied (13)`

If you see this error, this is because you do not have the correct permissions to view this directory. 

* If you want to use `GUFI` on this directory, you will need to get read permissions from the person who created this directory. 

!!! example

    ```sh
    john.doe@login03:nobackup/nesi12345$ gufi_du /nesi/nobackup/nesi12345/test.txt
    Error: Skipping directory "nesi/nobackup/nesi12345/test.txt": Permission denied (13)
    ```

### I can not use tab to autocomplete, and sometimes autocompleting using tab logs me out of my Mahuika login

This is a known problem. We are currently looking for a fix for this. 
