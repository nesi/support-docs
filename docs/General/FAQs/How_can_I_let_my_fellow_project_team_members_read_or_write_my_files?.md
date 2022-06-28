> ### See also
>
> [File permissions and
> groups](https://support.nesi.org.nz/hc/en-gb/articles/360000205435)

If you move or copy a file or directory from one project directory to
another, or from somewhere within your home directory to somewhere
within a project directory, generally the file, or the directory
together with its contents, as the case may be, will keep its original
ownership, group and permissions.

So, supposing Joe Bloggs moves a file from his home directory to the
project directory `/nesi/project/nesi99999`, his fellow team members
won\'t be able to write to it:

``` {dir="ltr"}
$ ls -l README
-rw-r--r-- 1 bloggsj bloggsj 235 Mar 14  2014 README
$ mv README /nesi/project/nesi99999/bloggsj/README
$ ls -l /nesi/project/nesi99999/bloggsj/README
-rw-r--r-- 1 bloggsj bloggsj 235 Mar 14  2014 /nesi/project/nesi99999/bloggsj/README
```

As you can see, the file stays in the group `bloggsj`, that is Joe
Bloggs\' personal group, even though it is now inside the project
directory.

There is, however, a solution involving the `rsync` command, a more
advanced version of `scp`. `rsync` is typically used to copy files
between two or more machines, but can also be used within the same
machine.

> ### Warning {#perms-group-warning}
>
> In both these commands, the `--no-perms` and `--no-group` options must
> both come after `-a`. `-a` implicitly asserts `--perms` and `--group`,
> and will therefore override whichever
> of `--no-perms` and `--no-group` come before it.

To copy a file (or directory and its contents), updating its group and setting its permissions {#to-copy-a-file-or-directory-and-its-contents-updating-its-group-and-setting-its-permissions dir="auto"}
----------------------------------------------------------------------------------------------

``` {dir="ltr"}
rsync -a --no-perms --no-group --chmod=ugo=rwX,Dg+s /path/to/source /path/to/destination
```

To move a file (or directory and its contents), updating its group and setting its permissions {#to-move-a-file-or-directory-and-its-contents-updating-its-group-and-setting-its-permissions dir="auto"}
----------------------------------------------------------------------------------------------

> ### Warning {#remove-source-warning}
>
> The `--remove-source-files` option is safe only if every source file
> is otherwise left intact during the moving process.

``` {dir="ltr"}
rsync --remove-source-files -a --no-perms --no-group --chmod=ugo=rwX,Dg+s /path/to/source /path/to/destination
```

If you want to set files to executable in all cases,
replace `...ugo=rwX...` with `...ugo=rwx...`. The capital `X` means,
\"Preserve whatever executable permissions existed on the source file
and aren\'t masked at the destination.\" A lower case `x` on the other
hand means, \"Make this entity executable, even if it wasn\'t so
previously, though this may be masked at the destination.\"

To fix the permissions of a file or directory that is already in its intended place {#to-fix-the-permissions-of-a-file-or-directory-that-is-already-in-its-intended-place dir="auto"}
-----------------------------------------------------------------------------------

Change to the parent directory, which could be a project or nobackup
directory, that you want to fix, and find and fix your files. You can do
this by means of the following commands.

``` {dir="ltr"}
# Replace nesi12345 with your desired project code
group=nesi12345
startdir=$(pwd)
# Replace /nesi/project with /nesi/nobackup if needed
cd /nesi/project/${group}
# Move all files, directories, etc. owned by yourself into the project group
# The --no-dereference option updates the group of symbolic links (where permitted)
find . -user $(whoami) -print0 | xargs -0 -I {} chgrp --no-dereference ${group} {}
# Make all files owned by yourself readable and writable by the group
find . -user $(whoami) -and -type f -print0 | xargs -0 -I {} chmod g+rw {}
# Make all directories owned by yourself readable, writable and executable by the group,
# and set the setgid bit
find . -user $(whoami) -and -type d -print0 | xargs -0 -I {} chmod g+rwxs {}
# Go back to the starting location
cd ${startdir}
```
