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
!!! info
    This page has been automatically migrated and may contain formatting errors.
[//]: <> (^^^^^^^^^^^^^^^^^^^^)
[//]: <> (REMOVE ME IF PAGE VALIDATED)

!!! info Tips
>
> An extended version of AlphaFold2 on NeSI Mahuika cluster which
> contains additional information such as visualisation of AlphaFold
> outputs, etc [can be found
> here](https://nesi.github.io/alphafold2-on-mahuika/)

# Description

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

# License and Disclaimer

This is not an officially supported Google product.

Copyright 2021 DeepMind Technologies Limited.

## [](https://github.com/deepmind/alphafold#alphafold-code-license)AlphaFold Code License

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at <https://www.apache.org/licenses/LICENSE-2.0>.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## [](https://github.com/deepmind/alphafold#model-parameters-license)Model Parameters License

The AlphaFold parameters are made available for non-commercial use only,
under the terms of the Creative Commons Attribution-NonCommercial 4.0
International (CC BY-NC 4.0) license. You can find details
at: <https://creativecommons.org/licenses/by-nc/4.0/legalcode>

# AlphaFold Databases

AlphaFold databases are stored in `/opt/nesi/db/alphafold_db/`  parent
directory. In order to make the database calling more convenient, we
have prepared modules for each version of the database. Running
`module spider AlphaFold2DB` will list the available versions based on
when they were downloaded (Year-Month)

    $ module spider AlphaFold2DB

    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    AlphaFold2DB: AlphaFold2DB/2022-06
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Description:
    AlphaFold2 databases

     Versions:
             AlphaFold2DB/2022-06
             AlphaFold2DB/2023-04

##  

Loading a module will set the `$AF2DB` variable which is pointing to
the  selected version of the database. For an example. 

    $ module load AlphaFold2DB/2023-04

    $ echo $AF2DB 
    /opt/nesi/db/alphafold_db/2023-04

# AlphaFold module ( &gt;= 2.3.2)

As of version 2.3.2 of AlphaFold, we recommend deploying AlphaFold via
the module (previous versoions were done via a Singularity container )

## Example Slurm script for monomer

Input *fasta* used in following example  is 3RGK
(<https://www.rcsb.org/structure/3rgk>).

    #!/bin/bash -e

    #SBATCH --account       nesi12345
    #SBATCH --job-name      af-2.3.2-monomer
    #SBATCH --mem           24G
    #SBATCH --cpus-per-task 8
    #SBATCH --gpus-per-node P100:1
    #SBATCH --time          02:00:00
    #SBATCH --output        %j.out

    module purge
    module load AlphaFold2DB/2023-04
    module load AlphaFold/2.3.2

    INPUT=/nesi/project/nesi12345/alphafold/input_data
    OUTPUT=/nesi/project/nesi12345/alphafold/results

    run_alphafold.py --use_gpu_relax \
    --data_dir=$AF2DB \
    --uniref90_database_path=$AF2DB/uniref90/uniref90.fasta \
    --mgnify_database_path=$AF2DB/mgnify/mgy_clusters_2022_05.fa \
    --bfd_database_path=$AF2DB/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
    --uniref30_database_path=$AF2DB/uniref30/UniRef30_2021_03 \
    --pdb70_database_path=$AF2DB/pdb70/pdb70 \
    --template_mmcif_dir=$AF2DB/pdb_mmcif/mmcif_files \
    --obsolete_pdbs_path=$AF2DB/pdb_mmcif/obsolete.dat \
    --model_preset=monomer \
    --max_template_date=2022-6-1 \
    --db_preset=full_dbs \
    --output_dir=$OUTPUT \
    --fasta_paths=${INPUT}/rcsb_pdb_3GKI.fasta

## Example Slurm script for multimer

Input *fasta* used in following example

    >T1083
    GAMGSEIEHIEEAIANAKTKADHERLVAHYEEEAKRLEKKSEEYQELAKVYKKITDVYPNIRSYMVLHYQNLTRRYKEAAEENRALAKLHHELAIVED
    >T1084
    MAAHKGAEHHHKAAEHHEQAAKHHHAAAEHHEKGEHEQAAHHADTAYAHHKHAEEHAAQAAKHDAEHHAPKPH

    #!/bin/bash -e

    #SBATCH --account       nesi12345
    #SBATCH --job-name      af-2.3.2-multimer
    #SBATCH --mem           30G
    #SBATCH --cpus-per-task 4
    #SBATCH --gpus-per-node P100:1
    #SBATCH --time          01:45:00
    #SBATCH --output        slurmout.%j.out

    module purge
    module load AlphaFold2DB/2023-04
    module load AlphaFold/2.3.2

    INPUT=/nesi/project/nesi12345/input_data
    OUTPUT=/nesi/project/nesi12345/alphafold/2.3_multimer

    run_alphafold.py \
    --use_gpu_relax \
    --data_dir=$AF2DB \
    --model_preset=multimer \
    --uniprot_database_path=$AF2DB/uniprot/uniprot.fasta \
    --uniref90_database_path=$AF2DB/uniref90/uniref90.fasta \
    --mgnify_database_path=$AF2DB/mgnify/mgy_clusters_2022_05.fa \
    --bfd_database_path=$AF2DB/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
    --uniref30_database_path=$AF2DB/uniref30/UniRef30_2021_03 \
    --pdb_seqres_database_path=$AF2DB/pdb_seqres/pdb_seqres.txt \
    --template_mmcif_dir=$AF2DB/pdb_mmcif/mmcif_files \
    --obsolete_pdbs_path=$AF2DB/pdb_mmcif/obsolete.dat \
    --max_template_date=2022-6-1 \
    --db_preset=full_dbs \
    --output_dir=${OUTPUT} \
    --fasta_paths=${INPUT}/test_multimer.fasta

# AlphaFold Singularity container (prior to v2.3.2)

If you would like to use a version prior to 2.3.2, It can be done via
the Singularity containers. 

We prepared a Singularity container image based on the [official
Dockerfile](https://hub.docker.com/r/catgumag/alphafold) with some
modifications. Image (.*simg*) and the corresponding definition file
(*.def*) are stored in `/opt/nesi/containers/AlphaFold/`

## [](https://github.com/DininduSenanayake/alphafold/tree/main/AlphaFold_Mahuika_instructions#example-slurm-script)Example Slurm scripts for Singularity container based AF2 deployment

### Monomer

    #!/bin/bash -e

    #SBATCH --account       nesi12345
    #SBATCH --job-name      alphafold2_monomer_example
    #SBATCH --mem           30G
    #SBATCH --cpus-per-task 6
    #SBATCH --gpus-per-node P100:1 
    #SBATCH --time          02:00:00
    #SBATCH --output        slurmout.%j.out

    module purge
    module load AlphaFold2DB/2022-06
    module load cuDNN/8.1.1.33-CUDA-11.2.0 Singularity/3.9.8

    INPUT=/path/to/input_data
    OUTPUT=/path/to/results

    export SINGULARITY_BIND="$INPUT,$OUTPUT,$AF2DB"

    singularity exec --nv /opt/nesi/containers/AlphaFold/alphafold_2.2.0.simg python /app/alphafold/run_alphafold.py \
    --use_gpu_relax \
    --data_dir=$AF2DB \
    --uniref90_database_path=$AF2DB/uniref90/uniref90.fasta \
    --mgnify_database_path=$AF2DB/mgnify/mgy_clusters_2018_12.fa \
    --bfd_database_path=$AF2DB/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
    --uniclust30_database_path=$AF2DB/uniclust30/uniclust30_2018_08/uniclust30_2018_08 \
    --pdb70_database_path=$AF2DB/pdb70/pdb70 \
    --template_mmcif_dir=$AF2DB/pdb_mmcif/mmcif_files \
    --obsolete_pdbs_path=$AF2DB/pdb_mmcif/obsolete.dat \
    --model_preset=monomer \
    --max_template_date=2022-1-1 \
    --db_preset=full_dbs \
    --output_dir=$OUTPUT \
    --fasta_paths=$INPUT/rcsb_pdb_3GKI.fasta

 

### Multimer

    #!/bin/bash -e

    #SBATCH --account       nesi12345
    #SBATCH --job-name      alphafold2_monomer_example
    #SBATCH --mem           30G
    #SBATCH --cpus-per-task 6
    #SBATCH --gpus-per-node P100:1 
    #SBATCH --time          02:00:00
    #SBATCH --output        slurmout.%j.out

    module purge
    module load AlphaFold2DB/2022-06
    module load cuDNN/8.1.1.33-CUDA-11.2.0 Singularity/3.9.8

    INPUT=/path/to/input_data
    OUTPUT=/path/to/results


    export SINGULARITY_BIND="$INPUT,$OUTPUT,$AF2DB"

    singularity exec --nv /opt/nesi/containers/AlphaFold/alphafold_2.2.0.simg python /app/alphafold/run_alphafold.py \
    --use_gpu_relax \
    --data_dir=$AF2DB \
    --uniref90_database_path=$AF2DB/uniref90/uniref90.fasta \
    --mgnify_database_path=$AF2DB/mgnify/mgy_clusters_2018_12.fa \
    --bfd_database_path=$AF2DB/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
    --uniclust30_database_path=$AF2DB/uniclust30/uniclust30_2018_08/uniclust30_2018_08 \
    --pdb_seqres_database_path=$AF2DB/pdb_seqres/pdb_seqres.txt \
    --template_mmcif_dir=$AF2DB/pdb_mmcif/mmcif_files \
    --obsolete_pdbs_path=$AF2DB/pdb_mmcif/obsolete.dat \
    --uniprot_database_path=$AF2DB/uniprot/uniprot.fasta \
    --model_preset=multimer \
    --max_template_date=2022-1-1 \
    --db_preset=full_dbs \
    --output_dir=$OUTPUT \
    --fasta_paths=$INPUT/rcsb_pdb_3GKI.fasta

###  

### Explanation of Slurm variables and Singularity flags

1.  Values for `--mem` , `--cpus-per-task` and `--time` Slurm variables
    are for *3RGK.fasta*. Adjust them accordingly
2.  We have tested this on both P100 and A100 GPUs where the runtimes
    were identical. Therefore, the above example was set to former
    via `P100:1`
3.  The `--nv` flag enables GPU support.
4.  `--pwd /app/alphafold` is to workaround this [existing
    issue](https://github.com/deepmind/alphafold/issues/32)

###  

## AlphaFold2 : Initial Release ( this version does not support `multimer`)

Input *fasta* used in following example and subsequent benchmarking is
3RGK (<https://www.rcsb.org/structure/3rgk>).

###  

# Troubleshooting

-   If you are to encounter the message "*RuntimeError: Resource
    exhausted: Out of memory*" , add the following variables to the
    slurm script

For module based runs 

    export TF_FORCE_UNIFIED_MEMORY=1
    export XLA_PYTHON_CLIENT_MEM_FRACTION=4.0

For Singularity based runs 

    export SINGULARITYENV_TF_FORCE_UNIFIED_MEMORY=1 
    export SINGULARITYENV_XLA_PYTHON_CLIENT_MEM_FRACTION=4.0
