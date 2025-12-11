---
created_at: 2025-10-01
description: "Freezer Quick Start"
tags: 
  - Freezer
  - storage
---
!!! info s3cmd configuration required
    Please ensure you have [configured](Configuring_s3cmd.md) the s3cmd tool.

## Using s3cmd tool to interact with Freezer

Freezer uses the AWS S3 standard as a protocol for temporarily hosting data prior to writing it to tape.
All the data is stored in buckets temporarily before being written to tape - this is similar to a folder on a filesystem, but designed for scalable storage.

Freezer has two types of data storage classes:

- Glacier: data that is on tape
- Standard: data that is in the S3 bucket

Please note that your bucket has the same name as your Freezer allocation. If you have forgotten the name of your bucket, please <a href="mailto:support@nesi.org.nz?subject=Forgot%20my%20Freezer%20bucket%20name">email us</a> and let us know which project this is for.



## List contents and buckets

### List contents of a bucket

List all objects in a bucket.

```sh
s3cmd ls -r -l -H s3://<freezer-bucket>/
```

To just list the files and folders in a directory in your bucket:

```sh
s3cmd ls -l -H s3://<freezer-bucket>/path_to_your_directory
```

This can also be used to list all the objects in path.

!!! warning
    The listing only shows the storage class when using the `-l` option. This is important to determine whether the data is available or must be restored from tape first.

### List all buckets

List all objects in all buckets (only for project owners)

```sh
s3cmd la
```

### Storage usage by specific bucket

```sh
s3cmd du -H s3://<freezer-bucket>
   7G      1781 objects s3://<freezer-bucket>/
```

`s3cmd du -H` without specifying a bucket is only available for project owners.

!!! warning

    If you have a large number files the `s3cmd du` command will fail. If you wish to receive information from `s3cmd du` we advise using a compression command such as `tar` to reduce the total number of files before adding them to Freezer.
    
## Uploading objects

### Synchronise data

Synchronize a directory tree to S3 (checks files freshness using size and md5 checksum, unless overridden by options). If you wish to have additional informative output, please use the `--verbose` flag as well.

```sh
s3cmd sync --verbose yourfolder s3://<freezer-bucket>/your_directory/your_folder/
```

If you have already tried use `put` or `sync` but were interrupted, you can use the `--skip-existing` to skip putting files into your freezer that have already been transferred:

```sh
s3cmd sync --skip-existing --verbose yourfolder s3://<freezer-bucket>/your_directory/your_folder/
```

### Put objects

To transfer files/folders to S3 gateway to be archived. `cd` into where the file/folder is on Mahuika and then use `s3cmd put`.

