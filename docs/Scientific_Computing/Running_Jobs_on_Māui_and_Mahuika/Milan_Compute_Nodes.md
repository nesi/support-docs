---
created_at: '2023-02-09T01:30:43Z'
hidden: false
label_names: []
position: 10
title: Milan Compute Nodes
vote_count: 0
vote_sum: 0
zendesk_article_id: 6367209795471
zendesk_section_id: 360000030876
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p> </p>
<h1>How to access</h1>
<p>To use Mahuika's Milan nodes, you will need to explicitly specify the <code>milan</code> partition in your <code>sbatch</code> command line. Jobs are submitted from the same Mahuika login node that you currently use, and share the same file system as other cluster nodes. </p>
<pre>sbatch -p milan ...</pre>
<p>Alternatively, the same effect can be achieved by placing a pragma into the job description file:</p>
<pre>#SBATCH --partition=milan</pre>
<h1>Hardware</h1>
<p>Each node has two AMD Milan CPUs, each with 8 "chiplets" of 8 cores and one level 3 cache, so each node has a total of <strong>128 cores</strong> or 256 hyperthreaded CPUs. This represents a significant increase of the number CPUs per node compared to the Broadwell nodes (36 cores). </p>
<p><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">The memory available to Slurm jobs is 512GB per node, so approximately 2GB per CPU. </span>There are 64 nodes available, 8 of which will have double the memory (1T).</p>
<h1>Software</h1>
<h2>Operating System</h2>
<p>The existing Mahuika compute nodes use Linux Centos 7.4 while the new ones use Rocky 8.5.  These are closely related Linux distributions. The move from 7 to 8 is more significant than the move from Centos to Rocky.</p>
<p>Many system libraries have changed version numbers between versions 7 and 8, so <strong>some software compiled on Centos 7 will not run as-is on Rocky 8</strong>. This can result in the runtime error <code>error while loading shared libraries:... cannot open shared object file</code>,  which can be fixed by providing a copy of the old system library.  </p>
<p>We have repaired several of our existing environment modules that way. For programs which you have compiled yourself, we have installed a new environment module that provides many of the Centos 7 libraries:</p>
<pre>module load LegacySystemLibs/7</pre>
<p>Please <a href="https://support.nesi.org.nz/hc/en-gb/requests/new" target="_blank" rel="noopener">let us know</a> if that isn't sufficient to get your existing compiled code running on the new nodes.</p>
<p>Of course you can also recompile code inside a job run in the Milan partition and so produce an executable linked against the new system libraries, but then that would be unlikely to work on the old nodes.</p>
<p>In the longer term, all Mahuika nodes will be upgraded to Rocky 8.</p>
<h2>Older Intel and Cray software</h2>
<p>The directories <code>/cm</code> and <code>/opt/cray</code> contain software which was installed on Mahuika's Broadwell nodes when we purchased it rather than installed by the NeSI Application Support team. They are not present on the Milan nodes. As with the system libraries, you could take a copy of these libraries and carry on, but it is best to migrate away from using them if possible.</p>
<p>This affects our pre-2020 toolchains such as<em> intel/2018b</em>, but we should have newer versions of such software already installed in most cases.</p>
<h2>Intel MKL performance</h2>
<p>In many ways, Intel's MKL is the best implementation of the BLAS and LAPACK libraries to which we have access, which is why we use it in our "<em>intel</em>" and "<em>gimkl</em>" toolchains.  Unfortunately, recent versions of MKL deliberately choose not to use the accelerated AVX instructions when not running on an Intel CPU.  </p>
<p>In order to persuade MKL to use the same fast optimised kernels on the new AMD Milan CPUs, you can do:</p>
<pre>module load AlwaysIntelMKL</pre>
<p>We have set that as the default for our most recent toolchain <em>gimkl/2022a</em>.</p>
<p>Two alternative implementations have also been installed: OpenBLAS and BLIS. If you try them then please let us know if they work better than MKL for your application. BLIS is expected to perform well as a BLAS alternative but not match MKL's LAPACK performance.  </p>
<h2>Do I need to recompile my code?</h2>
<p>Except for possible missing shared libraries (see above), you should not need to recompile your code. Please <a href="https://support.nesi.org.nz/hc/en-gb/requests/new" target="_blank" rel="noopener">let us know</a> if you encounter any issues not listed above.</p>
<h2>AOCC compiler suite</h2>
<p>AMD provides a compiler based on clang (C/C++) and flang (Fortran) which might perform better on their hardware. We have installed it but not integrated it into a high-level toolchain with MPI and BLAS. If you wish to try it:</p>
<pre><code>module load <span class="s1">AOCC</span></code></pre>
<p>For more information on AOCC compiler suite please, visit <a href="https://developer.amd.com/amd-aocc/" target="_blank" rel="noopener">AMD Optimizing C/C++ and Fortran Compilers (AOCC)</a></p>
<h1>Network</h1>
<p>Access to Mahuika's Milan nodes is currently only possible via the Slurm <code>sbatch</code> and <code>srun</code> commands. There is no ssh access, not even to the nodes where you have a job running. Programs that launch their remote tasks via ssh (eg: ORCA) are not expected to work. Other arbitrary connections to the new compute nodes such as might be used by debuggers, HTTP based progress monitoring, and non-MPI distributed programs such as Dask or PEST, will generally only work if you use the Infiniband address of the compute node, eg: <em>wmc012.ib.hpcf.nesi.org.nz</em>. This networking configuration is expected to be addressed in the future.</p>
<h1>Any questions?</h1>
<p>Don't hesitate to contact us at <a href="mailto:support@nesi.org.nz">support@nesi.org.nz</a>. No question is too big or small. We are available for Zoom sessions or <a href="https://support.nesi.org.nz/hc/en-gb/articles/4830713922063" target="_self">Weekly Online Office Hours</a> if it's easier to discuss your question in a call rather than via email.</p>