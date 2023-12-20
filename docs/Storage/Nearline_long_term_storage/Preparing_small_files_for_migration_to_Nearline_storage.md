---
created_at: '2019-12-16T09:20:39Z'
hidden: false
position: 1
tags: []
title: Preparing small files for migration to Nearline storage
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001298595
zendesk_section_id: 360000042255
---


Migration of files from your project or nobackup directory to your
nearline directory is a two-step process. In the first step, the data is
copied from project or nobackup to a staging file system with a maximum
capacity of 500 TB. In the second step, the data on the staging file
system is moved to tape.

To reduce the burden on our tape drives and file catalogue, project
teams are strongly encouraged to store only large files on nearline, and
in fact attemps to upload files smaller than 64 MB will be rejected.
Because your project or nobackup directory, or any subdirectory of the
same, will almost certainly contain some small files and may have a
large number of them, this article offers instructions for how to
straightforwardly find all these small files and combine them into a few
large archive files, perhaps as few as one.

## Can't I just compress the whole project (or nobackup) directory, or at least all its contents?

Yes, you certainly can do that. This is unlikely to suit you, however:

- Without special options, creating a SquashFS, tarball or other
  archive file is effectively taking a copy of the contents of every
  file in the directory. Unless your project or nobackup directory
  starts out at less than half full, you may well not have the disk
  space to create the full file.
- There are options to some archiving programs, including
  the `nn_archive_files`, `mksquashfs` and `tar` programs, that will
  cause the software to delete files during or just after the
  compression process. It is likely, however, that you will want at
  least some files to remain in your online storage.
- There are a few projects that have more than 500 TB of data, and
  such an archive file would be too big to be copied to the staging
  file system. Even if it were not, however, copying one very large
  archive file takes a long time, retrieval takes a long time as well,
  and since any interruption to either process will necessitate
  starting from scratch, the risk of wasted time increases
  (interruptions become more likely, and the likely consequences of
  interruptions become more severe).

## What is the recommended option, then?

If the directory is too big to be copied as a whole, we recommend that
you find all the small files within a directory, then group those small
files into an archive file, leaving large files to be copied to nearline
individually.

You do not have to create one single archive file for all small files in
`/nesi/project/<project_code>` or `/nesi/nobackup/<project_code>`, and
in fact you may prefer to create archive files pertaining to particular
subdirectories. There is no harm in either approach.
!!! tip "Tip"
    The archive creation process can take quite a long time. So that you
    can freely log out of the cluster, and to protect the process in case
    you're accidentally disconnected, you should create the archive by
    means of a Slurm job, or else in a `tmux` or `screen` session.

Archive creation is very simple, and can be achieved through the
following:

``` sh
startdir=$(pwd -P) && \
archive_file="archive.squash" && \
cd /nesi/project/nesi12345/my_directory && \
find . -type f -and -size -100M -print0 | xargs -0 -I {} nn_archive_files -p nesi12345 -t <time-limit> -n <num-processors> --verify --append --delete-files -- {} "${archive_file}"
# Return to where you started
cd "${startdir}"
```

 Some notes on the above script:

- The name of the archive is saved as a variable, `$archive_file`, so
  that it is kept consistent whenever it is used.
- While we have suggested creating the archive in situ
  (`archive_file="archive.squash"`) as an example, there is no reason
  not to use a relative or even absolute path
  (e.g. `archive_file="/path/to/archive.squash"`). You can also put it
  where you started running the sequence of commands from:
  `archive_file="${startdir}/archive.squash"`.
- We recommend going to the directory (`cd <dir>`) before running the
  `find` command, so that the archive stores files as relative paths,
  not absolute paths. This choice will make a big difference when you
  come to extract the archive. In the example above, we go one step
  further: The && means, "Only run the next command if this command is
  successful, i.e. it completes with an exit code of 0."
- The `-type f` option restricts the search to look for files only.
  Directories, symbolic links and other items will not be found.
  However, files within subdirectories will be found.
- The `-size -100M` option restricts the search to items that are less
  than 100 MB. This size criterion is not the only valid option, but
  it likely represents a good balance between creating an overly large
  archive on the one hand, and leaving many small files to be
  individually copied on the other.
- The conjunction `-and` does exactly what you expect: it limits
  search results to items satisfying both criteria. (`find` also
  recognises the option `-or`, not relevant here.)
- The option `-print0` separates results with the null character, so
  that spaces and other special characters in file names don't get
  misinterpreted as record separators.
- Piping to `xargs -0` gracefully handles a long list of arguments
  separated by null characters. `xargs` breaks up long lists of
  arguments, sending the arguments in small batches to the simple
  command given as an argument to `xargs`. In this case, that simple
  command is `nn_archive_files` with flags and arguments.
- The option `-I {}` to `xargs` instructs `xargs` to replace every
  later instance of `{}` with the name of the actual result, in this
  case a found file, or more precisely a relative path to a found
  file.
- The `--append` option causes the list of checksums to be appended
  to, rather than overwritten.
- `--delete-files` will delete each found file once that file has been
  added to the ever-growing archive.
- As given above, the command will submit one, or a series of, Slurm
  jobs. You can wait until they're done.
