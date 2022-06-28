Snapshots
---------

Snapshots are read only copies of the file system taken every day at
1215, and retained for seven days.\
\
Files from you project directory can be found
in `/nesi/project/.snapshots/`{.nohighlight} followed by the weekday
(capitalised) and project code, e.g;

``` {.nohighlight}
/nesi/project/.snapshots/Sunday/nesi99999/
```

 And for home directory;

``` {.nohighlight}
/home/username/.snapshots/Sunday/
```

> ### Warning {#prerequisites}
>
> Files in `/nesi/nobackup/`{.nohighlight} are not snapshotted.

 

Recovering a file or a directory from the snapshot is as simple as
copying it over, e.g.

``` {.nohighlight}
cp /nesi/project/.snapshots/Sunday/nesi99999/file.txt /nesi/project/nesi99999/file.txt
```

> ### Tip {#prerequisites}
>
> For copying directories use the flag -ir or just -r if you don\'t want
> to be prompted before overwriting.
