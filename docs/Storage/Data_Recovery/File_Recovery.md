---
created_at: '2018-05-22T01:49:31Z'
tags: []
title: File Recovery
vote_count: 9
vote_sum: 7
zendesk_article_id: 360000207315
zendesk_section_id: 360000042215
---

## Snapshots

Snapshots are read only copies of the file systems at a point in time. 
They are taken daily (or weekly for `/nesi/nobackup`) and retained for 
at least seven days.  
  
Files from your home directory can be found
in `/home/.snapshots/` followed by a snapshot timestamp and
username, e.g;

``` sl
/home/.snapshots/@GMT-2025.08.04-18.00.00/$USER
```

And similarly for a project or nobackup directory:

``` sl
/nesi/project/.snapshots/@GMT-2025.08.04-18.00.00/nesi99999/
```

Recovering a file or a directory from the snapshot is as simple as
copying it over, e.g.

``` sl
cp /nesi/nobackup/.snapshots/@GMT-2025.08.04-18.00.00/nesi99999/file.txt /nesi/nobackup/nesi99999/file.txt
```


!!! Tip
     For copying directories use the flag -ir or just -r if you don't want to be prompted before overwriting
