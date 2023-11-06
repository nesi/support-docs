---
created_at: '2020-02-24T20:26:39Z'
hidden: false
label_names: []
position: 8
title: Configuring Dask-MPI jobs
vote_count: 2
vote_sum: 2
zendesk_article_id: 360001392636
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<blockquote class="blockquote-warning">
<h3 id="octopus-warning">Start simple</h3>
<p>The technique explained in this page should be considered <strong>after</strong> trying simpler single node options (e.g.  <a href="https://docs.dask.org/en/stable/deploying-python.html" target="_blank" rel="noopener">Dask Distributed LocalCluster</a>), if</p>
<ul>
<li>you need more cores than what is available on a single node,</li>
<li>or your queuing time is too long.</li>
</ul>
<p>Note that using MPI to distribute computations on multiple nodes can have an impact on performances, compared to a single node setting.</p>
</blockquote>
<p><a href="https://dask.org/" target="_self">Dask</a> is a popular Python package for parallelising workflows. It can use a variety of parallelisation backends, including Python multiprocessing and multithreading. A separate <a href="https://mpi.dask.org" target="_self">Dask-MPI</a> package is provided for distributed high-performance computation using the <a href="https://en.wikipedia.org/wiki/Message_Passing_Interface" target="_self">MPI</a> (Message Passing Interface) backend, which can achieve scalability across many nodes and integrates well into an HPC environment.</p>
<p>Installing the Dask-MPI package and configuring jobs requires careful consideration to work reliably and efficiently. Internally it relies on the <a href="https://github.com/mpi4py/mpi4py" target="_self">mpi4py</a> package that provides an interface to the MPI library. MPI itself is implemented by different freely available distributions, including MPICH and OpenMPI, as well as a variety of vendor-specific distributions, such as Intel MPI and Cray MPI.</p>
<p>While some of the MPI distributions should be compatible with each other, it is advisable to use the same MPI distribution as the host HPC system for reliability. The Mahuika and Māui Ancil clusters use Intel MPI.</p>
<h1 id="h_3e6b313b-a712-4e88-8246-5550cac1d77c">Using Dask-MPI on Mahuika</h1>
<p>Dask-MPI can be readily used with the more recent Python modules available on Mahuika that come with the mpi4py package, e.g.</p>
<pre><code>module load Python/3.9.9-gimkl-2020a</code></pre>
<h1 id="h_3e6b313b-a712-4e88-8246-5550cac1d77c">Installing Dask-MPI with Conda on Mahuika and Māui Ancil</h1>
<p>Load an Anaconda3 or Miniconda3 module and use the following commands to install mpi4py with the Intel MPI distribution <em>before</em> installing the Dask-MPI package:</p>
<pre>conda install -c intel mpi4py<br>conda install -c conda-forge dask-mpi</pre>
<p>If you use an environment file, add the <code>intel</code> channel at the end of the list (so that it will not take priority over other channels) and request mpi4py with the Intel MPI distribution as follows:</p>
<pre><code>name: myenvironment
channels:
  - myfavouritechannel
  - intel
dependencies:
  - mypackage
  - anotherpackage
  - intel::mpi4py
  - dask-mpi</code></pre>
<blockquote class="blockquote-tip">
<h3 id="llama-tip">See also</h3>
<p>See the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001580415" target="_self">Miniconda3</a> page for more information on how to create and manage Miniconda environments on NeSI.</p>
</blockquote>
<h1 id="h_75b008cc-7843-40b2-bdb4-8252ca807fab">Configuring Slurm</h1>
<p>At runtime, Slurm will launch a number of Python processes as requested in the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000691716" target="_self">Slurm configuration script</a>. Each process is given an ID (or "rank") starting at rank 0. Dask-MPI then assigns different roles to the different ranks:</p>
<ul>
<li>Rank 0 becomes the scheduler that coordinates work and communication</li>
<li>Rank 1 becomes the worker that executes the main Python program and hands out workloads</li>
<li>Ranks 2 and above become additional workers that run workloads</li>
</ul>
<p>This implies that <strong>Dask-MPI jobs must be launched on at least 3 MPI ranks!</strong> Ranks 0 and 1 often perform much less work than the other ranks, it can therefore be beneficial to use <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000568236" target="_self">Hyperthreading</a> to place these two ranks onto a single physical core. Ensure that activating hyperthreading does not slow down the worker ranks by running a short test workload with and without hyperthreading.</p>
<p>In the following, two cases will be discussed:</p>
<ol>
<li>The worker ranks use little memory and they do not use parallelisation themselves</li>
<li>The worker ranks use a lot of memory and/or parallelisation</li>
</ol>
<p>Note that Slurm will place different MPI ranks on different nodes on the HPC by default - this has the advantage of much reduced queuing times as Slurm can use gaps in node utilisation, and this should not affect performance, unless individual work items are very small (e.g., if a given work item only takes a few seconds or less to run).</p>
<h2>Dask workers have low memory usage and no parallelisation</h2>
<p>This case is straightforward to set up. Use the following example to run a workload with 1 scheduler rank and 6 worker ranks. Each rank will be given 1 GB of memory and a single (logical) core.</p>
<pre><code>#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --ntasks=6
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G

module purge
module load Python/3.9.9-gimkl-2020a

