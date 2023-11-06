---
created_at: '2019-08-26T23:41:11Z'
hidden: false
label_names: []
position: 3
title: 'Offloading to GPU with OpenMP '
vote_count: 1
vote_sum: 1
zendesk_article_id: 360001127856
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>With OpenMP 4.5, it has become possible to offload computations from the CPU to a GPU, see <a href="https://www.openmp.org/wp-content/uploads/SC18-BoothTalks-Jost.pdf" target="_self">https://www.openmp.org/wp-content/uploads/SC18-BoothTalks-Jost.pdf</a></p>
<h1>Example</h1>
<p>In the following we show how to achieve this in the case of a reduction operation involving a large loop:</p>
<pre><code>#include &lt;iostream&gt;<br>#include &lt;cmath&gt;<br>int main() {<br> int n = 1000000000;<br> double total = 0;<br>#pragma omp target teams distribute \<br>parallel for map(tofrom: total) map(to: n) reduction(+:total)<br> for (int i = 0; i &lt; n; ++i) {<br> total += exp(sin(M_PI * (double) i/12345.6789));<br> }<br> std::cout &lt;&lt; "total is " &lt;&lt; total &lt;&lt; '\n';<br>}</code></pre>
<p>Save the above code in file total.cxx.</p>
<p>Note the pragma</p>
<pre><code>#pragma omp target teams distribute parallel for map(tofrom: total) \<br>map(to: n) reduction(+:total)</code></pre>
<p>which moves variables <code>total</code> and <code>n</code> to the GPU and creates teams of threads to perform the sum operation in parallel. </p>
<h1>Compile</h1>
<p>We'll use the Cray C++ compiler to build the executable but first we need to load a few modules:</p>
<pre><code>module load cray-libsci_acc/18.06.1 craype-accel-nvidia60 \<br> PrgEnv-cray/1.0.4 cuda92/blas/9.2.88 cuda92/toolkit/9.2.88</code></pre>
<p>(Ignore warning "<span class="s1">cudatoolkit &gt;= 8.0 is required").</span></p>
<p>To compare the execution times between the CPU and GPU version, we build two executables:</p>
<pre><code>CC -h noomp -o total total.cxx<br>CC -o totalOmpGpu total.cxx</code></pre>
<p>with executable <code>total</code> compiled with <code>-h noomp</code>, i.e. OpenMP turned off.</p>
<h1>Run</h1>
<p>The following commands will submit the runs to the Mahuika queue (note <code>--partition=gpu --gres=gpu:1</code> in the case of the executable that offloads to the GPU):</p>
<pre><code>time srun --ntasks=1 --cpus-per-task=1 ./total
time srun --ntasks=1 --cpus-per-task=1 --partition=gpu --gres=gpu:1 ./totalOmpGpu</code></pre>
<table style="height: 92px;" width="408">
<tbody>
<tr>
<td style="width: 197px;">
<p>executable</p>
</td>
<td style="width: 204px;">time [s]</td>
</tr>
<tr>
<td style="width: 197px;">total</td>
<td style="width: 204px;">10.9</td>
</tr>
<tr>
<td style="width: 197px;">totalOmpGpu</td>
<td style="width: 204px;">0.45</td>
</tr>
</tbody>
</table>