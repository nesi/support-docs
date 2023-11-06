---
created_at: '2018-05-21T01:43:06Z'
hidden: false
label_names:
- maui
- XC50
- cs500
position: 5
title: "M\u0101ui Ancillary"
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000203776
zendesk_section_id: 360000034335
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>The Māui Ancillary Nodes provide access to a Virtualised environment that supports:</p>
<ol>
<li>Pre- and post-processing of data for jobs running on the <a href="https://support.nesi.org.nz/hc/articles/360000163695">Maui</a> Supercomputer or <a href="https://support.nesi.org.nz/hc/articles/360000163575">Mahuika</a> HPC Cluster. Typically, as serial processes on a Slurm partition running on a set of Ancillary node VMs or baremetal servers.</li>
<li>Virtual laboratories that provide interactive access to data stored on the Māui (and Mahuika) storage together with domain analysis toolsets (e.g. Seismic, Genomics, Climate, etc.). To access the Virtual Laboratory nodes, users will first logon to the NeSI Lander node, then ssh to the relevant Virtual Laboratory. Users may submit jobs to Slurm partitions from Virtual Laboratory nodes.</li>
<li>Remote visualisation of data resident on the filesystems.</li>
<li>GPGPU computing.</li>
</ol>
<p>Scientific Workflows may access resources across the Māui Supercomputer and any (multi-cluster) Slurm partitions on the Māui or Mahuika systems.</p>
<h3>Notes:</h3>
<ol>
<li>The <code>/home, /nesi/project</code>, and <code>/nesi/nobackup</code> <a href="https://support.nesi.org.nz/hc/articles/360000177256">filesystems</a> are mounted on the Māui Ancillary Nodes.</li>
<li>The Maui Ancillary nodes have Skylake processors, while the Mahuika nodes use Broadwell processors.</li>
</ol>
<h2>Ancillary Node Specifications</h2>
<table style="width: 650px;">
<tbody>
<tr>
<td style="width: 182.767px;">
<p><strong>Multi-Purpose nodes</strong></p>
</td>
<td style="width: 444.233px;">
<p>1,120 cores in 28 × Skylake (Gold 6148, 2.4 GHz, dual socket 20 cores per socket) nodes, which will appear as 2,240 logical cores.</p>
</td>
</tr>
<tr>
<td style="width: 182.767px;">
<p><strong>Hyperthreading</strong></p>
</td>
<td style="width: 444.233px;">
<p>Enabled</p>
</td>
</tr>
<tr>
<td style="width: 182.767px;">
<p><strong>Local Disk</strong></p>
</td>
<td style="width: 444.233px;">
<p>1.2TB SSD</p>
</td>
</tr>
<tr>
<td style="width: 182.767px;">
<p><strong>Operating System</strong></p>
</td>
<td style="width: 444.233px;">
<p>CentOS 7.4</p>
</td>
</tr>
<tr>
<td style="width: 182.767px;">
<p><strong>GPGPUs</strong></p>
</td>
<td style="width: 444.233px;">
<p>5 <span class="">NVIDIA Tesla P100 PCIe 12GB</span> (5 nodes with 1 GPU)</p>
</td>
</tr>
<tr>
<td style="width: 182.767px;">
<p><strong>Remote Visualisation</strong></p>
</td>
<td style="width: 444.233px;">
<p><a href="https://www.nice-software.com/products/dcv">NICE DCV</a></p>
</td>
</tr>
<tr>
<td style="width: 182.767px;">
<p><strong>Memory capacity per Multi-Purpose node</strong></p>
</td>
<td style="width: 444.233px;">
<p>768 GB</p>
</td>
</tr>
<tr>
<td style="width: 182.767px;">
<p><strong>Interconnect</strong></p>
</td>
<td style="width: 444.233px;">
<p>EDR (100 Gb/s) InfiniBand</p>
</td>
</tr>
<tr>
<td style="width: 182.767px;">
<p><strong>Workload Manager</strong></p>
</td>
<td style="width: 444.233px;">
<p>Slurm (Multi-Cluster)</p>
</td>
</tr>
<tr>
<td style="width: 182.767px;">
<p><strong>OpenStack</strong></p>
</td>
<td style="width: 444.233px;">
<p>The Cray CS500 Ancillary nodes will normally be presented to users as Virtual Machines, provisioned from the physical hardware as required.</p>
</td>
</tr>
</tbody>
</table>
<p> </p>
<p>The Māui_Ancil nodes have different working environment than the Maui (login) nodes. Therefore a CS500 login node is provided, to create and submit your jobs on this architecture. To use you need to login from maui login nodes to:</p>
<pre><code>w-mauivlab01.maui.nesi.org.nz</code></pre>
<p>If you are looking for accessing this node from your local machine you could add the following section to <code class="nohighlight">~/.ssh/config</code> (extending the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000625535-Recommended-Terminal-Setup" target="_self">recommended terminal setup</a>)</p>
<pre><code>Host w-mauivlab01 
  User &lt;username&gt; 
  Hostname w-mauivlab01.maui.nesi.org.nz 
  ProxyCommand ssh -W %h:%p maui 
  ForwardX11 yes
  ForwardX11Trusted yes
  ServerAliveInterval 300
  ServerAliveCountMax 2</code></pre>