---
created_at: '2019-08-28T01:48:30Z'
hidden: false
label_names: []
position: 4
title: Offloading to GPU with OpenACC
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001131076
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>Many codes can be accelerated significantly by offloading computations to a GPU. Some NeSI <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001471955-GPU-use-on-NeSI" target="_self">Mahuika nodes have GPUs attached to them</a>. If you want your code to run faster, if you're developing your own code or if you have access to the source code and you feel comfortable editing the code, read on.</p>
<p>Here we show how to tell the compiler which part of your algorithm you want to run a GPU. We'll use OpenACC, which adds directives to your source code. The advantages of OpenACC over other approaches is that the source code changes are generally small and your code remains portable, i.e. it will run on both CPU and GPU. The main disadvantage of OpenACC is that only a few compilers support it. </p>
<p>More information about OpenACC can be found <a href="http://www.icl.utk.edu/~luszczek/teaching/courses/fall2016/cosc462/pdf/OpenACC_Fundamentals.pdf" target="_self">here</a>.</p>
<h1>Example</h1>
<p>In the following we show how to achieve this in the case of a reduction operation involving a large loop in C++ (a similar example can be written in Fortran):</p>
<pre><code>#include &lt;iostream&gt;<br>#include &lt;cmath&gt;<br>int main() {<br> double total = 0;<br> int i, n = 1000000000;<br>#pragma acc parallel loop copy(total) copyin(n) reduction(+:total)<br> for (i = 0; i &lt; n; ++i) {<br>   total += exp(sin(M_PI * (double) i/12345.6789));<br> }<br> std::cout &lt;&lt; "total is " &lt;&lt; total &lt;&lt; '\n';<br>}<br></code></pre>
<p>Save the above code in file total.cxx.</p>
<p>Note the pragma</p>
<pre><code>#pragma acc parallel loop copy(total) copyin(n) reduction(+:total)</code></pre>
<p>We're telling the compiler that the loop following this pragma should be executed in parallel on the GPU. Since GPUs have hundreds or more threads, the speedup can be significant. Also note that <code>total</code> is initialised on the CPU (above the pragma) and should be copied to the GPU and back to the CPU after completing the loop. (It is also possible to initialise this variable on the GPU.) Likewise the number of iterations <code>n</code> should be copied from the CPU  to the GPU. </p>
<h1>Compile</h1>
<p>We can use the NVIDIA compiler</p>
<p><code>module load NVHPC</code></p>
<p>and type</p>
<p><code>nvc++ -Minfo=all -acc -o totalAccNv total.cxx</code></p>
<p>to compile the example.</p>
<p>Alternatively, we can use the Cray C++ compiler to build the executable but first we need to load a few modules:</p>
<pre><code>module load craype-broadwell
module load cray-libsci_acc 
module load craype-accel-nvidia60 
module load PrgEnv-cray</code></pre>
<p>(Ignore warning "<span class="s1">cudatoolkit &gt;= 8.0 is required"). Furthermore, you may need to load <code>cuda/fft</code> or <code>cuda/blas</code><br></span></p>
<p>To compare the execution times between the CPU and GPU version, we build two executables:</p>
<pre><code>CC -h noacc -o total total.cxx<br>CC -o totalAccGpu total.cxx</code></pre>
<p>with executable <code>total</code> compiled with <code>-h noacc</code>, i.e. OpenACC turned off.</p>
<h1>Run</h1>
<p>The following commands will submit the runs to the Mahuika queue (note <code>--gpus-per-node=P100:1</code> in the case of the executable that offloads to the GPU):</p>
<pre><code>time srun --ntasks=1 --cpus-per-task=1 ./total
time srun --ntasks=1 --cpus-per-task=1 --gpus-per-node=P100:1 ./totalAccGpu</code></pre>
<table style="height: 104px;" width="417">
<tbody>
<tr>
<td style="width: 194.5px;">
<p>executable</p>
</td>
<td style="width: 199.5px;">time [s]</td>
</tr>
<tr>
<td style="width: 194.5px;">total</td>
<td style="width: 199.5px;">7.6</td>
</tr>
<tr>
<td style="width: 194.5px;">totalAccGpu</td>
<td style="width: 199.5px;">0.41</td>
</tr>
</tbody>
</table>
<p> </p>
<p>Check out <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001127856-Offloading-to-GPU-with-OpenMP-" target="_self">this page</a> to find out how you can offload computations to a GPU using OpenMP.</p>