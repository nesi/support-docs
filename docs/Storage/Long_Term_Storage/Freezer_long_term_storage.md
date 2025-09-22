---
created_at: 2025-04-04
description: "Our Freezer service allows you to store your data on tape for long term storage."
tags: 
  - Freezer
  - storage
---

Freezer, powered by Versity, is our completely redesigned long-term storage service to support research data. It consists of a staging area (disk) connected to a tape library. Users gain access to more persistent storage space for their research data, in return for slower access to those files that are stored on tape. We recommend that you use Freezer for larger datasets that you will only need to access occasionally and will not need to change in situ. The retrieval of data may be delayed, due to tape handling, queuing of the freezer backend service and size of the data to be ingested or retrieved.

Due to the tape storage backend, Freezer is intended for use with relatively large files and should not be used for a large number of small files. Freezer is compatible with the common Amazon Web Services Simple Storage Service (AWS S3) cloud protocol and existing tools such as those used for accessing AWS S3 service.

## Getting started

Before getting started, you will need an allocation and credentials. To apply for an allocation go to [MyNeSI](https://my.nesi.org.nz/).
Once onboarded, you can start to use Freezer. Currently Freezer is only available via specific access points, HPC3 and Mahuika. We are currently completing security hardening prior to opening Freezer to wider access.

### Interacting with Freezer

We recommend using `s3cmd` for interacting with Freezer. The `s3cmd` tool is available by default on HPC3 and Mahuika. It is not necessary to load any modules to use it.

### Configure s3cmd

You will need to configure the `s3cmd` tool before you use it for the first time. Configuring the `s3cmd` allows for user credentials and default buckets to be remembered. This will only need to be done once.

```sh
s3cmd --configure --multipart-chunk-size-mb=1024
```

Enter the following details when prompted in the terminal:

`Access Key`: Your NeSI user ID

`Secret Key`: This is the code from the 1-time link in your Freezer allocation email. Please let us know if you need to <a href="mailto:support@nesi.org.nz?subject=Reset%20Freezer%20Secret%20Key">reset this key</a>.

Please copy and paste the sections in <span style="color:blue">blue</span>.

<pre><code>Enter new values or accept defaults in brackets with Enter.
Refer to user manual for detailed description of all options.
Access key and Secret key are your identifiers for AWS S3. Leave them empty for using the env variables.
Access Key: <span style="color:green"><b>User ID</b></span>
Secret Key: <span style="color:green"><b>Your Freezer Secret Key</b></span>
Default Region: <span style="color:blue"><b>akl-1</b></span>
Use "s3.amazonaws.com" for S3 Endpoint and not modify it to the target Amazon S3.
S3 Endpoint: <span style="color:blue"><b>freezer.nesi.org.nz:7070</b></span>

Use "%(bucket)s.s3.amazonaws.com" to the target AWS S3. "%(bucket)s" and "%(location)s" vars can be used
if the target S3 system supports dns based buckets.
DNS-style bucket+hostname:port template for accessing a bucket:  <span style="color:blue"><b>210.7.37.122:7070</b></span>
Encryption password is used to protect your files from reading
by unauthorized persons while in transfer to S3
Encryption password: <span style="color:green"><b>Leave blank, </b>press &lt;Enter&gt;</span>
Path to GPG program [/usr/bin/gpg]: <span style="color:green"><b>Leave blank, </b>press &lt;Enter&gt;</span>

When using secure HTTPS protocol all communication with AWS S3
servers is protected from 3rd party eavesdropping. This method is
slower than plain HTTP, and can only be proxied with Python 2.7 or newer
Use HTTPS protocol: <span style="color:blue"><b>Yes</b></span>
On some networks all internet access must go through a HTTP proxy.
Try setting it here if you can't connect to S3 directly
HTTP Proxy server name: <span style="color:green"><b>Leave blank, </b>press &lt;Enter&gt;</span>
</code></pre>

You will then be presented with a summary.
<pre><code>New settings:
  Access Key: User ID
  Secret Key: Your Freezer Secret Key
  Default Region: akl-1
  S3 Endpoint: freezer.nesi.org.nz:7070
  DNS-style bucket+hostname:port template for accessing a bucket: 210.7.37.122:7070
  Encryption password:
  Path to GPG program: /usr/bin/gpg
  Use HTTPS protocol: True
  HTTP Proxy server name:
  HTTP Proxy server port: 0
</code></pre>

Press `Y` to confirm.

<pre><code>Test access with supplied credentials? [Y/n] <span style="color:blue"><b>Y</b></span>
Please wait, attempting to list all buckets...
Success. Your access key and secret key worked fine :-)

