---
created_at: '2021-08-17T03:13:55Z'
hidden: false
label_names: []
position: 6
title: AlphaFold
vote_count: 2
vote_sum: 2
zendesk_article_id: 4405170961039
zendesk_section_id: 360000040076
---


    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    [//]: <> (vvvvvvvvvvvvvvvvvvvv)
    !!! Info
        This page has been automatically migrated and may contain formatting errors.
    [//]: <> (^^^^^^^^^^^^^^^^^^^^)
    [//]: <> (REMOVE ME IF PAGE VALIDATED)
    <blockquote class="blockquote-tip">
<h3 id="llama-tip">Tips</h3>
<p><span>An extended version of AlphaFold2 on NeSI Mahuika cluster which contains additional information such as visualisation of AlphaFold outputs, etc <a href="https://nesi.github.io/alphafold2-on-mahuika/" target="_self">can be found here</a></span></p>
</blockquote>
<h1><span>Description</span></h1>
<p><span>This package provides an implementation of the inference pipeline of AlphaFold v2.0. This is a completely new model that was entered in CASP14 and published in Nature. For simplicity, we refer to this model as AlphaFold throughout the rest of this document.</span><span></span></p>
<p><span>Any publication that discloses findings arising from using this source code or the model parameters should <a href="https://github.com/deepmind/alphafold#citing-this-work">cite</a> the <a href="https://doi.org/10.1038/s41586-021-03819-2" rel="nofollow">AlphaFold paper</a>. Please also refer to the <a href="https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-03819-2/MediaObjects/41586_2021_3819_MOESM1_ESM.pdf" rel="nofollow">Supplementary Information</a> for a detailed description of the method.</span></p>
<p>Home page is at <a href="https://github.com/deepmind/alphafold">https://github.com/deepmind/alphafold</a> </p>
<h1>License and Disclaimer</h1>
<p>This is not an officially supported Google product.</p>
<p>Copyright 2021 DeepMind Technologies Limited.</p>
<h2>
<a id="user-content-alphafold-code-license" class="anchor" href="https://github.com/deepmind/alphafold#alphafold-code-license" aria-hidden="true"></a>AlphaFold Code License</h2>
<p>Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at<span> </span><a href="https://www.apache.org/licenses/LICENSE-2.0" rel="nofollow">https://www.apache.org/licenses/LICENSE-2.0</a>.</p>
<p>Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.</p>
<h2>
<a id="user-content-model-parameters-license" class="anchor" href="https://github.com/deepmind/alphafold#model-parameters-license" aria-hidden="true"></a>Model Parameters License</h2>
<p>The AlphaFold parameters are made available for non-commercial use only, under the terms of the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license. You can find details at:<span> </span><a href="https://creativecommons.org/licenses/by-nc/4.0/legalcode" rel="nofollow">https://creativecommons.org/licenses/by-nc/4.0/legalcode</a></p>
<h1>AlphaFold Databases</h1>
<p>AlphaFold databases are stored in <span><code>/opt/nesi/db/alphafold_db/</code>  parent directory. In order to make the database calling more convenient, we have prepared modules for each version of the database. Running <code>module spider AlphaFold2DB</code> will list the available versions based on when they were downloaded (Year-Month)</span></p>
<pre>$ module spider AlphaFold2DB<br><br>--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------<br>AlphaFold2DB: AlphaFold2DB/2022-06<br>--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------<br>Description:<br>AlphaFold2 databases<br><br> Versions:<br>         AlphaFold2DB/2022-06<br>         AlphaFold2DB/2023-04<br><br></pre>
<h2> </h2>
<p>Loading a module will set the <span><code>$AF2DB</code></span> variable which is pointing to the  selected version of the database. For an example. </p>
<pre>$ module load AlphaFold2DB/2023-04<br><br>$ echo $AF2DB <br>/opt/nesi/db/alphafold_db/2023-04</pre>
<h1>AlphaFold module ( &gt;= 2.3.2)</h1>
<p>As of version 2.3.2 of AlphaFold, we recommend deploying AlphaFold via the module (previous versoions were done via a Singularity container )</p>
<h2>Example Slurm script for monomer</h2>
<p>Input <em>fasta</em> used in following example  is 3RGK (<a href="https://www.rcsb.org/structure/3rgk" rel="nofollow">https://www.rcsb.org/structure/3rgk</a>).</p>
<pre>#!/bin/bash -e<br><br>#SBATCH --account       nesi12345<br>#SBATCH --job-name      af-2.3.2-monomer<br>#SBATCH --mem           24G<br>#SBATCH --cpus-per-task 8<br>#SBATCH --gpus-per-node P100:1<br>#SBATCH --time          02:00:00<br>#SBATCH --output        %j.out<br><br>module purge<br>module load AlphaFold2DB/2023-04<br>module load AlphaFold/2.3.2<br><br>INPUT=/nesi/project/nesi12345/alphafold/input_data<br>OUTPUT=/nesi/project/nesi12345/alphafold/results<br><br>run_alphafold.py --use_gpu_relax \<br>--data_dir=$AF2DB \<br>--uniref90_database_path=$AF2DB/uniref90/uniref90.fasta \<br>--mgnify_database_path=$AF2DB/mgnify/mgy_clusters_2022_05.fa \<br>--bfd_database_path=$AF2DB/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \<br>--uniref30_database_path=$AF2DB/uniref30/UniRef30_2021_03 \<br>--pdb70_database_path=$AF2DB/pdb70/pdb70 \<br>--template_mmcif_dir=$AF2DB/pdb_mmcif/mmcif_files \<br>--obsolete_pdbs_path=$AF2DB/pdb_mmcif/obsolete.dat \<br>--model_preset=monomer \<br>--max_template_date=2022-6-1 \<br>--db_preset=full_dbs \<br>--output_dir=$OUTPUT \<br>--fasta_paths=${INPUT}/rcsb_pdb_3GKI.fasta</pre>
<h2>Example Slurm script for multimer</h2>
<p>Input <em>fasta</em> used in following example</p>
<pre>&gt;T1083<br>GAMGSEIEHIEEAIANAKTKADHERLVAHYEEEAKRLEKKSEEYQELAKVYKKITDVYPNIRSYMVLHYQNLTRRYKEAAEENRALAKLHHELAIVED<br>&gt;T1084<br>MAAHKGAEHHHKAAEHHEQAAKHHHAAAEHHEKGEHEQAAHHADTAYAHHKHAEEHAAQAAKHDAEHHAPKPH</pre>
<pre>#!/bin/bash -e<br><br>#SBATCH --account       nesi12345<br>#SBATCH --job-name      af-2.3.2-multimer<br>#SBATCH --mem           30G<br>#SBATCH --cpus-per-task 4<br>#SBATCH --gpus-per-node P100:1<br>#SBATCH --time          01:45:00<br>#SBATCH --output        slurmout.%j.out<br><br>module purge<br>module load AlphaFold2DB/2023-04<br>module load AlphaFold/2.3.2<br><br>INPUT=/nesi/project/nesi12345/input_data<br>OUTPUT=/nesi/project/nesi12345/alphafold/2.3_multimer<br><br>run_alphafold.py \<br>--use_gpu_relax \<br>--data_dir=$AF2DB \<br>--model_preset=multimer \<br>--uniprot_database_path=$AF2DB/uniprot/uniprot.fasta \<br>--uniref90_database_path=$AF2DB/uniref90/uniref90.fasta \<br>--mgnify_database_path=$AF2DB/mgnify/mgy_clusters_2022_05.fa \<br>--bfd_database_path=$AF2DB/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \<br>--uniref30_database_path=$AF2DB/uniref30/UniRef30_2021_03 \<br>--pdb_seqres_database_path=$AF2DB/pdb_seqres/pdb_seqres.txt \<br>--template_mmcif_dir=$AF2DB/pdb_mmcif/mmcif_files \<br>--obsolete_pdbs_path=$AF2DB/pdb_mmcif/obsolete.dat \<br>--max_template_date=2022-6-1 \<br>--db_preset=full_dbs \<br>--output_dir=${OUTPUT} \<br>--fasta_paths=${INPUT}/test_multimer.fasta</pre>
<h1>AlphaFold Singularity container (prior to v2.3.2)</h1>
<p>If you would like to use a version prior to 2.3.2, It can be done via the Singularity containers. </p>
<p>We prepared a Singularity container image based on the <a href="https://hub.docker.com/r/catgumag/alphafold" target="_self">official Dockerfile</a> with some modifications. Image (.<em>simg</em>) and the corresponding definition file (<em>.def</em>) are stored in<span> <code>/opt/nesi/containers/AlphaFold/</code></span></p>
<h2>
<a id="user-content-example-slurm-script" class="anchor" href="https://github.com/DininduSenanayake/alphafold/tree/main/AlphaFold_Mahuika_instructions#example-slurm-script" aria-hidden="true"></a>Example Slurm scripts for Singularity container based AF2 deployment</h2>
<h3>Monomer<span class="wysiwyg-underline"></span>
</h3>
<pre>#!/bin/bash -e<br><br>#SBATCH --account       nesi12345<br>#SBATCH --job-name      alphafold2_monomer_example<br>#SBATCH --mem           30G<br>#SBATCH --cpus-per-task 6<br>#SBATCH --gpus-per-node P100:1 <br>#SBATCH --time          02:00:00<br>#SBATCH --output        slurmout.%j.out<br><br>module purge<br>module load AlphaFold2DB/2022-06<br>module load cuDNN/8.1.1.33-CUDA-11.2.0 Singularity/3.9.8<br><br>INPUT=/path/to/input_data<br>OUTPUT=/path/to/results<br><br>export SINGULARITY_BIND="$INPUT,$OUTPUT,$AF2DB"<br><br>singularity exec --nv /opt/nesi/containers/AlphaFold/alphafold_2.2.0.simg python /app/alphafold/run_alphafold.py \<br>--use_gpu_relax \<br>--data_dir=$AF2DB \<br>--uniref90_database_path=$AF2DB/uniref90/uniref90.fasta \<br>--mgnify_database_path=$AF2DB/mgnify/mgy_clusters_2018_12.fa \<br>--bfd_database_path=$AF2DB/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \<br>--uniclust30_database_path=$AF2DB/uniclust30/uniclust30_2018_08/uniclust30_2018_08 \<br>--pdb70_database_path=$AF2DB/pdb70/pdb70 \<br>--template_mmcif_dir=$AF2DB/pdb_mmcif/mmcif_files \<br>--obsolete_pdbs_path=$AF2DB/pdb_mmcif/obsolete.dat \<br>--model_preset=monomer \<br>--max_template_date=2022-1-1 \<br>--db_preset=full_dbs \<br>--output_dir=$OUTPUT \<br>--fasta_paths=$INPUT/rcsb_pdb_3GKI.fasta</pre>
<p> </p>
<h3>Multimer</h3>
<pre>#!/bin/bash -e<br><br>#SBATCH --account       nesi12345<br>#SBATCH --job-name      alphafold2_monomer_example<br>#SBATCH --mem           30G<br>#SBATCH --cpus-per-task 6<br>#SBATCH --gpus-per-node P100:1 <br>#SBATCH --time          02:00:00<br>#SBATCH --output        slurmout.%j.out<br><br>module purge<br>module load AlphaFold2DB/2022-06<br>module load cuDNN/8.1.1.33-CUDA-11.2.0 Singularity/3.9.8<br><br>INPUT=/path/to/input_data<br>OUTPUT=/path/to/results<br><br><br>export SINGULARITY_BIND="$INPUT,$OUTPUT,$AF2DB"<br><br>singularity exec --nv /opt/nesi/containers/AlphaFold/alphafold_2.2.0.simg python /app/alphafold/run_alphafold.py \<br>--use_gpu_relax \<br>--data_dir=$AF2DB \<br>--uniref90_database_path=$AF2DB/uniref90/uniref90.fasta \<br>--mgnify_database_path=$AF2DB/mgnify/mgy_clusters_2018_12.fa \<br>--bfd_database_path=$AF2DB/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \<br>--uniclust30_database_path=$AF2DB/uniclust30/uniclust30_2018_08/uniclust30_2018_08 \<br><strong>--pdb_seqres_database_path=$AF2DB/pdb_seqres/pdb_seqres.txt \</strong><br>--template_mmcif_dir=$AF2DB/pdb_mmcif/mmcif_files \<br>--obsolete_pdbs_path=$AF2DB/pdb_mmcif/obsolete.dat \<br>--uniprot_database_path=$AF2DB/uniprot/uniprot.fasta \<br><strong>--model_preset=multimer \</strong><br>--max_template_date=2022-1-1 \<br>--db_preset=full_dbs \<br>--output_dir=$OUTPUT \<br>--fasta_paths=$INPUT/rcsb_pdb_3GKI.fasta</pre>
<h3> </h3>
<h3 id="h_01G0ZDA2HNWJ1DV8VJSN2J0GV0">Explanation of Slurm variables and Singularity flags</h3>
<ol>
<li>Values for<span> </span><code>--mem</code><span> </span>,<span> </span><code>--cpus-per-task</code><span> </span>and<span> </span><code>--time</code><span> </span>Slurm variables are for<span> </span><em>3RGK.fasta</em>. Adjust them accordingly</li>
<li>We have tested this on both P100 and A100 GPUs where the runtimes were identical. Therefore, the above example was set to former via<span> </span><code>P100:1</code>
</li>
<li>The<span> </span><code>--nv</code><span> </span>flag enables GPU support.</li>
<li>
<code>--pwd /app/alphafold</code><span> </span>is to workaround this<span> </span><a href="https://github.com/deepmind/alphafold/issues/32">existing issue</a>
</li>
</ol>
<h3> </h3>
<h2>AlphaFold2 : Initial Release ( this version does not support <span><code>multimer</code></span>)</h2>
<p>Input <em>fasta</em> used in following example and subsequent benchmarking is 3RGK (<a href="https://www.rcsb.org/structure/3rgk" rel="nofollow">https://www.rcsb.org/structure/3rgk</a>).</p>
<div class="highlight highlight-source-shell position-relative">
<pre><span class="pl-c">#!/bin/bash -e</span>

<span class="pl-c">#SBATCH --account           nesi12345</span>
<span class="pl-c">#SBATCH --job-name          alphafold2</span>
<span class="pl-c">#SBATCH --mem               20G</span>
<span class="pl-c">#SBATCH --cpus-per-task     8</span>
<span class="pl-c">#SBATCH --gpus-per-node     P100:1</span>
<span class="pl-c">#SBATCH --time              01:20:00</span>
<span class="pl-c">#SBATCH --output            slurmout.%j.out</span>

module purge<br>module load AlphaFold2DB/2022-06
module load cuDNN/8.1.1.33-CUDA-11.2.0 Singularity/3.8.0

image=/opt/nesi/containers/AlphaFold/2021-10-07
database=$AF2DB

<span class="pl-k">export</span> SINGULARITY_BIND=<span class="pl-s"><span class="pl-pds">"</span><span class="pl-smi">$PWD</span>:/etc,<span class="pl-smi">$image</span>,/path/to/input/data:/var/inputdata,/path/to/outputs:/var/outputdata,<span class="pl-smi">$database</span>:/db<span class="pl-pds">"</span></span>

singularity run --pwd /app/alphafold --nv <span class="pl-smi">$image</span>/alphafold_2.0.1.simg python /app/alphafold/run_alphafold.py \
--fasta_paths=/var/inputdata/3RGK.fasta \
--output_dir=/var/outputdata \
--model_names=model_1 \
--preset=casp14 \
--max_template_date=2020-05-14 \
--data_dir=/db \
--uniref90_database_path=/db/uniref90/uniref90.fasta \
--mgnify_database_path=/db/mgnify/mgy_clusters_2018_12.fa \
--uniclust30_database_path=/db/uniclust30/uniclust30_2018_08/uniclust30_2018_08 \
--bfd_database_path=/db/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
--pdb70_database_path=/db/pdb70/pdb70 \
--template_mmcif_dir=/db/pdb_mmcif/mmcif_files \
--obsolete_pdbs_path=/db/pdb_mmcif/obsolete.dat</pre>
</div>
<h3> </h3>
<h1>Troubleshooting</h1>
<ul>
<li>If you are to encounter the message "<em>RuntimeError: Resource exhausted: Out of memory</em>" , add the following variables to the slurm script</li>
</ul>
<p>For module based runs </p>
<pre>export TF_FORCE_UNIFIED_MEMORY=1
export XLA_PYTHON_CLIENT_MEM_FRACTION=4.0</pre>
<p>For Singularity based runs </p>
<pre>export SINGULARITYENV_TF_FORCE_UNIFIED_MEMORY=1 <br>export SINGULARITYENV_XLA_PYTHON_CLIENT_MEM_FRACTION=4.0</pre>