srun python mydaskprogram.py</code></pre>
<h2>Dask workers have high memory usage and/or parallelisation</h2>
<p>This case is more complex to set up and uses Slurm "job packs" to handle the heterogeneous configuration. In the following example, the scheduler and first worker rank will be given 1 GB of memory and a single (logical) core each, while the remaining worker ranks will be given 4*3 GB = 12 GB of memory and 4 (logical) cores per rank.</p>
<pre><code>#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --ntasks=2 --mem-per-cpu=1G --cpus-per-task=1
#SBATCH hetjob
#SBATCH --ntasks=3 --mem-per-cpu=3G --cpus-per-task=4

module purge
module load Python/3.9.9-gimkl-2020a

srun --het-group=0-1 python mydaskprogram.py</code></pre>
<p>The <code>--het-group</code> flag asks <code>srun</code> to launch both job packs together.</p>
<h1>Example</h1>
<p>The following example illustrates how to run Dask-MPI on the HPC. It is based on the Dask Futures tutorial on the <a href="https://examples.dask.org" target="_self">Dask examples</a> webpage.</p>
<h2>Python program</h2>
<pre><code>import os
import dask_mpi as dm
import dask.distributed as dd

# Initialise Dask cluster and store worker files in current work directory
dm.initialize(local_directory=os.getcwd())

# Define two simple test functions
def inc(x):
    return x + 1

def add(x, y):
    return x + y

client = dd.Client()

# Submit chain of computations using futures
a = client.submit(inc, 1)
b = client.submit(inc, 2)
c = client.submit(add, a, b)

# Expect the same answer
print("Dask result:", c.result())
print("Local result:", add(inc(1), inc(2)))</code></pre>
<h2>Slurm script</h2>
<p>Replace <code>PROJECTID</code> with your project ID number and use the <code>sbatch</code> command to submit this Slurm script and run the test code on 3 MPI ranks:</p>
<pre><code>#!/bin/bash
#SBATCH --account=PROJECTID
#SBATCH --time=00:01:00
#SBATCH --ntasks=3
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=512M

module purge
module load Python/3.9.9-gimkl-2020a

srun python dask_example.py</code></pre>
<p>The Slurm output file should contain some status information from Dask-MPI, along with program output</p>
<pre>Dask result: 5<br>Local result: 5</pre>
<h1>Running Dask-MPI inside a Singularity container</h1>
<p>It is straightforward to run a Dask-MPI workload inside a Singularity container on the HPC. For reliable and efficient execution it is best to use the same MPI distribution inside and outside the container. This restricts choices to Intel MPI on the Mahuika and Māui Ancil clusters; see section <a href="#h_3e6b313b-a712-4e88-8246-5550cac1d77c" target="_self">Installing Dask-MPI with Conda</a> above for instructions. It will also reduce container portability between platforms that use different MPI distributions.</p>
<h2>Container configuration</h2>
<p>While it is impossible to cover every possible scenario, the following guidelines should help with configuring the container correctly.</p>
<ol>
<li>Make sure that the Intel MPI version of the "mpi4py" package is installed with Dask-MPI</li>
<li>The correct version of Python and the Intel MPI distribution need to be loaded at runtime.</li>
</ol>
<p>Here is an example of a minimal Singularity container definition file:</p>
<pre><code>Bootstrap: docker
From: continuumio/miniconda3:latest

%post
    conda install -y -n base -c intel mpi4py
    conda install -y -n base -c conda-forge dask-mpi

%runscript
    . $(conda info --base)/etc/profile.d/conda.sh
    conda activate base
    python "$@"
</code></pre>
<p>where the <code>%runscript</code> section ensures that the Python script passed to <code>singularity run</code> is executed using the Python interpreter of the base Conda environment inside the container.</p>
<blockquote class="blockquote-tip">
<h3 id="llama-tip">Tips</h3>
<p>You can build this container on NeSI, using the Mahuika Extension nodes, following the instructions from the <a href="https://support.nesi.org.nz/hc/en-gb/articles/6008779241999" target="_blank" rel="noopener">dedicated support page</a>.</p>
</blockquote>
<h2>Slurm configuration</h2>
<p>Slurm configuration is identical to the case without Singularity, see section <a href="#h_75b008cc-7843-40b2-bdb4-8252ca807fab" target="_self">Configuring Slurm</a> above. The Slurm job submission script needs to be slightly modified to setup and launch the container runtime environment, ensuring that Intel MPI finds Slurm's PMI-2 library on the host.</p>
<p>In the first case with low worker memory consumption and no parallelisation, use for example</p>
<pre><code>module load Singularity
export I_MPI_PMI_LIBRARY="/opt/slurm/lib64/libpmi2.so"
export SINGULARITY_BIND="/opt/slurm/lib64"
srun singularity run my_container.sif dask_example.py</code></pre>
<p>In the second case with high worker memory consumption and/or parallelisation, use for example</p>
<pre><code>module load Singularity<br>export I_MPI_PMI_LIBRARY="/opt/slurm/lib64/libpmi2.so"
export SINGULARITY_BIND="/opt/slurm/lib64"
srun --het-group=0-1 singularity run my_container.sif dask_example.py</code></pre>
<p><em>Note: You may need to append more folders to <code>SINGULARITY_BIND</code> to make your script accessible in the container, e.g. <code>$PWD</code></em></p>