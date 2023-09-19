---
created_at: '2018-04-22T21:09:28Z'
hidden: false
label_names:
- hpc
- info
- mahuika
- cs400
position: 3
title: Mahuika
vote_count: 6
vote_sum: 2
zendesk_article_id: 360000163575
zendesk_section_id: 360000034335
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p>Mahuika is a Cray CS400 cluster featuring Intel Xeon Broadwell nodes, FDR InfiniBand interconnect, and NVIDIA GPGPUs.</p>
<p>Mahuika is designed to provide a capacity, or high throughput, HPC resource that allows researchers to run many small (from one to a few hundred CPU cores) compute jobs simultaneously, and to conduct interactive data analysis. To support jobs that require large (up to 500GB) or huge (up to 4 TB) memory, or GPGPUs, and to provide virtual lab services, Mahuika has additional nodes optimised for this purpose.</p>
<p>The Mahuika login (or build) nodes, mahuika01 and mahuika02, provide access to GNU, Intel and Cray programming environments, including editors, compilers, linkers, and debugging tools. Typically, users will ssh to these nodes after logging onto the NeSI lander node.</p>
<h3 id="h_01H96W0P53DY1QQXM5YQRE2276">Notes</h3>
<ol>
<li>The Cray Programming Environment on Mahuika, differs from that on Māui.</li>
<li>The <code>/home, /nesi/project</code>, and <code>/nesi/nobackup</code> <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000177256" target="_blank" rel="noopener">filesystems</a> are mounted on Mahuika.</li>
<li>Read about how to compile and link code on Mahuika in section entitled: <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000329015" target="_blank" rel="noopener">Compiling software on Mahuika.</a>
</li>
<li>An extension to Mahuika with additional, upgraded resources is also available. see <a href="https://support.nesi.org.nz/hc/en-gb/articles/6367209795471-Milan-Compute-Nodes" target="_self">Milan Compute Nodes</a> for details on access</li>
</ol>
<h2 id="h_01H96W0P5313KDX18BRQVBX4HH">Mahuika HPC Cluster (Cray CS400)</h2>
<table style="width: 700px; height: 658px;">
<tbody>
<tr style="height: 55px;">
<td style="height: 55px; width: 240.278px;">
<p><span class=""><strong>Login nodes</strong></span></p>
</td>
<td style="height: 55px; width: 436.389px;">
<p><span class="">72 cores in 2× Broadwell (E5-2695v4, 2.1 GHz, dual socket 18 cores per socket) nodes</span></p>
</td>
</tr>
<tr style="height: 27.4333px;">
<td style="height: 27px; width: 240.278px;">
<p><span class=""><strong>Compute nodes</strong></span></p>
</td>
<td style="height: 27px; width: 436.389px;">
<p><span class="">8,136 cores in 226 × Broadwell (E5-2695v4, 2.1 GHz, dual socket 18 cores per socket) nodes;<br>7,552 cores in 64 <span>HPE Apollo 2000 XL225n nodes (</span><a href="https://www.amd.com/en/products/cpu/amd-epyc-7713" target="_blank" rel="noopener">AMD EPYC Milan 7713</a>) the Milan partition</span></p>
</td>
</tr>
<tr style="height: 22px;">
<td style="height: 22px; width: 240.278px;">
<p><span class=""><strong>Compute nodes (reserved for NeSI Cloud)<br></strong></span></p>
</td>
<td style="height: 22px; width: 436.389px;">
<p><span class="">288 cores in 8 × Broadwell (E5-2695v4, 2.1 GHz, dual socket 18 cores per socket) nodes</span></p>
</td>
</tr>
<tr style="height: 148px;">
<td style="width: 240.278px; height: 148px;">
<p><span class=""><strong>GPUs<br></strong></span></p>
</td>
<td style="width: 436.389px; height: 148px;">
<p><span class="">9 NVIDIA Tesla P100 PCIe 12GB cards (1 node with 1 GPU, </span>4 nodes with 2 GPUs)</p>
<p><span class="">8 NVIDIA A100 PCIe 40GB cards (4 nodes with 1 GPU, 2 nodes with 2 GPUs)<br></span></p>
<p><span class="">16 NVIDIA A100 HGX 80GB cards (4 nodes with 4 GPU each)</span><span class=""></span></p>
</td>
</tr>
<tr style="height: 22px;">
<td style="height: 22px; width: 240.278px;">
<p><span class=""><strong>Hyperthreading</strong></span></p>
</td>
<td style="height: 22px; width: 436.389px;">
<p><span class="">Enabled (accordingly, SLURM will see ~31,500 cores)</span></p>
</td>
</tr>
<tr style="height: 27px;">
<td style="height: 27px; width: 240.278px;">
<p><span class=""><strong>Theoretical Peak Performance</strong></span></p>
</td>
<td style="height: 27px; width: 436.389px;">
<p><span class="">308.6 TFLOPs</span></p>
</td>
</tr>
<tr style="height: 70px;">
<td style="height: 70px; width: 240.278px;">
<p><span class=""><strong>Memory capacity per compute node</strong></span></p>
</td>
<td style="height: 70px; width: 436.389px;">
<p><span class="">128 GB</span></p>
</td>
</tr>
<tr style="height: 70px;">
<td style="height: 70px; width: 240.278px;">
<p><span class=""><strong>Memory capacity per login (build) node</strong></span></p>
</td>
<td style="height: 70px; width: 436.389px;">
<p><span class="">512 GB</span></p>
</td>
</tr>
<tr style="height: 49px;">
<td style="height: 49px; width: 240.278px;">
<p><span class=""><strong>Total System memory</strong></span></p>
</td>
<td style="height: 49px; width: 436.389px;">
<p><span class="">84.0 TB</span></p>
</td>
</tr>
<tr style="height: 70px;">
<td style="height: 70px; width: 240.278px;">
<p><span class=""><strong>Interconnect</strong></span></p>
</td>
<td style="height: 70px; width: 436.389px;">
<p><span class="">FDR (54.5Gb/s) InfiniBand to EDR (100Gb/s) Core fabric. 3.97:1 Fat-tree topology</span></p>
</td>
</tr>
<tr style="height: 49px;">
<td style="height: 49px; width: 240.278px;">
<p><span class=""><strong>Workload Manager</strong></span></p>
</td>
<td style="height: 49px; width: 436.389px;">
<p><span class="">Slurm (Multi-Cluster)</span></p>
</td>
</tr>
<tr style="height: 49px;">
<td style="height: 49px; width: 240.278px;">
<p><span class=""><strong>Operating System</strong></span></p>
</td>
<td style="height: 49px; width: 436.389px;">
<p><span class="">CentOS 7.4 &amp; Rocky 8.5 on Milan</span></p>
</td>
</tr>
</tbody>
</table>
<p> </p>
<h2 id="h_01H96W0P54KT52HN8ZFTJXQNT7"> Storage (IBM ESS)</h2>
<table style="width: 700px;">
<tbody>
<tr>
<td width="186">
<p><span class=""><strong>Scratch storage</strong></span></p>
</td>
<td width="418">
<p><span class="">4,412 TB (IBM Spectrum Scale, version 5.0). Total I/O bandwidth to disks is ~130 GB/s</span></p>
</td>
</tr>
<tr>
<td width="186">
<p><span class=""><strong>Persistent storage</strong></span></p>
</td>
<td width="418">
<p><span class="">1,765 TB (IBM Spectrum Scale, version 5.0). Shared between Mahuika and Maui. Total I/O bandwidth to disks is ~65 GB/s (i.e. the /home and /nesi/project filesystems)</span></p>
</td>
</tr>
<tr>
<td width="186">
<p><span class=""><strong>Offline storage</strong></span></p>
</td>
<td width="418">
<p><span class="">Of the order of 100 PB (compressed)</span></p>
</td>
</tr>
</tbody>
</table>
<p>Scratch and persistent storage are accessible from Mahuika, as well as from Māui and the ancillary nodes. Offline storage will in due course be accessible indirectly, via a dedicated service.</p>
<p> </p>
<p> </p>