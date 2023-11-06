---
created_at: '2022-12-08T00:55:40Z'
hidden: false
label_names: []
position: 0
title: Build an Apptainer container on a Milan compute node
vote_count: 0
vote_sum: 0
zendesk_article_id: 6008779241999
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>This article describes a technique to build <a href="https://apptainer.org/" target="_blank" rel="noopener">Apptainer</a> containers using <a href="https://support.nesi.org.nz/hc/en-gb/articles/6367209795471" target="_self">Milan compute nodes</a>, via a Slurm job. You can also build <a href="https://support.nesi.org.nz/hc/en-gb/articles/360001107916" target="_blank" rel="noopener">Singularity</a> container using this technique.<span></span></p>
<h1 id="h_01HBS2PZYBSKYKSDS6JG37VQPJ">Building container via Slurm</h1>
<p>The new Milan compute nodes can be used to build Apptainer containers using the <a href="https://apptainer.org/docs/user/main/fakeroot.html" target="_blank" rel="noopener">fakeroot feature</a>. This functionality is only available on these nodes at the moment due to their operating system version.</p>
<p>To illustrate this functionality, create an example container definition file <code>my_container.def</code> from a shell session on NeSI as follows:</p>
<pre><code>cat &lt;&lt; EOF &gt; my_container.def
BootStrap: docker
From: ubuntu:20.04
%post
    apt-get -y update
    apt-get install -y wget
EOF
</code></pre>
<p>Then submit the following Slurm job submission script to build the container:</p>
<pre><code>#!/bin/bash -e
#SBATCH --job-name=apptainer_build
#SBATCH --partition=milan
#SBATCH --time=0-00:30:00
#SBATCH --mem=4GB
#SBATCH --cpus-per-task=2
<br># load environment module<br>module purge
module load Apptainer/1.2.2<br><br># recent Apptainer modules set APPTAINER_BIND, which typically breaks<br># container builds, so unset it here<br>unset APPTAINER_BIND<br><br># create a build and cache directory on nobackup storage<br>export APPTAINER_CACHEDIR="/nesi/nobackup/$SLURM_JOB_ACCOUNT/$USER/apptainer_cache"
export APPTAINER_TMPDIR="/nesi/nobackup/$SLURM_JOB_ACCOUNT/$USER/apptainer_tmpdir"
mkdir -p $APPTAINER_CACHEDIR $APPTAINER_TMPDIR
setfacl -b $APPTAINER_TMPDIR<br><br># build the container
apptainer build --force --fakeroot my_container.sif my_container.def
</code></pre>
<p>Note this script will start an Slurm job for 30 minutes using 2 cores and 4 GB of memory to build the image. Make sure to set these resources correctly, some containers can take hours to build and require tens of GB of memory.</p>
<p>Option --force will rebuild my_container.sif even if it already is in the directory.</p>
<p>More information about how to submit a Slurm job is available in the <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000684396" target="_blank" rel="noopener">Submitting your first job</a> support page.</p>
<blockquote class="blockquote-tip">
<h3 id="llama-tip">Build environment variables</h3>
<p>To build containers, you need to ensure that Apptainer has enough storage space to create intermediate files. It also requires a cache folder to save images pulled from a different location (e.g. DockerHub). By default both of these locations are set to <code>/tmp</code> which has limited space, large builds may exceed this limitation causing the builder to crash. The environment variables <code>APPTAINER_TMPDIR</code> and <code>APPTAINER_CACHEDIR</code> are used to overwrite the default location of these directories.</p>
<p>In this example, the Slurm job submission script creates these folders using your project <code>nobackup</code> folder.</p>
</blockquote>
<h1 id="h_01HBS2PZYBH5FNMXA8KPDW4XY3">Known limitations</h1>
<p>If your container uses RPM to install packages, i.e. is based on CentOS or Rocky Linux, you need to disable the <code>APPTAINER_TMPDIR</code> environment variable (use <code>unset APPTAINER_TMPDIR</code>) and request more memory for your Slurm job. Otherwise, RPM will crash due to an incompatibility with the <code>nobackup</code> filesystem.</p>
<p>If you encounter the following error when using a base Docker image in your Apptainer definition file</p>
<pre><code>While making image from oci registry: error fetching image to cache: while building SIF from layers: conveyor failed to get: unsupported image-specific operation on artifact with type "application/vnd.docker.container.image.v1+json"</code></pre>
<p>it is likely due to an upstream issue (e.g. bad image on Dockerhub). In this case, try an older image version or a different base image.</p>
<blockquote class="blockquote-warning">
<h3 id="h_01HBS2PZYBG8ZYH7J24VHVVBGW">Other limitations</h3>
<p>This method, using fakeroot, is known to <strong>not</strong> work for all types of Apptainer/Singularity containers.</p>
<p>If you encounter an issue, please contact us at <a href="mailto:support@nesi.org.nz">support@nesi.org.nz</a>.</p>
</blockquote>