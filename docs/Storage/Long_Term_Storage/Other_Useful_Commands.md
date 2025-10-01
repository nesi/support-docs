---
created_at: 2025-10-01
description: "Other Freezer commands"
tags: 
  - Freezer
  - storage
---

## Compressing files
Many files can be compressed into a single 'tarball'. This tarball can be uploaded to Freezer as a single file. Then when files need to be accessed again they can be un-tarred.

``` sh
# create tarball 'name.tar.gz'
tar -czf name.tar.gz /path/containing/files/

# un-tarr
tar -xzf tarname.tar.gz
```

## Large files and chunk size

Large files will automatically be split into smaller "chunks" for ease of upload. 

By default, if you have configured s3cmd with *--multipart-chunk-size-mb=1024*, 
the chunks will have a default value of 1GB. Otherwise the default chunk value is 15MB, 
which is typically too small for large files and should be increased. 
We recommend reconfiguring the S3 interface using the --multipart-chunk-size-mb parameter as above.

Important considerations:
- Any chunk size can be specified, however only *10,000* chunks can be created per file. 
- if the chunk size is too small you will get the following error `ERROR: Parameter problem: Chunk size 15 MB results in more than 10,000 chunks. Please increase --multipart-chunk-size-mb`.  

To determine an optimal chunk size for very large files, use the rough formula *file size/10000*. 
Add a buffer to ensure you're safely under the limit.  

For instance, for a file of ~50TB, a chunk size of 5 GB is a minimum. 
This can be set by using the flag `--multipart-chunk-size-mb=5120` to the command.  

Example: 

```sh
s3cmd put --multipart-chunk-size-mb=1000 yourfile s3://<freezer_bucket>/your_directory/your_file/ --verbose
```

``` out
upload: 'your_file' -> 's3://<freezer_bucket>/your_directory/your_file/'  [part 1 of 23, 1000MB] [1 of 1]
 1048576000 of 1048576000   100% in   25s    39.62 MB/s  done

....

upload: 'your_file' -> 's3://<freezer_bucket>/your_directory/your_file/'  [part 23 of 23, 169MB] [1 of 1]
 177209344 of 177209344   100% in    4s    35.90 MB/s  done
```

## Moving files
To move files within a bucket:

``` sh
s3cmd mv s3://<freezer_bucket>/your_directory/your_file.txt s3://<freezer_bucket>/other_directory/your_file.txt
```
``` out

move: 's3://<freezer_bucket>/your_directory/your_file.txt' -> 's3://<freezer_bucket>/other_directory/your_file.txt'  [1 of 1]
```

## Copying files
To make a copy of a file within a bucket to another location:

``` sh
s3cmd cp s3://<freezer_bucket>/your_directory/your_file.txt s3://<freezer_bucket>/your_directory/your_file_copy.txt
```

``` out
remote copy: 's3://<freezer_bucket>/your_directory/your_file.txt' -> 's3://<freezer_bucket>/your_directory/your_file_copy.txt'  [1 of 1]
```

## Deleting data

!!! warning

    Please be very careful using the `rm` command to delete data as the data can't be recovered once deleted

Data can be deleted from both the bucket (cache) and from tape (thought this is a flag to overwrite, rather than actual deletion)

```sh
s3cmd rm s3://<freezer_bucket>/your_directory/data_folder/
```

This command can also be used recursively.

```sh
s3cmd rm --recursive s3://<freezer_bucket>/your_directory/data_folder/
```

## s3cmd reference

[s3cmd tool](https://s3tools.org/usage)
