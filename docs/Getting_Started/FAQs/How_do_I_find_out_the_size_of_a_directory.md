---
created_at: '2022-02-09T01:40:51Z'
tags: []
description: Instructions for finding the size of a directory?
---

To simplify this process, we have written a script, `nn_dir_contents`.
This script can be run in a variety of ways.

|  Command                               | Result                                                                                      |
| -------------------------------------- | ------------------------------------------------------------------------------------------- |
| `nn_dir_contents`                      | Shows the size of, and number of directory entries in, the current working directory        |
| `nn_dir_contents -s`                   | Shows the size of the current working directory                                             |
| `nn_dir_contents -n`                   | Shows the number of directory entries in the current working directory                      |
| `nn_dir_contents <DIR>`                | Shows the size of, and number of directory entries in, the directory `DIR`                  |
| `nn_dir_contents -s <DIR>`             | Shows the size of the directory `DIR`                                                       |
| `nn_dir_contents -n <DIR>`             | Shows the number of directory entries in the directory `DIR`                                |
| `nn_dir_contents <DIR1> <DIR2> ...`    | Shows the size of, and number of directory entries in, the directories `DIR1`, `DIR2`, etc. |
| `nn_dir_contents -s <DIR1> <DIR2> ...` | Shows the sizes of the directories `DIR1`, `DIR2`, etc.                                     |
| `nn_dir_contents -n <DIR1> <DIR2> ...` | Shows the numbers of directory entries in the directories `DIR1`, `DIR2`, etc.              |

The last three forms of commands work with shell globbing (`*`, `?`,
etc.), and the last two are particularly useful if you want to find out
how much each subdirectory contributes to a directory's total disk space
or inode counts. The outputs of the last two commands can easily be
piped to `sort` if you want to get a list of directories from the
smallest to the largest (`sort -k 2h,2` for a human-readable sort), or
from the fewest files to the most (`sort -k 2n,2` for a numeric sort).

Only directory arguments are considered by `nn_dir_contents`, though
files do count towards a directory's contents.

`nn_dir_contents` is a wrapper for `du` and is run without any flags
that alter the behaviour of `du` with respect to sparse files. If you
think the sparsity of a file is relevant to you, you may need to run
`du` separately on directories that you believe contain sparse files.

`nn_dir_contents` relies on two consecutive executions of the `find`
command in order to count the number of files. It does not lock the
directory, so if the directory's contents are altered (files created or
deleted) while the command is running, the results may be inaccurate or
out of date. This is a known limitation of the command.
