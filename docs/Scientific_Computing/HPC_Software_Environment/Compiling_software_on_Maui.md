---
created_at: '2018-07-16T23:39:19Z'
position: 18
tags: []
title: "Compiling software on M\u0101ui"
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000336076
zendesk_section_id: 360000040056
---

[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! warning
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<div class="post-content">
<p>Building Fortran, C, or C++ code on the XC50 platform requires using the Cray programming environment. From a user perspective, the programming environment consists of a set of environment modules that select a compiler, essential libraries such as the MPI library, a CPU target, and more. The build process on the XC50 thus differs slightly from a standard Linux system. Non-compiled code, such as Python or R programs, do not use the programming environment. Note, however, that loading a module provided by NeSI/NIWA to get access to, e.g., the “RegCM” code, may change the Cray programming environment in that Cray environment modules may be swapped.</p>
<p><strong>Important:</strong></p>
<ul>
<li>It is essential to use a Programming Environment (PrgEnv-cray, PrgEnv-intel or PrgEnv-gnu) when you build code, otherwise it is very likely that problems at build time or run time appear</li>
<li>
<strong>Never</strong> use <code class="highlighter-rouge">module purge</code> on the XC50 platform, this will render the programming environment unusable, and you will have to log out and log back in</li>
<li>Code that was built on the XC50 platform is unlikely to run on Māui’s CS500 platform or on Mahuika’s CS400 platform; please rebuild your code when you change platform</li>
</ul>
<h2 id="the-build-node">The build node</h2>
<p>Māui has a dedicated build node, <code class="highlighter-rouge">login.maui.nesi.org.nz</code>, which should be used for building code. Please do not build code on the compute nodes by submitting a build job through SLURM:</p>
<ul>
<li>The compute nodes only run a thin operating system with very few command line utilities, it is thus likely that your build will fail</li>
<li>The file system on XC50 compute nodes is optimised for handling large block IO, small block IO that is typical for a build job is inefficient</li>
<li>Submitting a job will allocate entire nodes. This is a waste of compute resources, especially if only one core or a few cores are used</li>
</ul>
<p>Furthermore, please keep in mind that the build node is a shared resource. Instead of using as many parallel build processes as possible (with <code class="highlighter-rouge">make -j</code>), please limit the amount of processes (<code class="highlighter-rouge">make -j 5</code> for example).</p>
<h2 id="choosing-a-programming-environment">Choosing a programming environment</h2>
<p>The following Programming Environments are provided on Māui, named after the underlying compiler suite:</p>
<ol>
<li><code class="highlighter-rouge">PrgEnv-cray</code></li>
<li><code class="highlighter-rouge">PrgEnv-intel</code></li>
<li><code class="highlighter-rouge">PrgEnv-gnu</code></li>
</ol>
<p>The <code class="highlighter-rouge">PrgEnv-cray</code> environment is the default. If you want to change programming environment to use the Intel or GNU compilers, run</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs ruby"><span class="hljs-class"><span class="hljs-keyword">module</span> <span class="hljs-title">swap</span> <span class="hljs-title">PrgEnv</span>-<span class="hljs-title">cray</span> <span class="hljs-title">PrgEnv</span>-<span class="hljs-title">intel</span></span>
</code></pre>
</div>
</div>
<p>or</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs ruby"><span class="hljs-class"><span class="hljs-keyword">module</span> <span class="hljs-title">swap</span> <span class="hljs-title">PrgEnv</span>-<span class="hljs-title">cray</span> <span class="hljs-title">PrgEnv</span>-<span class="hljs-title">gnu</span></span>
</code></pre>
</div>
</div>
<p>Note that several compiler versions are currently installed, in case of GNU for example:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs javascript">&gt; <span class="hljs-built_in">module</span> avail gcc
-------------------------------------- <span class="hljs-regexp">/opt/m</span>odulefiles --------------------------------------
gcc/<span class="hljs-number">10.3</span><span class="hljs-number">.0</span> gcc/<span class="hljs-number">11.2</span><span class="hljs-number">.0</span> gcc/<span class="hljs-number">12.1</span><span class="hljs-number">.0</span>(<span class="hljs-keyword">default</span>)
</code></pre>
</div>
</div>
<p>To change GCC version, run for example</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs ruby"><span class="hljs-class"><span class="hljs-keyword">module</span> <span class="hljs-title">swap</span> <span class="hljs-title">gcc</span> <span class="hljs-title">gcc</span>/11.2.0</span>
</code></pre>
</div>
</div>
<p>GCC v6.1.0 or later is required to build code that can make use of the Intel Skylake microarchitecture and its advanced capabilities, such as AVX-512, on the XC50 platform.</p>
<p>Note: There is not <strong>the</strong> best compiler. Depending on your application/algorithms, different compilers can optimise the code better. Keep in mind trying different compilers.</p>
<h2 id="targetting-a-cpu">Targeting a CPU</h2>
<p>Compiling a program translates source code into machine instructions. It is important to let the compiler know for which CPU (“target”) the executable shall be build, to make best use of that CPU’s capabilities. Māui uses Intel Skylake microprocessors on all XC50 build and compute nodes, which come with AVX-512 vector instructions, enabling better performance for some codes.</p>
<p>CPU targets can be set by loading a module. By default, module <code class="highlighter-rouge">craype-x86-skylake</code> is loaded. In the rare case that you encounter problems with the Skylake target at build time or run time, try target for “Broadwell” processors instead:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs ruby"><span class="hljs-class"><span class="hljs-keyword">module</span> <span class="hljs-title">swap</span> <span class="hljs-title">craype</span>-<span class="hljs-title">x86</span>-<span class="hljs-title">skylake</span> <span class="hljs-title">craype</span>-<span class="hljs-title">broadwell</span></span>
</code></pre>
</div>
</div>
<p>Choosing the “Broadwell” target is also necessary if you want to build code using the older GCC compilers prior to GCC 6.1.0, which were released before Skylake became available. If you see the error message</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs coffeescript">craype-x86-skylake requires cce/<span class="hljs-number">8.6</span> <span class="hljs-keyword">or</span> later, intel/<span class="hljs-number">15.1</span> <span class="hljs-keyword">or</span> later, <span class="hljs-keyword">or</span> gcc/<span class="hljs-number">6.1</span> <span class="hljs-keyword">or</span> later
</code></pre>
</div>
</div>
<p>when trying to swap to the <code class="highlighter-rouge">PrgEnv-gnu</code> environment, or an error message of the kind</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs cs">f951: error: <span class="hljs-function">bad <span class="hljs-title">value</span> (<span class="hljs-params">skylake-avx512</span>) <span class="hljs-keyword">for</span> -march</span>= <span class="hljs-keyword">switch</span>
</code></pre>
</div>
</div>
<p>when you compile a program with a GNU compiler, run</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs ruby"><span class="hljs-class"><span class="hljs-keyword">module</span> <span class="hljs-title">swap</span> <span class="hljs-title">craype</span>-<span class="hljs-title">x86</span>-<span class="hljs-title">skylake</span> <span class="hljs-title">craype</span>-<span class="hljs-title">broadwell</span></span>
</code></pre>
</div>
</div>
<p>and try again.</p>
<p>Make sure that a target is always set. If you do not set a target, the compilers will produce generic code that runs on many processors of the “x86-64” family, and the program will thus not be able to benefit from capabilities such as AVX-512. You will see the following warning message when you run a compiler:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs sql">No supported cpu target is <span class="hljs-keyword">set</span>, CRAY_CPU_TARGET=x86<span class="hljs-number">-64</span> will be used.
<span class="hljs-keyword">Load</span> a valid targeting <span class="hljs-keyword">module</span> <span class="hljs-keyword">or</span> <span class="hljs-keyword">set</span> CRAY_CPU_TARGET
</code></pre>
</div>
</div>
<h2 id="using-the-compiler-drivers">Using the compiler drivers</h2>
<p>The programming environment provides compiler drivers for compiling Fortran, C, and C++ code. This means that you will need to use the following commands instead of the actual compilers:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs nginx"><span class="hljs-attribute">ftn</span> -o simpleMpi simpleMpi.f90 <span class="hljs-comment"># compile Fortran code</span>
cc  -o simpleMpi simpleMpi.c    <span class="hljs-comment"># compile C code</span>
CC  -o simpleMpi simpleMpi.cxx  <span class="hljs-comment"># compile C++ code</span>
</code></pre>
</div>
</div>
<p>The drivers will ensure correct linking of your code with compiler runtime libraries, and with Cray-supported libraries (such as Cray’s “libsci” scientific library, or Cray’s version of netCDF). It is therefore not recommended to use the compilers directly, there is a good chance that the executable will fail to build or run correctly.</p>
<p>The compiler drivers automatically add necessary compile and link flags to the compile/link line for the selected hardware and Cray-supported libraries. If you are interested in seeing what the compiler driver does, add the <code class="highlighter-rouge">-craype-verbose</code> flag:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs css"><span class="hljs-selector-tag">ftn</span> <span class="hljs-selector-tag">-craype-verbose</span> <span class="hljs-selector-tag">-o</span> <span class="hljs-selector-tag">simpleMpi</span> <span class="hljs-selector-tag">simpleMpi</span><span class="hljs-selector-class">.f90</span>
</code></pre>
</div>
</div>
<p>Further compiler driver options can be found on their man pages:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs nginx"><span class="hljs-attribute">man</span> ftn
man cc
man CC</code></pre>
</div>
</div>
<h2 id="compiling_and_running_mpi_code"><strong>Compiling and Running MPI code</strong></h2>
<p>The compiler drivers will also automatically build MPI codes correctly, there is no need to use special compilers or add additional compiler or linker flags.</p>
<p>Note that running an MPI code on the build node (<code class="highlighter-rouge">login.maui.nesi.org.nz</code>) using</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs">./simpleMPI
</code></pre>
</div>
</div>
<p>will fail with an error message, as there is no MPI runtime environment:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs objectivec">[Wed Oct <span class="hljs-number">18</span> <span class="hljs-number">02</span>:<span class="hljs-number">00</span>:<span class="hljs-number">14</span> <span class="hljs-number">2017</span>] [c0<span class="hljs-number">-0</span>c0s3n1] Fatal error <span class="hljs-keyword">in</span> <span class="hljs-built_in">MPI_Init</span>: Other <span class="hljs-built_in">MPI</span> error, error stack:
<span class="hljs-built_in">MPIR_Init_thread</span>(<span class="hljs-number">537</span>):
<span class="hljs-built_in">MPID_Init</span>(<span class="hljs-number">247</span>).......: channel initialization failed
<span class="hljs-built_in">MPID_Init</span>(<span class="hljs-number">636</span>).......:  PMI2 init failed: <span class="hljs-number">1</span>
</code></pre>
</div>
</div>
<p>If you want to run a short test of your build, use SLURM’s srun command that submits your program to a compute node on the fly, e.g.,</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs ini"><span class="hljs-attr">SLURM_PARTITION</span>=nesi_research srun -n <span class="hljs-number">6</span> simpleMPI
</code></pre>
</div>
</div>
<h2 id="common-compiler-options">Common compiler options</h2>
<p>Although the compiler drivers <code class="highlighter-rouge">ftn</code>, <code class="highlighter-rouge">cc</code> and <code class="highlighter-rouge">CC</code> have a few options of their own, such as the <code class="highlighter-rouge">-craype-verbose</code> flag, they will pass through any additional compiler options to the underlying compiler. This means that you will still need to choose compiler flags that are specific to the Cray, Intel, or GNU compilers, and you will need to change them if you decide to switch compilers.</p>
<p>For example, if you wanted to use the gfortran compiler, activate compiler warnings (<code class="highlighter-rouge">-Wall</code>), and require aggressive compiler optimisation (<code class="highlighter-rouge">-O3</code>), you would use the following commands:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code class="hljs ruby"><span class="hljs-class"><span class="hljs-keyword">module</span> <span class="hljs-title">swap</span> <span class="hljs-title">PrgEnv</span>-<span class="hljs-title">cray</span> <span class="hljs-title">PrgEnv</span>-<span class="hljs-title">gnu</span></span>
ftn -Wall -O3 -o simpleMpi simpleMpi.f9<span class="hljs-number">0</span>
</code></pre>
</div>
</div>
<p>The following table provides a list of commonly used compiler options:</p>
<table>
<thead>
<tr>
<th>Group</th>
<th>Cray</th>
<th>Intel</th>
<th>GNU</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Debugging</td>
<td>
<code class="highlighter-rouge">-g</code> or <code class="highlighter-rouge">-G{0,1,2,fast}</code>
</td>
<td>
<code class="highlighter-rouge">-g</code> or <code class="highlighter-rouge">-debug [keyword]</code>
</td>
<td><code class="highlighter-rouge">-g or -g{0,1,2,3}</code></td>
<td>Set level of debugging information, some levels may disable certain compiler optimisations</td>
</tr>
<tr>
<td>Light compiler optimisation</td>
<td><code class="highlighter-rouge">-O2</code></td>
<td><code class="highlighter-rouge">-O2</code></td>
<td><code class="highlighter-rouge">-O2</code></td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Aggressive compiler optimisation</td>
<td><code class="highlighter-rouge">-O3 -hfp3</code></td>
<td><code class="highlighter-rouge">-O3 -ipo</code></td>
<td><code class="highlighter-rouge">-O3 -ffast-math -funroll-loops</code></td>
<td>This may affect numerical accuracy</td>
</tr>
<tr>
<td>Vectorisation reports</td>
<td><code class="highlighter-rouge">-hlist=m</code></td>
<td><code class="highlighter-rouge">-qopt-report</code></td>
<td>
<code class="highlighter-rouge">-fopt-info-vec</code> or <code class="highlighter-rouge">-fopt-info-missed</code>
</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>OpenMP</td>
<td>
<code class="highlighter-rouge">-homp</code> (default)</td>
<td><code class="highlighter-rouge">-openmp</code></td>
<td><code class="highlighter-rouge">-fopenmp</code></td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
<p>Additional compiler options are documented on the compiler man pages, which are accessible <em>after</em> loading the corresponding programming environment:</p>
<table>
<thead>
<tr>
<th>language</th>
<th>cray</th>
<th>intel</th>
<th>gnu</th>
</tr>
</thead>
<tbody>
<tr>
<td>Fortran</td>
<td>man crayftn</td>
<td>man ifort</td>
<td>man gfortran</td>
</tr>
<tr>
<td>C</td>
<td>man craycc</td>
<td>man icc</td>
<td>man gcc</td>
</tr>
<tr>
<td>C++</td>
<td>man crayCC</td>
<td>man icpc</td>
<td>man g++</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2 id="building_code_that_depends_on_external_libraries_">Building Code that Depends on External Libraries&nbsp;</h2>
<p>While linking external libraries, one need to pay attention to the correct compiler and linker setup. This, depends on the correct library version (working properly with the compiler and the link type) and the used link options. These depend on whether the libraries have been provided by Cray, by NeSI/NIWA, or if you built them yourself.</p>
</div>

