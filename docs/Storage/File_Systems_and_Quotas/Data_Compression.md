---
created_at: '2023-02-08T00:21:51Z'
hidden: false
label_names:
- compression
- data_compression
- lz4
- data compression
- zlib
- z library
- z-library
position: 0
title: Data Compression
vote_count: 0
vote_sum: 0
zendesk_article_id: 6359601973135
zendesk_section_id: 360000033936
---

# Background

Spectrum Scale filesystems (previously GPFS) allow users to compress
data (but not metadata) transparently on demand without the need to
change metadata (file creation and modification dates, etc). This means
that that data can be compressed and then used without first needing to
decompress it, as the decompression happens automatically in the
background without the need for commands. It allows you to treat the
data as if it were not compressed.

The data will need to be re-compressed after it is used if you are to
maintain it in the compressed state. This can be done by the user (front
end) or at the back end via a policy for example. In the future, it is
intended that there will be some automatic process regularly compressing
flagged files, but at this time, it is only done manually by the NeSI
team for specific filesets identified as suitable for the compression;
or by the user manually on their own filesets.

For purposes of this Guide, we are going to focus on the user side and
what the users can do. As a default, the Zlib compression algorithm will
be used, although depending on the version of the filesystem, additional
ones might be added. It is possible to change algorithms at any time for
any file (we will cover that further ahead) when the compression is
requested.

# Compression Methods<span class="heading-anchor-wrapper"></span>

There are two methods for compressing and decompressing data:
**on-demand** and **deferred**:

## On-Demand (synchronous)<span class="heading-anchor-wrapper"></span>

