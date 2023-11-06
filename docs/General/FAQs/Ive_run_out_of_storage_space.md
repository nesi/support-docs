---
created_at: '2019-08-26T00:02:24Z'
hidden: false
label_names:
- disk quota exceeded
position: 0
title: I've run out of storage space
vote_count: 3
vote_sum: 1
zendesk_article_id: 360001125996
zendesk_section_id: 360000039036
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>There are two tracked resources in the NeSI filesystem, <em>disk space</em> and <em>inodes (number of files) </em>.</p>
<p>Trying to write to a filesystem over its inode or disk quota will cause an error (and probably kill your job).</p>
<p>Current file-count and disk space can be found using <code>nn_storage_quota</code>.</p>
<pre><code class="hljs css"><span class="hljs-selector-tag">Filesystem</span>         <span class="hljs-selector-tag">Available</span>      <span class="hljs-selector-tag">Used</span>     <span class="hljs-selector-tag">Use</span>%     <span class="hljs-selector-tag">Inodes</span>     <span class="hljs-selector-tag">IUsed</span>     <span class="hljs-selector-tag">IUse</span>%<br><span class="hljs-selector-tag">home_user123</span>             20<span class="hljs-selector-tag">G</span>    1<span class="hljs-selector-class">.957G</span>    <span class="wysiwyg-color-red">9<span class="hljs-selector-class">.79</span>%</span>      92160     21052    <span class="wysiwyg-color-red">22<span class="hljs-selector-class">.84</span>%</span><br><span class="hljs-selector-tag">project_nesi99999</span>         2<span class="hljs-selector-tag">T</span>      798<span class="hljs-selector-tag">G</span>   <span class="wysiwyg-color-red110">38<span class="hljs-selector-class">.96</span>%</span>     100000     66951    <span class="wysiwyg-color-red">66<span class="hljs-selector-class">.95</span>%</span><br><span class="hljs-selector-tag">nobackup_nesi99999</span>              6<span class="hljs-selector-class">.833T</span>            10000000    2691383   <span class="wysiwyg-color-red">26<span class="hljs-selector-class">.91</span>%</span></code></pre>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>There is a delay between making changes to a filesystem and seeing the change in <code>nn_storage_quota</code>, immediate file count and disk space can be found using the commands <code>du --inodes</code> and <code>du -h</code> respectively.</p>
</blockquote>
<p>There are a few ways to deal with file count problems</p>
<ul>
<li>
<strong>Use </strong><code>/nesi/nobackup/&lt;projectcode&gt;</code><br>The nobackup directory has a significantly higher inode count and no disk space limits. Files here are not backed up, so best used for intermediary or replaceable data.</li>
<li>
<strong>Delete unnecessary files</strong><br>Some applications will generate a large number of files during runtime, using the command <code>du --inodes -d 1 | sort -hr</code> (for inodes) or <code>du -h -d 1 | sort -hr</code> for disk space.  You can then drill down into the directories with the largest file count deleting files as viable.</li>
<li>
<strong>SquashFS archive (recommended)</strong><br>Many files can be compressed into a single SquashFS archive. We have written a utility, <code>nn_archive_files</code>, to help with this process. This utility can be run on Māui or Mahuika, but not, as yet, on Māui-ancil; and it can submit the work as a Slurm job, which is preferred. <code>nn_archive_files</code> can take, as trailing options, the same options as <code>mksquashfs</code>, including choice of compression algorithm; see <code>man mksquashfs</code> for more details.<br>
<pre><code>nn_archive_files -p &lt;project-code&gt; -n &lt;num-processors&gt; -t &lt;time-limit&gt; --verify -- /path/containing/files /path2/containing/files destination.squash</code></pre>
Then when files need to be accessed again they can be extracted using,
<pre><code>/usr/sbin/unsquashfs destination.squash</code></pre>
You can do many other things with SquashFS archives, like quickly list the files in the archive, extract some but not all of the contents, and so on. See <code>man unsquashfs</code> for more details.</li>
<li>
<strong>Tarball (usable, but SquashFS is recommended)</strong><br>Many files can be compressed into a single 'tarball' <br>
<pre><code>tar -czf name.tar /path/containing/files/</code></pre>
Then when files need to be accessed again they can be un-tarred using,
<pre><code>tar -xzf tarname.tar</code></pre>
</li>
<li>
<strong>Contact Support</strong><br>If you are following the recommendations here yet are still concerned about inodes or disk space, open a <a href="https://support.nesi.org.nz/hc/en-gb/requests/new" target="_blank" rel="noopener">support ticket</a> and we can raise the limit for you.</li>
</ul>