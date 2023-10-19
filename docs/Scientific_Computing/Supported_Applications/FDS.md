---
created_at: '2019-02-14T23:33:05Z'
hidden: false
label_names:
- mahuika
- engineering
position: 28
title: FDS
vote_count: 0
vote_sum: 0
zendesk_article_id: 360000759275
zendesk_section_id: 360000040076
---


[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)
<p>FDS (Fire Dynamics Simulator) was developed by the National Institute of Standards and Technology (NIST) for large-eddy simulation (LES) of low-speed flows, with an emphasis on smoke and heat transport from fires.</p>
<p>General documentation can be found <a href="https://github.com/firemodels/fds/releases/download/FDS6.7.1/FDS_User_Guide.pdf" target="_self">here</a>.</p>
<p>FDS can utilise both <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000690275-SLURM-Parallel-Execution#t_mpi">MPI</a> and <a href="https://support.nesi.org.nz/hc/en-gb/articles/360000690275-SLURM-Parallel-Execution#t_multi">OpenMP</a></p>
<h3>Example Script</h3>
<pre><code>#!/bin/bash -e

#SBATCH --time           02:00:00       #Walltime
#SBATCH --ntasks         4              #One task per mesh, NO MORE
#SBATCH --cpus-per-task  2              #More than 4 cpus/task not recommended.
#SBATCH --output         %x.out		#Name output file according to job name
#SBATCH --hint           nomultithread  #Hyperthreading decreases efficiency.

module load FDS/6.7.1-intel-2017a

input="/nesi/project/nesi99999/path/to/input.fds"

srun fds ${input}
</code></pre>
<h1>Recommendations</h1>
<ul>
<li>FDS will run in Hybrid Parallel, but will be less efficient that full MPI using the same number of CPUs.</li>
<li>MPI if the preferable method of scaling, if you can partition your mesh more you should do that before considering multi-threading (OpenMP). e.g. <code>ntasks=2, cpus-per-task=1</code> is preferable to <code>ntasks=1, cpus-per-task=2</code>
</li>
<li>Each mesh should have it's own task, assigning more tasks than there are meshes will cause an error.</li>
<li>Multi-threading efficiency drops off significantly after 4 physical cores. <code>--cpus-per-task 4</code>
</li>
<li>Hyper-threading is not recommended. Set <code>--hint nomultithread</code>
</li>
</ul>
<h2>Scaling with MPI</h2>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360002454995/mceclip1.png" alt="mceclip1.png"></p>
<h2>Scaling with oMP</h2>
<p><img src="https://support.nesi.org.nz/hc/article_attachments/360002454975/mceclip0.png" alt="mceclip0.png"></p>
<p> </p>
<p> </p>
<p> </p>