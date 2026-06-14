---
created_at: '2021-08-17T03:13:55Z'
tags: []
title: AlphaFold
vote_count: 2
vote_sum: 2
zendesk_article_id: 4405170961039
zendesk_section_id: 360000040076
---


[//]:AlphaFold.md> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]:AlphaFold.md> (APPS PAGE BOILERPLATE END)

!!! prerequisite Tips
     An extended version of AlphaFold2 on Mahuika cluster which
     contains additional information such as visualisation of AlphaFold
     outputs, etc [can be found
     here](https://nesi.github.io/alphafold2-on-mahuika/)

## AlphaFold 3

AlphaFold 3 is a substantial departure from AlphaFold 2: it predicts the
joint structure of complexes that can include proteins, nucleic acids
(DNA/RNA), ligands, ions and modified residues. It takes its input as a
**JSON file** (not a FASTA file), and the workflow is split into a
CPU-bound *data pipeline* (genetic and template search) and a GPU-bound
*inference* stage.

Home page is at <https://github.com/google-deepmind/alphafold3>.

!!! warning "You must request the model parameters from Google DeepMind"
    Unlike the AlphaFold 2 weights, the AlphaFold 3 model parameters are
    **not** redistributed by Mahuika. To obtain them you must agree to the
    [AlphaFold 3 Model Parameters Terms of Use](https://github.com/google-deepmind/alphafold3/blob/main/WEIGHTS_TERMS_OF_USE.md)
    and [request access from Google DeepMind](https://github.com/google-deepmind/alphafold3#obtaining-model-parameters)
    yourself. The terms permit non-commercial use only and prohibit
    sharing the weights. Once you receive them, store them in a directory
    you control (for example under your project space) and point
    `--model_dir` at it.

### AlphaFold 3 module and databases

The application and its databases are available as modules:

``` sh
$ module spider AlphaFold

 Versions:
        AlphaFold/2.3.2
        AlphaFold/3.0.0
        AlphaFold/3.0.1
        AlphaFold/3.0.2

$ module spider AlphaFold3DB

 Versions:
        AlphaFold3DB/2024-12
```

As with the AlphaFold 2 databases, loading the `AlphaFold3DB` module sets
an environment variable (`$AF3DB`) that points at the selected database
version, so you can pass it (and the individual files within it) to the
`--db_dir` and `--*_database_path` options:

``` sh
module load AlphaFold3DB/2024-12
echo $AF3DB
```

On Mahuika you also need to load `HMMER`, which AlphaFold 3 uses for its
genetic search. Loading it sets `$HMMER_DIR`, which you pass to the
`--*_binary_path` options:

``` sh
module load HMMER/3.4-GCC-12.3.0
echo $HMMER_DIR
```

### Input JSON

AlphaFold 3 reads a JSON description of the structure to fold rather than
a FASTA file. Unlike AlphaFold 2, there is **no** `--model_preset` for
choosing between monomer and multimer — a single model handles both, and
whether you fold a monomer or a complex is decided entirely by what you
list under `sequences` in the JSON. The `run_alphafold.py` command is
identical in either case.

**Monomer** — a single `protein` block with one chain `id`
(`fold_input.json`):

``` json
{
  "name": "my_protein",
  "modelSeeds": [1],
  "sequences": [
    {
      "protein": {
        "id": "A",
        "sequence": "GMRESYANENQFGFKTINSDIHKIVIVGGYGKLGGLFARYLRASGYPISILDREDWAVAESILANADVVIVSVPINLTLETIERLKPYLTENMLLADLTSVKREPLAKMLEVHTGAVLGLDVLVGGGNTAEAFIHGVQTILTKPSLHALILEYSSQEMQE"
      }
    }
  ],
  "dialect": "alphafold3",
  "version": 1
}
```

**Multimer** — add more entries to the `sequences` list, each with its
own chain `id`. This example is a heterodimer of two different proteins
(chains `A` and `B`):

``` json
{
  "name": "my_complex",
  "modelSeeds": [1],
  "sequences": [
    {
      "protein": {
        "id": "A",
        "sequence": "GMRESYANENQFGFKTINSDIHKIVIVGGYGKLGGLFARYLRASGYPISILDREDWAVAESILANADVVIVSVPINLTLETIERLKPYLTENMLLADLTSVKREPLAKMLEVHTGAVLGLDVLVGGGNTAEAFIHGVQTILTKPSLHALILEYSSQEMQE"
      }
    },
    {
      "protein": {
        "id": "B",
        "sequence": "MAAHKGAEHHHKAAEHHEQAAKHHHAAAEHHEKGEHEQAAHHADTAYAHHKHAEEHAAQAAKHDAEHHAPKPH"
      }
    }
  ],
  "dialect": "alphafold3",
  "version": 1
}
```

For a homo-multimer (the same sequence repeated), give a single `protein`
block a list of ids instead, for example `"id": ["A", "B"]`. A complex can
also mix molecule types — alongside `protein` blocks the `sequences` list
accepts `dna`, `rna`, `ligand` and `ion` entries. See the
[input documentation](https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md)
for the full schema.

### Example Slurm script

Unlike AlphaFold 2, the Mahuika build of AlphaFold 3 does not infer the
database files or search-tool binaries automatically: you pass the
genetic databases via the `--*_database_path` options (all found under
`$AF3DB`), the HMMER binaries via the `--*_binary_path` options (under
`$HMMER_DIR`), and your own copy of the model parameters via
`--model_dir`. The following runs both the data pipeline and inference in
a single GPU job for one input JSON:

``` sl
#!/bin/bash -e

#SBATCH --account       nesi12345
#SBATCH --job-name      af3-example
#SBATCH --mem           24G
#SBATCH --cpus-per-task 8
#SBATCH --gpus-per-node A100:1
#SBATCH --time          02:00:00
#SBATCH --output        %j.out

module purge
module load AlphaFold/3.0.2
module load AlphaFold3DB/2024-12
module load HMMER/3.4-GCC-12.3.0

INPUT=/nesi/project/nesi12345/alphafold3/fold_input.json
OUTPUT=/nesi/project/nesi12345/alphafold3/results
MODEL_DIR=/nesi/project/nesi12345/alphafold3/models

run_alphafold.py \
--json_path=${INPUT} \
--model_dir=${MODEL_DIR} \
--output_dir=${OUTPUT} \
--db_dir=${AF3DB} \
--uniref90_database_path=${AF3DB}/uniref90_2022_05.fa \
--mgnify_database_path=${AF3DB}/mgy_clusters_2022_05.fa \
--uniprot_cluster_annot_database_path=${AF3DB}/uniprot_all_2021_04.fa \
--small_bfd_database_path=${AF3DB}/bfd-first_non_consensus_sequences.fasta \
--pdb_database_path=${AF3DB}/mmcif_files \
--seqres_database_path=${AF3DB}/pdb_seqres_2022_09_28.fasta \
--hmmalign_binary_path=${HMMER_DIR}/hmmalign \
--hmmbuild_binary_path=${HMMER_DIR}/hmmbuild \
--hmmsearch_binary_path=${HMMER_DIR}/hmmsearch \
--jackhmmer_binary_path=${HMMER_DIR}/jackhmmer \
--nhmmer_binary_path=${HMMER_DIR}/nhmmer
```

To fold several inputs, place all of the JSON files in a directory and
replace `--json_path=${INPUT}` with `--input_dir=/path/to/json_dir`, or
call `run_alphafold.py` once per file (for example from a
[job array](../Parallel_Computing/Job_Arrays.md)).

!!! tip "Splitting the data pipeline and inference"
    The data pipeline (genetic/template search) is CPU-bound and does not
    need a GPU, while inference is GPU-bound. For large batches you can run
    the two stages as separate jobs — add `--norun_inference` to a CPU-only
    job to produce an enriched JSON (containing the MSAs), then feed that
    JSON into a GPU job with `--norun_data_pipeline` — so a GPU is not held
    idle during the search.

### AlphaFold 3 troubleshooting

- With the default configuration AlphaFold 3 fits inputs of up to roughly
    5,120 tokens on an 80&nbsp;GB GPU. For larger complexes, or if you hit
    out-of-memory errors during inference, enable unified memory so the
    GPU can spill into host memory:

    ``` sh
    export XLA_PYTHON_CLIENT_PREALLOCATE=true
    export XLA_PYTHON_CLIENT_MEM_FRACTION=0.95
    export XLA_CLIENT_MEM_FRACTION=0.95
    ```

- The data pipeline can be memory hungry for large sequences; increase
    `--mem` if the pipeline stage is killed.

### AlphaFold 3 license

The AlphaFold 3 source code is released under the
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
(CC BY-NC-SA 4.0) license](https://github.com/google-deepmind/alphafold3/blob/main/LICENSE).
The model parameters and any output generated using them are subject to
the [AlphaFold 3 Model Parameters Terms of Use](https://github.com/google-deepmind/alphafold3/blob/main/WEIGHTS_TERMS_OF_USE.md)
and are for non-commercial use only.

## Description

This package provides an implementation of the inference pipeline of
AlphaFold v2.0. This is a completely new model that was entered in
CASP14 and published in Nature. For simplicity, we refer to this model
as AlphaFold throughout the rest of this document.

Any publication that discloses findings arising from using this source
code or the model parameters
should [cite](https://github.com/deepmind/alphafold#citing-this-work) the
[AlphaFold paper](https://doi.org/10.1038/s41586-021-03819-2).
Please also refer to the [Supplementary
Information](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-021-03819-2/MediaObjects/41586_2021_3819_MOESM1_ESM.pdf) for
a detailed description of the method.

Home page is at <https://github.com/deepmind/alphafold>

## License and Disclaimer

This is not an officially supported Google product.

Copyright 2021 DeepMind Technologies Limited.

### [](https://github.com/deepmind/alphafold#alphafold-code-license)AlphaFold Code License

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at <https://www.apache.org/licenses/LICENSE-2.0>.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

### [](https://github.com/deepmind/alphafold#model-parameters-license)Model Parameters License

The AlphaFold parameters are made available for non-commercial use only,
under the terms of the Creative Commons Attribution-NonCommercial 4.0
International (CC BY-NC 4.0) license. You can find details
at: <https://creativecommons.org/licenses/by-nc/4.0/legalcode>

## AlphaFold Databases

AlphaFold databases are stored in `/opt/nesi/db/alphafold_db/`  parent
directory. In order to make the database calling more convenient, we
have prepared modules for each version of the database. Running
`module spider AlphaFold2DB` will list the available versions based on
when they were downloaded (Year-Month)

``` sh
$ module spider AlphaFold2DB

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
AlphaFold2DB: AlphaFold2DB/2022-06
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Description:
AlphaFold2 databases

 Versions:
         AlphaFold2DB/2022-06
         AlphaFold2DB/2023-04
```

Loading a module will set the `$AF2DB` variable which is pointing to
the  selected version of the database. For an example. 

``` sh
$ module load AlphaFold2DB/2023-04

$ echo $AF2DB 
/opt/nesi/db/alphafold_db/2023-04
```

## AlphaFold module ( &gt;= 2.3.2)

As of version 2.3.2 of AlphaFold, we recommend deploying AlphaFold via
the module (previous versoions were done via a Singularity container )

### Example Slurm script for monomer

Input *fasta* used in following example  is 3RGK
(<https://www.rcsb.org/structure/3rgk>).

``` sl
#!/bin/bash -e

#SBATCH --account       nesi12345
#SBATCH --job-name      af-2.3.2-monomer
#SBATCH --mem           24G
#SBATCH --cpus-per-task 8
#SBATCH --gpus-per-node A100:1
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
```

### Example Slurm script for multimer

Input *fasta* used in following example

``` sh
    T1083
GAMGSEIEHIEEAIANAKTKADHERLVAHYEEEAKRLEKKSEEYQELAKVYKKITDVYPNIRSYMVLHYQNLTRRYKEAAEENRALAKLHHELAIVED
    T1084
MAAHKGAEHHHKAAEHHEQAAKHHHAAAEHHEKGEHEQAAHHADTAYAHHKHAEEHAAQAAKHDAEHHAPKPH
```

``` sl
#!/bin/bash -e

#SBATCH --account       nesi12345
#SBATCH --job-name      af-2.3.2-multimer
#SBATCH --mem           30G
#SBATCH --cpus-per-task 4
#SBATCH --gpus-per-node A100:1
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
```

## AlphaFold Singularity container (prior to v2.3.2)

If you would like to use a version prior to 2.3.2, It can be done via
the Singularity containers.

We prepared a Singularity container image based on the [official
Dockerfile](https://hub.docker.com/r/catgumag/alphafold) with some
modifications. Image (.*simg*) and the corresponding definition file
(*.def*) are stored in `/opt/nesi/containers/AlphaFold/`

### [](https://github.com/DininduSenanayake/alphafold/tree/main/AlphaFold_Mahuika_instructions#example-slurm-script)Example Slurm scripts for Singularity container based AF2 deployment

#### Monomer

``` sl
#!/bin/bash -e

#SBATCH --account       nesi12345
#SBATCH --job-name      alphafold2_monomer_example
#SBATCH --mem           30G
#SBATCH --cpus-per-task 6
#SBATCH --gpus-per-node A100:1 
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
```

#### Multimer

``` sl
#!/bin/bash -e

#SBATCH --account       nesi12345
#SBATCH --job-name      alphafold2_monomer_example
#SBATCH --mem           30G
#SBATCH --cpus-per-task 6
#SBATCH --gpus-per-node A100:1 
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
```

#### Explanation of Slurm variables and Singularity flags

1. Values for `--mem` , `--cpus-per-task` and `--time` Slurm variables
    are for *3RGK.fasta*. Adjust them accordingly
2. The `--nv` flag enables GPU support.
3. `--pwd /app/alphafold` is to workaround this [existing
    issue](https://github.com/deepmind/alphafold/issues/32)

### AlphaFold2 : Initial Release ( this version does not support `multimer`)

Input *fasta* used in following example and subsequent benchmarking is
3RGK (<https://www.rcsb.org/structure/3rgk>).

## Troubleshooting

- If you are to encounter the message "*RuntimeError: Resource
    exhausted: Out of memory*" , add the following variables to the
    slurm script

For module based runs

``` sh
export TF_FORCE_UNIFIED_MEMORY=1
export XLA_PYTHON_CLIENT_MEM_FRACTION=4.0
```

For Singularity based runs

``` sl
export SINGULARITYENV_TF_FORCE_UNIFIED_MEMORY=1 
export SINGULARITYENV_XLA_PYTHON_CLIENT_MEM_FRACTION=4.0
```