Now verifying that encryption works...
Not configured. Never mind.

Save settings? [y/N] <span style="color:blue"><b>y</b></span>
Configuration saved to '/home/&lt;user_id&gt;/.s3cfg'
</code></pre>

## Using s3cmd tool to interact with Freezer

Freezer uses the AWS S3 standard as a protocol for temporarily hosting data prior to writing it to tape.
All of the data is stored in buckets - this is similar to a folder in a filesystem, but designed for scalable storage.

Freezer has two types of data storage classes:

- Glacier: data that is on tape
- Standard: data that is in the S3 bucket

Please note that your bucket has the same name as your Freezer allocation. If you have forgotten the name of your bucket, please <a href="mailto:support@nesi.org.nz?subject=Forgot%20my%20Freezer%20bucket%20name">email us</a> and let us know which project this is for.

### List contents of a bucket

List all objects in a bucket.

```sh
s3cmd ls -r -l -H s3://<freezer_bucket>/
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
s3cmd du -H s3://<freezer_bucket>
   7G      1781 objects s3://<freezer_bucket>/
```

`s3cmd du -H` without specifying a bucket is only available for project owners.

!!! warning

    If you have a large number files the `s3cmd du` command will fail. If you wish to receive information from `s3cmd du` we advise using a compression command such as `tar` to reduce the total number of files before adding them to Freezer.
    

### Put objects

To transfer files/folders to S3 gateway to be archived. CD into where the file/folder is on Mahuika and then use s3cmd put

!!! warning

    If you have large files you may need to change chunk size, please see next section for details
    
```sh
s3cmd put --verbose your_file s3://<freezer_bucket>/your_directory>/your_file
```

``` out
INFO: Cache file not found or empty, creating/populating it.
INFO: Compiling list of local files...
INFO: Running stat() and reading/calculating MD5 values on 1 files, this may take some time...
INFO: Summary: 1 local files to upload
upload: 'your_file' -> 's3://<freezer_bucket>/your_directory>/your_file'  [1 of 1]
 172202 of 172202   100% in    0s   920.89 KB/s  done
```

or folders

```sh
s3cmd put --recursive --verbose yourfolder s3://<freezer_bucket>/your_directory/your_folder/
```

``` out
INFO: Cache file not found or empty, creating/populating it.
INFO: Compiling list of local files...
INFO: Running stat() and reading/calculating MD5 values on 1 files, this may take some time...
INFO: Summary: 1 local files to upload
upload: 'yourfolder/your_file' -> 's3://<freezer_bucket>/your_directory/your_folder/yourfolder/yourfile'  [1 of 1]
 172202 of 172202   100% in    0s  1691.71 KB/s  done
```

Once the upload is successful, as signalled by the 'done' your files/folders stored as objects will automatically be archived to tape by the Freezer service. No further user action is needed. Do not delete your files from the bucket unless you do not wish for them to be archived to tape. They will remain in the bucket at least until they are copied to tape and likely for some time afterwards until the cache becomes too full and older files are removed.

### Large files and chunk size

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

### Synchronise data

Synchronize a directory tree to S3 (checks files freshness using size and md5 checksum, unless overridden by options). If you wish to have additional informative output, please use the `--verbose` flag as well.

```sh
s3cmd sync yourfolder s3://<freezer_bucket>/your_directory/your_folder/
```

### Preview or dry-run

Use any of the `s3cmd` options with `-n, --dry-run`to preview the action.

