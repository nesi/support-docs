---
created_at: '2020-01-14T22:10:50Z'
hidden: false
label_names: []
position: 18
title: Checksums
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001330415
zendesk_section_id: 360000030876
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

Applying a *checksum function* to a file will return its *checksum*.
Checksum functions are a type of [hash
function](https://en.wikipedia.org/wiki/Hash_function), and will always
return the same hash for any particular file contents, making them
useful for file validation. There are many different checksum functions.
The most commonly used are listed in the table below.

Checksums can be used to check for minor errors that may have been
introduced into a dataset. For example:

-   After downloading a file (compare your generated checksum with the
    checksum provided by the vendor).
-   When copying a file onto the cluster (generate a checksum on your
    local machine and another on the cluster).
-   Verifying your results/workflow. (making a checksum of a results
    file can be a quick way to confirm nothing has changed).
-   Corroborate files when working in a team.

While not necessary to do in every case, every time, file integrity
should be one of the first things you check when troubleshooting.

## Example

The file '`corrupt.bin`' has had 1 byte changed, yet on inspection would
appear identical. 

    -rw-rw-r--  1  393315  copy.bin
    -rw-rw-r--  1  393315  corrupt.bin
    -rw-rw-r--  1  393315  original.bin

By using a MD5 checksum (`md5sum *`) we can see that '`corrupt.bin`' has
diverged from the original, while '`copy.bin`' has not.

    002c33835b3921d92d8074f3b392ef65 copy.bin
    ef749eb4110c2a3b3c747390095d0b76 corrupt.bin
    002c33835b3921d92d8074f3b392ef65 original.bin

Note that filename, path, permissions or any other metadata does not
affect the checksum.
!!! info Note
>
> Checksum functions are designed so that similar files *will not*
> produce similar hashes.
>
> You will only need to compare a few characters of the string to
> confirm validity.

## Commands

The checksum for file '*filename.txt*' can be found with the following
commands.

<table style="height: 37px;" width="805">
<tbody>
<tr class="odd">
<td style="width: 149px"> </td>
<td style="width: 150px">Linux</td>
<td style="width: 150px">Windows(CMD/Powershell)</td>
<td style="width: 150px">Mac</td>
</tr>
<tr class="even">
<td style="width: 149px">SH1</td>
<td
style="width: 150px"><code>sha1sum </code><em><code>filename.txt</code></em></td>
<td
style="width: 150px"><code>certUtil -hashfile </code><em><code>filename.txt</code></em></td>
<td
style="width: 150px"><code>shasum </code><em><code>filename.txt</code></em></td>
</tr>
<tr class="odd">
<td style="width: 149px">SHA256</td>
<td
style="width: 150px"><code>sha256sum </code><em><code>filename.txt</code></em></td>
<td
style="width: 150px"><code>certUtil -hashfile </code><em><code>filename.txt</code></em><code> sha256</code></td>
<td
style="width: 150px"><code>shasum -a 256 </code><em><code>filename.txt</code></em></td>
</tr>
<tr class="even">
<td style="width: 149px">MD5</td>
<td
style="width: 150px"><code>md5sum </code><em><code>filename.txt</code></em></td>
<td
style="width: 150px"><code>certUtil -hashfile </code><em><code>filename.txt</code></em><code> md5</code></td>
<td
style="width: 150px"><code>md5 </code><em><code>filename.txt</code></em></td>
</tr>
</tbody>
</table>

 

 
