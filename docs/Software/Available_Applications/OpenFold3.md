---
title: OpenFold3
tags:
- biology
- machine_learning
- gpu
description: Predicting protein structures from amino acid sequences with OpenFold3
---

[//]: <> (APPS PAGE BOILERPLATE START)
{% set app_name = page.title | trim %}
{% set app = applications[app_name] %}
{% include "partials/app_header.html" %}
[//]: <> (APPS PAGE BOILERPLATE END)

## Description

OpenFold3 is a deep-learning system that predicts the three-dimensional
structure of a biomolecular assembly from sequence. It is an open source,
trainable, PyTorch reimplementation of Google DeepMind's
[AlphaFold 3](AlphaFold.md#alphafold-3), developed by the AlQuraishi Lab at
Columbia University together with the OpenFold Consortium, and it aims to
reproduce the architecture and results described in the AlphaFold 3 paper.

Like AlphaFold 3, it folds a whole assembly in one pass rather than one chain
at a time. A single query can combine protein, DNA and RNA chains with
small-molecule ligands, and the model returns coordinates for all of them
together. Protein and RNA chains are folded using evolutionary information from
a multiple sequence alignment, optionally supplemented by structural templates
for proteins. Coordinates are produced by a diffusion process, so each
prediction is sampled several times and the samples are ranked by the
confidence scores that accompany them — per-atom pLDDT, predicted aligned and
distance error, and pTM/ipTM for whole complexes and their interfaces.

Two differences from AlphaFold 3 matter in practice:

* **It is fully open.** Both the source code and the model parameters are
    released under the Apache 2.0 licence, for academic *and* commercial use.
* **It can be trained.** The training code, the training data pipeline and the
    preprocessed PDB training set are all published, so the model can be
    fine-tuned on your own structures or retrained from scratch. 

As with AlphaFold 3, OpenFold3 predicts *structure*. It does not compute
binding affinities, docking scores or any other measure of binding strength,
and a confident prediction is not evidence that two molecules interact.

## Setting up OpenFold3

### Downloading the parameters files 

If you are using OpenFold3 for the first time on Mahuika, you will need to download the OpenFold3 model parameters to your directory. 

1. Load OpenFold3:

	```bash
	module load OpenFold3
	```

2. Run `setup_openfold` in the terminal:

	```bash
	setup_openfold
	```

	You will be then asked a series of prompts:

	* You will need to write out in full the direct path to where you want to store OpenFold3 files.
	* `Please specify the OpenFold cache directory`: Best idea to change this to your project folder. Example: `/nesi/project/<PROJECT_ID>/<USERNAME>/openfold3`
	* `Please specify the directory for parameter download`: This should default to your cache directory. Example `/nesi/project/<PROJECT_ID>/<USERNAME>/openfold3`
	* `Select parameters to download`: Download whatever parameters you would like.
	* `Force re-download parameters even if they already exist?`: Set this to `yes`
	* `Run integration tests?`: `no`

	The setup should look something like this

	```bash
	user.name@login03:~$ setup_openfold
	[2026-08-11 17:54:31,291] [WARNING] [real_accelerator.py:199:get_accelerator] Setting accelerator to CPU. If you have GPU or other accelerator, we were unable to detect it.
	Setting up OpenFold3...
	Please specify the OpenFold cache directory (default: /home/user.name/.openfold3): /nesi/project/nesi12345/user.name/openfold3
	Please specify the directory for parameter download (default: /nesi/project/nesi12345/user.name/openfold3): 
	Select parameters to download:
	1) Download only the default checkpoint (openfold3-p2-155k)
	2) Download all parameters (openfold3-p2-145k, openfold3-p2-155k)
	3) Download a specific parameter by name
	Enter your choice (1/2/3, default: 1): 2
	Force re-download parameters even if they already exist? (yes/no, default: no) yes
	Run integration tests? (yes/no) no
	Parameters directory set to: /nesi/project/nesi12345/user.name/openfold3
	Starting parameter download...
	Downloading s3://openfold3-data/openfold3-parameters/of3-p2-145k.pt (2.13 GB) to /nesi/project/nesi12345/user.name/openfold3/of3-p2-145k.pt...
	of3-p2-145k.pt: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2.29G/2.29G [00:19<00:00, 115MB/s]
	Download complete.
	Downloading s3://openfold3-data/openfold3-parameters/of3-p2-155k.pt (2.13 GB) to /nesi/project/nesi12345/user.name/openfold3/of3-p2-155k.pt...
	of3-p2-155k.pt: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2.29G/2.29G [00:19<00:00, 116MB/s]
	Download complete.
	Download completed successfully.
	Starting Biotite CCD setup...
	Biotite CCD file at /opt/nesi/zen3/OpenFold3/0.4.4-foss-2026-CUDA-13.2.1/lib/python3.14/site-packages/biotite/structure/info/components.bcif is up-to-date with s3://openfold3-data/components.bcif, skipping.
	Skipping integration tests.
	Setup configuration saved to /nesi/project/nesi12345/user.name/openfold3/setup_config.json
	```

	!!! warning

		If you get an error message relating to Biotite CCD, get in touch with [Mahuika Support](mailto:support@nesi.org.nz).

3. Add the following line to your `.bashrc` and source it. **Make sure you change `OPENFOLD_CACHE` to what you gave in step 2**:

	```bash
	# Change the OPENFOLD_CACHE to what you used in step 2.
	OPENFOLD_CACHE=/nesi/project/<PROJECT_ID>/<USERNAME>/openfold3
	```

	then

	```bash
	printf '\n# Path to your OpenFold3 Cache\nexport OPENFOLD_CACHE='${OPENFOLD_CACHE}'\n' >> ~/.bashrc
	source ~/.bashrc
	```

	Check that your `OPENFOLD_CACHE` path is correct:

	```bash
	echo $OPENFOLD_CACHE
	```

	If this doesn't look right, you will need to change your `~/.bashrc` file by using `nano` or `vim`. 

4. Test that your setup was successful. In the terminal, copy the following json file from [openfold3](from https://github.com/aqlaboratory/openfold-3/blob/main/examples/example_inference_inputs/query_ubiquitin.json): 

	```bash
	cat > query_ubiquitin.json << 'EOF'
	{
	  "queries": {
	    "ubiquitin": {
	      "chains": [
	        {
	          "molecule_type": "protein",
	          "chain_ids": ["A"],
	          "sequence": "MQIFVKTLTGKTITLEVEPSDTIENVKAKIQDKEGIPPDQQRLIFAGKQLEDGRTLSDYNIQKESTLHLVLRLRGG"
	        }
	      ]
	    }
	  }
	}
	EOF
	```

	Then run the following in your terminal:

	```bash
	python - <<'EOF'
	import os, pathlib, zipfile

	import openfold3
	from openfold3.projects.of3_all_atom.config.inference_query_format import InferenceQuerySet
	print("[ok] openfold3 imports")

	import biotite.structure.info as info
	print(f"[ok] CCD: {len(info.all_residues())} components, "
	      f"ALA={info.residue('ALA').array_length()} atoms")

	cache = pathlib.Path(os.environ.get("OPENFOLD_CACHE", pathlib.Path.home() / ".openfold3"))
	ckpts = sorted(cache.glob("*.pt"))
	assert ckpts, f"no checkpoint in {cache}"
	for c in ckpts:
	    print(f"[ok] checkpoint {c.name}: {c.stat().st_size/1e9:.2f} GB, "
	          f"intact={zipfile.is_zipfile(c)}")

	InferenceQuerySet.from_json("query_ubiquitin.json")
	print("[ok] query JSON validates against this version's schema")
	EOF
	```

	If successful, you will get the following output:

	```bash
	[2026-08-11 18:03:24,289] [WARNING] [real_accelerator.py:199:get_accelerator] Setting accelerator to CPU. If you have GPU or other accelerator, we were unable to detect it.
	[ok] openfold3 imports
	[ok] CCD: 49282 components, ALA=13 atoms
	[ok] checkpoint of3-p2-145k.pt: 2.29 GB, intact=True
	[ok] checkpoint of3-p2-155k.pt: 2.29 GB, intact=True
	[ok] query JSON validates against this version's schema
	```

### Downloading the database files

Many of the databases that OpenFold3 uses are also used by AlphaFold3. To find those databases, see the [AlphaFold Databases](AlphaFold.md#alphafold-databases). However, OpenFold3 can also use other databases. If you want access to them, you will need to download them:

1. `cd` into the path where you would like to store your OpenFold3 databases. Ideally, this should be in your project directory:

	```bash
	mkdir -p /nesi/project/<PROJECT_ID>/openfold3_databases
	cd /nesi/project/<PROJECT_ID>/openfold3_databases
	```

2. Load OpenFold3:

	```bash
	module load OpenFold3
	```

3. Download the desired databases from the list below:

	```bash
	aws s3 ls --no-sign-request --human-readable s3://openfold/alignment_databases/
	```

	For example, the following will download and uncompress your desired databases:

	```bash
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/rfam.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/pdb_seqres.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/rnacentral.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/nucleotide_collection.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/uniref90.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/uniprot.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/mgnify.fasta.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/uniref30.tar.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/cfdb.tar.gz .
	aws s3 cp --no-sign-request s3://openfold/alignment_databases/bfd.tar.gz .
	```

	Be mindful of the amount of space you will need before you download the databases:

	| #  | Database | Format | Size | Type |
	|----|----------------------|------------|--------|--------------------|
	| 1  | pdb_seqres | .fasta.gz | 55 MB | protein |
	| 2  | rfam | .fasta.gz | 61 MB | RNA |
	| 3  | nucleotide_collection | .fasta.gz | 2.3 GB | RNA |
	| 4  | rnacentral | .fasta.gz | 4.2 GB | RNA |
	| 5  | uniref90 | .fasta.gz | 47 GB | protein |
	| 6  | uniprot | .fasta.gz | 61 GB | protein |
	| 7  | mgnify | .fasta.gz | 79 GB | protein |
	| 8  | uniref30 | .tar.gz | 141 GB | protein (HHblits) |
	| 9  | cfdb | .tar.gz | 290 GB | protein (HHblits) |
	| 10 | bfd | .tar.gz | 292 GB | protein (HHblits) |

	**Total download:** ~918 GB — budget ~3–4 TB of filesystem for the decompressed set.

## Using OpenFold3

Everything in OpenFold3 is driven by the single `run_openfold` command:

| Command | What it does |
| --------- | -------------- |
| `run_openfold predict` | Runs structure prediction (inference) |
| `run_openfold train` | Trains or fine-tunes the model |
| `run_openfold align-msa-server` | Fetches alignments from the ColabFold server only |

## Running a prediction session with OpenFold3

A prediction is split into two stages:

1. **Search stage (CPU)** — build a multiple sequence alignment (MSA), and
   optionally a template alignment, for every unique protein and RNA chain in
   your input. This is CPU- and I/O-bound and does not need a GPU.
2. **Prediction stage (GPU)** — turn those alignments into features and run the
   model to produce structures and confidence scores.

The following are the steps for running a prediction using OpenFold3
(Reference: [OpenFold3 Inference](https://openfold-3.readthedocs.io/en/latest/inference.html)).
Each step below also links the upstream page it is based on, which is the place
to look for anything not covered here.

### Step 1: Describe what you want to fold

*Reference: [OpenFold3 Input Format](https://openfold-3.readthedocs.io/en/latest/input_format_reference.html)*

OpenFold3 takes a single **query JSON** file, which can contain many
independent prediction targets (*queries*). Each query is one bioassembly and
is predicted in one forward pass. The key of each query (`query_1` below) names
its output directory.

Each chain needs a `molecule_type` (`protein`, `rna`, `dna` or `ligand`), one or
more `chain_ids`, and either a `sequence` (for polymers) or a `smiles`/
`ccd_codes` entry (for ligands):

``` json title="query.json"
{
    "queries": {
        "query_1": {
            "chains": [
                {
                    "molecule_type": "protein",
                    "chain_ids": ["A", "B"],
                    "sequence": "PVLSCGEWQCL"
                },
                {
                    "molecule_type": "dna",
                    "chain_ids": "C",
                    "sequence": "GACCTCT"
                },
                {
                    "molecule_type": "ligand",
                    "chain_ids": "Z",
                    "smiles": "CC(=O)OC1C[NH+]2CCC1CC2"
                },
                {
                    "molecule_type": "ligand",
                    "chain_ids": "I",
                    "ccd_codes": "NAG"
                }
            ]
        }
    }
}
```

Giving one chain block a list of `chain_ids` (`["A", "B"]` above) creates a
homomer — the same sequence repeated. Separate chain blocks with different
sequences create a heteromer. Both are handled by the same model and the same
command; there is no monomer/multimer preset to choose.

Useful optional fields on protein and RNA chains:

| Field | Purpose |
| ------- | --------- |
| `main_msa_file_paths` | Where to find this chain's precomputed MSAs (Step 3) |
| `paired_msa_file_paths` | Pre-paired MSAs, if you paired them yourself |
| `use_msas` | Set to `false` to give the model empty MSA features |
| `use_main_msas` / `use_paired_msas` | Turn unpaired or paired MSAs off individually |
| `template_alignment_file_path` | Precomputed template alignment (Step 4) |
| `template_cif_paths` | Template structures given directly as CIF files (Step 4) |
| `non_canonical_residues` | Map of 1-based position to CCD code, e.g. `{"1": "MHO"}` |

A query may also carry a `pocket_constraint` to bias a ligand towards a
particular binding site. See the
[input format reference](https://openfold-3.readthedocs.io/en/latest/input_format_reference.html)
for the complete schema.

!!! note "Which molecule types are supported"

    Protein and RNA chains use MSAs; DNA chains are predicted without an MSA
    (as in AlphaFold 3). Ligands must currently be non-covalent — covalently
    bound ligands, glycans and other cross-chain covalent bonds are not yet
    supported by the inference pipeline. Templates are supported for protein
    chains only.

### Step 2: Generate the MSAs from the local databases

*Reference: [OpenFold3-Style Precomputed MSA Generation](https://openfold-3.readthedocs.io/en/latest/precomputed_msa_generation_how_to.html)*

OpenFold3 ships a [Snakemake](snakemake.md) pipeline that
searches each unique sequence against the databases you downloaded and writes
one directory of alignments per chain. The pipeline is configured with a JSON
file, such as this example:

``` json title="config_protein.json"
{
    "input_fasta": "/nesi/nobackup/nesi12345/openfold3/queries.fasta",
    "openfold_env": "<GET PATH FROM 'echo $EBROOTOPENFOLD3'>",
    "databases": ["uniref90"],
    "base_database_path": "/nesi/project/nesi12345/openfold3_databases",
    "output_directory": "/nesi/nobackup/nesi12345/openfold3/alignments",
    "jackhmmer_output_format": "a3m",
    "jackhmmer_threads": 8,
    "nhmmer_threads": 8,
    "hhblits_threads": 8,
    "tmpdir": "/nesi/nobackup/nesi12345/openfold3/tmp",
    "run_template_search": true
}
```

The fields are:

* **`input_fasta`** *(path)* — the FASTA file of sequences to align, one record
    per unique sequence you intend to fold. Only protein and RNA chains need
    alignments, so for the `query_1` example in Step 1 this file holds just the
    one protein sequence:

    ``` bash
    >query_1_A
    PVLSCGEWQCL
    ```

* **`openfold_env`** *(path)* — the OpenFold3 environment the pipeline should
    run its tools from. On Mahuika this is the module's install directory, which
    `echo $EBROOTOPENFOLD3` prints once the module is loaded. JSON cannot expand
    environment variables, so paste in the literal path the `echo $EBROOTOPENFOLD3` prints. 
* **`databases`** *(list of strings)* — which databases to generate alignments
    against. One or more of `uniref90`, `uniprot`, `mgnify`, `cfdb` and `bfd`.
* **`base_database_path`** *(path)* — the directory holding those databases.
    
    * `uniref90`, `uniprot` and `mgnify` must be laid out as `{base_database_path}/{db}/{db}.fasta`; 
    * `cfdb` and `bfd` must be unpacked into `{base_database_path}/{cfdb|bfd}/`.

* **`output_directory`** *(path)* — where the per-chain alignment directories
    are written. This is the path you will point your query JSON at in Step 3.
* **`jackhmmer_output_format`** *(string)* — `sto` or `a3m`, the format
    `jackhmmer` writes its alignments in.
* **`jackhmmer_threads`**, **`nhmmer_threads`**, **`hhblits_threads`**
    *(integers)* — threads used by **one** invocation of each search tool.
    `jackhmmer` handles the FASTA databases, `nhmmer` the RNA searches, and
    `hhblits` the `cfdb` and `bfd` databases. 
* **`tmpdir`** *(path)* — scratch space for intermediate files.
* **`run_template_search`** *(boolean)* — whether to also run `hmmsearch`
    against `pdb_seqres` to produce the template alignments used in Step 4.
    Requires `uniref90` to be in `databases`, or UniRef90 alignments completed
    by an earlier run.

Always dry-run first to check the paths resolve:

``` bash
snakemake -np -s $OPENFOLD3_MSA_SNAKEFILE --configfile config_protein.json
```

Then submit the real run as a CPU job:

``` sl
#!/bin/bash -e

#SBATCH --account       nesi12345
#SBATCH --job-name      of3-msa
#SBATCH --cpus-per-task 8
#SBATCH --mem           64G
#SBATCH --time          12:00:00
#SBATCH --output        %j.out

module purge
module load OpenFold3

snakemake -s $OPENFOLD3_MSA_SNAKEFILE \
    --cores $SLURM_CPUS_PER_TASK \
    --configfile config_protein.json \
    --nolock \
    --keep-going \
    --latency-wait 120
```

!!! tip "Aligning many sequences at once"

	If your `input_fasta` holds several sequences and you want to run 
	multiple sequences at the same time, increase `--cpus-per-task` by a
	multiple of `jackhmmer_threads`/`nhmmer_threads`/`hhblits_threads`

!!! tip "Getting the search stage to run well"

    * **One database per job.** Running a single database at a time lets the
      filesystem cache work in your favour and is usually faster overall than
      searching several at once. Run the pipeline once per database and let
      the outputs accumulate in the same `output_directory`.
    * **Proteins and RNA must be run separately**, with a config file each.
    * **Watch your memory.** `jackhmmer` and `hhblits` memory scales with the
      database. Requesting too little `--mem` will get the job killed part
      way through a search.
    * **Alignments are reusable.** The same chain directory can be pointed at
      by any number of later predictions, so this cost is paid once per
      unique sequence, not once per prediction.

The result is one directory per unique sequence, named after its FASTA record,
with filenames recording which database each alignment came from. For the
single-sequence example above:

``` bash
alignments/
└── query_1_A/
    ├── uniref90_hits.a3m
    ├── uniprot_hits.a3m
    ├── mgnify_hits.a3m
    └── hmm_output.sto      # template alignment, if run_template_search was true
```

Every additional unique sequence in `input_fasta` gets its own directory
alongside it.

RNA chains produce `rfam_hits.sto`, `rnacentral_hits.a3m` and `nt_hits.a3m`
instead.

#### Optional: preparse the alignments into NPZ

If you are going to run many predictions, or many predictions that share
sequences, convert the raw alignments into compressed NumPy arrays once. This
cuts both the parsing time inside each prediction job and the disk space the
alignments occupy:

``` bash
preparse_alignments_of3.py \
    --alignments_directory /nesi/nobackup/nesi12345/openfold3/alignments \
    --alignment_array_directory /nesi/nobackup/nesi12345/openfold3/alignment_arrays \
    --num_workers 8 \
    --max_seq_counts '{"uniref90_hits": 10000, "uniprot_hits": 50000, "mgnify_hits": 5000}'
```

This produces one `.npz` per unique sequence (`query_1_A.npz`, …) which can be
used in place of the chain directory everywhere below.

### Step 3: Point the query JSON at the alignments

*Reference: [Precomputed MSA Use in the OpenFold3 Inference Pipeline](https://openfold-3.readthedocs.io/en/latest/precomputed_msa_how_to.html)*

This step edits the **query JSON from Step 1** by adding a `main_msa_file_paths` field to each protein and RNA
chain. This `main_msa_file_paths` field contains the information obtained from step 2. 
Only the protein chain get a `main_msa_file_paths` field. DNA and ligand chains do not get this `main_msa_file_paths` field because they do not use MSAs.

``` json title="query.json" hl_lines="9"
{
    "queries": {
        "query_1": {
            "chains": [
                {
                    "molecule_type": "protein",
                    "chain_ids": ["A", "B"],
                    "sequence": "PVLSCGEWQCL",
                    "main_msa_file_paths": "/nesi/nobackup/nesi12345/openfold3/alignments/query_1_A"
                },
                {
                    "molecule_type": "dna",
                    "chain_ids": "C",
                    "sequence": "GACCTCT"
                },
                {
                    "molecule_type": "ligand",
                    "chain_ids": "Z",
                    "smiles": "CC(=O)OC1C[NH+]2CCC1CC2"
                },
                {
                    "molecule_type": "ligand",
                    "chain_ids": "I",
                    "ccd_codes": "NAG"
                }
            ]
        }
    }
}
```

There is **one `main_msa_file_paths` per chain block**, not one per chain ID.
The block above covers chains A and B with a single path because they are the
same sequence and so share an alignment. A heteromer — two *different* protein
sequences — is written as two chain blocks, each with its own path pointing at
its own alignment directory.

!!! tip "Other forms of `main_msa_file_paths`"

	Three forms of `main_msa_file_paths` are accepted, and they are equivalent. A
	chain directory, as above; a list of individual alignment files, if you want
	only some of them:

	``` json
	"main_msa_file_paths": [
	    "/nesi/nobackup/nesi12345/openfold3/alignments/query_1_A/uniref90_hits.a3m",
	    "/nesi/nobackup/nesi12345/openfold3/alignments/query_1_A/mgnify_hits.a3m"
	]
	```

	or a single preparsed `.npz`, if you ran the optional preparse step:

	``` json
	"main_msa_file_paths": "/nesi/nobackup/nesi12345/openfold3/alignment_arrays/query_1_A.npz"
	```

	Use absolute paths — relative paths are resolved against the working directory
	of the job, which is rarely what you want in a Slurm script.

!!! note "Paired MSAs for heteromers"

    For a complex with two or more *different* protein chains, OpenFold3
    pairs the alignments across chains by species on the fly, using the
    alignments named in `msas_to_pair` (UniProt by default). Pairing puts
    the sequences from the same organism on the same row of each chain's
    alignment, which is what lets the model see residues in one chain
    co-varying with residues in the other — the main evolutionary signal
    for how the chains dock.

    This works as long as those alignment headers carry a species
    identifier, which UniProt headers do and metagenomic ones such as
    MGnify generally do not. Alignments from the Step 2 pipeline are fine
    as they are. Only supply `paired_msa_file_paths` if you have pre-paired
    the alignments yourself.

    *References:
    [Online MSA Pairing](https://openfold-3.readthedocs.io/en/latest/precomputed_msa_explanation.html#online-msa-pairing)
    and
    [Providing Species Information for Online Pairing](https://openfold-3.readthedocs.io/en/latest/precomputed_msa_how_to.html#providing-species-information-for-online-pairing)*

#### Optional: alignments from another pipeline

If your alignment filenames differ from the OpenFold3 defaults (for example
because you generated them with your own pipeline), tell the featuriser about
them in the `runner.yml`:

``` yaml
dataset_config_kwargs:
  msa:
    max_seq_counts:
      uniref90_hits: 10000
      uniprot_hits: 50000
      custom_database_hits: 10000
    msas_to_pair: ["uniprot_hits"]
    aln_order:
      - uniref90_hits
      - uniprot_hits
      - custom_database_hits
```

The `runner.yml` file contains the follow inputs:

* `max_seq_counts` caps how many sequences are taken from each file, 
* `aln_order` sets the order the alignments are stacked in, and 
* `msas_to_pair` names the alignments used for cross-chain pairing in heteromeric complexes. 

You do not need any of this if you used the OpenFold3 pipeline in Step 2.

### Step 4: Templates (optional)

*Reference: [Running OpenFold3 Inference with Templates](https://openfold-3.readthedocs.io/en/latest/template_how_to.html)*

Templates are optional and protein-only. There are three ways to handle them:

#### Use the template alignments from Step 2

If you set `run_template_search: true`, point each protein chain at its
`hmm_output.sto`.
For example: 

``` json title="query.json" hl_lines="10"
{
    "queries": {
        "query_1": {
            "chains": [
                {
                    "molecule_type": "protein",
                    "chain_ids": ["A", "B"],
                    "sequence": "PVLSCGEWQCL",
                    "main_msa_file_paths": "/nesi/nobackup/nesi12345/openfold3/alignments/query_1_A",
                    "template_alignment_file_path": "/nesi/nobackup/nesi12345/openfold3/alignments/query_1_A/hmm_output.sto"
                },
                {
                    "molecule_type": "dna",
                    "chain_ids": "C",
                    "sequence": "GACCTCT"
                },
                {
                    "molecule_type": "ligand",
                    "chain_ids": "Z",
                    "smiles": "CC(=O)OC1C[NH+]2CCC1CC2"
                },
                {
                    "molecule_type": "ligand",
                    "chain_ids": "I",
                    "ccd_codes": "NAG"
                }
            ]
        }
    }
}
```

The alignment only names its templates, so OpenFold3 also needs a directory of
mmCIF structures to read them from. That is set in the `runner.yml` you write
in [Step 5](#step-5-run-the-prediction).

!!! tip "Large batches"

    Alignment-based templates are the slow ones to prepare: for a job with
    many predictions, parsing the alignments and their structures can take
    longer than the model itself. OpenFold3 provides preprocessing scripts
    (`preprocess_template_alignments_precache_of3.py`,
    `preprocess_template_alignments_new_of3.py` and
    `preprocess_template_structures_of3.py`, all on your `PATH` once the
    module is loaded) that build a reusable template cache in a CPU job, so
    the GPU job is not held up by data preparation. See the
    [template how-to](https://openfold-3.readthedocs.io/en/latest/template_how_to.html).

    None of this applies to the CIF-direct mode below, which has no
    alignments to preprocess.

#### Supply template structures directly

If you already know which structures you want to use as templates, skip
alignments entirely and list the CIF files.
OpenFold3 aligns each one to your query with Kalign and picks the best-matching
chain. Only the protein chain changes; the rest of `query_1` is as above:

``` json title="query.json" hl_lines="10 11 12 13 14"
{
    "queries": {
        "query_1": {
            "chains": [
                {
                    "molecule_type": "protein",
                    "chain_ids": ["A", "B"],
                    "sequence": "PVLSCGEWQCL",
                    "main_msa_file_paths": "/nesi/nobackup/nesi12345/openfold3/alignments/query_1_A",
                    "template_cif_paths": [
                        "/nesi/nobackup/nesi12345/openfold3/templates/1dgc.cif",
                        "/nesi/nobackup/nesi12345/openfold3/templates/1ysa.cif"
                    ],
                    "template_cif_chain_ids": ["A", null]
                },
                {
                    "molecule_type": "dna",
                    "chain_ids": "C",
                    "sequence": "GACCTCT"
                },
                {
                    "molecule_type": "ligand",
                    "chain_ids": "Z",
                    "smiles": "CC(=O)OC1C[NH+]2CCC1CC2"
                },
                {
                    "molecule_type": "ligand",
                    "chain_ids": "I",
                    "ccd_codes": "NAG"
                }
            ]
        }
    }
}
```

* Use `null` to let OpenFold3 choose the chain. 
* `template_cif_paths` and `template_alignment_file_path` are mutually exclusive — use one or the other, never both on the same chain. 

#### Skip templates

Set `use_templates: false` under `experiment_settings` in your `runner.yml`.

### Step 5: Run the prediction

*References: [OpenFold3 Inference](https://openfold-3.readthedocs.io/en/latest/inference.html)
and [OpenFold3 Parameters](https://openfold-3.readthedocs.io/en/latest/parameters_reference.html)*

Write a `runner.yml` for the prediction job.

``` yaml title="inference.yml"
experiment_settings:
  mode: predict
  use_msa_server: false
  use_templates: true

model_update:
  presets:
    - predict

output_writer_settings:
  structure_format: cif
```

!!! note "Add this if you are using template alignments"

    If you gave your chains a `template_alignment_file_path` in
    [Step 4](#use-the-template-alignments-from-step-2), the alignment names
    its templates but does not contain them, so the `runner.yml` also has to
    say where the structures live:

    ``` yaml title="inference.yml" hl_lines="13 14 15 16 17"
    experiment_settings:
      mode: predict
      use_msa_server: false
      use_templates: true

    model_update:
      presets:
        - predict

    output_writer_settings:
      structure_format: cif

    template_preprocessor_settings:
      structure_directory: /opt/nesi/db/alphafold_db/2023-04/pdb_mmcif/mmcif_files/
      structure_file_format: cif
      fetch_missing_structures: false
      n_processes: 4
    ```

    That `structure_directory` is the PDB mmCIF mirror that comes with the
    [AlphaFold databases](AlphaFold.md#alphafold-databases). Setting
    `fetch_missing_structures: false` keeps the job reading from it rather
    than downloading anything it cannot find from the RCSB PDB mid-run.

    Neither setting is needed if you used `template_cif_paths` or turned
    templates off.

Then submit a GPU job:

``` sl
#!/bin/bash -e

#SBATCH --account       nesi12345
#SBATCH --job-name      of3-predict
#SBATCH --partition     genoa
#SBATCH --cpus-per-task 8
#SBATCH --mem           32G
#SBATCH --gpus-per-node L4:1
#SBATCH --time          02:00:00
#SBATCH --output        %j.out

module purge
module load OpenFold3

QUERY=/nesi/nobackup/nesi12345/openfold3/query.json
OUTPUT=/nesi/nobackup/nesi12345/openfold3/results
RUNNER=/nesi/nobackup/nesi12345/openfold3/inference.yml

run_openfold predict \
    --query-json ${QUERY} \
    --output-dir ${OUTPUT} \
    --runner-yaml ${RUNNER} \
    --num-diffusion-samples 5 \
    --num-model-seeds 1
```

Common `run_openfold predict` arguments:

| Argument | Default | Purpose |
| ---------- | --------- | --------- |
| `--query-json` | *required* | Input query JSON |
| `--output-dir` | `test_train_output/` | Where results are written |
| `--inference-ckpt-path` | — | Explicit path to a `.pt` checkpoint |
| `--inference-ckpt-name` | `openfold3-p2-155k` | Named checkpoint from `$OPENFOLD_CACHE` |
| `--num-diffusion-samples` | `5` | Structures generated per seed |
| `--num-model-seeds` | `1` | Independent forward passes per query |
| `--runner-yaml` | — | YAML config for everything else |

For *n* queries, *m* seeds and *l* diffusion samples you get *n × m* forward
passes and *n × m × l* structures, so increasing seeds is much more expensive
than increasing diffusion samples.

!!! note "Which checkpoint is used"

    If neither `--inference-ckpt-path` nor `--inference-ckpt-name` is given,
    OpenFold3 uses `openfold3-p2-155k` and looks for it in `$OPENFOLD_CACHE`.
    Provided you set `OPENFOLD_CACHE` during
    [setup](#downloading-the-parameters-files), the checkpoint you already
    downloaded is found and nothing is fetched from the network.

    You can also drop a `runner.yml` at `$OPENFOLD_CACHE/runner.yml` and it
    will be applied to every prediction automatically, without `--runner-yaml`.
    This is a convenient place to keep site-specific settings such as
    `use_msa_server: false`.

### Adjusting the prediction job

*Reference: [OpenFold3 Configuration Reference](https://openfold-3.readthedocs.io/en/latest/configuration_reference.html)*

These all go in the `runner.yml`:

**Use several GPUs.** Prediction is backed by PyTorch Lightning, which spreads
a batch of queries over the available GPUs. This only helps if your query JSON
contains several queries:

``` yaml
pl_trainer_args:
  devices: 2      # GPUs per node
  num_nodes: 1
```

**Run out of GPU memory.** Add the `low_mem` preset, which computes the
pairformer embeddings for each diffusion sample sequentially instead of
together. Expect a significant slowdown, especially with many diffusion
samples:

``` yaml
model_update:
  presets:
    - predict
    - low_mem
```

**Choose specific random seeds** instead of letting OpenFold3 pick them:

``` yaml
experiment_settings:
  seeds:
    - 100
    - 101
```

**Write PDB instead of mmCIF.** Per-residue pLDDT is stored in the B-factor
column of PDB output:

``` yaml
output_writer_settings:
  structure_format: pdb
```

**Save disk space on big batches** by skipping the per-atom confidence files
and keeping only the aggregated scores:

``` yaml
output_writer_settings:
  write_full_confidence_scores: False
```

**Save the trunk embeddings** as a `*_latent_output.pt` containing `si_trunk`,
`zij_trunk` and `atom_positions_predicted`:

``` yaml
output_writer_settings:
  write_latent_outputs: True
```

### Understanding the output

*Reference: [Model Outputs](https://openfold-3.readthedocs.io/en/latest/inference.html#model-outputs)*

Each query gets a directory named after its key, containing one subdirectory
per seed:

``` bash
results/
└── query_1
    └── seed_42
        ├── query_1_seed_42_sample_1_model.cif
        ├── query_1_seed_42_sample_1_confidences.json
        ├── query_1_seed_42_sample_1_confidences_aggregated.json
        └── timing.json
```

* `*_model.cif` (or `.pdb`) — the predicted structure.
* `*_confidences.json` — per-atom `plddt`, `pae` and `pde`.
* `*_confidences_aggregated.json` — whole-structure scores.
* `timing.json` — model runtime in seconds, excluding any MSA computation.

The aggregated file is the one to rank predictions with:

| Score | Meaning |
| ------- | --------- |
| `sample_ranking_score` | Weighted combination of `ptm`, `iptm`, `disorder` and `has_clash`. **Use this to pick the best sample.** |
| `avg_plddt` | Mean per-atom pLDDT; higher is more confident |
| `ptm` / `iptm` | Predicted TM-score for the complex, and its interface variant |
| `chain_ptm` / `chain_pair_iptm` | The same, per chain and per chain pair |
| `bespoke_iptm` | Per-chain interface score; use this to rank interfaces |
| `gpde` | Global predicted distance error; lower is better |
| `has_clash` | `1.0` if any two polymer chains clash sterically |
| `disorder` | Mean relative solvent-accessible surface area |

Alongside the per-query directories, OpenFold3 writes `inference_query_set.json`
(the validated input, with all resolved MSA and template paths),
`model_config.json` and `experiment_config.json`. Keep these — together they
record exactly what was run.

### Inference troubleshooting

* **CUDA out of memory.** Add the `low_mem` preset, reduce
  `--num-diffusion-samples`, or split a large complex into a smaller query.
* **A chain gets no MSA features.** OpenFold3 silently proceeds with an empty
  MSA if it cannot find alignments. Check `inference_query_set.json` in the
  output directory — it shows the paths actually used for each chain.
* **Predictions without MSAs are noticeably worse.** This is expected. If you
  want a fast, low-accuracy run, that trade-off is available via
  `"use_msas": false` on a chain, but do not use it for production results.

## Running a training session with OpenFold3

OpenFold3 is fully trainable — you can train it from scratch
or fine-tune the released checkpoints on your own structures. As with inference,
everything is driven by a YAML config file, and all the data comes from disk
rather than from any network service.

!!! warning "Training is a serious undertaking"

    The released OpenFold3 parameters were produced with 155,000 training
    steps on a large multi-node GPU cluster. Reproducing that on Mahuika is
    not realistic within a normal allocation. Fine-tuning from a released
    checkpoint on a focused dataset is far more achievable, and is what most
    users actually want. Talk to us before requesting a large GPU allocation
    for training.

### Step 1: Get the training data

*References: [Download the Dataset](https://openfold-3.readthedocs.io/en/latest/training.html#download-the-dataset)
and [OpenFold3 Training Data Pipeline](https://openfold-3.readthedocs.io/en/latest/data_pipeline_reference.html)*

The preprocessed PDB training set — structures, MSAs, templates and the dataset
caches that tie them together — is hosted on S3. Check the size before you start
so you can be sure of your `/nesi/nobackup` quota:

``` bash
module load OpenFold3

aws s3 ls --no-sign-request --summarize --human-readable --recursive s3://openfold3-data/pdb_training_set/ | tail -3
```

Then sync it to a directory that every node in your job can read:

``` bash
mkdir -p /nesi/nobackup/nesi12345/openfold3/pdb_training_set/
aws s3 sync --no-sign-request s3://openfold3-data/pdb_training_set/ /nesi/nobackup/nesi12345/openfold3/pdb_training_set/
```

!!! tip "Test the setup on a small subset first"

    OpenFold3 provides `setup-pdb-subset` (which runs `generate-pdb-subset`
    then `download-pdb-subset`) to build a miniature training set complete
    with MSAs, template files and dataset caches. Use it to confirm your
    config and paths work before committing to a long job:

    ``` bash
    setup-pdb-subset
    pytest --pyargs openfold3.tests.test_training_full
    ```

### Step 2: Write the training config

*References: [Prepare the Training Config](https://openfold-3.readthedocs.io/en/latest/training.html#prepare-the-training-config)
and [OpenFold3 Configuration Reference](https://openfold-3.readthedocs.io/en/latest/configuration_reference.html)*

The training config is the same `runner.yml` used for inference, with
`mode: train` and additional sections describing the datasets. A minimal
single-GPU config looks like this:

``` yaml title="training.yml"
experiment_settings:
  mode: train
  output_dir: /nesi/nobackup/nesi12345/openfold3/train_output
  restart_checkpoint_path: last

data_module_args:
  batch_size: 1
  num_workers: 4
  epoch_len: 500          # steps between checkpoints (effective batch size x steps)

logging_config:
  log_lr: false
  wandb_config: null

pl_trainer_args:
  devices: 1
  num_nodes: 1
  precision: bf16-mixed
  max_epochs: -1
  log_every_n_steps: 50

checkpoint_config:
  every_n_epochs: 1
  auto_insert_metric_name: false
  save_last: true
  save_top_k: -1

model_update:
  presets:
    - train
  custom:
    architecture:
      shared:
        use_confidence_emb_prob: 0.8
        diffusion:
          use_conditioning_prob: 0.8

dataset_configs:
  train:
    weighted-pdb:
      dataset_class: WeightedPDBDataset
      weight: 1.0
      config:
        template:
          n_templates: 4
          take_top_k: false
        crop:
          token_crop:
            enabled: true
            token_budget: 384
            crop_weights:
              contiguous: 0.2
              spatial: 0.4
              spatial_interface: 0.4
          chain_crop:
            enabled: true

  validation:
    val-weighted-pdb:
      dataset_class: ValidationPDBDataset
      config:
        msa:
          subsample_main: false
        template:
          n_templates: 4
          take_top_k: true
        crop:
          token_crop:
            enabled: false

dataset_paths:
  weighted-pdb:
    alignments_directory: none
    alignment_db_directory: none
    alignment_array_directory: /nesi/nobackup/nesi12345/openfold3/pdb_training_set/alignment_arrays
    dataset_cache_file: /nesi/nobackup/nesi12345/openfold3/pdb_training_set/dataset_caches/training_cache_with_templates.json
    target_structures_directory: /nesi/nobackup/nesi12345/openfold3/pdb_training_set/preprocessed_pdb_data/standard/structure_files
    target_structure_file_format: npz
    reference_molecule_directory: /nesi/nobackup/nesi12345/openfold3/pdb_training_set/preprocessed_pdb_data/standard/reference_mols
    template_cache_directory: /nesi/nobackup/nesi12345/openfold3/pdb_training_set/templates/train_template_cache
    template_structure_array_directory: /nesi/nobackup/nesi12345/openfold3/pdb_training_set/templates/template_structure_arrays
    template_structures_directory: none
    template_file_format: npz
    ccd_file: null

  val-weighted-pdb:
    alignments_directory: none
    alignment_db_directory: none
    alignment_array_directory: /nesi/nobackup/nesi12345/openfold3/pdb_training_set/alignment_arrays
    dataset_cache_file: /nesi/nobackup/nesi12345/openfold3/pdb_training_set/dataset_caches/validation_cache_with_templates.json
    target_structures_directory: /nesi/nobackup/nesi12345/openfold3/pdb_training_set/preprocessed_pdb_data/standard/structure_files
    target_structure_file_format: npz
    reference_molecule_directory: /nesi/nobackup/nesi12345/openfold3/pdb_training_set/preprocessed_pdb_data/standard/reference_mols
    template_cache_directory: /nesi/nobackup/nesi12345/openfold3/pdb_training_set/templates/val_template_cache
    template_structure_array_directory: /nesi/nobackup/nesi12345/openfold3/pdb_training_set/templates/template_structure_arrays
    template_structures_directory: none
    template_file_format: npz
    ccd_file: null
```

The parts you are most likely to change:

| Setting | Effect |
| --------- | -------- |
| `dataset_paths` | **Must** point at your copy of the data. Every path here is checked at startup. |
| `epoch_len` | How many steps make an "epoch", and therefore how often checkpoints are written |
| `token_budget` | Size of the training crop. Lower it if you run out of GPU memory. |
| `precision` | `bf16-mixed` is recommended on A100; `32-true` is the default and much slower |
| `devices` / `num_nodes` | GPUs per node and number of nodes |
| `num_workers` | Data loading processes. Keep this at or below `--cpus-per-task`. |

The upstream repository ships complete configs for every stage of the published
training schedule under
[`examples/training_yamls/`](https://github.com/aqlaboratory/openfold-3/tree/main/examples/training_yamls) —
[`initial_training.yml`](https://github.com/aqlaboratory/openfold-3/blob/main/examples/training_yamls/initial_training.yml),
[`finetune_1.yml`](https://github.com/aqlaboratory/openfold-3/blob/main/examples/training_yamls/finetune_1.yml),
[`finetune_2.yml`](https://github.com/aqlaboratory/openfold-3/blob/main/examples/training_yamls/finetune_2.yml)
and
[`finetune_3.yml`](https://github.com/aqlaboratory/openfold-3/blob/main/examples/training_yamls/finetune_3.yml).
Start from the one that matches what you are doing rather than building a
config from scratch.

The sections below cover the parts of that file where you have a decision to
make.

#### Dataset paths

Every path under `dataset_paths` must point at your copy of the data from
Step 1. The two blocks are the training and
validation sets; they differ only in which `dataset_cache_file` and
`template_cache_directory` they use.

#### Logging to Weights & Biases

The config above has `wandb_config: null`, so training metrics go only to the
Slurm output file. To log to Weights & Biases instead, replace the
`logging_config` block with:

``` yaml title="training.yml"
logging_config:
  log_lr: true
  wandb_config:
    project: openfold3-training
    entity: your-wandb-entity
    experiment_name: my-training-run
    group: null
    id: null
```

* `project` — groups related runs together in W&B.
* `entity` — your W&B user or team. **This one you must change**; the run will
    not log anywhere useful until you do.
* `experiment_name` — the name this run appears under. Worth setting to
    something you will recognise weeks later.
* `group` and `id` — optional. `group` collects several runs under one banner,
    `id` resumes logging into an existing run rather than starting a new one.
    Leave both `null` unless you need them.
* `log_lr: true` — also records the learning rate alongside the loss curves,
    which is what you want when chaining resumed jobs.

See [Step 4](#step-4-monitor-the-run) for how the logs get out of the job.

#### Checkpointing and resuming

*Reference: [Checkpointing and Resuming](https://openfold-3.readthedocs.io/en/latest/training.html#checkpointing-and-resuming)*

Checkpoints are written to `{output_dir}/checkpoints/`, controlled by
`checkpoint_config`:

``` yaml title="training.yml"
checkpoint_config:
  every_n_epochs: 1              # save every N epochs
  auto_insert_metric_name: false # don't put the metric in the filename
  save_last: true                # always keep last.ckpt
  save_top_k: -1                 # keep all checkpoints; set to K to keep only the best K
```

`save_top_k: -1` keeps every checkpoint, and each one is over 2 GB. Set a
finite value unless you have the quota for it.

`epoch_len` in `data_module_args` decides how many steps make an "epoch", and
therefore how often `every_n_epochs` actually fires.

Because Mahuika jobs have a wall-time limit, a long training run has to be
chained — submit, let it checkpoint, resume. Setting the restart path to `last`
makes the same script safe to resubmit as many times as it takes:

``` yaml title="training.yml"
experiment_settings:
  restart_checkpoint_path: last                     # resume from last.ckpt
  # restart_checkpoint_path: /path/to/specific.ckpt # or a named checkpoint
```

#### Fine-tuning from a released checkpoint

Fine-tuning uses the same mechanism, pointed at a downloaded checkpoint instead
of one of your own. This is the realistic way to use OpenFold3 training on
Mahuika:

``` yaml title="training.yml"
experiment_settings:
  mode: train
  output_dir: /nesi/nobackup/nesi12345/openfold3/finetune_output
  seed: 42
  restart_checkpoint_path: /nesi/project/nesi12345/user.name/openfold3/of3-p2-155k.pt
```

### Step 3: Launch the training job

*Reference: [Launch Training](https://openfold-3.readthedocs.io/en/latest/training.html#launch-training)*

For a single GPU, which is the right way to debug a config before scaling up:

``` sl
#!/bin/bash -e

#SBATCH --account       nesi12345
#SBATCH --job-name      of3-train
#SBATCH --cpus-per-task 8
#SBATCH --mem           64G
#SBATCH --gpus-per-node A100:1
#SBATCH --time          08:00:00
#SBATCH --output        %j.out

module purge
module load OpenFold3

# Keep Weights & Biases logging on disk; sync it from the login node afterwards
export WANDB_MODE=offline

run_openfold train --runner-yaml /nesi/nobackup/nesi12345/openfold3/training.yml --seed 42
```

For several GPUs on one node, request them in the job and set `devices` to
match. Mahuika GPU nodes carry two A100s each, so change the job header to:

``` sh
#SBATCH --cpus-per-task 16
#SBATCH --mem           128G
#SBATCH --gpus-per-node A100:2
```

and the `runner.yaml` config to:

``` yaml
pl_trainer_args:
  devices: 2       # GPUs per node
  num_nodes: 1
```

For multiple nodes, set `num_nodes` to match and launch one task per GPU with
`srun` so PyTorch Lightning can set up its process group:

``` sl
#!/bin/bash -e

#SBATCH --account           nesi12345
#SBATCH --job-name          of3-train-multinode
#SBATCH --nodes             4
#SBATCH --ntasks-per-node   2
#SBATCH --gpus-per-node     A100:2
#SBATCH --cpus-per-task     8
#SBATCH --mem               128G
#SBATCH --time              24:00:00
#SBATCH --output            %j.out

module purge
module load OpenFold3

export WANDB_MODE=offline

srun run_openfold train --runner-yaml /nesi/nobackup/nesi12345/openfold3/training.yml --seed 42
```

with the matching `runner.yaml` config:

``` yaml
pl_trainer_args:
  devices: 2       # GPUs per node
  num_nodes: 4     # total nodes
  distributed_timeout: PT30M
```

!!! warning "Multi-node jobs need shared storage"

    Every rank must be able to read the dataset and write to `output_dir`.
    Use `/nesi/nobackup` or `/nesi/project`, never `$TMPDIR`, which is
    node-local (and in RAM).

### Step 4: Monitor the run

*Reference: [Monitoring Training](https://openfold-3.readthedocs.io/en/latest/training.html#monitoring-training)*

Training metrics always go to the Slurm output file, so `tail -f` on it is
enough to see a run progressing.

If you enabled Weights & Biases in
[Step 2](#logging-to-weights-biases), there is one more step. The job scripts
in Step 3 set `WANDB_MODE=offline`, so the run writes its metrics to disk under
`{output_dir}/wandb/`. To view the progress through wandb, run the following from
the login node: 

``` bash
wandb sync /nesi/nobackup/nesi12345/openfold3/train_output/wandb/offline-run-*
```

### Step 5: Run inference with your trained checkpoint

*Reference: [Inferencing on fine-tuning checkpoints](https://openfold-3.readthedocs.io/en/latest/training.html#inferencing-on-fine-tuning-checkpoints)*

Training checkpoints are not directly loadable by `run_openfold predict` — they
contain optimiser state and other training data, and attempting to load one
raises:

``` bash
_pickle.UnpicklingError: Weights only load failed.
```

Convert the checkpoint to an inference-ready, EMA-only file first:

``` bash
convert_ckpt_to_ema_only.py train_output/checkpoints/epoch=10-step=5000.ckpt inference.ckpt
```

The result can be passed straight to prediction:

``` bash
run_openfold predict \
    --query-json query.json \
    --use-msa-server=False \
    --output-dir results/ \
    --inference-ckpt-path inference.ckpt
```
