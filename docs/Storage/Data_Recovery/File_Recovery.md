---
created_at: '2018-05-22T01:49:31Z'
tags:
- storage
- nobackup
description: Information about file recovery
---

## Snapshots

Snapshots are read only copies of the filesystems at a point in time.
They are taken daily (or weekly for `/nesi/nobackup`) and retained for
at least seven days.  
  
Files from your home directory can be found
in `/home/.snapshots/` followed by a snapshot timestamp and
username, e.g;

``` sh
/home/.snapshots/@GMT-2025.08.04-18.00.00/$USER
```

And similarly for a project or nobackup directory:

``` sh
/nesi/project/.snapshots/@GMT-2025.08.04-18.00.00/nesi99999/
```

Recovering a file or a directory from the snapshot is as simple as
copying it over, e.g.

``` sh
cp /nesi/nobackup/.snapshots/@GMT-2025.08.04-18.00.00/nesi99999/file.txt /nesi/nobackup/nesi99999/file.txt
```

!!! Tip
     For copying directories use the flag -ir or just -r if you don't want to be prompted before overwriting
