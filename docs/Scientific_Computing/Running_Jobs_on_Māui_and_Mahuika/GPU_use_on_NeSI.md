---
created_at: '2020-04-19T22:59:58Z'
hidden: false
label_names:
- gpu
position: 3
title: GPU use on NeSI
vote_count: 0
vote_sum: 0
zendesk_article_id: 360001471955
zendesk_section_id: 360000030876
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <p>This page provides generic information about how to access NeSI's GPU cards.</p>
<p>For application specific settings (e.g. OpenMP, Tensorflow on GPU, ...), please have a look at the dedicated pages listed at the end of this page.</p>
<blockquote class="blockquote-prereq">
<h3 id="prerequisites">Important</h3>
<p>An overview of available GPU cards is available in the <a href="https://support.nesi.org.nz/hc/en-gb/articles/4963040656783" target="_blank" rel="noopener">Available GPUs on NeSI</a> support page.</p>
<p>Details about<span class="diff-removed-string"> </span>GPU cards for each system<span class="diff-removed-string"> </span>and <span class="diff-added-string">usage</span> limits are in the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000204076" target="_blank" rel="noopener">Mahuika Slurm Partitions</a> and <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000204116#_Toc514341606" target="_blank" rel="noopener">Māui_Ancil (CS500) Slurm Partitions</a> support pages.</p>
<p>Details about pricing in terms of compute units can be found in the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001385735" target="_self">What is an allocation?</a> page.</p>
</blockquote>
<h1>Request GPU resources using Slurm</h1>
<p>To request a GPU for your <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000684396-Submitting-your-first-job" target="_self">Slurm job</a>, add the following option at the beginning of your submission script:</p>
<pre><code>#SBATCH --gpus-per-node=1</code></pre>
<p>You can specify the type and number of GPU you need using the following syntax</p>
<pre><code>#SBATCH --gpus-per-node=&lt;gpu_type&gt;:&lt;gpu_number&gt;</code></pre>
<p>If not specified, the default GPU type is <code>P100</code>. For some types of GPU, you also need to specify a partition. Here is a summary of typical use cases:</p>
<ul>
<li>
<p>1 P100 GPU on Mahuika</p>
<pre><code>#SBATCH --gpus-per-node=P100:1</code></pre>
</li>
<li>
<p>1 P100 GPU on Māui Ancillary Nodes</p>
<pre><code>#SBATCH --partition=nesi_gpu
#SBATCH --gpus-per-node=1
</code></pre>
</li>
<li>
<p>2 P100 GPUs per node on Mahuika</p>
<pre><code>#SBATCH --gpus-per-node=P100:2</code></pre>
<p><em>You cannot ask for more than 2 P100 GPU per node on Mahuika.</em></p>
</li>
<li>
<p>1 A100 (40GB) GPU on Mahuika</p>
<pre><code>#SBATCH --gpus-per-node=A100:1</code></pre>
</li>
<li>
<p>2 A100 (40GB) GPUs on Mahuika</p>
<pre><code>#SBATCH --gpus-per-node=A100:2</code></pre>
<p><em>You cannot ask for more than 2 A100 (40GB) GPUs per node on Mahuika.</em></p>
</li>
<li>
<p>1 A100-1g.5gb GPU on Mahuika</p>
<pre><code>#SBATCH --gpus-per-node=A100-1g.5gb:1</code></pre>
<p><em>This type of GPU is limited to 1 job per user and recommended for development and debugging.</em></p>
</li>
<li>
<p>1 A100 (80GB) GPU on Mahuika</p>
<pre><code>#SBATCH --partition=hgx
#SBATCH --gpus-per-node=A100:1</code></pre>
<p><em>These GPUs are on Milan nodes, check the <a href="https://support.nesi.org.nz/knowledge/articles/6367209795471/" target="_self">dedicated support page</a> for more information.</em></p>
</li>
<li>
<p>4 A100 (80GB &amp; NVLink) GPU on Mahuika</p>
<pre><code>#SBATCH --partition=hgx
#SBATCH --gpus-per-node=A100:4</code></pre>
<p><em>These GPUs are on Milan nodes, check the <a href="https://support.nesi.org.nz/knowledge/articles/6367209795471/" target="_self">dedicated support page</a> for more information.</em></p>
<p><em>You cannot ask for more than 4 A100 (80GB) GPUs per node on Mahuika.</em></p>
</li>
<li>
<p>1 A100 GPU on Mahuika, regardless of the type</p>
<pre><code>#SBATCH --partition=gpu,hgx
#SBATCH --gpus-per-node=A100:1</code></pre>
<p><em>With this configuration, your job will spend less time in the queue, using whichever A100 GPU is available. It may land on a regular Mahuika node (A100 40GB GPU) or on a Milan node (A100 80GB GPU).</em></p>
</li>
</ul>
<p>You can also use the <code>--gpus-per-node</code>option in <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001316356" target="_self" rel="undefined">Slurm interactive sessions</a>, with the <code>srun</code> and <code>salloc</code> commands. For example:</p>
<pre>srun --job-name "InteractiveGPU" --gpus-per-node 1 --cpus-per-task 8 --mem 2GB --time 00:30:00 --pty bash</pre>
<p>will request and then start a bash session with access to a GPU, for a duration of 30 minutes.</p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Important</h3>
When you use the <code>--gpus-per-node</code>option, Slurm automatically sets the <code>CUDA_VISIBLE_DEVICES</code> environment variable inside your job environment to list the index/es of the allocated GPU card/s on each node.
<pre>$ srun --job-name "GPUTest" --gpus-per-node=P100:2 --time 00:05:00 --pty bash
srun: job 20015016 queued and waiting for resources
srun: job 20015016 has been allocated resources
$ echo $CUDA_VISIBLE_DEVICES
0,1
</pre>
</blockquote>
<h1>Load CUDA and cuDNN modules</h1>
<p>To use an Nvidia GPU card with your application, you need to load the driver and the CUDA toolkit via the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001113076-The-HPC-environment-" target="_self">environment modules</a> mechanism:</p>
<pre>module load CUDA/11.0.2</pre>
<p>You can list the available versions using:</p>
<pre>module spider CUDA</pre>
<p>Please contact us at <a href="mailto:support@nesi.org.nz">support@nesi.org.nz</a> if you need a version not available on the platform.</p>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>On Māui Ancillary Nodes, use <code>module avail CUDA</code> to list available versions.</p>
</blockquote>
<p>The CUDA module also provides access to additional command line tools:</p>
<ul>
<ul>
<ul>
<li>
<a href="https://developer.nvidia.com/nvidia-system-management-interface" target="_self"><strong>nvidia-smi</strong></a> to directly monitor GPU resource utilisation,</li>
<li>
<a href="https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html" target="_self"><strong>nvcc </strong></a>to compile CUDA programs,</li>
<li>
<a href="https://docs.nvidia.com/cuda/cuda-gdb/index.html" target="_self"><strong>cuda-gdb</strong></a> to debug CUDA applications.</li>
</ul>
</ul>
</ul>
<p>In addition, the <a href="https://developer.nvidia.com/cudnn" target="_self">cuDNN</a> (NVIDIA CUDA® Deep Neural Network library) library is accessible via its dedicated module:</p>
<pre>module load cuDNN/8.0.2.39-CUDA-11.0.2</pre>
<p>which will automatically load the related CUDA version. Available versions can be listed using:</p>
<pre>module spider cuDNN</pre>
<h1>Example Slurm script</h1>
<p>The following Slurm script illustrates a minimal example to request a GPU card, load the CUDA toolkit and query some information about the GPU:</p>
<pre>#!/bin/bash -e<br>#SBATCH --job-name=GPUJob   # job name (shows up in the queue)<br>#SBATCH --time=00-00:10:00  # Walltime (DD-HH:MM:SS)<br>#SBATCH --gpus-per-node=1   # GPU resources required per node<br>#SBATCH --cpus-per-task=2   # number of CPUs per task (1 by default)<br>#SBATCH --mem=512MB         # amount of memory per node (1 by default)<br><br># load CUDA module<br>module purge<br>module load CUDA/11.0.2<br><br># display information about the available GPUs<br>nvidia-smi<br><br># check the value of the CUDA_VISIBLE_DEVICES variable<br>echo "CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES}"</pre>
<p>Save this in a <code>test_gpu.sl</code> file and submit it using:</p>
<pre>sbatch test_gpu.sl</pre>
<p>The content of job output file would look like:</p>
<pre>$ cat slurm-20016124.out

