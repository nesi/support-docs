---
created_at: '2022-02-09T01:40:51Z'
hidden: false
label_names: []
position: 0
title: How do I find out the size of a directory?
vote_count: 0
vote_sum: 0
zendesk_article_id: 4415563282959
zendesk_section_id: 360000039036
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    To simplify this process, we have written a script, `nn_dir_contents`.
This script can be run in a variety of ways.

<table style="border-collapse: collapse; width: 100%;" data-border="1">
<tbody>
<tr class="header">
<th style="width: 50%">Command</th>
<th style="width: 50%">Result</th>
</tr>
&#10;<tr class="odd">
<td style="width: 50%"><code>nn_dir_contents</code></td>
<td style="width: 50%">Shows the size of, and number of directory
entries in, the current working directory</td>
</tr>
<tr class="even">
<td style="width: 50%"><code>nn_dir_contents -s</code></td>
<td style="width: 50%">Shows the size of the current working
directory</td>
</tr>
<tr class="odd">
<td style="width: 50%"><code>nn_dir_contents -n</code></td>
<td style="width: 50%">Shows the number of directory entries in the
current working directory</td>
</tr>
<tr class="even">
<td style="width: 50%"><code>nn_dir_contents &lt;DIR&gt;</code></td>
<td style="width: 50%">Shows the size of, and number of directory
entries in, the directory <code>DIR</code></td>
</tr>
<tr class="odd">
<td style="width: 50%"><code>nn_dir_contents -s &lt;DIR&gt;</code></td>
<td style="width: 50%">Shows the size of the directory
<code>DIR</code></td>
</tr>
<tr class="even">
<td style="width: 50%"><code>nn_dir_contents -n &lt;DIR&gt;</code></td>
<td style="width: 50%">Shows the number of directory entries in the
directory <code>DIR</code></td>
</tr>
<tr class="odd">
<td
style="width: 50%"><code>nn_dir_contents &lt;DIR1&gt; &lt;DIR2&gt; ...</code></td>
<td style="width: 50%">Shows the size of, and number of directory
entries in, the directories <code>DIR1</code>, <code>DIR2</code>,
etc.</td>
</tr>
<tr class="even">
<td
style="width: 50%"><code>nn_dir_contents -s &lt;DIR1&gt; &lt;DIR2&gt; ...</code></td>
<td style="width: 50%">Shows the sizes of the directories
<code>DIR1</code>, <code>DIR2</code>, etc.</td>
</tr>
<tr class="odd">
<td
style="width: 50%"><code>nn_dir_contents -n &lt;DIR1&gt; &lt;DIR2&gt; ...</code></td>
<td style="width: 50%">Shows the numbers of directory entries in the
directories <code>DIR1</code>, <code>DIR2</code>, etc.</td>
</tr>
</tbody>
</table>

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
