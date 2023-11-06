---
created_at: '2015-10-14T22:58:53Z'
hidden: false
label_names:
- mahuika
- engineering
- general
position: 35
title: MATLAB
vote_count: 1
vote_sum: 1
zendesk_article_id: 212639047
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->
<div id="lic_append">
<blockquote class="blockquote-warning">
<h3 id="prerequisites">No Licence?</h3>
<p>If you want to run MATLAB code on the cluster, but are not a member of an institution without access to floating licences, MATLAB code can still be run on the cluster using MCR.</p>
</blockquote>
</div>
<h1 id="example-script-for-the-pan-cluster">Example script</h1>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>When developing MATLAB code on your local machine, take measures to ensure it will be platform independent.  Use relative paths when possible and not avoid using '\'s see <a href="https://www.mathworks.com/help/matlab/ref/fullfile.html" target="_self">here</a>.</p>
</blockquote>
<h2>Script Example</h2>
<pre><code class="bash">#!/bin/bash -e
#SBATCH --job-name   MATLAB_job   # Name to appear in squeue <br>#SBATCH --time       01:00:00     # Max walltime <br>#SBATCH --mem        512MB        # Max memory<br><br>module load MATLAB/2021b<br># Run the MATLAB script MATLAB_job.m <br>matlab -nodisplay &lt; MATLAB_job.m </code></pre>
<h2>Function Example</h2>
<pre><code>#!/bin/bash -e
#SBATCH --job-name       MATLAB_job    # Name to appear in squeue<br>#SBATCH --time           06:00:00      # Max walltime<br>#SBATCH --mem            2048MB        # Max memory<br>#SBATCH --cpus-per-task  4             # 2 physical cores.<br>#SBATCH --output         %x.log        # Location of output log<br><br>module load MATLAB/2021b<br><br>#Job run <br>matlab -batch "addpath(genpath('../parentDirectory'));myFunction(5,20)"<br># For versions older than 2019a, use '-nodisplay -r' instead of '-batch'</code></pre>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Command Line</h3>
<p>When using matlab on command line, all flag options use a single '<code>-</code>' e.g. <code>-nodisplay</code>, this differs from the GNU convention of using <code>--</code> for command line options of more than one character.</p>
</blockquote>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Bash in MATLAB</h3>
<p>Using the prefix <code>!</code> will allow you to run bash commands from within MATLAB. e.g. <code>!squeue -u $USER</code> will print your currently queued slurm jobs.</p>
</blockquote>
<h1 id="parallelism">Parallelism</h1>
<p>MATLAB does not support MPI therefore #SBATCH --ntasks should always be 1, but if given the necessary resources some MATLAB functions can make use of multiple threads (--cpus-per-task) or GPUs (--gpus-per-node).</p>
<h2>Implicit parallelism.</h2>
<p>Implicit parallelism requires no changes to be made in your code. By default MATLAB will utilise multi-threading for a wide range of operations, scalability will vary but generally you will not be able to utilise more than a 4-8 CPUs this way.</p>
<h2>Explicit parallelism.</h2>
<p>Explicit parallelism is when you write your code specifically to make use of multiple CPU's. This can be done using MATLABs <em>parpool</em>-based language constructs, MATLAB assigns each thread a 'worker' that can be assigned sections of code.</p>
<p>MATLAB will make temporary files under your home directory (in ~/.matlab/local_cluster_jobs) for communication with worker processes. To prevent simultaneous parallel MATLAB jobs from interfering with each other you should tell them to each use their own job-specific local directories:</p>
<pre><code class="matlab">pc = parcluster('local')
pc.JobStorageLocation = getenv('TMPDIR')
parpool(pc, str2num(getenv('SLURM_CPUS_PER_TASK')))
</code></pre>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>Parpool will throw a warning when started due to a difference in how time z<dfn class="dictionary-of-numbers">one is specified</dfn>. To fix this, add the following line to your SLURM script: <code>export TZ="Pacific/Auckland'</code></p>
</blockquote>
<p> The main ways to make use of parpool are;</p>
<p><strong>parfor: </strong>Executes each iteration of a loop on a different worker. e.g.</p>
<pre><code class="matlab">parfor i=1:100<br><br>   %Your operation here.<br><br>end</code></pre>
<p><code>parfor</code> operates similarly to a SLURM job array and must be embarrassingly parallel. Therefore all variables either need to be defined locally (used internally within one iteration of the loop), or static (not changing during execution of loop).</p>
<p>More info <a href="https://au.mathworks.com/help/parallel-computing/parfor.html" target="_self">here</a>.</p>
<p><strong>parfeval:</strong></p>
<p><code>parfeval</code> is used to assign a particular function to a thread, allowing it to be run asynchronously. e.g.</p>
<pre><code class="matlab">my_coroutine=parfeval(@my_async_function,2,in1,in2);<br><br>% Do something that doesn't require outputs from 'my_async_function'<br><br>[out1, out2]=fetchOutputs(my_coroutine); % If 'my_coroutine' has not finished execution will pause.<br><br>function [out1,out2]=my_async_function(in1,in2)<br><br>%Your operation here.<br><br>end</code></pre>
<p><code class="matlab">fetchOutputs</code> is used to retrieve the values.</p>
<p>More info <a href="https://au.mathworks.com/help/parallel-computing/parfeval.html" target="_self">here</a>.</p>
<blockquote class="blockquote-warning">
<h3 id="">Note</h3>
<p>When killed (cancelled, timeout, etc), job steps utilising parpool may show state <code>OUT_OF_MEMORY</code>, this is a quirk of how the steps are ended and not necessarily cause to raise total memory requested.</p>
</blockquote>
<hr>
<p>Determining which of <a href="https://au.mathworks.com/help/parallel-computing/troubleshoot-variables-in-parfor-loops.html" target="_self">these</a> categories your variables fall under is a good place to start when attempting to parallelise your code.</p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Tip</h3>
<p>If your code is parallel at a high level it is preferable to use <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000690275-Parallel-Execution#t_array" target="_self">SLURM job arrays</a> as there is less computational overhead and the multiple smaller jobs will queue faster.</p>
</blockquote>
<h1 id="GPU">Using GPUs</h1>
<p>As with standard parallelism, some MATLAB functions will work implicitly on GPUs while other require setup. More info on using GPUs with MATLAB <a href="https://au.mathworks.com/help/parallel-computing/run-matlab-functions-on-a-gpu.html" target="_self" rel="undefined">here</a>, and writing code for GPUs <a href="https://au.mathworks.com/hardware-support/nvidia-tesla.html" target="_blank" rel="noopener">here</a>.</p>
<p>MATLAB uses NVIDIA CUDA toolkit. Depending on the version of MATLAB, a different version of CUDA is needed, see <a href="https://nl.mathworks.com/help/releases/R2021b/parallel-computing/gpu-support-by-release.html" target="_self" rel="undefined">GPU Support by Release</a> in MATLAB documentation. Use <code>module spider CUDA</code> to list all available CUDA modules and select the appropriate one. For example, for MATLAB R2021a, use <code>module load CUDA/11.0.2</code> before launching MATLAB.</p>
<p>If you want to know more about how to access the different type of available GPUs on NeSI, check the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001471955" target="_blank" rel="noopener">GPU use on NeSI</a> support page.</p>
<blockquote class="blockquote-warning">
<h3 id="octopus-warning">Support for A100 GPUs</h3>
To use MATLAB with a A100 or a A100-1g.5gb GPU, you need to use a version of MATLAB supporting the <em>Ampere</em> architecture (see <a href="https://nl.mathworks.com/help/releases/R2021b/parallel-computing/gpu-support-by-release.html" target="_self" rel="undefined">GPU Support by Release</a>). We recommend that you use R2021a or a more recent version.</blockquote>
<blockquote class="blockquote-tip">
<h3 id="llama-tip">Note on GPU cost</h3>
<p>A GPU device-hour costs more than a core-hour, depending on the type of GPU. You can find a comparison table in our <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001385735" target="_blank" rel="noopener">What is an allocation?</a> support page.</p>
</blockquote>
<h2 id="gpuexample">GPU Example</h2>
<pre><code>#!/bin/bash -e
#SBATCH --job-name       MATLAB_GPU    # Name to appear in squeue
#SBATCH --time           01:00:00      # Max walltime
#SBATCH --mem            10G           # 10G per GPU
#SBATCH --cpus-per-task  4             # 4 CPUs per GPU
#SBATCH --output         %x.%j.log     # Location of output log
#SBATCH --gpus-per-node  1             # Number of GPUs to use (max 2)