The following modules were not unloaded:
   (Use "module --force purge" to unload all):

  1) slurm   2) NeSI
Wed May 12 12:08:27 2021
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.32.03    Driver Version: 460.32.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla P100-PCIE...  On   | 00000000:05:00.0 Off |                    0 |
| N/A   29C    P0    23W / 250W |      0MiB / 12198MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
CUDA_VISIBLE_DEVICES=0
</pre>
<blockquote class="blockquote-tip">
<h3 id="prerequisites">Note</h3>
<p>CUDA_VISIBLE_DEVICES=0 indicates that this job was allocated to CUDA GPU index 0 on this node. It is not a count of allocated GPUs.</p>
</blockquote>
<h1>NVIDIA Nsight Systems and Compute profilers</h1>
<p><a href="https://developer.nvidia.com/nsight-systems" target="_self">Nsight Systems</a> is a system-wide analysis tool, particularly good for profiling CPU-GPU interactions. It is provided on Mahuika via the <code>Nsight-Systems</code> module:</p>
<pre>$ module load Nsight-Systems/2020.5.1<br>Load `PyQt/5.12.1-gimkl-2020a-Python-3.8.2` module prior to running `nsys-ui`<br>$ nsys --version<br>NVIDIA Nsight Systems version 2020.5.1.85-5ee086b</pre>
<p>This module gives you access to the <a href="https://docs.nvidia.com/nsight-systems/UserGuide/index.html#cli-profiling" target="_self" rel="undefined">nsys</a> command line tool or the <a href="https://docs.nvidia.com/nsight-systems/UserGuide/index.html#gui-profiling" target="_self">nsys-ui</a> graphical interface.</p>
<p><a href="https://developer.nvidia.com/nsight-compute" target="_self">Nsight Compute</a> is a profiler for CUDA kernels. It is accessible on Mahuika using the <code>Nsight-Compute</code> module:</p>
<pre>$ module load Nsight-Compute/2020.3.0<br>Load `PyQt/5.12.1-gimkl-2020a-Python-3.8.2` module prior to running `nsys-ui`<br>$ ncu --version<br>NVIDIA (R) Nsight Compute Command Line Profiler<br>Copyright (c) 2018-2020 NVIDIA Corporation<br>Version 2020.3.0.0 (build 29307467) (public-release)</pre>
<p>Then you can use the <a href="https://docs.nvidia.com/nsight-compute/NsightComputeCli/" target="_self" rel="undefined">ncu</a> command line tool or the <a href="https://docs.nvidia.com/nsight-compute/NsightCompute/index.html" target="_self" rel="undefined">ncu-ui</a> graphical interface.</p>
<blockquote class="blockquote-warning">
<h3 id="prerequisites">Important</h3>
The <code>nsys-ui</code> and <code>ncu-ui</code> tools require access to a display server, either via <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001075975-X11-on-NeSI" target="_self">X11</a> or a <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001600235-Virtual-Desktop-via-Jupyter-on-NeSI" target="_self" rel="undefined">Virtual Desktop</a>. You also need to load the <code>PyQt</code> module beforehand:
<pre>module load PyQt/5.12.1-gimkl-2020a-Python-3.8.2
module load Nsight-Systems/2020.5.1
nsys-ui  # this will work only if you have a graphical session
</pre>
</blockquote>
<h1>Application and toolbox specific support pages</h1>
<p>The following pages provide additional information for supported applications:</p>
<ul>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/212457807-ABAQUS#gpus" target="_self">ABAQUS</a></li>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360000792856-GROMACS#nvidia_gpu_container" target="_self">GROMACS</a></li>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360002558216-Lambda-Stack" target="_self">Lambda Stack </a></li>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/212639047-MATLAB#GPU" target="_self">Matlab</a></li>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360000990436-TensorFlow-on-GPUs" target="_self">TensorFlow on GPUs </a></li>
</ul>
<p>And programming toolkits:</p>
<ul>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360001127856-Offloading-to-GPU-with-OpenMP-" target="_self" rel="undefined">Offloading to GPU with OpenMP </a></li>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360001131076-Offloading-to-GPU-with-OpenACC-using-the-Cray-compiler" target="_self">Offloading to GPU with OpenACC using the Cray compiler </a></li>
<li><a href="https://support.nesi.org.nz/hc/en-gb/articles/360001500156-NVIDIA-GPU-Containers" target="_self">NVIDIA GPU Containers </a></li>
</ul>