!!! warning

    If you have files larger than 10TB you may need to change chunk size, please see the [Large files and chunk size](Other_Useful_Commands.md#large-files-and-chunk-size) section for details 
    
```sh
s3cmd put --verbose your_file s3://<freezer-bucket>/your_directory/your_file
```

``` out
INFO: Cache file not found or empty, creating/populating it.
INFO: Compiling list of local files...
INFO: Running stat() and reading/calculating MD5 values on 1 files, this may take some time...
INFO: Summary: 1 local files to upload
upload: 'your_file' -> 's3://<freezer-bucket>/your_directory/your_file'  [1 of 1]
 172202 of 172202   100% in    0s   920.89 KB/s  done
```

or folders

```sh
s3cmd put --recursive --verbose yourfolder s3://<freezer-bucket>/your_directory/your_folder/
```

``` out
INFO: Cache file not found or empty, creating/populating it.
INFO: Compiling list of local files...
INFO: Running stat() and reading/calculating MD5 values on 1 files, this may take some time...
INFO: Summary: 1 local files to upload
upload: 'yourfolder/your_file' -> 's3://<freezer-bucket>/your_directory/your_folder/yourfolder/yourfile'  [1 of 1]
 172202 of 172202   100% in    0s  1691.71 KB/s  done
```

Once the upload is successful, as signalled by the 'done' your files/folders stored as objects will automatically be archived to tape by the Freezer service. No further user action is needed. Do not delete your files from the bucket unless you do not wish for them to be archived to tape. They will remain in the bucket at least until they are copied to tape and likely for some time afterwards until the cache becomes too full and older files are removed.

Partially uploaded files will be deleted automatically.

!!! warning

  If `put` was interrupted before it could finish, use `s3cmd sync --skip-existing --verbose` to resume from the stage that you were originally copying from. See [Synchronise data](#synchronise-data) for more information. 

### Preview or dry-run

Use any of the `s3cmd` options with `-n, --dry-run`to preview the action.

Only shows what should be uploaded or downloaded but doesn't actually do it. May still perform S3 requests to get bucket listings and other information though (only for file transfer commands).

## Restoring objects
### List objects before restore

List contained objects/files/folders:

```sh
s3cmd ls -l -H s3://<freezer-bucket>/your_directory/your_folder/
```

``` out
                    DIR                                                    s3://<freezer-bucket>/your_directory/your_folder/MY_TEST/
2025-06-16 23:13    10G  8add0bf4f023e3dbd36a329d1eae5bbd-684  STANDARD     s3://<freezer-bucket>/your_directory/your_folder/10G_test.file
2025-06-16 23:30    10G  8add0bf4f023e3dbd36a329d1eae5bbd-684  STANDARD     s3://<freezer-bucket>/your_directory/your_folder/10G_copy.file
2025-06-17 01:26     0   d41d8cd98f00b204e9800998ecf8427e     STANDARD     s3://<freezer-bucket>/your_directory/your_folder/1test.txt
```

or all objects recursive -r or --recursive

```sh
s3cmd ls -r -l -H s3://<freezer-bucket>/your_directory/your_folder/
```

``` out
2025-06-16 23:13    10G  8add0bf4f023e3dbd36a329d1eae5bbd-684  STANDARD     s3://<freezer-bucket>/your_directory/your_folder/10G_test.file
2025-06-16 23:30    10G  8add0bf4f023e3dbd36a329d1eae5bbd-684  STANDARD     s3://<freezer-bucket>/your_directory/your_folder/10G_copy.file
2025-06-17 01:31    14   95b28899a460dd8971705dfcd0f5f0d4     STANDARD     s3://<freezer-bucket>/your_directory/your_folder/MY_TEST/annotations/3/4/test3.txt
2025-06-17 01:31    14   e76c3a8939fb031bab02a89f6fab520b     STANDARD     s3://<freezer-bucket>/your_directory/your_folder/MY_TEST/annotations/3/test2.txt
2025-06-17 01:31    14   be2520c884c1be55bab187374a982b12     STANDARD     s3://<freezer-bucket>/your_directory/your_folder/MY_TEST/raw_data/test1.txt
2025-06-17 01:26     0   d41d8cd98f00b204e9800998ecf8427e     STANDARD     s3://<freezer-bucket>/your_directory/your_folder/test/test.txt
```

### Restore from tape

It is necessary to restore data from the tape (Glacier) prior to retrieving it. To restore file from Glacier storage:

```sh
s3cmd restore --recursive --verbose s3://<freezer-bucket>/your_directory/data_folder/
```

``` out
INFO: Retrieving list of remote files for s3://<freezer-bucket>/your_directory/your_folder/ ...
INFO: Summary: Restoring 6 remote files for 1 days at Standard priority
restore: 's3://n<freezer-bucket>/your_directory/your_folder/10G.file'
restore: 's3://<freezer-bucket>/your_directory/your_folder/10G_copy.file'
restore: 's3://<freezer-bucket>/your_directory/your_folder/MY_TEST/annotations/3/4/test3.txt'
restore: 's3://<freezer-bucket>/your_directory/your_folder/MY_TEST/annotations/3/test2.txt'
restore: 's3://<freezer-bucket>/your_directory/your_folder/MY_TEST/raw_data/test1.txt'
restore: 's3://<freezer-bucket>/your_directory/your_folder/test.txt'
```

By default files will remain in the S3 bucket for 1 day. If longer is required, this can be modified at the time of file restoration: 

```sh
s3cmd restore --recursive s3://<freezer-bucket>/your_directory/data_folder/ --restore-days=1
```

### Get objects after restore

!!! info
    Data needs to be restored (to storage class `STANDARD`) from the tape (storage class `GLACIER`), before it can be retrieved.

Example to get or download the directory `data_folder` and all contained objects/files/folders:

1. Create the `data_folder` you want to retrieve in file, and change directory into `data_folder`.
  ```sh
  mkdir -p data_folder
  cd data_folder
  ```

2. Retrieve the data from Freezer
  ```sh
  s3cmd get --recursive s3://<freezer-bucket>/your_directory/data_folder/
  ```

This will place the all files and subdirectories in the above `data_folder` into your current directory.


## s3cmd reference

[s3cmd tool](https://s3tools.org/usage)
