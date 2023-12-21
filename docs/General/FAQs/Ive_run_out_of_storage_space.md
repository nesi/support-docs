---
created_at: '2019-08-26T00:02:24Z'
hidden: false
weight: 0
tags:
- disk quota exceeded
title: I've run out of storage space
vote_count: 3
vote_sum: 1
zendesk_article_id: 360001125996
zendesk_section_id: 360000039036
---

There are two tracked resources in the NeSI filesystem, *disk space* and
*inodes (number of files)*.

Trying to write to a filesystem over its inode or disk quota will cause
an error (and probably kill your job).

Current file-count and disk space can be found using `nn_storage_quota`.

```sh
Filesystem         Available      Used     Use%     Inodes     IUsed     IUse%
home_user123             20G    1.957G    9.79%      92160     21052    22.84%
project_nesi99999         2T      798G   38.96%     100000     66951    66.95%
nobackup_nesi99999              6.833T            10000000    2691383   26.91%
```

!!! note
     There is a delay between making changes to a filesystem and seeing the
     change in `nn_storage_quota`, immediate file count and disk space can
     be found using the commands `du --inodes` and `du -h` respectively.

There are a few ways to deal with file count problems

### Use the nobackup filesystem

Your nobackup directories `/nesi/nobackup/<projectcode>` has a significantly higher inode count and no disk space limits.
Files here are not backed up, so best used for intermediary or replaceable data.

### Delete unnecessary files

Some applications will generate a large number of files during
runtime, using the command `du --inodes -d 1 | sort -hr` (for
inodes) or `du -h -d 1 | sort -hr` for disk space.  You can then
drill down into the directories with the largest file count deleting
files as viable.

### SquashFS archive

Many files can be compressed into a single SquashFS archive. We have
written a utility, `nn_archive_files`, to help with this process.
This utility can be run on Māui or Mahuika, but not, as yet, on
Māui-ancil; and it can submit the work as a Slurm job, which is
preferred. `nn_archive_files` can take, as trailing options, the
same options as `mksquashfs`, including choice of compression
algorithm; see `man mksquashfs` for more details.  

```sh
nn_archive_files -p <project-code> -n <num-processors> -t <time-limit> --verify -- /path/containing/files /path2/containing/files destination.squash
```

Then when files need to be accessed again they can be extracted
using,

```sh
/usr/sbin/unsquashfs destination.squash
```

You can do many other things with SquashFS archives, like quickly
list the files in the archive, extract some but not all of the
contents, and so on. See `man unsquashfs` for more details.

### Tarball

Many files can be compressed into a single 'tarball'

```sh
tar -czf name.tar /path/containing/files/
```

Then when files need to be accessed again they can be un-tarred
using,

```sh
tar -xzf tarname.tar
```

### Contact Support

If you are following the recommendations here yet are still concerned about inodes or disk space, {% include "partials/support_request.html" %} and we can raise the limit for you.
