---
created_at: '2018-07-12T03:48:47Z'
hidden: false
label_names: []
position: 17
title: Compiling software on Mahuika
vote_count: 1
vote_sum: 1
zendesk_article_id: 360000329015
zendesk_section_id: 360000040056
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <h1 id="where-to-build">Where to build</h1>
<p>You may compile (build) software on the Mahuika login nodes, <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">login.mahuika.nesi.org.nz</code>. Please be aware that these login nodes are limited and shared resources. Please limit the amount of processes on these nodes. For example, use <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">make -j 5</code> instead of <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">make -j</code>. If you require many CPU cores or long run times for your build process, please request these resources through a batch job submitted to Slurm, where you can also ask for a larger amount of compute resources to build your code.</p>
<h1 id="compilers-and-toolchains">Compilers and Toolchains</h1>
<p>Compilers produced by three different vendors are provided on Mahuika: Cray, GNU and Intel.</p>
<p>The GNU and Intel compilers can be accessed by loading one of the toolchains:</p>
<ul>
<li>
<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">module load gimkl/2020a</code> - the default toolchain, providing GNU compilers (version 9.2.0), Intel MPI and Intel MKL</li>
<li>
<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">module load intel/2020a</code> - Intel compilers (version 2020.0.166), Intel MPI and Intel MKL</li>
</ul>
<p>A large number of dependencies are built against these toolchains, so they are usually a good place to start when building your own software. However, if for any reason you require a different version of one of these compilers, you can load a compiler module directly, instead of loading a toolchain. For example, the installed versions of the GNU compilers can be listed with the following command:</p>
<p><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">module spider GCC</code></p>
<p>and version 7.4.0 loaded with the following command:</p>
<p><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">module load GCC/7.4.0</code></p>
<p>The Cray compilers behave differently to the GNU and Intel compilers, since they are installed as a Cray Programming Environment, and have some special features (see section Cray Programming Environment). The Cray compilers are loaded with:</p>
<p><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">module load PrgEnv-cray</code></p>
<h1>Third party applications</h1>
<p>Installation instructions vary from application to application, and we suggest that you carefully read the instructions provided by the developers of the software you plan to use. Nevertheless, the following should give you an impression which steps you usually need to consider:</p>
<ol>
<li>Change into your desired source code directory. We suggest you use <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">/nesi/project/&lt;projectID&gt;</code>, or more typically one of its subdirectories. You may instead use <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">/nesi/nobackup/&lt;projectID&gt;</code> (or one of its subdirectories) if you don't mind the software not being backed up and prone to automatic deletion in certain circumstances.</li>
<li>Download the source code. This could be done via a repository checkout (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">git clone &lt;source-url&gt;</code>) or via downloading a tarball (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">wget &lt;source-url&gt;</code>).</li>
<li>Ensure the tarball is not a tarbomb, using <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">tar tf &lt;source.tar&gt; | sort | less</code> (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">tar tzf ...</code> if the source code is a gzipped tarball, <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">tar tjf ...</code> if a bzip2 compressed tarball). If you find that the tarball is in fact a tarbomb, you will need to handle it using special techniques.</li>
<li>Unpack the tarball using <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">tar xf &lt;source.tar&gt;</code>. Change into the source directory.</li>
<li>
<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;"></code>Load the preferred toolchain (or compiler module) and modules for any additional required libraries (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">module load gimkl FFTW</code>)</li>
<li>Run the configure script with appropriate options, e.g. <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">./configure --prefix=&lt;desired install directory&gt; --use-fftw=$EBROOTFFTW  </code>(options can usually be listed using <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">./configure --help</code>)</li>
<li>In some applications you need to adjust the <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">Makefile</code> (generated by <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">configure</code>) to reflect your preferred compiler, and library options (see below)</li>
<li>Compile the code (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">make</code><code>)</code>
</li>
<li>install the binaries and libraries into the specified directory (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">make install</code>)<code></code>
</li>
</ol>
<p> </p>
<h1 id="compilers">Compilers</h1>
<p>Compilers are provided for Fortran, C, and C++. For MPI-parallelised code, different compilers typically need to be used. The different <strong>compilers</strong> are listed:</p>
<table>
<colgroup> <col width="10%"> <col width="30%"> <col width="30%"> <col width="30%"> </colgroup>
<thead>
<tr>
<th>Language</th>
<th>Cray</th>
<th>Intel</th>
<th>GNU</th>
</tr>
</thead>
<tbody>
<tr>
<td>Fortran</td>
<td>ftn</td>
<td>ifort</td>
<td>gfortran</td>
</tr>
<tr>
<td>Fortran + MPI</td>
<td>ftn</td>
<td>mpiifort</td>
<td>mpif90</td>
</tr>
<tr>
<td>C</td>
<td>cc</td>
<td>icc</td>
<td>gcc</td>
</tr>
<tr>
<td>C + MPI</td>
<td>cc</td>
<td>mpiicc</td>
<td>mpicc</td>
</tr>
<tr>
<td>C++</td>
<td>CC</td>
<td>icpc</td>
<td>g++</td>
</tr>
<tr>
<td>C++ + MPI</td>
<td>CC</td>
<td>mpiicpc</td>
<td>mpicxx</td>
</tr>
</tbody>
</table>
<p><strong>Note</strong>, Cray uses compiler wrappers which are described <a href="#cray-programming-environment">later in more detail</a>.</p>
<p>In general you then compile your code using:</p>
<p><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">&lt;compiler&gt; &lt;CompilerOptions&gt; &lt;source-file&gt;</code></p>
<p>e.g.</p>
<p><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">ftn -O3 hello.f90</code></p>
<h1 id="compiler-options">
<br>Compiler options</h1>
<p>Compilers are controlled using different options to control optimizations, output, source and library handling. There options vary between the different compiler vendors. That means you will need to change them if you decide to switch compilers. The following table provides a list of commonly used compiler <strong>options</strong> for the different compilers:</p>
<table>
<colgroup> <col width="20%"> <col width="20%"> <col width="20%"> <col width="20%"> <col width="20%"> </colgroup>
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
<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-g</code> or <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-G{0,1,2,fast}</code>
</td>
<td>
<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-g</code> or <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-debug [keyword]</code>
</td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-g or -g{0,1,2,3}</code></td>
<td>Set level of debugging information, some levels may disable certain compiler optimisations</td>
</tr>
<tr>
<td>Light compiler optimisation</td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-O2</code></td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-O2</code></td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-O2</code></td>
<td> </td>
</tr>
<tr>
<td>Aggressive compiler optimisation</td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-O3 -hfp3</code></td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-O3 -ipo</code></td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-O3 -ffast-math -funroll-loops</code></td>
<td>This may affect numerical accuracy</td>
</tr>
<tr>
<td>Architecture specific optimisation</td>
<td>Load this module first: <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">module load craype-broadwell</code>
</td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-xHost</code></td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-march=native -mtune=native</code></td>
<td>Build and compute nodes have the same architecture (Broadwell)</td>
</tr>
<tr>
<td>Vectorisation reports</td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-hlist=m</code></td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-qopt-report</code></td>
<td>
<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-fopt-info-vec</code> or <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-fopt-info-missed</code>
</td>
<td> </td>
</tr>
<tr>
<td>OpenMP</td>
<td>
<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-homp</code> (default)</td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-qopenmp</code></td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-fopenmp</code></td>
<td><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;"></code></td>
</tr>
</tbody>
</table>
<p>Additional compiler options are documented in the compiler man pages, e.g. <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">man mpicc</code>, which are available <em>after</em> loading the related compiler module. Additional documentation can be also found at the vendor web pages:</p>
<ul>
<li>
<a href="https://pubs.cray.com/content/S-3901/8.7/cray-fortran-reference-manual/fortran-compiler-introduction">Cray Fortran v8.7</a>, <a href="https://pubs.cray.com/content/S-2179/8.7/cray-c-and-c++-reference-manual/invoke-the-c-and-c++-compilers">Cray C and C++ v8.7</a>
</li>
<li>
<a href="https://software.intel.com/en-us/node/685016">Intel Parallel Studio XE Cluster Edition</a> for Linux is installed on the Mahuika HPC Cluster, Mahuika Ancillary Nodes</li>
<li><a href="https://software.intel.com/en-us/documentation/view-all?search_api_views_fulltext=&amp;current_page=0&amp;value=78151,83039;20813,80605,79893,20812,20902;20816;20802;20804">Intel Developer Guides</a></li>
<li><a href="https://gcc.gnu.org/onlinedocs/">GCC Manuals</a></li>
</ul>
<p><strong>Note</strong>: Cray uses compiler wrappers. To list the compiler options, please consult the man pages for the actual compiler, not the wrapper.</p>
<p>For example, the following commands would be used to compile with the gfortran compiler, activate compiler warnings (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-Wall</code>), and requiring aggressive compiler optimisation (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-O3</code>):</p>
<p><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">module load gimkl/2018b</code></p>
<p><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">mpif90 -Wall -O3 -o simpleMpi simpleMpi.f90</code></p>
<h1 id="compiler-options">Linking</h1>
<p>Your application may depend on one or more external software packages, normally libraries, and if so it will need to link against them when you compile the program. In general, to link against an external package, one must specify:</p>
<ul>
<li>The location of the header files, using the option <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-I/path/to/headers</code>
</li>
<li>The location of the compiled library or libraries, using <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-L/path/to/lib/</code>
</li>
<li>The name of each library, typically without prefixes and suffixes. For example, if the full library file name is <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">libfoo.so.1.2.3</code> (with aliases <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">libfoo.so.1</code> and <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">libfoo.so</code>), the expected entry on the link line is <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-lfoo</code>.</li>
</ul>
<p>Thus the linker expects to find the include headers in the <em>/path/to/headers</em> and the library at <em>/path/to/lib/lib.so</em> (we assume dynamic linking).</p>
<p>Note that you may need to list several libraries to link successfully, e.g., <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-lA -lB</code> for linking against libraries "A" and "B". The order in which you list libraries matters, as the linker will go through the list in order of appearance. If library "A" depends on library "B", specifying <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-lA -lB</code> will work. If library "B" depends on "A", use <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-lB -lA</code>. If they depend on each other, use <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-lA -lB -lA</code> (although such cases are quite rare).</p>
<h2>External Libraries</h2>
<p>There are already many libraries provided on the Mahuika platform. Most of them are provided in modules. You can search them using</p>
<p><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">module spider</code></p>
<p>and look in the module description using:</p>
<p><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">module help &lt;module-name&gt;</code></p>
<p>Sometimes modules provide multiple libraries, e.g. <em>cray-libsci</em>.</p>
<p>Most libraries are provided using the EasyBuild software management system, that NeSI/NIWA use to provide modules. Easybuild automatically defines environment variables <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">$EBROOT&lt;library name in upper case&gt;</code> when a module is loaded, which help pointing the compiler and linker to include files and libraries as in the example above. Thus, you can keep your Makefile independent of library versions, by defining e.g. <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-L$EBROOT&lt;library name in upper case&gt;/lib</code>. Therewith you can use another version by only swapping modules. If you are unsure which <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">$EBROOT&lt;...&gt;</code> variables are available, use</p>
<p><code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">module show &lt;module-name&gt;</code></p>
<p>to find out.</p>
<p>Note that specifying search paths with <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-I</code> and <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-L</code> is not strictly necessary in case of the GNU and Intel compilers, which will use the contents of <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">CPATH</code>, <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">LIRARY_PATH</code>, and <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">LD_LIBRARY_PATH</code> provided by the NeSI/NIWA module. This will not work with the Cray compiler.</p>
<p><strong>Important note:</strong> Make sure that you load the correct variant of a library, depending on your choice of compiler. Switching compiler environment will <em>not</em> switch NeSI/NIWA modules automatically. Furthermore, loading a NeSI/NIWA module may switch programming environment if it was built with a different compiler. In general, the used library should be build with the same compiler.</p>
<p><strong>Note:</strong> the mentioned MPI compilers are practically compiler wrappers adding the location to the MPI library. This can be observed calling e.g. <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">mpif90 -showme</code></p>
<h2>Common Linker Problems<span class="wysiwyg-underline"><br></span>
</h2>
<p>Linking can easily go wrong. Most often, you will see linker errors about "missing symbols" when the linker could not find a function used in your program or in one of the libraries that you linked against. To resolve this problem, have a closer look at the function names that the linker reported:</p>
<ul>
<li>Are you missing some object code files (these are compiled source files and have suffix <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">.o</code>) that should appear on the linker line? This can happen if the build system was not configured correctly or has a bug. Try running the linking step manually with all source files and debug the build system (which can be a lengthy and cumbersome process, unfortunately).</li>
<li>Do the missing functions have names that contain "mp" or "omp"? This could mean that some of your source files or external libraries were built with OpenMP support, which requires you to set an OpenMP flag (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-fopenmp</code> for GNU compilers, <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-qopenmp</code> for Intel) in your linker command. For the Cray compilers, OpenMP is enabled by default and can be controlled using <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-h[no]omp</code>.</li>
<li>Do you see a very long list of complex-looking function names, and does your source code or external library dependency include C++ code? You may need to explicitly link against the C++ standard library (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-lstdc++</code> for GNU and Cray compilers, <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-cxxlib</code> for Intel compilers); this is a particularly common problem for statically linked code.</li>
<li>Do the function names end with an underscore ("_")? You might be missing some Fortran code, either from your own sources or from a library that was written in Fortran, or parts of your Fortran code were built with flags such as <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-assume nounderscore</code> (Intel) or <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-fno-underscoring</code> (GNU), while others were using different flags (note that the Cray compiler always uses underscores).</li>
<li>Do the function names end with double underscores ("__")? Fortran compilers offer an option to add double underscores to Fortran subroutine names for compatibility reasons (<code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-h [no]second_underscore</code>, <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-assume [no]2underscores</code>, <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-f[no-]second-underscore</code>) which you may have to add or remove.</li>
<li>Compiler not necessarily enable preprocessing, which could result in <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">#ifndef VAR; Warning: Illegal preprocessor directive</code>. For example, using preprocessor directives in <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">.f</code> files with gfortran requires the <code style="font-family: Menlo, Consolas, 'DejaVu Sans Mono', monospace;">-cpp</code> option.</li>
</ul>
<p>Note that the linker requires that function names match exactly, so any variation in function name in your code will lead to a "missing symbols" error (with the exception of character case in Fortran source code).</p>
<h1 id="compiler-options">Cray Programming Environment</h1>
<p>The Cray Programming Environment includes the Cray compiler, various libraries and tools. These work nicely together and provide certain user-friendly features by using compiler wrappers. This works very similar as the Cray XC environment, provided on Maui, and is described in detail on the page <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000336076">Building Code on Maui</a>.</p>
<p><strong>Note:</strong> on Maui the three compilers (Cray, Gnu and Intel) are provided in this special environment, which provides support for both dynamic and static linking. In contrast to that, on Mahuika only the Cray compiler is provided in this environment. Furthermore, it only provides support for dynamic linking.</p>