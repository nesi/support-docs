---
created_at: '2019-04-30T00:21:48Z'
hidden: false
label_names: []
position: 1
title: 'Profiler: ARM MAP'
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000930396
zendesk_section_id: 360000278935
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <ul>
<li><a href="#introduction-to-profiling" target="_self">Introduction to profiling</a></li>
<li><a href="#h_23e5a159-4e9c-4f25-9395-53f03e1187f7" target="_self">Profiling test cases</a></li>
<li><a href="#h_e444a43e-f0a5-45a5-8ed2-8bd06abae1a9" target="_self">MAP profiler</a></li>
<li><a href="#using-the-express-launch" target="_self">MAP “Express Launch”</a></li>
<li><a href="#h_f78992f8-3f55-4b6f-ac5f-8bc82ff16873" target="_self">MAP GUI launch</a></li>
<li><a href="#map-profile" target="_self">MAP Profile</a></li>
</ul>
<p>The ARM (previously known as Allinea) provides a package called <em>forge</em>, which consists of a debugger, DDT and a profiler, MAP.</p>
<h1 id="introduction-to-profiling">Introduction to profiling</h1>
<p>Profiling tools help you understand how much resources are consumed during run time. This can be time, memory, or MPI communication. One main goal is to understand in which parts of your code most time is spent. Depending on the profiler and the applied methods, profiles can be gathered on basis of<span class="wysiwyg-color-black"> functions, loops within functions, or source code lines. </span>Profiling information is important for optimising code, as it enables you to focus your efforts on improving the parts of the code that will result in the biggest gains in performance.</p>
<h1 id="h_23e5a159-4e9c-4f25-9395-53f03e1187f7">Profiling test cases</h1>
<p>During a optimisation process profiling will be used regularly to monitor the behaviour and change in behaviour of the code. Therefore, it is advisable to have a representative but reasonable short test case. It should trigger all the desired features of the code. But keep in mind that with a reduced run time (e.g. fewer iterations) other parts of the code could become more dominant (e.g. initialisation phase). Furthermore, due to possible overhead from the profiling tool, the code could run slower than normal.</p>
<h1 id="h_e444a43e-f0a5-45a5-8ed2-8bd06abae1a9">MAP profiler</h1>
<p>MAP is a commercial product, which can profile parallel, multi-threaded and single-threaded C/C++, Fortran, as well as Python code. MAP supports codes with OpenMP threads and/or MPI communication and can be used without code modification.</p>
<p>MAP can be launched with a graphical user interface (GUI Launch) or without GUI (Express Launch). With the GUI the user specifies all the parameters including executables, options and parallelisation parameters in a guided form, while with the Express Launch a pre-existing script is modified. <span class="wysiwyg-color-black">The “Express Launch”, is preferable especially for jobs in complex scripts and workflows.</span></p>
<p><span class="wysiwyg-color-black">In either case, the analysis of the profiling data will be undertaken in the MAP GUI. This conveniently provides access to different metrics and allows</span> <span class="wysiwyg-color-black">the user to navigate through different levels of details, browsing through the code, and focusing on specific functions, loops and source code lines.  See section <a href="#map-profile" target="_self">MAP profile</a> below.</span></p>
<p><span class="wysiwyg-color-black">There is also an <a href="https://developer.arm.com/tools-and-software/server-and-hpc/arm-architecture-tools/downloads/download-arm-forge" target="_self">Arm Forge Client</a> you can download to your local machine. Therewith you can browse through your downloaded profiling data or even start your profiling/debug tasks from remote (not described in detail here).</span></p>
<p><span class="wysiwyg-color-black"><strong>Note:</strong> If you want to use the GUI on the NeSI systems, please remember to start your ssh session using X11 forwarding (e.g. using the <code>ssh -Y</code> option).</span></p>
<h1 id="using-the-express-launch">MAP “Express Launch”</h1>
<p>To use MAP we need to load the <em>forge</em> module in our batch script and add <code class="highlighter-rouge">map --profile</code> in front of the parallel run statements. For example:</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>module load forge
map --profile srun python scatter.py
</code></pre>
</div>
</div>
<p>Upon execution, a <code class="highlighter-rouge">.map</code> file will be generated. The results can be viewed, for instance, with</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>map python3_scatter_py_8p_1n_2019-01-14_00-31.map
</code></pre>
</div>
</div>
<p>(the <code class="highlighter-rouge">.map</code> file name will vary with each run.) See section <a href="#map-profile" target="_self">MAP profile</a> below for how to interpret the results.</p>
<h1 id="h_f78992f8-3f55-4b6f-ac5f-8bc82ff16873">MAP GUI launch</h1>
<p>The GUI can be started after loading <code class="highlighter-rouge">module load forge</code> and launching</p>
<div class="highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>map
</code></pre>
</div>
</div>
<p><a href="https://nesi.github.io/perf-training/python-scatter/images/ARM_MAP_main.png"><img src="https://nesi.github.io/perf-training/python-scatter/images/ARM_MAP_main.png" alt="Arm MAP main"></a></p>
<p>Click on “PROFILE”.</p>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360002074056/MAP_profile_python.PNG" alt="MAP_profile_python.PNG"></p>
<p>In the profile menu we need to specify the<em> executable/application</em> (in this case <code class="highlighter-rouge">python</code>), the arguments (here <code class="highlighter-rouge">scatter.py</code> and any additional options and arguments if necessary). Select the working directory, number of MPI processes, and OpenMP threads. Furthermore, the “submit to queue” parameter needs to be checked, for example the <code class="highlighter-rouge">--hint=nomultithread</code> can be specified there. In the environment Variables block, e.g. modules could be loaded or variables defined.</p>
<p>After <em>submit</em>ting, MAP will wait until the job is allocated, connect to the processes, run the program, gather all the data and present the profile information.</p>
<p> </p>
<h1 id="map-profile">MAP Profile</h1>
<p>By default the profile window is divided into the following three main sections (click on picture to enlarge).</p>
<p><a href="https://nesi.github.io/perf-training/python-scatter/images/ARM_MAP_scatter_mpi.png"><img src="https://nesi.github.io/perf-training/python-scatter/images/ARM_MAP_scatter_mpi.png" alt="example-map-scatter"></a></p>
<p>On top, various metrics can be selected in the “Metrics” menu. In the middle part, a source code navigator connects line by line source code with its profiling data. Most interesting is the profiling table at the bottom, which sorts the most time consuming parts of the program, providing function names, source code and line numbers.</p>
<p>There are various options to get even more information.</p>
<p>In the top part the metrics graphs can be changed to:</p>
<ul>
<li>Activity timeline</li>
<li>CPU instructions</li>
<li>CPU Time</li>
<li>IO</li>
<li>Memory</li>
<li>MPI</li>
</ul>
<p>using the <em>Metrics</em> Menu<em>. </em></p>
<p>As an example, “CPU instructions” presents the usage of different instruction sets during the program run time.</p>
<p><a href="https://nesi.github.io/perf-training/python-scatter/images/ARM_MAP_scatter_mpi_CPU.png"><img src="https://nesi.github.io/perf-training/python-scatter/images/ARM_MAP_scatter_mpi_CPU.png" alt="example-map-scatter_CPU"></a></p>
<p>The lower part can also be used to check the <em>application output</em> or show statistics on basis of <em>files</em> or <em>functions</em>.</p>
<p><strong>Note:</strong> often you can get additional information while hovering with your mouse over a certain item.</p>