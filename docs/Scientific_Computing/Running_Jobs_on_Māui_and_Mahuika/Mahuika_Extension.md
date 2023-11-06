---
created_at: '2022-08-09T23:13:33Z'
hidden: true
label_names: []
position: 0
title: Mahuika Extension
vote_count: 0
vote_sum: 0
zendesk_article_id: 5286956022159
zendesk_section_id: 360000030876
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p> </p>
<h1 id="01GAG6XAK1FF5ZNPMT8RF6MCWZ">Differences from other Mahuika compute nodes<span class="wysiwyg-font-size-x-large"></span>
</h1>
<h2><strong>Hardware</strong></h2>
<p>Each node has two AMD Milan CPU chips, each with 8 chiplets, each of which have 8 cores and one level 3 cache, so each node has a total of <strong>128 cores</strong> or 256 hyperthreaded CPUs.  This represents a significant increase of the number CPUs per node compared to the Broadwell nodes (36 cores). </p>
<p>It therefore makes sense to use a power of two for the number of cores requested by a job.<br><br>AMD Milan CPU overview, each node has two of these:</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/5300908636815/milan.png" alt="milan.png" width="377" height="395"></p>
<p><span class="wysiwyg-font-size-small"><strong>AMD-EPYC-Milan-architecture </strong>from <a style="background-color: #ffffff;" href="https://www.hpcwire.com/2021/03/15/amd-launches-epyc-milan-with-19-skus-for-hpc-enterprise-and-hyperscale/#foobox-4/0/AMD-Epyc-Milan-architecture.png" target="_self">HPCwire</a></span><span class="wysiwyg-font-size-small"></span></p>
<p><br>An overview of the AMD Milan CPUs can be found on the <a href="https://www.amd.com/en/processors/epyc-7003-series" target="_self">AMD website</a>.</p>
<p> </p>
<p><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">The memory available to Slurm jobs on these nodes is 460 GB, so approximately 1800 MB per CPU.  </span></p>
<p>Only 30 nodes are available so far, but that number will eventually increase to 64, eight of which will have double the memory.</p>
<h2 id="01GAG6XAK2WZMMAHZX0WJ98RF6"><strong><span class="wysiwyg-font-size-large">Operating System</span></strong></h2>
<p>The existing Mahuika compute nodes use Linux Centos 7.4 while Mahuika Extension use Rocky 8.5.  These are closely related Linux distributions. The move from 7 to 8 is more significant than the move from Centos to Rocky.</p>
<p>Many system libraries have changed version numbers between versions 7 and 8, so <strong>some software compiled on Centos 7 will not run as-is on Rocky 8</strong>. This can result in the runtime error<code>error while loading shared libraries:... cannot open shared object file</code>,  which can be fixed by providing a copy of the old system library.  </p>
<p>We have repaired several of our existing environment modules that way.  For programs which you have compiled yourself, we have installed a new environment module that provides many of the Centos 7 libraries:</p>
<pre>module load LegacySystemLibs/7</pre>
<p>Please let us know if that isn't sufficient to get your existing compiled code running on the new nodes.</p>
<p>Of course you can also recompile code inside a job run in the milan partition and so produce an executable linked against the new system libraries, but then that would be unlikely to work on the old nodes.</p>
<p>In the longer term all Mahuika nodes will be upgraded to Rocky 8.</p>
<h2 id="01GAG6XAK2NPSX27CEWEPHD0NJ"><strong><span class="wysiwyg-font-size-large">Older Intel and Cray software</span></strong></h2>
<p>The directories <code>/cm</code> and <code>/opt/cray</code> contain software which was installed on Mahuika when we purchased it rather than installed by the NeSI Application Support team. They are not present on the new nodes. As with the system libraries, you could take a copy of these libraries and carry on, but it is best to migrate away from using them if possible.</p>
<p>This affects our pre-2020 toolchains such as<em> intel/2018b</em>, but we should have newer versions of such software already installed in most cases.</p>
<h2 id="01GAG6XAK23RF9SHH94QH011RK"><span class="wysiwyg-font-size-large"><strong>Intel MKL performance</strong></span></h2>
<p>In many ways, Intel's MKL is the best implementation of the BLAS and LAPACK libraries to which we have access, which is why we use it in our "<em>intel</em>" and "<em>gimkl</em>" toolchains.  Unfortunately, recent versions of MKL deliberately choose not to use the accelerated AVX instructions when not running on an Intel CPU.  </p>
<p>In order to persuade MKL to use the same fast optimised kernels on the new AMD Milan CPUs, you can do</p>
<pre>module load AlwaysIntelMKL</pre>
<p>We have set that as the default for our most recent toolchain <em>gimkl/2022a</em>.</p>
<p>Two alternative implementations have also been installed: OpenBLAS and BLIS. If you try them then please let us know if they work better than MKL for your application.  BLIS is expected to perform well as a BLAS alternative but not match MKL's LAPACK performance.  </p>
<h2 id="01GAG6XAK2CBFM66VDVDG2BSDK"><span class="wysiwyg-font-size-large"><strong>Do I need to recompile my code?</strong></span></h2>
<p>Except for possible missing shared libraries (see above), you should not need to recompile your code. Please let us know if you encounter any issues not listed above.</p>
<h2 id="01GAG6XAK2DXD7EH0CWHCYRG22"><span class="wysiwyg-font-size-large"><strong>AOCC (<span>AMD Optimizing C/C++ and Fortran Compilers</span>)</strong></span></h2>
<p>AMD provides a compiler based on clang (C/C++) and flang (Fortran) which might perform better on their hardware.  We have installed it but not integrated it into a high-level toolchain with MPI and BLAS.  If you wish to try it:</p>
<pre><code>module load <span class="s1">AOCC</span></code></pre>
<p>For more information on AOCC compiler suite please, visit <a href="https://developer.amd.com/amd-aocc/" target="_blank" rel="noopener">AMD Optimizing C/C++ and Fortran Compilers (AOCC)</a></p>
<h2 id="01GAG6XAK2M6MMYE9057FTW7A4"><span class="wysiwyg-font-size-large"><strong>Network</strong></span></h2>
<p>Access to the new nodes is currently only possible via the Slurm <code>sbatch</code> and <code>srun</code> commands. There is no ssh access, not even to the nodes where you have a job running.  Programs that launch their remote tasks via ssh (eg: ORCA) are not expected to work.  Other arbitrary connections to the new compute nodes such as might be used by debuggers, HTTP based progress monitoring, and non-MPI distributed programs such as Dask or PEST, will generally only work if you use the InfiniBand address of the compute node, eg: <em>wmc012.ib.hpcf.nesi.org.nz</em>. Networking configuration is expected to be addressed in the future.<br><br><span class="wysiwyg-font-size-large"></span></p>
<p><span class="wysiwyg-font-size-large"></span><strong><span class="wysiwyg-font-size-x-large">Job<br></span><span class="wysiwyg-font-size-x-large"></span></strong><span class="wysiwyg-font-size-x-large"></span></p>
<p>In order to use the Mahuika Extension nodes, jobs are submitted in the same way as currently from the Mahuika login node with the following options.</p>
<p>Either:</p>
<ul>
<li>Add <code>#SBATCH --partition=milan</code> to the Slurm script</li>
<li>or with <code style="font-size: 15px;">sbatch -p milan MY_JOB_SCRIPT.sl</code>
</li>
</ul>
<p>Example of Slurm script:</p>
<pre>#!/bin/bash -e<br>#SBATCH --job-name=MilanJob       #Name of the job<br>#SBATCH --time=00:00:01           #Set a limit of 1 seconde on the total run time of the job allocation<br>#SBATCH --partition=milan         #Request the Milan partition for the resource allocation<br><br>srun pwd                          #Prints the working directory with the srun command</pre>
<p>Resource allocation limits:   </p>
<ul>
<li>7 days maximum walltime per job.</li>
<li>10 nodes per user at one time. eg 1x 10 nodes, or 2x 5 nodes </li>
<li>Please contact <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000748496-User-support" target="_self">NeSI support</a> if you require additional resources for jobs that are best suited to the Mahuika Extension.</li>
</ul>
<h1 id="01GAG6XAK3WY7N03E9SGCXN90B"><strong><span class="wysiwyg-font-size-x-large">Notes</span><span class="wysiwyg-font-size-large"><br></span></strong></h1>
<ul>
<li>
<strong>More node</strong>s will be added in the future.</li>
<li>Mahuika Extension is not a Cray system and the CPE differs from that on Mahuika and Maui. </li>
</ul>