Only shows what should be uploaded or downloaded but doesn't actually do it. May still perform S3 requests to get bucket listings and other information though (only for file transfer commands).

### List objects before restore

List contained objects/files/folders:

```sh
s3cmd ls -l -H s3://<freezer_bucket>/your_directory/your_folder/
```

``` out
                    DIR                                                    s3://<freezer_bucket>/your_directory/your_folder/MY_TEST/
2025-06-16 23:13    10G  8add0bf4f023e3dbd36a329d1eae5bbd-684  STANDARD     s3://<freezer_bucket>/your_directory/your_folder/10G_test.file
2025-06-16 23:30    10G  8add0bf4f023e3dbd36a329d1eae5bbd-684  STANDARD     s3://<freezer_bucket>/your_directory/your_folder/10G_copy.file
2025-06-17 01:26     0   d41d8cd98f00b204e9800998ecf8427e     STANDARD     s3://<freezer_bucket>/your_directory/your_folder/1test.txt
```

or all objects recursive -r or --recursive

```sh
s3cmd ls -r -l -H s3://<freezer_bucket>/your_directory/your_folder/
```

``` out
2025-06-16 23:13    10G  8add0bf4f023e3dbd36a329d1eae5bbd-684  STANDARD     s3://<freezer_bucket>/your_directory/your_folder/10G_test.file
2025-06-16 23:30    10G  8add0bf4f023e3dbd36a329d1eae5bbd-684  STANDARD     s3://<freezer_bucket>/your_directory/your_folder/10G_copy.file
2025-06-17 01:31    14   95b28899a460dd8971705dfcd0f5f0d4     STANDARD     s3://<freezer_bucket>/your_directory/your_folder/MY_TEST/annotations/3/4/test3.txt
2025-06-17 01:31    14   e76c3a8939fb031bab02a89f6fab520b     STANDARD     s3://<freezer_bucket>/your_directory/your_folder/MY_TEST/annotations/3/test2.txt
2025-06-17 01:31    14   be2520c884c1be55bab187374a982b12     STANDARD     s3://<freezer_bucket>/your_directory/your_folder/MY_TEST/raw_data/test1.txt
2025-06-17 01:26     0   d41d8cd98f00b204e9800998ecf8427e     STANDARD     s3://<freezer_bucket>/your_directory/your_folder/test/test.txt
```

### Restore from tape

It is necessary to restore data from the tape (Glacier) prior to retrieving it. To restore file from Glacier storage:

```sh
s3cmd restore --recursive --verbose s3://<freezer_bucket>/your_directory/data_folder/
```

``` out
INFO: Retrieving list of remote files for s3://<freezer_bucket>/your_directory/your_folder/ ...
INFO: Summary: Restoring 6 remote files for 1 days at Standard priority
restore: 's3://n<freezer_bucket>/your_directory/your_folder/10G.file'
restore: 's3://<freezer_bucket>/your_directory/your_folder/10G_copy.file'
restore: 's3://<freezer_bucket>/your_directory/your_folder/MY_TEST/annotations/3/4/test3.txt'
restore: 's3://<freezer_bucket>/your_directory/your_folder/MY_TEST/annotations/3/test2.txt'
restore: 's3://<freezer_bucket>/your_directory/your_folder/MY_TEST/raw_data/test1.txt'
restore: 's3://<freezer_bucket>/your_directory/your_folder/test.txt'
```

By default files will remain in the S3 bucket for 1 day. If longer is required, this can be modified at the time of file restoration: 

```sh
s3cmd restore --recursive s3://<freezer_bucket>/your_directory/data_folder/ --restore-days=1
```

### Get objects after restore

!!! info
    Data needs to be restored (to storage class `STANDARD`) from the tape (storage class `GLACIER`), before it can be retrieved.

Example to get or download the directory `data_folder` and all contained objects/files/folders:

```sh
s3cmd get --recursive s3://<freezer_bucket>/your_directory/data_folder/
```

This will place the all files and subdirectories in the above `data_folder` into your current directory.

### Deleting data

!!! warning

    Please be very careful using the rm command to delete data as the data can't be recovered once deleted

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
