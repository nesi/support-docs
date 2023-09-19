---
created_at: '2020-08-26T01:22:12Z'
hidden: true
label_names: []
position: 5
title: Offloading to a GPU with OpenACC using the PGI compiler
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001815716
zendesk_section_id: 360000040056
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p>With OpenACC it is possible to offload computations from the CPU to a GPU, see <a href="http://www.icl.utk.edu/~luszczek/teaching/courses/fall2016/cosc462/pdf/OpenACC_Fundamentals.pdf">http://www.icl.utk.edu/~luszczek/teaching/courses/fall2016/cosc462/pdf/OpenACC_Fundamentals.pdf</a>.</p>
<h1>Example</h1>
<p>In the following we show how to achieve this in the case of a reduction operation involving a large loop:</p>
<pre>#include &lt;iostream&gt;<code class="hljs cpp"><br><span class="hljs-meta"><span class="hljs-meta-string">#include &lt;math.h&gt;</span></span><br><span class="hljs-meta"><span class="hljs-meta-string">int main() {</span></span><br><span class="hljs-meta"><span class="hljs-meta-string"> int n = 1000000000;</span></span><br><span class="hljs-meta"><span class="hljs-meta-string"> double total = 0;</span></span><br><span class="hljs-meta"><span class="hljs-meta-string"> int i;</span></span><br><span class="hljs-meta"><span class="hljs-meta-string">#pragma acc parallel loop copy(total) copyin(n) reduction(+:total)</span></span><br><span class="hljs-meta"><span class="hljs-meta-string"> for (i = 0; i &lt; n; ++i) {</span></span><br><span class="hljs-meta"><span class="hljs-meta-string">  total += exp(sin(M_PI * (double) i/12345.6789));</span></span><br><span class="hljs-meta"><span class="hljs-meta-string"> }</span></span><br><span class="hljs-meta"><span class="hljs-meta-string"> std::cout &lt;&lt; "total is " &lt;&lt; total &lt;&lt; '\n';</span></span><br><span class="hljs-meta"><span class="hljs-meta-string">}</span></span><br></code></pre>
<p>Save the above code in file total.cxx.</p>
<p>Note the pragma</p>
<pre><code class="hljs cpp"><span class="hljs-meta">#<span class="hljs-meta-keyword">pragma</span> acc parallel loop copy(total) copyin(n) reduction(+:total)</span></code></pre>
<p>which moves variables <code>total</code> and <code>n</code> to the GPU and creates teams of threads to compute the total sum in parallel. </p>
<h1>Compile</h1>
<p>We'll use the PGI C++ compiler to build the executable but first we need to load a few modules:</p>
<p><code class="hljs ruby"><span class="hljs-class"><span class="hljs-keyword">module</span> <span class="hljs-title">load</span> PGI CUDA</span><br></code></p>
<p>To compare the execution times between the CPU and GPU version, we build two executables:</p>
<pre><code class="hljs css">pgc++ -fast -acc -ta=multicore -Minfo=accel <span class="hljs-selector-tag">-o</span> <span class="hljs-selector-tag">totalAccMulticore</span> <span class="hljs-selector-tag">total</span><span class="hljs-selector-class">.cxx</span><br>pgc++ -fast -acc -ta=tesla -Minfo=accel <span class="hljs-selector-tag">-o</span> <span class="hljs-selector-tag">totalAccGpu</span> <span class="hljs-selector-tag">total</span><span class="hljs-selector-class">.cxx</span></code></pre>
<p>Note that the PGI compiler can target CPU and GPU devices (-ta option). The -Minfo=all option provides information about vectorization and offloading.</p>
<h1>Run</h1>
<p>The following commands will submit the runs to the Mahuika queue (note <code>--partition=gpu --gres=gpu:1</code> in the case of the executable that offloads to the GPU):</p>
<pre><code class="hljs perl"><span class="hljs-keyword">time</span> srun --ntasks=<span class="hljs-number">1</span> --cpus-per-task=<span class="hljs-number">1</span> ./totalAccMulticore<br>OMP_NUM_THREADS=8 &amp;&amp; time srun --ntasks=1 --cpus-per-task=$OMP_NUM_THREADS --hint=nomultithread ./totalAccMulticore<br>time srun --ntasks=1 --cpus-per-task=1 --partition=gpu --gres=gpu:<span class="hljs-number">1</span> ./totalAccGpu<br><br></code></pre>
<table style="height: 32px;" width="408">
<tbody>
<tr>
<td style="width: 227px;">
<p>executable</p>
</td>
<td style="width: 158px;">time [s]</td>
</tr>
<tr>
<td style="width: 227px;">totalAccMulticore</td>
<td style="width: 158px;">
<p>121.3</p>
</td>
</tr>
<tr>
<td style="width: 227px;">totalAccMulticore 8 threads</td>
<td style="width: 158px;">
<p>36.8</p>
</td>
</tr>
<tr>
<td style="width: 227px;">totalAccGpu</td>
<td style="width: 158px;">3.1</td>
</tr>
</tbody>
</table>