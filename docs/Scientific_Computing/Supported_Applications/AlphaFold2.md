Description
===========

This package provides an implementation of the inference pipeline of
AlphaFold v2.0. This is a completely new model that was entered in
CASP14 and published in Nature. For simplicity, we refer to this model
as AlphaFold throughout the rest of this document.

Any publication that discloses findings arising from using this source
code or the model parameters
should [cite](https://github.com/deepmind/alphafold#citing-this-work) the [AlphaFold
paper](https://doi.org/10.1038/s41586-021-03819-2). Please also refer to
the [Supplementary
Information](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-03819-2/MediaObjects/41586_2021_3819_MOESM1_ESM.pdf) for
a detailed description of the method.

Home page is at <https://github.com/deepmind/alphafold> 

License and Disclaimer
======================

This is not an officially supported Google product.

Copyright 2021 DeepMind Technologies Limited.

[](https://github.com/deepmind/alphafold#alphafold-code-license){#user-content-alphafold-code-license .anchor}AlphaFold Code License
------------------------------------------------------------------------------------------------------------------------------------

Licensed under the Apache License, Version 2.0 (the \"License\"); you
may not use this file except in compliance with the License. You may
obtain a copy of the License
at <https://www.apache.org/licenses/LICENSE-2.0>.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an \"AS IS\" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[](https://github.com/deepmind/alphafold#model-parameters-license){#user-content-model-parameters-license .anchor}Model Parameters License
------------------------------------------------------------------------------------------------------------------------------------------

The AlphaFold parameters are made available for non-commercial use only,
under the terms of the Creative Commons Attribution-NonCommercial 4.0
International (CC BY-NC 4.0) license. You can find details
at: <https://creativecommons.org/licenses/by-nc/4.0/legalcode>

AlphaFold Databases
-------------------

There are eight reference databases (parameters) where all of them are
downloaded, verified and stored in NeSI filesystem
 `/opt/nesi/db/alphafold_db` .

::: {.highlight .highlight-source-shell .position-relative}
    $ /opt/nesi/db/alphafold_db/
    ├── bfd
    ├── mgnify
    ├── params
    ├── pdb70
    ├── pdb_mmcif
    ├── small_bfd
    ├── uniclust30
    └── uniref90
:::

Singularity container
---------------------

We prepared a Singularity container image based on the official
Dockerfile with some modifications. Image (.*simg*) and the
corresponding definition file (*.def*) are stored in
`/opt/nesi/containers/AlphaFold/2021-10-07`

[](https://github.com/DininduSenanayake/alphafold/tree/main/AlphaFold_Mahuika_instructions#example-slurm-script){#user-content-example-slurm-script .anchor}Example Slurm script
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Input *fasta* used in following example and subsequent benchmarking is
3RGK (<https://www.rcsb.org/structure/3rgk>).

::: {.highlight .highlight-source-shell .position-relative}
    #!/bin/bash -e

    #SBATCH --account           nesi12345
    #SBATCH --job-name          alphafold2
    #SBATCH --mem               20G
    #SBATCH --cpus-per-task     8
    #SBATCH --gpus-per-node     P100:1
    #SBATCH --time              01:20:00
    #SBATCH --output            slurmout.%j.out

    module purge
    module load cuDNN/8.1.1.33-CUDA-11.2.0 Singularity/3.8.0

    image=/opt/nesi/containers/AlphaFold/2021-10-07
    database=/opt/nesi/db/alphafold_db

    export SINGULARITY_BIND="$PWD:/etc,$image,/path/to/input/data:/var/inputdata,/path/to/outputs:/var/outputdata,$database:/db"

    singularity run --pwd /app/alphafold --nv $image/alphafold_2.0.1.simg python /app/alphafold/run_alphafold.py \
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
    --obsolete_pdbs_path=/db/pdb_mmcif/obsolete.dat
:::

###  

### [](https://github.com/DininduSenanayake/alphafold/tree/main/AlphaFold_Mahuika_instructions#explanation-of-slurm-variables-and--singularity-flags){#user-content-explanation-of-slurm-variables-and--singularity-flags .anchor}Explanation of Slurm variables and Singularity flags

1.  Values for `--mem` , `--cpus-per-task` and `--time` Slurm variables
    are for *3RGK.fasta*. Adjust them accordingly
2.  We have tested this on both P100 and A100 GPUs where the runtimes
    were identical. Therefore, the above example was set to former
    via `P100:1`
3.  The `--nv` flag enables GPU support.
4.  `--pwd /app/alphafold` is to workaround this [existing
    issue](https://github.com/deepmind/alphafold/issues/32)
