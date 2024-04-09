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

Snapshots are read only copies of the file system taken every day at
12:15, and retained for seven days.  
  
Files from you project directory can be found
in `/nesi/project/.snapshots/` followed by the weekday (capitalised) and
project code, e.g;

``` sl
/nesi/project/.snapshots/Sunday/nesi99999/
```

 And for home directory;

``` sl
/home/username/.snapshots/Sunday/
```

!!! Warning
     Files in `/nesi/nobackup/` are not snapshotted.

Recovering a file or a directory from the snapshot is as simple as
copying it over, e.g.

``` sl
cp /nesi/project/.snapshots/Sunday/nesi99999/file.txt /nesi/project/nesi99999/file.txt
```

!!! Tip
     For copying directories use the flag -ir or just -r if you don't want to be prompted before overwriting
