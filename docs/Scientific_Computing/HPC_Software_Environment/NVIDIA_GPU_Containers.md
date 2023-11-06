---
created_at: '2020-04-30T01:28:34Z'
hidden: false
label_names: []
position: 7
title: NVIDIA GPU Containers
vote_count: 2
vote_sum: 2
zendesk_article_id: 360001500156
zendesk_section_id: 360000040056
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<p>NVIDIA provides access to GPU accelerated software through their NGC container registry: <a href="https://www.nvidia.com/en-us/gpu-cloud/containers/">https://www.nvidia.com/en-us/gpu-cloud/containers/</a>.</p>
<p class="wysiwyg-indent1"><em>NGC offers a comprehensive catalog of GPU-accelerated software for deep learning, machine learning, and HPC. NGC containers deliver powerful and easy-to-deploy software proven to deliver the fastest results. By taking care of the plumbing, NGC enables users to focus on building lean models, producing optimal solutions and gathering faster insights.</em></p>
<p>Many of these containers are able to run under Singularity, which is supported on the NeSI platform. NVIDIA also specifies the GPU requirements for each container, i.e. whether it will run on our Pascal (sm60) GPUs.</p>
<p>There are instructions for converting their Docker images to Singularity images on the NVIDIA site but some small changes are required to these instructions on NeSI. As an example, here we show the steps required for running the NAMD image on NeSI, based on the NVIDIA instructions here: <a href="https://ngc.nvidia.com/catalog/containers/hpc:namd">https://ngc.nvidia.com/catalog/containers/hpc:namd</a>.</p>
<ol>
<li>Download the APOA1 benchmark data:
<ul>
<li>
<pre>wget -O - https://gitlab.com/NVHPC/ngc-examples/raw/master/namd/3.0/get_apoa1.sh | bash<br>cd apoa1</pre>
</li>
</ul>
</li>
<li>
<span style="font-weight: 400;">Load the Singularity module:</span>
<ul>
<li>
<pre><span style="font-weight: 400;">module load Singularity</span></pre>
</li>
</ul>
</li>
<li>
<span style="font-weight: 400;">Build the Singularity image. This step differs from the NVIDIA instructions because instead of using "build" we "pull" the image directly, which does not require root access:</span>
<ul>
<li>Please do refer  "<a href="https://support.nesi.org.nz/hc/en-gb/articles/360001107916-Singularity#build_environment_variables" target="_self">Build Environment Variables</a>" prior to running the following <code>pull</code> command</li>
<li>
<pre><span style="font-weight: 400;">singularity pull namd-3.0-alpha9-singlenode.sif docker://nvcr.io/hpc/namd:3.0-alpha9-singlenode</span></pre>
</li>
</ul>
</li>
<li>
<span style="font-weight: 400;">Copy the following into a Slurm script named <em>run.sl</em>:</span>
<ul>
<li>
<pre>#!/bin/bash -e<br><br>#SBATCH --job-name=namdgpu<br>#SBATCH --time=00:10:00<br>#SBATCH --ntasks=1<br>#SBATCH --cpus-per-task=8<br>#SBATCH --gpus-per-node P100:1<br>#SBATCH --mem=1G<br><br>module purge<br>module load Singularity<br><br># name of the NAMD input file, tag, etc<br>NAMD_INPUT=<span class="pl-s"><span class="pl-pds">"apoa1_nve_cuda.namd</span><span class="pl-pds">"<br>NAMD_SIF="<span style="font-weight: 400;">namd-3.0-alpha9-singlenode.sif</span>"<br>NAMD_EXE=namd3</span></span><br><br><span class="pl-c">#</span> singularity command with required arguments<br>SINGULARITY=<span class="pl-s"><span class="pl-pds">"s</span>ingularity exec --nv -B <span class="pl-pds">$(</span>pwd<span class="pl-pds">)</span>:/host_pwd </span>--pwd /host_pwd ${NAMD_SIF}<span class="pl-pds">"<br><span class="pl-s"><br><span class="pl-c">#</span> run NAMD<br><span class="pl-smi">${SINGULARITY}</span> ${NAMD_EXE} +ppn <span class="pl-smi">${SLURM_CPUS_PER_TASK}</span> +idlepoll <span class="pl-smi">${NAMD_INPUT}</span></span></span></pre>
</li>
</ul>
</li>
<li>Submit the job:
<ul>
<li>
<pre>sbatch run.sl</pre>
</li>
</ul>
</li>
<li>View the standard output from the simulation in the Slurm .out file.</li>
</ol>
<p> We expect similar steps to work for other NGC containers.</p>