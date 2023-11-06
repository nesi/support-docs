---
created_at: '2018-05-21T04:53:52Z'
hidden: false
label_names:
- storage
position: 3
title: I/O Performance Considerations
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000205355
zendesk_section_id: 360000033936
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p class="western">It is important to understand the different I/O performance characteristics of nodes that connect to storage using <em>native Spectrum Scale clients</em>, and those that employ<em> Cray’s DVS</em> <em>solution</em>.</p>
<p class="western">Applications that make heavy demands on metadata services and or have high levels of small I/O activity should generally not be run on <a href="https://support.nesi.org.nz/hc/articles/360000163695">Māui</a> (the Cray XC50).</p>
<h2 class="western">Nodes which access storage via native Spectrum Scale Clients</h2>
<p class="western">All <a href="https://support.nesi.org.nz/hc/articles/360000163575">Mauhika</a> HPC Cluster, <a href="https://support.nesi.org.nz/hc/articles/360000163595">Mahuika Ancillary</a>, <a href="https://support.nesi.org.nz/hc/articles/360000203776">Māui Ancillary</a> and Māui login (aka build) nodes have native Spectrum Scale clients installed and provide high performance access to storage:</p>
<ul>
<li>Metadata operations of the order of 190,000 file creates /second to a unique directory can be expected;</li>
<li>For 8MB transfer size, single stream I/O is ~3.3GB/s Write and ~5GB/s Read;</li>
<li>For 4KB transfer size, single stream I/O is ~1.3GB/s Write and ~2GB/s Read.</li>
</ul>
<h2 class="western">Nodes which access storage via DVS</h2>
<p class="western">Māui (XC50) utilizes a file system projection method via software, known as DVS (Data Virtualisation Service), to expose the Spectrum Scale file systems to XC compute nodes. DVS adds an additional layer of hardware and software between the XC compute nodes and storage (see Figure).</p>
<p class="western"> <img src="https://support.nesi.org.nz/hc/article_attachments/360000486995/cray_xc50.jpg" alt="cray_xc50.jpg"></p>
<p lang="en-US" align="justify"><font size="2">Figure 1: Cray XC50 DVS architecture.</font></p>
<p class="western">This <em>reduces the I/O performance of Māui for metadata and small (e.g. 4KB) I/O operations</em>. It does not impact the total bandwidth available from the Maui (i.e. ~130 GB/s when writing to the filesystem). Accordingly, the equivalent performance numbers for DVS connected compute nodes are:</p>
<ul>
<li>Metadata operations of the order of 36,000 file creates /second to a unique directory can be expected, i.e. approximately 23% of that achievable on a node that has a Spectrum Scale client.</li>
<li>For 8MB transfer size, single stream I/O, is ~3.2GB/s for Write and ~3.2 GB/s for Read;</li>
<li>For 4KB transfer size, single stream I/O, is ~2.3GB/s for Write and ~2.5GB/s for Read (when using <font face="Courier New, serif">IOBUF </font> – see Caution below). When <font face="Courier New, serif">IOBUF</font> is not used Read and Write performance is &lt;1GB/s.</li>
</ul>
<p class="western">Unless Cray’s <font color="#0000ff"> <u><a href="#_IOBUF_-_Caution">IOBUF</a></u> </font> capability is suitable for an application, <u>users should avoid the use of single-stream I/O with small buffers on </u>Māui.</p>
<h2 class="western"><span class="wysiwyg-color-red">IOBUF - Caution</span></h2>
<p class="western">Cray’s IOBUF ( <font face="Courier New, serif">man iobuf</font> ) is an I/O buffering library that can reduce the I/O wait time for programs that read or write large (or small) files sequentially. IOBUF intercepts standard I/O calls such as read and open and replaces the <font face="Courier New, serif">stdio</font> ( <font face="Courier New, serif">glibc, libio</font> ) layer of buffering with an additional layer of buffering, thus improving program performance by enabling asynchronous prefetching and caching of file data.</p>
<p class="western"><strong>Caution</strong>: IOBUF is not suitable for all I/O styles. IOBUF does not maintain coherent buffering between processes which open the same file. For this reason, do not use IOBUF with shared file I/O, such as MPI-IO routines like <font face="Courier New, serif">MPI_File_write_all</font> . IOBUF is <u>not thread-safe</u>, so do not use it with multithreaded programs in which the threads perform buffered I/O. IOBUF can be linked into programs that use these I/O styles, but buffering should not be enabled on those files.</p>
<h2>Data compression</h2>
<p><span style="color: #1d1c1d; font-family: Slack-Lato, Slack-Fractions, appleLogo, sans-serif; font-size: 15px; font-style: normal; font-variant-ligatures: common-ligatures; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: #ffffff; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;">The file system the NeSI platforms use allow for</span> transparent compression of data, meaning you can reduce the storage footprint of your data without needing to add any extra steps in your workflow unless you want to decompress the data after use. However, testing has shown that there can be an impact on job performance due to I/O. You can find out more about tests and results with regards to jobs performance of transparent data compression on the NeSI platforms on our <a href="https://support.nesi.org.nz/hc/en-gb/articles/6359601973135" target="_self">Data Compression support page</a>.</p>
<p class="western"> </p>