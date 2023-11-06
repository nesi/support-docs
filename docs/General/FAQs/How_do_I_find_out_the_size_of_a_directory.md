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
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>To simplify this process, we have written a script, <code>nn_dir_contents</code>. This script can be run in a variety of ways.</p>
<table style="border-collapse: collapse; width: 100%;" border="1">
<tbody>
<tr>
<th style="width: 50%;">Command</th>
<th style="width: 50%;">Result</th>
</tr>
<tr>
<td style="width: 50%;"><code>nn_dir_contents</code></td>
<td style="width: 50%;">Shows the size of, and number of directory entries in, the current working directory</td>
</tr>
<tr>
<td style="width: 50%;"><code>nn_dir_contents -s</code></td>
<td style="width: 50%;">Shows the size of the current working directory</td>
</tr>
<tr>
<td style="width: 50%;"><code>nn_dir_contents -n</code></td>
<td style="width: 50%;">Shows the number of directory entries in the current working directory</td>
</tr>
<tr>
<td style="width: 50%;"><code>nn_dir_contents &lt;DIR&gt;</code></td>
<td style="width: 50%;">Shows the size of, and number of directory entries in, the directory <code>DIR</code>
</td>
</tr>
<tr>
<td style="width: 50%;"><code>nn_dir_contents -s &lt;DIR&gt;</code></td>
<td style="width: 50%;">Shows the size of the directory <code>DIR</code>
</td>
</tr>
<tr>
<td style="width: 50%;"><code>nn_dir_contents -n &lt;DIR&gt;</code></td>
<td style="width: 50%;">Shows the number of directory entries in the directory <code>DIR</code>
</td>
</tr>
<tr>
<td style="width: 50%;"><code>nn_dir_contents &lt;DIR1&gt; &lt;DIR2&gt; ...</code></td>
<td style="width: 50%;">Shows the size of, and number of directory entries in, the directories <code>DIR1</code>, <code>DIR2</code>, etc.</td>
</tr>
<tr>
<td style="width: 50%;"><code>nn_dir_contents -s &lt;DIR1&gt; &lt;DIR2&gt; ...</code></td>
<td style="width: 50%;">Shows the sizes of the directories <code>DIR1</code>, <code>DIR2</code>, etc.</td>
</tr>
<tr>
<td style="width: 50%;"><code>nn_dir_contents -n &lt;DIR1&gt; &lt;DIR2&gt; ...</code></td>
<td style="width: 50%;">Shows the numbers of directory entries in the directories <code>DIR1</code>, <code>DIR2</code>, etc.</td>
</tr>
</tbody>
</table>
<p>The last three forms of commands work with shell globbing (<code>*</code>, <code>?</code>, etc.), and the last two are particularly useful if you want to find out how much each subdirectory contributes to a directory's total disk space or inode counts. The outputs of the last two commands can easily be piped to <code>sort</code> if you want to get a list of directories from the smallest to the largest (<code>sort -k 2h,2</code> for a human-readable sort), or from the fewest files to the most (<code>sort -k 2n,2</code> for a numeric sort).</p>
<p>Only directory arguments are considered by <code>nn_dir_contents</code>, though files do count towards a directory's contents.</p>
<p><code>nn_dir_contents</code> is a wrapper for <code>du</code> and is run without any flags that alter the behaviour of <code>du</code> with respect to sparse files. If you think the sparsity of a file is relevant to you, you may need to run <code>du</code> separately on directories that you believe contain sparse files.</p>
<p><code>nn_dir_contents</code> relies on two consecutive executions of the <code>find</code> command in order to count the number of files. It does not lock the directory, so if the directory's contents are altered (files created or deleted) while the command is running, the results may be inaccurate or out of date. This is a known limitation of the command.</p>