module load MATLAB/2021a
module load CUDA/11.0.2  # Drivers for using GPU

matlab -batch "gpuDevice()"</code></pre>
<h1>Adding Support Packages</h1>
<p>If you have X-11 set up you can install additional package through the GUI. You can also install manually if you already have the files by copying them into your Support Package root directory..</p>
<p>Support packages are usually saved in your home directory, you can see the path using the MATLAB command <code>matlabshared.supportpkg.getSupportPackageRoot</code> if it is unset, you can specify it with <code> matlabshared.supportpkg.setSupportPackageRoot("&lt;path&gt;")</code></p>
<h2>mexopencv</h2>
<p>mexopencv is <a href="https://github.com/kyamagu/mexopencv" target="_self">mex wrapper MATLAB wrapper for the openCV library.</a></p>
<p>Some of the internal MATLAB libraries clash with those used by OpenCV, to avoid problems cause by this</p>
<ul>
<li>Use a version of OpenCV built using GCC (as opposed to gimkl).</li>
<li>Compile using the -DWITH_OPENCL=OFF flag.</li>
</ul>
<p>Please contact support if you have any issues.</p>
<h1 id="mexing">Improving performance with mexing</h1>
<p>Like other scripting languages, MATLAB code will generally run slower than compiled code since every MATLAB instruction needs to be parsed and interpreted. Instructions inside large MATLAB loops are often performance hotspots due to the interpreter's overhead, which consumes CPU time at every iteration.</p>
<p>Fortunately MATLAB lets programmers extend their scripts with C/C++ or Fortran, which is referred to as <a href="https://au.mathworks.com/help/matlab/ref/mex.html" target="_self">mexing</a>.</p>
<p>more info about compiling software on NeSI <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000329015-Compiling-software-on-Mahuika" target="_self">here</a>.</p>
<h2>Writing mex functions</h2>
<p>  This involves the following steps (using C++ as an example):</p>
<ol>
<li>Focus on a loop to extend, preferably a nested set of loops.</li>
<li>Identify the input and output variables of the section of code to extend.</li>
<li>Write C++ code. The name of the C++ file should match the name of the function to call from MATLAB, e.g. <code>myFunction.cpp</code> for a function named <code>myFunction</code>.</li>
<li>Compile the extension using the MATLAB command <code>mex myFunction.cpp</code>
</li>
</ol>
<p>At the minimum, the C++ extension should contain:</p>
<pre>#include &lt;mex.h&gt;<br>#include &lt;matrix.h&gt;<br><br>void mexFunction(int nlhs, mxArray *plhs[],<br>                 int nrhs, const mxArray *prhs[]) {<br>    // implementation goes here<br>}</pre>
<p>Note that the above function should always be called <code>mexFunction</code> and its signature be <code>int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[]</code>. Here, <code>nlhs</code> and <code>nrhs</code> refer to the number of output and input arguments respectively. Access each dummy argument with index <code>i = 0 ... nlhs-1</code> and <code>j = 0 ... nrhs-1</code> respectively. Regardless of the type of argument, whether it is a number, a matrix or an object, its type is <code>mxArray</code>. Often you will need to cast the argument into a corresponding C++ type, e.g.</p>
<pre>// cast as a double, note the asterisk in front of mxGetPr<br>double x = (double) *mxGetPr(prhs[0]);</pre>
<p>or</p>
<pre>// cast as an array of doubles<br>double* arr = (double*) mxGetPr(prhs[0]);</pre>
<p>Use <code>mxCreateDoubleMatrix</code> and <code>mxCreateDoubleScalar</code> to create a matrix and a number, respectively. For example:</p>
<pre>// function returns [plhs[0], plhs[1]]<br>plhs[0] = mxCreateDoubleMatrix(3, 2, mxREAL);  // 3 by 2 matrix<br>plhs[1] = mxCreateDoubleScalar(2);  // number</pre>
<p>All numbers are doubles. Use flat array indexing <code>a[i + n*j - 1]</code> in C++ to access elements of a MATLAB matrix <code>a(i, j)</code> of size <code>n x m</code>.</p>
<p>MATLAB will take care of destroying matrices and other object so you should feel free to create objects inside C++ code (required for functions that have return values).</p>
<p>Some mex function source code examples can be found in the table <a href="https://au.mathworks.com/help/matlab/matlab_external/table-of-mex-file-source-code-files.html" target="_blank" rel="noopener">here</a>. </p>
<h2>Compilation</h2>
<p>MATLAB supports the following compilers.</p>
<table style="height: 121px; width: 660px;">
<tbody>
<tr>
<td style="width: 120px;">C++</td>
<td style="width: 122.267px;">up to GCC 6.3.x</td>
</tr>
<tr>
<td style="width: 120px;">C</td>
<td style="width: 122.267px;">up to GCC 6.3.x</td>
</tr>
<tr>
<td style="width: 120px;">FORTRAN</td>
<td style="width: 122.267px;">up to GNU gfortran 6.3.x</td>
</tr>
</tbody>
</table>
<p>The most up to date compilers supported by MATLAB can be loaded on NeSI using <code class="code-bash">module load gimkl/2017a</code></p>
<p>If no GCC module is loaded, the default system version of these compilers will be used.</p>
<p>Further configuration can be done within MATLAB using the command <code class="code-matlab">mex -setup</code></p>
<p><code>mex &lt;file_name&gt;</code>  will then compile the mex function. </p>
<p>Default compiler flags can be overwritten with by setting the appropriate environment variables. The COMPFLAGS variable is ignored as it is Windows specific.</p>
<table style="height: 88px;" width="675">
<tbody>
<tr>
<td style="width: 325.556px;">C++</td>
<td style="width: 325.556px;"><code>CXXFLAGS</code></td>
</tr>
<tr>
<td style="width: 325.556px;">C</td>
<td style="width: 325.556px;"><code>CFLAGS</code></td>
</tr>
<tr>
<td style="width: 325.556px;">FORTRAN</td>
<td style="width: 325.556px;"><code>FFLAGS</code></td>
</tr>
<tr>
<td style="width: 325.556px;">Linker</td>
<td style="width: 325.556px;"><code>LDFLAGS</code></td>
</tr>
</tbody>
</table>
<p>For example, adding OpenMP flags for a fortran compile:</p>
<div class="code_responsive">
<div class="programlisting">
<div class="codeinput">
<pre>mex FFLAGS='$FFLAGS -fopenmp' LDFLAGS='$LDFLAGS -fopenmp' &lt;file_name&gt;</pre>
</div>
</div>
</div>
<blockquote class="blockquote-warning">
<h3 id="">Compiler Version Errors</h3>
<p>Using an 'unsupported' compiler with versions of MATLAB 2020b onward will result in an Error (previously was a 'Warning').</p>
</blockquote>
<h1>Known Bugs</h1>
<p>When using versions of MATLAB more recent than 2021a you may notice the following warning.</p>
<div class="content">
<pre class="SC7580F400"><span class="SC7580F401"><span class="SC7580F402"></span><span class="SC7580F402">glibc_shim: Didn't find correct code to patch</span><span class="SC7580F402"></span></span></pre>
<p>This warning appears whenever MATLAB interfaces with the operating system (e.g. <code>ls</code> or <code>system()</code> or use of the <code>!</code> prefix).</p>
<p>Most of the time this should not affect your work.</p>
<p>We expect this issue to be fixed by our next operating system upgrade.</p>
</div>