---
created_at: '2023-03-21T09:33:04Z'
hidden: false
label_names: []
position: 0
title: Dorado
vote_count: 2
vote_sum: 2
zendesk_article_id: 6623692647951
zendesk_section_id: 360000040076
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <h1 id="description"><span>Description</span></h1>
<p dir="auto">Dorado is a high-performance, easy-to-use, open source basecaller for Oxford Nanopore reads.</p>
<h2 id="01H8FPNKQRBXFRE1RZGQQW75FD" dir="auto" tabindex="-1">
<a id="user-content-features" class="anchor" href="https://github.com/nanoporetech/dorado#features" aria-hidden="true"></a>Features</h2>
<ul dir="auto">
<li>One executable with sensible defaults, automatic hardware detection and configuration.</li>
<li>Nvidia GPUs including multi-GPU with linear scaling.</li>
<li>Modified basecalling (Remora models).</li>
<li>Duplex basecalling.</li>
<li>
<a href="https://github.com/nanoporetech/pod5-file-format">POD5</a><span> </span>support for highest basecalling performance.</li>
<li>Based on libtorch, the C++ API for pytorch.</li>
<li>Multiple custom optimisations in CUDA and Metal for maximising inference performance.</li>
</ul>
<h1 id="license_and_disclaimer">License and Disclaimer</h1>
<p dir="auto">(c) 2022 Oxford Nanopore Technologies Ltd.</p>
<p dir="auto">Dorado is distributed under the terms of the Oxford Nanopore Technologies, Ltd. Public License, v. 1.0. If a copy of the License was not distributed with this file, You can obtain one at<span> </span><a href="http://nanoporetech.com/" rel="nofollow">http://nanoporetech.com</a></p>
<p dir="auto">.</p>
<h2 id="example_slurm_script">Example Slurm script</h2>
<ul>
<li>The following Slurm script is a template to run Basecalling on the NVIDIA A100 GPUs. We do not recommend running Dorado jobs on CPUs.</li>
<li>
<span></span><code>--device 'cuda:all'</code><span> </span>will automatically pick up the GPU over CPU</li>
<li>We are not providing the models as part of the module yet. </li>
</ul>
<pre>#!/bin/bash -e<br><br>#SBATCH --account        nesi12345<br>#SBATCH --job-name       dorado<br>#SBATCH --gpus-per-node  A100:1<br>#SBATCH --mem            6G<br>#SBATCH --cpus-per-task  4<br>#SBATCH --time           00:10:00<br><span class="pl-c">#SBATCH --output         slurmout.%j.out</span><br><br>module purge<br>module load Dorado/0.3.4<br><br>dorado download --model dna_r10.4.1_e8.2_400bps_hac@v4.1.0<br><br>dorado basecaller  --device 'cuda:all' dna_r10.4.1_e8.2_400bps_hac@v4.1.0 pod5s/ &gt; calls.bam</pre>