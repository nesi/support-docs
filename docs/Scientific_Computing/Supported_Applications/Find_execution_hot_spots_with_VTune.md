---
created_at: '2020-01-15T21:56:01Z'
hidden: true
label_names: []
position: 14
title: Find execution hot spots with VTune
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001332675
zendesk_section_id: 360000040076
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<h2>What is VTune?</h2>
<p>VTune is a tool that allows you to quickly identify where most of the execution time of a program is spent. This is known as profiling. It is good practice to profile a code before attempting to modify the code to improve its performance. VTune collects key profiling data and presents them in an intuitive way.  Another tool that provides similar information is <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000930396-Profiler-ARM-MAP" target="_self">ARM MAP</a>.</p>
<h2>How to use VTune</h2>
<p>We'll show how to profile a C++ code with VTune - feel free to choose your own code instead. Start with </p>
<pre>git clone <a href="https://github.com/pletzer/fidibench">https://github.com/pletzer/fidibench</a></pre>
<p>and build the code using the "gimkl" tool chain</p>
<pre>cd fidibench<br>mkdir build<br>cd build<br>module load gimkl CMake<br>cmake ..<br>make</pre>
<p>This will compile a number of executables. Note that VTune does not require one to apply a special compiler switch to profile. You can profile an existing executable if you like. We choose "upwindCxx" as the executable to profile. It is under upwind/cxx, so</p>
<pre>cd upwind/cxx</pre>
<p>Run the executable with </p>
<pre>module load VTune<br><span class="s1">srun --ntasks=1 --cpus-per-task=2 --hint=nomultithread amplxe-cl -collect hotspots -result-dir vtune-res ./upwindCxx -numCells 256 -numSteps 10</span></pre>
<p>Executable <span class="s1">"upwindCxx" takes arguments "-numCells 256" (the number of cells in each dimension) and  "-numSteps 10" (the number of time steps). </span>Note the command "<span class="s1">amplxe-cl -collect hotspots -result-dir" which was inserted before the executable. The output may look like</span></p>
<p class="p1"><span class="s1">Top Hotspots</span></p>
<p class="p1"><span class="s1">Function<span class="Apple-converted-space">                                    </span>Module<span class="Apple-converted-space">          </span>CPU Time</span></p>
<p class="p1"><span class="s1">------------------------------------------<span class="Apple-converted-space">  </span>--------------<span class="Apple-converted-space">  </span>--------</span></p>
<p class="p1"><span class="s1">Upwind&lt;(unsigned long)3&gt;::advect._omp_fn.1<span class="Apple-converted-space">  </span>upwindCxx<span class="Apple-converted-space">        </span>25.979s</span></p>
<p class="p1"><span class="s1">_int_free <span class="Apple-converted-space">                                  </span>libc.so.6 <span class="Apple-converted-space">        </span>9.170s</span></p>
<p class="p1"><span class="s1">operator new<span class="Apple-converted-space">                                </span>libstdc++.so.6<span class="Apple-converted-space">    </span>6.521s</span></p>
<p class="p1"><span class="s1">free<span class="Apple-converted-space">                                        </span>libmpi.so.12<span class="Apple-converted-space">      </span>0.300s</span></p>
<p><span class="s1">indicating that the vast majority of time is spent in the "advect" method (26s), with significant amounts of time spent allocating (6.5s) and deallocating (9.2s) memory. </span></p>
<h2> Drilling further into the code</h2>
<p><span class="s1">Often this is enough to give you a feel for where the code can be improved. To explore further you can fire up</span> </p>
<pre><span class="s1">amplxe-gui &amp;</span></pre>
<p><span class="s1">Go to the bottom and select "Open Result...", choose the directory where the profiling results are saved and click on the .amplxe file. The summary will look similar to the above table. However, you can now dive into selected functions to get more information. Below we see that 16.5 out of 26 seconds were spent starting the two OpenMP threads.  <br><br></span></p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360003239635/Screen_Shot_2020-01-16_at_11.06.53_AM.png" alt="Screen_Shot_2020-01-16_at_11.06.53_AM.png"> </p>
<p> </p>