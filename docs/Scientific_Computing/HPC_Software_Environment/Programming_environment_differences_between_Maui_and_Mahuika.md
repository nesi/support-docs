---
created_at: '2018-04-23T00:52:59Z'
hidden: false
label_names:
- info
- software
- application
- cs400
- XC50
position: 19
title: Programming environment differences between Maui and Mahuika
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000164576
zendesk_section_id: 360000040056
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p>The compile environment of Māui and Mahuika have various similarities, but also significant differences. Both systems are configured with the Cray Programming Environment (CPE), but these vary in detail. In general we distinguish, between the XC50 part of Māui and the CS (Mahuika, Mahuika Ancillary Nodes, and Māui Ancillary nodes) systems.</p>
<p><span class="wysiwyg-font-size-small">Table 1: The Cray Programming Environment on Māui and Mahuika. Black text indicates components common to both systems, green to components only available on Mahuika, and blue to components only available on Māui XC part.<br></span></p>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>
<p>Programming Languages</p>
</th>
<th>
<p>Programming Models</p>
</th>
<th>
<p>Compilers</p>
</th>
<th>
<p>Tools</p>
</th>
<th>
<p>Optimised Scientific Libraries</p>
</th>
<th>
<p>I/O Libraries</p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="4">
<p>Fortran</p>
<p>C</p>
<p>C++</p>
<p>Chapel</p>
</td>
<td>
<p>Distributed Memory:</p>
<p>MPI Support:</p>
<p><span class="wysiwyg-color-green120">· Intel MPI<sup>1</sup></span></p>
<p><span class="wysiwyg-color-green120">· </span><span class="wysiwyg-color-green120">MVAPICH2<sup>1</sup></span></p>
<p><span class="wysiwyg-color-green120">· OpenMPI<sup>1</sup></span></p>
<p><span class="wysiwyg-color-green120">· MPICH<sup>1</sup></span></p>
<p><span class="wysiwyg-color-green120">· Cray-MVAPICH2<sup>1</sup></span> </p>
<p><span class="wysiwyg-color-blue80">Cray MPT<sup>2</sup>:</span></p>
<p><span class="wysiwyg-color-blue80">· MPI</span></p>
</td>
<td>
<p>· Cray Compiling Environment (CCE)</p>
<p>· GNU</p>
<p>· Intel</p>
</td>
<td>
<p>Performance Analysis:</p>
<p>· CrayPat &amp; Cray Apprentice2</p>
<p>· Allinea MAP</p>
<p>· Intel Vtune Amplifier XE, Advisor, <span class="wysiwyg-color-green120">Trace Analyser &amp; Collector</span></p>
</td>
<td>
<p>Dense:</p>
<p>· BLAS</p>
<p>· LAPACK</p>
<p>· ScaLAPACK</p>
<p>· Iterative Refinement Tool</p>
</td>
<td rowspan="4">
<p><span class="wysiwyg-color-blue80">NetCDF<sup>2</sup></span></p>
<p><span class="wysiwyg-color-blue80">HDF<sup>2</sup></span></p>
</td>
</tr>
<tr>
<td>
<p>Shared Memory</p>
<p>· OpenMP 4.0</p>
<p>· OpenACC 2.0</p>
</td>
<td>
<p>Environment Setup</p>
<p>· Modules</p>
<p><span class="wysiwyg-color-green120">· Lmod<sup>1</sup></span></p>
<p> </p>
</td>
<td>
<p>Porting Tools:</p>
<p>· Reveal</p>
<p>· CCDB</p>
</td>
<td>
<p>FFT:</p>
<p>· FFTW</p>
</td>
</tr>
<tr>
<td>
<p>PGAS</p>
<p>· UPC</p>
<p>· CAF</p>
<p>· CoArray C++</p>
</td>
<td>
<p> </p>
</td>
<td>
<p>Debuggers:</p>
<p>· lgdb</p>
<p>· Allinea DDT</p>
<p><span class="wysiwyg-color-blue80">· ATP<sup>2</sup></span></p>
<p><span class="wysiwyg-color-blue80">· STAT<sup>2</sup></span></p>
</td>
<td>
<p><span class="wysiwyg-color-blue80">Sparse:</span></p>
<p><span class="wysiwyg-color-blue80">· Cray PETSc (with CASK)<sup>2</sup></span></p>
<p><span class="wysiwyg-color-blue80">· Cray Trilinos (with CASK)<sup>2</sup></span></p>
</td>
</tr>
<tr>
<td>
<p> </p>
</td>
<td>
<p> </p>
</td>
<td>
<p>Data Analytics</p>
<p><span class="wysiwyg-color-blue80">· Urika XC Data Analytics<sup>2</sup></span></p>
<p><span class="wysiwyg-color-blue80">· Cray Graph Engine<sup>2</sup></span></p>
</td>
<td>
<p> </p>
</td>
</tr>
</tbody>
</table>
<p><strong>Notes: </strong></p>
<ol>
<li><span class="wysiwyg-color-green120"><sup>1</sup>Only available on Mahuika HPC Cluster, Mahuika Ancillary Nodes and Māui Ancillary nodes</span></li>
<li><span class="wysiwyg-color-blue80"><sup>2</sup>Only available on Māui Supercomputer.</span></li>
<li>On Māui (XC50) the Modules framework is used to simplify access to the various compiler suites and libraries. To access a particular compiler suite, you simply load (or switch to) the appropriate programming environment module using the command PrgEnv-X (where X is one of gnu, intel, or cray). This facility is not available on the Mahuika HPC Cluster, Mahuika Ancillary Nodes and Māui Ancillary nodes.</li>
<li>
<a href="https://software.intel.com/en-us/node/685016">Intel Parallel Studio XE Cluster Edition</a> for Linux will be installed on the Mahuika HPC Cluster, Mahuika Ancillary Nodes and Māui Ancillary nodes.</li>
<li>Intel Parallel Studio XE Professional Edition for CLE will be installed installed on Māui.</li>
</ol>
<h2>Key Similarities  between CPE on XC50 and CS400/500s</h2>
<p>As shown in the table above, Cray provides a list of tools, libraries, and compilers for both platforms. The Cray compiler environment comes with the compiler, basic numeric libraries, automatically including compile and link flags for system architecture and libraries (enabled/disabled by loading modules), and the Cray performance analysis tools (CrayPAT)</p>
<h2>Key Differences between CPE on XC50 and CS400/500s</h2>
<p>There are many similarities between the XC and CS programming environments (compilers and many tools and libraries are the same or at least similar), but also some important differences that affect how a user interacts with the system when building an application code:</p>
<ul>
<li>The XC platform uses compiler drivers (“ftn”, “cc”, “CC”), users should not use compilers directly. The CS platforms have compiler drivers only for Cray compiler. For GNU and Intel compilers, users run “gfortran”, “ifort”, “gcc”, “icc” etc.;</li>
<li>On the XC platform, a compiler is chosen by switching to its corresponding “PrgEnv-xxx” module. This will also switch automatically the version of the loaded Cray provided libraries, e.g., the cray-netcdf and cray-fftw library modules – no equivalent is available on the CS platforms; On the CS platforms the main software stack is based on Easybuild toolchains. The default one is “gimkl”, including GCC, Intel MPI, and Intel MKL.</li>
<li>The XC platform requires everyone to use Cray-MPI, but on the CS platform, users can choose to use various MPI libraries;</li>
<li>Getting rid of all modules via “module purge” renders an XC session unusable (a list of ~20 modules are necessary to guarantee operation). On CS there are only few modules necessary, the main one is called “NeSI”, providing the NeSI software stack and slurm module;</li>
<li>The XC platform defaults to static linking, the CS platform to dynamic linking;</li>
</ul>
<p>In summary, compilers, as well as various tools and libraries are common across both platforms. However, there are important differences in how the programming environment is used, requiring users to familiarise themselves with each platform. For more information see the specific user guides for <a href="https://nesi.github.io/hpc_training/lessons/maui-and-mahuika/building-code-mahuika">Mahuika (and Ancillary nodes)</a> and <a href="https://nesi.github.io/hpc_training/lessons/maui-and-mahuika/building-code-maui"> Māui XC50</a>.</p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>