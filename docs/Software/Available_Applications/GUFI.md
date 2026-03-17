---
created_at: '2025-10-30T17:00:00Z'
tags: 
  - locate
  - find
title: GUFI
vote_count: 0
vote_sum: 0
---


__GUFI__ (Grand Unified File Index) is designed for large-scale data centers to enable fast, secure and comprehensive searches of files and directories. It works by creating a hierarchical index, allowing users to quickly find and characterize data across multiple filesystems.

GUFI uses a database that is indexed on the weekend. It may not find or measure the size of files that were created or moved around after the index was updated.
<span style="color: orange;">
Note: </span> Currently, GUFI only works on `login03`. Check that you are connected to `login03` by running: `hostname`.  If you are not on `login03` you can connect by running: `ssh login03`.

There are two commands that GUFI provides:

* `gufi_find`: For finding files and subdirectories in a directory
* `gufi_du`: For obtaining the size of files and directories

For `gufi_find` and `gufi_du` to work, you must provide the full indexed pathname (e.g. `.` won't work). Please note that `/nesi/home` is required in place of `/home` for the GUFI search index. For example:

    * /nesi/home/$USER/foo
    * /nesi/nobackup/nesi12345/bar
    * /nesi/project/nesi12345/baz

## Prerequisite: Load `gufi` Module

To use `gufi_find` and `gufi_du`, you must first load the `gufi` module:

```sh
module load gufi
```

## Finding Files and Directories using GUFI

In GUFI, you provide the same arguments to `gufi_find` as you do with the `find` command (but with the full pathname specified: `.` or `~` won't be effective).
For example, if you want to find a dataset in your scratch directory:
    
```sh
    gufi_find /nesi/nobackup/nesi12345 -name foo.dat
```

Or if you want to find the largest file in your directory:

```sh
    gufi_find /nesi/home/$USER -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -n 1
    gufi_find /nesi/project/nesi12345 -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -n 1
    gufi_find /nesi/nobackup/nesi12345 -type f -printf '%s %p\n' 2>/dev/null | sort -nr | head -n 1
```

## Obtaining the Size of Files and Directories using GUFI


With GUFI, you provide the same arguments to `gufi_du` as you do with the `du` command:

If you want to find the size of your in your home directory:
    
```sh
    gufi_du -s /nesi/home/$USER
```

If you want to find the size of your project directory in `project` or `nobackup`:
    
```sh
    gufi_du -s /nesi/project/nesi12345
    gufi_du -s /nesi/nobackup/nesi12345
```

If you want to obtain the number of files a directory named `baz` in your scratch directory you would do the following:

```sh
    gufi_du --inodes -s /nesi/nobackup/nesi12345/baz
```

## Troubleshooting

### My file or directory exists, but `GUFI` does not include it during its search

If you recieve an error such as:<br> 
`Could not get realpath of "/search/nesi/home/foo": No such file or directory (2)`
it is likely that your directory has not been indexed by `GUFI` yet. You will need to wait until the end of the week for those files and directories to be indexed by `GUFI`. 

In the meantime, you can either use `find` or `du` instead of `gufi_find` or `gufi_du` as alternatives for these functions. 


### I get the message: `Does "XYZ" have treesummary data?`

If you get a message such as: `Error: Skipping directory "/search/nesi/nobackup/nesi99991": Permission denied (13)`

This means that `gufi_find` or `gufi_du` was not able to find any information about the path you gave it to search. This could be because:

1. The directory you are search in doesn't exist, 
    * Check that the path you provided is correct.
2. You don't have permissions to read the files you were trying to search 
    * You require read access.  For example you may need to be added to the project.
3. Your files and directories were created before they were included in the `GUFI` database. 
    * You will need to wait until the files and directories are indexed by `GUFI`.

### I can not use tab to autocomplete, and sometimes autocompleting using tab logs me out of my Mahuika login

This is a known problem. We are currently looking for a fix for this. 
