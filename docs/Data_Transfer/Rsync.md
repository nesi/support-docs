---
created_at: 2026-01-05
description: How to transfer data on the REANNZ HPC using RSync.
---

!!! prerequisite
    Have SSH setup as described in [Standard Terminal Setup](../Getting_Started/Accessing_the_HPCs/Standard_Terminal_Setup.md)

Rsync is an utility that provides fast incremental file transfer and
efficient file synchronization between a computer and a storage disk.
The basic command syntax of:

```bash
rsync -options source target
```

If the data source or target location is a remote site, it is defined
with syntax:

```txt
userame@server:/path/in/server
```

The most frequently used Rsync options:

- `-r` - Recurse into directories.
- `-a` - Use archive mode: copy files and directories recursively and preserve access permissions and time stamps.
- `-z` - Compress.
- `-e ssh` - Specify the remote shell to use.
- `-n` - Show what files would be transferred.

A more extensive list can be found in the [Rsync documentation](https://download.samba.org/pub/rsync/rsync.1).
