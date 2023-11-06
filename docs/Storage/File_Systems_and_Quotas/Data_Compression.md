---
created_at: '2023-02-08T00:21:51Z'
hidden: false
label_names:
- compression
- data_compression
- lz4
- data compression
- zlib
- z library
- z-library
position: 0
title: Data Compression
vote_count: 0
vote_sum: 0
zendesk_article_id: 6359601973135
zendesk_section_id: 360000033936
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<h1 id="01GZCPY5ZAYCDDS05TPWE8H6RS" data-renderer-start-pos="2">Background</h1>
<p data-renderer-start-pos="2">Spectrum Scale filesystems (previously GPFS) allow users to compress data (but not metadata) transparently on demand without the need to change metadata (file creation and modification dates, etc). This means that that data can be compressed and then used without first needing to decompress it, as the decompression happens automatically in the background without the need for commands. It allows you to treat the data as if it were not compressed.</p>
<p data-renderer-start-pos="2">The data will need to be re-compressed after it is used if you are to maintain it in the compressed state. This can be done by the user (front end) or at the back end via a policy for example. In the future, it is intended that there will be some automatic process regularly compressing flagged files, but at this time, it is only done manually by the NeSI team for specific filesets identified as suitable for the compression; or by the user manually on their own filesets.</p>
<p data-renderer-start-pos="263">For purposes of this Guide, we are going to focus on the user side and what the users can do. As a default, the Zlib compression algorithm will be used, although depending on the version of the filesystem, additional ones might be added. It is possible to change algorithms at any time for any file (we will cover that further ahead) when the compression is requested.</p>
<h1 id="Compression-Methods" data-renderer-start-pos="708">Compression Methods<span class="heading-anchor-wrapper"></span>
</h1>
<p data-renderer-start-pos="729">There are two methods for compressing and decompressing data: <strong data-renderer-mark="true">on-demand</strong> and <strong data-renderer-mark="true">deferred</strong>:</p>
<h2 id="On-Demand-(synchronous)" data-renderer-start-pos="833">On-Demand (synchronous)<span class="heading-anchor-wrapper"></span>
</h2>
<p><strong>note:</strong> <em>as at 2 May 2023, the `mm` commands are not available by default, contact <a href="mailto:support@nesi.org.nz">support@nesi.org.nz</a> for assistance</em></p>
<p data-renderer-start-pos="858">This method (using the <code class="code css-z5oxh7" data-renderer-mark="true">mmchattr</code> command) acts similar to <code class="code css-z5oxh7" data-renderer-mark="true">gzip</code>/<code class="code css-z5oxh7" data-renderer-mark="true">gunzip</code> commands where the file being targeted is compressed or decompressed on command invocation. If the command fails halfway through the file or is cancelled, the file will be marked as "illcompressed" . This state means that the file is only partially compressed.</p>
<p data-renderer-start-pos="1277"><code class="code css-z5oxh7" data-renderer-mark="true">ls</code> command will show files with their original sizes. However,  <code class="code css-z5oxh7" data-renderer-mark="true">du</code> commands will calculate the approximate usage of the file system as opposed to the uncompressed usage. This will be the total counting against quotas as well. Therefore, if files are compressed, quota usage will decrease. And vice versa, if files are decompressed, fully or partially, quota usage will increase. Be aware that if, in the process of decompression, the quota will be exceeded, an error message will be displayed</p>
<div class="code-block  css-iwznuw">
<div>
<pre>$ du -h FileA.txt<br>41M FileA.txt<br><br>$ ls -lh FileA.txt<br>-rw-r--r-- 1 user001 user001 41M Jul 6 01:03 FileA.txt<br><br>$ time mmchattr --compression yes FileA.txt<br>real 0m1.343s<br>user 0m0.002s<br>sys 0m0.000s<br><br>$ ls -lh FileA.txt<br>-rw-r--r-- 1 user001 user001 41M Jul 6 01:03 FileA.txt<br><br>$ du -h FileA.txt<br>8.0M FileA.txt</pre>
</div>
</div>
<h2 id="01GZD2B8MP042PM8KS3B337G67" data-renderer-start-pos="2125"> </h2>
<h2 id="Deferred" data-renderer-start-pos="2125">Deferred<span class="heading-anchor-wrapper"></span>
</h2>
<p data-renderer-start-pos="2135">This method (also using the <code class="code css-z5oxh7" data-renderer-mark="true">mmchattr</code> command) does not decompress or compress data immediately but, instead marks them for compression/decompression to be invoked later. The user can later schedule a secondary task to compress or decompress tagged data. In the future, the deferred tag will flag the data for automatic compression/decompression. This tagging process is quick and can be done by using the same command as above with one extra flag (<code class="code css-z5oxh7" data-renderer-mark="true">-I defer</code>). During this process, there is no change in space occupancy for any of the files involved.</p>
<div class="code-block  css-iwznuw">
<div>
<div class="code-block  css-iwznuw">
<pre>$ du -h FileA.txt<br>41M FileA.txt<br><br>$ ls -lh FileA.txt<br>-rw-r--r-- 1 user001 user001 41M Jul 6 01:03 FileA.txt<br><br>$ time mmchattr -I defer --compression yes FileA.txt<br>real 0m0.002s<br>user 0m0.002s<br>sys 0m0.000s<br><br>$ ls -lh FileA.txt<br>-rw-r--r-- 1 user001 user001 41M Jul 6 01:03 FileA.txt<br><br>&lt;bash&gt;$ du -h FileA.txt<br>41M FileA.txt</pre>
</div>
</div>
</div>
<h4 id="01GRW2VN3S7FHMR92CHBZXQG6E" data-renderer-start-pos="3012"> </h4>
<h3 id="How-to-process-deferred-tagged-files" data-renderer-start-pos="3012">How to process deferred tagged files<span class="heading-anchor-wrapper"></span>
</h3>
<p data-renderer-start-pos="3050">Users can process compression/decompression on the tagged files via the <code class="code css-z5oxh7" data-renderer-mark="true">mmrestripefile</code> command (using <code class="code css-z5oxh7" data-renderer-mark="true">-z</code> flag).</p>
<div class="code-block  css-iwznuw">
<div></div>
</div>
<pre data-renderer-start-pos="3314">$ mmrestripefile -z FileA.txt<br>Scanning FileA.txt<br>Scan completed successfully.</pre>
<h1 id="States-of-a-compressed-file" data-renderer-start-pos="3316">States of a compressed file<span class="heading-anchor-wrapper"></span>
</h1>
<p data-renderer-start-pos="3345">Compressed files on Scale filesystems can be in 4 different states depending on the extended attributes of the file when manipulated for compression. We can check those attributes with the <code class="code css-z5oxh7" data-renderer-mark="true">mmlsattr</code> command:</p>
<pre data-renderer-start-pos="3906">$ mmlsattr -L FileA.txt<br>file name: FileA.txt<br>metadata replication: 1 max 2<br>data replication: 1 max 2<br>immutable: no<br>appendOnly: no<br>flags:<br>storage pool name: data<br>fileset name: home_user001<br>snapshot name:<br>creation time: Wed Jul 6 00:54:27 2022<br>Misc attributes: ARCHIVE<br>Encrypted: no</pre>
<p data-renderer-start-pos="3906">The misc attributes will have or not have a <code class="code css-z5oxh7" data-renderer-mark="true">COMPRESSION</code> value, depending on if the file is or not tagged for compression. In addition, a file will exhibit the flag <code class="code css-z5oxh7" data-renderer-mark="true">illcompressed</code> when the desired final state is not the achieved yet (fully compressed or uncompressed).</p>
<p data-renderer-start-pos="4169">A file that is fully compressed (not showing the flag <code class="code css-z5oxh7" data-renderer-mark="true">illcompressed</code> and having the misc attribute <code class="code css-z5oxh7" data-renderer-mark="true">COMPRESSION</code> ), if updated or appended data to, becomes automatically <code class="code css-z5oxh7" data-renderer-mark="true">illcompressed</code> and either needs to be re-compressed using the <code class="code css-z5oxh7" data-renderer-mark="true">mmchattr --compression yes</code> command or the <code class="code css-z5oxh7" data-renderer-mark="true">mmrestripefile -z</code> one (because it's already tagged for compression).</p>
<h4 id="The-different-states" data-renderer-start-pos="4508">The different states<span class="heading-anchor-wrapper"></span>
</h4>
<ul>
<li>
<p data-renderer-start-pos="4532"><strong data-renderer-mark="true">Uncompressed</strong> and <strong data-renderer-mark="true">untagged</strong> for compression (default) - as shown for the file <code class="code css-z5oxh7" data-renderer-mark="true">FileA.txt</code> above.</p>
</li>
<li>
<p data-renderer-start-pos="4628"><strong data-renderer-mark="true">Partially compressed </strong>and <strong data-renderer-mark="true">tagged</strong> for compression - When file is partially compressed (either because it was decompressed for access or the full compression didn’t finish). It is still marked for compression as the <code class="code css-z5oxh7" data-renderer-mark="true">COMPRESSION</code> misc attribute suggests, but because it's not fully compressed the <code class="code css-z5oxh7" data-renderer-mark="true">illcompressed</code> flag will be shown.</p>
<div class="code-block  css-iwznuw">
<div>
<pre>$ mmlsattr -L FileA.txt<br>file name: FileA.txt<br>metadata replication: 1 max 2<br>data replication: 1 max 2<br>immutable: no<br>appendOnly: no<br>flags: illcompressed<br>storage pool name: data<br>fileset name: home_user001<br>snapshot name:<br>creation time: Wed Jul 6 00:54:27 2022<br>Misc attributes: ARCHIVE COMPRESSION (library z)<br>Encrypted: no<span class="prismjs css-1g7m763" data-code-lang="" data-ds--code--code-block=""></span><span class="prismjs css-1g7m763" data-code-lang="" data-ds--code--code-block=""></span></pre>
</div>
</div>
</li>
<li>
<p data-renderer-start-pos="5364"><strong data-renderer-mark="true">Fully compressed </strong>and <strong data-renderer-mark="true">tagged</strong> for compression - The file is fully compressed to its maximum possible state and because the file is tagged for compression, only the misc attribute <code class="code css-z5oxh7" data-renderer-mark="true">COMPRESSION</code> will be shown.</p>
<div class="code-block  css-iwznuw">
<div>
<pre>$ mmlsattr -L FileA.txt<br>file name: FileA.txt<br>metadata replication: 1 max 2<br>data replication: 1 max 2<br>immutable: no<br>appendOnly: no<br>flags:<br>storage pool name: data<br>fileset name: home_user001<br>snapshot name:<br>creation time: Wed Jul 6 00:54:27 2022<br>Misc attributes: ARCHIVE COMPRESSION (library z)<br>Encrypted: no<span class="prismjs css-1g7m763" data-code-lang="" data-ds--code--code-block=""></span></pre>
</div>
</div>
</li>
<li>
<p data-renderer-start-pos="5949"><strong data-renderer-mark="true">Full or partially compressed </strong>and <strong data-renderer-mark="true">untagged</strong> for compression - The file might be fully or partially compressed and in this case because the misc attribute <code class="code css-z5oxh7" data-renderer-mark="true">COMPRESSION</code> is not shown, it means the file is untagged for being compressed (meaning it's tagged to be in the uncompressed state). When a fully compressed file is untagged, the flag <code class="code css-z5oxh7" data-renderer-mark="true">illcompressed</code> will be shown. After full decompression is complete the file will become uncompressed and untagged for compression.</p>
<div class="code-block  css-iwznuw">
<div>
<pre>$ mmlsattr -L FileA.txt<br>file name: FileA.txt<br>metadata replication: 1 max 2<br>data replication: 1 max 2<br>immutable: no<br>appendOnly: no<br>flags: illcompressed<br>storage pool name: data<br>fileset name: home_user001<br>snapshot name:<br>creation time: Wed Jul 6 00:54:27 2022<br>Misc attributes: ARCHIVE<br>Encrypted: no</pre>
</div>
</div>
</li>
</ul>
<h1 id="Using-different-algorithms" data-renderer-start-pos="6801">Using different compression algorithms<span class="heading-anchor-wrapper"></span>
</h1>
<p data-renderer-start-pos="6829">The default algorithm is the Zlib and will be shown on the misc attributes of a tagged file as “library z”. Depending on the Scale version installed, files can be tagged with different algorithms.</p>
<p data-renderer-start-pos="7026">Currently supported compression libraries are:</p>
<ul class="ak-ul" data-indent-level="1">
<li>
<p data-renderer-start-pos="7070">z Cold data. Favours compression efficiency over access speed.</p>
</li>
<li>
<p data-renderer-start-pos="7135">lz4 Active, non-specific data. Favours access speed over compression efficiency.</p>
</li>
</ul>
<h1 id="Timing" data-renderer-start-pos="7612">Performance impacts<span class="heading-anchor-wrapper"></span>
</h1>
<p data-renderer-start-pos="7620">Experiments showed that I/O performance was definitely affected if a file was in a compressed state. The extent of the effect, however, depends on the magnitude of I/O operations on the affected files.  I/O intensive workloads may experience a significant performance drop.<br><br>If compression has a significant impact on your software performance, please confirm it first by running a test job with and without compression and then contact us at <a href="mailto:support@nesi.org.nz">support@nesi.org.nz</a>. We will help you minimise the impact of compression on your workflow or find other ways to help you manage your project storage.</p>
<p data-renderer-start-pos="12002">If you are interested in learning more about this type of data compression <a href="https://www.ibm.com/docs/en/spectrum-scale/4.2.2?topic=systems-file-compression">you can find further details on the IBM website</a>.</p>