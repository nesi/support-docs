---
created_at: '2018-07-16T23:39:19Z'
hidden: false
label_names: []
position: 18
title: "Compiling software on M\u0101ui"
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000336076
zendesk_section_id: 360000040056
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<header class="site-header">
<div class="wrapper"><nav class="site-nav">
<h1 class="trigger"><span style="font-size: 1.2em; font-weight: 600;">Building on the <span>XC50 Platform</span></span></h1>
</nav></div>
</header>
<div class="wrapper">
<article class="post">
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
<pre class="highlight"><code>module swap PrgEnv-cray PrgEnv-intel
</code></pre>
</div>
</div>
<p>or</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module swap PrgEnv-cray PrgEnv-gnu
</code></pre>
</div>
</div>
<p>Note that several compiler versions are currently installed, in case of GNU for example:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>&gt; module avail gcc
-------------------------------------- /opt/modulefiles --------------------------------------
gcc/10.3.0 gcc/11.2.0 gcc/12.1.0(default)
</code></pre>
</div>
</div>
<p>To change GCC version, run for example</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module swap gcc gcc/11.2.0
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
<pre class="highlight"><code>module swap craype-x86-skylake craype-broadwell
</code></pre>
</div>
</div>
<p>Choosing the “Broadwell” target is also necessary if you want to build code using the older GCC compilers prior to GCC 6.1.0, which were released before Skylake became available. If you see the error message</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>craype-x86-skylake requires cce/8.6 or later, intel/15.1 or later, or gcc/6.1 or later
</code></pre>
</div>
</div>
<p>when trying to swap to the <code class="highlighter-rouge">PrgEnv-gnu</code> environment, or an error message of the kind</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>f951: error: bad value (skylake-avx512) for -march= switch
</code></pre>
</div>
</div>
<p>when you compile a program with a GNU compiler, run</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module swap craype-x86-skylake craype-broadwell
</code></pre>
</div>
</div>
<p>and try again.</p>
<p>Make sure that a target is always set. If you do not set a target, the compilers will produce generic code that runs on many processors of the “x86-64” family, and the program will thus not be able to benefit from capabilities such as AVX-512. You will see the following warning message when you run a compiler:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>No supported cpu target is set, CRAY_CPU_TARGET=x86-64 will be used.
Load a valid targeting module or set CRAY_CPU_TARGET
</code></pre>
</div>
</div>
<h2 id="using-the-compiler-drivers">Using the compiler drivers</h2>
<p>The programming environment provides compiler drivers for compiling Fortran, C, and C++ code. This means that you will need to use the following commands instead of the actual compilers:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>ftn -o simpleMpi simpleMpi.f90 # compile Fortran code
cc  -o simpleMpi simpleMpi.c    # compile C code
CC  -o simpleMpi simpleMpi.cxx  # compile C++ code
</code></pre>
</div>
</div>
<p>The drivers will ensure correct linking of your code with compiler runtime libraries, and with Cray-supported libraries (such as Cray’s “libsci” scientific library, or Cray’s version of netCDF). It is therefore not recommended to use the compilers directly, there is a good chance that the executable will fail to build or run correctly.</p>
<p>The compiler drivers automatically add necessary compile and link flags to the compile/link line for the selected hardware and Cray-supported libraries. If you are interested in seeing what the compiler driver does, add the <code class="highlighter-rouge">-craype-verbose</code> flag:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>ftn -craype-verbose -o simpleMpi simpleMpi.f90
</code></pre>
</div>
</div>
<p>Further compiler driver options can be found on their man pages:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>man ftn
man cc
man CC</code></pre>
</div>
</div>
<h2><strong>Compiling and Running MPI code</strong></h2>
<p>The compiler drivers will also automatically build MPI codes correctly, there is no need to use special compilers or add additional compiler or linker flags.</p>
<p>Note that running an MPI code on the build node (<code class="highlighter-rouge">login.maui.nesi.org.nz</code>) using</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>./simpleMPI
</code></pre>
</div>
</div>
<p>will fail with an error message, as there is no MPI runtime environment:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>[Wed Oct 18 02:00:14 2017] [c0-0c0s3n1] Fatal error in MPI_Init: Other MPI error, error stack:
MPIR_Init_thread(537):
MPID_Init(247).......: channel initialization failed
MPID_Init(636).......:  PMI2 init failed: 1
</code></pre>
</div>
</div>
<p>If you want to run a short test of your build, use SLURM’s srun command that submits your program to a compute node on the fly, e.g.,</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>SLURM_PARTITION=nesi_research srun -n 6 simpleMPI
</code></pre>
</div>
</div>
<h2 id="common-compiler-options">Common compiler options</h2>
<p>Although the compiler drivers <code class="highlighter-rouge">ftn</code>, <code class="highlighter-rouge">cc</code> and <code class="highlighter-rouge">CC</code> have a few options of their own, such as the <code class="highlighter-rouge">-craype-verbose</code> flag, they will pass through any additional compiler options to the underlying compiler. This means that you will still need to choose compiler flags that are specific to the Cray, Intel, or GNU compilers, and you will need to change them if you decide to switch compilers.</p>
<p>For example, if you wanted to use the gfortran compiler, activate compiler warnings (<code class="highlighter-rouge">-Wall</code>), and require aggressive compiler optimisation (<code class="highlighter-rouge">-O3</code>), you would use the following commands:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module swap PrgEnv-cray PrgEnv-gnu
ftn -Wall -O3 -o simpleMpi simpleMpi.f90
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
<td> </td>
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
<td> </td>
</tr>
<tr>
<td>OpenMP</td>
<td>
<code class="highlighter-rouge">-homp</code> (default)</td>
<td><code class="highlighter-rouge">-openmp</code></td>
<td><code class="highlighter-rouge">-fopenmp</code></td>
<td> </td>
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
<p> </p>
<h2>Building Code that Depends on External Libraries </h2>
<p>While linking external libraries, one need to pay attention to the correct compiler and linker setup. This, depends on the correct library version (working properly with the compiler and the link type) and the used link options. These depend on whether the libraries have been provided by Cray, by NeSI/NIWA, or if you built them yourself.</p>
</div>
<div class="post-content">
<p>Many libraries are provided in modules. You can search them using</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module avail
</code></pre>
</div>
</div>
<p>and look in the module description using:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module help &lt;module-name&gt;
</code></pre>
</div>
</div>
<p>Sometimes modules provide multiple libraries, e.g. <em>cray-libsci</em>.</p>
<h2 id="using-libraries-provided-by-cray">Using libraries provided by Cray</h2>
<p>If a library has been provided by Cray, the compiler drivers will automatically take care of adding search paths for include files and libraries, and they will add the library names to the linker line. For example, to build a program that uses the netCDF library provided by the <code class="highlighter-rouge">cray-netcdf</code> module, run the commands</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module load cray-netcdf
ftn -o simple_xy_wr simple_xy_wr.f90
</code></pre>
</div>
</div>
<p>Keep in mind that such automatic treatment of dependencies will <strong>only</strong> work if the libraries have been provided by Cray - you can recognise those by their module name, which always starts with <code class="highlighter-rouge">cray-</code>, e.g., <code class="highlighter-rouge">cray-netcdf</code>, or <code class="highlighter-rouge">cray-libsci</code>.</p>
<p>Note also that correct versions of the libraries (Cray CCE, Intel, or GNU builds) will automatically be used after swapping programming environment. This is particularly important for libraries that provide Fortran 90 modules, due to their compiler-specific format.</p>
<h2 id="using-libraries-provided-by-nesiniwa">Using libraries provided by NeSI/NIWA</h2>
<p>The situation is different when you use a library that is provided by NeSI/NIWA. They can be recognised by the <code class="highlighter-rouge">CrayCCE</code>, <code class="highlighter-rouge">CrayIntel</code>, or <code class="highlighter-rouge">CrayGNU</code> suffix attached to their version number. In this case, you will have to provide search paths using the <code class="highlighter-rouge">-I</code> flag for include files, and <code class="highlighter-rouge">-L</code> for library files, and the library names have to be explicitly added to the linker line. Libraries are not always provided for all compiler suites and versions.</p>
<p>Note that library names are specified in a specifically formatted form, <code class="highlighter-rouge">-l&lt;library name&gt;</code>. The linker then expects to find a library file named <code class="highlighter-rouge">lib&lt;library name&gt;.a</code> (for a static library) or <code class="highlighter-rouge">lib&lt;library name&gt;.so</code> (for a shared library), e.g., <code class="highlighter-rouge">libnetcdf.a</code>. Note that you may need to list several libraries to link successfully, e.g., <code class="highlighter-rouge">-lA -lB</code> for linking against libraries “A” and “B”. The order in which you list libraries matters, as the linker will go through the list in order of appearance. If library “A” depends on library “B”, specifying <code class="highlighter-rouge">-lA -lB</code> will work. If library “B” depends on “A”, use <code class="highlighter-rouge">-lB -lA</code>. If they depend on each other, use <code class="highlighter-rouge">-lA -lB -lA</code> (although such cases are quite rare).</p>
<p>Consider the following example where the <code class="highlighter-rouge">grib_api</code> library is used:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module load grib_api/1.23.1-CrayGNU-18.08
cc -I$EBROOTGRIB_API/include -o mygribprogram mygribprogram.c -L$EBROOTGRIB_API/lib -lgrib_api
</code></pre>
</div>
</div>
<p>The EasyBuild software management system that NeSI/NIWA use to provide modules automatically defines environment variables <code class="highlighter-rouge">$EBROOT&lt;library name in upper case&gt;</code> when a module is loaded, which help pointing the compiler and linker to include files and libraries as in the example above. If you are unsure which <code class="highlighter-rouge">$EBROOT&lt;...&gt;</code> variables are available, use</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module show grib_api/1.23.1-CrayGNU-18.08
</code></pre>
</div>
</div>
<p>to find out.</p>
<p>Note that specifying search paths with <code class="highlighter-rouge">-I</code> and <code class="highlighter-rouge">-L</code> is not strictly necessary in case of the GNU and Intel compilers, which will use the contents of <code class="highlighter-rouge">CPATH</code>, <code class="highlighter-rouge">LIRARY_PATH</code>, and <code class="highlighter-rouge">LD_LIBRARY_PATH</code> provided by the NeSI/NIWA module. This will not work with the Cray compiler.</p>
<p><strong>Important note:</strong> Make sure that you load the correct variant ofXC50 a library, depending on your choice of compiler. Switching compiler environment will <em>not</em> switch NeSI/NIWA modules automatically. Furthermore, loading a NeSI/NIWA module may switch programming environment if it was built with a different compiler.</p>
<p>As mentioned earlier, EasyBuild uses the following module naming conventions (“toolchain names”) to identify the programming environment that was used to build the software:</p>
<ul>
<li>
<code class="highlighter-rouge">CrayCCE</code> for libraries and tools built with the Cray compilers (<code class="highlighter-rouge">PrgEnv-cray</code>)</li>
<li>
<code class="highlighter-rouge">CrayIntel</code> for libraries and tools built with the Intel compilers (<code class="highlighter-rouge">PrgEnv-intel</code>)</li>
<li>
<code class="highlighter-rouge">CrayGNU</code> for libraries and tools built with the GNU compilers (<code class="highlighter-rouge">PrgEnv-gnu</code>)</li>
</ul>
<h2 id="using-your-own-libraries">Using your own libraries</h2>
<p>Linking against libraries that you built yourself is the same as linking against libraries provided by NeSI/NIWA - you will just need to point the compiler to the location where the include and library files are using the <code class="highlighter-rouge">-I</code> and <code class="highlighter-rouge">-L</code> flags.</p>
<h2 id="static-and-dynamic-linking">Static and dynamic linking</h2>
<p>The XC50 compilers drivers default to static linking where possible for maximum efficiency, avoiding the need to load shared libraries for hundreds or thousands of MPI ranks at runtime. If all dependencies are available as static libraries, the resulting executables will be completely self-contained (although they may still need the Cray MPI environment at runtime).</p>
<p>Here is an example that shows how to find out how your code was linked:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module load GSL/2.4-CrayGNU-2017.06
cc -I$EBROOTGRIB_API/include -o mygribprogram mygribprogram.c -L$EBROOTGRIB_API/lib -lgrib_api
ldd mygribprogram
</code></pre>
</div>
</div>
<p>If you see the message <code class="highlighter-rouge">not a dynamic executable</code>, your program was statically linked. Otherwise you will see a list of shared library dependencies that are needed at runtime.</p>
<p>If you have to link your code dynamically, either set</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>export CRAYPE_LINK_TYPE=dynamic
</code></pre>
</div>
</div>
<p>in your build environment (useful when using complex build systems), or add the <code class="highlighter-rouge">-dynamic</code> flag to the compiler driver commands, e.g.,</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>cc -I$EBROOTGRIB_API/include -o mygribprogram mygribprogram.c -L$EBROOTGRIB_API/lib -lgrib_api -dynamic
</code></pre>
</div>
</div>
<p>Using the <code class="highlighter-rouge">ldd</code> tool, you should now see a number of libraries that are dynamically linked.</p>
<p>You may occassionally see a warning message of the kind:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>/opt/cray/pe/hdf5/1.10.1.1/INTEL/16.0/lib/libhdf5.a(H5PL.o): In function `H5PL_load':
H5PL.c:(.text+0x612): warning: Using 'dlopen' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking
</code></pre>
</div>
</div>
<p>This simply means that the library must be accessible at runtime despite fully static linking and the program is thus not entirely self-contained, which is usually not an issue.</p>
<h2 id="common-linker-problems">Common linker problems</h2>
<p>Linking can easily go wrong. Most often, you will see linker errors about “missing symbols” when the linker could not find a function used in your program or in one of the libraries that you linked against. To resolve this problem, have a closer look at the function names that the linker reported:</p>
<ul>
<li>Are you missing some object code files (these are compiled source files and have suffix <code class="highlighter-rouge">.o</code>) that should appear on the linker line? This can happen if the build system was not configured correctly or has a bug. Try running the linking step manually with all source files and debug the build system (which can be a lengthy and cumbersome process, unfortunately).</li>
<li>Do the missing functions have names that contain “mp” or “omp”? This could mean that some of your source files or external libraries were built with OpenMP support, which requires you to set an OpenMP flag (<code class="highlighter-rouge">-fopenmp</code> for GNU compilers, <code class="highlighter-rouge">-qopenmp</code> for Intel) in your linker command. For the Cray compilers, OpenMP is enabled by default and can be controlled using <code class="highlighter-rouge">-h[no]omp</code>.</li>
<li>Do you see a very long list of complex-looking function names, and does your source code or external library dependency include C++ code? You may need to explicitly link against the C++ standard library (<code class="highlighter-rouge">-lstdc++</code> for GNU and Cray compilers, <code class="highlighter-rouge">-cxxlib</code> for Intel compilers); this is a particularly common problem for statically linked code.</li>
<li>Do the function names end with an underscore (“_”)? You might be missing some Fortran code, either from your own sources or from a library that was written in Fortran, or parts of your Fortran code were built with flags such as <code class="highlighter-rouge">-assume nounderscore</code> (Intel) or <code class="highlighter-rouge">-fno-underscoring</code> (GNU), while others were using different flags (note that the Cray compiler always uses underscores).</li>
<li>Do the function names end with double underscores (“__”)? Fortran compilers offer an option to add double underscores to Fortran subroutine names for compatibility reasons (<code class="highlighter-rouge">-h [no]second_underscore</code>, <code class="highlighter-rouge">-assume [no]2underscores</code>, <code class="highlighter-rouge">-f[no-]second-underscore</code>) which you may have to add or remove.</li>
</ul>
<p>Note that the linker requires that function names match exactly, so any variation in function name in your code will lead to a “missing symbols” error (with the exception of character case in Fortran source code).</p>
<h1 id="building-code-on-the-cs500-platform">Building code on the CS500 platform</h1>
<p>Building code on the CS500 platform is different from the XC50 platform:</p>
<ul>
<li>The CS500 platform does not currently use compiler drivers (these will be made available by Cray in the near future)</li>
<li>The CS500 module environment can be reset using <code class="highlighter-rouge">module purge</code> without problems - you will need to run <code class="highlighter-rouge">module load NeSI</code> afterwards to make the NeSI software stack available again.</li>
</ul>
<p>Building code on the CS500 platform follows the same process as building code on Mahuika. The only difference is that CS500 nodes use Intel Skylake CPUs, while Mahuika’s CS400 nodes use the older Intel Broadwell CPUs. This means that programs that were compiled on the CS500 platform may fail to run on Mahuika, producing either an error message (if built with the Intel compiler), or an “illegal instruction” error (if built with the Cray or GNU compilers).</p>
<p>Please refer to section <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000329015">Building code on Mahuika</a> for further instructions.</p>
</div>
</article>
</div>