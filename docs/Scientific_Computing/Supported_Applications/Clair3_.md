---
created_at: '2022-08-10T21:31:45Z'
hidden: false
label_names: []
position: 3
title: 'Clair3 '
vote_count: 0
vote_sum: 0
zendesk_article_id: 5292628239375
zendesk_section_id: 360000040076
---



[//]: <> (REMOVE ME IF PAGE VALIDATED)
[//]: <> (vvvvvvvvvvvvvvvvvvvv)
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

<h1 id="description"><span>Description</span></h1>
<p dir="auto"><a href="https://github.com/HKU-BAL/Clair3" target="_self">Clair3 homepage</a></p>
<p dir="auto">Clair3 is a germline small variant caller for long-reads. Clair3 makes the best of two major method categories: pileup calling handles most variant candidates with speed, and full-alignment tackles complicated candidates to maximize precision and recall. Clair3 runs fast and has superior performance, especially at lower coverage. Clair3 is simple and modular for easy deployment and integration.</p>
<p dir="auto">Clair3 is the 3<sup>rd</sup> generation of <a href="https://github.com/HKU-BAL/Clair">Clair</a> (the 2<sup>nd</sup>) and <a href="https://github.com/aquaskyline/Clairvoyante">Clairvoyante</a> (the 1<sup>st</sup>).</p>
<p dir="auto">A short pre-print describing Clair3's algorithms and results is at <a href="https://www.biorxiv.org/content/10.1101/2021.12.29.474431v1" rel="nofollow">bioRxiv</a>.</p>
<p dir="auto"> </p>
<h1 id="license_and_disclaimer">License and Disclaimer</h1>
<p dir="auto">Copyright 2021 The University of Hong Kong, Department of Computer Science</p>
<p dir="auto">Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:</p>
<ol dir="auto">
<li>
<p dir="auto">Re-distributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.</p>
</li>
<li>
<p dir="auto">Re-distributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.</p>
</li>
<li>
<p dir="auto">Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.</p>
</li>
</ol>
<pre> </pre>
<h2 class="highlight highlight-source-shell notranslate position-relative overflow-auto">Example Slurm script</h2>
<p dir="auto"><strong>Caution</strong>: Absolute path is needed for both <code>INPUT_DIR</code> and <code>OUTPUT_DIR</code><span class="pl-c"><br><br><br></span></p>
<pre>#!/bin/bash -e<br><br>#SBATCH --account       nesi12345<br>#SBATCH --job-name      cliar3_job<br>#SBATCH --mem           6G #12G is just a place holder. Adjust accordingly<br>#SBATCH --cpus-per-task 4 #4 just a place holder. Adjust accordingly<br>#SBATCH --time          01:00:00<br>#SBATCH --output        slurmout.%j.out<br><br><br>#Caution: Absolute path is needed for both INPUT_DIR and OUTPUT_DIR<br><br>INPUT_DIR=/path/to/input/data         # e.g. /nesi/nobackup/nesi12345/input (absolute path needed)<br>OUTPUT_DIR=/path/to/save/outputs      # /nesi/nobackup/nesi12345/output (absolute path needed)<br>REF=/path/to/reference/genomes        # use the suggested Slurm variable which will read the value from `--cpus-per-task`<br>MODEL_NAME=/model/name                # e.g. r941_prom_hac_g360+g422<br><br><br>module purge<br>module load Clair3/0.1.12-Miniconda3<br><br>run_clair3.sh \<br>--bam_fn=${INPUT_DIR} \<br>--ref_fn=${REF} \<br>--threads=$SLURM_CPUS_PER_TASK \<br>--platform=ont \<br>--model_path=${CONDA_PREFIX}/bin/models/${MODEL_NAME} \<br>--output=${OUTPUT_DIR} --enable_phasing<br><br></pre>
<p dir="auto"><span class="pl-c"><br><br><br><br></span></p>
<p dir="auto"><code></code></p>