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
<p>Applying a <em>checksum function</em> to a file will return its <em>checksum</em>. Checksum functions are a type of <a href="https://en.wikipedia.org/wiki/Hash_function" target="_blank" rel="noopener">hash function</a>, and will always return the same hash for any particular file contents, making them useful for file validation. There are many different checksum functions. The most commonly used are listed in the table below.</p>
<p>Checksums can be used to check for minor errors that may have been introduced into a dataset. For example:</p>
<ul>
<li>After downloading a file (compare your generated checksum with the checksum provided by the vendor).</li>
<li>When copying a file onto the cluster (generate a checksum on your local machine and another on the cluster).</li>
<li>Verifying your results/workflow. (making a checksum of a results file can be a quick way to confirm nothing has changed).</li>
<li>Corroborate files when working in a team.</li>
</ul>
<p>While not necessary to do in every case, every time, file integrity should be one of the first things you check when troubleshooting.</p>
<h2>Example</h2>
<p>The file '<code>corrupt.bin</code>' has had 1 byte changed, yet on inspection would appear identical. </p>
<pre><code>-rw-rw-r--  1  393315  copy.bin
-rw-rw-r--  1  393315  corrupt.bin
-rw-rw-r--  1  393315  original.bin
</code></pre>
<p>By using a MD5 checksum (<code>md5sum *</code>) we can see that '<code>corrupt.bin</code>' has diverged from the original, while '<code>copy.bin</code>' has not.</p>
<pre><code>002c33835b3921d92d8074f3b392ef65 copy.bin
<span class="wysiwyg-color-red90">ef749eb4110c2a3b3c747390095d0b76</span><span class="wysiwyg-color-black"> corrupt.bin
</span>002c33835b3921d92d8074f3b392ef65 original.bin
</code></pre>
<p>Note that filename, path, permissions or any other metadata does not affect the checksum.</p>
<blockquote class="blockquote-prereq">
<h3 id="prerequisites">Note</h3>
<p>Checksum functions are designed so that similar files <em>will not</em> produce similar hashes.</p>
<p>You will only need to compare a few characters of the string to confirm validity.</p>
</blockquote>
<h2>Commands</h2>
<p>The checksum for file '<em>filename.txt</em>' can be found with the following commands.</p>
<table style="height: 37px;" width="805">
<tbody>
<tr>
<td style="width: 149px;"> </td>
<td style="width: 150px;">Linux</td>
<td style="width: 150px;">Windows(CMD/Powershell)</td>
<td style="width: 150px;">Mac</td>
</tr>
<tr>
<td style="width: 149px;">SH1</td>
<td style="width: 150px;"><code>sha1sum <em>filename.txt</em></code></td>
<td style="width: 150px;"><code>certUtil -hashfile <em>filename.txt</em></code></td>
<td style="width: 150px;"><code>shasum <em>filename.txt</em></code></td>
</tr>
<tr>
<td style="width: 149px;">SHA256</td>
<td style="width: 150px;"><code>sha256sum <em>filename.txt</em></code></td>
<td style="width: 150px;"><code>certUtil -hashfile <em>filename.txt</em> sha256</code></td>
<td style="width: 150px;"><code>shasum -a 256 <em>filename.txt</em></code></td>
</tr>
<tr>
<td style="width: 149px;">MD5</td>
<td style="width: 150px;"><code>md5sum <em>filename.txt</em></code></td>
<td style="width: 150px;"><code>certUtil -hashfile <em>filename.txt</em> md5</code></td>
<td style="width: 150px;"><code>md5 <em>filename.txt</em></code></td>
</tr>
</tbody>
</table>
<p> </p>
<p> </p>