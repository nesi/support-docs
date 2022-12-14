---
created_at: '2021-08-25T02:05:42Z'
hidden: false
label_names: []
position: 0
title: 'Profiler: VTune'
vote_count: 0
vote_sum: 0
zendesk_article_id: 4405523725583
zendesk_section_id: 360000278935
---

##  

##  What is VTune?  

VTune is a **performance** analysis tool.  
It can be used to identify and **analyse** various aspects in both
serial and parallel programs and can be used for both OpenMP and MPI
applications.  
It can be used with a command line interface (**CLI**) or a graphical
user interface (**GUI**).  
  
  

 

## Where to find more resources on VTune?  

-   Main page is at
    [https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/vtune-profiler.html](https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/vtune-profiler.html#gs.bjani9)
-   Tutorials are available at
    <https://software.intel.com/content/www/us/en/develop/articles/vtune-tutorials.html>

##  

##  How to use VTune?

  
VTune is available on Mahuika by loading the VTune **module**.

    $ module spider VTune
    Versions:
    VTune/2019_update4
    VTune/2019_update8

First login to Mahuika and then run:

    module load VTune

To use the VTune amplifier command line tool help run:

    amplxe-cl -help

##  

##  How do I profile an application with VTune?  

The hotspot analysis is the most commonly used analysis and generally
the first approach to optimizing an application.

-   Example on Mahuika with the matrix sample.  
    The matrix sample is composed of a pre-built matrix in C++ for
    matrix multiplication.

<!-- -->

    $ ml VTune/2019_update8
    $ cp -r /opt/nesi/mahuika/VTune/2019_update8/samples_2019/en/vtune_amplifier/C++/matrix .
    $ cd matrix
    $ amplxe-cl -collect hotspots ./matrix

  
The **amplxe-cl** command collects hotspots data.

The option **collect** specifies the collection experiment to run.  
The option **hotspots** is to collect basic hotspots to have a general
performance overview.  
  
This is the type of output you are going to get:

    $ amplxe-cl -collect hotspots ./matrix
    amplxe: Collection started. To stop the collection, either press CTRL-C or enter from another console window: amplxe-cl -r /scale_wlg_persistent/filesets/home/asav179/o/matrix/r000hs -command stop.
    Addr of buf1 = 0x2aaab8e08010
    Offs of buf1 = 0x2aaab8e08180
    Addr of buf2 = 0x2aaabae09010
    Offs of buf2 = 0x2aaabae091c0
    Addr of buf3 = 0x2aaabce0a010
    Offs of buf3 = 0x2aaabce0a100
    Addr of buf4 = 0x2aaabee0b010
    Offs of buf4 = 0x2aaabee0b140
    Threads #: 16 Pthreads
    Matrix size: 2048
    Using multiply kernel: multiply1
    Freq = 2.101000 GHz
    Execution time = 2.515 seconds
    amplxe: Collection stopped.
    amplxe: Using result path `/scale_wlg_persistent/filesets/home/asav179/o/matrix/r000hs'
    amplxe: Executing actions 19 % Resolving information for `libpthread.so.0'
    amplxe: Warning: Cannot locate debugging information for file `/lib64/libpthread.so.0'.
    amplxe: Executing actions 19 % Resolving information for `matrix'
    amplxe: Warning: Cannot locate debugging information for file `/lib64/libc.so.6'.
    amplxe: Executing actions 75 % Generating a report Elapsed Time: 2.552s
    CPU Time: 36.440s
    Effective Time: 36.440s
    Idle: 0s
    Poor: 36.440s
    Ok: 0s
    Ideal: 0s
    Over: 0s
    Spin Time: 0s
    Overhead Time: 0s
    Total Thread Count: 17
    Paused Time: 0s
    Top Hotspots
    Function Module CPU Time
    --------- ------ --------
    multiply1 matrix 36.420s
    init_arr matrix 0.010s
    init_arr matrix 0.010s
    Effective Physical Core Utilization: 85.4% (30.750 out of 36)
    Effective Logical Core Utilization: 46.1% (33.194 out of 72)
    | The metric value is low, which may signal a poor utilization of logical
    | CPU cores while the utilization of physical cores is acceptable. Consider
    | using logical cores, which in some cases can improve processor throughput
    | and overall performance of multi-threaded applications.
    Collection and Platform Info
    Application Command Line: ./matrix
    Operating System: 3.10.0-693.2.2.el7.x86_64 NAME="CentOS Linux" VERSION="7 (Core)" ID="centos" ID_LIKE="rhel fedora" VERSION_ID="7" PRETTY_NAME="CentOS Linux 7 (Core)" ANSI_COLOR="0;31" CPE_NAME="cpe:/o:centos:centos:7" HOME_URL="https://www.centos.org/" BUG_REPORT_URL="https://bugs.centos.org/" CENTOS_MANTISBT_PROJECT="CentOS-7" CENTOS_MANTISBT_PROJECT_VERSION="7" REDHAT_SUPPORT_PRODUCT="centos" REDHAT_SUPPORT_PRODUCT_VERSION="7"
    Computer Name: mahuika01
    Result Size: 3 MB
    Collection start time: 05:35:42 15/09/2021 UTC
    Collection stop time: 05:35:45 15/09/2021 UTC
    Collector Type: Event-based counting driver,User-mode sampling and tracing
    CPU
    Name: Intel(R) Xeon(R) Processor code named Broadwell
    Frequency: 2.095 GHz
    Logical CPU Count: 72
    amplxe: Executing actions 100 % done

The output one receives the overall elapsed and idle times as well as
the CPU times of the individual functions in descending order (list of
hotspots).  
The utilization of the CPUs is also analyzed and judged.

###  

### <span class="wysiwyg-underline">Note:</span>

You can run the VTune GUI via Jupyter+VDT to visualise profiling
results.

1.  First launch VDT then open a terminal and cd to directory.
2.  Then run:

<!-- -->

    module load VTune
    amplxe-gui --path-to-open <vtune_result_dir>

 
