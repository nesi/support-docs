---
created_at: '2019-07-22T03:46:24Z'
hidden: false
label_names: []
position: 2
title: OpenMP settings
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001070496
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p><a href="https://en.wikipedia.org/wiki/OpenMP" target="_self">OpenMP</a> is an application programming interface that lets you write parallel programs on shared memory platforms. In a parallel section, OpenMP code can create multiple threads that run on separate cores, executing their shares of the total workload concurrently. OpenMP is suited for the Mahuika and Māui HPCs as each platform has 36 and 40 physical cores per node respectively.  Each physical core can handle up to two threads in parallel using <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000568236" target="_self">Hyperthreading</a>. Therefore you can run up to 72 threads on Mahuika and 80 threads on Maui. </p>
<p>The environment variable that controls the number of threads is OMP_NUM_THREADS, e.g.,</p>
<pre>export OMP_NUM_THREADS=16</pre>
<p>allows OpenMP code to fork 16 threads. To make sure that resources requested from SLURM and used by your program are consistent, is usually a good idea to set</p>
<pre>#SBATCH --cpus-per-task=16<br>[...]<br>export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK</pre>
<p>in your SLURM script - although this can sometimes be more complicated, e.g., with <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000997675" target="_self">TensorFlow on CPUs</a>.</p>
<p>On Mahuika, you will be charged for the number of physical cores that you requested - the second logical core on a physical core is free, although SLURM always reports both cores. On Māui you will be charged for full nodes.</p>
<p>In order to achieve good and consistent parallel scaling, additional settings may be required. This is particularly true on Mahuika whose nodes are shared between different SLURM jobs. Following are some settings that can help improve scaling and/or make your timings more consistent, additional information can be found in our article <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000995575" target="_self">Thread Placement and Thread Affinity</a>.</p>
<p>1. --hint=nomultithread. Set this in conjunction with srun or sbatch to tell SLURM that you don't want to use hyperthreads. Your program will only be presented with physical cores. Inversely, --hint=multithread will request two threads per physical core. If --hint is not set, SLURM will currently assume --hint=multithread by default.</p>
<p>2. OMP_PROC_BIND. Set this to "true" to pin the threads down during program execution. By default, threads may migrate from one core to another, depending on the load on the node. In an HPC setting, it is generally advisable to pin the threads to avoid delays caused by thread migration.</p>
<p>3. OMP_PLACES. Set this to "cores" if you want to pin the threads to physical cores, or to "threads" if you want to use hyperthreading. </p>
<p>The effect of each setting is illustrated below. In this experiment we measured the execution time twice of the finite difference code <a href="https://github.com/pletzer/fidibench" target="_self">upwindCxx -numCells 256 -numSteps 10.</a> The code was built with the gimpi/2018b toolchain on Mahuika.</p>
<table style="height: 146px;" width="737">
<tbody>
<tr>
<td style="width: 181px;">Number of physical cores</td>
<td style="width: 181px;">--hint not used, OMP_PROC_BIND and OMP_PLACES unset</td>
<td style="width: 181px;">
<p>--hint=<span class="wysiwyg-color-red">no</span>multithread</p>
<p>OMP_PROC_BIND=true</p>
<p> OMP_PLACES=<span class="wysiwyg-color-red">cores</span></p>
</td>
<td style="width: 181px;">
<p>--hint=multithread</p>
<p>OMP_PROC_BIND=true</p>
<p> OMP_PLACES=<span class="wysiwyg-color-red">threads</span></p>
</td>
</tr>
<tr>
<td style="width: 181px;">1</td>
<td style="width: 181px;">1m43s, 1m42s</td>
<td style="width: 181px;">1m42s, 1m42s</td>
<td style="width: 181px;">1m30s, 1m30s</td>
</tr>
<tr>
<td style="width: 181px;">2</td>
<td style="width: 181px;">1m30s, 1m31s</td>
<td style="width: 181px;">1m03, 55s</td>
<td style="width: 181px;">56s, 56s</td>
</tr>
<tr>
<td style="width: 181px;">4</td>
<td style="width: 181px;"><strong><span class="wysiwyg-color-red">58s, 1m27s</span></strong></td>
<td style="width: 181px;"><strong><span class="wysiwyg-color-blue90">45s, 41s</span></strong></td>
<td style="width: 181px;"><strong><span class="wysiwyg-color-green110">27s, 28s</span></strong></td>
</tr>
<tr>
<td style="width: 181px;">8</td>
<td style="width: 181px;">24s, 27s</td>
<td style="width: 181px;">18s, 17s</td>
<td style="width: 181px;">16s, 16s</td>
</tr>
</tbody>
</table>
<h2 id="h_01H92B46P2B7G8CF0B5E1AC4VT"> </h2>
<h2 id="h_01H92B46P2SERC08GM742KD9YB">Results</h2>
<p>In the default case, --hint was not used and the environment variables OMP_PROC_BIND and OMP_PLACES were not set. Significant variations of execution times are sometimes observed due to the random placement of threads, which may or may not share a physical core. </p>
<p>The third column shows the settings for the case with no multithreading. The fourth column places 2 threads per physical cores (i.e. OMP_NUM_THREADS = 2 times the number of physical cores) and this often gives the best performance.</p>
<h2 id="h_01H92B46P2RFFF3DWTYMABFERV"> Bottom line</h2>
<p>Be explicit by using --hint and setting OMP_PROC_BIND and OMP_PLACES. In many cases we expect one of the following to work best:</p>
<table style="height: 50px;" width="688">
<tbody>
<tr>
<td style="width: 168px;">1 thread per core</td>
<td style="width: 169px;">--hint=nomultithread</td>
<td style="width: 169px;">OMP_PROC_BIND=true</td>
<td style="width: 169px;">OMP_PLACES=cores</td>
</tr>
<tr>
<td style="width: 168px;">2 threads per core</td>
<td style="width: 169px;">--hint=multithread</td>
<td style="width: 169px;">OMP_PROC_BIND=true</td>
<td style="width: 169px;">OMP_PLACES=threads</td>
</tr>
</tbody>
</table>
<p>Let us know if you find other settings to work better for you.</p>