**note:** *as at 2 May 2023, the \`mm\` commands are not available by
default, contact <support@nesi.org.nz> for assistance*

This method (using the `mmchattr` command) acts similar to
`gzip`/`gunzip` commands where the file being targeted is compressed or
decompressed on command invocation. If the command fails halfway through
the file or is cancelled, the file will be marked as "illcompressed" .
This state means that the file is only partially compressed.

`ls` command will show files with their original sizes. However,  `du`
commands will calculate the approximate usage of the file system as
opposed to the uncompressed usage. This will be the total counting
against quotas as well. Therefore, if files are compressed, quota usage
will decrease. And vice versa, if files are decompressed, fully or
partially, quota usage will increase. Be aware that if, in the process
of decompression, the quota will be exceeded, an error message will be
displayed

    $ du -h FileA.txt
    41M FileA.txt

    $ ls -lh FileA.txt
    -rw-r--r-- 1 user001 user001 41M Jul 6 01:03 FileA.txt

    $ time mmchattr --compression yes FileA.txt
    real 0m1.343s
    user 0m0.002s
    sys 0m0.000s

    $ ls -lh FileA.txt
    -rw-r--r-- 1 user001 user001 41M Jul 6 01:03 FileA.txt

    $ du -h FileA.txt
    8.0M FileA.txt

##  

## Deferred<span class="heading-anchor-wrapper"></span>

This method (also using the `mmchattr` command) does not decompress or
compress data immediately but, instead marks them for
compression/decompression to be invoked later. The user can later
schedule a secondary task to compress or decompress tagged data. In the
future, the deferred tag will flag the data for automatic
compression/decompression. This tagging process is quick and can be done
by using the same command as above with one extra flag (`-I defer`).
During this process, there is no change in space occupancy for any of
the files involved.

    $ du -h FileA.txt
    41M FileA.txt

    $ ls -lh FileA.txt
    -rw-r--r-- 1 user001 user001 41M Jul 6 01:03 FileA.txt

    $ time mmchattr -I defer --compression yes FileA.txt
    real 0m0.002s
    user 0m0.002s
    sys 0m0.000s

    $ ls -lh FileA.txt
    -rw-r--r-- 1 user001 user001 41M Jul 6 01:03 FileA.txt

    <bash>$ du -h FileA.txt
    41M FileA.txt

####  

### How to process deferred tagged files<span class="heading-anchor-wrapper"></span>

Users can process compression/decompression on the tagged files via the
`mmrestripefile` command (using `-z` flag).

    $ mmrestripefile -z FileA.txt
    Scanning FileA.txt
    Scan completed successfully.

# States of a compressed file<span class="heading-anchor-wrapper"></span>

Compressed files on Scale filesystems can be in 4 different states
depending on the extended attributes of the file when manipulated for
compression. We can check those attributes with the `mmlsattr` command:

    $ mmlsattr -L FileA.txt
    file name: FileA.txt
    metadata replication: 1 max 2
    data replication: 1 max 2
    immutable: no
    appendOnly: no
    flags:
    storage pool name: data
    fileset name: home_user001
    snapshot name:
    creation time: Wed Jul 6 00:54:27 2022
    Misc attributes: ARCHIVE
    Encrypted: no

The misc attributes will have or not have a `COMPRESSION` value,
depending on if the file is or not tagged for compression. In addition,
a file will exhibit the flag `illcompressed` when the desired final
state is not the achieved yet (fully compressed or uncompressed).

A file that is fully compressed (not showing the flag `illcompressed`
and having the misc attribute `COMPRESSION` ), if updated or appended
data to, becomes automatically `illcompressed` and either needs to be
re-compressed using the `mmchattr --compression yes` command or the
`mmrestripefile -z` one (because it's already tagged for compression).

#### The different states<span class="heading-anchor-wrapper"></span>

-   **Uncompressed** and **untagged** for compression (default) - as
    shown for the file `FileA.txt` above.

-   **Partially compressed** and **tagged** for compression - When file
    is partially compressed (either because it was decompressed for
    access or the full compression didn’t finish). It is still marked
    for compression as the `COMPRESSION` misc attribute suggests, but
    because it's not fully compressed the `illcompressed` flag will be
    shown.

        $ mmlsattr -L FileA.txt
        file name: FileA.txt
        metadata replication: 1 max 2
        data replication: 1 max 2
        immutable: no
        appendOnly: no
        flags: illcompressed
        storage pool name: data
        fileset name: home_user001
        snapshot name:
        creation time: Wed Jul 6 00:54:27 2022
        Misc attributes: ARCHIVE COMPRESSION (library z)
        Encrypted: no

-   **Fully compressed** and **tagged** for compression - The file is
    fully compressed to its maximum possible state and because the file
    is tagged for compression, only the misc attribute `COMPRESSION`
    will be shown.

        $ mmlsattr -L FileA.txt
        file name: FileA.txt
        metadata replication: 1 max 2
        data replication: 1 max 2
        immutable: no
        appendOnly: no
        flags:
        storage pool name: data
        fileset name: home_user001
        snapshot name:
        creation time: Wed Jul 6 00:54:27 2022
        Misc attributes: ARCHIVE COMPRESSION (library z)
        Encrypted: no

-   **Full or partially compressed** and **untagged** for compression -
    The file might be fully or partially compressed and in this case
    because the misc attribute `COMPRESSION` is not shown, it means the
    file is untagged for being compressed (meaning it's tagged to be in
    the uncompressed state). When a fully compressed file is untagged,
    the flag `illcompressed` will be shown. After full decompression is
    complete the file will become uncompressed and untagged for
    compression.

        $ mmlsattr -L FileA.txt
        file name: FileA.txt
        metadata replication: 1 max 2
        data replication: 1 max 2
        immutable: no
        appendOnly: no
        flags: illcompressed
        storage pool name: data
        fileset name: home_user001
        snapshot name:
        creation time: Wed Jul 6 00:54:27 2022
        Misc attributes: ARCHIVE
        Encrypted: no

# Using different compression algorithms<span class="heading-anchor-wrapper"></span>

The default algorithm is the Zlib and will be shown on the misc
attributes of a tagged file as “library z”. Depending on the Scale
version installed, files can be tagged with different algorithms.

Currently supported compression libraries are:

-   z Cold data. Favours compression efficiency over access speed.

-   lz4 Active, non-specific data. Favours access speed over compression
    efficiency.

# Performance impacts<span class="heading-anchor-wrapper"></span>

Experiments showed that I/O performance was definitely affected if a
file was in a compressed state. The extent of the effect, however,
depends on the magnitude of I/O operations on the affected files.  I/O
intensive workloads may experience a significant performance drop.  
  
If compression has a significant impact on your software performance,
please confirm it first by running a test job with and without
compression and then contact us at <support@nesi.org.nz>. We will help
you minimise the impact of compression on your workflow or find other
ways to help you manage your project storage.

If you are interested in learning more about this type of data
compression [you can find further details on the IBM
website](https://www.ibm.com/docs/en/spectrum-scale/4.2.2?topic=systems-file-compression).
