## Snapshots

Snapshots are read only copies of the file system taken every day at
12:15, and retained for seven days.  
  
Files from you project directory can be found
in `/nesi/project/.snapshots/` followed by the weekday (capitalised) and
project code, e.g;

    /nesi/project/.snapshots/Sunday/nesi99999/

 And for home directory;

    /home/username/.snapshots/Sunday/

> ### Warning
>
> Files in `/nesi/nobackup/` are not snapshotted.

 

Recovering a file or a directory from the snapshot is as simple as
copying it over, e.g.

    cp /nesi/project/.snapshots/Sunday/nesi99999/file.txt /nesi/project/nesi99999/file.txt

> ### Tip
>
> For copying directories use the flag <kbd>-ir</kbd> or just
> <kbd>-r</kbd> if you don't want to be prompted before overwriting.
