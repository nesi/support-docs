---
created_at: '2018-05-21T04:53:52Z'
tags:
- storage
- nobackup
- project
title: I/O Performance Considerations
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000205355
zendesk_section_id: 360000033936
---

It is important to understand the different I/O performance
characteristics of nodes that connect to storage using *native Spectrum
Scale clients*, and those that employ *Cray’s DVS* *solution*.

Applications that make heavy demands on metadata services and or have
high levels of small I/O activity should generally not be run on
[Māui](../../Scientific_Computing_old/The_NeSI_High_Performance_Computers/Maui.md) (the Cray
XC50).

## Nodes which access storage via native Spectrum Scale Clients

All [Mauhika](../../Scientific_Computing_old/The_NeSI_High_Performance_Computers/Mahuika.md)
HPC Cluster, [Mahuika Ancillary](../../Scientific_Computing_old/The_NeSI_High_Performance_Computers/Mahuika.md),
[Māui Ancillary](../../Scientific_Computing_old/The_NeSI_High_Performance_Computers/Maui_Ancillary.md) and
Māui login (aka build) nodes have native Spectrum Scale clients
installed and provide high performance access to storage:

- Metadata operations of the order of 190,000 file creates /second to
    a unique directory can be expected;
- For 8MB transfer size, single stream I/O is ~3.3GB/s Write and
    ~5GB/s Read;
- For 4KB transfer size, single stream I/O is ~1.3GB/s Write and
    ~2GB/s Read.

## Nodes which access storage via DVS

Māui (XC50) utilizes a file system projection method via software, known
as DVS (Data Virtualisation Service), to expose the Spectrum Scale file
systems to XC compute nodes. DVS adds an additional layer of hardware
and software between the XC compute nodes and storage (see Figure).

 ![cray\_xc50.jpg](../../assets/images/I-O_Performance_Considerations.jpg)

Figure 1: Cray XC50 DVS architecture.

This *reduces the I/O performance of Māui for metadata and small (e.g.
4KB) I/O operations*. It does not impact the total bandwidth available
from the Māui (i.e. ~130 GB/s when writing to the filesystem).
Accordingly, the equivalent performance numbers for DVS connected
compute nodes are:

- Metadata operations of the order of 36,000 file creates /second to a
    unique directory can be expected, i.e. approximately 23% of that
    achievable on a node that has a Spectrum Scale client.
- For 8MB transfer size, single stream I/O, is ~3.2GB/s for Write and
    ~3.2 GB/s for Read;
- For 4KB transfer size, single stream I/O, is ~2.3GB/s for Write and
    ~2.5GB/s for Read (when using IOBUF see Caution below).
    When IOBUF is not used Read and Write performance is &lt;1GB/s.

Unless Cray’s  [IOBUF](#iobuf)
 capability is suitable for an application, users should avoid
the use of single-stream I/O with small buffers on Māui.

## IOBUF

Cray’s IOBUF ( `man iobuf` ) is an
I/O buffering library that can reduce the I/O wait time for programs
that read or write large (or small) files sequentially. IOBUF intercepts
standard I/O calls such as read and open and replaces the
stdio (
glibc, libio ) layer of buffering
with an additional layer of buffering, thus improving program
performance by enabling asynchronous prefetching and caching of file
data.

!!! danger
    IOBUF is not suitable for all I/O styles. IOBUF does not
    maintain coherent buffering between processes which open the same file.
    For this reason, do not use IOBUF with shared file I/O, such as MPI-IO
    routines like MPI_File_write_all .
    IOBUF is *not thread-safe*, so do not use it with multithreaded programs in
    which the threads perform buffered I/O. IOBUF can be linked into
    programs that use these I/O styles, but buffering should not be enabled
    on those files.

## Data compression

The file system the NeSI platforms use allow for transparent compression
of data, meaning you can reduce the storage footprint of your data
without needing to add any extra steps in your workflow unless you want
to decompress the data after use. However, testing has shown that there
can be an impact on job performance due to I/O. You can find out more
about tests and results regarding performance of transparent
data compression on the NeSI platforms on our
[Data Compression support page](../../Storage/File_Systems_and_Quotas/Data_Compression.md).
