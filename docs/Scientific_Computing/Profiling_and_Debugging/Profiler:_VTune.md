---
created_at: '2021-08-25T02:05:42Z'
hidden: false
label_names: []
position: 0
title: 'Profiler: VTune'
vote_count: 1
vote_sum: -1
zendesk_article_id: 4405523725583
zendesk_section_id: 360000278935
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <h2> </h2>
<h2>
<br>What is VTune?<br><br>
</h2>
<p>VTune is a <strong>performance</strong> analysis tool.<br>It can be used to identify and <strong>analyse</strong> various aspects in both serial and parallel programs and can be used for both OpenMP and MPI applications.<br>It can be used with a command line interface (<strong>CLI</strong>) or a graphical user interface (<strong>GUI</strong>).<br><br><br></p>
<p> </p>
<h2>Where to find more resources on VTune?<br><br>
</h2>
<ul>
<li>Main page is at <a href="https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/vtune-profiler.html#gs.bjani9">https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/vtune-profiler.html</a>
</li>
<li>Tutorials are available at <a href="https://software.intel.com/content/www/us/en/develop/articles/vtune-tutorials.html">https://software.intel.com/content/www/us/en/develop/articles/vtune-tutorials.html</a>
</li>
</ul>
<h2> </h2>
<h2>
<br>How to use VTune?</h2>
<p><br>VTune is available on Mahuika by loading the VTune <strong>module</strong>.</p>
<pre>$ module spider VTune<br>Versions:<br>VTune/2019_update4<br>VTune/2019_update8</pre>
<p>First login to Mahuika and then run:</p>
<pre>module load VTune</pre>
<p>To use the VTune amplifier command line tool help run:</p>
<pre>amplxe-cl -help</pre>
<h2> </h2>
<h2>
<br>How do I profile an application with VTune?<br><br>
</h2>
<p>The hotspot analysis is the most commonly used analysis and generally the first approach to optimizing an application.</p>
<ul>
<li>Example on Mahuika with the matrix sample.<br>The matrix sample is composed of a pre-built matrix in C++ for matrix multiplication.</li>
</ul>
<pre>$ ml VTune/2019_update8<br>$ cp -r /opt/nesi/mahuika/VTune/2019_update8/samples_2019/en/vtune_amplifier/C++/matrix .<br>$ cd matrix<br>$ amplxe-cl -collect hotspots ./matrix<span></span></pre>
<p><br>The <strong>amplxe-cl</strong> command collects hotspots data.</p>
<p>The option <strong>collect</strong> specifies the collection experiment to run.<br>The option <strong>hotspots</strong> is to collect basic hotspots to have a general performance overview.<br><br>This is the type of output you are going to get:</p>
<pre>$ amplxe-cl -collect hotspots ./matrix<br>amplxe: Collection started. To stop the collection, either press CTRL-C or enter from another console window: amplxe-cl -r /scale_wlg_persistent/filesets/home/asav179/o/matrix/r000hs -command stop.<br>Addr of buf1 = 0x2aaab8e08010<br>Offs of buf1 = 0x2aaab8e08180<br>Addr of buf2 = 0x2aaabae09010<br>Offs of buf2 = 0x2aaabae091c0<br>Addr of buf3 = 0x2aaabce0a010<br>Offs of buf3 = 0x2aaabce0a100<br>Addr of buf4 = 0x2aaabee0b010<br>Offs of buf4 = 0x2aaabee0b140<br>Threads #: 16 Pthreads<br>Matrix size: 2048<br>Using multiply kernel: multiply1<br>Freq = 2.101000 GHz<br>Execution time = 2.515 seconds<br>amplxe: Collection stopped.<br>amplxe: Using result path `/scale_wlg_persistent/filesets/home/asav179/o/matrix/r000hs'<br>amplxe: Executing actions 19 % Resolving information for `libpthread.so.0'<br>amplxe: Warning: Cannot locate debugging information for file `/lib64/libpthread.so.0'.<br>amplxe: Executing actions 19 % Resolving information for `matrix'<br>amplxe: Warning: Cannot locate debugging information for file `/lib64/libc.so.6'.<br>amplxe: Executing actions 75 % Generating a report Elapsed Time: 2.552s<br>CPU Time: 36.440s<br>Effective Time: 36.440s<br>Idle: 0s<br>Poor: 36.440s<br>Ok: 0s<br>Ideal: 0s<br>Over: 0s<br>Spin Time: 0s<br>Overhead Time: 0s<br>Total Thread Count: 17<br>Paused Time: 0s<br>Top Hotspots<br>Function Module CPU Time<br>--------- ------ --------<br>multiply1 matrix 36.420s<br>init_arr matrix 0.010s<br>init_arr matrix 0.010s<br>Effective Physical Core Utilization: 85.4% (30.750 out of 36)<br>Effective Logical Core Utilization: 46.1% (33.194 out of 72)<br>| The metric value is low, which may signal a poor utilization of logical<br>| CPU cores while the utilization of physical cores is acceptable. Consider<br>| using logical cores, which in some cases can improve processor throughput<br>| and overall performance of multi-threaded applications.<br>Collection and Platform Info<br>Application Command Line: ./matrix<br>Operating System: 3.10.0-693.2.2.el7.x86_64 NAME="CentOS Linux" VERSION="7 (Core)" ID="centos" ID_LIKE="rhel fedora" VERSION_ID="7" PRETTY_NAME="CentOS Linux 7 (Core)" ANSI_COLOR="0;31" CPE_NAME="cpe:/o:centos:centos:7" HOME_URL="https://www.centos.org/" BUG_REPORT_URL="https://bugs.centos.org/" CENTOS_MANTISBT_PROJECT="CentOS-7" CENTOS_MANTISBT_PROJECT_VERSION="7" REDHAT_SUPPORT_PRODUCT="centos" REDHAT_SUPPORT_PRODUCT_VERSION="7"<br>Computer Name: mahuika01<br>Result Size: 3 MB<br>Collection start time: 05:35:42 15/09/2021 UTC<br>Collection stop time: 05:35:45 15/09/2021 UTC<br>Collector Type: Event-based counting driver,User-mode sampling and tracing<br>CPU<br>Name: Intel(R) Xeon(R) Processor code named Broadwell<br>Frequency: 2.095 GHz<br>Logical CPU Count: 72<br>amplxe: Executing actions 100 % done</pre>
<p>The output one receives the overall elapsed and idle times as well as the CPU times of the individual functions in descending order (list of hotspots).<br>The utilization of the CPUs is also analyzed and judged.</p>
<h3> </h3>
<h3><span class="wysiwyg-underline">Note:</span></h3>
<p><span>You can run the VTune GUI via Jupyter+VDT to visualise profiling results.</span></p>
<ol>
<li><span>First launch VDT then open a terminal and cd to directory.</span></li>
<li><span>Then run:</span></li>
</ol>
<pre><span>module load VTune<br>amplxe-gui --path-to-open &lt;vtune_result_dir&gt;</span></pre>
<p> </p>